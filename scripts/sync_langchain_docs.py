#!/usr/bin/env python3
"""Sync, translate, build, and export the current LangChain docs."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tarfile
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


UPSTREAM_URL = "https://github.com/langchain-ai/docs.git"
TARBALL_URL = "https://github.com/langchain-ai/docs/archive/refs/heads/{ref}.tar.gz"


def run(
    command: list[str],
    *,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
) -> None:
    printable = " ".join(command)
    print(f"+ {printable}", file=sys.stderr)
    subprocess.run(command, cwd=cwd, env=env, check=True)


def capture(command: list[str], *, cwd: Path | None = None) -> str:
    return subprocess.check_output(command, cwd=cwd, text=True).strip()


def load_dotenv(path: Path = Path(".env")) -> None:
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


def upstream_sha(ref: str, upstream_url: str) -> str:
    output = capture(["git", "ls-remote", upstream_url, ref])
    if not output:
        raise RuntimeError(f"Could not resolve upstream ref {ref}")
    return output.split()[0]


def clone_or_download(upstream_dir: Path, ref: str, upstream_url: str) -> None:
    if upstream_dir.exists():
        shutil.rmtree(upstream_dir)
    upstream_dir.parent.mkdir(parents=True, exist_ok=True)

    try:
        run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                "--branch",
                ref,
                upstream_url,
                str(upstream_dir),
            ]
        )
        return
    except subprocess.CalledProcessError:
        print("git clone failed; falling back to GitHub tarball", file=sys.stderr)

    archive_path = upstream_dir.parent / "langchain-docs.tar.gz"
    url = TARBALL_URL.format(ref=ref)
    urllib.request.urlretrieve(url, archive_path)
    extract_dir = upstream_dir.parent / "tarball"
    if extract_dir.exists():
        shutil.rmtree(extract_dir)
    extract_dir.mkdir(parents=True)
    with tarfile.open(archive_path, "r:gz") as archive:
        archive.extractall(extract_dir)
    roots = [path for path in extract_dir.iterdir() if path.is_dir()]
    if len(roots) != 1:
        raise RuntimeError("Unexpected tarball layout")
    roots[0].rename(upstream_dir)


def copy_translated_src(upstream_dir: Path, translated_src: Path) -> None:
    original_src = upstream_dir / "src"
    backup_src = upstream_dir / "src.original"
    if backup_src.exists():
        shutil.rmtree(backup_src)
    original_src.rename(backup_src)
    shutil.copytree(translated_src, original_src)


def build_official_docs(upstream_dir: Path) -> None:
    run(["uv", "sync", "--all-groups"], cwd=upstream_dir)
    run(["npm", "install"], cwd=upstream_dir)
    env = os.environ.copy()
    env["PYTHONPATH"] = str(upstream_dir)
    run(["uv", "run", "pipeline", "build"], cwd=upstream_dir, env=env)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream-url", default=UPSTREAM_URL)
    parser.add_argument("--ref", default="main")
    parser.add_argument("--work-dir", type=Path, default=Path(".langchain-work"))
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument("--cache", type=Path, default=Path(".translation-cache/minimax.json"))
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--skip-if-unchanged", action="store_true")
    parser.add_argument("--skip-build", action="store_true")
    parser.add_argument(
        "--mock-translator",
        action="store_true",
        help="Do not call MiniMax; use unchanged source text for smoke tests.",
    )
    return parser.parse_args()


def main() -> int:
    load_dotenv()
    args = parse_args()
    sha = upstream_sha(args.ref, args.upstream_url)
    state_path = Path(".langchain-docs-upstream.json")
    if args.skip_if_unchanged and state_path.exists() and not args.force:
        state = json.loads(state_path.read_text(encoding="utf-8"))
        if state.get("upstream_sha") == sha:
            print(f"upstream unchanged at {sha}", file=sys.stderr)
            return 0

    if not os.environ.get("MINIMAX_API_KEY") and not args.mock_translator:
        print("MINIMAX_API_KEY is required for translation.", file=sys.stderr)
        return 2

    upstream_dir = args.work_dir / "upstream"
    translated_src = args.work_dir / "src.zh"
    clone_or_download(upstream_dir, args.ref, args.upstream_url)
    if translated_src.exists():
        shutil.rmtree(translated_src)

    translate_command = [
        sys.executable,
        "scripts/translate_minimax.py",
        "--source-dir",
        str(upstream_dir / "src"),
        "--target-dir",
        str(translated_src),
        "--cache",
        str(args.cache),
    ]
    if args.limit:
        translate_command.extend(["--limit", str(args.limit)])
    if args.force:
        translate_command.append("--force")
    if args.mock_translator:
        translate_command.append("--mock")
    run(translate_command)

    copy_translated_src(upstream_dir, translated_src)
    if not args.skip_build:
        build_official_docs(upstream_dir)
        run(
            [
                sys.executable,
                "scripts/export_static_site.py",
                "--build-dir",
                str(upstream_dir / "build"),
                "--out-dir",
                str(args.site_dir),
            ]
        )

    state = {
        "upstream_url": args.upstream_url,
        "upstream_ref": args.ref,
        "upstream_sha": sha,
        "synced_at": datetime.now(timezone.utc).isoformat(),
        "translator": {
            "provider": "MiniMax",
            "model": os.environ.get("MINIMAX_MODEL", "MiniMax-M2.7-highspeed"),
            "base_url": os.environ.get("MINIMAX_BASE_URL", "https://api.minimax.io/v1"),
        },
        "output": {
            "site_dir": str(args.site_dir),
            "cache": str(args.cache),
        },
    }
    state_path.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"synced upstream {sha}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
