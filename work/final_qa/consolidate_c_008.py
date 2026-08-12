#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MASTER = ROOT / "output" / "masters" / "scenario_008.master.json"
REVIEWS = ROOT / "reviews"
OUT = REVIEWS / "C.008.consolidated.corrections.jsonl"
REPORT = REVIEWS / "C.008.consolidated.report.json"
INPUTS = [
    REVIEWS / "C.resume.corrections.jsonl",
    REVIEWS / "C.manual.008_0189_0450.corrections.jsonl",
    REVIEWS / "C.manual.008_0451_0600.corrections.jsonl",
    REVIEWS / "C.manual.008_0601_0750.corrections.jsonl",
    REVIEWS / "C.manual.008_0751_0900.corrections.jsonl",
    REVIEWS / "C.manual.008_0901_1050.corrections.jsonl",
    REVIEWS / "C.manual.008_1051_1200.corrections.jsonl",
    REVIEWS / "C.manual.008_1201_1350.corrections.jsonl",
    REVIEWS / "C.manual.008_1351_1500.corrections.jsonl",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    sys.path.insert(0, str(ROOT))
    import audit_master

    master_doc = json.loads(MASTER.read_text(encoding="utf-8-sig"))
    entries = master_doc["entries"]
    assert len(entries) == 1500
    by_id = {entry["stable_id"]: dict(entry) for entry in entries}
    assert len(by_id) == 1500

    rows: list[dict] = []
    input_report: list[dict] = []
    for path in INPUTS:
        loaded = [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
        loaded = [row for row in loaded if row.get("script") == "008"]
        rows.extend(loaded)
        input_report.append({"path": str(path.resolve()), "sha256": sha(path), "selected_records": len(loaded)})

    stable_ids = [row["stable_id"] for row in rows]
    sequences = [int(row["sequence"]) for row in rows]
    assert len(rows) == 219
    assert len(set(stable_ids)) == len(rows)
    assert len(set(sequences)) == len(rows)

    guard_failures = []
    for row in rows:
        entry = by_id[row["stable_id"]]
        if int(entry["sequence"]) != int(row["sequence"]) or entry["draft_ko"] != row["old_ko"]:
            guard_failures.append(row["sequence"])
            continue
        entry["draft_ko"] = row["new_ko"]
    assert not guard_failures

    ruby_map = audit_master.load_ruby_map(ROOT / "ruby_map.approved.json")
    issues: list[dict] = []
    for entry in sorted(by_id.values(), key=lambda item: int(item["sequence"])):
        audit_master.audit_entry(entry, "008", issues, ruby_map=ruby_map)
    assert not issues, [(issue["sequence"], issue["rule_id"]) for issue in issues]

    rows.sort(key=lambda row: int(row["sequence"]))
    OUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    corrected_projection = [
        {"stable_id": entry["stable_id"], "sequence": entry["sequence"], "draft_ko": entry["draft_ko"]}
        for entry in sorted(by_id.values(), key=lambda item: int(item["sequence"]))
    ]
    corrected_sha = hashlib.sha256(
        json.dumps(corrected_projection, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    report = {
        "schema_version": "fatal-twelve-c-008-consolidated-review-v1",
        "source_authority": "Japanese source_jp only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "game_executed": False,
        "script": "008",
        "master_entries": 1500,
        "exhaustive_checked": 1500,
        "review_coverage": [
            {"range": [1, 188], "reviewer": "C", "evidence": "C.resume.corrections.jsonl and resume_corrections_report.json"},
            {"range": [189, 450], "reviewer": "C", "evidence": "C.manual.008_0189_0450.report.json"},
            {"range": [451, 600], "reviewer": "C", "evidence": "C.manual.008_0451_0600.report.json"},
            {"range": [601, 750], "reviewer": "C", "evidence": "C.manual.008_0601_0750.report.json"},
            {"range": [751, 900], "reviewer": "C", "evidence": "C.manual.008_0751_0900.report.json"},
            {"range": [901, 1050], "reviewer": "C", "evidence": "C.manual.008_0901_1050.report.json"},
            {"range": [1051, 1200], "reviewer": "C", "evidence": "C.manual.008_1051_1200.report.json"},
            {"range": [1201, 1350], "reviewer": "C", "evidence": "C.manual.008_1201_1350.report.json"},
            {"range": [1351, 1500], "reviewer": "C", "evidence": "C.manual.008_1351_1500.report.json"},
        ],
        "corrections": len(rows),
        "unchanged_approved": 1500 - len(rows),
        "stable_id_unique": len(set(stable_ids)),
        "sequence_unique": len(set(sequences)),
        "old_ko_guard_failures": guard_failures,
        "post_correction_audit_issues": len(issues),
        "master_sha256": sha(MASTER),
        "input_files": input_report,
        "output_sha256": sha(OUT),
        "corrected_projection_sha256": corrected_sha,
        "verdict": "PASS",
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
