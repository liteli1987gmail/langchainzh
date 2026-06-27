#!/usr/bin/env python3
"""Export the built docs with the official Mintlify CLI."""

from __future__ import annotations

import argparse
import os
import shlex
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-dir", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, default=Path("site"))
    parser.add_argument(
        "--mint-command",
        default=os.environ.get("MINT_COMMAND", "npx --yes mint@latest"),
        help="Command prefix used to run Mintlify CLI, for example 'mint' or 'npx --yes mint@latest'.",
    )
    parser.add_argument(
        "--output-zip",
        type=Path,
        default=None,
        help="Optional path for the Mintlify export zip. Defaults to a temp file.",
    )
    return parser.parse_args()


def run(command: list[str], cwd: Path, env: dict[str, str]) -> None:
    print("+ " + " ".join(shlex.quote(part) for part in command))
    subprocess.run(command, cwd=cwd, env=env, check=True)


def find_export_root(extract_dir: Path) -> Path:
    candidates = [extract_dir]
    candidates.extend(path for path in extract_dir.iterdir() if path.is_dir())
    for candidate in candidates:
        if (candidate / "serve.js").exists() or (candidate / "_next").exists():
            return candidate
    html_roots = [
        path.parent
        for path in extract_dir.rglob("*.html")
        if path.name == "index.html"
    ]
    if html_roots:
        return min(html_roots, key=lambda path: len(path.parts))
    raise RuntimeError("Could not find Mintlify export root in zip")


def copy_export(export_root: Path, out_dir: Path) -> None:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    shutil.copytree(export_root, out_dir)
    # Mintlify offline exports are self-contained and may not include the legacy
    # search index expected by the previous static exporter.
    search_index = out_dir / "search-index.json"
    if not search_index.exists():
        search_index.write_text("[]\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    build_dir = args.build_dir.resolve()
    if not (build_dir / "docs.json").exists():
        raise SystemExit(f"Missing docs.json in Mintlify build dir: {build_dir}")

    mint_command = shlex.split(args.mint_command)
    if not mint_command:
        raise SystemExit("--mint-command cannot be empty")

    env = os.environ.copy()
    # Keep Mintlify/npx caches outside the repo by default, but allow callers to
    # override them for CI cache actions.
    env.setdefault("npm_config_cache", "/private/tmp/npm-cache-langchain")

    with tempfile.TemporaryDirectory(prefix="mintlify-export-") as temp_name:
        temp_dir = Path(temp_name)
        output_zip = (
            args.output_zip.resolve()
            if args.output_zip
            else temp_dir / "mintlify-export.zip"
        )
        output_zip.parent.mkdir(parents=True, exist_ok=True)

        validate_command = [*mint_command, "validate"]
        run(validate_command, cwd=build_dir, env=env)

        export_command = [*mint_command, "export", "--output", str(output_zip)]
        run(export_command, cwd=build_dir, env=env)

        if not output_zip.exists():
            raise RuntimeError(f"Mintlify export did not create {output_zip}")

        extract_dir = temp_dir / "extracted"
        extract_dir.mkdir()
        with zipfile.ZipFile(output_zip) as archive:
            archive.extractall(extract_dir)

        export_root = find_export_root(extract_dir)
        copy_export(export_root, args.out_dir)

    print(f"exported Mintlify site to {args.out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
