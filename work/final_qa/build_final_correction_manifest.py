from __future__ import annotations

import copy
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import audit_master


ROOT = Path(__file__).resolve().parent
WORK = ROOT.parent
REVIEWS = ROOT / "reviews"
MASTERS = ROOT / "output" / "masters"
MANIFEST = REVIEWS / "global_correction_manifest.json"
REPORT = REVIEWS / "global_correction_manifest.validation.json"
RUBY_MAP = ROOT / "ruby_map.approved.json"
STRUCTURAL_SPEC = REVIEWS / "structural_fixes_spec.json"
APPROVALS = REVIEWS / "qa_approvals.draft.json"
SUPPLEMENT = WORK / "system_ui" / "runtime_application" / "numeral_composed_string_keys.ko.rpy"
EXPECTED_RENDER_GLOBAL_STRING_OLD_KEYS = 797


SCENARIOS = [
    "001", "002", "003", "004", "005_1", "005_2", "006", "007_1", "007_2", "008",
    "009", "010", "011_01", "011_01F", "011_01G", "011_01H", "011_02", "011_02GH",
    "012_01F", "012_01GH", "012_02", "BAD_END_01", "BAD_END_02", "BAD_END_03",
    "BAD_END_04", "MIHARU_END", "NG_plus", "TRUE_END", "UNHAPPY_END",
]


CORRECTION_FILES = [
    ("A", "A.001.consolidated.corrections.jsonl"),
    ("A", "A.002.consolidated.corrections.jsonl"),
    ("A", "A.003_004.consolidated.corrections.jsonl"),
    ("A", "A.endings.consolidated.corrections.jsonl"),
    ("A", "A.manual.system_ui.corrections.jsonl"),
    ("B", "B.005_1_005_2_006.consolidated.corrections.jsonl"),
    ("C", "C.007_1_007_2.consolidated.corrections.jsonl"),
    ("C", "C.008.consolidated.corrections.jsonl"),
    ("C", "C.011_01.consolidated.corrections.jsonl"),
    ("C", "C.011_01FGH.consolidated.corrections.jsonl"),
    ("C", "C.NG_plus.consolidated.corrections.jsonl"),
    ("ROOT", "ROOT.009.consolidated.corrections.jsonl"),
    ("ROOT", "ROOT.010.consolidated.corrections.jsonl"),
    ("ROOT", "ROOT.011_02_and_GH.consolidated.corrections.jsonl"),
    ("ROOT", "ROOT.012_01F.consolidated.corrections.jsonl"),
    ("ROOT", "ROOT.012_01GH.consolidated.corrections.jsonl"),
    ("ROOT", "ROOT.012_02.consolidated.corrections.jsonl"),
    ("ROOT", "ROOT.base_numeric_token_fixes.corrections.jsonl"),
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def text_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", "surrogatepass")).hexdigest()


def workspace_path(path: Path) -> str:
    return path.resolve().relative_to(WORK.parent.resolve()).as_posix()


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def load_master(script: str) -> tuple[Path, dict, list[dict]]:
    path = MASTERS / ("system_ui.master.json" if script == "system_ui" else f"scenario_{script}.master.json")
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    entries = payload["entries"]
    if script != "system_ui":
        assert payload["script_key"] == script
        assert [row["sequence"] for row in entries] == list(range(1, len(entries) + 1))
    assert len({row["stable_id"] for row in entries}) == len(entries)
    return path, payload, entries


def main() -> None:
    if len(SCENARIOS) != 29 or len(CORRECTION_FILES) != 18:
        raise SystemExit("manifest universe mismatch")

    master_by_id: dict[str, tuple[str, dict]] = {}
    master_inventory = {}
    master_entries = {}
    for script in [*SCENARIOS, "system_ui"]:
        path, payload, entries = load_master(script)
        master_entries[script] = entries
        master_inventory[script] = {
            "path": workspace_path(path),
            "sha256": sha256(path),
            "records": len(entries),
            "source_authority": payload.get("source_authority"),
            "english_reference_used": payload.get("english_reference_used"),
            "external_translation_api_used": payload.get("external_translation_api_used"),
        }
        for row in entries:
            if row["stable_id"] in master_by_id:
                raise SystemExit(f"duplicate master stable_id: {row['stable_id']}")
            master_by_id[row["stable_id"]] = (script, row)
    scenario_master_records = sum(len(master_entries[script]) for script in SCENARIOS)
    assert scenario_master_records == 18184

    correction_inventory = []
    all_rows = []
    input_hashes_before = {}
    for reviewer, filename in CORRECTION_FILES:
        path = REVIEWS / filename
        input_hashes_before[filename] = sha256(path)
        rows = load_jsonl(path)
        per_script = Counter()
        failures = []
        for index, row in enumerate(rows, 1):
            required = {"script", "stable_id", "sequence", "old_ko", "new_ko", "category", "reason", "reviewer"}
            if not required.issubset(row):
                failures.append({"line": index, "reason": "missing required field", "missing": sorted(required - set(row))})
                continue
            joined = master_by_id.get(row["stable_id"])
            if joined is None:
                failures.append({"line": index, "stable_id": row["stable_id"], "reason": "no master join"})
                continue
            script, master = joined
            if row["script"] != script or int(row["sequence"]) != master["sequence"]:
                failures.append({"line": index, "stable_id": row["stable_id"], "reason": "script/sequence identity mismatch"})
            if row["old_ko"] != master["draft_ko"]:
                failures.append({"line": index, "stable_id": row["stable_id"], "reason": "exact old guard mismatch"})
            if row["new_ko"] == row["old_ko"]:
                failures.append({"line": index, "stable_id": row["stable_id"], "reason": "no-op correction"})
            if row["reviewer"] != reviewer:
                failures.append({"line": index, "stable_id": row["stable_id"], "reason": "reviewer mismatch"})
            per_script[script] += 1
            all_rows.append({**row, "source_file": workspace_path(path), "manifest_reviewer": reviewer})
        if failures:
            raise SystemExit(json.dumps({"file": filename, "failures": failures}, ensure_ascii=False, indent=2))
        correction_inventory.append({
            "reviewer": reviewer,
            "path": workspace_path(path),
            "sha256": input_hashes_before[filename],
            "records": len(rows),
            "scripts": dict(sorted(per_script.items())),
        })

    by_stable_id = defaultdict(list)
    by_script_sequence = defaultdict(list)
    for row in all_rows:
        by_stable_id[row["stable_id"]].append(row)
        by_script_sequence[(row["script"], int(row["sequence"]))].append(row)
    duplicate_ids = {key: rows for key, rows in by_stable_id.items() if len(rows) > 1}
    duplicate_sequences = {key: rows for key, rows in by_script_sequence.items() if len(rows) > 1}
    if duplicate_ids or duplicate_sequences:
        raise SystemExit(json.dumps({
            "duplicate_stable_ids": duplicate_ids,
            "duplicate_script_sequences": {f"{key[0]}:{key[1]}": value for key, value in duplicate_sequences.items()},
        }, ensure_ascii=False, indent=2))

    final_target = {}
    for script, entries in master_entries.items():
        for entry in entries:
            final_target[entry["stable_id"]] = entry["draft_ko"]
    for row in all_rows:
        final_target[row["stable_id"]] = row["new_ko"]

    overlay = json.loads(STRUCTURAL_SPEC.read_text(encoding="utf-8-sig"))
    assert overlay["records"] == len(overlay["entries"]) == 178
    overlay_failures = []
    for row in overlay["entries"]:
        joined = master_by_id.get(row["stable_id"])
        if joined is None or joined[0] != row["script"] or joined[1]["sequence"] != row["sequence"]:
            overlay_failures.append({"stable_id": row["stable_id"], "reason": "identity mismatch"})
        elif final_target[row["stable_id"]] != row["final_ko"]:
            overlay_failures.append({
                "stable_id": row["stable_id"],
                "reason": "final target mismatch",
                "expected": row["final_ko"],
                "actual": final_target[row["stable_id"]],
            })
        elif text_sha256(row["final_ko"]) != row["final_ko_sha256"]:
            overlay_failures.append({"stable_id": row["stable_id"], "reason": "spec final hash mismatch"})
    assert overlay_failures == [], overlay_failures

    approvals = json.loads(APPROVALS.read_text(encoding="utf-8-sig"))
    assert approvals["blanket_approvals"] is False
    assert approvals["records"] == len(approvals["entries"]) == 10
    approval_index = {}
    approval_verification = []
    for row in approvals["entries"]:
        script, master = master_by_id[row["stable_id"]]
        target = final_target[row["stable_id"]]
        passed = (
            script == row["script"]
            and master["sequence"] == row["sequence"]
            and text_sha256(master["source_jp"]) == row["source_sha256"]
            and text_sha256(target) == row["target_sha256"]
        )
        approval_verification.append({
            "script": script,
            "sequence": master["sequence"],
            "stable_id": row["stable_id"],
            "rule_id": row["rule_id"],
            "source_target_hash_guard_pass": passed,
        })
        if not passed:
            raise SystemExit(f"approval hash guard failed: {row['stable_id']}:{row['rule_id']}")
        key = (row["stable_id"], row["rule_id"], row["source_sha256"], row["target_sha256"])
        if key in approval_index:
            raise SystemExit(f"duplicate approval key: {key}")
        approval_index[key] = row

    ruby_map = audit_master.load_ruby_map(RUBY_MAP)
    issues = []
    for script in SCENARIOS:
        for source in master_entries[script]:
            entry = copy.deepcopy(source)
            entry["draft_ko"] = final_target[entry["stable_id"]]
            audit_master.audit_entry(entry, script, issues, ruby_map=ruby_map)
    approved_scenario_issues = []
    unapproved_scenario_issues = []
    used_approval_keys = set()
    for issue in issues:
        key = (issue["stable_id"], issue["rule_id"], issue["source_sha256"], issue["target_sha256"])
        if key in approval_index:
            approved_scenario_issues.append(issue)
            used_approval_keys.add(key)
        else:
            unapproved_scenario_issues.append(issue)
    scenario_approval_keys = {
        key for key, row in approval_index.items() if row["scope"] == "scenario"
    }
    unused_scenario_approvals = sorted(scenario_approval_keys - used_approval_keys)
    if unapproved_scenario_issues or unused_scenario_approvals:
        raise SystemExit(json.dumps({
            "unapproved_scenario_issues": unapproved_scenario_issues,
            "unused_scenario_approvals": unused_scenario_approvals,
        }, ensure_ascii=False, indent=2))

    supplement_text = SUPPLEMENT.read_text(encoding="utf-8-sig")
    supplement_pairs = len(re.findall(r'^\s*old\s+"Numeral\s+[IVXLCDM]+"\s*$', supplement_text, flags=re.MULTILINE))
    assert supplement_pairs == 12

    input_hashes_after = {filename: sha256(REVIEWS / filename) for _, filename in CORRECTION_FILES}
    assert input_hashes_before == input_hashes_after
    scenario_correction_count = sum(1 for row in all_rows if row["script"] != "system_ui")
    ui_correction_count = sum(1 for row in all_rows if row["script"] == "system_ui")
    assert scenario_correction_count == 2472
    assert ui_correction_count == 167
    assert len(all_rows) == len(by_stable_id) == 2639

    component_conflict_report = REVIEWS / "ROOT.011_02_and_GH.consolidated.report.json"
    component_conflict_history = json.loads(component_conflict_report.read_text(encoding="utf-8-sig"))["corrections"]["overlap_resolution"]
    assert len(component_conflict_history) == 4

    manifest = {
        "schema_version": "fatal-twelve-global-correction-manifest-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "correction_files": [
            {key: item[key] for key in ("reviewer", "path", "sha256", "records")}
            for item in correction_inventory
        ],
        "supplemental_strings": [{
            "path": workspace_path(SUPPLEMENT),
            "sha256": sha256(SUPPLEMENT),
            "pairs": supplement_pairs,
        }],
        "policy_artifacts": [
            {
                "kind": "ruby_map",
                "path": workspace_path(RUBY_MAP),
                "sha256": sha256(RUBY_MAP),
                "entries": len(json.loads(RUBY_MAP.read_text(encoding="utf-8-sig"))["entries"]),
            },
            {
                "kind": "structural_overlay_spec",
                "path": workspace_path(STRUCTURAL_SPEC),
                "sha256": sha256(STRUCTURAL_SPEC),
                "records": overlay["records"],
                "status": "fully_merged_into_canonical_correction_rows",
            },
            {
                "kind": "record_bound_qa_approvals",
                "path": workspace_path(APPROVALS),
                "sha256": sha256(APPROVALS),
                "records": approvals["records"],
                "blanket_approvals": False,
            },
        ],
        "scope": {
            "scenario_count": len(SCENARIOS),
            "scenario_master_records": scenario_master_records,
            "scenario_corrections": scenario_correction_count,
            "system_ui_master_records": len(master_entries["system_ui"]),
            "system_ui_corrections": ui_correction_count,
            "expected_render_global_string_old_keys": EXPECTED_RENDER_GLOBAL_STRING_OLD_KEYS,
            "total_unique_corrections": len(all_rows),
        },
        "validation": {
            "exact_old_guard_pass": True,
            "stable_id_unique": True,
            "script_sequence_unique": True,
            "structural_overlay_merged": overlay["records"],
            "record_bound_approvals_verified": approvals["records"],
            "scenario_preflight_unapproved_issues": 0,
            "scenario_preflight_approved_issues": len(approved_scenario_issues),
            "historical_component_conflicts_materialized": len(component_conflict_history),
        },
        "actions_not_performed": ["master apply", "corrected master generation", "RPY render", "game execution"],
    }
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    report = {
        "schema_version": "fatal-twelve-global-correction-manifest-validation-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "manifest": {"path": workspace_path(MANIFEST), "sha256": sha256(MANIFEST)},
        "summary": {
            "correction_files": len(correction_inventory),
            "scenario_count": len(SCENARIOS),
            "scenario_master_records": scenario_master_records,
            "scenario_corrections": scenario_correction_count,
            "system_ui_master_records": len(master_entries["system_ui"]),
            "system_ui_corrections": ui_correction_count,
            "expected_render_global_string_old_keys": EXPECTED_RENDER_GLOBAL_STRING_OLD_KEYS,
            "total_unique_corrections": len(all_rows),
            "duplicate_stable_ids": len(duplicate_ids),
            "duplicate_script_sequences": len(duplicate_sequences),
            "historical_component_conflicts_materialized": len(component_conflict_history),
            "exact_old_guard_failures": 0,
            "structural_overlay_records": overlay["records"],
            "structural_overlay_failures": len(overlay_failures),
            "record_bound_approvals": approvals["records"],
            "scenario_preflight_approved_issues": len(approved_scenario_issues),
            "historical_component_conflicts_materialized": len(component_conflict_history),
            "scenario_preflight_unapproved_issues": len(unapproved_scenario_issues),
            "unused_scenario_approvals": len(unused_scenario_approvals),
            "supplemental_string_pairs": supplement_pairs,
            "verdict": "PASS",
        },
        "correction_file_inventory": correction_inventory,
        "per_script_correction_counts": dict(sorted(Counter(row["script"] for row in all_rows).items())),
        "master_inventory": master_inventory,
        "duplicate_conflict_ledger": [],
        "materialized_component_conflict_history": {
            "source_report": {"path": workspace_path(component_conflict_report), "sha256": sha256(component_conflict_report)},
            "records": component_conflict_history,
        },
        "structural_overlay": {
            "path": workspace_path(STRUCTURAL_SPEC),
            "sha256": sha256(STRUCTURAL_SPEC),
            "records": overlay["records"],
            "by_transform": overlay["by_transform"],
            "failures": overlay_failures,
        },
        "record_bound_approvals": {
            "path": workspace_path(APPROVALS),
            "sha256": sha256(APPROVALS),
            "records": approvals["records"],
            "verification": approval_verification,
            "approved_scenario_issues": [
                {key: issue.get(key) for key in ("script", "sequence", "stable_id", "rule_id", "source_sha256", "target_sha256")}
                for issue in approved_scenario_issues
            ],
            "unapproved_scenario_issues": unapproved_scenario_issues,
            "unused_scenario_approvals": unused_scenario_approvals,
        },
        "selected_input_immutability": {
            "sha256_before": dict(sorted(input_hashes_before.items())),
            "sha256_after": dict(sorted(input_hashes_after.items())),
            "pass": input_hashes_before == input_hashes_after,
        },
        "supplemental_strings": manifest["supplemental_strings"],
        "ruby_map": manifest["policy_artifacts"][0],
        "actions_not_performed": manifest["actions_not_performed"],
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({
        "manifest": workspace_path(MANIFEST),
        "manifest_sha256": sha256(MANIFEST),
        "report": workspace_path(REPORT),
        "report_sha256": sha256(REPORT),
        **report["summary"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
