#!/usr/bin/env python3
"""news-image-20261124: print Tuesday 24 November 2026's front page.

The page is drawn ahead of time by build_image_v1.py (Pillow, deterministic)
and stored as assets/entry.png: 30 verified stories from 24 November 2026.
Nvidia brings Jensen Huang back as chief executive, Ukraine's 2,400 km
strike off Libya gets the Wall Street Journal's inside story, NATO sends
AWACS aircraft to Poland, and the EU proposes its 22nd sanctions package.
A region bar, a DATE CHECK box and a markets strip (Monday's close, labelled
as such) complete the page.

This program only places that finished page at /output/entry.png. It reads
nothing else, reaches no network, and writes the same bytes every run.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "assets" / "entry.png"
DEST_DIR = Path(os.environ.get("OUTPUT_DIR", "/output"))


def main():
    if not SOURCE.is_file():
        print(f"missing {SOURCE}")
        return 1
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    target = DEST_DIR / "entry.png"
    shutil.copyfile(SOURCE, target)
    print(f"wrote {target} ({target.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
