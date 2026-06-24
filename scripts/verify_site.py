#!/usr/bin/env python3
"""Verify the generated static site has the minimum deployable shape."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument("--min-pages", type=int, default=1)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    index = args.site_dir / "index.html"
    search_index = args.site_dir / "search-index.json"

    if not index.exists():
        raise SystemExit(f"Missing {index}")
    if not search_index.exists():
        raise SystemExit(f"Missing {search_index}")

    html_pages = sorted(args.site_dir.rglob("*.html"))
    if len(html_pages) < args.min_pages:
        raise SystemExit(
            f"Expected at least {args.min_pages} HTML pages, found {len(html_pages)}"
        )

    try:
        json.loads(search_index.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid search index JSON: {exc}") from exc

    print(
        f"verified {len(html_pages)} HTML pages in {args.site_dir}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
