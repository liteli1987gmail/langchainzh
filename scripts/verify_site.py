#!/usr/bin/env python3
"""Verify the generated static site has the minimum deployable shape."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


RESIDUAL_PATTERNS = [
    "<fragment>",
    "</fragment>",
    "&lt;fragment",
    "&lt;/fragment",
    "&lt;Card",
    "&lt;CardGroup",
    "&lt;Callout",
    "&lt;Tip&gt;",
    "&lt;Note&gt;",
    "&lt;Warning&gt;",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument("--min-pages", type=int, default=1)
    parser.add_argument(
        "--skip-residual-scan",
        action="store_true",
        help="Skip scan for visible unrendered MDX/Mintlify wrapper tags.",
    )
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

    if not args.skip_residual_scan:
        residual_hits: list[str] = []
        for page in html_pages:
            text = page.read_text(encoding="utf-8", errors="ignore")
            found = [pattern for pattern in RESIDUAL_PATTERNS if pattern in text]
            if found:
                residual_hits.append(f"{page}: {', '.join(found)}")
        if residual_hits:
            sample = "\n".join(residual_hits[:20])
            raise SystemExit(
                "Found visible unrendered MDX/Mintlify residue:\n" + sample
            )

    print(
        f"verified {len(html_pages)} HTML pages in {args.site_dir}",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
