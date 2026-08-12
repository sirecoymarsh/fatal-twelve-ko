from __future__ import annotations

import ast
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
CATALOG = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\catalog\scenario_009.catalog.jsonl")
META = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\catalog\scenario_009.catalog.meta.json")
VALIDATION = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\catalog\scenario_009.validation.json")
SOURCE = HERE.parent / "jp_recovery" / "raw" / "scenario" / "009.rpy"
DRAFT_JSON = HERE / "draft_009_801_1200.json"
DRAFT_RPY = HERE / "draft_009_801_1200.rpy"
REPORT = HERE / "draft_009_801_1200.structure_check.json"

START = 801
END = 1200
SOURCE_FILE = "scenario/009.rpy"
CATALOG_SHA256 = "acba3c94ebbf88c9d06790bd5ae9902901cabe2dfaafe97437da53b73641b20e"
STATUS = "first_draft_unreviewed"
QA = "deferred_until_full_first_draft"

TOKEN_PATTERNS = {
    "renpy_text_tag": re.compile(r"\{[^{}\r\n]+\}"),
    "interpolation": re.compile(r"\[[^\[\]\r\n]+\]"),
    "printf": re.compile(r"%(?:\([^)]+\))?[#0 +\-]*\d*(?:\.\d+)?[diouxXeEfFgGcrsa%]"),
    "number": re.compile(r"(?:[0-9０-９]+(?:[.,．，][0-9０-９]+)*)|(?:[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]+)"),
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def replace_statement_text(statement: str, source_jp: str, target_ko: str) -> str:
    start = statement.find('"')
    if start < 0:
        raise ValueError(f"no string literal in statement: {statement!r}")
    escaped = False
    end = None
    for pos in range(start + 1, len(statement)):
        ch = statement[pos]
        if escaped:
            escaped = False
        elif ch == "\\":
            escaped = True
        elif ch == '"':
            end = pos
            break
    if end is None:
        raise ValueError(f"unterminated string literal: {statement!r}")
    literal = statement[start:end + 1]
    if ast.literal_eval(literal) != source_jp:
        raise ValueError(f"source literal mismatch: {statement!r}")
    return statement[:start] + json.dumps(target_ko, ensure_ascii=False) + statement[end + 1:]


def token_multiset(text: str) -> Counter[tuple[str, str]]:
    out: Counter[tuple[str, str]] = Counter()
    for kind, pattern in TOKEN_PATTERNS.items():
        out.update((kind, m.group(0)) for m in pattern.finditer(text))
    return out


all_rows = [json.loads(line) for line in CATALOG.read_text(encoding="utf-8").splitlines() if line]
rows = [
    row for row in all_rows
    if row["source"]["script"] == SOURCE_FILE and START <= row["command_index"] <= END
]
rows.sort(key=lambda row: row["command_index"])
row_by_index = {row["command_index"]: row for row in rows}

packet = json.loads(DRAFT_JSON.read_text(encoding="utf-8"))
entries = packet["entries"]
rpy_text = DRAFT_RPY.read_text(encoding="utf-8")
rpy_lines = rpy_text.splitlines()
meta = json.loads(META.read_text(encoding="utf-8"))
validation = json.loads(VALIDATION.read_text(encoding="utf-8"))

checks: dict[str, dict] = {}


def add(name: str, passed: bool, detail=None) -> None:
    item = {"passed": bool(passed)}
    if detail is not None:
        item["detail"] = detail
    checks[name] = item


expected_indices = list(range(START, END + 1))
catalog_indices = [row["command_index"] for row in rows]
draft_indices = [entry["command_index"] for entry in entries]
add(
    "exact_range",
    catalog_indices == expected_indices and draft_indices == expected_indices,
    {
        "expected_count": len(expected_indices),
        "catalog_count": len(rows),
        "draft_count": len(entries),
        "catalog_first_last": [catalog_indices[0], catalog_indices[-1]] if catalog_indices else [],
        "draft_first_last": [draft_indices[0], draft_indices[-1]] if draft_indices else [],
    },
)

expected_rpy_structure = {
    "translate_blocks": sum(row["localization"]["translation_id"] is not None for row in rows),
    "strings_entries": sum(row["localization"]["translation_id"] is None for row in rows),
    "unique_translation_ids": len({
        row["localization"]["translation_id"] for row in rows
        if row["localization"]["translation_id"] is not None
    }),
}
metadata_ok = (
    packet.get("packet_id") == "scenario_009_ast_ordinal_801_1200"
    and packet.get("source_file") == SOURCE_FILE
    and packet.get("sequence_start") == START
    and packet.get("sequence_end") == END
    and packet.get("entry_count") == 400
    and packet.get("first_source_line") == 3107
    and packet.get("last_source_line") == 4540
    and packet.get("rpy_structure") == expected_rpy_structure
    and packet.get("catalog", {}).get("sha256") == CATALOG_SHA256
)
add("packet_metadata", metadata_ok)

packet_flags_ok = (
    packet.get("status") == STATUS
    and packet.get("qa") == QA
    and packet.get("source_language") == "ja"
    and packet.get("target_language") == "ko"
    and packet.get("source_authority") == "Japanese only"
    and packet.get("english_reference_used") is False
    and packet.get("external_translation_api_used") is False
    and packet.get("translation_validation") == "not_performed"
    and packet.get("structure_validation") == "performed_during_generation"
)
add("packet_flags", packet_flags_ok)

identity_mismatches = []
bad_entries = []
token_mismatches = []
for entry in entries:
    ci = entry["command_index"]
    row = row_by_index.get(ci)
    if row is None:
        identity_mismatches.append({"command_index": ci, "reason": "not in catalog range"})
        continue
    source = row["source"]
    loc = row["localization"]
    speaker = row["speaker"]["code"] if row["speaker"] else "narrator"
    voice = row["voice_call"]["statement"] if row["voice_call"] else ""
    expected = {
        "sequence": ci,
        "stable_id": row["stable_id"],
        "translation_id": loc["translation_id"],
        "menu_key": loc["menu_key"],
        "id_origin": loc["id_origin"],
        "source_file": source["script"],
        "source_line": source["line"],
        "source_label": source["label"],
        "lane": row["lane"],
        "speaker": speaker,
        "source_jp": source["text_ja"],
        "source_statement_code": source["statement_code"],
        "source_group_code": source["group_code"],
        "source_text_sha256": source["text_sha256"],
        "source_group_sha256": source["group_sha256"],
        "renpy_digest": source["renpy_digest"],
        "voice_call": voice,
        "protected_tokens": row["protected_tokens"],
    }
    diffs = {
        key: {"expected": value, "actual": entry.get(key)}
        for key, value in expected.items() if entry.get(key) != value
    }
    if diffs:
        identity_mismatches.append({"command_index": ci, "diffs": diffs})
    if (
        not isinstance(entry.get("draft_ko"), str)
        or not entry["draft_ko"].strip()
        or entry.get("source_authority") != "Japanese only"
        or entry.get("english_reference_used") is not False
        or entry.get("status") != STATUS
        or entry.get("qa") != QA
    ):
        bad_entries.append(ci)
    expected_tokens: Counter[tuple[str, str]] = Counter()
    for packed, count in row["protected_token_multiset"].items():
        kind, value = packed.split("\0", 1)
        expected_tokens[(kind, value)] = count
    actual_tokens = token_multiset(entry["draft_ko"])
    if actual_tokens != expected_tokens:
        token_mismatches.append({
            "command_index": ci,
            "expected": [[k, v, n] for (k, v), n in sorted(expected_tokens.items())],
            "actual": [[k, v, n] for (k, v), n in sorted(actual_tokens.items())],
        })

add(
    "exact_catalog_identity",
    not identity_mismatches,
    {"mismatch_count": len(identity_mismatches), "mismatches": identity_mismatches[:20]},
)
add("entry_flags_and_nonempty", not bad_entries, {"bad_commands": bad_entries})
add(
    "protected_token_multisets",
    not token_mismatches,
    {"mismatch_count": len(token_mismatches), "mismatches": token_mismatches[:20]},
)

headers = []
for i, line in enumerate(rpy_lines):
    m = re.fullmatch(r"translate korean (\S+):", line)
    if m and m.group(1) != "strings":
        headers.append((i, m.group(1)))
actual_ids = [translation_id for _, translation_id in headers]
expected_nonmenu_rows = [row for row in rows if row["localization"]["translation_id"] is not None]
expected_ids = [row["localization"]["translation_id"] for row in expected_nonmenu_rows]
add(
    "translate_blocks",
    len(actual_ids) == 394 and len(set(actual_ids)) == 394,
    {"blocks": len(actual_ids), "unique_ids": len(set(actual_ids))},
)
add("translate_id_order", actual_ids == expected_ids)

entry_by_id = {
    entry["translation_id"]: entry for entry in entries if entry["translation_id"] is not None
}
block_mismatches = []
for line_index, translation_id in headers:
    entry = entry_by_id.get(translation_id)
    if entry is None:
        block_mismatches.append({"translation_id": translation_id, "reason": "no packet entry"})
        continue
    body = []
    j = line_index + 1
    while j < len(rpy_lines) and rpy_lines[j].strip():
        body.append(rpy_lines[j])
        j += 1
    expected_body = []
    replaced = 0
    for code_line in entry["source_group_code"]:
        if code_line == entry["source_statement_code"]:
            expected_body.append("    # " + code_line)
            expected_body.append(
                "    " + replace_statement_text(
                    code_line, entry["source_jp"], entry["draft_ko"]
                )
            )
            replaced += 1
        else:
            expected_body.append("    " + code_line)
    if replaced != 1 or body != expected_body:
        block_mismatches.append({
            "translation_id": translation_id,
            "command_index": entry["command_index"],
            "expected": expected_body,
            "actual": body,
        })
add(
    "control_voice_display_tail",
    not block_mismatches,
    {"mismatch_count": len(block_mismatches), "mismatches": block_mismatches[:10]},
)

expected_menu_entries = [entry for entry in entries if entry["translation_id"] is None]
actual_menu_pairs = []
for i, line in enumerate(rpy_lines):
    m = re.fullmatch(r"    old (.+)", line)
    if not m:
        continue
    if i + 1 >= len(rpy_lines):
        actual_menu_pairs.append(("<missing-next-line>", "<missing-next-line>"))
        continue
    n = re.fullmatch(r"    new (.+)", rpy_lines[i + 1])
    if not n:
        actual_menu_pairs.append((ast.literal_eval(m.group(1)), "<missing-new-line>"))
        continue
    actual_menu_pairs.append((ast.literal_eval(m.group(1)), ast.literal_eval(n.group(1))))
expected_menu_pairs = [(entry["source_jp"], entry["draft_ko"]) for entry in expected_menu_entries]
add(
    "menu_strings_lane",
    actual_menu_pairs == expected_menu_pairs and len(actual_menu_pairs) == 6,
    {
        "expected_count": len(expected_menu_pairs),
        "actual_count": len(actual_menu_pairs),
        "expected_pairs": expected_menu_pairs,
        "actual_pairs": actual_menu_pairs,
    },
)

expected_explicit_voice = sum(
    row["voice_call"] is not None
    for row in expected_nonmenu_rows
)
expected_json_voice = sum(row["voice_call"] is not None for row in rows)
actual_explicit_voice = sum(bool(re.match(r"    voice\s+", line)) for line in rpy_lines)
actual_json_voice = sum(bool(entry["voice_call"]) for entry in entries)
add(
    "voice_count",
    (
        expected_explicit_voice == actual_explicit_voice == 129
        and expected_json_voice == actual_json_voice == 130
    ),
    {
        "expected_explicit_rpy": expected_explicit_voice,
        "actual_explicit_rpy": actual_explicit_voice,
        "expected_json_including_menu_prompt": expected_json_voice,
        "actual_json_including_menu_prompt": actual_json_voice,
    },
)

validation_ok = (
    validation.get("passed") is True
    and validation.get("source_rebuild_performed") is True
    and validation.get("records") == 1588
    and validation.get("errors") == []
    and validation.get("warnings") == []
    and meta.get("statistics", {}).get("records") == 1588
    and meta.get("policy", {}).get("semantic_source_language") == "ja"
    and meta.get("policy", {}).get("reference_prose_parsed") is False
    and meta.get("policy", {}).get("live_game_modified") is False
)
add(
    "catalog_source_rebuild_validation",
    validation_ok,
    {
        "records": validation.get("records"),
        "errors": len(validation.get("errors", [])),
        "warnings": len(validation.get("warnings", [])),
        "source_rebuild_performed": validation.get("source_rebuild_performed"),
    },
)

passed = all(item["passed"] for item in checks.values())
lane_counts = Counter(entry["lane"] for entry in entries)
report = {
    "schema_version": "fatal-twelve-ko-structure-check-v1",
    "subject": str(DRAFT_JSON),
    "validation_scope": "structure_only",
    "translation_qa_performed": False,
    "translation_qa": QA,
    "passed": passed,
    "summary": {
        "catalog_total_records": len(all_rows),
        "draft_entries": len(entries),
        "command_index_start": START,
        "command_index_end": END,
        "first_source_line": entries[0]["source_line"] if entries else None,
        "last_source_line": entries[-1]["source_line"] if entries else None,
        "lanes": dict(sorted(lane_counts.items())),
        "translate_blocks": len(actual_ids),
        "voice_lines": actual_explicit_voice,
        "json_voice_records": actual_json_voice,
        "menu_entries": len(actual_menu_pairs),
        "unique_translation_ids": len(set(actual_ids)),
    },
    "hashes": {
        "japanese_source_sha256": sha256(SOURCE),
        "catalog_sha256": sha256(CATALOG),
        "catalog_meta_sha256": sha256(META),
        "catalog_validation_sha256": sha256(VALIDATION),
        "draft_json_sha256": sha256(DRAFT_JSON),
        "draft_rpy_sha256": sha256(DRAFT_RPY),
    },
    "checks": checks,
}
REPORT.write_text(
    json.dumps(report, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(json.dumps(report, ensure_ascii=False, indent=2))
if not passed:
    sys.exit(1)
