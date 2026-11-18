#!/usr/bin/env python3
"""Build per-unit answer sheets (answers only) from the video map.

Parses notes/csp-2025-video-map.md so the answers can never drift from the report.
Writes notes/answers/unit-NN-<slug>.md and notes/answers/README.md.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "notes", "csp-2025-video-map.md")
OUT = os.path.join(ROOT, "notes", "answers")

UNITS = {
    1: "Digital Information",
    2: "The Internet",
    3: "Intro to App Design",
    4: "Variables, Conditionals, and Functions",
    5: "Data",
    6: "Lists, Loops, and Traversals",
    7: "Parameters, Return, and Libraries",
    8: "Cybersecurity and Global Impacts",
    9: "Create PT Prep",
    10: "Algorithms",
}

def split_row(line):
    parts = re.split(r"(?<!\\)\|", line.strip())
    return [p.strip().replace("\\|", "|") for p in parts[1:-1]]

rows = []
for line in open(SRC):
    if not line.startswith("|"):
        continue
    cells = split_row(line)
    if len(cells) != 8 or not cells[0].isdigit():
        continue
    unit = int(cells[0])
    rows.append({
        "unit": unit,
        "lesson": cells[1],
        "video": cells[2],
        "channel": cells[3],
        "length": cells[4],
        "date": cells[5],
        "url": cells[6],
    })

def esc(x):
    return str(x).replace("|", "\\|")

os.makedirs(OUT, exist_ok=True)

def slug(name):
    s = name.lower().replace(",", "").replace("&", "and")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s

index = ["# Answer sheets", "",
         "One file per unit. Each row is only the answer: the lesson and the video to watch.", ""]

total = 0
for unit, title in UNITS.items():
    urows = [r for r in rows if r["unit"] == unit]
    total += len(urows)
    fname = f"unit-{unit:02d}-{slug(title)}.md"
    lines = [f"# Unit {unit} — {title}", ""]
    lines.append("| Lesson | Answer | Link |")
    lines.append("|---|---|---|")
    missing = 0
    for r in urows:
        if r["video"] == "—":
            missing += 1
            lines.append(f"| {esc(r['lesson'])} | No video — use the Code.org lesson plan | — |")
        else:
            lines.append(f"| {esc(r['lesson'])} | {esc(r['video'])} ({esc(r['channel'])}) | {r['url']} |")
    lines.append("")
    open(os.path.join(OUT, fname), "w").write("\n".join(lines))
    index.append(f"- [Unit {unit} — {title}]({fname}) — {len(urows)} lessons"
                 + (f", {missing} without a video" if missing else ""))

index += ["", f"Total: {total} lessons. Regenerate with `python3 scripts/build_answers.py`."]
open(os.path.join(OUT, "README.md"), "w").write("\n".join(index) + "\n")
print(f"wrote {len(UNITS)} unit files, {total} lessons")
