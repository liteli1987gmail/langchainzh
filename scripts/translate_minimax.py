#!/usr/bin/env python3
"""Translate LangChain docs with MiniMax's OpenAI-compatible API.

- code fences are never sent to the model;
- MDX/JSX tags and Markdown structure are preserved in-place;
- only extracted prose text slots are sent to the model;
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
import signal
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from contextlib import contextmanager, nullcontext
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock
from typing import Any


TEXT_EXTENSIONS = {".md", ".mdx", ".txt"}
CACHE_VERSION = 3
JSON_BATCH_MAX_CHARS = 20_000
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
Return only the requested translated content.

Hard rules:
- You will usually receive JSON arrays of short text slots.
- Translate only the text values.
- Preserve ids and JSON shape exactly.
- Preserve Markdown and MDX syntax that appears inside a text value.
- Preserve URLs, anchors, file paths, package names, import/export statements, code identifiers, CLI commands, env var names, and API names.
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


@dataclass(frozen=True)
class TextSlot:
    index: int
    text: str


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
            "Return only the translated result, with no wrapper tags or commentary.\n\n"
            f"{fragment}"
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
                with wall_clock_timeout(self.config.timeout):
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


@contextmanager
def wall_clock_timeout(seconds: int):
    if (
        seconds <= 0
        or threading.current_thread() is not threading.main_thread()
        or not hasattr(signal, "SIGALRM")
    ):
        yield
        return

    previous_handler = signal.getsignal(signal.SIGALRM)

    def handle_timeout(signum, frame):  # type: ignore[no-untyped-def]
        raise TimeoutError(f"MiniMax request exceeded {seconds}s wall-clock timeout")

    signal.signal(signal.SIGALRM, handle_timeout)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous_handler)


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
        return {"version": CACHE_VERSION, "files": {}}
    with path.open("r", encoding="utf-8") as handle:
        cache = json.load(handle)
    cache.setdefault("files", {})
    cache["version"] = CACHE_VERSION
    return cache


def save_cache(path: Path, cache: dict[str, Any]) -> None:
    cache["version"] = CACHE_VERSION
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(cache, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def translation_store_path(cache_path: Path, model: str, source_hash: str) -> Path:
    key = sha256_text(f"{model}\0{source_hash}")
    return cache_path.parent / "translations" / key[:2] / f"{key}.txt"


def cached_translation_text(
    cache_path: Path,
    cache_entry: dict[str, Any] | None,
    *,
    source_hash: str,
    model: str,
) -> str | None:
    if not cache_entry:
        return None
    if cache_entry.get("sha256") != source_hash or cache_entry.get("model") != model:
        return None

    inline_text = cache_entry.get("text")
    if isinstance(inline_text, str):
        return inline_text

    cache_file = cache_entry.get("cache_file")
    if not isinstance(cache_file, str):
        return None
    root = cache_path.parent.resolve()
    text_path = (cache_path.parent / cache_file).resolve()
    if not text_path.is_relative_to(root):
        raise RuntimeError(f"Refusing unsafe translation cache path: {cache_file}")
    if not text_path.exists():
        return None
    return text_path.read_text(encoding="utf-8")


def remember_translation(
    cache_path: Path,
    cache: dict[str, Any],
    rel_path: str,
    *,
    source_hash: str,
    model: str,
    translated_text: str,
) -> None:
    text_path = translation_store_path(cache_path, model, source_hash)
    text_path.parent.mkdir(parents=True, exist_ok=True)
    text_path.write_text(translated_text, encoding="utf-8")
    cache.setdefault("files", {})[rel_path] = {
        "sha256": source_hash,
        "model": model,
        "cache_file": text_path.relative_to(cache_path.parent).as_posix(),
        "translated_at": datetime.now(timezone.utc).isoformat(),
    }


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


def collect_json_strings(
    value: Any,
    *,
    key: str = "",
    path: tuple[str | int, ...] = (),
) -> list[tuple[tuple[str | int, ...], str]]:
    if isinstance(value, dict):
        items: list[tuple[tuple[str | int, ...], str]] = []
        for item_key, item_value in value.items():
            items.extend(
                collect_json_strings(
                    item_value,
                    key=item_key,
                    path=(*path, item_key),
                )
            )
        return items
    if isinstance(value, list):
        items = []
        for index, item in enumerate(value):
            items.extend(collect_json_strings(item, key=key, path=(*path, index)))
        return items
    if isinstance(value, str) and should_translate_json_string(key, value):
        return [(path, value)]
    return []


def set_json_path(root: Any, path: tuple[str | int, ...], value: str) -> None:
    current = root
    for part in path[:-1]:
        current = current[part]
    current[path[-1]] = value


def json_batches(
    items: list[tuple[tuple[str | int, ...], str]],
    max_chars: int,
) -> list[list[tuple[int, tuple[str | int, ...], str]]]:
    batches: list[list[tuple[int, tuple[str | int, ...], str]]] = []
    current: list[tuple[int, tuple[str | int, ...], str]] = []
    current_chars = 0
    for index, (path, text) in enumerate(items):
        entry_chars = len(text) + 80
        if current and current_chars + entry_chars > max_chars:
            batches.append(current)
            current = []
            current_chars = 0
        current.append((index, path, text))
        current_chars += entry_chars
    if current:
        batches.append(current)
    return batches


def parse_json_batch_response(text: str) -> Any:
    stripped = text.strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", stripped, flags=re.DOTALL)
    if fenced:
        stripped = fenced.group(1).strip()
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        start = stripped.find("[")
        end = stripped.rfind("]")
        if start == -1 or end == -1 or end <= start:
            raise
        return json.loads(stripped[start : end + 1])


def translate_json_batch(
    batch: list[tuple[int, tuple[str | int, ...], str]],
    client: MiniMaxClient,
) -> dict[int, str]:
    if client.config.mock:
        return {item_id: text for item_id, _, text in batch}

    payload = [{"id": item_id, "text": text} for item_id, _, text in batch]
    fragment = (
        "Translate only the text values to Simplified Chinese. "
        "Return valid JSON only: an array with the same id values and translated text values. "
        "Do not translate keys or id values.\n\n"
        + json.dumps(payload, ensure_ascii=False, indent=2)
    )
    response = client.translate(fragment, content_type="JSON string batch")
    parsed = parse_json_batch_response(response)

    if isinstance(parsed, list) and all(isinstance(item, str) for item in parsed):
        if len(parsed) != len(batch):
            raise RuntimeError("MiniMax JSON batch returned a string list with the wrong length")
        return {
            item_id: translated
            for (item_id, _, _), translated in zip(batch, parsed, strict=True)
        }

    if not isinstance(parsed, list):
        raise RuntimeError("MiniMax JSON batch did not return a JSON array")

    translations: dict[int, str] = {}
    for item in parsed:
        if not isinstance(item, dict) or "id" not in item or "text" not in item:
            raise RuntimeError("MiniMax JSON batch returned an unexpected item shape")
        translations[int(item["id"])] = str(item["text"])

    expected_ids = {item_id for item_id, _, _ in batch}
    if set(translations) != expected_ids:
        raise RuntimeError("MiniMax JSON batch returned mismatched ids")
    return translations


def translate_json_values_batched(
    parsed: Any,
    client: MiniMaxClient,
    max_chars: int,
) -> Any:
    items = collect_json_strings(parsed)
    batch_limit = min(max_chars, JSON_BATCH_MAX_CHARS)
    batches = json_batches(items, batch_limit)
    print(
        f"translate-json: strings={len(items)} batches={len(batches)}",
        file=sys.stderr,
    )
    for batch in batches:
        translations = translate_json_batch(batch, client)
        for item_id, path, _ in batch:
            set_json_path(parsed, path, translations[item_id])
    return parsed


def translate_json_document(text: str, client: MiniMaxClient, max_chars: int) -> str:
    if len(text) <= max_chars:
        translated = client.translate(text, content_type="JSON document")
        json.loads(translated)
        return translated.rstrip() + "\n"

    parsed = json.loads(text)
    translated = translate_json_values_batched(parsed, client, max_chars)
    return json.dumps(translated, ensure_ascii=False, indent=2) + "\n"


def split_edge_whitespace(text: str) -> tuple[str, str, str]:
    leading_len = len(text) - len(text.lstrip())
    trailing_len = len(text) - len(text.rstrip())
    if leading_len == len(text):
        return text, "", ""
    leading = text[:leading_len]
    core_end = len(text) - trailing_len if trailing_len else len(text)
    return leading, text[leading_len:core_end], text[core_end:]


def should_translate_text_slot(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if not has_translatable_english(stripped):
        return False
    if stripped.startswith(("/", "http://", "https://", "#", "{", "$")):
        return False
    if "/" in stripped or "\\" in stripped:
        return False
    if re.fullmatch(r"[A-Za-z0-9_.:-]+", stripped) and any(
        marker in stripped for marker in ("_", ".", ":", "-")
    ):
        return False
    if re.fullmatch(r"[A-Z0-9_./:@#?=&%+${}\[\]<>-]+", stripped):
        return False
    return True


def find_matching_paren(text: str, open_index: int) -> int:
    depth = 0
    for index in range(open_index, len(text)):
        char = text[index]
        if char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
            if depth == 0:
                return index
    return -1


def find_matching_brace(text: str, open_index: int) -> int:
    depth = 0
    quote = ""
    escaped = False
    for index in range(open_index, len(text)):
        char = text[index]
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = ""
            continue
        if char in {"'", '"', "`"}:
            quote = char
        elif char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return index
    return -1


def looks_like_html_or_mdx_tag(text: str, index: int) -> bool:
    if text[index] != "<" or index + 1 >= len(text):
        return False
    next_char = text[index + 1]
    return next_char.isalpha() or next_char in {"/", "!", "?"}


def append_text_part(parts: list[str | TextSlot], raw: str, slots: list[str]) -> None:
    if not raw:
        return
    leading, core, trailing = split_edge_whitespace(raw)
    if not should_translate_text_slot(core):
        parts.append(raw)
        return
    if leading:
        parts.append(leading)
    slot = TextSlot(len(slots), core)
    slots.append(core)
    parts.append(slot)
    if trailing:
        parts.append(trailing)


def extract_inline_text_slots(text: str, slots: list[str]) -> list[str | TextSlot]:
    parts: list[str | TextSlot] = []
    buffer: list[str] = []
    index = 0

    def flush_buffer() -> None:
        nonlocal buffer
        if buffer:
            append_text_part(parts, "".join(buffer), slots)
            buffer = []

    while index < len(text):
        if text.startswith("![", index) or text.startswith("[", index):
            is_image = text.startswith("![", index)
            label_start = index + (2 if is_image else 1)
            label_end = text.find("]", label_start)
            if label_end != -1 and label_end + 1 < len(text) and text[label_end + 1] == "(":
                target_end = find_matching_paren(text, label_end + 1)
                if target_end != -1:
                    flush_buffer()
                    parts.append("![" if is_image else "[")
                    label = text[label_start:label_end]
                    parts.extend(extract_inline_text_slots(label, slots))
                    parts.append(text[label_end:target_end + 1])
                    index = target_end + 1
                    continue

        char = text[index]
        if char == "`":
            fence_len = 1
            while index + fence_len < len(text) and text[index + fence_len] == "`":
                fence_len += 1
            close_index = text.find("`" * fence_len, index + fence_len)
            if close_index != -1:
                flush_buffer()
                parts.append(text[index:close_index + fence_len])
                index = close_index + fence_len
                continue

        if char == "<" and looks_like_html_or_mdx_tag(text, index):
            close_index = text.find(">", index + 1)
            if close_index != -1:
                flush_buffer()
                parts.append(text[index:close_index + 1])
                index = close_index + 1
                continue

        if char == "{":
            close_index = find_matching_brace(text, index)
            if close_index != -1:
                flush_buffer()
                parts.append(text[index:close_index + 1])
                index = close_index + 1
                continue

        if char in {"*", "_"}:
            marker_len = 1
            while (
                index + marker_len < len(text)
                and text[index + marker_len] == char
                and marker_len < 3
            ):
                marker_len += 1
            flush_buffer()
            parts.append(text[index:index + marker_len])
            index += marker_len
            continue

        buffer.append(char)
        index += 1

    flush_buffer()
    return parts


def extract_markdown_line_slots(line: str, slots: list[str]) -> list[str | TextSlot]:
    prefix_match = re.match(
        r"^(\s*(?:(?:#{1,6}|[-*+]|\d+\.|>)\s+))(.+)$",
        line,
    )
    if not prefix_match:
        return extract_inline_text_slots(line, slots)
    return [
        prefix_match.group(1),
        *extract_inline_text_slots(prefix_match.group(2), slots),
    ]


def render_parts(parts: list[str | TextSlot], translated_slots: dict[int, str]) -> str:
    rendered: list[str] = []
    for part in parts:
        if isinstance(part, str):
            rendered.append(part)
        else:
            rendered.append(translated_slots.get(part.index, part.text))
    return "".join(rendered)


def translate_text_slots(
    slots: list[str],
    client: MiniMaxClient,
    max_chars: int,
) -> dict[int, str]:
    if not slots:
        return {}
    batch_items = [((index,), text) for index, text in enumerate(slots)]
    translated: dict[int, str] = {}
    for batch in json_batches(batch_items, min(max_chars, JSON_BATCH_MAX_CHARS)):
        translated.update(translate_json_batch(batch, client))
    suspicious = [
        (index, value)
        for index, value in translated.items()
        if re.search(r"</?[A-Za-z][A-Za-z0-9_.:-]*(?:\s[^>]*)?>", value)
        or "<fragment" in value
        or "</fragment" in value
    ]
    if suspicious:
        sample = "; ".join(f"{index}: {value[:80]}" for index, value in suspicious[:5])
        raise RuntimeError(f"Translated text slot contains MDX/HTML tags: {sample}")
    return translated


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


def should_preserve_line(line: str) -> bool:
    stripped = line.lstrip()
    return (
        bool(re.match(r"^\s*(import|export)\b", line))
        or "data:image/" in line
        or "base64," in line
        or stripped.startswith("<img ")
    )


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
        if should_preserve_line(line):
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
        if len(part) > max_chars:
            if current:
                chunks.append(current)
                current = ""
            for start in range(0, len(part), max_chars):
                chunks.append(part[start : start + max_chars])
            continue
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


def restore_edge_newlines(source: str, translated: str) -> str:
    leading = len(source) - len(source.lstrip("\n"))
    trailing = len(source) - len(source.rstrip("\n"))
    return ("\n" * leading) + translated.strip("\n") + ("\n" * trailing)


def translate_markdown(text: str, client: MiniMaxClient, max_chars: int) -> str:
    document_parts: list[str | TextSlot] = []
    slots: list[str] = []
    in_frontmatter = False
    frontmatter_opening = text.startswith("---\n")

    def append_literal(value: str) -> None:
        if value:
            document_parts.append(value)

    def append_translatable(value: str) -> None:
        document_parts.extend(extract_inline_text_slots(value, slots))

    for unit_type, unit_text in split_fenced_blocks(text):
        if unit_type == "literal":
            append_literal(unit_text)
            continue

        for nested_type, nested_text in split_preserved_lines(unit_text):
            if nested_type == "literal" or not has_translatable_english(nested_text):
                append_literal(nested_text)
                continue

            for line in nested_text.splitlines(keepends=True):
                newline = ""
                body = line
                if body.endswith("\r\n"):
                    body = body[:-2]
                    newline = "\r\n"
                elif body.endswith("\n"):
                    body = body[:-1]
                    newline = "\n"

                if frontmatter_opening and body.strip() == "---":
                    append_literal(body + newline)
                    in_frontmatter = True
                    frontmatter_opening = False
                    continue

                if in_frontmatter and body.strip() == "---":
                    append_literal(body + newline)
                    in_frontmatter = False
                    continue

                if in_frontmatter:
                    match = re.match(r"^(\s*[A-Za-z0-9_-]+\s*:\s*)(.*)$", body)
                    if match and should_translate_text_slot(match.group(2)):
                        append_literal(match.group(1))
                        append_translatable(match.group(2))
                        append_literal(newline)
                    else:
                        append_literal(body + newline)
                    continue

                document_parts.extend(extract_markdown_line_slots(body, slots))
                append_literal(newline)

    print(f"translate-slots: count={len(slots)}", file=sys.stderr)
    translated_slots = translate_text_slots(slots, client, max_chars)
    return render_parts(document_parts, translated_slots).rstrip() + "\n"


def translate_file(
    source_path: Path,
    target_path: Path,
    rel_path: str,
    client: MiniMaxClient,
    cache: dict[str, Any],
    cache_path: Path,
    *,
    force: bool,
    verbose_cache: bool,
    cache_lock: Any | None = None,
) -> tuple[str, bool]:
    source_text = source_path.read_text(encoding="utf-8")
    source_hash = sha256_text(source_text)
    with cache_lock or nullcontext():
        cache_entry = cache.setdefault("files", {}).get(rel_path)
    if not force:
        cached_text = cached_translation_text(
            cache_path,
            cache_entry,
            source_hash=source_hash,
            model=client.config.model,
        )
        if cached_text is not None:
            if verbose_cache:
                print(f"cache: {rel_path}", file=sys.stderr)
            target_path.parent.mkdir(parents=True, exist_ok=True)
            target_path.write_text(cached_text, encoding="utf-8")
            return "cached", False

        if (
            target_path.exists()
            and cache_entry
            and cache_entry.get("sha256") == source_hash
            and cache_entry.get("model") == client.config.model
        ):
            if verbose_cache:
                print(f"backfill-cache: {rel_path}", file=sys.stderr)
            translated = target_path.read_text(encoding="utf-8")
            with cache_lock or nullcontext():
                remember_translation(
                    cache_path,
                    cache,
                    rel_path,
                    source_hash=source_hash,
                    model=client.config.model,
                    translated_text=translated,
                )
            return "cached", True

    if source_path.suffix.lower() in TEXT_EXTENSIONS:
        print(f"translate: {rel_path}", file=sys.stderr)
        translated = translate_markdown(source_text, client, client.config.max_chars)
    elif source_path.name == "docs.json":
        print(f"translate: {rel_path}", file=sys.stderr)
        translated = translate_json_document(
            source_text, client, client.config.max_chars * 3
        )
    else:
        shutil.copy2(source_path, target_path)
        return "copied", False

    target_path.parent.mkdir(parents=True, exist_ok=True)
    target_path.write_text(translated, encoding="utf-8")
    with cache_lock or nullcontext():
        remember_translation(
            cache_path,
            cache,
            rel_path,
            source_hash=source_hash,
            model=client.config.model,
            translated_text=translated,
        )
    return "translated", True


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
    parser.add_argument(
        "--save-every",
        type=int,
        default=20,
        help="Persist the translation cache after this many cache updates.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=int(os.environ.get("TRANSLATION_WORKERS", "1")),
        help="Number of files to translate concurrently.",
    )
    parser.add_argument(
        "--keep-going",
        action="store_true",
        help="Record file-level translation failures and continue other files.",
    )
    parser.add_argument(
        "--failure-log",
        type=Path,
        help="Write keep-going failures to this JSON file.",
    )
    parser.add_argument(
        "--verbose-cache",
        action="store_true",
        help="Print one line for every cached translation restored.",
    )
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
    cached_count = 0
    copied_count = 0
    seen_translatable = 0
    dirty_cache_updates = 0
    failures: list[dict[str, str]] = []
    cache_lock = Lock()
    workers = max(1, args.workers)

    def record_result(action: str, cache_changed: bool) -> None:
        nonlocal translated_count, cached_count, dirty_cache_updates
        if action == "translated":
            translated_count += 1
        elif action == "cached":
            cached_count += 1
        if cache_changed:
            dirty_cache_updates += 1
            if args.save_every > 0 and dirty_cache_updates >= args.save_every:
                with cache_lock:
                    save_cache(args.cache, cache)
                dirty_cache_updates = 0

    def process_translation(
        source_path: Path,
        target_path: Path,
        rel_path: str,
    ) -> tuple[str, bool]:
        worker_client = client if workers == 1 else MiniMaxClient(config)
        return translate_file(
            source_path,
            target_path,
            rel_path,
            worker_client,
            cache,
            args.cache,
            force=args.force,
            verbose_cache=args.verbose_cache,
            cache_lock=cache_lock,
        )

    def record_failure(rel_path: str, exc: Exception) -> None:
        message = str(exc)
        failures.append({"path": rel_path, "error": message})
        print(f"failed: {rel_path}: {message}", file=sys.stderr)

    executor: ThreadPoolExecutor | None = None
    futures = {}
    try:
        if workers > 1 and not args.dry_run:
            executor = ThreadPoolExecutor(max_workers=workers)

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
                if executor:
                    future = executor.submit(
                        process_translation,
                        source_path,
                        target_path,
                        rel_path,
                    )
                    futures[future] = rel_path
                else:
                    try:
                        action, cache_changed = process_translation(
                            source_path,
                            target_path,
                            rel_path,
                        )
                        record_result(action, cache_changed)
                    except Exception as exc:
                        if not args.keep_going:
                            raise
                        record_failure(rel_path, exc)
            else:
                copy_asset(source_path, target_path)
                copied_count += 1

        for future in as_completed(futures):
            rel_path = futures[future]
            try:
                action, cache_changed = future.result()
                record_result(action, cache_changed)
            except Exception as exc:
                if not args.keep_going:
                    raise
                record_failure(rel_path, exc)
    finally:
        if executor:
            executor.shutdown(cancel_futures=True)
        if not args.dry_run:
            with cache_lock:
                save_cache(args.cache, cache)
        if args.failure_log is not None:
            args.failure_log.parent.mkdir(parents=True, exist_ok=True)
            args.failure_log.write_text(
                json.dumps(failures, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

    print(
        f"done: translated={translated_count} cached={cached_count} copied_assets={copied_count} failed={len(failures)}",
        file=sys.stderr,
    )
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
