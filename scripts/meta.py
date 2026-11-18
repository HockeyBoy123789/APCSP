import json, re, ssl, urllib.request, sys, concurrent.futures as cf

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0 Safari/537.36"
CTX = ssl._create_unverified_context()

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=45, context=CTX) as r:
        return r.read().decode("utf-8", "replace")

def meta(vid):
    try:
        h = get("https://www.youtube.com/watch?v=" + vid)
        pr = re.search(r'ytInitialPlayerResponse\s*=\s*(\{.*?\});\s*(?:var|</script>)', h, re.S)
        d = json.loads(pr.group(1))
        vd = d.get("videoDetails", {})
        mf = d.get("microformat", {}).get("playerMicroformatRenderer", {})
        return {
            "id": vid,
            "title": vd.get("title"),
            "channel": vd.get("author"),
            "lengthSeconds": int(vd.get("lengthSeconds", 0)),
            "publishDate": mf.get("publishDate", ""),
            "uploadDate": mf.get("uploadDate", ""),
            "description": (vd.get("shortDescription") or "")[:700],
        }
    except Exception as e:
        return {"id": vid, "error": str(e)}

ids = json.load(open("ids.json"))
with cf.ThreadPoolExecutor(max_workers=6) as ex:
    out = list(ex.map(meta, ids))
json.dump(out, open("meta.json", "w"), indent=1)
ok = [m for m in out if "error" not in m]
print("ok", len(ok), "of", len(ids))
for m in out:
    if "error" in m:
        print("ERR", m["id"], m["error"])
