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
DOWNLOAD_CHUNK_BYTES = 1024 * 1024
DOWNLOAD_LOG_BYTES = 25 * 1024 * 1024
DOWNLOAD_READ_TIMEOUT_SECONDS = 60


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


def upstream_sha(ref: str, upstream_url: str) -> str:
    output = capture(["git", "ls-remote", upstream_url, ref])
    if not output:
        raise RuntimeError(f"Could not resolve upstream ref {ref}")
    return output.split()[0]


def is_default_github_upstream(upstream_url: str) -> bool:
    normalized = upstream_url.rstrip("/")
    return normalized in {
        "https://github.com/langchain-ai/docs.git",
        "https://github.com/langchain-ai/docs",
    }


def clone_upstream(upstream_dir: Path, ref: str, upstream_url: str) -> None:
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


def safe_extract_tarball(archive_path: Path, extract_dir: Path) -> None:
    with tarfile.open(archive_path, "r:gz") as archive:
        extract_root = extract_dir.resolve()
        for member in archive.getmembers():
            target = (extract_dir / member.name).resolve()
            if not str(target).startswith(str(extract_root)):
                raise RuntimeError(f"Refusing unsafe tarball path: {member.name}")
        archive.extractall(extract_dir)


def download_tarball(upstream_dir: Path, ref: str) -> None:
    archive_path = upstream_dir.parent / "langchain-docs.tar.gz"
    url = TARBALL_URL.format(ref=ref)
    request = urllib.request.Request(url, method="GET")
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    print(f"Downloading upstream docs tarball: {url}", file=sys.stderr)
    with opener.open(request, timeout=DOWNLOAD_READ_TIMEOUT_SECONDS) as response:
        expected_size = response.headers.get("Content-Length")
        expected = int(expected_size) if expected_size and expected_size.isdigit() else None
        downloaded = 0
        next_log = DOWNLOAD_LOG_BYTES
        with archive_path.open("wb") as archive_file:
            while True:
                chunk = response.read(DOWNLOAD_CHUNK_BYTES)
                if not chunk:
                    break
                archive_file.write(chunk)
                downloaded += len(chunk)
                if downloaded >= next_log:
                    if expected:
                        print(
                            f"Downloaded {downloaded // (1024 * 1024)} MiB"
                            f" / {expected // (1024 * 1024)} MiB",
                            file=sys.stderr,
                        )
                    else:
                        print(
                            f"Downloaded {downloaded // (1024 * 1024)} MiB",
                            file=sys.stderr,
                        )
                    next_log += DOWNLOAD_LOG_BYTES

    if archive_path.stat().st_size == 0:
        raise RuntimeError("Downloaded empty upstream tarball")
    print(
        f"Downloaded upstream docs tarball: {archive_path.stat().st_size // (1024 * 1024)} MiB",
        file=sys.stderr,
    )

    extract_dir = upstream_dir.parent / "tarball"
    if extract_dir.exists():
        shutil.rmtree(extract_dir)
    extract_dir.mkdir(parents=True)
    safe_extract_tarball(archive_path, extract_dir)
    roots = [path for path in extract_dir.iterdir() if path.is_dir()]
    if len(roots) != 1:
        raise RuntimeError("Unexpected tarball layout")
    roots[0].rename(upstream_dir)


def checkout_upstream(
    upstream_dir: Path,
    ref: str,
    upstream_url: str,
    checkout_method: str,
) -> None:
    if upstream_dir.exists():
        shutil.rmtree(upstream_dir)
    upstream_dir.parent.mkdir(parents=True, exist_ok=True)

    method = checkout_method
    if method == "auto":
        method = "tarball" if is_default_github_upstream(upstream_url) else "git"

    if method == "tarball":
        try:
            download_tarball(upstream_dir, ref)
            return
        except Exception:
            if checkout_method != "auto":
                raise
            print("tarball download failed; falling back to git clone", file=sys.stderr)
            if upstream_dir.exists():
                shutil.rmtree(upstream_dir)
            clone_upstream(upstream_dir, ref, upstream_url)
            return

    if method == "git":
        clone_upstream(upstream_dir, ref, upstream_url)
        return

    raise ValueError(f"Unknown checkout method: {checkout_method}")


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
    parser.add_argument(
        "--checkout-method",
        choices=("auto", "tarball", "git"),
        default="auto",
    )
    parser.add_argument("--work-dir", type=Path, default=Path(".langchain-work"))
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument("--cache", type=Path, default=Path(".translation-cache/minimax.json"))
    parser.add_argument(
        "--state",
        type=Path,
        default=Path(".langchain-docs-upstream.json"),
    )
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
    load_env_files()
    args = parse_args()
    sha = upstream_sha(args.ref, args.upstream_url)
    state_path = args.state
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
    checkout_upstream(upstream_dir, args.ref, args.upstream_url, args.checkout_method)
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
            "base_url": os.environ.get("MINIMAX_BASE_URL")
            or os.environ.get("MINIMAX_URL")
            or "https://api.minimaxi.com/v1",
        },
        "output": {
            "site_dir": str(args.site_dir),
            "cache": str(args.cache),
        },
    }
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"synced upstream {sha}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
