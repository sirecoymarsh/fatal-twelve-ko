from __future__ import annotations

import copy
import csv
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import audit_master


ROOT = Path(__file__).resolve().parent
REVIEWS = ROOT / "reviews"
MASTERS = ROOT / "output" / "masters"
RUBY_MAP = ROOT / "ruby_map.approved.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_master(script: str) -> tuple[dict, list[dict]]:
    path = MASTERS / f"scenario_{script}.master.json"
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    entries = payload["entries"]
    assert payload["script_key"] == script
    assert [row["sequence"] for row in entries] == list(range(1, len(entries) + 1))
    assert len({row["stable_id"] for row in entries}) == len(entries)
    return payload, entries


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def load_corrections(path: Path) -> list[dict]:
    if path.suffix.lower() == ".jsonl":
        rows = load_jsonl(path)
    elif path.suffix.lower() == ".tsv":
        with path.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle, delimiter="\t"))
    else:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        rows = payload if isinstance(payload, list) else payload.get("corrections", [])
    return [row for row in rows if isinstance(row, dict) and isinstance(row.get("new_ko"), str)]


def script_of(row: dict) -> str:
    return str(row.get("script") or row.get("script_key") or "")


def canonical_row(source: dict, script: str, master: dict, reviewer: str) -> dict:
    sequence = int(source["sequence"])
    assert sequence == master["sequence"]
    stable_id = source.get("stable_id") or master["stable_id"]
    old_ko = source.get("old_ko") if source.get("old_ko") is not None else master["draft_ko"]
    assert stable_id == master["stable_id"]
    assert old_ko == master["draft_ko"]
    return {
        "script": script,
        "stable_id": stable_id,
        "sequence": sequence,
        "old_ko": old_ko,
        "new_ko": source["new_ko"],
        "category": source.get("category") or "manual",
        "reason": source.get("reason") or source.get("note") or "selected final correction",
        "reviewer": reviewer,
    }


def merge_change(rows: dict[int, dict], master: dict, new_ko: str, *, category: str, reason: str, reviewer: str) -> bool:
    sequence = master["sequence"]
    merged = sequence in rows
    if merged:
        row = rows[sequence]
        row["new_ko"] = new_ko
        if category not in row["category"]:
            row["category"] = f"{row['category']} + {category}"
        if reason not in row["reason"]:
            row["reason"] = f"{row['reason']}; {reason}"
    else:
        rows[sequence] = {
            "script": reviewer_script(master),
            "stable_id": master["stable_id"],
            "sequence": sequence,
            "old_ko": master["draft_ko"],
            "new_ko": new_ko,
            "category": category,
            "reason": reason,
            "reviewer": reviewer,
        }
    return merged


def reviewer_script(master: dict) -> str:
    # stable IDs are authoritative and encode the owning script.
    prefix = master["stable_id"].split("::scenario/", 1)[1].split(".rpy::", 1)[0]
    return prefix


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
        newline="\n",
    )


def corrected_entries(script: str, corrections: list[dict]) -> list[dict]:
    _, entries = load_master(script)
    by_id = {row["stable_id"]: row for row in corrections if row["script"] == script}
    result = []
    for source in entries:
        entry = copy.deepcopy(source)
        if entry["stable_id"] in by_id:
            row = by_id[entry["stable_id"]]
            assert row["old_ko"] == entry["draft_ko"]
            entry["draft_ko"] = row["new_ko"]
        result.append(entry)
    return result


def audit_scripts(scripts: list[str], corrections: list[dict]) -> list[dict]:
    ruby_map = audit_master.load_ruby_map(RUBY_MAP)
    issues: list[dict] = []
    for script in scripts:
        for entry in corrected_entries(script, corrections):
            audit_master.audit_entry(entry, script, issues, ruby_map=ruby_map)
    return issues


def validate_rows(rows: list[dict], scripts: list[str]) -> dict:
    masters = {}
    for script in scripts:
        _, entries = load_master(script)
        masters.update({row["stable_id"]: row for row in entries})
    failures = []
    for row in rows:
        master = masters.get(row["stable_id"])
        if master is None:
            failures.append({"stable_id": row["stable_id"], "reason": "no master join"})
            continue
        if row["sequence"] != master["sequence"] or row["old_ko"] != master["draft_ko"]:
            failures.append({"stable_id": row["stable_id"], "reason": "identity or exact old guard"})
        if row["new_ko"] == row["old_ko"]:
            failures.append({"stable_id": row["stable_id"], "reason": "no-op correction"})
    return {
        "rows": len(rows),
        "stable_id_unique": len({row["stable_id"] for row in rows}) == len(rows),
        "script_sequence_unique": len({(row["script"], row["sequence"]) for row in rows}) == len(rows),
        "exact_old_guard_pass": not failures,
        "failures": failures,
    }


def build_a001() -> tuple[Path, Path, list[dict]]:
    script = "001"
    _, entries = load_master(script)
    by_sequence = {row["sequence"]: row for row in entries}
    inputs = [
        REVIEWS / "A.manual_decisions.json",
        REVIEWS / "A.manual.001_0170_0338.json",
        REVIEWS / "A.resume.corrections.jsonl",
        REVIEWS / "A.manual.001_0508_end.corrections.jsonl",
    ]
    rows: dict[int, dict] = {}
    source_counts = {}
    for path in inputs:
        selected = [row for row in load_corrections(path) if script_of(row) == script]
        source_counts[path.name] = len(selected)
        for source in selected:
            row = canonical_row(source, script, by_sequence[int(source["sequence"])], "A")
            if row["sequence"] in rows:
                assert rows[row["sequence"]]["new_ko"] == row["new_ko"]
            rows[row["sequence"]] = row

    # Audit the selected projection first, then make only deterministic structural repairs.
    projection = corrected_entries(script, list(rows.values()))
    ruby_map = audit_master.load_ruby_map(RUBY_MAP)
    issues: list[dict] = []
    for entry in projection:
        audit_master.audit_entry(entry, script, issues, ruby_map=ruby_map)

    quote_sequences = []
    quote_merge_count = 0
    for issue in issues:
        if issue["rule_id"] != "JP_QUOTE_STYLE":
            continue
        sequence = int(issue["sequence"])
        entry = projection[sequence - 1]
        target = entry["draft_ko"]
        source_skeleton = audit_master.quote_skeleton(entry["source_jp"])
        target_skeleton = audit_master.quote_skeleton(target)
        if source_skeleton == ["「", "」"] and target_skeleton == [] and target.startswith("“") and target.endswith("”"):
            fixed = "「" + target[1:-1] + "」"
        elif source_skeleton == ["『", "』"] and target_skeleton == ["「", "」"]:
            fixed = target.replace("「", "『", 1)
            close = fixed.rfind("」")
            assert close >= 0
            fixed = fixed[:close] + "』" + fixed[close + 1 :]
        else:
            raise AssertionError((sequence, source_skeleton, target_skeleton, target))
        quote_merge_count += int(merge_change(
            rows,
            by_sequence[sequence],
            fixed,
            category="인용부호 구조",
            reason="source_jp의 「」/『』 skeleton에 맞춰 curly/잘못된 낫표를 교정",
            reviewer="A",
        ))
        projection[sequence - 1]["draft_ko"] = fixed
        quote_sequences.append(sequence)

    width_sequences = []
    width_merge_count = 0
    digit_map = str.maketrans("０１２３４５６７８９", "0123456789")
    for issue in issues:
        if issue["rule_id"] != "KO_WIDTH_STYLE":
            continue
        sequence = int(issue["sequence"])
        target = projection[sequence - 1]["draft_ko"]
        fixed = target.translate(digit_map).replace("\u3000", " ")
        assert fixed != target
        width_merge_count += int(merge_change(
            rows,
            by_sequence[sequence],
            fixed,
            category="typography",
            reason="한국어 target의 전각 숫자/U+3000을 반각 숫자/ASCII 공백으로 정규화",
            reviewer="A",
        ))
        projection[sequence - 1]["draft_ko"] = fixed
        width_sequences.append(sequence)

    # Frozen ruby map requires the correct reading of 小熊, and seq374 has a clear subject-name error.
    for sequence, before, after, category, reason in [
        (177, "코구마", "오구마", "고유명사/ruby", "小熊(おぐま)의 승인 고유명 표기 오구마를 ruby base/reading에 반영"),
    ]:
        target = projection[sequence - 1]["draft_ko"]
        assert before in target
        fixed = target.replace(before, after)
        merge_change(rows, by_sequence[sequence], fixed, category=category, reason=reason, reviewer="A")
        projection[sequence - 1]["draft_ko"] = fixed

    output_rows = sorted(rows.values(), key=lambda row: row["sequence"])
    validation = validate_rows(output_rows, [script])
    assert validation["stable_id_unique"] and validation["exact_old_guard_pass"]
    post_issues = audit_scripts([script], output_rows)
    allowed = {("scenario.rpa::scenario/001.rpy::tid::f001_s1_end_3f7863e1", "GLOSSARY_MISMATCH")}
    unexpected = [issue for issue in post_issues if (issue["stable_id"], issue["rule_id"]) not in allowed]
    assert unexpected == [], unexpected

    output = REVIEWS / "A.001.consolidated.corrections.jsonl"
    report_path = REVIEWS / "A.001.consolidated.report.json"
    write_jsonl(output, output_rows)
    report = {
        "schema_version": "fatal-twelve-a-001-consolidated-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "reviewer": "A",
        "script": script,
        "source_authority": "Japanese source_jp only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "game_executed": False,
        "master_modified": False,
        "exhaustive_checked": len(entries),
        "coverage_evidence": [
            {"range": [1, 169], "path": "reviews/A.manual_decisions.json"},
            {"range": [170, 338], "path": "reviews/A.manual.001_0170_0338.json"},
            {"range": [339, 507], "path": "reviews/A.resume.corrections.jsonl"},
            {"range": [508, 844], "path": "reviews/A.manual.001_0508_end.report.json", "checked": 337},
        ],
        "inputs": [
            {"path": str(path.relative_to(ROOT)), "sha256": sha256(path), "selected_records": source_counts[path.name]}
            for path in inputs
        ],
        "corrections": {
            "selected_input_rows": sum(source_counts.values()),
            "output_rows": len(output_rows),
            "quote_repairs": quote_sequences,
            "quote_repairs_merged_into_existing": quote_merge_count,
            "width_repairs": width_sequences,
            "width_repairs_merged_into_existing": width_merge_count,
            "ruby_name_repair": [177],
            "approved_source_anomaly_not_rewritten": [374],
        },
        "validation": {**validation, "post_correction_audit_issue_count": len(post_issues), "post_correction_unapproved_issue_count": len(unexpected), "post_correction_approved_issues": post_issues},
        "ruby_map": {"path": str(RUBY_MAP.relative_to(ROOT)), "sha256": sha256(RUBY_MAP)},
        "output": {"path": str(output.relative_to(ROOT)), "sha256": sha256(output)},
        "verdict": "PASS",
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return output, report_path, output_rows


def update_a003_004() -> tuple[Path, Path, list[dict]]:
    output = REVIEWS / "A.003_004.consolidated.corrections.jsonl"
    report_path = REVIEWS / "A.003_004.consolidated.report.json"
    before_hash = sha256(output)
    before_report_hash = sha256(report_path)
    current = load_jsonl(output)
    rows = {(row["script"], int(row["sequence"])): row for row in current}
    assert len(rows) == len(current)
    merged = []
    added = []
    fixed_sequences = [421, 485, 538, 596, 668, 805, 1079]
    _, entries = load_master("003")
    by_sequence = {row["sequence"]: row for row in entries}
    for sequence in fixed_sequences:
        key = ("003", sequence)
        master = by_sequence[sequence]
        target = rows[key]["new_ko"] if key in rows else master["draft_ko"]
        assert "꿈속 세계" in target
        fixed = target.replace("꿈속 세계", "꿈의 세계")
        if key in rows:
            row = rows[key]
            row["new_ko"] = fixed
            row["category"] = f"{row['category']} + 고정 용어"
            row["reason"] = f"{row['reason']}; 夢の世界의 고정 표기를 꿈의 세계로 통일"
            merged.append(sequence)
        else:
            rows[key] = {
                "script": "003",
                "stable_id": master["stable_id"],
                "sequence": sequence,
                "old_ko": master["draft_ko"],
                "new_ko": fixed,
                "category": "고정 용어",
                "reason": "夢の世界의 고정 표기를 꿈의 세계로 통일",
                "reviewer": "A",
            }
            added.append(sequence)
    output_rows = sorted(rows.values(), key=lambda row: (row["script"], row["sequence"]))
    validation = validate_rows(output_rows, ["003", "004"])
    assert validation["stable_id_unique"] and validation["exact_old_guard_pass"]
    # 004 has three explicitly approved record-level policy findings; there must be nothing else.
    allowed = {
        ("scenario.rpa::scenario/004.rpy::tid::f004_26d57359", "RESIDUAL_HANJA"),
        ("scenario.rpa::scenario/004.rpy::tid::f004_ee6737b0", "RESIDUAL_HANJA"),
        ("scenario.rpa::scenario/004.rpy::tid::f004_s2_end_d2d3ac84", "GLOSSARY_MISMATCH"),
    }
    post_issues = audit_scripts(["003", "004"], output_rows)
    unexpected = [issue for issue in post_issues if (issue["stable_id"], issue["rule_id"]) not in allowed]
    assert unexpected == [], unexpected
    write_jsonl(output, output_rows)
    report = json.loads(report_path.read_text(encoding="utf-8-sig"))
    report["generated_at_utc"] = datetime.now(timezone.utc).isoformat()
    report["corrections"]["output_rows"] = len(output_rows)
    report["corrections"]["per_script"] = dict(Counter(row["script"] for row in output_rows))
    report["corrections"]["mechanical_changed_rows"] = report["corrections"].get("mechanical_changed_rows", 0) + len(added)
    report["corrections"]["categories"] = dict(sorted(Counter(row["category"] for row in output_rows).items()))
    report["inventory_consolidation_update"] = {
        "input_corrections_sha256": before_hash,
        "input_report_sha256": before_report_hash,
        "fixed_term": "夢の世界 -> 꿈의 세계",
        "sequences": fixed_sequences,
        "added_rows": added,
        "merged_rows": merged,
        "record_rule_approvals_deferred_to_global_manifest": [
            {"script": "004", "sequence": 53, "rule_id": "RESIDUAL_HANJA"},
            {"script": "004", "sequence": 57, "rule_id": "RESIDUAL_HANJA"},
            {"script": "004", "sequence": 529, "rule_id": "GLOSSARY_MISMATCH"},
        ],
    }
    report["validation"]["output_row_checked"] = len(output_rows)
    report["validation"]["output_row_failure_count"] = len(validation["failures"])
    report["validation"]["exact_old_guard_pass"] = validation["exact_old_guard_pass"]
    report["validation"]["post_inventory_audit_issue_count"] = len(post_issues)
    report["validation"]["post_inventory_unapproved_issue_count"] = len(unexpected)
    report["output_sha256"] = sha256(output)
    report["verdict"] = "PASS"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return output, report_path, output_rows


def build_c007() -> tuple[Path, Path, list[dict]]:
    scripts = ["007_1", "007_2"]
    master_entries = {script: load_master(script)[1] for script in scripts}
    by_sequence = {script: {row["sequence"]: row for row in entries} for script, entries in master_entries.items()}
    source = REVIEWS / "C.decisions.tsv"
    source_rows = [row for row in load_corrections(source) if script_of(row) in scripts]
    rows: dict[tuple[str, int], dict] = {}
    excluded = []
    for item in source_rows:
        script = script_of(item)
        sequence = int(item["sequence"])
        if script == "007_1" and sequence == 365:
            excluded.append({
                "script": script,
                "sequence": sequence,
                "reason": "decision conflicts with approved ruby mapping; authoritative master text is retained",
                "excluded_new_ko": item["new_ko"],
            })
            continue
        rows[(script, sequence)] = canonical_row(item, script, by_sequence[script][sequence], "C")

    width_sequences = []
    width_merged = []
    term_sequences = []
    digit_map = str.maketrans("０１２３４５６７８９", "0123456789")
    for script in scripts:
        for master in master_entries[script]:
            key = (script, master["sequence"])
            target = rows[key]["new_ko"] if key in rows else master["draft_ko"]
            fixed = target.translate(digit_map).replace("\u3000", " ")
            if fixed != target:
                if key in rows:
                    rows[key]["new_ko"] = fixed
                    rows[key]["category"] = f"{rows[key]['category']} + typography"
                    rows[key]["reason"] = f"{rows[key]['reason']}; 전각 숫자/U+3000을 반각 숫자/ASCII 공백으로 정규화"
                    width_merged.append([script, master["sequence"]])
                else:
                    rows[key] = {
                        "script": script,
                        "stable_id": master["stable_id"],
                        "sequence": master["sequence"],
                        "old_ko": master["draft_ko"],
                        "new_ko": fixed,
                        "category": "typography",
                        "reason": "한국어 target의 전각 숫자/U+3000을 반각 숫자/ASCII 공백으로 정규화",
                        "reviewer": "C",
                    }
                width_sequences.append([script, master["sequence"]])

    for sequence in [1070, 1132, 1147]:
        script = "007_2"
        key = (script, sequence)
        master = by_sequence[script][sequence]
        target = rows[key]["new_ko"] if key in rows else master["draft_ko"]
        assert "꿈속 세상" in target
        fixed = target.replace("꿈속 세상", "꿈의 세계")
        if key in rows:
            rows[key]["new_ko"] = fixed
            rows[key]["category"] = f"{rows[key]['category']} + 고정 용어"
            rows[key]["reason"] = f"{rows[key]['reason']}; 夢の世界의 고정 표기를 꿈의 세계로 통일"
        else:
            rows[key] = {
                "script": script,
                "stable_id": master["stable_id"],
                "sequence": sequence,
                "old_ko": master["draft_ko"],
                "new_ko": fixed,
                "category": "고정 용어",
                "reason": "夢の世界의 고정 표기를 꿈의 세계로 통일",
                "reviewer": "C",
            }
        term_sequences.append([script, sequence])

    output_rows = sorted(rows.values(), key=lambda row: (row["script"], row["sequence"]))
    validation = validate_rows(output_rows, scripts)
    assert validation["stable_id_unique"] and validation["exact_old_guard_pass"]
    allowed = {
        ("scenario.rpa::scenario/007_1.rpy::tid::f007_1_a2f320a9", "TARGET_QUOTE_UNBALANCED"),
        ("scenario.rpa::scenario/007_2.rpy::tid::f007_2_b28c38e7", "NO_HANGUL"),
    }
    post_issues = audit_scripts(scripts, output_rows)
    unexpected = [issue for issue in post_issues if (issue["stable_id"], issue["rule_id"]) not in allowed]
    assert unexpected == [], unexpected
    output = REVIEWS / "C.007_1_007_2.consolidated.corrections.jsonl"
    report_path = REVIEWS / "C.007_1_007_2.consolidated.report.json"
    write_jsonl(output, output_rows)
    report = {
        "schema_version": "fatal-twelve-c-007-consolidated-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "reviewer": "C",
        "scripts": scripts,
        "source_authority": "Japanese source_jp only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "game_executed": False,
        "master_modified": False,
        "exhaustive_checked": sum(len(master_entries[script]) for script in scripts),
        "coverage": {script: len(master_entries[script]) for script in scripts},
        "input": {"path": str(source.relative_to(ROOT)), "sha256": sha256(source), "decision_rows": len(source_rows)},
        "corrections": {
            "output_rows": len(output_rows),
            "per_script": dict(Counter(row["script"] for row in output_rows)),
            "excluded_decisions": excluded,
            "width_repair_rows": width_sequences,
            "width_repair_count": len(width_sequences),
            "width_merged_with_decision": width_merged,
            "fixed_term_rows": term_sequences,
        },
        "record_rule_approvals_deferred_to_global_manifest": [
            {"script": "007_1", "sequence": 269, "rule_id": "TARGET_QUOTE_UNBALANCED"},
            {"script": "007_2", "sequence": 61, "rule_id": "NO_HANGUL"},
        ],
        "validation": {
            **validation,
            "post_correction_audit_issue_count": len(post_issues),
            "post_correction_unapproved_issue_count": len(unexpected),
            "post_correction_approved_issues": post_issues,
        },
        "ruby_map": {"path": str(RUBY_MAP.relative_to(ROOT)), "sha256": sha256(RUBY_MAP)},
        "output": {"path": str(output.relative_to(ROOT)), "sha256": sha256(output)},
        "verdict": "PASS",
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return output, report_path, output_rows


def build_root_011() -> tuple[Path, Path, list[dict]]:
    scripts = ["011_02", "011_02GH"]
    masters = {script: load_master(script)[1] for script in scripts}
    by_sequence = {script: {row["sequence"]: row for row in entries} for script, entries in masters.items()}
    manual_path = REVIEWS / "ROOT.manual.011_02_and_GH.corrections.jsonl"
    seed_path = REVIEWS / "ROOT.corrections.jsonl"
    seed_rows = [row for row in load_corrections(seed_path) if script_of(row) == "011_02GH"]
    manual_rows = [row for row in load_corrections(manual_path) if script_of(row) in scripts]
    rows: dict[tuple[str, int], dict] = {}
    for source in seed_rows:
        script = script_of(source)
        sequence = int(source["sequence"])
        rows[(script, sequence)] = canonical_row(source, script, by_sequence[script][sequence], "ROOT")
    overlaps = []
    for source in manual_rows:
        script = script_of(source)
        sequence = int(source["sequence"])
        key = (script, sequence)
        row = canonical_row(source, script, by_sequence[script][sequence], "ROOT")
        if key in rows:
            overlaps.append({
                "script": script,
                "sequence": sequence,
                "stable_id": row["stable_id"],
                "old_ko": row["old_ko"],
                "seed_new_ko": rows[key]["new_ko"],
                "manual_final_new_ko": row["new_ko"],
                "resolution": "manual final wins and already includes seed typography",
            })
        rows[key] = row
    output_rows = sorted(rows.values(), key=lambda row: (row["script"], row["sequence"]))
    validation = validate_rows(output_rows, scripts)
    assert validation["stable_id_unique"] and validation["exact_old_guard_pass"]
    allowed = {("scenario.rpa::scenario/011_02.rpy::tid::sentei11_0f96b932", "TARGET_QUOTE_UNBALANCED")}
    post_issues = audit_scripts(scripts, output_rows)
    unexpected = [issue for issue in post_issues if (issue["stable_id"], issue["rule_id"]) not in allowed]
    assert unexpected == [], unexpected
    output = REVIEWS / "ROOT.011_02_and_GH.consolidated.corrections.jsonl"
    report_path = REVIEWS / "ROOT.011_02_and_GH.consolidated.report.json"
    write_jsonl(output, output_rows)
    report = {
        "schema_version": "fatal-twelve-root-011-02-and-gh-consolidated-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "reviewer": "ROOT",
        "scripts": scripts,
        "source_authority": "Japanese source_jp only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "game_executed": False,
        "master_modified": False,
        "exhaustive_checked": sum(len(masters[script]) for script in scripts),
        "coverage": {script: len(masters[script]) for script in scripts},
        "inputs": [
            {"path": str(seed_path.relative_to(ROOT)), "sha256": sha256(seed_path), "selected_records": len(seed_rows), "role": "seed"},
            {"path": str(manual_path.relative_to(ROOT)), "sha256": sha256(manual_path), "selected_records": len(manual_rows), "role": "manual_final"},
        ],
        "corrections": {
            "seed_rows": len(seed_rows),
            "manual_rows": len(manual_rows),
            "overlap_count": len(overlaps),
            "overlap_resolution": overlaps,
            "output_rows": len(output_rows),
            "per_script": dict(Counter(row["script"] for row in output_rows)),
        },
        "record_rule_approvals_deferred_to_global_manifest": [
            {"script": "011_02", "sequence": 124, "rule_id": "TARGET_QUOTE_UNBALANCED"},
        ],
        "validation": {
            **validation,
            "post_correction_audit_issue_count": len(post_issues),
            "post_correction_unapproved_issue_count": len(unexpected),
            "post_correction_approved_issues": post_issues,
        },
        "ruby_map": {"path": str(RUBY_MAP.relative_to(ROOT)), "sha256": sha256(RUBY_MAP)},
        "output": {"path": str(output.relative_to(ROOT)), "sha256": sha256(output)},
        "verdict": "PASS",
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    return output, report_path, output_rows


def main() -> None:
    built = []
    for builder in (build_a001, update_a003_004, build_c007, build_root_011):
        output, report, rows = builder()
        built.append({
            "output": str(output.relative_to(ROOT)),
            "output_sha256": sha256(output),
            "report": str(report.relative_to(ROOT)),
            "report_sha256": sha256(report),
            "rows": len(rows),
        })
    print(json.dumps({"built": built, "ruby_map_sha256": sha256(RUBY_MAP)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
