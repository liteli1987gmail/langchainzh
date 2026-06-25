#!/usr/bin/env python3
"""Optimize generated static assets for free static-hosting limits."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageSequence


GIF_ATTEMPTS = (
    {"step": 2, "scale": 0.85, "colors": 128},
    {"step": 3, "scale": 0.72, "colors": 96},
    {"step": 4, "scale": 0.65, "colors": 64},
    {"step": 5, "scale": 0.58, "colors": 64},
)


def compress_gif(source: Path, target: Path, *, step: int, scale: float, colors: int) -> None:
    image = Image.open(source)
    width, height = image.size
    size = (max(1, int(width * scale)), max(1, int(height * scale)))
    frames = []
    durations = []
    last_kept = -1
    default_duration = image.info.get("duration", 100)

    for index, frame in enumerate(ImageSequence.Iterator(image)):
        duration = frame.info.get("duration", default_duration)
        if index % step == 0:
            resized = frame.convert("RGBA").resize(size, Image.Resampling.LANCZOS)
            quantized = resized.convert("P", palette=Image.Palette.ADAPTIVE, colors=colors)
            frames.append(quantized)
            durations.append(duration)
            last_kept = len(durations) - 1
        elif last_kept >= 0:
            durations[last_kept] += duration

    frames[0].save(
        target,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=durations,
        loop=0,
        disposal=2,
    )


def optimize_large_gif(path: Path, max_bytes: int) -> bool:
    original_size = path.stat().st_size
    best_path: Path | None = None
    best_size = original_size

    for attempt_index, attempt in enumerate(GIF_ATTEMPTS, start=1):
        tmp_path = path.with_name(f".{path.name}.opt{attempt_index}.tmp")
        try:
            compress_gif(path, tmp_path, **attempt)
            size = tmp_path.stat().st_size
            if size < best_size:
                if best_path and best_path.exists():
                    best_path.unlink()
                best_path = tmp_path
                best_size = size
            else:
                tmp_path.unlink()
            if size <= max_bytes:
                break
        except Exception:
            if tmp_path.exists():
                tmp_path.unlink()
            raise

    if best_path is None:
        return original_size <= max_bytes

    best_path.replace(path)
    print(f"optimized {path}: {original_size} -> {best_size}")
    return best_size <= max_bytes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument("--max-file-mib", type=float, default=25.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    max_bytes = int(args.max_file_mib * 1024 * 1024)
    oversized = [
        path
        for path in args.site_dir.rglob("*")
        if path.is_file() and path.stat().st_size > max_bytes
    ]

    failures = []
    for path in oversized:
        if path.suffix.lower() == ".gif":
            if not optimize_large_gif(path, max_bytes):
                failures.append(path)
        else:
            failures.append(path)

    if failures:
        print("Files still exceed hosting limit:")
        for path in failures:
            print(f"{path}: {path.stat().st_size}")
        return 1

    print(f"asset limits ok: {len(oversized)} optimized")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
