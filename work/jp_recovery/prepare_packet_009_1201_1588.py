#!/usr/bin/env python3
"""Prepare scenario/009 visible items 1201..1588 from Japanese-only catalog."""

from __future__ import annotations

import ast
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(r"C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc")
WORK = ROOT / "work/jp_recovery"
CATALOG = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\catalog\scenario_009.catalog.jsonl")
SOURCE = WORK / "raw/scenario/009.rpy"
STYLE_GUIDE = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\style_guide.md")
GLOSSARY = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\glossary_draft.json")
OUTPUT = WORK / "packet_009_1201_1588.json"
SOURCE_LIST = WORK / "packet_009_1201_1588_sources.txt"
CHUNK_DIR = WORK / "packet_009_1201_1588_chunks"

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
    if len(records) != 1588:
        raise RuntimeError(f"expected 1588 catalog records, got {len(records)}")
    selected = records[1200:1588]
    if len(selected) != 388:
        raise RuntimeError(f"expected 388 entries, got {len(selected)}")

    source_lines = SOURCE.read_text(encoding="utf-8", errors="strict").splitlines()
    entries: list[dict] = []
    rows: list[str] = []
    for sequence, record in enumerate(selected, 1201):
        source = record["source"]
        loc = record["localization"]
        prefix, literal, suffix = split_statement(source["statement_code"])
        voice = record.get("voice_call")
        translation_id = loc["translation_id"]
        entry = {
            "sequence": sequence,
            "stable_id": record["stable_id"],
            "translation_id": translation_id,
            "translation_id_origin": loc["id_origin"],
            "translation_id_exactness": (
                "exact_recomputed_renpy_6_99_japanese_canonical_code"
                if translation_id
                else "exact_japanese_menu_string_identity"
            ),
            "menu_key": loc.get("menu_key"),
            "source_file": "scenario/009.rpy",
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
            "menu_context": record.get("menu_context"),
            "protected_tokens": record.get("protected_tokens", []),
            "draft_ko": None,
            "source_authority": "Japanese only",
            "english_reference_used": False,
            "status": "first_draft_unreviewed",
            "qa": "deferred_until_full_first_draft",
        }
        entries.append(entry)
        rows.append(
            f"{sequence:03d}\tL{entry['source_line']:04d}\t{entry['item_type']}\t"
            f"{entry['speaker']}\t{entry['source_jp']}"
        )

    assert [e["sequence"] for e in entries] == list(range(1201, 1589))
    assert all(a["source_line"] < b["source_line"] for a, b in zip(entries, entries[1:]))
    for entry in entries:
        assert source_lines[entry["source_line"] - 1].strip() == entry["source_statement"]
    exact_ids = [e["translation_id"] for e in entries if e["translation_id"]]
    assert len(exact_ids) == len(set(exact_ids))

    payload = {
        "packet_id": "scenario_009_1201_1588",
        "source_file": "scenario/009.rpy",
        "sequence_start": 1201,
        "sequence_end": 1588,
        "source_line_start": entries[0]["source_line"],
        "source_line_end": entries[-1]["source_line"],
        "entry_count": 388,
        "item_counts": {
            lane: sum(e["item_type"] == lane for e in entries)
            for lane in sorted({e["item_type"] for e in entries})
        },
        "semantic_source_language": "Japanese",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "translation_engine": "Codex internal model",
        "translation_id_method": "Ren'Py 6.99 canonical Japanese AST digest; menu items use exact Japanese string identity",
        "status": "first_draft_unreviewed",
        "qa": "deferred_until_full_first_draft",
        "style_guide": {"path": str(STYLE_GUIDE), "sha256": sha256_file(STYLE_GUIDE)},
        "glossary": {"path": str(GLOSSARY), "sha256": sha256_file(GLOSSARY)},
        "inputs": {
            "japanese_rpy": {"path": str(SOURCE), "sha256": sha256_file(SOURCE)},
            "japanese_only_catalog": {"path": str(CATALOG), "sha256": sha256_file(CATALOG)},
        },
        "entries": entries,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    SOURCE_LIST.write_text("\n".join(rows) + "\n", encoding="utf-8")
    CHUNK_DIR.mkdir(parents=True, exist_ok=True)
    for start in range(0, 388, 25):
        chunk = rows[start : start + 25]
        (CHUNK_DIR / f"sources_{start + 1201:04d}_{start + len(chunk) + 1200:04d}.txt").write_text(
            "\n".join(chunk) + "\n", encoding="utf-8"
        )

    print(json.dumps({
        "status": "ok",
        "entries": len(entries),
        "sequence": [1201, 1588],
        "source_lines": [entries[0]["source_line"], entries[-1]["source_line"]],
        "item_counts": payload["item_counts"],
        "translation_ids": len(exact_ids),
        "menu_strings": sum(not e["translation_id"] for e in entries),
        "voice_calls": sum(bool(e["voice_call"]) for e in entries),
        "renpy_tails": sum(bool(e["renpy_tail"]) for e in entries),
    }, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
