#!/usr/bin/env python3
"""Deploy the generated static site to Cloudflare Pages with Wrangler."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


MAX_CLOUDFLARE_FREE_ASSET_BYTES = 25 * 1024 * 1024


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument(
        "--project-name",
        default=os.environ.get("CLOUDFLARE_PROJECT_NAME", "langchainzh"),
    )
    parser.add_argument("--branch", default="main")
    parser.add_argument(
        "--account-id",
        default=os.environ.get("CLOUDFLARE_ACCOUNT_ID"),
        help="Optional Cloudflare account id; also read from CLOUDFLARE_ACCOUNT_ID.",
    )
    parser.add_argument(
        "--skip-verify",
        action="store_true",
        help="Skip local static-site checks before deploying.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the Wrangler command without deploying.",
    )
    return parser.parse_args()


def clean_proxy_env(env: dict[str, str]) -> dict[str, str]:
    """Wrangler's proxy agent rejects socks URLs; leave http(s) proxies intact."""
    cleaned = dict(env)
    for key in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
        value = cleaned.get(key, "")
        if value.lower().startswith(("socks://", "socks4://", "socks4a://", "socks5://", "socks5h://")):
            cleaned.pop(key, None)
    return cleaned


def configure_npm_cache(env: dict[str, str]) -> None:
    cache = env.get("NPM_CONFIG_CACHE") or env.get("npm_config_cache")
    cache_path = Path(cache).expanduser() if cache else None
    if cache_path is None or not npm_cache_is_writable(cache_path):
        cache_path = Path(tempfile.gettempdir()) / "langchainzh-npm-cache"
        if not npm_cache_is_writable(cache_path):
            raise SystemExit(f"Unable to create writable npm cache at {cache_path}")

    env["NPM_CONFIG_CACHE"] = str(cache_path)
    env["npm_config_cache"] = str(cache_path)


def configure_wrangler_env(env: dict[str, str]) -> None:
    wrangler_tmp = Path(tempfile.gettempdir()) / "langchainzh-wrangler"
    wrangler_tmp.mkdir(parents=True, exist_ok=True)
    env.setdefault("WRANGLER_WRITE_LOGS", "false")
    env.setdefault("WRANGLER_LOG_PATH", str(wrangler_tmp / "logs"))
    env.setdefault("WRANGLER_CACHE_DIR", str(wrangler_tmp / "cache"))


def npm_cache_is_writable(cache_path: Path) -> bool:
    try:
        probe_dir = cache_path / "_cacache" / "tmp"
        probe_dir.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(prefix=".langchainzh-", dir=probe_dir):
            pass
    except OSError:
        return False
    return True


def run(cmd: list[str], *, env: dict[str, str] | None = None) -> None:
    print("+ " + " ".join(cmd))
    subprocess.run(cmd, check=True, env=env)


def check_site(site_dir: Path) -> None:
    run([sys.executable, "scripts/verify_site.py", "--site-dir", str(site_dir), "--min-pages", "20"])

    oversized = [
        (path.stat().st_size, path)
        for path in site_dir.rglob("*")
        if path.is_file() and path.stat().st_size > MAX_CLOUDFLARE_FREE_ASSET_BYTES
    ]
    if oversized:
        details = "\n".join(f"{size} {path}" for size, path in sorted(oversized, reverse=True)[:10])
        raise SystemExit(
            "Cloudflare Pages Free has a 25 MiB single-file limit. "
            f"Run scripts/optimize_site_assets.py first.\n{details}"
        )


def main() -> int:
    args = parse_args()
    if not args.site_dir.exists():
        raise SystemExit(f"Missing site directory: {args.site_dir}")
    if not shutil.which("npx"):
        raise SystemExit("Missing npx. Install Node.js/npm, then retry.")

    if not args.skip_verify:
        check_site(args.site_dir)

    env = clean_proxy_env(os.environ)
    configure_npm_cache(env)
    configure_wrangler_env(env)
    if args.account_id:
        env["CLOUDFLARE_ACCOUNT_ID"] = args.account_id

    cmd = [
        "npx",
        "--yes",
        "wrangler@latest",
        "pages",
        "deploy",
        str(args.site_dir),
        "--project-name",
        args.project_name,
        "--branch",
        args.branch,
    ]

    if args.dry_run:
        print("+ " + " ".join(cmd))
        print(
            "Dry run only. For real deploy, authenticate with `wrangler login` "
            "or set CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID."
        )
        return 0

    try:
        run(cmd, env=env)
    except subprocess.CalledProcessError as exc:
        raise SystemExit(
            "Cloudflare deploy failed. Authenticate with `wrangler login`, or set "
            "`CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`, then rerun.\n"
            f"Command exited with {exc.returncode}."
        ) from exc

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
