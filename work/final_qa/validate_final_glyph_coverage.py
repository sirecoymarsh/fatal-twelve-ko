#!/usr/bin/env python3
"""Audit final Fatal Twelve Korean targets against the shipped Noto cmap.

This is a read-only, no-game-execution verifier.  It binds itself to a
successful ``run_final_apply.py`` output, reads every corrected scenario/UI
``draft_ko`` target plus all emitted global string targets, removes Ren'Py
markup/interpolation syntax while retaining visible ruby text, and verifies
that both Korean font-contract OTFs map every remaining visible code point to
a real, nonzero glyph ID.

No third-party Python package is required.  The small SFNT parser implements
the Unicode cmap formats used by the shipped Noto CJK fonts (4 and 12), and
the RPA reader uses a restricted unpickler and never writes into the game.
"""

from __future__ import annotations

import argparse
import ast
import collections
import datetime as dt
import hashlib
import io
import json
import os
import pickle
import re
import struct
import sys
import unicodedata
import zlib
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Sequence


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
DEFAULT_OUTPUT_ROOT = HERE / "final_apply_output"
DEFAULT_SYSTEM_RPA = Path(
    r"F:\DOWN\Fatal.Twelve.Incl.DLC\Fatal.Twelve.Incl.DLC\Fatal Twelve\game\system.rpa"
)
DEFAULT_CONTRACT = REPO_ROOT / "work" / "patch_architecture" / "language_contract.json"
DEFAULT_BOOTSTRAP = (
    REPO_ROOT
    / "work"
    / "patch_architecture"
    / "skeleton"
    / "game"
    / "f12_korean_bootstrap.rpy"
)

PIPELINE_SCHEMA = "fatal-twelve-final-text-pipeline-result-v1"
CORRECTED_INDEX_SCHEMA = "fatal-twelve-corrected-master-index-v1"
RENDER_SCHEMA = "fatal-twelve-final-rpy-render-manifest-v1"
REPORT_SCHEMA = "fatal-twelve-final-glyph-coverage-v1"
EXPECTED_MASTERS = 30
EXPECTED_SCENARIO_MASTERS = 29
EXPECTED_RECORDS = 18_916
EXPECTED_SCENARIO_RECORDS = 18_184
EXPECTED_UI_RECORDS = 732
EXPECTED_GLOBAL_STRINGS = 797

RPA_HEADER_RE = re.compile(rb"^RPA-3\.0 ([0-9a-fA-F]+) ([0-9a-fA-F]+)$")
TEXT_TAG_RE = re.compile(r"\{/?[A-Za-z][^{}]*\}")
INTERPOLATION_RE = re.compile(r"(?<!\[)\[[^\[\]\n]+\](?!\])")
PERCENT_MAPPING_RE = re.compile(r"%\([^)]+\)[#0 +\-]*\d*(?:\.\d+)?[A-Za-z%]")
QUOTED_LITERAL_RE = re.compile(r'(?<!\\)"(?:\\.|[^"\\])*"')
BOOTSTRAP_DISPLAY_RE = re.compile(
    r'^\s*(?:label|textbutton)\s+(?P<literal>"(?:\\.|[^"\\])*")\s*:',
    re.MULTILINE,
)


class GlyphAuditError(ValueError):
    """An input contract or binary-structure failure."""


class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module: str, name: str) -> Any:  # pragma: no cover - safety boundary
        raise pickle.UnpicklingError(f"global object forbidden in RPA index: {module}.{name}")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise GlyphAuditError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise GlyphAuditError(f"JSON root must be an object: {path}")
    return value


def write_json_atomic(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    os.replace(temporary, path)


def write_text_atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(text, encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def require_file(path: Path, label: str) -> Path:
    resolved = path.resolve()
    if not resolved.is_file():
        raise GlyphAuditError(f"{label} does not exist: {resolved}")
    return resolved


def require_hash(path: Path, expected: Any, label: str) -> str:
    if not isinstance(expected, str) or not re.fullmatch(r"[0-9a-fA-F]{64}", expected):
        raise GlyphAuditError(f"{label}: invalid expected SHA-256")
    actual = file_sha256(path)
    if actual.lower() != expected.lower():
        raise GlyphAuditError(
            f"{label}: SHA-256 mismatch; expected {expected.lower()}, got {actual}"
        )
    return actual


def resolve_reported_path(value: Any, root: Path, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise GlyphAuditError(f"{label}: missing reported path")
    path = Path(value)
    if not path.is_absolute():
        path = root / path
    return require_file(path, label)


def normalize_rpa_name(value: Any) -> str:
    if isinstance(value, bytes):
        name = value.decode("utf-8", errors="strict")
    elif isinstance(value, str):
        name = value
    else:
        raise GlyphAuditError(f"invalid RPA entry name type: {type(value).__name__}")
    normalized = PurePosixPath(name.replace("\\", "/"))
    if normalized.is_absolute() or ".." in normalized.parts or not normalized.parts:
        raise GlyphAuditError(f"unsafe RPA entry name: {name!r}")
    return str(normalized)


def read_rpa_index(path: Path) -> tuple[dict[str, list[tuple[int, int, bytes]]], dict[str, Any]]:
    archive_size = path.stat().st_size
    with path.open("rb") as handle:
        header_bytes = handle.readline()
        header = header_bytes.rstrip(b"\r\n")
        match = RPA_HEADER_RE.fullmatch(header)
        if not match:
            raise GlyphAuditError(f"unsupported RPA header: {header!r}")
        index_offset = int(match.group(1), 16)
        key = int(match.group(2), 16)
        if not len(header_bytes) <= index_offset < archive_size:
            raise GlyphAuditError("RPA index offset outside archive")
        handle.seek(index_offset)
        compressed_index = handle.read()
    try:
        raw_index = zlib.decompress(compressed_index)
        value = RestrictedUnpickler(io.BytesIO(raw_index), encoding="bytes").load()
    except (zlib.error, pickle.UnpicklingError, EOFError, ValueError) as exc:
        raise GlyphAuditError(f"invalid restricted RPA index: {exc}") from exc
    if not isinstance(value, dict):
        raise GlyphAuditError("RPA index root is not a dictionary")

    entries: dict[str, list[tuple[int, int, bytes]]] = {}
    for raw_name, raw_segments in value.items():
        name = normalize_rpa_name(raw_name)
        if name in entries:
            raise GlyphAuditError(f"duplicate normalized RPA entry: {name}")
        if not isinstance(raw_segments, (list, tuple)):
            raise GlyphAuditError(f"RPA segments are not a sequence: {name}")
        segments: list[tuple[int, int, bytes]] = []
        for raw_segment in raw_segments:
            if not isinstance(raw_segment, (list, tuple)) or len(raw_segment) < 2:
                raise GlyphAuditError(f"invalid RPA segment: {name}")
            offset = int(raw_segment[0]) ^ key
            length = int(raw_segment[1]) ^ key
            prefix = raw_segment[2] if len(raw_segment) > 2 else b""
            if not isinstance(prefix, bytes):
                raise GlyphAuditError(f"non-byte RPA prefix: {name}")
            if offset < len(header_bytes) or length < 0 or offset + length > index_offset:
                raise GlyphAuditError(f"RPA segment outside payload region: {name}")
            segments.append((offset, length, prefix))
        entries[name] = segments
    return entries, {
        "path": str(path),
        "size": archive_size,
        "sha256": file_sha256(path),
        "format": "RPA-3.0",
        "header": header.decode("ascii"),
        "index_offset": index_offset,
        "entry_count": len(entries),
        "compressed_index_sha256": sha256_bytes(compressed_index),
        "raw_index_sha256": sha256_bytes(raw_index),
    }


def read_rpa_entry(path: Path, segments: Sequence[tuple[int, int, bytes]]) -> bytes:
    chunks: list[bytes] = []
    with path.open("rb") as handle:
        for offset, length, prefix in segments:
            handle.seek(offset)
            payload = handle.read(length)
            if len(payload) != length:
                raise GlyphAuditError("short read while extracting RPA entry in memory")
            chunks.append(prefix + payload)
    return b"".join(chunks)


def u16(data: bytes, offset: int, label: str) -> int:
    if offset < 0 or offset + 2 > len(data):
        raise GlyphAuditError(f"{label}: uint16 outside data")
    return struct.unpack_from(">H", data, offset)[0]


def u32(data: bytes, offset: int, label: str) -> int:
    if offset < 0 or offset + 4 > len(data):
        raise GlyphAuditError(f"{label}: uint32 outside data")
    return struct.unpack_from(">I", data, offset)[0]


def sfnt_tables(data: bytes) -> tuple[str, dict[str, tuple[int, int]]]:
    if len(data) < 12:
        raise GlyphAuditError("font is shorter than SFNT header")
    scaler = data[:4]
    if scaler not in (b"OTTO", b"\x00\x01\x00\x00", b"true"):
        raise GlyphAuditError(f"unsupported SFNT scaler type: {scaler!r}")
    num_tables = u16(data, 4, "SFNT numTables")
    if 12 + 16 * num_tables > len(data):
        raise GlyphAuditError("SFNT table directory is truncated")
    tables: dict[str, tuple[int, int]] = {}
    for index in range(num_tables):
        position = 12 + 16 * index
        try:
            tag = data[position : position + 4].decode("ascii")
        except UnicodeDecodeError as exc:
            raise GlyphAuditError("non-ASCII SFNT table tag") from exc
        offset = u32(data, position + 8, f"SFNT {tag} offset")
        length = u32(data, position + 12, f"SFNT {tag} length")
        if offset + length > len(data):
            raise GlyphAuditError(f"SFNT table outside font: {tag}")
        if tag in tables:
            raise GlyphAuditError(f"duplicate SFNT table: {tag}")
        tables[tag] = (offset, length)
    return scaler.decode("latin-1"), tables


def parse_cmap_format4(data: bytes, offset: int) -> tuple[dict[int, int], int]:
    length = u16(data, offset + 2, "cmap format 4 length")
    end = offset + length
    if length < 16 or end > len(data):
        raise GlyphAuditError("cmap format 4 is truncated")
    segment_count_x2 = u16(data, offset + 6, "cmap format 4 segCountX2")
    if not segment_count_x2 or segment_count_x2 % 2:
        raise GlyphAuditError("cmap format 4 invalid segCountX2")
    count = segment_count_x2 // 2
    ends_offset = offset + 14
    reserved_offset = ends_offset + 2 * count
    starts_offset = reserved_offset + 2
    deltas_offset = starts_offset + 2 * count
    ranges_offset = deltas_offset + 2 * count
    if ranges_offset + 2 * count > end:
        raise GlyphAuditError("cmap format 4 arrays are truncated")
    if u16(data, reserved_offset, "cmap format 4 reservedPad") != 0:
        raise GlyphAuditError("cmap format 4 reservedPad is nonzero")

    mapping: dict[int, int] = {}
    previous_end = -1
    for index in range(count):
        start = u16(data, starts_offset + 2 * index, "cmap format 4 startCode")
        stop = u16(data, ends_offset + 2 * index, "cmap format 4 endCode")
        delta = u16(data, deltas_offset + 2 * index, "cmap format 4 idDelta")
        range_offset = u16(data, ranges_offset + 2 * index, "cmap format 4 idRangeOffset")
        if start > stop or stop < previous_end:
            raise GlyphAuditError("cmap format 4 segments are invalid or unsorted")
        previous_end = stop
        for codepoint in range(start, stop + 1):
            if codepoint == 0xFFFF:
                continue
            if range_offset == 0:
                glyph_id = (codepoint + delta) & 0xFFFF
            else:
                word_position = ranges_offset + 2 * index
                glyph_position = word_position + range_offset + 2 * (codepoint - start)
                if glyph_position + 2 > end:
                    raise GlyphAuditError("cmap format 4 glyphIdArray address outside subtable")
                glyph_id = u16(data, glyph_position, "cmap format 4 glyphIdArray")
                if glyph_id:
                    glyph_id = (glyph_id + delta) & 0xFFFF
            if glyph_id:
                mapping[codepoint] = glyph_id
    return mapping, length


def parse_cmap_format12(data: bytes, offset: int) -> tuple[dict[int, int], int]:
    length = u32(data, offset + 4, "cmap format 12 length")
    end = offset + length
    if length < 16 or end > len(data):
        raise GlyphAuditError("cmap format 12 is truncated")
    groups = u32(data, offset + 12, "cmap format 12 nGroups")
    if 16 + 12 * groups > length:
        raise GlyphAuditError("cmap format 12 groups are truncated")
    mapping: dict[int, int] = {}
    previous_end = -1
    for index in range(groups):
        position = offset + 16 + 12 * index
        start = u32(data, position, "cmap format 12 startCharCode")
        stop = u32(data, position + 4, "cmap format 12 endCharCode")
        start_gid = u32(data, position + 8, "cmap format 12 startGlyphID")
        if start > stop or stop > 0x10FFFF or start <= previous_end:
            raise GlyphAuditError("cmap format 12 groups are invalid or unsorted")
        previous_end = stop
        for codepoint in range(start, stop + 1):
            glyph_id = start_gid + (codepoint - start)
            if glyph_id:
                mapping[codepoint] = glyph_id
    return mapping, length


def parse_unicode_cmap(data: bytes, tables: dict[str, tuple[int, int]]) -> tuple[dict[int, int], dict[str, Any]]:
    if "cmap" not in tables:
        raise GlyphAuditError("font has no cmap table")
    cmap_offset, cmap_length = tables["cmap"]
    cmap = data[cmap_offset : cmap_offset + cmap_length]
    if len(cmap) < 4 or u16(cmap, 0, "cmap version") != 0:
        raise GlyphAuditError("invalid cmap table header")
    record_count = u16(cmap, 2, "cmap numTables")
    if 4 + 8 * record_count > len(cmap):
        raise GlyphAuditError("cmap encoding records are truncated")

    mapping: dict[int, int] = {}
    conflicts: list[dict[str, int]] = []
    records: list[dict[str, Any]] = []
    parsed_cache: dict[int, tuple[dict[int, int], int, int]] = {}
    for index in range(record_count):
        position = 4 + 8 * index
        platform = u16(cmap, position, "cmap platformID")
        encoding = u16(cmap, position + 2, "cmap encodingID")
        subtable_offset = u32(cmap, position + 4, "cmap subtable offset")
        if subtable_offset + 2 > len(cmap):
            raise GlyphAuditError("cmap subtable offset outside cmap")
        format_number = u16(cmap, subtable_offset, "cmap subtable format")
        is_unicode = platform == 0 or (platform == 3 and encoding in (1, 10))
        record: dict[str, Any] = {
            "index": index,
            "platform_id": platform,
            "encoding_id": encoding,
            "format": format_number,
            "subtable_offset": subtable_offset,
            "unicode_record": is_unicode,
        }
        if is_unicode and format_number in (4, 12):
            if subtable_offset not in parsed_cache:
                if format_number == 4:
                    submap, length = parse_cmap_format4(cmap, subtable_offset)
                else:
                    submap, length = parse_cmap_format12(cmap, subtable_offset)
                parsed_cache[subtable_offset] = (submap, length, format_number)
            submap, length, cached_format = parsed_cache[subtable_offset]
            if cached_format != format_number:
                raise GlyphAuditError("cmap cache format mismatch")
            record.update({"parsed": True, "length": length, "mapped_codepoints": len(submap)})
            for codepoint, glyph_id in submap.items():
                previous = mapping.get(codepoint)
                if previous is None:
                    mapping[codepoint] = glyph_id
                elif previous != glyph_id:
                    if len(conflicts) < 100:
                        conflicts.append(
                            {"codepoint": codepoint, "first_glyph_id": previous, "other_glyph_id": glyph_id}
                        )
        else:
            record["parsed"] = False
        records.append(record)
    if not parsed_cache:
        raise GlyphAuditError("font has no Unicode cmap format 4/12 subtable")
    return mapping, {
        "encoding_records": records,
        "parsed_unique_subtables": len(parsed_cache),
        "parsed_formats": sorted({item[2] for item in parsed_cache.values()}),
        "mapped_codepoints": len(mapping),
        "cross_subtable_mapping_conflicts": len(conflicts),
        "conflict_examples": conflicts,
    }


def parse_font(data: bytes, entry_name: str) -> dict[str, Any]:
    scaler, tables = sfnt_tables(data)
    if "maxp" not in tables:
        raise GlyphAuditError(f"{entry_name}: font has no maxp table")
    maxp_offset, maxp_length = tables["maxp"]
    if maxp_length < 6:
        raise GlyphAuditError(f"{entry_name}: maxp table is truncated")
    num_glyphs = u16(data, maxp_offset + 4, f"{entry_name} maxp numGlyphs")
    mapping, cmap_info = parse_unicode_cmap(data, tables)
    invalid = [
        {"codepoint": codepoint, "glyph_id": glyph_id}
        for codepoint, glyph_id in mapping.items()
        if glyph_id <= 0 or glyph_id >= num_glyphs
    ]
    if invalid:
        raise GlyphAuditError(
            f"{entry_name}: cmap contains {len(invalid)} glyph IDs outside 1..{num_glyphs - 1}"
        )
    return {
        "entry": entry_name,
        "bytes": len(data),
        "sha256": sha256_bytes(data),
        "sfnt_scaler_type": scaler,
        "sfnt_table_count": len(tables),
        "sfnt_tables": sorted(tables),
        "num_glyphs": num_glyphs,
        "cmap": cmap_info,
        "_mapping": mapping,
    }


def strip_nonvisible_syntax(text: str) -> str:
    # Removing tags only (not their contents) retains both {rb}base{/rb} and
    # {rt}reading{/rt}, which are independently drawn by Ren'Py.
    value = TEXT_TAG_RE.sub("", text)
    value = INTERPOLATION_RE.sub("", value)
    value = PERCENT_MAPPING_RE.sub("", value)
    return value


def is_visible_codepoint(char: str) -> bool:
    if char in "\t\r\n" or char == " ":
        return False
    category = unicodedata.category(char)
    return category not in {"Cc", "Cf", "Cs", "Co", "Cn"}


def character_class(codepoint: int) -> str:
    if 0xAC00 <= codepoint <= 0xD7A3:
        return "hangul_syllable"
    if 0x1100 <= codepoint <= 0x11FF or 0xA960 <= codepoint <= 0xA97F or 0xD7B0 <= codepoint <= 0xD7FF:
        return "hangul_jamo"
    if 0x3130 <= codepoint <= 0x318F:
        return "hangul_compatibility_jamo"
    if (
        0x3400 <= codepoint <= 0x4DBF
        or 0x4E00 <= codepoint <= 0x9FFF
        or 0xF900 <= codepoint <= 0xFAFF
        or 0x20000 <= codepoint <= 0x3134F
    ):
        return "cjk_ideograph"
    category = unicodedata.category(chr(codepoint))
    if category.startswith("L"):
        return "letter_other"
    if category.startswith("N"):
        return "number"
    if category.startswith("P"):
        return "punctuation"
    if category.startswith("S"):
        return "symbol"
    if category.startswith("M"):
        return "mark"
    if category.startswith("Z"):
        return "separator"
    return "other"


def parse_new_targets(path: Path) -> list[str]:
    targets: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines(), 1):
        stripped = line.strip()
        if not stripped.startswith("new "):
            continue
        try:
            value = ast.literal_eval(stripped[4:])
        except (SyntaxError, ValueError) as exc:
            raise GlyphAuditError(f"{path}:{line_number}: invalid new string literal") from exc
        if not isinstance(value, str):
            raise GlyphAuditError(f"{path}:{line_number}: new target is not a string")
        targets.append(value)
    return targets


def parse_bootstrap_visible_literals(path: Path) -> list[str]:
    values: list[str] = []
    text = path.read_text(encoding="utf-8-sig")
    for match in BOOTSTRAP_DISPLAY_RE.finditer(text):
        try:
            value = ast.literal_eval(match.group("literal"))
        except (SyntaxError, ValueError):
            continue
        if isinstance(value, str) and value:
            values.append(value)
    return list(dict.fromkeys(values))


def collect_final_targets(output_root: Path, bootstrap: Path) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    pipeline_path = require_file(output_root / "final_text_pipeline_result.json", "final pipeline result")
    pipeline = read_json(pipeline_path)
    if pipeline.get("schema_version") != PIPELINE_SCHEMA or pipeline.get("status") != "PASS":
        raise GlyphAuditError("final text pipeline result is not PASS")
    if pipeline.get("game_executed") is not False or pipeline.get("source_masters_modified") is not False:
        raise GlyphAuditError("final text pipeline violated no-game/source-immutability contract")

    index_ref = pipeline.get("corrected_master_index")
    if not isinstance(index_ref, dict):
        raise GlyphAuditError("pipeline result has no corrected_master_index reference")
    index_path = resolve_reported_path(index_ref.get("path"), output_root, "corrected master index")
    index_sha = require_hash(index_path, index_ref.get("sha256"), "corrected master index")
    index = read_json(index_path)
    if index.get("schema_version") != CORRECTED_INDEX_SCHEMA:
        raise GlyphAuditError("unexpected corrected master index schema")
    refs = index.get("masters")
    if not isinstance(refs, list) or len(refs) != EXPECTED_MASTERS:
        raise GlyphAuditError(f"corrected master index must contain {EXPECTED_MASTERS} masters")

    items: list[dict[str, Any]] = []
    master_inputs: list[dict[str, Any]] = []
    scripts: set[str] = set()
    scenario_records = 0
    ui_records = 0
    scenario_masters = 0
    ui_masters = 0
    for ref in refs:
        if not isinstance(ref, dict):
            raise GlyphAuditError("invalid corrected master reference")
        script = ref.get("script_key")
        if not isinstance(script, str) or script in scripts:
            raise GlyphAuditError("invalid or duplicate corrected master script_key")
        scripts.add(script)
        path = resolve_reported_path(ref.get("path"), output_root, f"corrected master {script}")
        sha = require_hash(path, ref.get("sha256"), f"corrected master {script}")
        document = read_json(path)
        entries = document.get("entries")
        if not isinstance(entries, list):
            raise GlyphAuditError(f"corrected master {script} has no entries")
        is_ui = script == "system_ui" or document.get("schema_version") == "fatal-twelve-system-ui-master-v1"
        if is_ui:
            ui_masters += 1
            ui_records += len(entries)
        else:
            scenario_masters += 1
            scenario_records += len(entries)
        for position, entry in enumerate(entries, 1):
            if not isinstance(entry, dict) or entry.get("sequence") != position:
                raise GlyphAuditError(f"{script}:{position}: invalid entry sequence")
            text = entry.get("draft_ko")
            stable_id = entry.get("stable_id")
            expected_text_sha = entry.get("draft_ko_sha256")
            if not isinstance(text, str) or not isinstance(stable_id, str):
                raise GlyphAuditError(f"{script}:{position}: invalid target identity")
            actual_text_sha = sha256_bytes(text.encode("utf-8"))
            if expected_text_sha != actual_text_sha:
                raise GlyphAuditError(f"{script}:{position}: draft_ko SHA-256 mismatch")
            items.append(
                {
                    "origin": "system_ui_master" if is_ui else "scenario_master",
                    "id": stable_id,
                    "script": script,
                    "sequence": position,
                    "text": text,
                }
            )
        master_inputs.append(
            {
                "script_key": script,
                "kind": "system_ui" if is_ui else "scenario",
                "path": str(path),
                "sha256": sha,
                "records": len(entries),
            }
        )
    if (
        scenario_masters != EXPECTED_SCENARIO_MASTERS
        or ui_masters != 1
        or scenario_records != EXPECTED_SCENARIO_RECORDS
        or ui_records != EXPECTED_UI_RECORDS
        or len(items) != EXPECTED_RECORDS
    ):
        raise GlyphAuditError(
            "corrected corpus exact-count mismatch: "
            + repr(
                {
                    "scenario_masters": scenario_masters,
                    "ui_masters": ui_masters,
                    "scenario_records": scenario_records,
                    "ui_records": ui_records,
                    "records": len(items),
                }
            )
        )

    render_ref = pipeline.get("render_manifest")
    if not isinstance(render_ref, dict):
        raise GlyphAuditError("pipeline result has no render_manifest reference")
    render_path = resolve_reported_path(render_ref.get("path"), output_root, "render manifest")
    render_sha = require_hash(render_path, render_ref.get("sha256"), "render manifest")
    render = read_json(render_path)
    if render.get("schema_version") != RENDER_SCHEMA:
        raise GlyphAuditError("unexpected render manifest schema")
    summary = render.get("summary")
    if not isinstance(summary, dict) or summary.get("total_unique_global_old_keys") != EXPECTED_GLOBAL_STRINGS:
        raise GlyphAuditError("render manifest does not report exactly 797 global strings")
    global_ref = render.get("global_strings")
    if not isinstance(global_ref, dict):
        raise GlyphAuditError("render manifest has no global_strings reference")
    global_path = resolve_reported_path(global_ref.get("path"), output_root, "rendered global strings")
    global_sha = require_hash(global_path, global_ref.get("sha256"), "rendered global strings")
    global_targets = parse_new_targets(global_path)
    if len(global_targets) != EXPECTED_GLOBAL_STRINGS:
        raise GlyphAuditError(
            f"rendered global strings contain {len(global_targets)} new targets, expected {EXPECTED_GLOBAL_STRINGS}"
        )
    for position, text in enumerate(global_targets, 1):
        items.append(
            {
                "origin": "rendered_global_string",
                "id": f"global-string-{position:04d}",
                "script": "global_strings",
                "sequence": position,
                "text": text,
            }
        )

    bootstrap_literals = parse_bootstrap_visible_literals(bootstrap)
    for position, text in enumerate(bootstrap_literals, 1):
        items.append(
            {
                "origin": "korean_slot_bootstrap",
                "id": f"bootstrap-literal-{position:02d}",
                "script": "f12_slot",
                "sequence": position,
                "text": text,
            }
        )

    return items, {
        "pipeline_result": {"path": str(pipeline_path), "sha256": file_sha256(pipeline_path)},
        "corrected_master_index": {"path": str(index_path), "sha256": index_sha},
        "corrected_masters": master_inputs,
        "render_manifest": {"path": str(render_path), "sha256": render_sha},
        "global_strings": {
            "path": str(global_path),
            "sha256": global_sha,
            "targets": len(global_targets),
        },
        "bootstrap": {
            "path": str(bootstrap),
            "sha256": file_sha256(bootstrap),
            "visible_selector_literals": bootstrap_literals,
        },
        "counts": {
            "scenario_masters": scenario_masters,
            "system_ui_masters": ui_masters,
            "masters": scenario_masters + ui_masters,
            "scenario_records": scenario_records,
            "system_ui_records": ui_records,
            "master_records": scenario_records + ui_records,
            "global_string_targets": len(global_targets),
            "bootstrap_visible_selector_literals": len(bootstrap_literals),
            "collected_text_items": len(items),
        },
    }


def inventory_codepoints(items: Sequence[dict[str, Any]]) -> tuple[list[int], dict[str, Any], dict[int, list[dict[str, Any]]]]:
    occurrences: collections.Counter[int] = collections.Counter()
    examples: dict[int, list[dict[str, Any]]] = collections.defaultdict(list)
    ignored: collections.Counter[str] = collections.Counter()
    visible_text_digest = hashlib.sha256()
    unique_target_strings: set[str] = set()
    for item in items:
        text = item["text"]
        unique_target_strings.add(text)
        visible = strip_nonvisible_syntax(text)
        visible_text_digest.update(
            json.dumps(
                [item["origin"], item["id"], visible], ensure_ascii=False, separators=(",", ":")
            ).encode("utf-8")
            + b"\n"
        )
        for character in visible:
            if not is_visible_codepoint(character):
                if character == " ":
                    ignored["ascii_space"] += 1
                elif character in "\t\r\n":
                    ignored["line_or_tab_control"] += 1
                else:
                    ignored[f"unicode_category_{unicodedata.category(character)}"] += 1
                continue
            codepoint = ord(character)
            occurrences[codepoint] += 1
            if len(examples[codepoint]) < 3:
                examples[codepoint].append(
                    {
                        "origin": item["origin"],
                        "script": item["script"],
                        "sequence": item["sequence"],
                        "id": item["id"],
                    }
                )

    codepoints = sorted(occurrences)
    class_unique: collections.Counter[str] = collections.Counter()
    class_occurrences: collections.Counter[str] = collections.Counter()
    inventory: list[dict[str, Any]] = []
    for codepoint in codepoints:
        cls = character_class(codepoint)
        class_unique[cls] += 1
        class_occurrences[cls] += occurrences[codepoint]
        character = chr(codepoint)
        inventory.append(
            {
                "codepoint": codepoint,
                "hex": f"U+{codepoint:04X}",
                "character": character,
                "unicode_name": unicodedata.name(character, "<unnamed>"),
                "unicode_category": unicodedata.category(character),
                "class": cls,
                "occurrences": occurrences[codepoint],
            }
        )
    return codepoints, {
        "unique_target_strings": len(unique_target_strings),
        "required_unique_codepoints": len(codepoints),
        "visible_codepoint_occurrences": sum(occurrences.values()),
        "visible_corpus_sha256": visible_text_digest.hexdigest(),
        "syntax_stripping": {
            "renpy_text_tags_removed_but_contents_retained": True,
            "ruby_base_and_rt_contents_retained": True,
            "square_bracket_interpolations_removed": True,
            "percent_mapping_interpolations_removed": True,
            "ascii_space_and_control_whitespace_excluded": True,
        },
        "ignored_nonvisible_occurrences": dict(sorted(ignored.items())),
        "class_unique_codepoints": dict(sorted(class_unique.items())),
        "class_occurrences": dict(sorted(class_occurrences.items())),
        "visible_codepoint_inventory": inventory,
    }, examples


def load_font_contract(path: Path) -> tuple[dict[str, Any], list[tuple[str, str]]]:
    document = read_json(path)
    font_contract = document.get("font_contract")
    if not isinstance(font_contract, dict) or font_contract.get("reuse_shipped_fonts") is not True:
        raise GlyphAuditError("language contract does not require shipped font reuse")
    body = font_contract.get("korean_body_font")
    emphasis = font_contract.get("korean_emphasis_font")
    if not isinstance(body, str) or not isinstance(emphasis, str):
        raise GlyphAuditError("language contract lacks Korean body/emphasis font paths")
    baseline = document.get("baseline", {}).get("sha256", {}).get("game/system.rpa")
    if not isinstance(baseline, str):
        raise GlyphAuditError("language contract lacks baseline system.rpa SHA-256")
    return document, [("body", body), ("emphasis", emphasis)]


def build_markdown(report: dict[str, Any], json_path: Path, json_sha: str) -> str:
    corpus = report["corpus"]
    coverage = report["coverage"]
    lines = [
        "# Fatal Twelve Korean glyph coverage",
        "",
        f"- Verdict: **{report['verdict']}**",
        f"- Missing font/codepoint pairs: **{coverage['missing_font_codepoint_pairs']}**",
        f"- Missing unique code points: **{coverage['missing_unique_codepoints']}**",
        f"- Required visible code points: **{corpus['required_unique_codepoints']}**",
        f"- Corrected master records: **{corpus['source_counts']['master_records']}**",
        f"- Rendered global string targets: **{corpus['source_counts']['global_string_targets']}**",
        f"- Game executed: **{str(report['game_executed']).lower()}**",
        "",
        "## Shipped font results",
        "",
        "| Role | Archive entry | Glyphs | Required | Missing | cmap formats |",
        "|---|---|---:|---:|---:|---|",
    ]
    for font in report["fonts"]:
        formats = ", ".join(str(value) for value in font["cmap"]["parsed_formats"])
        lines.append(
            f"| {font['role']} | `{font['entry']}` | {font['num_glyphs']} | "
            f"{font['coverage']['required_codepoints']} | {font['coverage']['missing_codepoints']} | {formats} |"
        )
    lines += [
        "",
        "The audit read the font bytes directly from the shipped `system.rpa`,",
        "accepted only Unicode cmap format 4/12 mappings whose glyph ID is in",
        "`1..numGlyphs-1`, retained both Ren'Py ruby base and ruby reading text,",
        "and did not start the game.",
        "",
        f"- JSON report: `{json_path}`",
        f"- JSON SHA-256: `{json_sha}`",
        "",
    ]
    return "\n".join(lines)


def audit(args: argparse.Namespace) -> tuple[dict[str, Any], Path, Path]:
    output_root = args.final_apply_output.resolve()
    if not output_root.is_dir():
        raise GlyphAuditError(f"final apply output does not exist: {output_root}")
    contract_path = require_file(args.language_contract, "language contract")
    bootstrap_path = require_file(args.bootstrap, "Korean slot bootstrap")
    system_rpa = require_file(args.system_rpa, "shipped system.rpa")
    contract, role_entries = load_font_contract(contract_path)
    if args.font_entry:
        role_entries = [(f"override_{index}", value) for index, value in enumerate(args.font_entry, 1)]
    expected_archive_sha = str(contract["baseline"]["sha256"]["game/system.rpa"]).lower()

    items, target_inputs = collect_final_targets(output_root, bootstrap_path)
    codepoints, corpus_details, examples = inventory_codepoints(items)
    if not codepoints:
        raise GlyphAuditError("final target corpus contains no visible code points")

    rpa_entries, archive_info = read_rpa_index(system_rpa)
    if archive_info["sha256"].lower() != expected_archive_sha:
        raise GlyphAuditError(
            "shipped system.rpa does not match language-contract baseline: "
            f"expected {expected_archive_sha}, got {archive_info['sha256']}"
        )

    font_results: list[dict[str, Any]] = []
    missing_union: set[int] = set()
    missing_pairs = 0
    for role, entry_name in role_entries:
        normalized = normalize_rpa_name(entry_name)
        if normalized not in rpa_entries:
            raise GlyphAuditError(f"font-contract entry missing from system.rpa: {normalized}")
        data = read_rpa_entry(system_rpa, rpa_entries[normalized])
        parsed = parse_font(data, normalized)
        mapping = parsed.pop("_mapping")
        missing = [codepoint for codepoint in codepoints if mapping.get(codepoint, 0) == 0]
        missing_pairs += len(missing)
        missing_union.update(missing)
        parsed["role"] = role
        parsed["archive_segments"] = [
            {"offset": offset, "length": length, "prefix_bytes": len(prefix)}
            for offset, length, prefix in rpa_entries[normalized]
        ]
        parsed["coverage"] = {
            "required_codepoints": len(codepoints),
            "mapped_to_nonzero_in_range_glyph_id": len(codepoints) - len(missing),
            "missing_codepoints": len(missing),
            "pass": not missing,
            "missing": [
                {
                    "codepoint": codepoint,
                    "hex": f"U+{codepoint:04X}",
                    "character": chr(codepoint),
                    "unicode_name": unicodedata.name(chr(codepoint), "<unnamed>"),
                    "class": character_class(codepoint),
                    "examples": examples.get(codepoint, []),
                }
                for codepoint in missing
            ],
        }
        font_results.append(parsed)

    verdict = "PASS" if missing_pairs == 0 else "FAIL"
    report_path = (
        args.report.resolve()
        if args.report is not None
        else output_root / "audit" / "final_glyph_coverage.report.json"
    )
    markdown_path = (
        args.markdown_report.resolve()
        if args.markdown_report is not None
        else report_path.with_suffix(".md")
    )
    report: dict[str, Any] = {
        "schema_version": REPORT_SCHEMA,
        "verdict": verdict,
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "audit_mode": "read-only final target collection plus direct shipped RPA/SFNT cmap inspection",
        "game_executed": False,
        "game_files_modified": False,
        "third_party_font_library_used": False,
        "inputs": {
            "final_apply_output": str(output_root),
            **target_inputs,
            "language_contract": {
                "path": str(contract_path),
                "sha256": file_sha256(contract_path),
                "font_roles": [{"role": role, "entry": entry} for role, entry in role_entries],
            },
            "system_rpa": archive_info,
        },
        "corpus": {
            "source_counts": target_inputs["counts"],
            **corpus_details,
        },
        "font_acceptance_rule": {
            "unicode_cmap_records": "platform 0 or platform 3 encoding 1/10",
            "accepted_cmap_formats": [4, 12],
            "real_glyph_requirement": "code point must map to glyph ID in 1..numGlyphs-1; glyph ID 0 (.notdef) is missing",
            "every_contract_font_must_cover_every_required_codepoint": True,
        },
        "fonts": font_results,
        "coverage": {
            "fonts_checked": len(font_results),
            "required_unique_codepoints": len(codepoints),
            "missing_font_codepoint_pairs": missing_pairs,
            "missing_unique_codepoints": len(missing_union),
            "missing_union": [
                {
                    "codepoint": codepoint,
                    "hex": f"U+{codepoint:04X}",
                    "character": chr(codepoint),
                    "unicode_name": unicodedata.name(chr(codepoint), "<unnamed>"),
                    "examples": examples.get(codepoint, []),
                }
                for codepoint in sorted(missing_union)
            ],
            "every_required_codepoint_has_nonzero_glyph_in_every_font": missing_pairs == 0,
        },
        "pass_conditions": {
            "final_pipeline_status_pass": True,
            "corrected_masters_exact_count": True,
            "rendered_global_strings_exact_count": True,
            "system_rpa_hash_matches_contract": True,
            "font_cmap_structures_valid": True,
            "missing_glyphs_zero": missing_pairs == 0,
        },
    }
    write_json_atomic(report_path, report)
    json_sha = file_sha256(report_path)
    write_text_atomic(markdown_path, build_markdown(report, report_path, json_sha))
    return report, report_path, markdown_path


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--final-apply-output",
        type=Path,
        default=DEFAULT_OUTPUT_ROOT,
        help=f"successful run_final_apply.py output root (default: {DEFAULT_OUTPUT_ROOT})",
    )
    parser.add_argument("--system-rpa", type=Path, default=DEFAULT_SYSTEM_RPA)
    parser.add_argument("--language-contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--bootstrap", type=Path, default=DEFAULT_BOOTSTRAP)
    parser.add_argument(
        "--font-entry",
        action="append",
        help="override font-contract RPA entry; repeat to check several fonts",
    )
    parser.add_argument("--report", type=Path)
    parser.add_argument("--markdown-report", type=Path)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        report, report_path, markdown_path = audit(args)
    except GlyphAuditError as exc:
        print(f"glyph coverage audit failed: {exc}", file=sys.stderr)
        return 2
    result = {
        "verdict": report["verdict"],
        "required_unique_codepoints": report["coverage"]["required_unique_codepoints"],
        "fonts_checked": report["coverage"]["fonts_checked"],
        "missing_font_codepoint_pairs": report["coverage"]["missing_font_codepoint_pairs"],
        "missing_unique_codepoints": report["coverage"]["missing_unique_codepoints"],
        "report": str(report_path),
        "report_sha256": file_sha256(report_path),
        "markdown_report": str(markdown_path),
        "markdown_report_sha256": file_sha256(markdown_path),
        "game_executed": False,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if report["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
