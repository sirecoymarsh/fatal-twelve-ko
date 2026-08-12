#!/usr/bin/env python3
"""Read/list/extract individual RPA-3.0 entries without modifying the archive."""

from __future__ import annotations

import argparse
import io
import json
import pickle
import re
import zlib
from pathlib import Path, PurePosixPath
from typing import Any, Sequence

from build_catalog import file_info, sha256_bytes


HEADER_RE = re.compile(r"^RPA-3\.0 ([0-9a-fA-F]+) ([0-9a-fA-F]+)$")


class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module: str, name: str) -> Any:  # pragma: no cover - safety boundary
        raise pickle.UnpicklingError(f"global object forbidden in RPA index: {module}.{name}")


def safe_unpickle(data: bytes) -> Any:
    return RestrictedUnpickler(io.BytesIO(data), encoding="bytes").load()


def normalize_name(value: Any) -> str:
    if isinstance(value, bytes):
        name = value.decode("utf-8", errors="strict")
    elif isinstance(value, str):
        name = value
    else:
        raise ValueError(f"invalid RPA entry name type: {type(value).__name__}")
    posix = PurePosixPath(name.replace("\\", "/"))
    if posix.is_absolute() or ".." in posix.parts or not posix.parts:
        raise ValueError(f"unsafe RPA entry name: {name!r}")
    return str(posix)


def read_index(path: Path) -> tuple[dict[str, list[dict[str, Any]]], dict[str, Any]]:
    archive_size = path.stat().st_size
    with path.open("rb") as handle:
        header_bytes = handle.readline()
        header = header_bytes.decode("ascii", errors="strict").rstrip("\r\n")
        match = HEADER_RE.match(header)
        if not match:
            raise ValueError(f"unsupported RPA header: {header!r}")
        index_offset = int(match.group(1), 16)
        key = int(match.group(2), 16)
        if not len(header_bytes) <= index_offset < archive_size:
            raise ValueError("RPA index offset is outside archive")
        handle.seek(index_offset)
        compressed_index = handle.read()
    raw_index = zlib.decompress(compressed_index)
    value = safe_unpickle(raw_index)
    if not isinstance(value, dict):
        raise ValueError("RPA index root is not a dictionary")

    entries: dict[str, list[dict[str, Any]]] = {}
    for raw_name, raw_segments in value.items():
        name = normalize_name(raw_name)
        if name in entries:
            raise ValueError(f"duplicate normalized RPA entry: {name}")
        if not isinstance(raw_segments, (list, tuple)):
            raise ValueError(f"RPA entry segments are not a sequence: {name}")
        segments: list[dict[str, Any]] = []
        for raw_segment in raw_segments:
            if not isinstance(raw_segment, (list, tuple)) or len(raw_segment) < 2:
                raise ValueError(f"invalid RPA segment for {name}")
            offset = int(raw_segment[0]) ^ key
            length = int(raw_segment[1]) ^ key
            prefix = raw_segment[2] if len(raw_segment) > 2 else b""
            if not isinstance(prefix, bytes):
                raise ValueError(f"non-byte RPA prefix for {name}")
            if offset < len(header_bytes) or length < 0 or offset + length > index_offset:
                raise ValueError(f"RPA segment outside payload region: {name}")
            segments.append(
                {
                    "offset": offset,
                    "length": length,
                    "prefix": prefix,
                    "prefix_length": len(prefix),
                }
            )
        entries[name] = segments

    info = {
        **file_info(path),
        "header": header,
        "format": "RPA-3.0",
        "index_offset": index_offset,
        "xor_key_hex": f"{key:08x}",
        "entry_count": len(entries),
        "compressed_index_sha256": sha256_bytes(compressed_index),
        "raw_index_sha256": sha256_bytes(raw_index),
    }
    return entries, info


def read_entry(path: Path, segments: list[dict[str, Any]]) -> bytes:
    chunks: list[bytes] = []
    with path.open("rb") as handle:
        for segment in segments:
            handle.seek(segment["offset"])
            payload = handle.read(segment["length"])
            if len(payload) != segment["length"]:
                raise EOFError("short read while extracting RPA entry")
            chunks.append(segment["prefix"] + payload)
    return b"".join(chunks)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true")
    group.add_argument("--extract", metavar="ENTRY")
    parser.add_argument("--output", type=Path)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    entries, info = read_index(args.archive)
    if args.list:
        listing = {
            "archive": info,
            "entries": {
                name: [
                    {k: v for k, v in segment.items() if k != "prefix"}
                    for segment in segments
                ]
                for name, segments in sorted(entries.items())
            },
        }
        text = json.dumps(listing, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text, encoding="utf-8")
        else:
            print(text, end="")
        return 0

    name = normalize_name(args.extract)
    if name not in entries:
        raise SystemExit(f"entry not found: {name}")
    if args.output is None:
        raise SystemExit("--output is required with --extract")
    payload = read_entry(args.archive, entries[name])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(payload)
    print(
        json.dumps(
            {
                "archive": str(args.archive.resolve()),
                "entry": name,
                "output": str(args.output.resolve()),
                "size": len(payload),
                "sha256": sha256_bytes(payload),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
