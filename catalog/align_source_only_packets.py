#!/usr/bin/env python3
"""Align draft packets to the exact Japanese Ren'Py AST catalog.

The primary join is source_file + source_line + normalized speaker. Exact
Japanese source equality is mandatory. Sequence order and English prose are
never used as alignment evidence. Existing draft_ko values are immutable.
"""

from __future__ import annotations

import argparse
import ast
import copy
import datetime as dt
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable, Sequence


CATALOG_SCHEMA = "fatal-twelve-renpy-catalog-v1"
ALIGNED_SCHEMA = "fatal-twelve-aligned-draft-v1"
MUTABLE_ENTRY_FIELDS = {
    "stable_id",
    "sequence",
    "translation_id",
    "translation_id_status",
    "id_origin",
    "alignment",
}
ADDED_ENTRY_FIELDS = {
    "source_packet_sequence",
    "source_packet_stable_id",
    "catalog_command_index",
    "catalog_stable_id",
    "menu_key",
    "source_text_sha256",
    "source_group_sha256",
    "renpy_digest",
    "catalog_lane",
    "catalog_voice_call",
    "source_statement_code",
    "source_group_code",
    "protected_tokens",
}
TRANSLATE_HEADER_RE = re.compile(r"^translate korean (?!strings:)([A-Za-z0-9_]+):$", re.MULTILINE)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def file_info(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    return {"path": str(path.resolve()), "size": len(raw), "sha256": sha256_bytes(raw)}


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, values: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n" for value in values)
    path.write_text(text, encoding="utf-8")


def normalize_source_file(value: str) -> str:
    return value.replace("\\", "/").lstrip("./")


def normalize_speaker(value: Any) -> str:
    if value is None or value == "narrator":
        return "narrator"
    if not isinstance(value, str) or not value:
        raise ValueError(f"invalid speaker: {value!r}")
    return value


def catalog_speaker(record: dict[str, Any]) -> str:
    speaker = record.get("speaker")
    return "narrator" if speaker is None else normalize_speaker(speaker.get("code"))


def source_payload_hash(entries: Iterable[dict[str, Any]], field: str) -> str:
    values = [entry.get(field) for entry in entries]
    blob = json.dumps(values, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return sha256_bytes(blob)


def build_index(catalog: list[dict[str, Any]]) -> dict[tuple[str, int, str], list[dict[str, Any]]]:
    index: dict[tuple[str, int, str], list[dict[str, Any]]] = defaultdict(list)
    for record in catalog:
        if record.get("schema_version") != CATALOG_SCHEMA:
            raise ValueError(f"unexpected catalog schema: {record.get('schema_version')}")
        key = (
            normalize_source_file(record["source"]["script"]),
            int(record["source"]["line"]),
            catalog_speaker(record),
        )
        index[key].append(record)
    return index


def match_catalog(
    entry: dict[str, Any],
    index: dict[tuple[str, int, str], list[dict[str, Any]]],
) -> dict[str, Any]:
    key = (
        normalize_source_file(entry["source_file"]),
        int(entry["source_line"]),
        normalize_speaker(entry.get("speaker")),
    )
    candidates = index.get(key, [])
    exact_text = [candidate for candidate in candidates if candidate["source"]["text_ja"] == entry.get("source_jp")]
    if len(exact_text) == 1:
        candidates = exact_text
    if len(candidates) != 1:
        raise ValueError(f"catalog join for {key!r} returned {len(candidates)} candidates")
    record = candidates[0]
    if entry.get("source_jp") != record["source"]["text_ja"]:
        raise ValueError(
            f"Japanese source mismatch at {key}: packet={entry.get('source_jp')!r} "
            f"catalog={record['source']['text_ja']!r}"
        )
    return record


def unchanged_except_metadata(before: dict[str, Any], after: dict[str, Any]) -> None:
    for key, value in before.items():
        if key in MUTABLE_ENTRY_FIELDS:
            continue
        if after.get(key) != value:
            raise ValueError(f"non-metadata field changed: {key}")
    unexpected = set(after) - set(before) - ADDED_ENTRY_FIELDS - MUTABLE_ENTRY_FIELDS
    if unexpected:
        raise ValueError(f"unexpected added fields: {sorted(unexpected)}")


def alignment_status(record: dict[str, Any]) -> str:
    if record["localization"]["translation_id"] is not None:
        return "aligned_exact_ast_hash"
    if record["alignment"]["confidence"] == "exact":
        return "aligned_exact_menu_old_key"
    return "aligned_source_menu_reference_missing"


def align_entry(entry: dict[str, Any], record: dict[str, Any], packet_sequence: int) -> dict[str, Any]:
    before = copy.deepcopy(entry)
    aligned = copy.deepcopy(entry)
    localization = record["localization"]
    catalog_alignment = copy.deepcopy(record["alignment"])
    catalog_alignment["join_evidence"] = {
        "method": "source identity join; no sequence zip",
        "keys": ["source_file", "source_line", "speaker"],
        "source_file": normalize_source_file(entry["source_file"]),
        "source_line": int(entry["source_line"]),
        "speaker": normalize_speaker(entry.get("speaker")),
        "source_text_exact_match": True,
        "source_text_sha256": record["source"]["text_sha256"],
        "catalog_command_index": record["command_index"],
        "catalog_stable_id": record["stable_id"],
    }

    aligned["source_packet_sequence"] = packet_sequence
    aligned["source_packet_stable_id"] = entry.get("stable_id")
    aligned["stable_id"] = record["stable_id"]
    aligned["sequence"] = record["command_index"]
    aligned["catalog_command_index"] = record["command_index"]
    aligned["catalog_stable_id"] = record["stable_id"]
    aligned["translation_id"] = localization["translation_id"]
    aligned["menu_key"] = localization["menu_key"]
    aligned["translation_id_status"] = alignment_status(record)
    aligned["id_origin"] = localization["id_origin"]
    aligned["alignment"] = catalog_alignment
    aligned["source_text_sha256"] = record["source"]["text_sha256"]
    aligned["source_group_sha256"] = record["source"]["group_sha256"]
    aligned["renpy_digest"] = record["source"]["renpy_digest"]
    aligned["catalog_lane"] = record["lane"]
    aligned["catalog_voice_call"] = copy.deepcopy(record["voice_call"])
    aligned["source_statement_code"] = record["source"]["statement_code"]
    aligned["source_group_code"] = copy.deepcopy(record["source"]["group_code"])
    aligned["protected_tokens"] = copy.deepcopy(record["protected_tokens"])

    unchanged_except_metadata(before, aligned)
    if aligned.get("draft_ko") != before.get("draft_ko"):
        raise ValueError("draft_ko changed during metadata alignment")
    if aligned.get("source_jp") != before.get("source_jp"):
        raise ValueError("source_jp changed during metadata alignment")
    return aligned


def alignment_summary(entries: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "entries": len(entries),
        "source_packet_sequence_start": min(entry["source_packet_sequence"] for entry in entries),
        "source_packet_sequence_end": max(entry["source_packet_sequence"] for entry in entries),
        "catalog_sequence_start": min(entry["sequence"] for entry in entries),
        "catalog_sequence_end": max(entry["sequence"] for entry in entries),
        "translation_ids": sum(entry["translation_id"] is not None for entry in entries),
        "menu_keys": sum(entry["menu_key"] is not None for entry in entries),
        "reference_missing": sum(entry["alignment"]["confidence"] == "unmatched-reference" for entry in entries),
        "sequence_changed": sum(entry["source_packet_sequence"] != entry["sequence"] for entry in entries),
        "translation_text_modified": False,
    }


def aligned_document(source: dict[str, Any], entries: list[dict[str, Any]], catalog_path: Path) -> dict[str, Any]:
    aligned = copy.deepcopy(source)
    aligned["entries"] = entries
    aligned["schema_version"] = ALIGNED_SCHEMA
    aligned["alignment_status"] = "complete_exact_source_join"
    aligned["translation_id_alignment"] = (
        "complete: source_file+source_line+speaker+exact Japanese source -> AST catalog; no sequence zip"
    )
    aligned["alignment_catalog"] = {**file_info(catalog_path), "schema_version": CATALOG_SCHEMA}
    aligned["sequence_semantics"] = "AST catalog command_index including Ren'Py menu strings"
    aligned["source_packet_sequence_semantics"] = "translator work order excluding menu choice lines; preserved separately"
    aligned["alignment_summary"] = alignment_summary(entries)
    return aligned


def replace_statement_text(statement: str, source_jp: str, target_ko: str) -> str:
    start = statement.find('"')
    if start < 0:
        raise ValueError(f"no string literal in statement: {statement!r}")
    escaped = False
    end = None
    for pos in range(start + 1, len(statement)):
        char = statement[pos]
        if escaped:
            escaped = False
        elif char == "\\":
            escaped = True
        elif char == '"':
            end = pos
            break
    if end is None:
        raise ValueError(f"unterminated string literal: {statement!r}")
    literal = statement[start : end + 1]
    try:
        decoded = ast.literal_eval(literal)
    except (SyntaxError, ValueError) as exc:
        raise ValueError(f"cannot decode source literal {literal!r}") from exc
    if decoded != source_jp:
        raise ValueError(f"source literal mismatch: decoded={decoded!r}, expected={source_jp!r}")
    target_literal = json.dumps(target_ko, ensure_ascii=False)
    return statement[:start] + target_literal + statement[end + 1 :]


def render_recovery_rpy(entries: list[dict[str, Any]]) -> tuple[str, dict[str, Any]]:
    lines = [
        "# Fatal Twelve Korean aligned draft: scenario/001 source packet 151-350",
        "# Japanese source identity and Ren'Py 6.99 AST IDs; no English prose used.",
        "# draft_ko payload is copied byte-for-value from the source JSON; QA deferred.",
        "",
    ]
    say_ids: list[str] = []
    menu_entries: list[dict[str, Any]] = []
    for entry in sorted(entries, key=lambda item: item["source_packet_sequence"]):
        translation_id = entry["translation_id"]
        if translation_id is None:
            if entry["menu_key"] is None:
                raise ValueError(f"record has neither translation ID nor menu key: {entry['stable_id']}")
            menu_entries.append(entry)
            continue
        say_ids.append(translation_id)
        statement = entry["source_statement_code"]
        group = entry["source_group_code"]
        if statement not in group:
            raise ValueError(f"statement missing from group_code: {entry['stable_id']}")
        replaced_count = 0
        rendered_group = []
        for code_line in group:
            if code_line == statement:
                rendered_group.append(replace_statement_text(code_line, entry["source_jp"], entry["draft_ko"]))
                replaced_count += 1
            else:
                rendered_group.append(code_line)
        if replaced_count != 1:
            raise ValueError(f"expected one statement replacement, got {replaced_count}: {entry['stable_id']}")
        lines.append(f"translate korean {translation_id}:")
        lines.append("")
        lines.extend(f"    {code_line}" for code_line in rendered_group)
        lines.append("")
        lines.append("")

    if menu_entries:
        lines.append("translate korean strings:")
        lines.append("")
        for entry in menu_entries:
            lines.append(f"    # {entry['menu_key']} | source line {entry['source_line']}")
            lines.append(f"    old {json.dumps(entry['source_jp'], ensure_ascii=False)}")
            lines.append(f"    new {json.dumps(entry['draft_ko'], ensure_ascii=False)}")
            lines.append("")

    text = "\n".join(lines).rstrip() + "\n"
    parsed_ids = TRANSLATE_HEADER_RE.findall(text)
    if parsed_ids != say_ids:
        raise ValueError("rendered RPY translate IDs do not match aligned JSON order")
    if len(parsed_ids) != len(set(parsed_ids)):
        raise ValueError("duplicate translate IDs in rendered recovery RPY")
    if text.count("\n    old ") != len(menu_entries) or text.count("\n    new ") != len(menu_entries):
        raise ValueError("rendered RPY strings count mismatch")
    return text, {
        "translate_blocks": len(say_ids),
        "strings_entries": len(menu_entries),
        "unique_translate_ids": len(set(say_ids)),
    }


def exact_record(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "sequence": record["command_index"],
        "stable_id": record["stable_id"],
        "translation_id": record["localization"]["translation_id"],
        "menu_key": record["localization"]["menu_key"],
        "id_origin": record["localization"]["id_origin"],
        "source_file": record["source"]["script"],
        "source_line": record["source"]["line"],
        "label": record["source"]["label"],
        "speaker": catalog_speaker(record),
        "lane": record["lane"],
        "source_jp": record["source"]["text_ja"],
        "voice_call": record["voice_call"],
        "protected_tokens": record["protected_tokens"],
        "alignment": record["alignment"],
    }


def contiguous_ranges(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    if not records:
        return []
    groups: list[list[dict[str, Any]]] = [[records[0]]]
    for record in records[1:]:
        if record["command_index"] == groups[-1][-1]["command_index"] + 1:
            groups[-1].append(record)
        else:
            groups.append([record])
    ranges = []
    for ordinal, group in enumerate(groups, 1):
        labels: list[str | None] = []
        for record in group:
            label = record["source"]["label"]
            if label not in labels:
                labels.append(label)
        ranges.append(
            {
                "range_id": f"scenario_001_untranslated_{ordinal:03d}",
                "sequence_start": group[0]["command_index"],
                "sequence_end": group[-1]["command_index"],
                "count": len(group),
                "source_line_start": group[0]["source"]["line"],
                "source_line_end": group[-1]["source"]["line"],
                "first_stable_id": group[0]["stable_id"],
                "last_stable_id": group[-1]["stable_id"],
                "labels": labels,
            }
        )
    return ranges


def map_existing_translation(
    entry: dict[str, Any],
    index: dict[tuple[str, int, str], list[dict[str, Any]]],
) -> dict[str, Any]:
    if not isinstance(entry.get("draft_ko"), str) or not entry["draft_ko"].strip():
        raise ValueError(f"empty draft_ko at {entry.get('source_file')}:{entry.get('source_line')}")
    return match_catalog(entry, index)


def make_markdown(report: dict[str, Any]) -> str:
    lines = [
        "# scenario/001 exact untranslated ranges",
        "",
        f"- Catalog records: {report['catalog_records']}",
        f"- Exact-source draft records: {report['draft_translated_records']}",
        f"- Untranslated records: **{report['untranslated_records']}**",
        f"- Contiguous ranges: {len(report['ranges'])}",
        "- sequence means AST catalog command_index and includes Ren'Py menu strings.",
        "",
        "| Range | sequence | count | source line | label |",
        "|---|---:|---:|---:|---|",
    ]
    for item in report["ranges"]:
        sequence = (
            f"{item['sequence_start']}-{item['sequence_end']}"
            if item["sequence_start"] != item["sequence_end"]
            else str(item["sequence_start"])
        )
        source = (
            f"{item['source_line_start']}-{item['source_line_end']}"
            if item["source_line_start"] != item["source_line_end"]
            else str(item["source_line_start"])
        )
        labels = ", ".join(label or "<none>" for label in item["labels"])
        lines.append(f"| {item['range_id']} | {sequence} | {item['count']} | {source} | {labels} |")
    lines.extend(
        [
            "",
            "See scenario_001_untranslated_records.json/jsonl for exact Japanese source, speaker, ID/menu key, voice, and protected tokens.",
            "Draft presence is source-identity based. This report does not claim translation QA completion.",
            "",
        ]
    )
    return "\n".join(lines)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--coverage-output-dir", type=Path, required=True)
    parser.add_argument("--recovery-json", type=Path, required=True)
    parser.add_argument("--recovery-rpy", type=Path, required=True)
    parser.add_argument("--bridge-json", type=Path, required=True)
    parser.add_argument("--tail-json", type=Path, required=True)
    parser.add_argument("--tail-rpy", type=Path, required=True)
    parser.add_argument("--menus-json", type=Path, required=True)
    parser.add_argument("--menus-rpy", type=Path, required=True)
    parser.add_argument("--source-packet-start", type=int, default=351)
    return parser.parse_args(argv)





def process_menus(
    args: argparse.Namespace,
    index: dict[tuple[str, int, str], list[dict[str, Any]]],
) -> tuple[Path, Path, dict[str, Any]]:
    """Align the six missing menu strings and preserve their RPY byte-for-byte."""
    source = read_json(args.menus_json)
    original_entries = source["entries"]
    before_draft_hash = source_payload_hash(original_entries, "draft_ko")
    before_source_hash = source_payload_hash(original_entries, "source_jp")
    aligned_entries = []
    comparison = {
        "entries": len(original_entries),
        "existing_stable_id_mismatch": 0,
        "existing_menu_key_mismatch": 0,
        "existing_sequence_mismatch": 0,
        "unexpected_translation_id": 0,
    }
    for entry in original_entries:
        packet_sequence = int(entry["sequence"])
        record = match_catalog(entry, index)
        localization = record["localization"]
        if entry.get("stable_id") != record["stable_id"]:
            comparison["existing_stable_id_mismatch"] += 1
        if entry.get("menu_key") != localization["menu_key"]:
            comparison["existing_menu_key_mismatch"] += 1
        if packet_sequence != record["command_index"]:
            comparison["existing_sequence_mismatch"] += 1
        if entry.get("translation_id") is not None or localization["translation_id"] is not None:
            comparison["unexpected_translation_id"] += 1
        aligned_entries.append(align_entry(entry, record, packet_sequence))
    if len(aligned_entries) != 6:
        raise ValueError(f"expected six missing menus, got {len(aligned_entries)}")
    if any(comparison[key] for key in comparison if key != "entries"):
        raise ValueError(f"menu structural metadata mismatch: {comparison}")

    aligned = aligned_document(source, aligned_entries, args.catalog)
    aligned["menu_structural_comparison"] = comparison
    output_json = args.output_dir / "001_missing_menus_aligned.json"
    output_rpy = args.output_dir / "001_missing_menus_aligned.rpy"
    write_json(output_json, aligned)
    output_rpy.write_bytes(args.menus_rpy.read_bytes())

    after = read_json(output_json)
    after_draft_hash = source_payload_hash(after["entries"], "draft_ko")
    after_source_hash = source_payload_hash(after["entries"], "source_jp")
    if before_draft_hash != after_draft_hash or before_source_hash != after_source_hash:
        raise ValueError("menu translation/source payload changed")
    rpy_text = output_rpy.read_text(encoding="utf-8")
    old_values = [ast.literal_eval(line.strip()[4:]) for line in rpy_text.splitlines() if line.strip().startswith("old ")]
    new_values = [ast.literal_eval(line.strip()[4:]) for line in rpy_text.splitlines() if line.strip().startswith("new ")]
    if old_values != [entry["source_jp"] for entry in aligned_entries]:
        raise ValueError("menu RPY old strings/order do not match aligned JSON")
    if new_values != [entry["draft_ko"] for entry in aligned_entries]:
        raise ValueError("menu RPY new strings/order do not match aligned JSON")
    if file_info(args.menus_rpy)["sha256"] != file_info(output_rpy)["sha256"]:
        raise ValueError("menu RPY bytes changed")

    manifest_item = {
        "kind": "scenario001_missing_menus_json_and_rpy",
        "input_json": file_info(args.menus_json),
        "input_rpy": file_info(args.menus_rpy),
        "output_json": file_info(output_json),
        "output_rpy": file_info(output_rpy),
        "entries": len(aligned_entries),
        "source_packet_sequence": [
            min(entry["source_packet_sequence"] for entry in aligned_entries),
            max(entry["source_packet_sequence"] for entry in aligned_entries),
        ],
        "catalog_sequence": [
            min(entry["sequence"] for entry in aligned_entries),
            max(entry["sequence"] for entry in aligned_entries),
        ],
        "draft_ko_sha256_before": before_draft_hash,
        "draft_ko_sha256_after": after_draft_hash,
        "source_jp_sha256_before": before_source_hash,
        "source_jp_sha256_after": after_source_hash,
        "structural_comparison": comparison,
        "rpy_bytes_preserved": True,
        "translation_text_modified": False,
    }
    return output_json, output_rpy, manifest_item

def process_tail(
    args: argparse.Namespace,
    index: dict[tuple[str, int, str], list[dict[str, Any]]],
) -> tuple[Path, Path, dict[str, Any]]:
    """Align the exact-ID tail JSON and preserve its RPY byte-for-byte."""
    source = read_json(args.tail_json)
    original_entries = source["entries"]
    before_draft_hash = source_payload_hash(original_entries, "draft_ko")
    before_source_hash = source_payload_hash(original_entries, "source_jp")
    aligned_entries = []
    comparison = {
        "entries": len(original_entries),
        "existing_translation_id_mismatch": 0,
        "existing_command_index_mismatch": 0,
        "existing_stable_id_mismatch": 0,
    }
    for entry in original_entries:
        packet_sequence = int(entry["sequence"])
        record = match_catalog(entry, index)
        if entry.get("translation_id") != record["localization"]["translation_id"]:
            comparison["existing_translation_id_mismatch"] += 1
        if int(entry.get("command_index")) != record["command_index"]:
            comparison["existing_command_index_mismatch"] += 1
        if entry.get("stable_id") != record["stable_id"]:
            comparison["existing_stable_id_mismatch"] += 1
        aligned_entries.append(align_entry(entry, record, packet_sequence))
    if any(comparison[key] for key in comparison if key != "entries"):
        raise ValueError(f"tail structural metadata mismatch: {comparison}")

    aligned = aligned_document(source, aligned_entries, args.catalog)
    aligned["tail_structural_comparison"] = comparison
    output_json = args.output_dir / "translation_001_after_2922_aligned.json"
    output_rpy = args.output_dir / "translation_001_after_2922_aligned.rpy"
    write_json(output_json, aligned)
    output_rpy.write_bytes(args.tail_rpy.read_bytes())

    after = read_json(output_json)
    after_draft_hash = source_payload_hash(after["entries"], "draft_ko")
    after_source_hash = source_payload_hash(after["entries"], "source_jp")
    if before_draft_hash != after_draft_hash or before_source_hash != after_source_hash:
        raise ValueError("tail translation/source payload changed")
    rpy_text = output_rpy.read_text(encoding="utf-8")
    parsed_ids = TRANSLATE_HEADER_RE.findall(rpy_text)
    exact_ids = [entry["translation_id"] for entry in aligned_entries]
    if parsed_ids != exact_ids or len(parsed_ids) != len(set(parsed_ids)):
        raise ValueError("tail RPY translate IDs/order do not match exact aligned JSON")
    if file_info(args.tail_rpy)["sha256"] != file_info(output_rpy)["sha256"]:
        raise ValueError("tail RPY bytes changed")

    manifest_item = {
        "kind": "scenario001_tail_json_and_rpy",
        "input_json": file_info(args.tail_json),
        "input_rpy": file_info(args.tail_rpy),
        "output_json": file_info(output_json),
        "output_rpy": file_info(output_rpy),
        "entries": len(aligned_entries),
        "source_packet_sequence": [
            min(entry["source_packet_sequence"] for entry in aligned_entries),
            max(entry["source_packet_sequence"] for entry in aligned_entries),
        ],
        "catalog_sequence": [
            min(entry["sequence"] for entry in aligned_entries),
            max(entry["sequence"] for entry in aligned_entries),
        ],
        "draft_ko_sha256_before": before_draft_hash,
        "draft_ko_sha256_after": after_draft_hash,
        "source_jp_sha256_before": before_source_hash,
        "source_jp_sha256_after": after_source_hash,
        "structural_comparison": comparison,
        "rpy_bytes_preserved": True,
        "translation_text_modified": False,
    }
    return output_json, output_rpy, manifest_item

def process_bridge(
    args: argparse.Namespace,
    index: dict[tuple[str, int, str], list[dict[str, Any]]],
) -> tuple[Path, dict[str, Any]]:
    """Align the separate sequence-351 bridge without choosing its prose."""
    source = read_json(args.bridge_json)
    original_entries = source["entries"]
    if len(original_entries) != 1:
        raise ValueError(f"expected one bridge entry, got {len(original_entries)}")
    before_draft_hash = source_payload_hash(original_entries, "draft_ko")
    before_source_hash = source_payload_hash(original_entries, "source_jp")
    entry = original_entries[0]
    packet_sequence = int(entry["sequence"])
    record = match_catalog(entry, index)
    aligned_entries = [align_entry(entry, record, packet_sequence)]
    output_path = args.output_dir / "001_sequence351_bridge_aligned.json"
    write_json(output_path, aligned_document(source, aligned_entries, args.catalog))
    reloaded = read_json(output_path)
    after_draft_hash = source_payload_hash(reloaded["entries"], "draft_ko")
    after_source_hash = source_payload_hash(reloaded["entries"], "source_jp")
    if before_draft_hash != after_draft_hash or before_source_hash != after_source_hash:
        raise ValueError("bridge translation/source payload changed")
    manifest_item = {
        "kind": "sequence351_bridge",
        "input": file_info(args.bridge_json),
        "output": file_info(output_path),
        "entries": 1,
        "source_packet_sequence": [packet_sequence, packet_sequence],
        "catalog_sequence": [record["command_index"], record["command_index"]],
        "draft_ko_sha256_before": before_draft_hash,
        "draft_ko_sha256_after": after_draft_hash,
        "source_jp_sha256_before": before_source_hash,
        "source_jp_sha256_after": after_source_hash,
        "translation_text_modified": False,
    }
    return output_path, manifest_item


def process_initial_packets(
    args: argparse.Namespace,
    index: dict[tuple[str, int, str], list[dict[str, Any]]],
) -> tuple[list[Path], list[dict[str, Any]]]:
    """Realign part001-part003 so stale technical IDs cannot reach assembly."""
    source_paths = [args.input_dir / f"001_part{part:03d}.json" for part in range(1, 4)]
    missing = [str(path) for path in source_paths if not path.is_file()]
    if missing:
        raise ValueError(f"missing initial packets: {missing}")
    aligned_paths = []
    manifest_files = []
    packet_sequence = 1
    for source_path in source_paths:
        source = read_json(source_path)
        original_entries = source["entries"]
        before_draft_hash = source_payload_hash(original_entries, "draft_ko")
        before_source_hash = source_payload_hash(original_entries, "source_jp")
        aligned_entries = []
        sequence_start = packet_sequence
        id_mismatches = 0
        for entry in original_entries:
            if int(entry["sequence"]) != packet_sequence:
                raise ValueError(
                    f"unexpected initial packet sequence in {source_path.name}: expected {packet_sequence}, got {entry.get('sequence')}"
                )
            record = match_catalog(entry, index)
            if entry.get("translation_id") != record["localization"]["translation_id"]:
                id_mismatches += 1
            aligned_entries.append(align_entry(entry, record, packet_sequence))
            packet_sequence += 1
        aligned = aligned_document(source, aligned_entries, args.catalog)
        aligned["existing_translation_id_mismatches_corrected"] = id_mismatches
        output_path = args.output_dir / source_path.name.replace(".json", "_aligned.json")
        write_json(output_path, aligned)
        reloaded = read_json(output_path)
        after_draft_hash = source_payload_hash(reloaded["entries"], "draft_ko")
        after_source_hash = source_payload_hash(reloaded["entries"], "source_jp")
        if before_draft_hash != after_draft_hash or before_source_hash != after_source_hash:
            raise ValueError(f"translation/source payload changed in {output_path.name}")
        manifest_files.append(
            {
                "kind": "initial_packet_realign",
                "input": file_info(source_path),
                "output": file_info(output_path),
                "entries": len(aligned_entries),
                "source_packet_sequence": [sequence_start, packet_sequence - 1],
                "catalog_sequence": [
                    min(entry["sequence"] for entry in aligned_entries),
                    max(entry["sequence"] for entry in aligned_entries),
                ],
                "existing_translation_id_mismatches_corrected": id_mismatches,
                "draft_ko_sha256_before": before_draft_hash,
                "draft_ko_sha256_after": after_draft_hash,
                "source_jp_sha256_before": before_source_hash,
                "source_jp_sha256_after": after_source_hash,
                "translation_text_modified": False,
            }
        )
        aligned_paths.append(output_path)
    return aligned_paths, manifest_files

def process_source_packets(
    args: argparse.Namespace,
    index: dict[tuple[str, int, str], list[dict[str, Any]]],
) -> tuple[list[Path], list[dict[str, Any]]]:
    source_paths = [args.input_dir / f"001_part{part:03d}_source_only.json" for part in range(4, 10)]
    missing = [str(path) for path in source_paths if not path.is_file()]
    if missing:
        raise ValueError(f"missing source-only packets: {missing}")

    aligned_paths: list[Path] = []
    manifest_files: list[dict[str, Any]] = []
    packet_sequence = args.source_packet_start
    for source_path in source_paths:
        source = read_json(source_path)
        original_entries = source["entries"]
        before_draft_hash = source_payload_hash(original_entries, "draft_ko")
        before_source_hash = source_payload_hash(original_entries, "source_jp")
        aligned_entries = []
        sequence_start = packet_sequence
        for entry in original_entries:
            existing_sequence = entry.get("sequence")
            if existing_sequence is not None and int(existing_sequence) != packet_sequence:
                raise ValueError(
                    f"unexpected source packet sequence in {source_path.name}: expected {packet_sequence}, got {existing_sequence}"
                )
            record = match_catalog(entry, index)
            aligned_entries.append(align_entry(entry, record, packet_sequence))
            packet_sequence += 1

        output_path = args.output_dir / source_path.name.replace("_source_only.json", "_aligned.json")
        write_json(output_path, aligned_document(source, aligned_entries, args.catalog))
        reloaded = read_json(output_path)
        after_draft_hash = source_payload_hash(reloaded["entries"], "draft_ko")
        after_source_hash = source_payload_hash(reloaded["entries"], "source_jp")
        if before_draft_hash != after_draft_hash or before_source_hash != after_source_hash:
            raise ValueError(f"translation/source payload changed in {output_path.name}")
        manifest_files.append(
            {
                "kind": "source_only_packet",
                "input": file_info(source_path),
                "output": file_info(output_path),
                "entries": len(aligned_entries),
                "source_packet_sequence": [sequence_start, packet_sequence - 1],
                "catalog_sequence": [
                    min(entry["sequence"] for entry in aligned_entries),
                    max(entry["sequence"] for entry in aligned_entries),
                ],
                "draft_ko_sha256_before": before_draft_hash,
                "draft_ko_sha256_after": after_draft_hash,
                "source_jp_sha256_before": before_source_hash,
                "source_jp_sha256_after": after_source_hash,
                "translation_text_modified": False,
            }
        )
        aligned_paths.append(output_path)
    return aligned_paths, manifest_files


def process_recovery(
    args: argparse.Namespace,
    index: dict[tuple[str, int, str], list[dict[str, Any]]],
) -> tuple[Path, Path, dict[str, Any]]:
    if not args.recovery_json.is_file() or not args.recovery_rpy.is_file():
        raise ValueError("recovery JSON/RPY input missing")
    source = read_json(args.recovery_json)
    original_entries = source["entries"]
    before_draft_hash = source_payload_hash(original_entries, "draft_ko")
    before_source_hash = source_payload_hash(original_entries, "source_jp")
    aligned_entries = []
    comparison = {
        "entries": len(original_entries),
        "existing_translation_id_match": 0,
        "existing_translation_id_mismatch": 0,
        "existing_nonnull_id_corrected_to_menu_key": 0,
        "catalog_sequence_differs_from_packet_sequence": 0,
    }
    for expected_sequence, entry in enumerate(original_entries, 151):
        if int(entry.get("sequence")) != expected_sequence:
            raise ValueError(f"recovery packet sequence mismatch: expected {expected_sequence}, got {entry.get('sequence')}")
        record = match_catalog(entry, index)
        exact_id = record["localization"]["translation_id"]
        if entry.get("translation_id") == exact_id:
            comparison["existing_translation_id_match"] += 1
        else:
            comparison["existing_translation_id_mismatch"] += 1
            if entry.get("translation_id") is not None and exact_id is None:
                comparison["existing_nonnull_id_corrected_to_menu_key"] += 1
        if expected_sequence != record["command_index"]:
            comparison["catalog_sequence_differs_from_packet_sequence"] += 1
        aligned_entries.append(align_entry(entry, record, expected_sequence))

    aligned = aligned_document(source, aligned_entries, args.catalog)
    aligned["recovery_structural_comparison"] = comparison
    output_json = args.output_dir / "draft_001_151_350_aligned.json"
    output_rpy = args.output_dir / "draft_001_151_350_aligned.rpy"
    write_json(output_json, aligned)
    rpy_text, rpy_stats = render_recovery_rpy(aligned_entries)
    output_rpy.write_text(rpy_text, encoding="utf-8")

    after = read_json(output_json)
    after_draft_hash = source_payload_hash(after["entries"], "draft_ko")
    after_source_hash = source_payload_hash(after["entries"], "source_jp")
    if before_draft_hash != after_draft_hash or before_source_hash != after_source_hash:
        raise ValueError("recovery translation/source payload changed")

    manifest_item = {
        "kind": "jp_recovery_json_and_rpy",
        "input_json": file_info(args.recovery_json),
        "input_rpy": file_info(args.recovery_rpy),
        "output_json": file_info(output_json),
        "output_rpy": file_info(output_rpy),
        "entries": len(aligned_entries),
        "source_packet_sequence": [151, 350],
        "catalog_sequence": [
            min(entry["sequence"] for entry in aligned_entries),
            max(entry["sequence"] for entry in aligned_entries),
        ],
        "draft_ko_sha256_before": before_draft_hash,
        "draft_ko_sha256_after": after_draft_hash,
        "source_jp_sha256_before": before_source_hash,
        "source_jp_sha256_after": after_source_hash,
        "structural_comparison": comparison,
        "rendered_rpy": rpy_stats,
        "translation_text_modified": False,
    }
    return output_json, output_rpy, manifest_item


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    catalog = read_jsonl(args.catalog)
    index = build_index(catalog)
    if len({record["stable_id"] for record in catalog}) != len(catalog):
        raise ValueError("duplicate stable IDs in catalog")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    args.coverage_output_dir.mkdir(parents=True, exist_ok=True)

    initial_aligned_paths, initial_manifest_files = process_initial_packets(args, index)
    aligned_paths, manifest_files = process_source_packets(args, index)
    manifest_files = initial_manifest_files + manifest_files
    recovery_json, recovery_rpy, recovery_manifest = process_recovery(args, index)
    bridge_json, bridge_manifest = process_bridge(args, index)
    tail_json, tail_rpy, tail_manifest = process_tail(args, index)
    menus_json, menus_rpy, menus_manifest = process_menus(args, index)
    manifest_files.insert(0, menus_manifest)
    manifest_files.insert(0, tail_manifest)
    manifest_files.insert(0, bridge_manifest)
    manifest_files.insert(0, recovery_manifest)

    manifest = {
        "schema_version": "fatal-twelve-alignment-manifest-v1",
        "created_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "catalog": file_info(args.catalog),
        "join": {
            "keys": ["source_file", "source_line", "speaker"],
            "additional_assertion": "source_jp exact equality",
            "sequence_zip_used": False,
            "English_prose_used": False,
        },
        "allowed_entry_changes": sorted(MUTABLE_ENTRY_FIELDS),
        "allowed_entry_additions": sorted(ADDED_ENTRY_FIELDS),
        "files": manifest_files,
        "total_entries": sum(item["entries"] for item in manifest_files),
        "translation_text_modified": False,
    }
    manifest_path = args.output_dir / "alignment_manifest.json"
    write_json(manifest_path, manifest)

    coverage_paths = initial_aligned_paths + [recovery_json, bridge_json, tail_json, menus_json] + aligned_paths
    translated: dict[str, list[dict[str, Any]]] = {}
    duplicate_drafts: list[dict[str, Any]] = []
    coverage_sources = []
    for path in coverage_paths:
        data = read_json(path)
        matched = 0
        for entry in data["entries"]:
            record = map_existing_translation(entry, index)
            stable_id = record["stable_id"]
            occurrence = {
                "packet": path.name,
                "source_file": entry.get("source_file"),
                "source_line": entry.get("source_line"),
                "source_packet_sequence": entry.get("source_packet_sequence", entry.get("sequence")),
                "draft_status": entry.get("status"),
                "draft_ko_sha256": sha256_text(entry["draft_ko"]),
            }
            if stable_id in translated:
                previous = translated[stable_id]
                duplicate_drafts.append(
                    {
                        "stable_id": stable_id,
                        "catalog_sequence": record["command_index"],
                        "source_file": record["source"]["script"],
                        "source_line": record["source"]["line"],
                        "source_jp_sha256": record["source"]["text_sha256"],
                        "occurrences": previous + [occurrence],
                        "different_draft_values": any(
                            item["draft_ko_sha256"] != occurrence["draft_ko_sha256"] for item in previous
                        ),
                        "resolution": "not_selected; translation review deferred",
                    }
                )
                previous.append(occurrence)
            else:
                translated[stable_id] = [occurrence]
            matched += 1
        coverage_sources.append({"file": file_info(path), "matched_records": matched})

    untranslated = [record for record in catalog if record["stable_id"] not in translated]
    ranges = contiguous_ranges(untranslated)
    duplicate_report = {
        "schema_version": "fatal-twelve-duplicate-draft-sources-v1",
        "definition": "Exact Japanese source identity appears in more than one draft packet; no prose was selected or reviewed.",
        "duplicates": duplicate_drafts,
    }
    write_json(args.coverage_output_dir / "scenario_001_duplicate_draft_sources.json", duplicate_report)
    exact_untranslated = [exact_record(record) for record in untranslated]
    records_report = {
        "schema_version": "fatal-twelve-untranslated-records-v1",
        "catalog": file_info(args.catalog),
        "definition": "No nonempty exact-source draft_ko in aligned part001-part003, aligned recovery 151-350, aligned sequence351 bridge, aligned part004-part009, aligned tail 657-844, or aligned missing-menu packet.",
        "records": exact_untranslated,
    }
    write_json(args.coverage_output_dir / "scenario_001_untranslated_records.json", records_report)
    write_jsonl(args.coverage_output_dir / "scenario_001_untranslated_records.jsonl", exact_untranslated)
    range_report = {
        "schema_version": "fatal-twelve-untranslated-ranges-v1",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "catalog": file_info(args.catalog),
        "coverage_sources": coverage_sources,
        "catalog_records": len(catalog),
        "draft_translated_records": len(translated),
        "duplicate_draft_source_records": len(duplicate_drafts),
        "untranslated_records": len(untranslated),
        "ranges": ranges,
    }
    write_json(args.coverage_output_dir / "scenario_001_untranslated_ranges.json", range_report)
    (args.coverage_output_dir / "scenario_001_untranslated_ranges.md").write_text(
        make_markdown(range_report), encoding="utf-8"
    )

    result = {
        "catalog_records": len(catalog),
        "aligned_files": [str(path) for path in initial_aligned_paths] + [str(recovery_json), str(recovery_rpy), str(bridge_json), str(tail_json), str(tail_rpy), str(menus_json), str(menus_rpy)] + [str(path) for path in aligned_paths],
        "alignment_manifest": str(manifest_path),
        "aligned_entries": manifest["total_entries"],
        "translation_text_modified": False,
        "recovery_structural_comparison": recovery_manifest["structural_comparison"],
        "draft_translated_records": len(translated),
        "duplicate_draft_source_records": len(duplicate_drafts),
        "untranslated_records": len(untranslated),
        "untranslated_ranges": len(ranges),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
