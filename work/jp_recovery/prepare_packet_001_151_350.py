#!/usr/bin/env python3
"""Prepare Japanese-only scenario/001 entries 151..350.

The separate localization file is read only for ``translate english ID:``
headers.  Its indented prose is neither parsed nor copied.  Translation IDs are
technical lookup keys; all semantic source text comes from the Japanese RPYC
decompilation.
"""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path


ROOT = Path(r"C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc")
JP_RPY = ROOT / "work/jp_recovery/raw/scenario/001.rpy"
ID_HEADERS = Path(
    r"P:\AI\Codex\projects\fatal-twelve-ko\work\extracted\tl\tl\english\scenario\001.rpy"
)
EXISTING_DRAFT_DIR = Path(
    r"P:\AI\Codex\projects\fatal-twelve-ko\translations\draft\scenario"
)
OUTPUT = ROOT / "work/jp_recovery/packet_001_151_350.json"
CONTEXT_OUTPUT = ROOT / "work/jp_recovery/context_001_151_350.txt"

HEADER_RE = re.compile(r"^translate\s+english\s+([A-Za-z0-9_.-]+)\s*:\s*$")
SAY_RE = re.compile(
    r"^\s*(?:(?P<speaker>[A-Za-z_]\w*)\s+)?(?P<literal>(?:[rRuUbBfF]*)(?:\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'))(?P<tail>\s+.*)?$"
)
NON_SAY_PREFIXES = {
    "voice", "play", "queue", "scene", "show", "hide", "with", "call", "jump",
    "image", "define", "default", "text", "add", "use", "key", "timer", "on", "event",
}


def technical_ids() -> list[str]:
    ids: list[str] = []
    # Deliberately stream one line at a time and retain header IDs only.
    with ID_HEADERS.open("r", encoding="utf-8", errors="strict") as handle:
        for line in handle:
            match = HEADER_RE.fullmatch(line.strip())
            if match:
                ids.append(match.group(1))
    return ids


def japanese_say_entries() -> tuple[list[dict], list[str]]:
    lines = JP_RPY.read_text(encoding="utf-8", errors="strict").splitlines()
    entries: list[dict] = []
    for index, line in enumerate(lines):
        match = SAY_RE.fullmatch(line)
        if not match:
            continue
        try:
            text = ast.literal_eval(match.group("literal"))
        except (SyntaxError, ValueError):
            continue
        if not isinstance(text, str):
            continue
        speaker = match.group("speaker")
        if speaker in NON_SAY_PREFIXES:
            continue
        voice_call = ""
        if index and re.fullmatch(r"\s*voice\s+.+", lines[index - 1]):
            voice_call = lines[index - 1].strip()
        entries.append(
            {
                "sequence": len(entries) + 1,
                "source_line": index + 1,
                "speaker": speaker or "narrator",
                "source_jp": text,
                "voice_call": voice_call,
                "renpy_tail": match.group("tail") or "",
            }
        )
    return entries, lines


def verify_prefix(entries: list[dict], ids: list[str]) -> None:
    existing: list[dict] = []
    for filename in ("001_part001.json", "001_part002.json", "001_part003.json"):
        payload = json.loads((EXISTING_DRAFT_DIR / filename).read_text(encoding="utf-8"))
        existing.extend(payload["entries"])
    assert len(existing) == 150
    for index, record in enumerate(existing):
        source = entries[index]
        assert record["sequence"] == source["sequence"]
        assert record["source_line"] == source["source_line"]
        assert record["speaker"] == source["speaker"]
        assert record["source_jp"] == source["source_jp"]
        assert record["translation_id"] == ids[index]


def main() -> int:
    ids = technical_ids()
    entries, source_lines = japanese_say_entries()
    verify_prefix(entries, ids)

    selected = entries[150:350]
    assert len(selected) == 200
    for index, record in enumerate(selected, 150):
        record["translation_id"] = ids[index]
        record["stable_id"] = f"scenario/001.rpy::{ids[index]}"
        record["source_file"] = "scenario/001.rpy"
        record["draft_ko"] = None
        record["source_authority"] = "Japanese only"
        record["english_reference_used"] = False
        record["status"] = "first_draft_unreviewed"
        record["qa"] = "deferred"

    payload = {
        "packet_id": "scenario_001_151_350",
        "sequence_start": 151,
        "sequence_end": 350,
        "entry_count": 200,
        "semantic_source_language": "Japanese",
        "technical_id_headers_only": True,
        "english_prose_exposed_to_translator": False,
        "status": "first_draft_unreviewed",
        "qa": "deferred",
        "entries": selected,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lo = max(1, selected[0]["source_line"] - 25)
    hi = min(len(source_lines), selected[-1]["source_line"] + 25)
    context = [f"{line_no:5}: {source_lines[line_no - 1]}" for line_no in range(lo, hi + 1)]
    CONTEXT_OUTPUT.write_text("\n".join(context) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": "ok",
        "entries": len(selected),
        "sequence": [selected[0]["sequence"], selected[-1]["sequence"]],
        "source_lines": [selected[0]["source_line"], selected[-1]["source_line"]],
        "prefix_alignment": 150,
    }, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
