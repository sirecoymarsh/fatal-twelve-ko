from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parent
REVIEWS = BASE / "reviews"
MASTERS = BASE / "output" / "masters"
MANIFEST_PATH = REVIEWS / "global_correction_manifest.draft.json"
REPORT_PATH = REVIEWS / "global_correction_manifest.inventory_report.json"


SCENARIOS = [
    "001", "002", "003", "004", "005_1", "005_2", "006", "007_1", "007_2", "008",
    "009", "010", "011_01", "011_01F", "011_01G", "011_01H", "011_02", "011_02GH",
    "012_01F", "012_01GH", "012_02", "BAD_END_01", "BAD_END_02", "BAD_END_03",
    "BAD_END_04", "MIHARU_END", "NG_plus", "TRUE_END", "UNHAPPY_END",
]


# The file is selected only for rows matching script_filter. A grouped file can therefore
# be the selected source for several scenarios without duplicating records globally.
SELECTIONS = {
    "001": [("A.001.consolidated.corrections.jsonl", "consolidated")],
    "002": [("A.002.consolidated.corrections.jsonl", "consolidated")],
    "003": [("A.003_004.consolidated.corrections.jsonl", "consolidated")],
    "004": [("A.003_004.consolidated.corrections.jsonl", "consolidated")],
    "005_1": [("B.005_1_005_2_006.consolidated.corrections.jsonl", "consolidated")],
    "005_2": [("B.005_1_005_2_006.consolidated.corrections.jsonl", "consolidated")],
    "006": [("B.005_1_005_2_006.consolidated.corrections.jsonl", "consolidated")],
    "007_1": [("C.007_1_007_2.consolidated.corrections.jsonl", "consolidated")],
    "007_2": [("C.007_1_007_2.consolidated.corrections.jsonl", "consolidated")],
    "008": [("C.008.consolidated.corrections.jsonl", "consolidated")],
    "009": [("ROOT.009.consolidated.corrections.jsonl", "consolidated")],
    "010": [("ROOT.010.consolidated.corrections.jsonl", "consolidated")],
    "011_01": [("C.011_01.consolidated.corrections.jsonl", "consolidated")],
    "011_01F": [("C.011_01FGH.consolidated.corrections.jsonl", "consolidated")],
    "011_01G": [("C.011_01FGH.consolidated.corrections.jsonl", "consolidated")],
    "011_01H": [("C.011_01FGH.consolidated.corrections.jsonl", "consolidated")],
    "011_02": [("ROOT.011_02_and_GH.consolidated.corrections.jsonl", "consolidated")],
    "011_02GH": [("ROOT.011_02_and_GH.consolidated.corrections.jsonl", "consolidated")],
    "012_01F": [("ROOT.012_01F.consolidated.corrections.jsonl", "consolidated")],
    "012_01GH": [("ROOT.012_01GH.consolidated.corrections.jsonl", "consolidated")],
    "012_02": [("ROOT.012_02.consolidated.corrections.jsonl", "consolidated")],
    "BAD_END_01": [("A.endings.consolidated.corrections.jsonl", "consolidated")],
    "BAD_END_02": [("A.endings.consolidated.corrections.jsonl", "consolidated")],
    "BAD_END_03": [("A.endings.consolidated.corrections.jsonl", "consolidated")],
    "BAD_END_04": [("A.endings.consolidated.corrections.jsonl", "consolidated")],
    "MIHARU_END": [("A.endings.consolidated.corrections.jsonl", "consolidated")],
    "NG_plus": [("C.NG_plus.consolidated.corrections.jsonl", "consolidated")],
    "TRUE_END": [("A.endings.consolidated.corrections.jsonl", "consolidated")],
    "UNHAPPY_END": [("A.endings.consolidated.corrections.jsonl", "consolidated")],
}


COVERAGE_EVIDENCE = {
    "001": {"status": "verified_partitioned_review_and_consolidated_structural_pass", "formal_verification": True, "evidence": ["reviews/A.001.consolidated.report.json"]},
    "002": {"status": "verified", "formal_verification": True, "evidence": ["reviews/A.002.consolidated.report.json"]},
    "003": {"status": "verified", "formal_verification": True, "evidence": ["reviews/A.003_004.consolidated.report.json"]},
    "004": {"status": "verified", "formal_verification": True, "evidence": ["reviews/A.003_004.consolidated.report.json"]},
    "005_1": {"status": "verified", "formal_verification": True, "evidence": ["reviews/B.005_1_005_2_006.consolidated.report.json"]},
    "005_2": {"status": "verified", "formal_verification": True, "evidence": ["reviews/B.005_1_005_2_006.consolidated.report.json"]},
    "006": {"status": "verified", "formal_verification": True, "evidence": ["reviews/B.005_1_005_2_006.consolidated.report.json"]},
    "007_1": {"status": "verified_consolidated_structural_pass", "formal_verification": True, "evidence": ["reviews/C.007_1_007_2.consolidated.report.json"]},
    "007_2": {"status": "verified_consolidated_structural_pass", "formal_verification": True, "evidence": ["reviews/C.007_1_007_2.consolidated.report.json"]},
    "008": {"status": "verified", "formal_verification": True, "evidence": ["reviews/C.008.consolidated.report.json"]},
    "009": {
        "status": "verified_composite_head_and_tail",
        "formal_verification": True,
        "evidence": ["reviews/ROOT.manual.009_001_0884.report.json", "reviews/ROOT.009.consolidated.report.json"],
    },
    "010": {"status": "verified", "formal_verification": True, "evidence": ["reviews/ROOT.010.consolidated.report.json"]},
    "011_01": {"status": "verified", "formal_verification": True, "evidence": ["reviews/C.011_01.consolidated.report.json"]},
    "011_01F": {"status": "verified", "formal_verification": True, "evidence": ["reviews/C.011_01FGH.consolidated.report.json"]},
    "011_01G": {"status": "verified", "formal_verification": True, "evidence": ["reviews/C.011_01FGH.consolidated.report.json"]},
    "011_01H": {"status": "verified", "formal_verification": True, "evidence": ["reviews/C.011_01FGH.consolidated.report.json"]},
    "011_02": {"status": "verified_consolidated", "formal_verification": True, "evidence": ["reviews/ROOT.011_02_and_GH.consolidated.report.json"]},
    "011_02GH": {"status": "verified_consolidated", "formal_verification": True, "evidence": ["reviews/ROOT.011_02_and_GH.consolidated.report.json"]},
    "012_01F": {"status": "verified", "formal_verification": True, "evidence": ["reviews/ROOT.012_01F.consolidated.report.json"]},
    "012_01GH": {"status": "verified", "formal_verification": True, "evidence": ["reviews/ROOT.012_01GH.consolidated.report.json"]},
    "012_02": {"status": "verified", "formal_verification": True, "evidence": ["reviews/ROOT.012_02.consolidated.report.json"]},
    "BAD_END_01": {"status": "verified", "formal_verification": True, "evidence": ["reviews/A.endings.consolidated.report.json"]},
    "BAD_END_02": {"status": "verified", "formal_verification": True, "evidence": ["reviews/A.endings.consolidated.report.json"]},
    "BAD_END_03": {"status": "verified_zero_corrections", "formal_verification": True, "evidence": ["reviews/A.endings.consolidated.report.json"]},
    "BAD_END_04": {"status": "verified", "formal_verification": True, "evidence": ["reviews/A.endings.consolidated.report.json"]},
    "MIHARU_END": {"status": "verified_zero_corrections", "formal_verification": True, "evidence": ["reviews/A.endings.consolidated.report.json"]},
    "NG_plus": {"status": "verified", "formal_verification": True, "evidence": ["reviews/C.NG_plus.consolidated.report.json"]},
    "TRUE_END": {"status": "verified", "formal_verification": True, "evidence": ["reviews/A.endings.consolidated.report.json"]},
    "UNHAPPY_END": {"status": "verified", "formal_verification": True, "evidence": ["reviews/A.endings.consolidated.report.json"]},
}


READINESS = {}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_records(path: Path) -> list[dict]:
    if path.suffix.lower() == ".jsonl":
        return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
    if path.suffix.lower() == ".tsv":
        return list(csv.DictReader(path.read_text(encoding="utf-8-sig").splitlines(), delimiter="\t"))
    payload = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and isinstance(payload.get("corrections"), list):
        return payload["corrections"]
    return []


def correction_records(path: Path) -> list[dict]:
    return [record for record in load_records(path) if isinstance(record, dict) and isinstance(record.get("new_ko"), str)]


def record_script(record: dict) -> str:
    return str(record.get("script") or record.get("script_key") or "")


def master_path(script: str) -> Path:
    return MASTERS / f"scenario_{script}.master.json"


def main() -> None:
    if set(SELECTIONS) != set(SCENARIOS) or set(COVERAGE_EVIDENCE) != set(SCENARIOS):
        raise SystemExit("scenario mapping is not exactly 29 scripts")

    master_entries = {}
    master_by_sequence = {}
    master_by_id = {}
    master_inventory = {}
    for script in SCENARIOS:
        path = master_path(script)
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        entries = payload["entries"]
        if payload.get("script_key") != script:
            raise SystemExit(f"master script mismatch: {script}")
        if [entry["sequence"] for entry in entries] != list(range(1, len(entries) + 1)):
            raise SystemExit(f"non-contiguous master: {script}")
        master_entries[script] = entries
        master_by_sequence[script] = {entry["sequence"]: entry for entry in entries}
        master_inventory[script] = {
            "path": str(path.relative_to(BASE)),
            "sha256": sha256(path),
            "records": len(entries),
            "source_authority": payload.get("source_authority"),
            "english_reference_used": payload.get("english_reference_used"),
            "external_translation_api_used": payload.get("external_translation_api_used"),
        }
        for entry in entries:
            if entry["stable_id"] in master_by_id:
                raise SystemExit(f"duplicate master stable_id: {entry['stable_id']}")
            master_by_id[entry["stable_id"]] = (script, entry)
    total_master_records = sum(len(entries) for entries in master_entries.values())
    if len(SCENARIOS) != 29 or total_master_records != 18184:
        raise SystemExit(f"master universe mismatch: {len(SCENARIOS)} scripts, {total_master_records} records")

    candidate_inventory = []
    candidate_hashes_before = {}
    for path in sorted(REVIEWS.iterdir()):
        if not path.is_file() or path in {MANIFEST_PATH, REPORT_PATH}:
            continue
        if path.suffix.lower() not in {".json", ".jsonl", ".tsv"}:
            continue
        records = correction_records(path)
        if not records:
            continue
        candidate_hashes_before[path.name] = sha256(path)
        scripts = Counter(record_script(record) for record in records)
        stable_ids = [record.get("stable_id") for record in records if record.get("stable_id")]
        script_sequence = [(record_script(record), int(record["sequence"])) for record in records]
        old_guard_checked = 0
        old_guard_failures = []
        stable_id_identity_failures = []
        for record in records:
            script = record_script(record)
            sequence = int(record["sequence"])
            entry = master_by_sequence.get(script, {}).get(sequence)
            if entry is None:
                old_guard_failures.append({"script": script, "sequence": sequence, "reason": "no master join"})
                continue
            if record.get("old_ko") is not None:
                old_guard_checked += 1
                if record["old_ko"] != entry["draft_ko"]:
                    old_guard_failures.append({"script": script, "sequence": sequence, "stable_id": entry["stable_id"]})
            if record.get("stable_id") is not None and record["stable_id"] != entry["stable_id"]:
                stable_id_identity_failures.append({"script": script, "sequence": sequence, "provided": record["stable_id"], "master": entry["stable_id"]})
        selected_for = sorted(script for script, selections in SELECTIONS.items() if any(name == path.name for name, _ in selections))
        if path.name == "A.manual.system_ui.corrections.jsonl":
            disposition = "selected_non_scenario_companion"
        elif selected_for:
            disposition = "selected_or_selected_component"
        elif path.name == "ROOT.manual.010_001_0480.corrections.jsonl":
            disposition = "superseded_invalid_question_mark_damage"
        else:
            disposition = "superseded_or_intermediate_not_selected"
        candidate_inventory.append({
            "path": str(path.relative_to(BASE)),
            "sha256": candidate_hashes_before[path.name],
            "format": path.suffix.lower().lstrip("."),
            "records": len(records),
            "scripts": dict(sorted(scripts.items())),
            "stable_id_present": len(stable_ids),
            "stable_id_unique": len(set(stable_ids)),
            "internal_duplicate_stable_id_count": len(stable_ids) - len(set(stable_ids)),
            "internal_duplicate_script_sequence_count": len(script_sequence) - len(set(script_sequence)),
            "old_guard_checked": old_guard_checked,
            "old_guard_failure_count": len(old_guard_failures),
            "old_guard_failures": old_guard_failures,
            "stable_id_identity_failure_count": len(stable_id_identity_failures),
            "stable_id_identity_failures": stable_id_identity_failures,
            "selected_for_scenarios": selected_for,
            "disposition": disposition,
        })

    logical_records = []
    scenario_entries = []
    for script in SCENARIOS:
        selected_inputs = []
        raw_count = 0
        missing_stable = 0
        missing_old = 0
        for filename, role in SELECTIONS[script]:
            path = REVIEWS / filename
            records = [record for record in correction_records(path) if record_script(record) == script]
            selected_inputs.append({
                "path": str(path.relative_to(BASE)),
                "sha256": sha256(path),
                "format": path.suffix.lower().lstrip("."),
                "script_filter": script,
                "role": role,
                "selected_records": len(records),
                "has_stable_id_for_every_record": all(record.get("stable_id") for record in records),
                "has_old_ko_for_every_record": all(record.get("old_ko") is not None for record in records),
            })
            raw_count += len(records)
            for record in records:
                sequence = int(record["sequence"])
                entry = master_by_sequence[script].get(sequence)
                if entry is None:
                    raise SystemExit(f"selected row has no master join: {filename}:{script}:{sequence}")
                stable_id = record.get("stable_id") or entry["stable_id"]
                old_ko = record.get("old_ko") if record.get("old_ko") is not None else entry["draft_ko"]
                if record.get("stable_id") is None:
                    missing_stable += 1
                if record.get("old_ko") is None:
                    missing_old += 1
                if stable_id != entry["stable_id"] or old_ko != entry["draft_ko"]:
                    raise SystemExit(f"selected identity/old guard mismatch: {filename}:{script}:{sequence}")
                logical_records.append({
                    "script": script,
                    "sequence": sequence,
                    "stable_id": stable_id,
                    "old_ko": old_ko,
                    "new_ko": record["new_ko"],
                    "category": record.get("category"),
                    "reason": record.get("reason") or record.get("note"),
                    "source_file": str(path.relative_to(BASE)),
                    "source_role": role,
                    "source_had_stable_id": record.get("stable_id") is not None,
                    "source_had_old_ko": record.get("old_ko") is not None,
                })
        apply_ready, readiness_reason = READINESS.get(script, (True, "selected correction set is stable-id keyed and conflict-free"))
        coverage = COVERAGE_EVIDENCE[script]
        scenario_entries.append({
            "script": script,
            "master": master_inventory[script],
            "coverage": {
                "expected_records": len(master_entries[script]),
                "claimed_checked_records": len(master_entries[script]),
                **coverage,
            },
            "selected_inputs": selected_inputs,
            "selected_raw_records": raw_count,
            "legacy_records_missing_stable_id": missing_stable,
            "legacy_records_missing_old_ko": missing_old,
            "apply_ready": apply_ready,
            "readiness_reason": readiness_reason,
        })

    by_stable_id = defaultdict(list)
    for record in logical_records:
        by_stable_id[record["stable_id"]].append(record)
    exact_duplicates = []
    conflicts = []
    for stable_id, records in by_stable_id.items():
        if len(records) == 1:
            continue
        base = {
            "stable_id": stable_id,
            "script": records[0]["script"],
            "sequence": records[0]["sequence"],
            "records": records,
            "old_ko_all_equal": len({record["old_ko"] for record in records}) == 1,
            "new_ko_all_equal": len({record["new_ko"] for record in records}) == 1,
        }
        if base["new_ko_all_equal"]:
            exact_duplicates.append(base)
        else:
            manual_records = [record for record in records if record["source_role"] == "manual_final"]
            seed_records = [record for record in records if record["source_role"] == "seed_component"]
            if base["script"] == "011_02GH" and len(manual_records) == 1 and len(seed_records) == 1:
                base["resolution"] = {
                    "status": "resolved_by_declared_precedence",
                    "policy": "manual_final supersedes seed_component when the manual final text already reflects seed mechanics",
                    "winner_source_file": manual_records[0]["source_file"],
                    "final_new_ko": manual_records[0]["new_ko"],
                }
            else:
                base["resolution"] = {"status": "unresolved"}
            conflicts.append(base)

    conflict_ids = {item["stable_id"] for item in conflicts}
    duplicate_ids = {item["stable_id"] for item in exact_duplicates}
    resolved_records = {}
    for stable_id, records in by_stable_id.items():
        if stable_id in conflict_ids:
            conflict = next(item for item in conflicts if item["stable_id"] == stable_id)
            if conflict["resolution"]["status"] != "resolved_by_declared_precedence":
                continue
            winner = next(record for record in records if record["source_file"] == conflict["resolution"]["winner_source_file"])
            resolved_records[stable_id] = winner
        else:
            resolved_records[stable_id] = records[0]
    unresolved_conflicts = [item for item in conflicts if item["resolution"]["status"] == "unresolved"]

    for scenario in scenario_entries:
        script = scenario["script"]
        script_logical = [record for record in logical_records if record["script"] == script]
        script_unique = {record["stable_id"] for record in script_logical}
        script_conflicts = [item for item in conflicts if item["script"] == script]
        scenario["selected_unique_stable_ids_before_resolution"] = len(script_unique)
        scenario["duplicate_or_conflict_stable_ids"] = len(script_logical) - len(script_unique)
        scenario["conflict_count"] = len(script_conflicts)
        scenario["resolved_unique_corrections"] = len([record for record in resolved_records.values() if record["script"] == script])

    selected_hashes_after = {}
    for script, selections in SELECTIONS.items():
        for filename, _ in selections:
            selected_hashes_after[filename] = sha256(REVIEWS / filename)
    selected_hashes_before = {name: candidate_hashes_before[name] for name in selected_hashes_after}
    if selected_hashes_before != selected_hashes_after:
        raise SystemExit("selected correction input changed during inventory")

    formal_verified_records = sum(
        len(master_entries[item["script"]]) for item in scenario_entries if item["coverage"]["formal_verification"]
    )
    readiness_counts = Counter("ready" if item["apply_ready"] else "needs_consolidation" for item in scenario_entries)
    component_conflict_report = REVIEWS / "ROOT.011_02_and_GH.consolidated.report.json"
    component_conflict_history = json.loads(component_conflict_report.read_text(encoding="utf-8-sig"))["corrections"]["overlap_resolution"]
    if len(component_conflict_history) != 4:
        raise SystemExit("materialized component conflict history mismatch")
    manifest = {
        "schema_version": "fatal-twelve-global-correction-manifest-draft-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "draft_do_not_apply",
        "scope": {
            "scenario_count": len(SCENARIOS),
            "scenario_master_records": total_master_records,
            "system_ui_included_in_scenario_count": False,
            "system_ui_companion": {
                "path": "reviews/A.manual.system_ui.corrections.jsonl",
                "sha256": sha256(REVIEWS / "A.manual.system_ui.corrections.jsonl"),
                "records": len([record for record in correction_records(REVIEWS / "A.manual.system_ui.corrections.jsonl") if record_script(record) == "system_ui"]),
                "status": "separate_companion_not_part_of_29_scenarios",
            },
        },
        "selection_policy": [
            "Prefer a script's consolidated correction artifact over every seed/manual component it supersedes.",
            "When a consolidated artifact contains several scripts, select only rows matching that scenario's script key.",
            "Every selected canonical correction row is stable-id keyed and exact-joined to the authoritative master.",            "Zero-correction scripts retain a selected consolidated coverage artifact and an empty row set.",
        ],
        "future_output": {
            "canonical_manifest_path": "reviews/global_correction_manifest.json",
            "status": "all scenario selections consolidated; no master apply/render performed by inventory task",
        },
        "scenarios": scenario_entries,
        "selected_union": {
            "raw_records": len(logical_records),
            "unique_stable_ids_before_resolution": len(by_stable_id),
            "exact_duplicate_stable_id_count": len(exact_duplicates),
            "conflicting_stable_id_count": len(conflicts),
            "resolved_conflicting_stable_id_count": len(conflicts) - len(unresolved_conflicts),
            "unresolved_conflicting_stable_id_count": len(unresolved_conflicts),
            "resolved_unique_correction_count": len(resolved_records),
            "legacy_source_records_missing_stable_id": sum(not record["source_had_stable_id"] for record in logical_records),
            "legacy_source_records_missing_old_ko": sum(not record["source_had_old_ko"] for record in logical_records),
        },
        "readiness": {
            "apply_ready_scenarios": readiness_counts["ready"],
            "needs_consolidation_scenarios": readiness_counts["needs_consolidation"],
            "apply_ready_script_keys": [item["script"] for item in scenario_entries if item["apply_ready"]],
            "needs_consolidation_script_keys": [item["script"] for item in scenario_entries if not item["apply_ready"]],
            "global_apply_ready": readiness_counts["needs_consolidation"] == 0 and not unresolved_conflicts,
        },
        "coverage": {
            "claimed_checked_records": total_master_records,
            "formally_verified_records": formal_verified_records,
            "provisional_records": total_master_records - formal_verified_records,
            "formally_verified_scenarios": sum(item["coverage"]["formal_verification"] for item in scenario_entries),
            "provisional_scenarios": sum(not item["coverage"]["formal_verification"] for item in scenario_entries),
        },
        "conflict_ledger": conflicts,
        "exact_duplicate_ledger": exact_duplicates,
        "materialized_component_conflict_history": component_conflict_history,
        "selected_input_sha256_snapshot": dict(sorted(selected_hashes_after.items())),
        "actions_not_performed": ["master apply", "corrected master generation", "RPY render", "game execution"],
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    report = {
        "schema_version": "fatal-twelve-global-correction-inventory-report-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "manifest": {
            "path": str(MANIFEST_PATH.relative_to(BASE)),
            "sha256": sha256(MANIFEST_PATH),
            "status": manifest["status"],
        },
        "summary": {
            "scenario_count": len(SCENARIOS),
            "master_records": total_master_records,
            "candidate_correction_files": len(candidate_inventory),
            "selected_distinct_files": len(selected_hashes_after),
            "selected_raw_records": len(logical_records),
            "selected_unique_stable_ids": len(by_stable_id),
            "resolved_final_unique_corrections": len(resolved_records),
            "raw_duplicate_or_conflict_rows": len(logical_records) - len(by_stable_id),
            "exact_duplicates": len(exact_duplicates),
            "new_text_conflicts": len(conflicts),
            "historical_component_conflicts_materialized": len(component_conflict_history),
            "resolved_conflicts": len(conflicts) - len(unresolved_conflicts),
            "unresolved_conflicts": len(unresolved_conflicts),
            "old_guard_failures_in_selected_rows": 0,
            "apply_ready_scenarios": readiness_counts["ready"],
            "needs_consolidation_scenarios": readiness_counts["needs_consolidation"],
        },
        "coverage": manifest["coverage"],
        "needs_consolidation": [
            {"script": item["script"], "reason": item["readiness_reason"]}
            for item in scenario_entries if not item["apply_ready"]
        ],
        "conflicts_preserving_old_new_and_source": conflicts,
        "materialized_component_conflicts_preserving_old_new_and_source": {
            "source_report": {"path": str(component_conflict_report.relative_to(BASE)), "sha256": sha256(component_conflict_report)},
            "records": component_conflict_history,
        },
        "candidate_file_inventory": candidate_inventory,
        "selected_input_immutability": {
            "sha256_before": dict(sorted(selected_hashes_before.items())),
            "sha256_after": dict(sorted(selected_hashes_after.items())),
            "pass": selected_hashes_before == selected_hashes_after,
        },
        "master_inventory": master_inventory,
        "actions_not_performed": manifest["actions_not_performed"],
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({
        "manifest": str(MANIFEST_PATH),
        "manifest_sha256": sha256(MANIFEST_PATH),
        "report": str(REPORT_PATH),
        "report_sha256": sha256(REPORT_PATH),
        "scenario_count": len(SCENARIOS),
        "master_records": total_master_records,
        "selected_raw_records": len(logical_records),
        "resolved_unique_corrections": len(resolved_records),
        "conflicts": len(conflicts),
        "unresolved_conflicts": len(unresolved_conflicts),
        "apply_ready_scenarios": readiness_counts["ready"],
        "needs_consolidation_scenarios": readiness_counts["needs_consolidation"],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
