# CONTEXT — read this first

Handoff file for continuing work in this folder. **Update this file before the session runs out of context.**

Last updated: 2026-11-18

## What this project is

Adrian is working through Code.org's AP Computer Science Principles course, **csp-2025** version.
The deliverable so far is a lesson-by-lesson map of YouTube videos that explain each lesson's concept.

## Current state

| Item | Status |
|---|---|
| Folder | `/Users/adrian/Desktop/APCSP` (git repo, branch `main`) |
| Curriculum confirmed | Yes — 10 units, 97 instructional lessons |
| Video research | Done for all 97 lessons |
| Report (raw) | `notes/csp-2025-video-map.md` (single table + notes) |
| Report (formatted) | `notes/csp-2025-video-guide.md` — verified: 97 rows, 88 URLs, 0 metadata diffs |
| Answer sheets | `notes/answers/` — 10 per-unit files: code, lesson, video, clickable link |
| Reference solutions | `src/` — 7 lessons (U3L7, U4L12, U6L4, U6L8, U6L12, U6L13, U7L8) extracted from answer-key videos |
| Commits | `225335d` scaffold, `e86ea3c` video map, `6d133a4` App Lab solutions + OCR pipeline, plus this session's project solutions |

## This week (2026-11-12 → 2026-11-18)

- Finished the end-of-unit app projects that were still missing from `src/`:
  **U3 L7 Coding Quiz**, **U4 L12 Fortune Teller**, and **U6 L13 Hackathon**
  (AP CS Test Taker Demographics example).
- Each new folder has a `README.md` (task, design-element IDs, key ideas, caveats) and
  a commented App Lab text-mode `app.js`; all three pass `node --check`.
- Updated `src/README.md` with the new folders and refreshed this handoff file.
- Extracted the code from Mr. Kaiser walkthroughs frame by frame (OCR + direct PNG
  frames), because the originally mapped U3 L7 / U4 L12 videos were not usable answer
  keys.

## How the curriculum was confirmed

`curriculum.code.org/csp-current` is a JS app; the real course is `studio.code.org/courses/csp-2025`.
The page embeds the whole course structure in a `data-courses-show` attribute (HTML-escaped JSON).
Parse that, not the rendered DOM.

- Site notice: "Looking for the 26-27 version of CSP? You are in the right place! There are no changes
  to the curriculum for this year and this is the current version." So csp-2025 applies to 2026–27.
- 10 units: Digital Information / The Internet / Intro to App Design / Variables, Conditionals, Functions /
  Data / Lists, Loops, Traversals / Parameters, Return, Libraries / Cybersecurity and Global Impacts /
  Create PT Prep / Algorithms.
- 97 lessons after excluding end-of-unit surveys and two alternate-path lessons
  (U4 "Lesson 7 (Alternate)", U6 "Lesson 3 (Alternate)").

## Critical numbering fact

Units 1–4 kept their numbers. Units 5–10 were reordered for 2024–25:

| Pre-2024 unit | Today |
|---|---|
| 5 Lists, Loops, Traversals | 6 |
| 6 Algorithms | 10 |
| 7 Parameters, Return, Libraries | 7 (unchanged) |
| 8 Create PT Prep | 9 |
| 9 Data | 5 |
| 10 Cybersecurity / Global Impacts | 8 |

Any pre-2024 video labelled Unit 5/6/8/9/10 must be re-mapped, never assumed.

## Files

- `notes/csp-2025-video-guide.md` — reader-facing guide (per-unit sections, TOC, gaps, appendices).
- `notes/csp-2025-video-map.md` — raw single-table source of truth; the scripts parse this.
- `notes/answers/README.md` — index of the 10 answer sheets.
- `notes/answers/unit-NN-*.md` — answers only: Code | Lesson | Answer | Link, with clickable video
  links. Codes are `U{unit}L{lesson}` (e.g. U1L4). Generated, do not hand-edit.
- `data/lessons.json` — scraped lesson list (unit, number, title, duration).
- `data/queries.json` / `data/results.json` — search query per lesson and raw top-12 YouTube results.
- `data/meta.json` — verified metadata for 121 candidate videos (title, channel, seconds, publishDate, description).
- `scripts/yt.py` — YouTube search scraper (parses `ytInitialData`; needs unverified SSL context on this machine).
- `scripts/meta.py` — watch-page metadata scraper (reads `ytInitialPlayerResponse`).
- `scripts/build_report.py` — builds the markdown table from `meta.json` + the ROWS list.
- `scripts/build_answers.py` — parses the map and regenerates `notes/answers/` (97 lessons checked),
  adding Code.org lesson codes and clickable video links.
- `scripts/run_search.py`, `scripts/make_queries.py` — batch search pipeline.
- `scripts/ocr_video.swift` — samples a video and OCRs every frame (AVFoundation + Vision).
- `scripts/frame.swift` — dumps one frame as PNG (most accurate way to read code).
- `scripts/ocr_code.py` — filters OCR output to code-like lines / a time window.
- `scripts/README.md` — full extraction workflow, including the yt-dlp command.
- `src/` — App Lab reference solutions, one folder per lesson; see `src/README.md`.

## Method / honesty notes

- Verdicts are based on title, channel, description and format — not a full watch-through.
- "No decent coverage" currently: U3 L8, U4 L13, U5 L6, U7 L9, U7 L10, U7 L11, U8 L4, U8 L7, U8 L10.
- Solution-forward but usable: U1 L3, U1 L12, U2 L7, U5 L5, U6 L4, U6 L8, U6 L12, U6 L13, U7 L3, U7 L8.
- Code.org's YouTube channel now displays as **CodeAI** (site rebrand); old titles still say Code.org.
- YouTube network access was flaky at the end of the session (DNS timeouts). If it fails, retry later;
  everything needed is already cached in `data/`.

## In flight

Reference solutions in `src/` — started 2026-11-17.

- Done: **U3 L7 Coding Quiz**, **U4 L12 Fortune Teller**, **U6 L4 RemindMe**,
  **U6 L8 Lock Screen Maker**, **U6 L12 Random Forecaster**, **U6 L13 Hackathon**
  (AP CS Test Taker Demographics example), **U7 L8 Make a Library**. Each has a
  per-lesson README and commented App Lab JS.
- Method: read the answer-key video frame by frame (OCR + direct frame images), then
  write a clean version. Frames beat OCR; see `scripts/README.md`.
- Not literal transcriptions: the walkthrough videos edit code live, so the files are
  the final working version, with inferred glue (element lists, event handlers) called
  out in each README.
- Only ~10 of the 97 mapped videos are actual answer-key walkthroughs. The rest are
  concept tutorials and cannot supply complete code.

Answer-sheet work is finished: `notes/answers/` has codes, lessons, videos and
clickable links; 97 rows, 88 links, 9 gaps.

- `notes/csp-2025-video-guide.md` is the reader-facing version: intro, how-to-use, at-a-glance counts,
  linked TOC, one section per unit with its own 7-column table and a one-line takeaway, gaps section,
  and two appendices (numbering map, method/limits).
- `notes/csp-2025-video-map.md` is kept as the raw source table.
- Verified: 97 lesson rows (13/8/8/13/9/14/11/11/4/6), 88 distinct URLs, 9 placeholder rows,
  zero differences against `data/meta.json`.

## Next steps (pick up here)

0. Regenerate answers after any pick change: `python3 scripts/build_answers.py`
1. Continue reference solutions from the answer-key videos:
   U7 L3 Practice, U7 L4 RPS Make, U4 L2 Investigate,
   U4 L8 Conditionals Make, U4 L11 Functions Make.
2. Optional: fill the 9 gaps with Code.org teacher-forum or teacher-PD resources (not YouTube).
3. Optional: extend `scripts/build_report.py` to emit CSV/JSON for a spreadsheet.
4. Always update this file before context runs out, and commit.

## How to extract another lesson's code (repeatable)

This is the procedure that produced `src/unit-06/lesson-04-lists-make/` and the three
solutions beside it. It works from any answer-key video in the map, even in a fresh
session with no memory of this conversation.

### Prerequisites (one-time)

```bash
python3 -m pip install --user yt-dlp     # only needed once
swiftc --version                          # Xcode CLT must be installed
```

### Pipeline

```bash
cd ~/Desktop/APCSP
VIDEO=ChYHvfktgCE                         # pick from the table below / notes/answers
NAME=u6l13

# 1. Download 720p H.264. Format 136 is H.264; do NOT let yt-dlp pick AV1 (fmt 398),
#    because AVFoundation cannot decode AV1 and OCR silently outputs nothing.
python3 -m yt_dlp --no-check-certificates \
  -f '136/bv*[ext=mp4][vcodec^=avc1]/b[ext=mp4]' \
  -o /tmp/$NAME.%(ext)s "https://youtu.be/$VIDEO"

# 2. OCR one frame every 2 seconds (~2 min per 20 min of video).
swiftc -O scripts/ocr_video.swift -o /tmp/ocr
/tmp/ocr /tmp/$NAME.mp4 2 > /tmp/ocr_$NAME.txt

# 3. Find the timestamps where real code is on screen.
python3 scripts/ocr_code.py /tmp/ocr_$NAME.txt
python3 scripts/ocr_code.py /tmp/ocr_$NAME.txt --find 1000

# 4. Read frames directly — OCR guesses, the image does not.
swiftc -O scripts/frame.swift -o /tmp/frame
/tmp/frame /tmp/$NAME.mp4 1000 /tmp/f1000.png   # then open /tmp/f1000.png
```

**Read frames, not just OCR.** OCR confuses `"` with `v`, `&` with `8`, `|` with `l`,
and drops brackets. Pick a frame in the middle of a stable run, read it, and use OCR
only to locate the timestamps.

### Then write the solution

1. Create `src/unit-NN/lesson-NN-slug/`.
2. `README.md`: lesson name, source video + URL, timestamps where code appears, what the
   app does, a table of required element IDs, key ideas, caveats.
3. `app.js` (or `library.js`): clean, commented App Lab text-mode code. Note at the top
   where it came from. Keep the video's final working version; the walkthroughs edit
   code live, so early frames are not the answer.
4. `node --check src/.../app.js` — syntax check.
5. Add the new folder to the layout in `src/README.md`.
6. Update "In flight" and this file, then commit.

### Answer-key videos still to do (from the map)

| Lesson | Video ID | Length | Notes |
|---|---|---|---|
| U7 L3 Parameters/Return Practice | `8t-HxetA4ns` | 4:33 | answer tutorial |
| U7 L4 Parameters/Return Make (RPS) | `XFcgoBRHl-c` | 14:19 | class build |
| U4 L2 Variables Investigate | `G6X4jByg41I` | 30:30 | works every level |
| U4 L8 Conditionals Make | `rTU79XM8V1Q` | 28:12 | museum-ticket app |
| U4 L11 Functions Make | `T5mFiXHqTmo` | 42:13 | quote-maker app |

Done already: U6 L4 (`z_OOZ2gaY-s`), U6 L8 (`B-yYUaC5GxE`), U6 L12 (`pk32rysRQAg`),
U6 L13 (`ChYHvfktgCE`), U7 L8 (`1joEzBtosrY`).

The mapped videos for U3 L7 and U4 L12 were not usable answer keys, so those two were
extracted from Mr. Kaiser walkthroughs instead: U3 L7 `ItucouYL8y4` (Coding Quiz) and
U4 L12 `OTx-S3ZmGxE` (Fortune Teller). The U6 L13 app is one example hackathon project
(AP CS Test Taker Demographics), not a required topic.

**Hard limit:** only these answer-key / walkthrough videos contain completed code. The
other coding-lesson videos are concept tutorials (e.g. U4 L3 `2DLWC7DMPx0` never solves
the Code.org levels). For those, a reference solution has to be written from Code.org's
public lesson plan, not extracted from video — say so in the README if that happens.

## Commands

```bash
cd ~/Desktop/APCSP
python3 scripts/build_report.py     # regenerates the markdown table
git add -A && git commit -m "..."   # commit after changes
```
