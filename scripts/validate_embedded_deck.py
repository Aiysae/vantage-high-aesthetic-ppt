#!/usr/bin/env python3
"""Validate the visible structure of an embedded-image PPTX deck.

Embedded-image mode requires one full-slide picture and no visible text objects
per slide. This check intentionally inspects the PPTX XML rather than judging
image quality or OCR accuracy.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from zipfile import BadZipFile, ZipFile


SLIDE_RE = re.compile(r"^ppt/slides/slide\d+\.xml$")
PIC_RE = re.compile(r"<p:pic\b")
TEXT_SHAPE_RE = re.compile(r"<p:sp\b")
TEXT_RUN_RE = re.compile(r"<a:t(?:\s|>)")


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        archive = ZipFile(path)
    except (OSError, BadZipFile) as exc:
        return [f"not a readable PPTX: {exc}"]

    with archive:
        slides = sorted(name for name in archive.namelist() if SLIDE_RE.match(name))
        if not slides:
            return ["no slide XML files found"]

        for slide_name in slides:
            xml = archive.read(slide_name).decode("utf-8", errors="replace")
            pictures = len(PIC_RE.findall(xml))
            text_shapes = len(TEXT_SHAPE_RE.findall(xml))
            text_runs = len(TEXT_RUN_RE.findall(xml))
            if pictures != 1:
                errors.append(f"{slide_name}: expected 1 picture shape, found {pictures}")
            if text_shapes or text_runs:
                errors.append(
                    f"{slide_name}: expected 0 visible text objects, "
                    f"found {text_shapes} shapes / {text_runs} text runs"
                )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deck", type=Path, help="path to the PPTX to validate")
    args = parser.parse_args()
    errors = validate(args.deck)
    if errors:
        print("embedded-image validation: FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("embedded-image validation: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
