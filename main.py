#!/usr/bin/env python3
"""news-image-20261124 entry: write the front page for Tuesday 24 November 2026
to /output/entry.png.

The image is produced by build_image_v1.py (Pillow, deterministic) from 30
verified 24-Nov stories: Nvidia reinstating Jensen Huang as CEO (+31%, best
US market day since April 2025) as the lead, the WSJ inside story of
Ukraine's 2,400 km Libya strike, NATO's AWACS deployment to Poland and the
EU's 22nd sanctions package as heroes, plus 6 medium stories, 20 briefs, a
region-count bar, a DATE CHECK box and a markets strip (Monday's close,
labelled as such). Four illustrations were generated for this day; no
leaderboard images were used.

This entrypoint is stdlib-only: it copies the pre-built assets/entry.png
to /output/entry.png, byte for byte.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")

OUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, OUT)
print(f"wrote {OUT} ({os.path.getsize(OUT)} bytes)")
