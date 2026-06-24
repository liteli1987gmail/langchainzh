#!/usr/bin/env python3
"""Check whether the upstream LangChain docs ref changed."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path


DEFAULT_UPSTREAM_URL = "https://github.com/langchain-ai/docs.git"


def capture(command: list[str]) -> str:
    return subprocess.check_output(command, text=True).strip()


def current_upstream_sha(upstream_url: str, ref: str) -> str:
    output = capture(["git", "ls-remote", upstream_url, ref])
    if not output:
        raise RuntimeError(f"Could not resolve {ref} from {upstream_url}")
    return output.split()[0]


def recorded_sha(state_path: Path) -> str:
    if not state_path.exists():
        return ""
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ""
    return str(state.get("upstream_sha") or "")


def write_github_output(values: dict[str, str]) -> None:
    output_path = os.environ.get("GITHUB_OUTPUT")
    if not output_path:
        return
    with Path(output_path).open("a", encoding="utf-8") as handle:
        for key, value in values.items():
            handle.write(f"{key}={value}\n")


def write_github_summary(lines: list[str]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    with Path(summary_path).open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines))
        handle.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--upstream-url", default=DEFAULT_UPSTREAM_URL)
    parser.add_argument("--ref", default="main")
    parser.add_argument(
        "--state",
        type=Path,
        default=Path(".langchain-docs-upstream.json"),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    current_sha = current_upstream_sha(args.upstream_url, args.ref)
    previous_sha = recorded_sha(args.state)
    changed = "true" if current_sha != previous_sha else "false"

    write_github_output(
        {
            "changed": changed,
            "current_sha": current_sha,
            "previous_sha": previous_sha,
        }
    )
    write_github_summary(
        [
            "## LangChain upstream check",
            "",
            f"- Upstream: `{args.upstream_url}`",
            f"- Ref: `{args.ref}`",
            f"- Current SHA: `{current_sha}`",
            f"- Recorded SHA: `{previous_sha or 'none'}`",
            f"- Changed: `{changed}`",
        ]
    )

    print(f"current={current_sha}")
    print(f"recorded={previous_sha or 'none'}")
    print(f"changed={changed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
