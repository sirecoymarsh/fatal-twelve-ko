import collections
import glob
import json

ROOT = {"009", "010", "011_02", "011_02GH", "012_01F", "012_01GH", "012_02"}
TERMS = {
    "運命の大広間": ["운명의 대회랑", "운명의 대광장", "운명의 대전당", "운명의 대회관"],
    "夢の世界": ["꿈의 세계", "꿈속 세계", "꿈속 세상", "꿈의 세상"],
    "女神の選定": ["여신의 선정"],
    "運命の終着点": ["운명의 종착점"],
    "アラン": ["아란", "알란"],
    "アラン・スコーピオン": ["아란 스코피온", "아란 스콜피온", "알란 스코피온", "알란 스콜피온"],
    "パサジール": ["파사지르"],
}

for jp, variants in TERMS.items():
    hits = []
    counts = collections.Counter()
    for raw in glob.glob("work/final_qa/output/masters/*.json"):
        key = raw.split("scenario_")[-1].split(".master")[0]
        if key not in ROOT:
            continue
        data = json.load(open(raw, encoding="utf-8-sig"))
        for entry in data["entries"]:
            if jp not in entry["source_jp"]:
                continue
            found = [v for v in variants if v in entry["draft_ko"]]
            counts.update(found or ["<none>"])
            hits.append((key, entry["sequence"], entry["stable_id"], found, entry["source_jp"], entry["draft_ko"]))
    print(f"\n## {jp}: {len(hits)}")
    print(dict(counts))
    for item in hits:
        if not item[3] or item[3] != [variants[0]]:
            print(item)
