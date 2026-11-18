# CONTEXT — read this first

Handoff file for continuing work in this folder. **Update this file before the session runs out of context.**

Last updated: 2026-11-17

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
| Answer sheets | `notes/answers/` — 10 per-unit files, answers only (lesson → video + link) |
| Commits | `225335d` scaffold, `e86ea3c` video map, plus formatting commit |

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
- `notes/answers/unit-NN-*.md` — answers only: Lesson | Answer | Link. Generated, do not hand-edit.
- `data/lessons.json` — scraped lesson list (unit, number, title, duration).
- `data/queries.json` / `data/results.json` — search query per lesson and raw top-12 YouTube results.
- `data/meta.json` — verified metadata for 121 candidate videos (title, channel, seconds, publishDate, description).
- `scripts/yt.py` — YouTube search scraper (parses `ytInitialData`; needs unverified SSL context on this machine).
- `scripts/meta.py` — watch-page metadata scraper (reads `ytInitialPlayerResponse`).
- `scripts/build_report.py` — builds the markdown table from `meta.json` + the ROWS list.
- `scripts/build_answers.py` — parses the map and regenerates `notes/answers/` (97 lessons checked).
- `scripts/run_search.py`, `scripts/make_queries.py` — batch search pipeline.

## Method / honesty notes

- Verdicts are based on title, channel, description and format — not a full watch-through.
- "No decent coverage" currently: U3 L8, U4 L13, U5 L6, U7 L9, U7 L10, U7 L11, U8 L4, U8 L7, U8 L10.
- Solution-forward but usable: U1 L3, U1 L12, U2 L7, U5 L5, U6 L4, U6 L8, U6 L12, U6 L13, U7 L3, U7 L8.
- Code.org's YouTube channel now displays as **CodeAI** (site rebrand); old titles still say Code.org.
- YouTube network access was flaky at the end of the session (DNS timeouts). If it fails, retry later;
  everything needed is already cached in `data/`.

## In flight

Nothing. The formatting pass is finished.

- `notes/csp-2025-video-guide.md` is the reader-facing version: intro, how-to-use, at-a-glance counts,
  linked TOC, one section per unit with its own 7-column table and a one-line takeaway, gaps section,
  and two appendices (numbering map, method/limits).
- `notes/csp-2025-video-map.md` is kept as the raw source table.
- Verified: 97 lesson rows (13/8/8/13/9/14/11/11/4/6), 88 distinct URLs, 9 placeholder rows,
  zero differences against `data/meta.json`.

## Next steps (pick up here)

0. Regenerate answers after any pick change: `python3 scripts/build_answers.py`
1. Optional: fill the 9 gaps with Code.org teacher-forum or teacher-PD resources (not YouTube).
2. Optional: extend `scripts/build_report.py` to emit CSV/JSON for a spreadsheet.
3. Optional: add a per-unit "study order" (which lessons to pair with which video) for Adrian's pacing.
4. Always update this file before context runs out, and commit.

## Commands

```bash
cd ~/Desktop/APCSP
python3 scripts/build_report.py     # regenerates the markdown table
git add -A && git commit -m "..."   # commit after changes
```
