#!/usr/bin/env python3
"""Create deterministic ROOT-review corrections from the frozen glossary.

This is part of the single consolidated QA pass.  It only touches the ROOT
reviewer's assigned scripts and writes guarded JSONL; masters remain unchanged.
"""

import glob
import json
from pathlib import Path

ROOT = {"009", "010", "011_02", "011_02GH", "012_01F", "012_01GH", "012_02"}
OUT = Path("work/final_qa/reviews/ROOT.corrections.jsonl")

digit_map = str.maketrans("０１２３４５６７８９", "0123456789")


def fix(entry):
    source = entry["source_jp"]
    old = entry["draft_ko"]
    new = old
    reasons = []

    def replace_if(source_token, old_token, new_token, reason):
        nonlocal new
        if source_token in source and old_token in new:
            new = new.replace(old_token, new_token)
            reasons.append(reason)

    replace_if("アラン", "알란", "아란", "glossary: アラン=아란")
    replace_if("スコーピオン", "스콜피온", "스코피온", "glossary: スコーピオン=스코피온")
    for variant in ("운명의 대광장", "운명의 대전당", "운명의 대회관"):
        replace_if("運命の大広間", variant, "운명의 대회랑", "glossary: 運命の大広間=운명의 대회랑")
    for variant in ("꿈속 세상", "꿈속 세계", "꿈의 세상"):
        replace_if("夢の世界", variant, "꿈의 세계", "glossary: 夢の世界=꿈의 세계")
    # The canonical term ends in a vowel. Repair particles left behind by a
    # consonant-final draft variant, including the title-bracket form.
    if "夢の世界" in source and "꿈의 세계" in new:
        particle_pairs = (
            ("꿈의 세계≫으로", "꿈의 세계≫로"),
            ("꿈의 세계≫은", "꿈의 세계≫는"),
            ("꿈의 세계≫이", "꿈의 세계≫가"),
            ("꿈의 세계≫을", "꿈의 세계≫를"),
            ("꿈의 세계≫과", "꿈의 세계≫와"),
            ("꿈의 세계으로", "꿈의 세계로"),
            ("꿈의 세계은", "꿈의 세계는"),
            ("꿈의 세계이", "꿈의 세계가"),
            ("꿈의 세계을", "꿈의 세계를"),
            ("꿈의 세계과", "꿈의 세계와"),
        )
        for bad, good in particle_pairs:
            if bad in new:
                new = new.replace(bad, good)
                reasons.append("glossary replacement particle agreement: 세계")
    replace_if("りーたん", "린카링", "리땅", "glossary nickname: りーたん=리땅")
    replace_if("ダイアナ", "다이애나", "다이아나", "glossary: ダイアナ=다이아나")

    digit_fixed = new.translate(digit_map)
    if digit_fixed != new:
        new = digit_fixed
        reasons.append("한국어 문장 안 전각 숫자를 의미가 같은 반각 숫자로 정규화")
    if "\u3000" in new:
        new = new.replace("\u3000", " ")
        reasons.append("한국어 문장 안 전각 공백을 일반 공백으로 정규화")

    if new == old:
        return None
    category = "term" if any(r.startswith("glossary") for r in reasons) else "typography"
    return {
        "script": entry["source_file"].split("/")[-1].removesuffix(".rpy"),
        "stable_id": entry["stable_id"],
        "sequence": entry["sequence"],
        "old_ko": old,
        "new_ko": new,
        "category": category,
        "reason": "; ".join(dict.fromkeys(reasons)),
        "reviewer": "ROOT",
        "source_jp": source,
    }


def main():
    corrections = []
    for raw in sorted(glob.glob("work/final_qa/output/masters/*.json")):
        key = raw.split("scenario_")[-1].split(".master")[0]
        if key not in ROOT:
            continue
        data = json.load(open(raw, encoding="utf-8-sig"))
        for entry in data["entries"]:
            item = fix(entry)
            if item:
                corrections.append(item)
    ids = [x["stable_id"] for x in corrections]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate stable_id in generated corrections")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in corrections), encoding="utf-8")
    print(json.dumps({"corrections": len(corrections), "output": str(OUT)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
