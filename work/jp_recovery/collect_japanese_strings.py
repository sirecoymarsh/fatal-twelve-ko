#!/usr/bin/env python3
"""Collect Japanese Unicode string literals from decompiled Fatal Twelve scripts.

Input files must be UTF-8 ``.rpy`` files produced from the extracted copies of
``scenario.rpa`` and ``system.rpa``.  No English translation archive is read.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import io
import json
import re
import tokenize
from collections import Counter, defaultdict
from pathlib import Path


JAPANESE_RANGES = (
    (0x3040, 0x30FF),  # Hiragana and Katakana
    (0x31F0, 0x31FF),  # Katakana phonetic extensions
    (0x3400, 0x4DBF),  # CJK Extension A
    (0x4E00, 0x9FFF),  # CJK unified ideographs
    (0xF900, 0xFAFF),  # CJK compatibility ideographs
    (0xFF66, 0xFF9D),  # Half-width Katakana
)
SAY_LINE_RE = re.compile(
    r"^\s*(?:(?P<speaker>[A-Za-z_]\w*)\s+)?(?P<literal>(?:[rRuUbBfF]*)(?:\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'))(?:\s+.*)?$"
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def has_japanese(text: str) -> bool:
    return any(lo <= ord(char) <= hi for char in text for lo, hi in JAPANESE_RANGES)


def source_archive(relative_path: Path) -> str:
    return "scenario.rpa" if relative_path.parts[0].lower() == "scenario" else "system.rpa"


def decode_literal(token_text: str) -> str | None:
    try:
        value = ast.literal_eval(token_text)
    except (SyntaxError, ValueError):
        return None
    if isinstance(value, str):
        return value
    if isinstance(value, bytes):
        return value.decode("utf-8", "strict")
    return None


def collect_file(path: Path, root: Path) -> tuple[list[dict], dict]:
    raw = path.read_bytes()
    text = raw.decode("utf-8", "strict")
    if "\ufffd" in text:
        raise ValueError(f"Replacement character U+FFFD found in {path}")
    c1_controls = [char for char in text if 0x80 <= ord(char) <= 0x9F]
    if c1_controls:
        raise ValueError(f"C1 control characters found in {path}: {len(c1_controls)}")

    relative = path.relative_to(root)
    archive = source_archive(relative)
    records: list[dict] = []
    token_number = 0
    try:
        tokens = tokenize.generate_tokens(io.StringIO(text).readline)
        for token in tokens:
            if token.type != tokenize.STRING:
                continue
            decoded = decode_literal(token.string)
            if decoded is None or not has_japanese(decoded):
                continue
            token_number += 1
            records.append(
                {
                    "id": f"{archive}::{relative.as_posix()}::{token.start[0]}:{token.start[1]}::{token_number}",
                    "source_archive": archive,
                    "source_file": relative.as_posix(),
                    "line": token.start[0],
                    "column": token.start[1],
                    "text": decoded,
                    "text_utf8_sha256": hashlib.sha256(decoded.encode("utf-8")).hexdigest(),
                }
            )
    except tokenize.TokenError as exc:
        raise ValueError(f"Could not tokenize {path}: {exc}") from exc

    info = {
        "source_archive": archive,
        "source_file": relative.as_posix(),
        "size": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "encoding": "UTF-8 (strict decode passed)",
        "replacement_character_count": 0,
        "c1_control_count": 0,
        "japanese_string_count": len(records),
    }
    return records, info


def collect_say_sample(path: Path, limit: int) -> list[dict]:
    text = path.read_text(encoding="utf-8", errors="strict")
    records: list[dict] = []
    for line_number, source_line in enumerate(text.splitlines(), 1):
        match = SAY_LINE_RE.match(source_line)
        if not match:
            continue
        decoded = decode_literal(match.group("literal"))
        if decoded is None or not has_japanese(decoded):
            continue
        records.append(
            {
                "number": len(records) + 1,
                "line": line_number,
                "speaker": match.group("speaker") or None,
                "text": decoded,
                "text_utf8_hex_prefix": decoded.encode("utf-8").hex()[:48],
            }
        )
        if len(records) == limit:
            return records
    raise ValueError(f"Only found {len(records)} Japanese say statements in {path}")


def write_sample_markdown(path: Path, records: list[dict]) -> None:
    lines = [
        "# scenario/001 첫 30개 일본어 대사·내레이션",
        "",
        "- 원천: `scenario.rpa::scenario/001.rpyc`",
        "- 영어 번역 자료 미사용",
        "- 인코딩: UTF-8",
        "",
        "| 번호 | RPYC 복원 RPY 줄 | 화자 ID | 일본어 원문 |",
        "|---:|---:|---|---|",
    ]
    for record in records:
        speaker = record["speaker"] or "(내레이션)"
        escaped = record["text"].replace("|", "\\|").replace("\n", "<br>")
        lines.append(f"| {record['number']} | {record['line']} | `{speaker}` | {escaped} |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("rpy_root", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--sample-count", type=int, default=30)
    args = parser.parse_args()

    root = args.rpy_root.resolve()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)

    paths = sorted(
        path for path in root.rglob("*.rpy") if path.is_file() and path.suffix == ".rpy"
    )
    all_records: list[dict] = []
    files: list[dict] = []
    for path in paths:
        records, info = collect_file(path, root)
        all_records.extend(records)
        files.append(info)

    catalog_path = output / "japanese_strings.jsonl"
    with catalog_path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in all_records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")

    archive_counts = Counter(record["source_archive"] for record in all_records)
    unique_counts: dict[str, int] = {}
    for archive in ("scenario.rpa", "system.rpa"):
        unique_counts[archive] = len(
            {record["text"] for record in all_records if record["source_archive"] == archive}
        )

    summary = {
        "format": "fatal-twelve-japanese-unicode-catalog-v1",
        "english_translation_data_used": False,
        "input_root": str(root),
        "rpy_file_count": len(paths),
        "japanese_string_count": dict(sorted(archive_counts.items())),
        "unique_japanese_string_count": unique_counts,
        "catalog": {
            "path": str(catalog_path),
            "sha256": sha256_file(catalog_path),
            "encoding": "UTF-8",
        },
        "files": files,
    }

    sample_input = root / "scenario" / "001.rpy"
    sample = collect_say_sample(sample_input, args.sample_count)
    sample_json = output / "scenario_001_first_30.json"
    sample_json.write_text(
        json.dumps(
            {
                "source": "scenario.rpa::scenario/001.rpyc",
                "english_translation_data_used": False,
                "encoding": "UTF-8",
                "entries": sample,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    sample_md = output / "scenario_001_first_30.md"
    write_sample_markdown(sample_md, sample)
    summary["sample"] = {
        "json_path": str(sample_json),
        "json_sha256": sha256_file(sample_json),
        "markdown_path": str(sample_md),
        "markdown_sha256": sha256_file(sample_md),
        "entry_count": len(sample),
    }

    summary_path = output / "unicode_catalog_summary.json"
    summary_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "rpy_files": len(paths),
        "strings": dict(sorted(archive_counts.items())),
        "sample_entries": len(sample),
        "summary": str(summary_path),
    }, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
