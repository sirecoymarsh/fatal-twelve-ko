#!/usr/bin/env python3
"""Merge the Japanese-only packet with Codex first-draft Korean text.

Only structural checks are performed here.  Prose review and correction are
explicitly deferred until the complete first draft exists.
"""

from __future__ import annotations

import collections
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(r"C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc")
WORK = ROOT / "work/jp_recovery"
PACKET = WORK / "packet_002_001_300.json"
TRANSLATIONS = WORK / "translations_002_001_300.tsv"
OUTPUT_JSON = WORK / "draft_002_001_300.json"
OUTPUT_RPY = WORK / "draft_002_001_300.rpy"
GLOSSARY = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\glossary_draft.json")

TAG_RE = re.compile(r"\{[^{}\r\n]+\}")
INTERPOLATION_RE = re.compile(r"\[[^\[\]\r\n]+\]")
PRINTF_RE = re.compile(r"%(?:\([^)]+\))?[#0 +\-]*\d*(?:\.\d+)?[diouxXeEfFgGcrsa%]")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def runtime_tokens(text: str) -> collections.Counter[str]:
    tokens = TAG_RE.findall(text) + INTERPOLATION_RE.findall(text) + PRINTF_RE.findall(text)
    return collections.Counter(tokens)


def renpy_string(text: str) -> str:
    # JSON double-quoted strings use the subset of escaping accepted by Ren'Py.
    return json.dumps(text, ensure_ascii=False)


def load_translations() -> dict[int, str]:
    rows: dict[int, str] = {}
    for line_no, line in enumerate(TRANSLATIONS.read_text(encoding="utf-8", errors="strict").splitlines(), 1):
        if "\t" not in line:
            raise ValueError(f"missing tab on TSV line {line_no}")
        raw_sequence, text = line.split("\t", 1)
        sequence = int(raw_sequence)
        if sequence in rows:
            raise ValueError(f"duplicate sequence: {sequence}")
        if not text:
            raise ValueError(f"empty draft: {sequence}")
        rows[sequence] = text
    if sorted(rows) != list(range(1, 301)):
        raise ValueError("translation sequence must be exactly 1..300")
    return rows


def main() -> int:
    payload = json.loads(PACKET.read_text(encoding="utf-8", errors="strict"))
    translations = load_translations()
    entries = payload["entries"]
    if len(entries) != 300:
        raise ValueError(f"expected 300 packet entries, got {len(entries)}")

    for entry in entries:
        ko = translations[entry["sequence"]]
        if runtime_tokens(entry["source_jp"]) != runtime_tokens(ko):
            raise ValueError(f"runtime token mismatch at sequence {entry['sequence']}")
        entry["draft_ko"] = ko
        entry["status"] = "first_draft_unreviewed"
        entry["qa"] = "deferred_until_full_first_draft"
        entry["english_reference_used"] = False

    payload.update(
        {
            "status": "first_draft_unreviewed",
            "qa": "deferred_until_full_first_draft",
            "english_reference_used": False,
            "translation_source": "Japanese source, speaker, and scene context only",
            "external_translation_api_used": False,
            "translation_engine": "Codex internal model",
            "translation_review_performed": False,
            "glossary": {
                "path": str(GLOSSARY),
                "sha256": sha256_file(GLOSSARY),
                "status": "provisional_first_draft_unreviewed",
            },
            "structural_validation": {
                "performed": True,
                "scope": [
                    "entry count and source order",
                    "Ren'Py translation ID uniqueness",
                    "voice statement preservation",
                    "display-tail preservation",
                    "runtime tag/interpolation/printf-token preservation",
                    "strict UTF-8 serialization",
                ],
                "prose_qa_performed": False,
            },
        }
    )
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    rpy: list[str] = [
        "# Auto-generated Korean first draft for scenario/002 items 1..300.",
        "# Semantic source: Japanese only. Prose QA is deferred.",
        "# status: first_draft_unreviewed",
        "# qa: deferred_until_full_first_draft",
        "",
    ]
    for entry in entries:
        translation_id = entry["translation_id"]
        if not translation_id:
            raise ValueError(f"menu/string entry needs separate strings block: {entry['sequence']}")
        rpy.extend(
            [
                f"# sequence: {entry['sequence']:03d}",
                f"# source: {entry['source_file']}:{entry['source_line']}",
                f"# source_jp: {entry['source_jp']}",
                f"translate korean {translation_id}:",
            ]
        )
        if entry["voice_call"]:
            rpy.append(f"    {entry['voice_call']}")
        statement = ""
        if entry["statement_prefix"]:
            statement += entry["statement_prefix"] + " "
        statement += renpy_string(entry["draft_ko"])
        statement += entry["renpy_tail"]
        rpy.extend([f"    {statement}", ""])

    OUTPUT_RPY.write_text("\n".join(rpy), encoding="utf-8")

    # Output-only structural assertions.  These do not judge or edit prose.
    reparsed = json.loads(OUTPUT_JSON.read_text(encoding="utf-8", errors="strict"))
    assert reparsed["entry_count"] == 300 == len(reparsed["entries"])
    assert [e["sequence"] for e in reparsed["entries"]] == list(range(1, 301))
    assert len({e["translation_id"] for e in reparsed["entries"]}) == 300
    assert sum(bool(e["voice_call"]) for e in reparsed["entries"]) == 126
    assert sum(bool(e["renpy_tail"]) for e in reparsed["entries"]) == 0
    assert all(e["status"] == "first_draft_unreviewed" for e in reparsed["entries"])
    assert all(e["qa"] == "deferred_until_full_first_draft" for e in reparsed["entries"])
    assert all(e["english_reference_used"] is False for e in reparsed["entries"])

    print(
        json.dumps(
            {
                "status": "ok",
                "entries": len(entries),
                "sequence": [entries[0]["sequence"], entries[-1]["sequence"]],
                "source_lines": [entries[0]["source_line"], entries[-1]["source_line"]],
                "item_counts": payload["item_counts"],
                "voice_calls": sum(bool(e["voice_call"]) for e in entries),
                "renpy_tails": sum(bool(e["renpy_tail"]) for e in entries),
                "json_sha256": sha256_file(OUTPUT_JSON),
                "rpy_sha256": sha256_file(OUTPUT_RPY),
            },
            ensure_ascii=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
