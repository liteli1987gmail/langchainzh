#!/usr/bin/env python3
"""Translate LangChain docs with MiniMax's OpenAI-compatible API.

The translator is intentionally conservative:
- code fences are never sent to the model;
- imports/exports are preserved;
- unchanged files are skipped through a sha256 cache;
- source and destination directories stay separate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TEXT_EXTENSIONS = {".md", ".mdx", ".txt"}
JSON_DISPLAY_KEYS = {
    "anchor",
    "description",
    "group",
    "label",
    "name",
    "placeholder",
    "tab",
    "title",
}
JSON_SKIP_KEYS = {
    "api",
    "background",
    "color",
    "colors",
    "dark",
    "default",
    "favicon",
    "font",
    "href",
    "icon",
    "id",
    "light",
    "logo",
    "openapi",
    "page",
    "pages",
    "path",
    "src",
    "url",
    "version",
}


SYSTEM_PROMPT = """You are a senior technical translator.
Translate English developer documentation into Simplified Chinese.
Return only the translated content.

Hard rules:
- Preserve Markdown and MDX structure.
- Preserve JSX/Mintlify component names and attribute names.
- Preserve URLs, anchors, file paths, package names, import/export statements, code identifiers, CLI commands, env var names, and API names.
- Keep fenced code blocks unchanged. They are normally removed before you see a fragment.
- Keep frontmatter keys unchanged, but translate human-readable values.
- Do not include reasoning, analysis, or <think> blocks.
- Do not add explanations, summaries, or wrappers.
"""


@dataclass(frozen=True)
class TranslationConfig:
    api_key: str
    base_url: str
    model: str
    temperature: float
    timeout: int
    max_chars: int
    retries: int
    retry_delay: float
    mock: bool


class MiniMaxClient:
    def __init__(self, config: TranslationConfig) -> None:
        self.config = config
        self.endpoint = resolve_endpoint(config.base_url)
        self.opener = (
            urllib.request.build_opener()
            if os.environ.get("MINIMAX_USE_PROXY", "").lower() in {"1", "true", "yes"}
            else urllib.request.build_opener(urllib.request.ProxyHandler({}))
        )

    def translate(self, fragment: str, *, content_type: str) -> str:
        if self.config.mock:
            return fragment

        prompt = (
            f"Translate this {content_type} fragment into Simplified Chinese. "
            "Keep formatting and non-prose tokens unchanged.\n\n"
            "<fragment>\n"
            f"{fragment}"
            "\n</fragment>"
        )
        payload = {
            "model": self.config.model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            "temperature": self.config.temperature,
        }
        data = json.dumps(payload).encode("utf-8")
        headers = {
            "Authorization": f"Bearer {self.config.api_key}",
            "Content-Type": "application/json",
        }

        last_error: Exception | None = None
        for attempt in range(self.config.retries + 1):
            request = urllib.request.Request(
                self.endpoint,
                data=data,
                headers=headers,
                method="POST",
            )
            try:
                with self.opener.open(request, timeout=self.config.timeout) as response:
                    body = response.read().decode("utf-8")
                parsed = json.loads(body)
                return strip_thinking(
                    parsed["choices"][0]["message"]["content"].strip()
                )
            except (KeyError, json.JSONDecodeError) as exc:
                raise RuntimeError(f"Unexpected MiniMax response shape: {exc}") from exc
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as exc:
                last_error = exc
                if attempt >= self.config.retries:
                    break
                sleep_for = self.config.retry_delay * (2**attempt)
                print(
                    f"MiniMax request failed ({exc}); retrying in {sleep_for:.1f}s",
                    file=sys.stderr,
                )
                time.sleep(sleep_for)

        raise RuntimeError(f"MiniMax request failed after retries: {last_error}")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def strip_thinking(text: str) -> str:
    stripped = text.lstrip()
    if not stripped.startswith("<think>"):
        return text.strip()

    close_tag = "</think>"
    close_index = stripped.find(close_tag)
    if close_index == -1:
        raise RuntimeError("MiniMax response contained an unterminated <think> block")

    return stripped[close_index + len(close_tag) :].strip()


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


def load_env_files() -> None:
    load_dotenv(Path(".env"))
    load_dotenv(Path.home() / ".serenity_env")


def resolve_endpoint(base_url: str) -> str:
    value = base_url.rstrip("/")
    if value.endswith("/chat/completions"):
        return value
    return value + "/chat/completions"


def default_base_url() -> str:
    if os.environ.get("MINIMAX_BASE_URL"):
        return os.environ["MINIMAX_BASE_URL"]
    if os.environ.get("MINIMAX_URL"):
        endpoint = os.environ["MINIMAX_URL"].rstrip("/")
        suffix = "/chat/completions"
        return endpoint[: -len(suffix)] if endpoint.endswith(suffix) else endpoint
    return "https://api.minimaxi.com/v1"


def load_cache(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"version": 1, "files": {}}
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def save_cache(path: Path, cache: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(cache, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def iter_source_files(source_dir: Path) -> list[Path]:
    return sorted(path for path in source_dir.rglob("*") if path.is_file())


def is_probably_path(value: str) -> bool:
    stripped = value.strip()
    if not stripped:
        return True
    if stripped.startswith(("/", "http://", "https://", "#", "{", "$")):
        return True
    if re.fullmatch(r"[A-Za-z0-9_./:@#?=&%+-]+", stripped) and "/" in stripped:
        return True
    if re.fullmatch(r"[A-Za-z0-9_.:-]+", stripped):
        return True
    return False


def should_translate_json_string(key: str, value: str) -> bool:
    lowered = key.lower()
    if lowered in JSON_SKIP_KEYS:
        return False
    if lowered in JSON_DISPLAY_KEYS:
        return bool(value.strip()) and not is_probably_path(value)
    return bool(re.search(r"[A-Za-z]", value)) and not is_probably_path(value)


def translate_json_value(value: Any, client: MiniMaxClient, key: str = "") -> Any:
    if isinstance(value, dict):
        return {
            item_key: translate_json_value(item_value, client, item_key)
            for item_key, item_value in value.items()
        }
    if isinstance(value, list):
        return [translate_json_value(item, client, key) for item in value]
    if isinstance(value, str) and should_translate_json_string(key, value):
        return client.translate(value, content_type="JSON string")
    return value


def translate_json_document(text: str, client: MiniMaxClient, max_chars: int) -> str:
    if len(text) <= max_chars:
        translated = client.translate(text, content_type="JSON document")
        json.loads(translated)
        return translated.rstrip() + "\n"

    parsed = json.loads(text)
    translated = translate_json_value(parsed, client)
    return json.dumps(translated, ensure_ascii=False, indent=2) + "\n"


def split_fenced_blocks(text: str) -> list[tuple[str, str]]:
    units: list[tuple[str, str]] = []
    buffer: list[str] = []
    fence: list[str] = []
    in_fence = False
    fence_marker = ""

    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        marker = stripped[:3]
        starts_fence = marker in {"```", "~~~"}

        if in_fence:
            fence.append(line)
            if stripped.startswith(fence_marker):
                units.append(("literal", "".join(fence)))
                fence = []
                in_fence = False
            continue

        if starts_fence:
            if buffer:
                units.append(("text", "".join(buffer)))
                buffer = []
            fence_marker = marker
            fence = [line]
            in_fence = True
        else:
            buffer.append(line)

    if fence:
        units.append(("literal", "".join(fence)))
    if buffer:
        units.append(("text", "".join(buffer)))
    return units


def split_preserved_lines(text: str) -> list[tuple[str, str]]:
    units: list[tuple[str, str]] = []
    buffer: list[str] = []
    preserved: list[str] = []

    def flush_buffer() -> None:
        nonlocal buffer
        if buffer:
            units.append(("text", "".join(buffer)))
            buffer = []

    def flush_preserved() -> None:
        nonlocal preserved
        if preserved:
            units.append(("literal", "".join(preserved)))
            preserved = []

    for line in text.splitlines(keepends=True):
        if re.match(r"^\s*(import|export)\b", line):
            flush_buffer()
            preserved.append(line)
        else:
            flush_preserved()
            buffer.append(line)

    flush_buffer()
    flush_preserved()
    return units


def chunk_text(text: str, max_chars: int) -> list[str]:
    if len(text) <= max_chars:
        return [text]

    chunks: list[str] = []
    current = ""
    for part in re.split(r"(\n{2,})", text):
        if len(current) + len(part) > max_chars and current:
            chunks.append(current)
            current = part
        else:
            current += part
    if current:
        chunks.append(current)
    return chunks


def has_translatable_english(text: str) -> bool:
    return bool(re.search(r"[A-Za-z]{3,}", text))


def translate_markdown(text: str, client: MiniMaxClient, max_chars: int) -> str:
    translated_units: list[str] = []
    for unit_type, unit_text in split_fenced_blocks(text):
        if unit_type == "literal":
            translated_units.append(unit_text)
            continue

        for nested_type, nested_text in split_preserved_lines(unit_text):
            if nested_type == "literal" or not has_translatable_english(nested_text):
                translated_units.append(nested_text)
                continue
            translated_units.extend(
                client.translate(chunk, content_type="Markdown/MDX")
                for chunk in chunk_text(nested_text, max_chars)
            )
    return "".join(translated_units).rstrip() + "\n"


def translate_file(
    source_path: Path,
    target_path: Path,
    rel_path: str,
    client: MiniMaxClient,
    cache: dict[str, Any],
    *,
    force: bool,
) -> bool:
    source_text = source_path.read_text(encoding="utf-8")
    source_hash = sha256_text(source_text)
    cache_entry = cache.setdefault("files", {}).get(rel_path)
    if (
        not force
        and target_path.exists()
        and cache_entry
        and cache_entry.get("sha256") == source_hash
        and cache_entry.get("model") == client.config.model
    ):
        return False

    if source_path.suffix.lower() in TEXT_EXTENSIONS:
        translated = translate_markdown(source_text, client, client.config.max_chars)
    elif source_path.name == "docs.json":
        translated = translate_json_document(
            source_text, client, client.config.max_chars * 3
        )
    else:
        shutil.copy2(source_path, target_path)
        return False

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(translated, encoding="utf-8")
    cache["files"][rel_path] = {
        "sha256": source_hash,
        "model": client.config.model,
        "translated_at": datetime.now(timezone.utc).isoformat(),
    }
    return True


def copy_asset(source_path: Path, target_path: Path) -> None:
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, target_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--target-dir", type=Path, required=True)
    parser.add_argument(
        "--cache",
        type=Path,
        default=Path(".translation-cache/minimax.json"),
    )
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--mock",
        action="store_true",
        default=os.environ.get("TRANSLATION_MOCK", "").lower()
        in {"1", "true", "yes"},
        help="Do not call MiniMax; copy translatable text unchanged for smoke tests.",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("MINIMAX_MODEL", "MiniMax-M2.7-highspeed"),
    )
    parser.add_argument(
        "--base-url",
        default=default_base_url(),
    )
    parser.add_argument("--temperature", type=float, default=0.1)
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--max-chars", type=int, default=24000)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--retry-delay", type=float, default=3.0)
    return parser.parse_args()


def main() -> int:
    load_env_files()
    args = parse_args()
    api_key = os.environ.get("MINIMAX_API_KEY")
    if not api_key and not args.dry_run and not args.mock:
        print("MINIMAX_API_KEY is required.", file=sys.stderr)
        return 2

    if not args.source_dir.exists():
        print(f"Source directory does not exist: {args.source_dir}", file=sys.stderr)
        return 2

    config = TranslationConfig(
        api_key=api_key or "dry-run",
        base_url=args.base_url,
        model=args.model,
        temperature=args.temperature,
        timeout=args.timeout,
        max_chars=args.max_chars,
        retries=args.retries,
        retry_delay=args.retry_delay,
        mock=args.mock,
    )
    client = MiniMaxClient(config)
    cache = load_cache(args.cache)
    files = iter_source_files(args.source_dir)
    translated_count = 0
    copied_count = 0
    seen_translatable = 0

    for source_path in files:
        rel_path = source_path.relative_to(args.source_dir).as_posix()
        target_path = args.target_dir / rel_path
        suffix = source_path.suffix.lower()
        is_translatable = suffix in TEXT_EXTENSIONS or source_path.name == "docs.json"

        if args.limit and is_translatable:
            seen_translatable += 1
            if seen_translatable > args.limit:
                if not args.dry_run:
                    copy_asset(source_path, target_path)
                    copied_count += 1
                continue

        if args.dry_run:
            action = "translate" if is_translatable else "copy"
            print(f"{action}: {rel_path}")
            continue

        if is_translatable:
            print(f"translate: {rel_path}", file=sys.stderr)
            changed = translate_file(
                source_path,
                target_path,
                rel_path,
                client,
                cache,
                force=args.force,
            )
            if changed:
                translated_count += 1
        else:
            copy_asset(source_path, target_path)
            copied_count += 1

    if not args.dry_run:
        save_cache(args.cache, cache)

    print(
        f"done: translated={translated_count} copied_assets={copied_count}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
