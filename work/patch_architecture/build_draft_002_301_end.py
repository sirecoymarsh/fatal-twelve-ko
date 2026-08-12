from __future__ import annotations

import ast
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "work" / "catalog_design" / "scenario_002.catalog.jsonl"
SEEDS = [
    Path(__file__).with_name("draft_002_301_420.seed.tsv"),
    Path(__file__).with_name("draft_002_421_540.seed.tsv"),
    Path(__file__).with_name("draft_002_541_668.seed.tsv"),
]
STYLE_GUIDE = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\style_guide.md")
GLOSSARY = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\glossary_draft.json")
OUTPUT_JSON = Path(__file__).with_name("draft_002_301_end.json")
OUTPUT_RPY = Path(__file__).with_name("draft_002_301_end.rpy")

SOURCE_FILE = "scenario/002.rpy"
EXPECTED_FIRST_COMMAND = 301
EXPECTED_LAST_COMMAND = 668
EXPECTED_COUNT = 368
EXPECTED_CATALOG_SHA256 = "832387bcbf5b8b08abe8ae75873b6d0dc2b4c537c9a1ec4e152dcf55b6251f47"
STYLE_GUIDE_SHA256 = "b2b87352fdfd9b25af688152b0ce8a7460ffeb88fc06ae6e45f1c5df2ae83891"
GLOSSARY_SHA256 = "d7b49d77fcde5da240cb816890c75f9f15a2e83544db34a6193b8e939906300e"
STATUS = "first_draft_unreviewed"
QA = "deferred_until_full_first_draft"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_drafts() -> dict[int, str]:
    drafts: dict[int, str] = {}
    for path in SEEDS:
        for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if not raw_line:
                continue
            index_text, draft = raw_line.split("\t", 1)
            index = int(index_text)
            if index in drafts:
                raise ValueError(f"duplicate command_index {index} in {path}:{line_number}")
            if not draft.strip():
                raise ValueError(f"empty draft at command_index {index}")
            drafts[index] = draft
    expected = set(range(EXPECTED_FIRST_COMMAND, EXPECTED_LAST_COMMAND + 1))
    if set(drafts) != expected:
        raise ValueError(
            f"draft index mismatch: missing={sorted(expected - set(drafts))}, "
            f"extra={sorted(set(drafts) - expected)}"
        )
    return drafts


def load_source_rows() -> list[dict]:
    rows = []
    with CATALOG.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            record = json.loads(raw_line)
            if (
                record["source"]["script"] == SOURCE_FILE
                and record["command_index"] >= EXPECTED_FIRST_COMMAND
            ):
                rows.append(record)
    rows.sort(key=lambda row: row["command_index"])
    expected = list(range(EXPECTED_FIRST_COMMAND, EXPECTED_LAST_COMMAND + 1))
    indices = [row["command_index"] for row in rows]
    if indices != expected:
        raise ValueError(f"catalog command range changed: {indices[:3]}...{indices[-3:]}")
    if len(rows) != EXPECTED_COUNT:
        raise ValueError(f"catalog row count changed: {len(rows)}")
    return rows


def assert_protected_tokens(record: dict, draft: str) -> None:
    patterns = {
        "renpy_text_tag": re.compile(r"\{[^{}\r\n]+\}"),
        "interpolation": re.compile(r"\[[^\[\]\r\n]+\]"),
        "printf": re.compile(r"%(?:\([^)]+\))?[#0 +\-]*\d*(?:\.\d+)?[diouxXeEfFgGcrsa%]"),
        "number": re.compile(
            r"(?:[0-9０-９]+(?:[.,．，][0-9０-９]+)*)|(?:[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]+)"
        ),
    }
    actual: Counter[tuple[str, str]] = Counter()
    for kind, pattern in patterns.items():
        actual.update((kind, match.group(0)) for match in pattern.finditer(draft))
    for packed, expected_count in record["protected_token_multiset"].items():
        kind, value = packed.split("\0", 1)
        actual_count = actual[(kind, value)]
        if actual_count != expected_count:
            raise ValueError(
                f"protected token mismatch at command {record['command_index']}: "
                f"{value!r} expected={expected_count} actual={actual_count}"
            )


def replace_statement_text(statement: str, source_jp: str, target_ko: str) -> str:
    start = statement.find('"')
    if start < 0:
        raise ValueError(f"no string literal in statement: {statement!r}")
    escaped = False
    end = None
    for position in range(start + 1, len(statement)):
        character = statement[position]
        if escaped:
            escaped = False
        elif character == "\\":
            escaped = True
        elif character == '"':
            end = position
            break
    if end is None:
        raise ValueError(f"unterminated string literal: {statement!r}")
    literal = statement[start : end + 1]
    if ast.literal_eval(literal) != source_jp:
        raise ValueError(f"source literal mismatch: {statement!r}")
    target_literal = json.dumps(target_ko, ensure_ascii=False)
    return statement[:start] + target_literal + statement[end + 1 :]


def build_entry(record: dict, draft: str) -> dict:
    source = record["source"]
    localization = record["localization"]
    speaker = record["speaker"]["code"] if record["speaker"] else "narrator"
    return {
        "sequence": record["command_index"],
        "command_index": record["command_index"],
        "stable_id": record["stable_id"],
        "translation_id": localization["translation_id"],
        "menu_key": localization["menu_key"],
        "id_origin": localization["id_origin"],
        "source_file": source["script"],
        "source_line": source["line"],
        "source_label": source["label"],
        "lane": record["lane"],
        "speaker": speaker,
        "source_jp": source["text_ja"],
        "source_statement_code": source["statement_code"],
        "source_group_code": source["group_code"],
        "source_text_sha256": source["text_sha256"],
        "source_group_sha256": source["group_sha256"],
        "renpy_digest": source["renpy_digest"],
        "voice_call": record["voice_call"]["statement"] if record["voice_call"] else "",
        "protected_tokens": record["protected_tokens"],
        "draft_ko": draft,
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "status": STATUS,
        "qa": QA,
    }


def build_rpy(entries: list[dict]) -> tuple[str, dict]:
    lines = [
        "# -*- coding: utf-8 -*-",
        "# Fatal Twelve scenario/002.rpy Korean first draft, AST ordinal 301-end.",
        "# Semantic/style source: Japanese only; English prose was not opened or used.",
        f"# status: {STATUS}",
        f"# qa: {QA}",
        "",
    ]
    translate_ids = []
    menu_entries = []
    for entry in entries:
        if entry["translation_id"] is None:
            if entry["menu_key"] is None:
                raise ValueError(f"entry has neither translation ID nor menu key: {entry['stable_id']}")
            menu_entries.append(entry)
            continue

        translate_ids.append(entry["translation_id"])
        lines.append(
            f"# {entry['stable_id']} | {entry['source_file']}:{entry['source_line']}"
        )
        lines.append(f"translate korean {entry['translation_id']}:")
        group = entry["source_group_code"]
        statement = entry["source_statement_code"]
        replaced = 0
        for code_line in group:
            if code_line == statement:
                lines.append(f"    # {statement}")
                lines.append(
                    "    " + replace_statement_text(statement, entry["source_jp"], entry["draft_ko"])
                )
                replaced += 1
            else:
                # voice and any future display/control tail are copied byte-for-value.
                lines.append(f"    {code_line}")
        if replaced != 1:
            raise ValueError(f"expected one Say replacement: {entry['stable_id']}")
        lines.append("")

    if menu_entries:
        lines.append("translate korean strings:")
        lines.append("")
        for entry in menu_entries:
            lines.append(
                f"    # {entry['stable_id']} | {entry['source_file']}:{entry['source_line']}"
            )
            lines.append(f"    old {json.dumps(entry['source_jp'], ensure_ascii=False)}")
            lines.append(f"    new {json.dumps(entry['draft_ko'], ensure_ascii=False)}")
            lines.append("")

    if len(translate_ids) != len(set(translate_ids)):
        raise ValueError("duplicate translation IDs")
    return "\n".join(lines).rstrip() + "\n", {
        "translate_blocks": len(translate_ids),
        "strings_entries": len(menu_entries),
        "unique_translation_ids": len(set(translate_ids)),
    }


def main() -> None:
    if sha256(CATALOG) != EXPECTED_CATALOG_SHA256:
        raise ValueError("scenario/002 catalog SHA-256 changed")
    if sha256(STYLE_GUIDE) != STYLE_GUIDE_SHA256:
        raise ValueError("style guide SHA-256 changed")
    if sha256(GLOSSARY) != GLOSSARY_SHA256:
        raise ValueError("glossary SHA-256 changed")

    drafts = load_drafts()
    rows = load_source_rows()
    entries = []
    for row in rows:
        draft = drafts[row["command_index"]]
        assert_protected_tokens(row, draft)
        entries.append(build_entry(row, draft))

    rpy_text, rpy_stats = build_rpy(entries)
    lane_counts = Counter(entry["lane"] for entry in entries)
    packet = {
        "schema_version": "fatal-twelve-ko-first-draft-v1",
        "packet_id": "scenario_002_ast_ordinal_301_end",
        "source_file": SOURCE_FILE,
        "sequence_semantics": "exact AST catalog command_index including Ren'Py menu strings",
        "sequence_start": EXPECTED_FIRST_COMMAND,
        "sequence_end": EXPECTED_LAST_COMMAND,
        "entry_count": len(entries),
        "first_source_line": entries[0]["source_line"],
        "last_source_line": entries[-1]["source_line"],
        "item_counts": dict(sorted(lane_counts.items())),
        "source_language": "ja",
        "target_language": "ko",
        "translation_basis": "Japanese source only; Codex internal translation",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "translation_validation": "not_performed",
        "structure_validation": "performed_during_generation",
        "status": STATUS,
        "qa": QA,
        "style_guide": {"path": str(STYLE_GUIDE), "sha256": STYLE_GUIDE_SHA256},
        "glossary": {"path": str(GLOSSARY), "sha256": GLOSSARY_SHA256},
        "catalog": {
            "path": str(CATALOG.relative_to(ROOT)).replace("\\", "/"),
            "sha256": EXPECTED_CATALOG_SHA256,
            "stable_id_source": "exact catalog stable_id",
            "join_contract": "source_file+source_line+speaker+source_jp exact identity; no ordinal zip",
        },
        "rpy_structure": rpy_stats,
        "entries": entries,
    }
    OUTPUT_JSON.write_text(
        json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    OUTPUT_RPY.write_text(rpy_text, encoding="utf-8", newline="\n")
    print(
        json.dumps(
            {
                "json": str(OUTPUT_JSON),
                "rpy": str(OUTPUT_RPY),
                "entry_count": len(entries),
                "first_source_line": entries[0]["source_line"],
                "last_source_line": entries[-1]["source_line"],
                "sequence_start": entries[0]["sequence"],
                "sequence_end": entries[-1]["sequence"],
                "rpy_structure": rpy_stats,
                "status": STATUS,
                "qa": QA,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
