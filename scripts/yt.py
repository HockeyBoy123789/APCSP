import json, re, urllib.parse, urllib.request, sys, os, ssl

CTX = ssl._create_unverified_context()

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"

def fetch(url, timeout=45):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=timeout, context=CTX) as r:
        return r.read().decode("utf-8", "replace")

def initial_data(html):
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    if not m:
        m = re.search(r'window\["ytInitialData"\] = (\{.*?\});', html, re.S)
    return json.loads(m.group(1)) if m else None

def walk_videos(obj, out):
    if isinstance(obj, dict):
        if "videoRenderer" in obj:
            v = obj["videoRenderer"]
            try:
                vid = v["videoId"]
                title = "".join(r.get("text", "") for r in v["title"].get("runs", [])) or v["title"].get("simpleText", "")
                ch = v.get("ownerText", {}).get("runs", [{}])[0].get("text", "")
                length = v.get("lengthText", {}).get("simpleText", "")
                pub = v.get("publishedTimeText", {}).get("simpleText", "")
                views = v.get("viewCountText", {}).get("simpleText", "")
                desc = " ".join(r.get("text", "") for s in v.get("detailedMetadataSnippets", []) for r in s.get("snippetText", {}).get("runs", []))
                out.append({"id": vid, "title": title, "channel": ch, "length": length, "published": pub, "views": views, "desc": desc[:300]})
            except Exception:
                pass
        for val in obj.values():
            walk_videos(val, out)
    elif isinstance(obj, list):
        for val in obj:
            walk_videos(val, out)

def search(q, n=10):
    url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(q)
    d = initial_data(fetch(url))
    out = []
    if d:
        walk_videos(d, out)
    seen, res = set(), []
    for v in out:
        if v["id"] in seen:
            continue
        seen.add(v["id"])
        res.append(v)
    return res[:n]

if __name__ == "__main__":
    q = sys.argv[1]
    for v in search(q, 12):
        print(f"{v['id']} | {v['length']} | {v['published']} | {v['channel']} | {v['title']}")
