from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parent
MASTER_PATHS = {
    "011_02": BASE / "output" / "masters" / "scenario_011_02.master.json",
    "011_02GH": BASE / "output" / "masters" / "scenario_011_02GH.master.json",
}
SEED_PATH = BASE / "reviews" / "ROOT.corrections.jsonl"
CONSOLIDATED_009_PATH = BASE / "reviews" / "ROOT.009.consolidated.corrections.jsonl"
OUTPUT_PATH = BASE / "reviews" / "ROOT.manual.011_02_and_GH.corrections.jsonl"
REPORT_PATH = BASE / "reviews" / "ROOT.manual.011_02_and_GH.report.json"


# 일본어 source_jp만 의미 기준으로 삼아 확정한 수동 교정이다.
# tuple: (sequence, new_ko, category, reason)
DECISIONS = {
    "011_02": [
        (18, "1년을 12개월로 나눈 달력을 비롯해 시계 문자판과 십이지, 황도 십이궁에 이르기까지, 일본뿐 아니라 전 세계에서 하나의 단위로 인정받는 숫자다.", "의미/문법", "暦와 １年を12に分けた의 관계 및 나열 구조 교정"),
        (20, "1부터 차례로 세어 도달한 열두 번째. 우연이라기에는 확실히 절묘하다.", "명백한 직역", "数を重ねた를 횟수를 쌓았다고 옮긴 표현 교정"),
        (23, "나는 여신의 말을 듣고 한 가지 걸리는 점이 생겼다.", "문법/자연스러움", "引っかかることがあった의 자연스러운 내면 서술 복원"),
        (36, "「도발해 봤자 소용없어. 나도 지명하지 않겠어」", "의미/자연스러움", "挑発したところで何もない의 결과 없음 의미를 자연스럽게 복원"),
        (53, "이런 상황이라면 나라도 쉽게 그렇게 예상할 수 있다.", "문법", "容易い의 가능 표현과 부사 위치 교정"),
        (89, "빵 이야기로 치면 내가 빵을 먹고 싶다고 생각했으니, 빵을 먹은 세계 쪽이 실현될 가능성이 더 큰 건 당연하겠지.", "문법/의미", "세계 자체의 가능성이 높다는 직역을 실현 가능성으로 명확화"),
        (90, "「이야기가 옆길로 새 버렸군요」", "명백한 직역", "話が逸れる의 관용 표현 복원"),
        (94, "「지금 본류 세계에는 ≪우리가 목숨을 잃은 세계≫와 ≪우리가 목숨을 잃지 않은 세계≫가 동시에 존재한다는 뜻이야?」", "조사/문법", "ぼくたちが가 두 세계를 수식하는 병렬 관계와 조사를 교정"),
        (96, "「≪운명의 대회랑≫은 본래 세계에 있어서는 이물질이나 다름없습니다. 하지만 이곳에서의 인지가 본류 세계에 영향을 미친다고 생각하셔도 좋습니다」", "조사/의미", "世界にとって를 장소 표현으로 옮긴 조사를 관점 표현으로 교정"),
        (115, "「선정 참가자가 탈락하면, ≪죽음이 없던 일이 된 세계≫는 어떻게 되는 거야?」", "문법/의미", "死がなかったことになっている의 없던 일이 된다는 의미와 문장 구조 교정"),
        (125, "파르카는 대화를 끊고 그대로 평소처럼 선정 종료를 선언했다.", "문법/자연스러움", "選定を終える宣言의 부자연스러운 명사 수식 교정"),
    ],
    "011_02GH": [
        (5, "「이번에는 두 분 모두 지명하지 않으실 줄로만 알았습니다만」", "강조 누락", "확신에 찬 추측을 나타내는 てっきり의 강조 복원"),
        (23, "그러니 시도해 보는 것이다.", "어휘/의미", "계획을 실제로 실행해 본다는 문맥의 試す를 자연스럽게 복원"),
        (29, "「어머. 저는 여신이라고요? 당신 같은 인간의 감각으로 저를 비교하다니 너무 경솔합니다」", "명백한 직역/문법", "浅慮が過ぎる의 부자연스러운 직역과 비교 대상 누락 교정"),
        (41, "지금까지 지명할 때와 달리 나는 3가지 정보를 빠르게 말했다.", "typography+문법", "기존 전각 숫자 정규화를 반영하고 早口で口にした의 부자연스러운 표현을 교정"),
        (49, "그 뜻을 알아 버렸기에, 머릿속이 새하얘지지 않도록 필사적으로 버티고 있었다.", "문법/명백한 직역", "頭が真っ白になりそうなところ를 억제하는 동작 관계를 자연스럽게 복원"),
        (58, "「또 네게 거짓말을 해 버렸네. 생각해 보면 난 린카에게 거짓말을 하거나 비밀을 감추기만 했어」", "의미/문법", "嘘や隠し事をしてばかりだった의 병렬 동작과 문법 복원"),
        (65, "「미하루, 말했잖아. 자신을 용서할 수 있었다고……」", "호칭/문법", "海晴가 주어가 아니라 상대를 부르는 호격임을 복원"),
        (70, "「틀리지 않아. 나는 린카를――사랑하니까」", "문법/자연스러움", "違わないよ를 부자연스러운 이중 부정 없이 복원"),
        (72, "「고마워. 린카가 나한테 그런 마음을 품고 있다는 건 티가 다 났어. 그래서 난 만족할 수 있었어」", "의미/문법", "想ってくれた의 연애 감정과 문장 구조 복원"),
        (86, "「너와 특별한 관계로 지낸 3일. 이별이 머지않았다고 생각하니, 그 시간은 무척 짙고 충만했어」", "typography+문법", "기존 전각 숫자 정규화를 반영하고 관계·이별 시점 및 濃密な時間의 직역을 교정"),
        (91, "「괜찮아, 린카. 선정이 시작된 뒤 약 3개월 동안 살아온 나에 대한 기억은 너한테만 남아. 린카만 아는 내가 있어. 그것을 상상하는 것만으로도 무척 행복해」", "typography+의미", "기존 전각 숫자 정규화를 반영하고 ぼくの記憶가 린카에게 남는 대상 관계를 명확화"),
        (93, "3장의 카드는 한 번도 멈추지 않고 움직여 운명의 대회랑 중심에서 멈췄다.", "typography+문법", "기존 전각 숫자 정규화를 반영하고 止まることなく停止した의 이동·정지 관계를 자연화"),
        (95, "「꿈의 세계라니, 참 잘 붙인 이름이야. 내가 오늘까지 살아온 나날은 정말 꿈만 같아」", "의미/자연스러움", "夢の世界とはよく言ったものだ의 명칭이 절묘하다는 비반어적 감탄 복원"),
        (100, "미하루가 탈락해 가는 것, 본래 죽음의 운명으로 돌아가는 것은――막을 수 없다.", "문법/의미", "동일 사건을 설명하는 두 구절의 목적격 중복과 止められない의 동사 교정"),
        (107, "그리고 내 의식은 혼탁함 속으로 떨어져 간다.", "의미", "混濁에 원문에 없는 어둠을 덧붙인 표현 교정"),
        (169, "「그 가운데서 운명의 노예인 12명 모두가 ≪죽지 않은 것≫으로 되어 있는 세계를 찾아, 실을 잣듯 묶는 것입니다」", "의미/문법", "死ななかったことになっている의 의미와 12人の皆サマ의 어색한 배열 교정"),
        (174, "왜 우리에게 잠깐의 희망이 주어졌는지. 세계라는 게 뒤집힐 가능성은 아직 남아 있는지.", "의미/태", "世界ってやつが覆る의 주체가 세계인데 타동 구조로 바뀐 오류 교정"),
        (180, "「≪시시마이 린카는 죽어 있다≫는데도 ≪시시마이 린카가 살아 있다≫는 모순」", "문법/의미", "死んでいるのに의 상태와 역접 관계 복원"),
        (183, "「그러면 ≪미하루가 살아 있는≫ 지류도 존재하는 거지? 미하루도 나도 살아 있을 가능성이! 지금이라도 그 세계로 바꿀 수 없어?」", "문법", "사람의 생존 가능성을 나타내는 서술형 교정"),
        (189, "「미하루는 예전에 당신의 ≪그릇≫이었지? 꿈속에서 이야기도 나눴다고 했어. 동정이나 친근감 같은 건 없어?」", "의미", "元の≪器≫를 본래가 아닌 이전의 그릇이라는 뜻으로 복원"),
        (199, "「우리는 대체 무엇{rt}・{/rt}을 하도록 강요당한 거야?」", "의미/문법", "何をさせられてた의 무엇을 하도록이라는 동작을 복원하고 standalone {rt}를 보존"),
        (209, "빛은 한데 수렴하며 여신 파르카에게로 모여들었다.", "어휘/중복", "集束して와 集まって를 모두 모이다로 반복한 표현 교정"),
        (212, "「세계에서 밀려난 마음이라는 조각은 이 ≪운명의 대회랑≫에 {rb}개념{/rb}{rt}꿈{/rt}이 되어 수용됩니다――그러므로 여러분은 ≪운명의 노예≫」", "어휘/의미", "문맥상 あぶれてしまった가 세계에서 배제되어 남겨진 상태임을 복원하고 Ruby 보존"),
        (237, "하지만 감긴 눈꺼풀 뒤로 수많은 꿈이 떠올랐다.", "문법/자연스러움", "눈을 감은 눈꺼풀이라는 잘못된 수식 관계 교정"),
        (239, "내게 아이를 향한 마음을 맡긴 게이코 씨. 분명 남편과는 마음 깊은 곳에서 서로 통했기에 편지 같은 건 필요 없었고, 아이에게는 게이코 씨가 정한 것과 같은 이름이 붙었을 것이다.", "명백한 직역/의미", "深いところでは通じていた의 내면 깊은 곳에서 서로 통했다는 의미 복원"),
        (241, "하지만 파사지르에게는 더 다양한 세계를 제대로 보여 줄게.", "문법/중복", "もっと色々な世界를 더 많은 여러로 중복 수식한 표현 교정"),
        (253, "그렇기에 내게는 내 의지로 그를 탈락시키겠다는 답밖에 없었다.", "어휘/문법", "선택과 결론을 뜻하는 答え에 대답을 쓴 표현 교정"),
        (256, "그에게 무슨 일이 있었는지 자세히는 모르지만, 그의 삶은 틀림없이 충만해졌을 것이다.", "명백한 직역/문법", "充実したものになったに違いない의 부자연스러운 명사화와 추정 표현 교정"),
        (270, "「유감, 스럽지만. 그것은 불가능합니다」", "연출/구두점", "残念、ながら의 의도적인 단어 내부 단절 연출 복원"),
        (278, "「당신의 몸은 제가 취하겠습니다」", "어휘/의미", "강제로 육체를 차지하는 문맥의 いただきます를 복원"),
        (290, "「그러니 당신의 {rb}육체{/rb}{rt}몸{/rt}도 {rb}정신{/rb}{rt}마음{/rt}도 저와 {rb}동질{/rb}{rt}같음{/rt}입니다. 다른 분들에게는 불가능했던 진정한 기적을 이제 보여 드리지요」", "호칭/문법", "他の皆サマ를 다른 여러분이라고 옮긴 어색한 호칭 교정 및 Ruby 보존"),
        (292, "내장이 직접 휘저어진다면 분명 이런 감각일 것이다.", "의미/태", "かき回される의 피동이 능동으로 바뀐 오류 교정"),
        (297, "「당신을 취해, 저는 현실 세계의 주민이 되겠습니다」", "어휘/의미", "육체와 존재를 차지하는 いただいて의 의미 복원"),
        (304, "그래서 마음이 잠식되고 있음을 자각하면서도, 나는 그렇게 외칠 수 있었다.", "접속어 누락/문법", "앞 문장과의 인과를 나타내는 だから를 복원"),
        (321, "「저는 당신을 취해, 현실 세계의 주민이 되는 것입니다」", "어휘/의미", "육체와 존재를 차지하는 いただいて 용례 통일"),
        (323, "그것을――증명하는――것처럼――.", "연출/구두점", "それを――証明する――ように――의 세 단계 단절 연출 복원"),
        (324, "내――저는 곧――의식은 이제――당신의 몸을――취하겠습――사라져 가――니다.", "어휘/의미", "교차 삽입된 頂戴いたします의 육체 강탈 의미와 대시 배열 보존"),
    ],
}


EXPECTED_COUNTS = {"011_02": 131, "011_02GH": 325}
ROMAN_RE = re.compile(r"[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]")
NUM_RE = re.compile(r"[0-9０-９]+")
TAG_RE = re.compile(r"\{[^{}\n]*\}|\[[^\[\]\n]*\]")
RUBY_TAG_RE = re.compile(r"\{/?(?:rb|rt)\}")
QUOTE_CHARS = "「」『』≪≫“”‘’\""
FW_TRANS = str.maketrans("０１２３４５６７８９", "0123456789")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
        newline="\n",
    )


def normalized_numbers(text: str) -> Counter:
    return Counter(value.translate(FW_TRANS) for value in NUM_RE.findall(text))


def counter_dict(counter: Counter) -> dict:
    return dict(sorted(counter.items()))


def validate_record(entry: dict, row: dict) -> dict:
    old_text = row["old_ko"]
    new_text = row["new_ko"]
    protected_differences = []
    for token in entry.get("protected_tokens") or []:
        if isinstance(token, dict):
            if token.get("kind") == "number":
                continue
            value = token.get("value")
        else:
            value = token
        if value and old_text.count(value) != new_text.count(value):
            protected_differences.append({
                "token": value,
                "old_count": old_text.count(value),
                "new_count": new_text.count(value),
            })

    old_numbers = normalized_numbers(old_text)
    new_numbers = normalized_numbers(new_text)
    old_roman = Counter(ROMAN_RE.findall(old_text))
    new_roman = Counter(ROMAN_RE.findall(new_text))
    old_quotes = Counter(ch for ch in old_text if ch in QUOTE_CHARS)
    new_quotes = Counter(ch for ch in new_text if ch in QUOTE_CHARS)
    old_tags = Counter(TAG_RE.findall(old_text))
    new_tags = Counter(TAG_RE.findall(new_text))
    old_ruby = Counter(RUBY_TAG_RE.findall(old_text))
    new_ruby = Counter(RUBY_TAG_RE.findall(new_text))
    checks = {
        "exact_old_guard_pass": entry["draft_ko"] == old_text,
        "protected_tokens_pass": not protected_differences,
        "numbers_pass": old_numbers == new_numbers,
        "roman_numerals_pass": old_roman == new_roman,
        "quotes_pass": old_quotes == new_quotes,
        "renpy_tags_pass": old_tags == new_tags,
        "ruby_tags_pass": old_ruby == new_ruby,
        "newlines_pass": old_text.count("\n") == new_text.count("\n"),
    }
    return {
        "script": row["script"],
        "sequence": row["sequence"],
        "stable_id": row["stable_id"],
        **checks,
        "pass": all(checks.values()),
        "protected_token_differences": protected_differences,
        "old_numbers_normalized": counter_dict(old_numbers),
        "new_numbers_normalized": counter_dict(new_numbers),
        "old_roman": counter_dict(old_roman),
        "new_roman": counter_dict(new_roman),
        "old_quotes": counter_dict(old_quotes),
        "new_quotes": counter_dict(new_quotes),
        "old_renpy_tags": counter_dict(old_tags),
        "new_renpy_tags": counter_dict(new_tags),
        "old_ruby_tags": counter_dict(old_ruby),
        "new_ruby_tags": counter_dict(new_ruby),
        "old_newline_count": old_text.count("\n"),
        "new_newline_count": new_text.count("\n"),
    }


def scope_structure_audit(entries: list[dict]) -> dict:
    checks = {
        "roman_numerals": lambda s: Counter(ROMAN_RE.findall(s)),
        "quotation_marks": lambda s: Counter(ch for ch in s if ch in QUOTE_CHARS),
        "renpy_tags": lambda s: Counter(TAG_RE.findall(s)),
        "ruby_tag_markers": lambda s: Counter(RUBY_TAG_RE.findall(s)),
        "newlines": lambda s: s.count("\n"),
    }
    result = {}
    for name, extractor in checks.items():
        failures = []
        for entry in entries:
            source_value = extractor(entry["source_jp"])
            draft_value = extractor(entry["draft_ko"])
            if source_value != draft_value:
                failures.append({
                    "sequence": entry["sequence"],
                    "stable_id": entry["stable_id"],
                    "source": counter_dict(source_value) if isinstance(source_value, Counter) else source_value,
                    "draft": counter_dict(draft_value) if isinstance(draft_value, Counter) else draft_value,
                })
        result[name] = {
            "pass_count": len(entries) - len(failures),
            "failure_count": len(failures),
            "failures": failures,
        }
    ruby_records = []
    for entry in entries:
        source_ruby = Counter(RUBY_TAG_RE.findall(entry["source_jp"]))
        draft_ruby = Counter(RUBY_TAG_RE.findall(entry["draft_ko"]))
        if source_ruby or draft_ruby:
            ruby_records.append({
                "sequence": entry["sequence"],
                "stable_id": entry["stable_id"],
                "source_ruby_tags": counter_dict(source_ruby),
                "draft_ruby_tags": counter_dict(draft_ruby),
                "marker_pass": source_ruby == draft_ruby,
            })
    result["ruby_records_including_standalone_rt"] = ruby_records
    result["all_pass"] = all(item["failure_count"] == 0 for key, item in result.items() if key != "ruby_records_including_standalone_rt")
    return result


def main() -> None:
    master_hashes_before = {script: sha256(path) for script, path in MASTER_PATHS.items()}
    seed_hash_before = sha256(SEED_PATH)
    consolidated_hash_before = sha256(CONSOLIDATED_009_PATH)

    masters = {}
    entries_by_script = {}
    all_target_entries = []
    target_by_id = {}
    for script, path in MASTER_PATHS.items():
        master = json.loads(path.read_text(encoding="utf-8-sig"))
        if master.get("script_key") != script:
            raise SystemExit(f"script_key mismatch: {script}")
        entries = master["entries"]
        if len(entries) != EXPECTED_COUNTS[script]:
            raise SystemExit(f"entry count mismatch: {script} {len(entries)}")
        if [entry["sequence"] for entry in entries] != list(range(1, EXPECTED_COUNTS[script] + 1)):
            raise SystemExit(f"non-contiguous sequence: {script}")
        masters[script] = master
        entries_by_script[script] = {entry["sequence"]: entry for entry in entries}
        all_target_entries.extend(entries)
        for entry in entries:
            if entry["stable_id"] in target_by_id:
                raise SystemExit(f"duplicate target stable_id: {entry['stable_id']}")
            target_by_id[entry["stable_id"]] = (script, entry)

    rows = []
    for script, decisions in DECISIONS.items():
        sequences = [decision[0] for decision in decisions]
        if len(sequences) != len(set(sequences)):
            raise SystemExit(f"duplicate decision sequence: {script}")
        for sequence, new_ko, category, reason in decisions:
            entry = entries_by_script[script].get(sequence)
            if entry is None:
                raise SystemExit(f"missing sequence: {script} {sequence}")
            if entry["draft_ko"] == new_ko:
                raise SystemExit(f"no-op decision: {script} {sequence}")
            rows.append({
                "script": script,
                "stable_id": entry["stable_id"],
                "sequence": sequence,
                "old_ko": entry["draft_ko"],
                "new_ko": new_ko,
                "category": category,
                "reason": reason,
                "reviewer": "ROOT",
            })
    rows.sort(key=lambda row: (row["script"], row["sequence"], row["stable_id"]))
    if len(rows) != len({row["stable_id"] for row in rows}):
        raise SystemExit("duplicate stable_id in manual output")

    seed_rows = load_jsonl(SEED_PATH)
    consolidated_rows = load_jsonl(CONSOLIDATED_009_PATH)
    seed_by_id = {row["stable_id"]: row for row in seed_rows}
    consolidated_by_id = {row["stable_id"]: row for row in consolidated_rows}
    if len(seed_by_id) != len(seed_rows):
        raise SystemExit("duplicate stable_id inside ROOT.corrections.jsonl")
    if len(consolidated_by_id) != len(consolidated_rows):
        raise SystemExit("duplicate stable_id inside ROOT.009.consolidated.corrections.jsonl")

    target_seed_rows = [row for row in seed_rows if row["stable_id"] in target_by_id]
    target_seed_guard_failures = []
    for row in target_seed_rows:
        script, entry = target_by_id[row["stable_id"]]
        if row.get("script") != script or row.get("sequence") != entry["sequence"] or row.get("old_ko") != entry["draft_ko"]:
            target_seed_guard_failures.append({
                "stable_id": row["stable_id"],
                "seed_script": row.get("script"),
                "seed_sequence": row.get("sequence"),
                "master_script": script,
                "master_sequence": entry["sequence"],
                "old_exact": row.get("old_ko") == entry["draft_ko"],
            })

    manual_ids = {row["stable_id"] for row in rows}
    seed_overlap_ids = sorted(manual_ids & set(seed_by_id))
    consolidated_overlap_ids = sorted(manual_ids & set(consolidated_by_id))
    seed_merges = []
    for stable_id in seed_overlap_ids:
        manual = next(row for row in rows if row["stable_id"] == stable_id)
        seed = seed_by_id[stable_id]
        seed_merges.append({
            "script": manual["script"],
            "sequence": manual["sequence"],
            "stable_id": stable_id,
            "seed_old_exact_master": seed.get("old_ko") == manual["old_ko"],
            "seed_new_ko": seed.get("new_ko"),
            "manual_final_new_ko": manual["new_ko"],
            "seed_mechanics_reflected": seed.get("category") == "typography" and "０１２３４５６７８９".find("１") >= 0 and not any(ch in manual["new_ko"] for ch in "０１２３４５６７８９"),
        })

    validations = [validate_record(target_by_id[row["stable_id"]][1], row) for row in rows]
    failures = [record for record in validations if not record["pass"]]
    if target_seed_guard_failures:
        raise SystemExit(f"target seed old guard failures: {target_seed_guard_failures}")
    if consolidated_overlap_ids:
        raise SystemExit(f"unexpected 009 consolidated overlap: {consolidated_overlap_ids}")
    if failures:
        raise SystemExit(f"manual validation failures: {failures}")

    write_jsonl(OUTPUT_PATH, rows)

    structure_by_script = {
        script: scope_structure_audit(list(entries_by_script[script].values()))
        for script in MASTER_PATHS
    }
    sequence_fingerprints = {
        script: hashlib.sha256(",".join(str(x) for x in range(1, EXPECTED_COUNTS[script] + 1)).encode("ascii")).hexdigest()
        for script in MASTER_PATHS
    }
    validation_checks = [
        "exact_old_guard",
        "protected_tokens",
        "numbers_with_fullwidth_normalization",
        "Roman_numerals",
        "quotation_marks",
        "RenPy_tags",
        "ruby_tag_markers_including_standalone_rt",
        "newlines",
    ]
    summary_by_check = {}
    for key in (
        "exact_old_guard_pass",
        "protected_tokens_pass",
        "numbers_pass",
        "roman_numerals_pass",
        "quotes_pass",
        "renpy_tags_pass",
        "ruby_tags_pass",
        "newlines_pass",
    ):
        summary_by_check[key] = {
            "pass_count": sum(record[key] for record in validations),
            "failure_count": sum(not record[key] for record in validations),
        }

    report = {
        "schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scripts": ["011_02", "011_02GH"],
        "reviewer": "ROOT",
        "source_policy": {
            "semantic_authority": "Japanese source_jp only",
            "official_english_new_prose_opened_or_used": False,
            "external_translation_api_used": False,
            "game_run": False,
            "master_modified": False,
            "existing_correction_files_modified": False,
        },
        "exhaustive_review": {
            "checked": sum(EXPECTED_COUNTS.values()),
            "expected_checked": 456,
            "by_script": {
                script: {
                    "sequence_start": 1,
                    "sequence_end": EXPECTED_COUNTS[script],
                    "checked": EXPECTED_COUNTS[script],
                    "contiguous": True,
                    "checked_sequences_sha256": sequence_fingerprints[script],
                    "manual_correction_count": len(DECISIONS[script]),
                    "unchanged_after_review_count": EXPECTED_COUNTS[script] - len(DECISIONS[script]),
                }
                for script in MASTER_PATHS
            },
        },
        "inputs": {
            "masters": {
                script: {"path": str(path), "sha256": master_hashes_before[script]}
                for script, path in MASTER_PATHS.items()
            },
            "existing_seed": {"path": str(SEED_PATH), "sha256": seed_hash_before},
            "existing_009_consolidated": {"path": str(CONSOLIDATED_009_PATH), "sha256": consolidated_hash_before},
        },
        "output": {
            "path": str(OUTPUT_PATH),
            "sha256": sha256(OUTPUT_PATH),
        },
        "counts": {
            "checked": sum(EXPECTED_COUNTS.values()),
            "manual_correction_count": len(rows),
            "manual_output_unique_stable_id_count": len(manual_ids),
            "manual_output_duplicate_stable_id_count": len(rows) - len(manual_ids),
            "existing_seed_total_rows": len(seed_rows),
            "existing_seed_target_script_rows": len(target_seed_rows),
            "existing_seed_target_old_guard_pass_count": len(target_seed_rows) - len(target_seed_guard_failures),
            "existing_seed_target_old_guard_failure_count": len(target_seed_guard_failures),
            "existing_seed_manual_overlap_count": len(seed_overlap_ids),
            "existing_009_consolidated_total_rows": len(consolidated_rows),
            "existing_009_consolidated_manual_overlap_count": len(consolidated_overlap_ids),
            "exact_old_guard_pass_count": sum(record["exact_old_guard_pass"] for record in validations),
            "validation_pass_count": sum(record["pass"] for record in validations),
            "validation_failure_count": len(failures),
        },
        "existing_stable_id_checks": {
            "ROOT_corrections_internal_duplicate_count": len(seed_rows) - len(seed_by_id),
            "ROOT_009_consolidated_internal_duplicate_count": len(consolidated_rows) - len(consolidated_by_id),
            "ROOT_corrections_target_old_guard_failures": target_seed_guard_failures,
            "ROOT_corrections_manual_overlaps": seed_merges,
            "ROOT_009_consolidated_manual_overlap_ids": consolidated_overlap_ids,
        },
        "validation": {
            "all_pass": not failures,
            "checks": validation_checks,
            "summary_by_check": summary_by_check,
            "failures": failures,
            "records": validations,
        },
        "full_checked_scope_structure_audit": structure_by_script,
        "immutability_hash_check": {
            "masters_unchanged": all(sha256(path) == master_hashes_before[script] for script, path in MASTER_PATHS.items()),
            "existing_seed_unchanged": sha256(SEED_PATH) == seed_hash_before,
            "existing_009_consolidated_unchanged": sha256(CONSOLIDATED_009_PATH) == consolidated_hash_before,
        },
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    print(json.dumps({
        "checked": sum(EXPECTED_COUNTS.values()),
        "corrections": len(rows),
        "by_script": {script: len(DECISIONS[script]) for script in DECISIONS},
        "seed_target_rows": len(target_seed_rows),
        "seed_manual_overlaps": len(seed_overlap_ids),
        "overlap_sequences": sorted(item["sequence"] for item in seed_merges),
        "consolidated_009_overlaps": len(consolidated_overlap_ids),
        "validation_all_pass": not failures,
        "output": str(OUTPUT_PATH),
        "output_sha256": sha256(OUTPUT_PATH),
        "report": str(REPORT_PATH),
        "report_sha256": sha256(REPORT_PATH),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
