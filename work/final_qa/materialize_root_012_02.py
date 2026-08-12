#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MASTER = ROOT / "output" / "masters" / "scenario_012_02.master.json"
SEEDS = ROOT / "reviews" / "ROOT.corrections.jsonl"
OUT = ROOT / "reviews" / "ROOT.012_02.consolidated.corrections.jsonl"
REPORT = ROOT / "reviews" / "ROOT.012_02.consolidated.report.json"

MANUAL: dict[int, tuple[str, str, str]] = {
    15: ("「여신마저 구한다, 인가. 생각해 본 적도 없군」", "문법", "女神さえ救う、か의 인용·반추 호흡을 자연스럽게 복원"),
    18: ("「불길 속에서도 의연하구나…… 네 어머니가 네게 지어 준 이름 그대로야」", "어휘/이름 의미", "凛としている는 단순히 늠름한 외양이 아니라 의연한 태도"),
    29: ("「허허. 너는 정말 터무니없을 만큼 착한 사람이로구나. 언젠가 후회할지도 모르지만, 지금은 아니겠지」", "명백한 직역", "お人好し의 성격 의미를 낯선 한자어 호인 대신 자연스럽게 복원"),
    45: ("「……그런가 했는데, 아닌 모양이네. 넌 살아갈 의지가 넘치잖아」", "문법/의미", "生きる気マンマン의 강한 생존 의지를 자연스럽게 복원"),
    46: ("「하핫, 그거 좋네. 그게……」", "감탄사", "かかっ를 가나 음차가 아닌 일본어 웃음소리의 한국어 표현으로 직접 번역"),
    67: ("「굳이 말하자면, 적어도 네 친구들만은 구하는 게 좋겠군」", "조사/말투", "友人たちくらい의 최소 범위 강조와 아란의 말투 복원"),
    77: ("「이 세계에 축적된 힘은 세계 밖으로 흘러나온 여러분의 마음 조각들」", "명백한 직역", "世界から零れ落ちた를 흘러넘쳐 떨어졌다고 중복 번역한 표현 교정"),
    78: ("「각자 인격은 없고, 그저 {rb}마음{/rb}{rt}꿈{/rt}일 뿐입니다. 하지만」", "문법/중복", "人格を持たない、ただの想い의 문장 구조와 강조를 자연스럽게 복원; ruby 보존"),
    99: ("잔뜩 일그러진 얼굴이 문득 미소로 바뀐다.", "의미/첨가", "しわくちゃになった顔에 원문에 없는 눈물 원인을 단정한 표현 제거"),
    103: ("아니, 그걸 하찮다고 할 수는 없어.", "문법/의미", "ちっぽけなんてあるもんか의 강한 자기부정을 자연스럽게 복원"),
    115: ("아침인데도 무척 더워 나는 땀을 흘리고 있었다.", "명백한 직역", "朝はすっかり暑く의 부자연스러운 부사 결합 교정"),
    129: ("서서히 솟아오르던 실감은 시선이 쿠션 위로 옮겨 가는 순간 멎었다.", "문법/주어", "湧いてくる実感과 시선 이동·중단의 관계를 자연스럽게 복원"),
    143: ("털썩 주저앉는 바람에 눈물방울이 흘러내렸다.", "명백한 직역", "座った勢いで를 앉는 기세라고 한 직역 교정"),
    168: ("조금 전 일인데도 너무 많은 일이 몰아쳐서, 이제 뭐가 뭔지 모르겠다.", "명백한 직역", "密度が高過ぎて가 짧은 시간에 사건이 몰아친다는 의미임을 자연스럽게 복원"),
    178: ("실은 데려오고 싶었지만 이곳에는 데려올 수 없었고, 우리는 반드시 이곳에 와야 했다.", "문법/의미", "この場所はそうもいかない와 来なければいけない의 목적어·당위 관계 복원"),
    193: ("「그런 의미에서는 우리와 똑같네. 우리는 아직도 자신이 죽었던 기억을 품고 있어」", "문법", "自分の死の記憶의 한국어 관형 관계를 자연스럽게 복원"),
    198: ("그저 작은 주문 같은 행동일 뿐이다.", "오역", "おまじない는 물건인 부적이 아니라 소원을 비는 주문·행위"),
    199: ("수많은 사람이 마음을 내게 맡겼다.", "조사/의미", "想いを託された의 맡긴 주체와 수탁 관계를 명확하게 복원"),
    201: ("지금의 나는 모두 덕분에 살아 있다. 존재한다. 나로서 서 있다.", "명백한 직역", "成り立っている의 존재가 성립·유지된다는 의미를 한국어로 자연스럽게 복원"),
    204: ("이토록 눈부신 세계가 격동의 12주를 마친 보상이라면 조금 아쉽다.", "문법/의미", "12週間を終えた와 物足りない의 자연스러운 한국어 결합"),
}

FW_TRANS = str.maketrans("０１２３４５６７８９％", "0123456789%")
ROMAN_RE = re.compile(r"[\u2160-\u2188]+")
TAG_RE = re.compile(r"\{[^{}]+\}|\[[^\[\]]+\]")
KANA_RE = re.compile(r"[ぁ-ゖゝ-ゟァ-ヺヽヾㇰ-ㇿｦ-ﾟ]")


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def quote_skeleton(text: str) -> list[str]:
    return [ch for ch in text if ch in "「」『』≪≫"]


def explicit_numbers(text: str) -> list[str]:
    return re.findall(r"\d+(?:\.\d+)?", text.translate(FW_TRANS))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    master_doc = json.loads(MASTER.read_text(encoding="utf-8-sig"))
    entries = master_doc["entries"]
    by_seq = {int(e["sequence"]): e for e in entries}
    assert len(entries) == 209 and set(by_seq) == set(range(1, 210))
    by_stable = {e["stable_id"]: e for e in entries}

    seed_rows = [r for r in load_jsonl(SEEDS) if r.get("script") == "012_02"]
    assert len(seed_rows) == 3
    for row in seed_rows:
        e = by_stable[row["stable_id"]]
        assert row["old_ko"] == e["draft_ko"]
        assert int(row["sequence"]) == int(e["sequence"])

    selected: dict[int, dict] = {int(r["sequence"]): dict(r) for r in seed_rows}
    overlap = []
    for sequence, (new_ko, category, reason) in MANUAL.items():
        e = by_seq[sequence]
        if sequence in selected:
            overlap.append(sequence)
        selected[sequence] = {
            "script": "012_02",
            "stable_id": e["stable_id"],
            "sequence": sequence,
            "old_ko": e["draft_ko"],
            "new_ko": new_ko,
            "category": category,
            "reason": reason,
            "reviewer": "ROOT",
            "source_jp": e["source_jp"],
        }

    rows = [selected[k] for k in sorted(selected)]
    assert len({r["stable_id"] for r in rows}) == len(rows)
    checks = Counter()
    failures = []
    for row in rows:
        e = by_seq[int(row["sequence"])]
        old, new, source = e["draft_ko"], row["new_ko"], e["source_jp"]
        values = {
            "old_guard": row["old_ko"] == old,
            "changed": new != old,
            "encoding": "\ufffd" not in new and not any(0x80 <= ord(c) <= 0x9F for c in new),
            "fullwidth_clear": not re.search(r"[０-９]", new) and "\u3000" not in new,
            "tag_exact": Counter(TAG_RE.findall(source)) == Counter(TAG_RE.findall(new)),
            "roman_exact": ROMAN_RE.findall(source) == ROMAN_RE.findall(new),
            "quote_exact": quote_skeleton(source) == quote_skeleton(new),
            "newline_exact": source.count("\n") == new.count("\n"),
            "numbers_exact": explicit_numbers(source) == explicit_numbers(new),
            "residual_kana_clear": KANA_RE.search(new) is None,
        }
        for key, passed in values.items():
            checks[key] += passed
        if not all(values.values()):
            failures.append({"sequence": row["sequence"], "bad": [k for k, v in values.items() if not v]})
    assert not failures, failures

    OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    report = {
        "schema_version": "fatal-twelve-root-consolidated-review-v1",
        "script": "012_02",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "exhaustive_checked": 209,
        "manual_corrections": len(MANUAL),
        "seed_corrections": len(seed_rows),
        "seed_manual_overlap_sequences": overlap,
        "output_unique_corrections": len(rows),
        "checks": dict(checks),
        "failures": failures,
        "master_sha256": sha(MASTER),
        "seed_sha256": sha(SEEDS),
        "output_sha256": sha(OUT),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
