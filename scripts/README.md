# Scripts

Two groups: the original YouTube **video-map** pipeline, and the **code-extraction**
helpers used to reconstruct solutions in `src/`.

## Video map / answer sheets

| Script | Purpose |
|---|---|
| `yt.py` | Searches YouTube and parses `ytInitialData` (needs the unverified SSL context on this Mac). |
| `meta.py` | Reads watch-page metadata from `ytInitialPlayerResponse`. |
| `make_queries.py` | Builds one search query per lesson. |
| `run_search.py` | Runs the cached queries in batches. |
| `build_report.py` | Regenerates `notes/csp-2025-video-map.md` from `data/meta.json`. |
| `build_answers.py` | Regenerates `notes/answers/` from the map (codes + clickable links). |

## Code extraction (reference solutions)

Requires `yt-dlp` (`python3 -m pip install --user yt-dlp`). The Swift tools need
Xcode command-line tools; they use AVFoundation and the built-in Vision OCR.

```bash
# 1. Download a 720p H.264 stream (AVFoundation cannot decode AV1).
python3 -m yt_dlp --no-check-certificates \
  -f '136/bv*[ext=mp4][vcodec^=avc1]/b[ext=mp4]' -o lesson.mp4 'https://youtu.be/VIDEO_ID'

# 2. OCR one frame every 2 seconds.
swiftc -O scripts/ocr_video.swift -o /tmp/ocr
/tmp/ocr lesson.mp4 2 > ocr.txt

# 3. Filter to code-like lines, or dump a time window.
python3 scripts/ocr_code.py ocr.txt
python3 scripts/ocr_code.py ocr.txt --find 900

# 4. Pull a single frame to read the code visually.
swiftc -O scripts/frame.swift -o /tmp/frame
/tmp/frame lesson.mp4 1000 frame.png
```

Frames beat OCR for accuracy: read the image, then confirm with the OCR text.
OCR mistakes to expect: `v` for `"`, `8` for `&`, `l` for `|`, and dropped
brackets. The code is usually stable for several seconds, so pick a frame in the
middle of a run.
