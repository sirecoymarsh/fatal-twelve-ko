#!/usr/bin/env python3
"""Write scenario/003 items 1..400 first-draft JSON and Ren'Py.

This performs structural validation only; prose QA/correction is deferred.
"""

from __future__ import annotations

import collections
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(r"C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc")
WORK = ROOT / "work/jp_recovery"
PACKET = WORK / "packet_003_001_400.json"
TRANSLATIONS = WORK / "translations_003_001_400.tsv"
OUTPUT_JSON = WORK / "draft_003_001_400.json"
OUTPUT_RPY = WORK / "draft_003_001_400.rpy"

TAG_RE = re.compile(r"\{[^{}\r\n]+\}")
INTERPOLATION_RE = re.compile(r"\[[^\[\]\r\n]+\]")
PRINTF_RE = re.compile(r"%(?:\([^)]+\))?[#0 +\-]*\d*(?:\.\d+)?[diouxXeEfFgGcrsa%]")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runtime_tokens(text: str) -> collections.Counter[str]:
    values = TAG_RE.findall(text) + INTERPOLATION_RE.findall(text) + PRINTF_RE.findall(text)
    return collections.Counter(values)


def renpy_string(text: str) -> str:
    return json.dumps(text, ensure_ascii=False)


def load_translations() -> dict[int, str]:
    rows: dict[int, str] = {}
    for line_no, line in enumerate(TRANSLATIONS.read_text(encoding="utf-8", errors="strict").splitlines(), 1):
        if "\t" not in line:
            raise ValueError(f"missing tab on TSV line {line_no}")
        raw_sequence, text = line.split("\t", 1)
        sequence = int(raw_sequence)
        if sequence in rows or not text:
            raise ValueError(f"invalid TSV sequence {sequence}")
        rows[sequence] = text
    if sorted(rows) != list(range(1, 401)):
        raise ValueError("translation sequence must be exactly 1..400")
    return rows


def main() -> int:
    payload = json.loads(PACKET.read_text(encoding="utf-8", errors="strict"))
    entries = payload["entries"]
    translations = load_translations()
    if len(entries) != 400:
        raise ValueError(f"expected 400 packet entries, got {len(entries)}")

    for entry in entries:
        target = translations[entry["sequence"]]
        if runtime_tokens(entry["source_jp"]) != runtime_tokens(target):
            raise ValueError(f"runtime token mismatch at sequence {entry['sequence']}")
        entry["draft_ko"] = target
        entry["status"] = "first_draft_unreviewed"
        entry["qa"] = "deferred_until_full_first_draft"
        entry["english_reference_used"] = False

    payload.update({
        "status": "first_draft_unreviewed",
        "qa": "deferred_until_full_first_draft",
        "english_reference_used": False,
        "translation_source": "Japanese source, speaker, and scene context only",
        "external_translation_api_used": False,
        "translation_engine": "Codex internal model",
        "translation_review_performed": False,
        "structural_validation": {
            "performed": True,
            "scope": [
                "entry count and source order",
                "Ren'Py ID/menu-key uniqueness",
                "menu lane separation",
                "voice and display-tail preservation",
                "runtime tag/interpolation/printf-token preservation",
                "strict UTF-8 serialization",
            ],
            "prose_qa_performed": False,
        },
    })
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    translated = [e for e in entries if e["translation_id"]]
    menu_strings = [e for e in entries if not e["translation_id"]]
    rpy: list[str] = [
        "# Auto-generated Korean first draft for scenario/003 items 1..400.",
        "# Semantic source: Japanese only. Prose QA is deferred.",
        "# status: first_draft_unreviewed",
        "# qa: deferred_until_full_first_draft",
        "",
    ]
    for entry in translated:
        rpy.extend([
            f"# sequence: {entry['sequence']:03d}",
            f"# source: {entry['source_file']}:{entry['source_line']}",
            f"# source_jp: {entry['source_jp']}",
            f"translate korean {entry['translation_id']}:",
        ])
        if entry["voice_call"]:
            rpy.append(f"    {entry['voice_call']}")
        statement = (entry["statement_prefix"] + " " if entry["statement_prefix"] else "")
        statement += renpy_string(entry["draft_ko"])
        statement += entry["renpy_tail"]
        rpy.extend([f"    {statement}", ""])

    if menu_strings:
        rpy.extend([
            "# Menu/prompt display strings are kept in a separate Ren'Py strings lane.",
            "# Conditions, branches, voice calls, and display tails remain in the source script.",
            "translate korean strings:",
        ])
        for entry in menu_strings:
            rpy.extend([
                f"    # sequence: {entry['sequence']:03d}",
                f"    # source: {entry['source_file']}:{entry['source_line']}",
                f"    # menu_key: {entry['menu_key']}",
                f"    old {renpy_string(entry['source_jp'])}",
                f"    new {renpy_string(entry['draft_ko'])}",
                "",
            ])

    OUTPUT_RPY.write_text("\n".join(rpy), encoding="utf-8")

    reparsed = json.loads(OUTPUT_JSON.read_text(encoding="utf-8", errors="strict"))
    out_entries = reparsed["entries"]
    assert reparsed["entry_count"] == 400 == len(out_entries)
    assert [e["sequence"] for e in out_entries] == list(range(1, 401))
    assert len({e["translation_id"] for e in out_entries if e["translation_id"]}) == 397
    assert len({e["menu_key"] for e in out_entries if e["menu_key"]}) == 3
    assert sum(bool(e["voice_call"]) for e in out_entries) == 172
    assert sum(bool(e["renpy_tail"]) for e in out_entries) == 2
    assert all(e["status"] == "first_draft_unreviewed" for e in out_entries)
    assert all(e["qa"] == "deferred_until_full_first_draft" for e in out_entries)
    assert all(e["english_reference_used"] is False for e in out_entries)

    print(json.dumps({
        "status": "ok",
        "entries": len(out_entries),
        "sequence": [1, 400],
        "source_lines": [out_entries[0]["source_line"], out_entries[-1]["source_line"]],
        "item_counts": payload["item_counts"],
        "translation_ids": len(translated),
        "menu_strings": len(menu_strings),
        "voice_calls": sum(bool(e["voice_call"]) for e in out_entries),
        "renpy_tails": sum(bool(e["renpy_tail"]) for e in out_entries),
        "json_sha256": sha256_file(OUTPUT_JSON),
        "rpy_sha256": sha256_file(OUTPUT_RPY),
    }, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
