#!/usr/bin/env python3
"""Prepare the first 300 visible items in scenario/002 from Japanese only.

The input catalog was built without a reference translation file.  Its Ren'Py
IDs are recomputed from the canonical Japanese statement groups using the
Ren'Py 6.99 algorithm.
"""

from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(r"C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc")
WORK = ROOT / "work/jp_recovery"
CATALOG = WORK / "catalog_002_japanese_only.json"
SOURCE = WORK / "raw/scenario/002.rpy"
STYLE_GUIDE = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\style_guide.md")
OUTPUT = WORK / "packet_002_001_300.json"
SOURCE_LIST = WORK / "packet_002_001_300_sources.txt"
CHUNK_DIR = WORK / "packet_002_001_300_chunks"

QUOTED_RE = re.compile(
    r'^(?:(?P<prefix>[A-Za-z_][A-Za-z0-9_]*(?:\s+[A-Za-z_][A-Za-z0-9_]*)*)\s+)?'
    r'(?P<literal>"(?:\\.|[^"\\])*")(?P<suffix>.*)$'
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def split_statement(code: str) -> tuple[str, str, str]:
    match = QUOTED_RE.fullmatch(code)
    if not match:
        raise ValueError(f"unexpected visible statement: {code!r}")
    prefix = match.group("prefix") or ""
    literal = match.group("literal")
    suffix = match.group("suffix") or ""
    value = ast.literal_eval(literal)
    if not isinstance(value, str):
        raise ValueError(code)
    return prefix, literal, suffix


def main() -> int:
    records = [
        json.loads(line)
        for line in CATALOG.read_text(encoding="utf-8", errors="strict").splitlines()
        if line.strip()
    ]
    selected = records[:300]
    if len(selected) != 300:
        raise RuntimeError(f"expected 300 entries, got {len(selected)}")

    source_lines = SOURCE.read_text(encoding="utf-8", errors="strict").splitlines()
    entries: list[dict] = []
    source_rows: list[str] = []
    for sequence, record in enumerate(selected, 1):
        source = record["source"]
        loc = record["localization"]
        prefix, literal, suffix = split_statement(source["statement_code"])
        voice = record.get("voice_call")
        entry = {
            "sequence": sequence,
            "stable_id": record["stable_id"],
            "translation_id": loc["translation_id"],
            "translation_id_origin": loc["id_origin"],
            "translation_id_exactness": "exact_recomputed_renpy_6_99_japanese_canonical_code",
            "source_file": "scenario/002.rpy",
            "source_line": source["line"],
            "source_label": source["label"],
            "item_type": record["lane"],
            "speaker": (record.get("speaker") or {}).get("code") or "narrator",
            "speaker_name_jp": (record.get("speaker") or {}).get("display_name_ja"),
            "source_jp": source["text_ja"],
            "source_statement": source["statement_code"],
            "source_literal": literal,
            "statement_prefix": prefix,
            "renpy_tail": suffix,
            "voice_call": voice["statement"] if voice else "",
            "voice_line": voice["line"] if voice else None,
            "protected_tokens": record.get("protected_tokens", []),
            "draft_ko": None,
            "source_authority": "Japanese only",
            "english_reference_used": False,
            "status": "first_draft_unreviewed",
            "qa": "deferred_until_full_first_draft",
        }
        entries.append(entry)
        who = entry["speaker"]
        source_rows.append(
            f"{sequence:03d}\tL{entry['source_line']:04d}\t{entry['item_type']}\t{who}\t{entry['source_jp']}"
        )

    # Source-order and source-line integrity checks are structural, not prose QA.
    assert [entry["sequence"] for entry in entries] == list(range(1, 301))
    assert all(a["source_line"] < b["source_line"] for a, b in zip(entries, entries[1:]))
    for entry in entries:
        assert source_lines[entry["source_line"] - 1].strip() == entry["source_statement"]
    assert all(entry["translation_id"] for entry in entries)
    assert len({entry["translation_id"] for entry in entries}) == 300

    payload = {
        "packet_id": "scenario_002_001_300",
        "source_file": "scenario/002.rpy",
        "sequence_start": 1,
        "sequence_end": 300,
        "source_line_start": entries[0]["source_line"],
        "source_line_end": entries[-1]["source_line"],
        "entry_count": 300,
        "item_counts": {
            lane: sum(entry["item_type"] == lane for entry in entries)
            for lane in sorted({entry["item_type"] for entry in entries})
        },
        "semantic_source_language": "Japanese",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "translation_engine": "Codex internal model",
        "translation_id_method": "Ren'Py 6.99 md5(concat(canonical Japanese group code + CRLF))[:8], label-prefixed, duplicate-suffixed",
        "status": "first_draft_unreviewed",
        "qa": "deferred_until_full_first_draft",
        "style_guide": {
            "path": str(STYLE_GUIDE),
            "sha256": sha256_file(STYLE_GUIDE),
        },
        "inputs": {
            "japanese_rpy": {"path": str(SOURCE), "sha256": sha256_file(SOURCE)},
            "japanese_only_catalog": {"path": str(CATALOG), "sha256": sha256_file(CATALOG)},
        },
        "entries": entries,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    SOURCE_LIST.write_text("\n".join(source_rows) + "\n", encoding="utf-8")

    CHUNK_DIR.mkdir(parents=True, exist_ok=True)
    for start in range(0, 300, 25):
        rows = source_rows[start : start + 25]
        path = CHUNK_DIR / f"sources_{start + 1:03d}_{start + len(rows):03d}.txt"
        path.write_text("\n".join(rows) + "\n", encoding="utf-8")

    print(json.dumps({
        "status": "ok",
        "entry_count": len(entries),
        "sequence": [entries[0]["sequence"], entries[-1]["sequence"]],
        "source_lines": [entries[0]["source_line"], entries[-1]["source_line"]],
        "item_counts": payload["item_counts"],
        "voice_calls": sum(bool(entry["voice_call"]) for entry in entries),
        "renpy_tails": sum(bool(entry["renpy_tail"]) for entry in entries),
    }, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
