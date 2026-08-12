#!/usr/bin/env python3
"""Generate deterministic ROOT-review candidates from Japanese/Korean masters.

This does not modify translations.  It applies the already-recorded guarded seed
corrections in memory, then emits high-recall candidates for the human/model QA
pass.  English localization resources are never opened.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


BASE = Path(__file__).resolve().parent
MASTER_DIR = BASE / "output" / "masters"
REVIEWS = BASE / "reviews"
OUT = BASE / "output" / "root_semantic_candidates.tsv"
ROOT_SCRIPTS = [
    "009",
    "010",
    "011_02",
    "011_02GH",
    "012_01F",
    "012_01GH",
    "012_02",
]

ENTITY_TERMS = {
    "凛火": "린카",
    "海晴": "미하루",
    "直未": "나오미",
    "真央": "마오",
    "パルカ": "파르카",
    "ソーニャ": "소냐",
    "アラン": "아란",
    "スコーピオン": "스코피온",
    "フェデリーコ": "페데리코",
    "オデット": "오데트",
    "ダイアナ": "다이아나",
    "スケール": "스케일",
    "アムリタ": "암리타",
    "リンダ": "린다",
    "ユウ": "유우",
    "ゲイコ": "게이코",
    "桂子": "게이코",
    "茂継": "시게쓰구",
    "チャンホ": "창호",
    "レーテ": "레테",
}

ENTITY_ALIASES = {
    "린카": ("凛火", "リンカ"),
    "미하루": ("海晴", "ミハル"),
    "나오미": ("直未", "ナオミ"),
    "마오": ("真央", "マオ"),
    "파르카": ("パルカ",),
    "소냐": ("ソーニャ",),
    "아란": ("アラン",),
    "페데리코": ("フェデリーコ",),
    "오데트": ("オデット",),
    "다이아나": ("ダイアナ",),
    "스케일": ("スケール",),
    "암리타": ("アムリタ",),
    "린다": ("リンダ",),
    "유우": ("ユウ",),
    "게이코": ("ゲイコ", "桂子"),
    "시게쓰구": ("茂継",),
    "창호": ("チャンホ",),
    "레테": ("レーテ", "レテ"),
}

CANONICAL_TERMS = {
    "女神の選定": "여신의 선정",
    "運命の終着点": "운명의 종착점",
    "運命の大広間": "운명의 대회랑",
    "運命の広間": "운명의 대회랑",
    "夢の世界": "꿈의 세계",
    "パサジール": "파사지르",
}

BAD_VARIANTS = {
    "알란": "아란",
    "스콜피온": "스코피온",
    "다이애나": "다이아나",
    "운명의 대광장": "운명의 대회랑",
    "운명의 대전당": "운명의 대회랑",
    "운명의 대회관": "운명의 대회랑",
    "꿈속 세상": "꿈의 세계",
    "꿈속 세계": "꿈의 세계",
    "꿈의 세상": "꿈의 세계",
    "린카링": "리땅",
}

JP_RE = re.compile(r"[\u3041-\u3096\u30a1-\u30fa\u30fc\u3005\u4e00-\u9fff]")
HANGUL_RE = re.compile(r"[가-힣]")
LATIN_WORD_RE = re.compile(r"(?<![A-Za-z])[A-Za-z]{3,}(?![A-Za-z])")
FULLWIDTH_RE = re.compile(r"[０-９　]")
NUM_RE = re.compile(r"[0-9０-９ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]+")


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def normalize_num(s: str) -> str:
    return s.translate(str.maketrans("０１２３４５６７８９", "0123456789"))


def load_seed() -> dict[tuple[str, str], str]:
    out: dict[tuple[str, str], str] = {}
    for p in sorted(REVIEWS.glob("ROOT*.corrections.jsonl")):
        for line in p.read_text(encoding="utf-8-sig").splitlines():
            if not line.strip():
                continue
            x = json.loads(line)
            key = (str(x["script"]), x["stable_id"])
            previous = out.get(key)
            if previous is not None and previous != x["new_ko"]:
                raise SystemExit(f"conflicting ROOT correction: {key}")
            out[key] = x["new_ko"]
    return out


def emit(rows: list[dict], e: dict, ko: str, category: str, detail: str) -> None:
    rows.append(
        {
            "script": e["script_key"],
            "sequence": e["sequence"],
            "stable_id": e["stable_id"],
            "source_line": e["source_line"],
            "lane": e["lane"],
            "speaker": e.get("speaker") or "",
            "category": category,
            "detail": detail,
            "source_jp": e["source_jp"],
            "current_ko": ko,
            "current_ko_sha256": sha(ko),
        }
    )


def main() -> None:
    seed = load_seed()
    entries: list[dict] = []
    by_script: dict[str, list[dict]] = {}
    for script in ROOT_SCRIPTS:
        p = MASTER_DIR / f"scenario_{script}.master.json"
        d = json.loads(p.read_text(encoding="utf-8"))
        chunk = d["entries"]
        for e in chunk:
            e = dict(e)
            e["script_key"] = script
            e["current_ko"] = seed.get((script, e["stable_id"]), e["draft_ko"])
            entries.append(e)
        by_script[script] = chunk

    findings: list[dict] = []
    for e in entries:
        jp, ko = e["source_jp"], e["current_ko"]

        for bad, good in BAD_VARIANTS.items():
            if bad in ko:
                emit(findings, e, ko, "bad_variant", f"{bad} -> {good}")

        for src, dst in CANONICAL_TERMS.items():
            if src in jp and dst not in ko:
                emit(findings, e, ko, "term_missing", f"{src} -> {dst}")

        # Entity omission is high recall: Korean can naturally omit a repeated
        # subject, so this is review-only rather than an automatic correction.
        for src, dst in ENTITY_TERMS.items():
            if src in jp and dst not in ko:
                emit(findings, e, ko, "entity_missing", f"{src} -> {dst}")

        jp_entities = {
            dst for dst, aliases in ENTITY_ALIASES.items()
            if any(alias in jp for alias in aliases)
        }
        ko_entities = {
            dst for dst in ENTITY_ALIASES
            if re.search(rf"(?<![가-힣]){re.escape(dst)}", ko)
        }
        if jp_entities and ko_entities and jp_entities != ko_entities:
            emit(
                findings,
                e,
                ko,
                "entity_set_mismatch",
                f"jp={sorted(jp_entities)} ko={sorted(ko_entities)}",
            )

        if FULLWIDTH_RE.search(ko):
            emit(findings, e, ko, "fullwidth_target", repr(FULLWIDTH_RE.findall(ko)))

        residual = sorted(set(JP_RE.findall(ko)))
        if residual:
            emit(findings, e, ko, "residual_japanese", "".join(residual))

        latin = LATIN_WORD_RE.findall(ko)
        if latin:
            emit(findings, e, ko, "latin_word", ",".join(latin))

        # Dialogue/choice quote conventions.
        if e["lane"] in {"dialogue", "spoken_choice", "dialogue_choice_prompt"}:
            if not (ko.startswith("「") and (ko.endswith("」") or ko.endswith("」:"))):
                emit(findings, e, ko, "dialogue_quote", "expected Japanese corner brackets")
        if ko.count("「") != ko.count("」"):
            emit(findings, e, ko, "unbalanced_quote", f"open={ko.count('「')} close={ko.count('」')}")

        if "？" in jp and "?" not in ko and "？" not in ko:
            emit(findings, e, ko, "question_punctuation", "source has a question mark; target does not")

        jp_negative = bool(re.search(r"(?:ない|なかった|なく|ません|ぬ|ず|じゃない|ではない)", jp))
        ko_negative = bool(re.search(r"(?:안 |않|못 |없|아니|말[고라]|못하|지 못)", ko))
        if jp_negative and not ko_negative:
            emit(findings, e, ko, "negation_candidate", "Japanese negation has no obvious Korean negation marker")

        # Normalized numeric value mismatch.  This remains review-only because
        # counters can be lexicalized in Korean.
        jnums = Counter(normalize_num(x) for x in NUM_RE.findall(jp))
        knums = Counter(normalize_num(x) for x in NUM_RE.findall(ko))
        if jnums != knums:
            emit(findings, e, ko, "number_mismatch", f"jp={dict(jnums)} ko={dict(knums)}")

        # Extreme compression/expansion is useful for spotting omissions and
        # accidental duplicated clauses.  Ignore punctuation for the ratio.
        jlen = len(re.sub(r"[\s\W_]+", "", jp, flags=re.UNICODE))
        klen = len(re.sub(r"[\s\W_]+", "", ko, flags=re.UNICODE))
        if jlen >= 12 and (klen / max(jlen, 1) < 0.32 or klen / jlen > 1.45):
            emit(findings, e, ko, "extreme_length", f"jp_chars={jlen} ko_chars={klen} ratio={klen/jlen:.2f}")

        # Obvious punctuation/lane anomalies.
        if e["lane"] == "narration" and jp.endswith("。") and not re.search(r"[.!?」…―]$", ko):
            emit(findings, e, ko, "terminal_punctuation", "JP sentence ends with 。 but KO has no terminal punctuation")

        # Repeated Korean word/short phrase, excluding intentional stammering.
        m = re.search(r"(?<![가-힣])([가-힣]{2,8})(?:\s+|,\s*)\1(?![가-힣])", ko)
        if m:
            emit(findings, e, ko, "repetition", m.group(0))

    # Exact same target for multiple distinct Japanese sources can expose a
    # copied/misaligned line.  Report only targets of meaningful length.
    grouped: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        if len(e["current_ko"]) >= 14:
            grouped[e["current_ko"]].append(e)
    for ko, group in grouped.items():
        sources = {e["source_jp"] for e in group}
        if len(group) > 1 and len(sources) > 1:
            for e in group:
                emit(findings, e, ko, "duplicate_target", f"{len(group)} entries / {len(sources)} distinct JP sources")

    fields = [
        "script", "sequence", "stable_id", "source_line", "lane", "speaker",
        "category", "detail", "source_jp", "current_ko", "current_ko_sha256",
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(sorted(findings, key=lambda x: (x["script"], int(x["sequence"]), x["category"])))

    summary = {
        "schema_version": "fatal-twelve-root-semantic-candidates-v1",
        "root_scripts": ROOT_SCRIPTS,
        "entry_count": len(entries),
        "seed_correction_count": len(seed),
        "finding_count": len(findings),
        "category_counts": dict(sorted(Counter(x["category"] for x in findings).items())),
        "output": str(OUT),
        "output_sha256": hashlib.sha256(OUT.read_bytes()).hexdigest(),
        "translation_modified": False,
        "english_reference_used": False,
    }
    (OUT.with_suffix(".summary.json")).write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
