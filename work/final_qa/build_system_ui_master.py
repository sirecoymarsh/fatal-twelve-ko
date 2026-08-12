#!/usr/bin/env python3
"""Consolidate four Japanese-source UI drafts into one global strings master."""

from __future__ import annotations

import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path


INPUTS = [
    Path("work/system_ui/characters.draft.json"),
    Path("work/system_ui/gamedata.draft.json"),
    Path("work/system_ui/screens.draft.json"),
    Path("work/system_ui/script.draft.json"),
]
OUT = Path("work/final_qa/output/masters/system_ui.master.json")
PACKET_DIR = Path("work/final_qa/review_packets/A_UI")


def load(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    entries = data.get("entries") or data.get("records")
    if not isinstance(entries, list):
        raise ValueError(f"{path}: missing entries/records")
    return entries


def token_values(entry: dict) -> list[str]:
    raw = entry.get("protected_tokens")
    if raw is None:
        raw = entry.get("protected_tokens_source") or []
    result = []
    for token in raw:
        if isinstance(token, str):
            result.append(token)
        elif isinstance(token, dict) and token.get("value") is not None:
            result.append(str(token["value"]))
    return result


def main() -> None:
    occurrences = []
    for path in INPUTS:
        for index, entry in enumerate(load(path), 1):
            key = entry.get("lookup_key") or entry.get("source_jp")
            if not isinstance(key, str) or not key:
                raise ValueError(f"{path}#{index}: missing lookup key")
            target = entry.get("draft_ko")
            if not isinstance(target, str) or not target:
                raise ValueError(f"{path}#{index}: missing draft_ko")
            occurrences.append((path, index, key, target, entry))

    grouped = defaultdict(list)
    for item in occurrences:
        grouped[item[2]].append(item)

    conflicts = []
    entries = []
    for sequence, key in enumerate(sorted(grouped), 1):
        group = grouped[key]
        targets = sorted({item[3] for item in group})
        if len(targets) != 1:
            conflicts.append({"lookup_key": key, "targets": targets})
            continue
        target = targets[0]
        all_tokens = sorted({token for item in group for token in token_values(item[4])})
        contexts = []
        for path, index, _, _, entry in group:
            contexts.append({
                "draft_file": str(path.resolve()),
                "draft_entry_index": index - 1,
                "original_stable_id": entry.get("stable_id"),
                "source_file": entry.get("source_file"),
                "source_line": entry.get("source_line"),
                "source_lines": entry.get("source_lines"),
                "lane": entry.get("lane"),
                "section": entry.get("section"),
                "occurrences": entry.get("occurrences"),
                "statement": entry.get("statement"),
                "statements": entry.get("statements"),
                "origin": entry.get("origin") or entry.get("key_origin"),
                "emitted_to_rpy": entry.get("emitted_to_rpy", True),
                "duplicate_of": entry.get("duplicate_of"),
            })
        entries.append({
            "stable_id": "system-ui::" + hashlib.sha256(key.encode("utf-8")).hexdigest()[:24],
            "sequence": sequence,
            "command_index": sequence,
            "source_file": "system-ui/global-strings",
            "source_line": next((c["source_line"] for c in contexts if c["source_line"] is not None), None),
            "lane": "strings",
            "speaker": None,
            "source_jp": key,
            "source_text_sha256": hashlib.sha256(key.encode("utf-8")).hexdigest(),
            "translation_id": None,
            "menu_key": key,
            "protected_tokens": all_tokens,
            "draft_ko": target,
            "draft_ko_sha256": hashlib.sha256(target.encode("utf-8")).hexdigest(),
            "source_authority": "Japanese only",
            "english_reference_used": False,
            "external_translation_api_used": False,
            "status": "first_draft_unreviewed",
            "qa": "deferred_until_full_first_draft",
            "contexts": contexts,
        })

    if conflicts:
        raise ValueError("UI target conflicts: " + json.dumps(conflicts, ensure_ascii=False))
    expected_occurrences = 61 + 569 + 87 + 22
    if len(occurrences) != expected_occurrences:
        raise ValueError(f"expected {expected_occurrences} catalog records, got {len(occurrences)}")
    aliases = len(occurrences) - len(entries)
    doc = {
        "schema_version": "fatal-twelve-system-ui-master-v1",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "status": "first_draft_unreviewed",
        "qa": "deferred_until_full_first_draft",
        "input_catalog_records": len(occurrences),
        "unique_runtime_string_keys": len(entries),
        "duplicate_context_aliases": aliases,
        "entries": entries,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    PACKET_DIR.mkdir(parents=True, exist_ok=True)
    packet_files = []
    chunk_size = 160
    for start in range(0, len(entries), chunk_size):
        chunk = entries[start:start + chunk_size]
        path = PACKET_DIR / f"A_UI__system_ui__{chunk[0]['sequence']:04d}-{chunk[-1]['sequence']:04d}__{len(chunk)}.tsv"
        with path.open("w", encoding="utf-8-sig", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=[
                "sequence", "stable_id", "source_jp", "draft_ko", "protected_tokens", "contexts"
            ], delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_ALL)
            writer.writeheader()
            for entry in chunk:
                writer.writerow({
                    "sequence": entry["sequence"],
                    "stable_id": entry["stable_id"],
                    "source_jp": entry["source_jp"],
                    "draft_ko": entry["draft_ko"],
                    "protected_tokens": json.dumps(entry["protected_tokens"], ensure_ascii=False),
                    "contexts": json.dumps(entry["contexts"], ensure_ascii=False),
                })
        packet_files.append(str(path.resolve()))

    report = {
        "inputs": [str(p.resolve()) for p in INPUTS],
        "catalog_records": len(occurrences),
        "unique_runtime_string_keys": len(entries),
        "duplicate_context_aliases": aliases,
        "target_conflicts": 0,
        "master": str(OUT.resolve()),
        "review_packets": packet_files,
    }
    report_path = OUT.with_name("system_ui.master.coverage.json")
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    main()
