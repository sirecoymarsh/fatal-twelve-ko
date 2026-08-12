from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
CATALOG = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\catalog\scenario_007_2.catalog.jsonl")
STYLE_GUIDE = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\style_guide.md")
GLOSSARY = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\glossary_draft.json")

SOURCE_FILE = "scenario/007_2.rpy"
CATALOG_SHA256 = "08345a226272a267ec7a2754b0106744fc04b8a25327db2b2868f47c2fc4d598"
STYLE_GUIDE_SHA256 = "b2b87352fdfd9b25af688152b0ce8a7460ffeb88fc06ae6e45f1c5df2ae83891"
GLOSSARY_SHA256 = "d7b49d77fcde5da240cb816890c75f9f15a2e83544db34a6193b8e939906300e"
STATUS = "first_draft_unreviewed"
QA = "deferred_until_full_first_draft"

PARTS = {
    "001_117": {
        "start": 1,
        "end": 117,
        "seed": HERE / "draft_007_2_001_117.seed.tsv",
        "json": HERE / "draft_007_2_001_117.json",
        "rpy": HERE / "draft_007_2_001_117.rpy",
    },
    "118_234": {
        "start": 118,
        "end": 234,
        "seed": HERE / "draft_007_2_118_234.seed.tsv",
        "json": HERE / "draft_007_2_118_234.json",
        "rpy": HERE / "draft_007_2_118_234.rpy",
    },
    "235_350": {
        "start": 235,
        "end": 350,
        "seed": HERE / "draft_007_2_235_350.seed.tsv",
        "json": HERE / "draft_007_2_235_350.json",
        "rpy": HERE / "draft_007_2_235_350.rpy",
    },
}
FINAL_JSON = HERE / "draft_007_2_001_350.json"
FINAL_RPY = HERE / "draft_007_2_001_350.rpy"


TOKEN_PATTERNS = {
    "renpy_text_tag": re.compile(r"\{[^{}\r\n]+\}"),
    "interpolation": re.compile(r"\[[^\[\]\r\n]+\]"),
    "printf": re.compile(r"%(?:\([^)]+\))?[#0 +\-]*\d*(?:\.\d+)?[diouxXeEfFgGcrsa%]"),
    "number": re.compile(
        r"(?:[0-9０-９]+(?:[.,．，][0-9０-９]+)*)|(?:[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]+)"
    ),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_frozen_inputs() -> None:
    expected = {
        CATALOG: CATALOG_SHA256,
        STYLE_GUIDE: STYLE_GUIDE_SHA256,
        GLOSSARY: GLOSSARY_SHA256,
    }
    for path, wanted in expected.items():
        actual = sha256(path)
        if actual != wanted:
            raise ValueError(f"frozen input changed: {path} expected={wanted} actual={actual}")


def load_seed(path: Path, start: int, end: int) -> dict[int, str]:
    drafts: dict[int, str] = {}
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw_line:
            continue
        try:
            index_text, draft = raw_line.split("\t", 1)
        except ValueError as exc:
            raise ValueError(f"seed requires one TAB at {path}:{line_number}") from exc
        index = int(index_text)
        if index in drafts:
            raise ValueError(f"duplicate command_index {index} at {path}:{line_number}")
        if not draft.strip():
            raise ValueError(f"empty Korean draft at {path}:{line_number}")
        drafts[index] = draft
    expected = set(range(start, end + 1))
    if set(drafts) != expected:
        raise ValueError(
            f"seed index mismatch for {path.name}: "
            f"missing={sorted(expected - set(drafts))}, extra={sorted(set(drafts) - expected)}"
        )
    return drafts


def load_catalog_rows(start: int, end: int) -> list[dict]:
    rows = []
    with CATALOG.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            record = json.loads(raw_line)
            if (
                record["source"]["script"] == SOURCE_FILE
                and start <= record["command_index"] <= end
            ):
                rows.append(record)
    rows.sort(key=lambda record: record["command_index"])
    indices = [record["command_index"] for record in rows]
    expected = list(range(start, end + 1))
    if indices != expected:
        raise ValueError(
            f"catalog command range changed for {start}-{end}: "
            f"first={indices[:3]} last={indices[-3:]} count={len(indices)}"
        )
    return rows


def assert_protected_tokens(record: dict, draft: str) -> None:
    actual: Counter[tuple[str, str]] = Counter()
    for kind, pattern in TOKEN_PATTERNS.items():
        actual.update((kind, match.group(0)) for match in pattern.finditer(draft))
    expected: Counter[tuple[str, str]] = Counter()
    for packed, count in record["protected_token_multiset"].items():
        kind, value = packed.split("\0", 1)
        expected[(kind, value)] = count
    if actual != expected:
        raise ValueError(
            f"protected token mismatch at command {record['command_index']}: "
            f"expected={dict(expected)} actual={dict(actual)}"
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
    return statement[:start] + json.dumps(target_ko, ensure_ascii=False) + statement[end + 1 :]


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


def build_rpy(entries: list[dict], start: int, end: int) -> tuple[str, dict]:
    lines = [
        "# -*- coding: utf-8 -*-",
        f"# Fatal Twelve scenario/007_2.rpy Korean first draft, AST ordinal {start}-{end}.",
        "# Semantic/style source: Japanese only; English prose was not opened or used.",
        f"# status: {STATUS}",
        f"# qa: {QA}",
        "",
    ]
    translate_ids: list[str] = []
    menu_entries: list[dict] = []
    for entry in entries:
        if entry["translation_id"] is None:
            if entry["menu_key"] is None:
                raise ValueError(f"entry has neither translation ID nor menu key: {entry['stable_id']}")
            menu_entries.append(entry)
            continue
        translate_ids.append(entry["translation_id"])
        lines.append(f"# {entry['stable_id']} | {entry['source_file']}:{entry['source_line']}")
        lines.append(f"translate korean {entry['translation_id']}:")
        replaced = 0
        for code_line in entry["source_group_code"]:
            if code_line == entry["source_statement_code"]:
                lines.append(f"    # {code_line}")
                lines.append(
                    "    "
                    + replace_statement_text(code_line, entry["source_jp"], entry["draft_ko"])
                )
                replaced += 1
            else:
                lines.append(f"    {code_line}")
        if replaced != 1:
            raise ValueError(f"expected one Say replacement: {entry['stable_id']}")
        lines.append("")

    if menu_entries:
        lines.extend(["translate korean strings:", ""])
        for entry in menu_entries:
            lines.append(f"    # {entry['stable_id']} | {entry['source_file']}:{entry['source_line']}")
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


def write_packet(
    *, start: int, end: int, drafts: dict[int, str], output_json: Path, output_rpy: Path
) -> dict:
    rows = load_catalog_rows(start, end)
    entries = []
    for row in rows:
        draft = drafts[row["command_index"]]
        assert_protected_tokens(row, draft)
        entries.append(build_entry(row, draft))

    rpy_text, rpy_stats = build_rpy(entries, start, end)
    lane_counts = Counter(entry["lane"] for entry in entries)
    packet = {
        "schema_version": "fatal-twelve-ko-first-draft-v1",
        "packet_id": f"scenario_007_2_ast_ordinal_{start}_{end}",
        "source_file": SOURCE_FILE,
        "sequence_semantics": "exact AST catalog command_index including Ren'Py menu strings",
        "sequence_start": start,
        "sequence_end": end,
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
            "path": str(CATALOG),
            "sha256": CATALOG_SHA256,
            "stable_id_source": "exact catalog stable_id",
            "join_contract": "source_file+source_line+speaker+source_jp exact identity; no ordinal zip",
        },
        "rpy_structure": rpy_stats,
        "entries": entries,
    }
    output_json.write_text(
        json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    output_rpy.write_text(rpy_text, encoding="utf-8", newline="\n")
    return {
        "json": str(output_json),
        "json_sha256": sha256(output_json),
        "rpy": str(output_rpy),
        "rpy_sha256": sha256(output_rpy),
        "entry_count": len(entries),
        "first_source_line": entries[0]["source_line"],
        "last_source_line": entries[-1]["source_line"],
        "sequence_start": start,
        "sequence_end": end,
        "rpy_structure": rpy_stats,
        "status": STATUS,
        "qa": QA,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--part",
        choices=[*PARTS, "all"],
        default="all",
        help="Build one checkpoint or both checkpoints plus the merged packet.",
    )
    args = parser.parse_args()
    assert_frozen_inputs()

    wanted = list(PARTS) if args.part == "all" else [args.part]
    reports = []
    loaded: dict[str, dict[int, str]] = {}
    for name in wanted:
        spec = PARTS[name]
        drafts = load_seed(spec["seed"], spec["start"], spec["end"])
        loaded[name] = drafts
        reports.append(
            write_packet(
                start=spec["start"],
                end=spec["end"],
                drafts=drafts,
                output_json=spec["json"],
                output_rpy=spec["rpy"],
            )
        )

    if args.part == "all":
        merged = {}
        for name in PARTS:
            merged.update(loaded[name])
        reports.append(
            write_packet(
                start=1,
                end=350,
                drafts=merged,
                output_json=FINAL_JSON,
                output_rpy=FINAL_RPY,
            )
        )
    print(json.dumps({"reports": reports}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
