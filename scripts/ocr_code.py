#!/usr/bin/env python3
"""Summarize code-like lines from an ocr_video.swift transcript.

Usage:
    python3 scripts/ocr_code.py ocr.txt            # code-like lines only
    python3 scripts/ocr_code.py ocr.txt --all      # every line, per timestamp
    python3 scripts/ocr_code.py ocr.txt --find 900 # lines around t=900s

The OCR output has the shape:

    === t=1000.0 ===
    Lesson 4: Lists Make
    onEvent("addButton", "click", function() {

This script drops UI chrome (titles, toolboxes) so the frames showing real code
stand out, and collapses runs of identical lines.
"""
import re
import sys

CODE = re.compile(
    r"""(
        onEvent\s*\( | function\s*\(? | \bvar\s+\w+ | \blet\s+\w+ | \breturn\b |
        setText\s*\( | setProperty\s*\( | getText\s*\( | getNumber\s*\( |
        getProperty\s*\( | appendItem\s*\( | insertItem\s*\( | removeItem\s*\( |
        console\.log\s*\( | \bfor\s*\( | \bwhile\s*\( | \bif\s*\( | \belse\b |
        \bindex\b | \binputList\b | \blist\b | \w+\s*=\s*[^=] | \w+\.length |
        \btoString\b | \bparseInt\b | \bMath\. | \bprompt\w*\s*\(
    )""",
    re.X,
)

# Lines that are clearly the Code.org UI or the App Lab toolbox, not code.
NOISE = re.compile(
    r"^(Lesson \d|Code|Design|Instructions|Help & Tips|Toolbox|Workspace|"
    r"Version History|Show Text|Show Toolbox|Run|Reset|Submit|Share|Remix|"
    r"Saved|Saving|Debug Console|Show Debug Commands|Watchers|Clear|"
    r"New reminder|Add|screen1|RemindME|Ui controls|UI controls|Control|Math|"
    r"Variables|Functions|Code\.org|C\.S\. Principles)\b",
    re.I,
)


def main() -> None:
    path = sys.argv[1]
    show_all = "--all" in sys.argv
    find = None
    if "--find" in sys.argv:
        find = float(sys.argv[sys.argv.index("--find") + 1])

    t = 0.0
    last = None
    for raw in open(path, errors="replace"):
        line = raw.rstrip("\n")
        m = re.match(r"=== t=([\d.]+) ===", line)
        if m:
            t = float(m.group(1))
            last = None
            continue
        s = line.strip()
        if not s:
            continue
        if find is not None and abs(t - find) > 6:
            continue
        if not show_all:
            if NOISE.match(s) or not CODE.search(s):
                continue
        if s == last:
            continue
        last = s
        print(f"{t:7.1f}  {s}")


if __name__ == "__main__":
    main()
