#!/usr/bin/env python3
"""Shared guarded writer for Japanese-only semantic review decisions."""
from __future__ import annotations

import collections
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Mapping

ROOT = Path(__file__).resolve().parent
FW_TRANS = str.maketrans("０１２３４５６７８９％", "0123456789%")
ROMAN_RE = re.compile(r"[\u2160-\u2188]+")
TAG_RE = re.compile(r"\{[^{}]+\}|\[[^\[\]]+\]")
KANA_RE = re.compile(r"[ぁ-ゖゝ-ゟァ-ヺヽヾㇰ-ㇿｦ-ﾟ]")


def quote_skeleton(text: str) -> list[str]:
    return [ch for ch in text if ch in "「」『』≪≫"]


def numbers(text: str) -> list[str]:
    return re.findall(r"\d+(?:\.\d+)?", text.translate(FW_TRANS))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def materialize(
    *,
    master_name: str,
    script: str,
    start: int,
    end: int,
    decisions: Mapping[int, tuple[str, str, str]],
    reviewer: str,
    output_stem: str,
) -> dict:
    sys.path.insert(0, str(ROOT))
    import audit_master

    master = ROOT / "output" / "masters" / master_name
    out = ROOT / "reviews" / f"{output_stem}.corrections.jsonl"
    report_path = ROOT / "reviews" / f"{output_stem}.report.json"
    ruby_map = audit_master.load_ruby_map(ROOT / "ruby_map.approved.json")
    entries = json.loads(master.read_text(encoding="utf-8-sig"))["entries"]
    by_seq = {int(entry["sequence"]): entry for entry in entries}
    assert set(range(start, end + 1)) <= set(by_seq)

    rows: list[dict] = []
    failures: list[dict] = []
    post_issues: list[dict] = []
    checks = collections.Counter()
    for sequence, (new_ko, category, reason) in sorted(decisions.items()):
        assert start <= sequence <= end
        entry = by_seq[sequence]
        old, source = str(entry["draft_ko"]), str(entry["source_jp"])
        row = {
            "script": script,
            "stable_id": entry["stable_id"],
            "sequence": sequence,
            "old_ko": old,
            "new_ko": new_ko,
            "category": category,
            "reason": reason,
            "reviewer": reviewer,
            "source_jp": source,
        }
        values = {
            "changed": new_ko != old,
            "encoding": "\ufffd" not in new_ko and not any(0x80 <= ord(ch) <= 0x9F for ch in new_ko),
            "width_clear": re.search(r"[０-９]", new_ko) is None and "\u3000" not in new_ko,
            "tag_exact": collections.Counter(TAG_RE.findall(source)) == collections.Counter(TAG_RE.findall(new_ko)),
            "roman_exact": ROMAN_RE.findall(source) == ROMAN_RE.findall(new_ko),
            "quote_exact": quote_skeleton(source) == quote_skeleton(new_ko),
            "newline_exact": source.count("\n") == new_ko.count("\n"),
            "number_exact": numbers(source) == numbers(new_ko),
            "kana_clear": KANA_RE.search(new_ko) is None,
        }
        for key, passed in values.items():
            checks[key] += int(passed)
        if not all(values.values()):
            failures.append({"sequence": sequence, "bad": [key for key, passed in values.items() if not passed]})
        corrected = dict(entry)
        corrected["draft_ko"] = new_ko
        audit_master.audit_entry(corrected, script, post_issues, ruby_map=ruby_map)
        rows.append(row)

    assert len({row["stable_id"] for row in rows}) == len(rows)
    assert not failures, failures
    assert not post_issues, [(issue["sequence"], issue["rule_id"]) for issue in post_issues]
    out.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
    report = {
        "schema_version": "fatal-twelve-semantic-review-part-v1",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "script": script,
        "range": [start, end],
        "exhaustive_checked": end - start + 1,
        "manual_corrections": len(rows),
        "unchanged_approved": end - start + 1 - len(rows),
        "checks": dict(checks),
        "post_correction_audit_issues": len(post_issues),
        "failures": failures,
        "master_sha256": sha(master),
        "output_sha256": sha(out),
    }
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    return report
