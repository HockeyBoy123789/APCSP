import json, concurrent.futures as cf
from yt import search

Q = json.load(open("queries.json"))

def run(item):
    key, q = item
    try:
        return key, search(q, 12)
    except Exception as e:
        return key, [{"error": str(e)}]

with cf.ThreadPoolExecutor(max_workers=5) as ex:
    results = dict(ex.map(run, Q.items()))

json.dump(results, open("results.json", "w"), indent=1)
print("done", len(results))
