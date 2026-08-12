from __future__ import annotations

import hashlib
import importlib.util
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parent
REVIEWS = BASE / "reviews"
MASTER_PATHS = {
    "003": BASE / "output" / "masters" / "scenario_003.master.json",
    "004": BASE / "output" / "masters" / "scenario_004.master.json",
}
DECISION_PATH = BASE / "a_003_004_decisions.py"
OUTPUT_PATH = REVIEWS / "A.003_004.consolidated.corrections.jsonl"
REPORT_PATH = REVIEWS / "A.003_004.consolidated.report.json"
EXPECTED_COUNTS = {"003": 1526, "004": 1067}

FULLWIDTH_DIGIT_SEQUENCES = {
    "003": [1323, 1324, 1346, 1347, 1351, 1384, 1420, 1440, 1441, 1465, 1467, 1488, 1525],
    "004": [808, 835, 895, 897, 899, 908, 925, 945, 947, 949, 955, 979, 982, 993, 1061],
}
FULLWIDTH_PERCENT_SEQUENCES = {"003": [749], "004": []}
GREAT_HALL_SEQUENCES = {
    "003": [1416, 1459, 1489, 1490, 1507],
    "004": [867, 918, 963, 965, 994, 1002],
}
NEGATED_EVENT_SEQUENCES = {
    "003": [41, 159, 226, 227, 395, 402, 403, 917, 1015, 1203, 1215, 1232, 1349],
    "004": [8, 14],
}
QUOTE_REPAIR_SEQUENCES = {"003": [], "004": [356]}

ROMAN_RE = re.compile(r"[\u2160-\u216b]")
NUM_RE = re.compile(r"[0-9\uff10-\uff19]+")
TAG_RE = re.compile(r"\{[^{}\n]*\}|\[[^\[\]\n]*\]")
RUBY_TAG_RE = re.compile(r"\{/?(?:rb|rt)\}")
PERCENT_FORMAT_RE = re.compile(r"%(?:\([^)]+\))?[#0\- +]?(?:\d+|\*)?(?:\.\d+)?[diouxXeEfFgGcrs%]")
KANA_RE = re.compile(r"[\u3041-\u3096\u309d-\u309f\u30a1-\u30fa\u30fc-\u30ff\u31f0-\u31ff\uff66-\uff9f]")
HAN_RE = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
FULLWIDTH_WIDTH_RE = re.compile(r"[\uff10-\uff19\uff05]")
QUOTE_CHARS = "\u300c\u300d\u300e\u300f\u226a\u226b\u201c\u201d\u2018\u2019\""
FW_TRANS = str.maketrans("".join(chr(0xFF10 + i) for i in range(10)), "0123456789")
HAN_ALLOWLIST = {("004", 53), ("004", 57)}

NUMERIC_SEMANTIC_EXCEPTIONS = {
    ("003", 126): "source Arabic ２ is translated lexically as Korean 두",
    ("003", 1223): "source lexical ゼロ is represented as digit 0",
    ("004", 90): "source Arabic ３ is translated lexically as Korean 세",
    ("004", 208): "source kanji 一 in 一年生 is represented as digit 1",
    ("004", 281): "source Arabic ２ is translated lexically as Korean 두",
    ("004", 286): "source Arabic ２ is translated lexically as Korean 두",
    ("004", 287): "source Arabic ２ is translated lexically as Korean 두",
    ("004", 343): "source Arabic １/２ are translated lexically as Korean 혼자/둘",
    ("004", 428): "source Arabic ２ is translated lexically as Korean 둘",
    ("004", 442): "source Arabic ２ is translated lexically as Korean 두",
    ("004", 454): "source Arabic ３ is translated lexically as Korean 셋",
    ("004", 520): "source Arabic ３ is translated lexically as Korean 세",
    ("004", 579): "source kanji 一 in 一階 is represented as digit 1",
    ("004", 611): "source Arabic ３ is translated lexically as Korean 셋",
    ("004", 717): "source kanji 二 in 二人組 is represented as digit 2",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_decisions() -> dict[str, list[tuple]]:
    spec = importlib.util.spec_from_file_location("a_003_004_decisions", DECISION_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit("cannot load decision module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.DECISIONS


def normalized_numbers(text: str) -> Counter:
    return Counter(value.translate(FW_TRANS) for value in NUM_RE.findall(text))


def normalized_percent_formats(text: str) -> Counter:
    return Counter(PERCENT_FORMAT_RE.findall(text.replace("\uff05", "%")))


def counter_dict(value: Counter) -> dict:
    return dict(sorted(value.items()))


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
        newline="\n",
    )


def extract_correction_objects(path: Path) -> list[dict]:
    try:
        if path.suffix.lower() == ".jsonl":
            objects = [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
        else:
            payload = json.loads(path.read_text(encoding="utf-8-sig"))
            if isinstance(payload, list):
                objects = payload
            elif isinstance(payload, dict) and isinstance(payload.get("corrections"), list):
                objects = payload["corrections"]
            else:
                objects = []
    except (UnicodeDecodeError, json.JSONDecodeError):
        return []
    return [obj for obj in objects if isinstance(obj, dict) and isinstance(obj.get("new_ko"), str)]


def inventory_existing_a(target_by_id: dict, target_by_key: dict) -> tuple[list[dict], list[dict]]:
    inventory = []
    target_hits = []
    for path in sorted(REVIEWS.glob("A*")):
        if not path.is_file() or path in {OUTPUT_PATH, REPORT_PATH}:
            continue
        if path.suffix.lower() not in {".json", ".jsonl"}:
            continue
        objects = extract_correction_objects(path)
        inventory.append({
            "file": str(path.relative_to(BASE)),
            "sha256_before": sha256(path),
            "correction_object_count": len(objects),
        })
        for obj in objects:
            stable_id = obj.get("stable_id")
            script = str(obj.get("script") or obj.get("script_key") or "")
            sequence = obj.get("sequence")
            resolved = None
            if stable_id in target_by_id:
                resolved = target_by_id[stable_id]
            elif isinstance(sequence, int) and (script, sequence) in target_by_key:
                resolved = target_by_key[(script, sequence)]
            if resolved is None:
                continue
            resolved_script, entry = resolved
            exact_old = obj.get("old_ko") is None or obj.get("old_ko") == entry["draft_ko"]
            target_hits.append({
                "file": str(path.relative_to(BASE)),
                "script": resolved_script,
                "sequence": entry["sequence"],
                "stable_id": entry["stable_id"],
                "exact_old_guard_pass": exact_old,
                "new_ko": obj["new_ko"],
            })
    return inventory, target_hits


def detect_mechanical(entries_by_script: dict[str, dict[int, dict]]) -> dict[str, dict[str, list[int]]]:
    found = {}
    for script, by_sequence in entries_by_script.items():
        found[script] = {
            "fullwidth_digits": [seq for seq, entry in by_sequence.items() if re.search(r"[\uff10-\uff19]", entry["draft_ko"])],
            "fullwidth_percent": [seq for seq, entry in by_sequence.items() if "\uff05" in entry["draft_ko"]],
            "great_hall_term": [seq for seq, entry in by_sequence.items() if "대전당" in entry["draft_ko"]],
            "negated_event_term": [seq for seq, entry in by_sequence.items() if "없었던 일" in entry["draft_ko"]],
            "quote_repairs": [356] if script == "004" and "『좋은 아침, 리땅』" in by_sequence[356]["draft_ko"] else [],
        }
        expected = {
            "fullwidth_digits": FULLWIDTH_DIGIT_SEQUENCES[script],
            "fullwidth_percent": FULLWIDTH_PERCENT_SEQUENCES[script],
            "great_hall_term": GREAT_HALL_SEQUENCES[script],
            "negated_event_term": NEGATED_EVENT_SEQUENCES[script],
            "quote_repairs": QUOTE_REPAIR_SEQUENCES[script],
        }
        if found[script] != expected:
            raise SystemExit(f"mechanical inventory mismatch {script}: {found[script]} != {expected}")
    return found


def apply_mechanical(script: str, sequence: int, text: str) -> tuple[str, list[tuple[str, str]]]:
    changes = []
    new_text = text
    digit_text = new_text.translate(FW_TRANS)
    if digit_text != new_text:
        new_text = digit_text
        changes.append(("typography", "전각 숫자를 값이 같은 ASCII 숫자로 정규화"))
    percent_text = new_text.replace("\uff05", "%")
    if percent_text != new_text:
        new_text = percent_text
        changes.append(("typography", "전각 퍼센트 기호를 ASCII %로 정규화"))
    hall_text = new_text.replace("대전당", "대회랑")
    if hall_text != new_text:
        new_text = hall_text
        changes.append(("고정 용어", "大広間의 고정 표기를 대회랑으로 통일"))
    event_text = new_text.replace("없었던 일", "없던 일")
    if event_text != new_text:
        new_text = event_text
        changes.append(("고정 표기", "なかったこと의 고정 표기를 없던 일로 통일"))
    if script == "004" and sequence == 356:
        quote_text = new_text.replace("『좋은 아침, 리땅』", "좋은 아침, 리땅")
        if quote_text == new_text:
            raise SystemExit("004:356 quote repair pattern missing")
        new_text = quote_text
        changes.append(("인용부호 구조", "source_jp에 없는 안쪽 『』 한 쌍 제거"))
    return new_text, changes


def structural_counter(text: str, kind: str):
    if kind == "roman":
        return Counter(ROMAN_RE.findall(text))
    if kind == "quotes":
        return Counter(ch for ch in text if ch in QUOTE_CHARS)
    if kind == "tags":
        return Counter(TAG_RE.findall(text))
    if kind == "ruby":
        return Counter(RUBY_TAG_RE.findall(text))
    if kind == "newlines":
        return text.count("\n")
    raise ValueError(kind)


def validate_row(entry: dict, row: dict) -> dict:
    old = row["old_ko"]
    new = row["new_ko"]
    protected_differences = []
    for token in entry.get("protected_tokens") or []:
        if isinstance(token, dict):
            if token.get("kind") == "number":
                continue
            value = token.get("value")
        else:
            value = token
        if value and old.count(value) != new.count(value):
            protected_differences.append({"token": value, "old": old.count(value), "new": new.count(value)})
    checks = {
        "exact_old_guard": entry["draft_ko"] == old,
        "changed": old != new,
        "protected_tokens": not protected_differences,
        "numbers": normalized_numbers(old) == normalized_numbers(new),
        "percent_formats": normalized_percent_formats(old) == normalized_percent_formats(new),
        "roman": structural_counter(old, "roman") == structural_counter(new, "roman"),
        "quotes_against_source": structural_counter(entry["source_jp"], "quotes") == structural_counter(new, "quotes"),
        "tags": structural_counter(old, "tags") == structural_counter(new, "tags"),
        "ruby": structural_counter(old, "ruby") == structural_counter(new, "ruby"),
        "newlines": structural_counter(old, "newlines") == structural_counter(new, "newlines"),
        "width": not FULLWIDTH_WIDTH_RE.search(new),
    }
    return {
        "script": row["script"],
        "sequence": row["sequence"],
        "stable_id": row["stable_id"],
        "checks": checks,
        "pass": all(checks.values()),
        "protected_differences": protected_differences,
    }


def full_scope_audit(all_entries: list[tuple[str, dict]], patched_by_id: dict[str, str]) -> dict:
    structure = {}
    for kind in ["roman", "quotes", "tags", "ruby", "newlines"]:
        failures = []
        for script, entry in all_entries:
            patched = patched_by_id[entry["stable_id"]]
            source_value = structural_counter(entry["source_jp"], kind)
            target_value = structural_counter(patched, kind)
            if source_value != target_value:
                failures.append({
                    "script": script,
                    "sequence": entry["sequence"],
                    "stable_id": entry["stable_id"],
                    "source": counter_dict(source_value) if isinstance(source_value, Counter) else source_value,
                    "target": counter_dict(target_value) if isinstance(target_value, Counter) else target_value,
                })
        structure[kind] = {"failure_count": len(failures), "failures": failures, "pass": not failures}

    numeric_strict_failures = []
    numeric_exception_records = []
    for script, entry in all_entries:
        source_numbers = normalized_numbers(entry["source_jp"])
        target_numbers = normalized_numbers(patched_by_id[entry["stable_id"]])
        if source_numbers == target_numbers:
            continue
        key = (script, entry["sequence"])
        record = {
            "script": script,
            "sequence": entry["sequence"],
            "stable_id": entry["stable_id"],
            "source_numbers": counter_dict(source_numbers),
            "target_numbers": counter_dict(target_numbers),
        }
        if key in NUMERIC_SEMANTIC_EXCEPTIONS:
            record["reason"] = NUMERIC_SEMANTIC_EXCEPTIONS[key]
            numeric_exception_records.append(record)
        else:
            numeric_strict_failures.append(record)
    seen_exception_keys = {(r["script"], r["sequence"]) for r in numeric_exception_records}
    if seen_exception_keys != set(NUMERIC_SEMANTIC_EXCEPTIONS):
        raise SystemExit(f"numeric exception audit mismatch: {seen_exception_keys}")

    width_failures = []
    kana_failures = []
    han_failures = []
    han_allowlisted = []
    percent_format_failures = []
    for script, entry in all_entries:
        text = patched_by_id[entry["stable_id"]]
        if FULLWIDTH_WIDTH_RE.search(text):
            width_failures.append({"script": script, "sequence": entry["sequence"], "matches": FULLWIDTH_WIDTH_RE.findall(text)})
        if KANA_RE.search(text):
            kana_failures.append({"script": script, "sequence": entry["sequence"], "matches": KANA_RE.findall(text)})
        han = Counter(HAN_RE.findall(text))
        if han:
            record = {"script": script, "sequence": entry["sequence"], "characters": counter_dict(han)}
            if (script, entry["sequence"]) in HAN_ALLOWLIST:
                han_allowlisted.append(record)
            else:
                han_failures.append(record)
        source_formats = normalized_percent_formats(entry["source_jp"])
        target_formats = normalized_percent_formats(text)
        if source_formats != target_formats:
            percent_format_failures.append({
                "script": script,
                "sequence": entry["sequence"],
                "source": counter_dict(source_formats),
                "target": counter_dict(target_formats),
            })
    return {
        "structure": structure,
        "numeric_semantics": {
            "checked": len(all_entries),
            "strict_match_count": len(all_entries) - len(numeric_exception_records) - len(numeric_strict_failures),
            "audited_lexical_equivalent_count": len(numeric_exception_records),
            "audited_lexical_equivalents": numeric_exception_records,
            "failure_count": len(numeric_strict_failures),
            "failures": numeric_strict_failures,
            "pass": not numeric_strict_failures,
        },
        "width": {"failure_count": len(width_failures), "failures": width_failures, "pass": not width_failures},
        "residual_japanese_kana": {"failure_count": len(kana_failures), "failures": kana_failures, "pass": not kana_failures},
        "residual_han": {
            "failure_count": len(han_failures),
            "failures": han_failures,
            "allowlisted_records": han_allowlisted,
            "allowlist_reason": "004 seq53/57 are explicit name/kanji explanations; 桂, 樹, 春樹 must remain visible",
            "pass": not han_failures,
        },
        "percent_interpolation": {
            "failure_count": len(percent_format_failures),
            "failures": percent_format_failures,
            "pass": not percent_format_failures,
        },
    }


def main() -> None:
    master_hashes_before = {script: sha256(path) for script, path in MASTER_PATHS.items()}
    decisions = load_decisions()
    masters = {}
    entries_by_script = {}
    target_by_id = {}
    target_by_key = {}
    all_entries = []
    coverage = {}
    for script, path in MASTER_PATHS.items():
        master = json.loads(path.read_text(encoding="utf-8-sig"))
        entries = master["entries"]
        if master.get("script_key") != script:
            raise SystemExit(f"script key mismatch: {script}")
        if len(entries) != EXPECTED_COUNTS[script]:
            raise SystemExit(f"entry count mismatch: {script}")
        if [entry["sequence"] for entry in entries] != list(range(1, EXPECTED_COUNTS[script] + 1)):
            raise SystemExit(f"non-contiguous sequences: {script}")
        if master.get("english_reference_used") is not False or master.get("external_translation_api_used") is not False:
            raise SystemExit(f"source authority metadata mismatch: {script}")
        if len({entry["stable_id"] for entry in entries}) != len(entries):
            raise SystemExit(f"duplicate stable_id within {script}")
        masters[script] = master
        entries_by_script[script] = {entry["sequence"]: entry for entry in entries}
        digest_payload = "\n".join(f"{script}:{entry['sequence']}:{entry['stable_id']}" for entry in entries).encode("utf-8")
        coverage[script] = {
            "checked": len(entries),
            "expected": EXPECTED_COUNTS[script],
            "sequence_start": entries[0]["sequence"],
            "sequence_end": entries[-1]["sequence"],
            "sequence_contiguous": True,
            "stable_id_unique": True,
            "sequence_stable_id_sha256": hashlib.sha256(digest_payload).hexdigest(),
            "source_authority": master.get("source_authority"),
            "english_reference_used": master.get("english_reference_used"),
            "external_translation_api_used": master.get("external_translation_api_used"),
        }
        for entry in entries:
            if entry["stable_id"] in target_by_id:
                raise SystemExit(f"cross-script duplicate stable_id: {entry['stable_id']}")
            pair = (script, entry)
            target_by_id[entry["stable_id"]] = pair
            target_by_key[(script, entry["sequence"])] = pair
            all_entries.append(pair)
    if len(all_entries) != sum(EXPECTED_COUNTS.values()):
        raise SystemExit("exhaustive checked count mismatch")

    inventory, existing_target_hits = inventory_existing_a(target_by_id, target_by_key)
    if existing_target_hits:
        raise SystemExit(f"unexpected existing A corrections for 003/004 require explicit merge: {existing_target_hits}")
    existing_hashes_before = {item["file"]: item["sha256_before"] for item in inventory}

    mechanical_inventory = detect_mechanical(entries_by_script)
    manual_by_key = {}
    for script in MASTER_PATHS:
        script_decisions = decisions.get(script)
        if not isinstance(script_decisions, list):
            raise SystemExit(f"missing decision list: {script}")
        sequences = [decision[0] for decision in script_decisions]
        if len(sequences) != len(set(sequences)):
            raise SystemExit(f"duplicate manual decision sequence: {script}")
        for sequence, new_ko, category, reason in script_decisions:
            if sequence not in entries_by_script[script]:
                raise SystemExit(f"manual sequence missing from master: {script}:{sequence}")
            manual_by_key[(script, sequence)] = (new_ko, category, reason)

    rows = []
    patched_by_id = {}
    mechanical_changed_keys = set()
    semantic_changed_keys = set(manual_by_key)
    merged_manual_mechanical_keys = set()
    per_kind_counts = defaultdict(int)
    for script, entry in all_entries:
        sequence = entry["sequence"]
        old = entry["draft_ko"]
        key = (script, sequence)
        if key in manual_by_key:
            new, category, reason = manual_by_key[key]
        else:
            new, category, reason = old, "", ""
        new, mechanical_changes = apply_mechanical(script, sequence, new)
        if mechanical_changes:
            mechanical_changed_keys.add(key)
            for mechanical_category, _ in mechanical_changes:
                per_kind_counts[mechanical_category] += 1
            mechanical_categories = [item[0] for item in mechanical_changes]
            mechanical_reasons = [item[1] for item in mechanical_changes]
            if key in manual_by_key:
                merged_manual_mechanical_keys.add(key)
                category = category + "+" + "+".join(mechanical_categories)
                reason = reason + "; " + "; ".join(mechanical_reasons)
            else:
                category = "+".join(mechanical_categories)
                reason = "; ".join(mechanical_reasons)
        patched_by_id[entry["stable_id"]] = new
        if new == old:
            if key in manual_by_key:
                raise SystemExit(f"manual no-op: {script}:{sequence}")
            continue
        rows.append({
            "script": script,
            "stable_id": entry["stable_id"],
            "sequence": sequence,
            "old_ko": old,
            "new_ko": new,
            "category": category,
            "reason": reason,
            "reviewer": "A",
        })
    rows.sort(key=lambda row: (row["script"], row["sequence"]))
    if len(rows) != len({row["stable_id"] for row in rows}):
        raise SystemExit("duplicate stable_id in output rows")
    expected_row_count = len(semantic_changed_keys | mechanical_changed_keys)
    if len(rows) != expected_row_count:
        raise SystemExit(f"row count mismatch: {len(rows)} != {expected_row_count}")

    row_validations = []
    for row in rows:
        _, entry = target_by_id[row["stable_id"]]
        result = validate_row(entry, row)
        row_validations.append(result)
    failed_rows = [item for item in row_validations if not item["pass"]]
    if failed_rows:
        raise SystemExit("row validation failed: " + json.dumps(failed_rows, ensure_ascii=False))

    scope = full_scope_audit(all_entries, patched_by_id)
    scope_pass = (
        all(item["pass"] for item in scope["structure"].values())
        and scope["numeric_semantics"]["pass"]
        and scope["width"]["pass"]
        and scope["residual_japanese_kana"]["pass"]
        and scope["residual_han"]["pass"]
        and scope["percent_interpolation"]["pass"]
    )
    if not scope_pass:
        raise SystemExit("full scope validation failed: " + json.dumps(scope, ensure_ascii=False))

    write_jsonl(OUTPUT_PATH, rows)
    output_hash = sha256(OUTPUT_PATH)
    master_hashes_after = {script: sha256(path) for script, path in MASTER_PATHS.items()}
    existing_hashes_after = {item["file"]: sha256(BASE / item["file"]) for item in inventory}
    immutable_pass = master_hashes_before == master_hashes_after and existing_hashes_before == existing_hashes_after
    if not immutable_pass:
        raise SystemExit("master or existing A correction changed")

    per_script_rows = Counter(row["script"] for row in rows)
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "reviewer": "A",
        "task": "scenario_003 and scenario_004 exhaustive final Japanese-source-only QA",
        "source_policy": {
            "meaning_authority": "source_jp only",
            "english_new_prose_opened_or_used": False,
            "external_translation_api_used": False,
            "game_executed": False,
        },
        "exhaustive_checked": len(all_entries),
        "expected_exhaustive_checked": 2593,
        "coverage_pass": len(all_entries) == 2593 and all(item["checked"] == item["expected"] for item in coverage.values()),
        "coverage": coverage,
        "corrections": {
            "output_rows": len(rows),
            "per_script": dict(sorted(per_script_rows.items())),
            "manual_semantic_or_grammar_decisions": len(semantic_changed_keys),
            "manual_per_script": {script: len(decisions[script]) for script in MASTER_PATHS},
            "mechanical_changed_rows": len(mechanical_changed_keys),
            "mechanical_manual_merge_count": len(merged_manual_mechanical_keys),
            "mechanical_manual_merge_keys": [f"{script}:{sequence}" for script, sequence in sorted(merged_manual_mechanical_keys)],
            "stable_id_unique": len(rows) == len({row["stable_id"] for row in rows}),
            "categories": dict(sorted(Counter(row["category"] for row in rows).items())),
        },
        "mechanical_inventory": mechanical_inventory,
        "existing_a_correction_inventory": inventory,
        "existing_a_target_hits": existing_target_hits,
        "existing_a_target_hit_count": len(existing_target_hits),
        "existing_a_merge_count": 0,
        "validation": {
            "output_row_checked": len(row_validations),
            "output_row_failure_count": len(failed_rows),
            "exact_old_guard_pass": all(item["checks"]["exact_old_guard"] for item in row_validations),
            "protected_tokens_pass": all(item["checks"]["protected_tokens"] for item in row_validations),
            "numbers_old_new_pass": all(item["checks"]["numbers"] for item in row_validations),
            "percent_formats_old_new_pass": all(item["checks"]["percent_formats"] for item in row_validations),
            "roman_old_new_pass": all(item["checks"]["roman"] for item in row_validations),
            "quotes_against_source_pass": all(item["checks"]["quotes_against_source"] for item in row_validations),
            "renpy_tags_old_new_pass": all(item["checks"]["tags"] for item in row_validations),
            "ruby_old_new_pass": all(item["checks"]["ruby"] for item in row_validations),
            "newline_old_new_pass": all(item["checks"]["newlines"] for item in row_validations),
            "width_per_row_pass": all(item["checks"]["width"] for item in row_validations),
            "full_scope": scope,
            "all_pass": not failed_rows and scope_pass,
        },
        "intentional_han_preservation": {
            "004:53": "桂 is the kanji being explained in the name 桂子",
            "004:57": "樹 and 春樹 are the kanji/name forms being explicitly explained",
        },
        "immutability": {
            "master_sha256_before": master_hashes_before,
            "master_sha256_after": master_hashes_after,
            "existing_a_sha256_before": existing_hashes_before,
            "existing_a_sha256_after": existing_hashes_after,
            "pass": immutable_pass,
        },
        "artifacts": {
            "output": str(OUTPUT_PATH.relative_to(BASE)),
            "output_sha256": output_hash,
            "report": str(REPORT_PATH.relative_to(BASE)),
        },
    }
    if not report["coverage_pass"] or not report["validation"]["all_pass"] or not report["immutability"]["pass"]:
        raise SystemExit("final report gates failed")
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({
        "output": str(OUTPUT_PATH),
        "report": str(REPORT_PATH),
        "exhaustive_checked": report["exhaustive_checked"],
        "correction_rows": len(rows),
        "per_script": dict(sorted(per_script_rows.items())),
        "manual_decisions": len(semantic_changed_keys),
        "mechanical_rows": len(mechanical_changed_keys),
        "existing_a_target_hits": len(existing_target_hits),
        "validation_all_pass": report["validation"]["all_pass"],
        "output_sha256": output_hash,
        "report_sha256": sha256(REPORT_PATH),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
