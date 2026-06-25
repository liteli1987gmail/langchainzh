#!/usr/bin/env python3
"""Check MiniMax key and endpoint without printing the key."""

from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from pathlib import Path


def load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def load_env_files() -> None:
    load_dotenv(Path(".env"))
    load_dotenv(Path.home() / ".serenity_env")


def base_url() -> str:
    if os.environ.get("MINIMAX_BASE_URL"):
        return os.environ["MINIMAX_BASE_URL"].rstrip("/")
    if os.environ.get("MINIMAX_URL"):
        endpoint = os.environ["MINIMAX_URL"].rstrip("/")
        suffix = "/chat/completions"
        return endpoint[: -len(suffix)] if endpoint.endswith(suffix) else endpoint
    return "https://api.minimaxi.com/v1"


def main() -> int:
    load_env_files()
    api_key = os.environ.get("MINIMAX_API_KEY")
    if not api_key:
        raise SystemExit("MINIMAX_API_KEY is missing")

    base = base_url()
    endpoint = base.rstrip("/") + "/chat/completions"
    model = os.environ.get("MINIMAX_MODEL", "MiniMax-M2.7-highspeed")
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": "Reply with OK only."}],
        "temperature": 0,
        "max_tokens": 8,
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    opener = (
        urllib.request.build_opener()
        if os.environ.get("MINIMAX_USE_PROXY", "").lower() in {"1", "true", "yes"}
        else urllib.request.build_opener(urllib.request.ProxyHandler({}))
    )
    try:
        with opener.open(request, timeout=60) as response:
            data = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"MiniMax HTTP error: {exc.code} {exc.reason}") from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"MiniMax URL error: {exc.reason!r}") from exc

    text = data.get("choices", [{}])[0].get("message", {}).get("content", "")
    print(f"MiniMax OK: endpoint={base} model={model} response={text[:20]!r}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
