#!/usr/bin/env python3
"""Read-only extractor for Ren'Py RPA-3.0 archives.

The source archive is opened only as ``rb``.  Every extracted payload and the
archive itself are SHA-256 hashed so later work can be tied to an exact game
baseline.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import pickle
import posixpath
import re
import zlib
from pathlib import Path
from typing import BinaryIO


HEADER_RE = re.compile(rb"^RPA-3\.0 ([0-9a-fA-F]{16}) ([0-9a-fA-F]{8})\n$")


class PrimitiveOnlyUnpickler(pickle.Unpickler):
    """Allow primitive pickle opcodes but reject imports/global constructors."""

    def find_class(self, module: str, name: str):  # pragma: no cover - defensive
        raise pickle.UnpicklingError(
            f"RPA index attempted to load forbidden global {module}.{name}"
        )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_index(handle: BinaryIO):
    header = handle.readline()
    match = HEADER_RE.fullmatch(header)
    if not match:
        raise ValueError(f"Unsupported or malformed RPA header: {header!r}")

    index_offset = int(match.group(1), 16)
    key = int(match.group(2), 16)
    handle.seek(index_offset)
    compressed_index = handle.read()
    raw_index = zlib.decompress(compressed_index)
    index = PrimitiveOnlyUnpickler(io.BytesIO(raw_index), encoding="bytes").load()
    if not isinstance(index, dict):
        raise TypeError(f"Expected dict RPA index, got {type(index).__name__}")
    return header.decode("ascii").rstrip("\n"), index_offset, key, index


def normalize_name(value: object) -> str:
    if isinstance(value, bytes):
        value = value.decode("utf-8", "strict")
    if not isinstance(value, str):
        raise TypeError(f"Unexpected RPA path type: {type(value).__name__}")
    return value.replace("\\", "/")


def safe_target(root: Path, archive_name: str) -> Path:
    normalized = posixpath.normpath(archive_name)
    if normalized in ("", ".", "..") or normalized.startswith(("../", "/")):
        raise ValueError(f"Unsafe archive path: {archive_name!r}")
    target = (root / Path(normalized)).resolve()
    resolved_root = root.resolve()
    if os.path.commonpath((str(resolved_root), str(target))) != str(resolved_root):
        raise ValueError(f"Archive path escaped output root: {archive_name!r}")
    return target


def extract_archive(
    archive: Path,
    output_root: Path,
    suffixes: tuple[str, ...],
    exact_names: frozenset[str],
) -> dict:
    archive_hash_before = sha256_file(archive)
    records: list[dict] = []

    with archive.open("rb") as handle:
        header, index_offset, key, raw_index = load_index(handle)
        entries = {normalize_name(k): spans for k, spans in raw_index.items()}

        for name in sorted(entries):
            lowered = name.lower()
            if exact_names and name not in exact_names:
                continue
            if suffixes and not lowered.endswith(suffixes):
                continue

            chunks: list[bytes] = []
            decoded_spans: list[dict] = []
            for raw_span in entries[name]:
                if not isinstance(raw_span, tuple) or len(raw_span) not in (2, 3):
                    raise TypeError(f"Malformed span for {name!r}: {raw_span!r}")
                offset = int(raw_span[0]) ^ key
                length = int(raw_span[1]) ^ key
                prefix = raw_span[2] if len(raw_span) == 3 else b""
                if not isinstance(prefix, bytes):
                    raise TypeError(f"Non-byte prefix for {name!r}")
                handle.seek(offset)
                payload = handle.read(length)
                if len(payload) != length:
                    raise EOFError(
                        f"Short RPA read for {name!r}: wanted {length}, got {len(payload)}"
                    )
                chunks.append(prefix + payload)
                decoded_spans.append(
                    {"offset": offset, "length": length, "prefix_length": len(prefix)}
                )

            data = b"".join(chunks)
            target = safe_target(output_root, name)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            records.append(
                {
                    "archive_path": name,
                    "output_path": str(target),
                    "size": len(data),
                    "sha256": sha256_bytes(data),
                    "spans": decoded_spans,
                }
            )

    archive_hash_after = sha256_file(archive)
    if archive_hash_after != archive_hash_before:
        raise RuntimeError(f"Source archive changed while being read: {archive}")

    return {
        "archive": str(archive.resolve()),
        "archive_size": archive.stat().st_size,
        "archive_sha256": archive_hash_before,
        "header": header,
        "index_offset": index_offset,
        "xor_key_hex": f"{key:08x}",
        "index_entry_count": len(raw_index),
        "extracted_count": len(records),
        "entries": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    parser.add_argument("archives", nargs="+", type=Path)
    parser.add_argument(
        "--suffix",
        action="append",
        default=[],
        help="Extract only names ending in this suffix (case-insensitive; repeatable).",
    )
    parser.add_argument(
        "--name",
        action="append",
        default=[],
        help="Extract only this exact archive path (repeatable).",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Write a JSON provenance manifest (default: OUTPUT/extraction_manifest.json).",
    )
    args = parser.parse_args()

    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    suffixes = tuple(value.lower() for value in args.suffix)
    exact_names = frozenset(value.replace("\\", "/") for value in args.name)

    archive_records = [
        extract_archive(path.resolve(), output, suffixes, exact_names)
        for path in args.archives
    ]
    manifest = {
        "format": "fatal-twelve-rpa-readonly-extraction-v1",
        "source_open_mode": "rb",
        "archives": archive_records,
    }
    manifest_path = (args.manifest or (output / "extraction_manifest.json")).resolve()
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    for record in archive_records:
        print(
            f"{Path(record['archive']).name}: "
            f"{record['extracted_count']} / {record['index_entry_count']} entries, "
            f"sha256={record['archive_sha256']}"
        )
    print(f"manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
