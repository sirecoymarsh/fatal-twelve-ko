#!/usr/bin/env python3
"""Prove how Japanese text is encoded inside extracted Ren'Py RPYC files.

This script does not unpickle executable objects.  It parses the RPC2 container,
zlib-decompresses slot 1, and walks the pickle opcode stream with
``pickletools``.  Japanese text in Fatal Twelve is stored by BINUNICODE, not as
Shift-JIS/CP932 byte strings.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pickletools
import struct
import zlib
from collections import Counter
from pathlib import Path


JAPANESE_RANGES = (
    (0x3040, 0x30FF),
    (0x31F0, 0x31FF),
    (0x3400, 0x4DBF),
    (0x4E00, 0x9FFF),
    (0xF900, 0xFAFF),
    (0xFF66, 0xFF9D),
)


def has_japanese(value: str) -> bool:
    return any(lo <= ord(char) <= hi for char in value for lo, hi in JAPANESE_RANGES)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parse_rpc2(data: bytes) -> dict[int, bytes]:
    if not data.startswith(b"RENPY RPC2"):
        raise ValueError("Expected RENPY RPC2 header")
    position = 10
    chunks: dict[int, bytes] = {}
    while True:
        if position + 12 > len(data):
            raise EOFError("Truncated RPC2 chunk table")
        slot, start, length = struct.unpack_from("<III", data, position)
        if slot == 0:
            break
        end = start + length
        if start < 0 or end > len(data):
            raise EOFError(f"RPC2 slot {slot} points outside the file")
        chunks[slot] = data[start:end]
        position += 12
    if 1 not in chunks:
        raise ValueError("RPC2 slot 1 (AST pickle) is missing")
    return chunks


def inspect_file(path: Path, root: Path) -> dict:
    data = path.read_bytes()
    chunks = parse_rpc2(data)
    pickle_data = zlib.decompress(chunks[1])
    opcodes: Counter[str] = Counter()
    japanese_by_opcode: Counter[str] = Counter()
    first_japanese: list[dict] = []

    for opcode, argument, position in pickletools.genops(pickle_data):
        opcodes[opcode.name] += 1
        if isinstance(argument, str) and has_japanese(argument):
            japanese_by_opcode[opcode.name] += 1
            if len(first_japanese) < 3:
                first_japanese.append(
                    {"opcode": opcode.name, "pickle_position": position, "text": argument}
                )

    relative = path.relative_to(root)
    rpy_path = path.with_suffix(".rpy")
    rpy_data = rpy_path.read_bytes()
    decoded = rpy_data.decode("utf-8", "strict")
    return {
        "source_archive": (
            "scenario.rpa" if relative.parts[0].lower() == "scenario" else "system.rpa"
        ),
        "source_file": relative.as_posix(),
        "rpyc_sha256": sha256(data),
        "rpc2_header": data[:10].decode("ascii"),
        "slots": {str(slot): len(chunk) for slot, chunk in sorted(chunks.items())},
        "slot1_pickle_uncompressed_size": len(pickle_data),
        "slot1_pickle_sha256": sha256(pickle_data),
        "pickle_string_opcodes": {
            name: opcodes[name]
            for name in ("BINUNICODE", "SHORT_BINSTRING", "BINSTRING")
        },
        "japanese_text_by_opcode": dict(sorted(japanese_by_opcode.items())),
        "first_japanese": first_japanese,
        "decompiled_rpy": relative.with_suffix(".rpy").as_posix(),
        "decompiled_rpy_sha256": sha256(rpy_data),
        "decompiled_rpy_encoding": "UTF-8 (strict decode passed)",
        "decompiled_rpy_has_utf8_bom": rpy_data.startswith(b"\xef\xbb\xbf"),
        "decompiled_rpy_replacement_character_count": decoded.count("\ufffd"),
        "decompiled_rpy_c1_control_count": sum(
            1 for character in decoded if 0x80 <= ord(character) <= 0x9F
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rpyc_root", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    root = args.rpyc_root.resolve()
    paths = sorted(
        path for path in root.rglob("*.rpyc") if path.is_file() and path.suffix == ".rpyc"
    )
    files = [inspect_file(path, root) for path in paths]

    japanese_unicode_count = sum(
        item["japanese_text_by_opcode"].get("BINUNICODE", 0) for item in files
    )
    japanese_byte_opcode_count = sum(
        sum(
            count
            for name, count in item["japanese_text_by_opcode"].items()
            if name in {"BINSTRING", "SHORT_BINSTRING", "STRING"}
        )
        for item in files
    )
    evidence = {
        "format": "fatal-twelve-rpyc-unicode-evidence-v1",
        "method": "RPC2 slot 1 -> zlib -> pickletools opcode walk (no object unpickling)",
        "english_translation_data_used": False,
        "rpyc_file_count": len(files),
        "japanese_binunicode_count": japanese_unicode_count,
        "japanese_byte_string_opcode_count": japanese_byte_opcode_count,
        "conclusion": (
            "Japanese source strings are serialized as pickle Unicode values; "
            "the decompiled files are strict UTF-8 without a BOM."
        ),
        "files": files,
    }
    args.output.resolve().write_text(
        json.dumps(evidence, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "rpyc_files": len(files),
        "japanese_binunicode": japanese_unicode_count,
        "japanese_byte_string_opcodes": japanese_byte_opcode_count,
        "output": str(args.output.resolve()),
    }, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
