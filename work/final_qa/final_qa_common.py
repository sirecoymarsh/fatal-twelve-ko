#!/usr/bin/env python3
"""Shared structural helpers for Fatal Twelve correction and final rendering."""

from __future__ import annotations

import ast
import collections
import hashlib
import json
import os
import re
import unicodedata
from pathlib import Path
from typing import Any


NUMBER_RE = re.compile(r"(?<![0-9])(?:[0-9]+(?:\.[0-9]+)?)(?![0-9])")
RUNTIME_TAG_RE = re.compile(r"(?<!\{)\{[^{}\r\n]+\}(?!\})")
INTERPOLATION_RE = re.compile(r"(?<!\[)\[[A-Za-z_][^\[\]\r\n]*\](?!\])")
PERCENT_FORMAT_RE = re.compile(r"%(?:\([^)]+\))?[#0 +\-]?[0-9]*(?:\.[0-9]+)?[diouxXeEfFgGcrs%]")
TRANSLATE_HEADER_RE = re.compile(r"(?m)^translate korean ([A-Za-z0-9_]+):$")


def text_sha256(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    os.replace(temporary, path)


def token_validation_findings(entry: dict[str, Any], target: str) -> list[dict[str, Any]]:
    """Return runtime/protected-token mismatches without modifying *target*."""
    protected = entry.get("protected_tokens")
    source_jp = entry.get("source_jp")
    if not isinstance(protected, list):
        return [{"kind": "invalid_protected_tokens", "message": "protected_tokens is not an array"}]
    if not isinstance(source_jp, str):
        return [{"kind": "invalid_source_jp", "message": "source_jp is not a string"}]
    if not isinstance(target, str):
        return [{"kind": "invalid_target", "message": "target is not a string"}]

    findings: list[dict[str, Any]] = []
    hard_tokens: list[dict[str, Any]] = []
    legacy_string_metadata = False
    for position, token in enumerate(protected):
        if isinstance(token, dict):
            if token.get("severity") == "hard":
                hard_tokens.append(token)
            continue
        if not isinstance(token, str) or not token:
            findings.append(
                {
                    "kind": "invalid_protected_token_metadata",
                    "position": position,
                    "expected": token,
                    "actual": None,
                    "message": "protected token must be an object or a nonempty legacy string",
                }
            )
            continue
        legacy_string_metadata = True

        # The system-UI catalog predates the structured token schema and stores
        # a de-duplicated list of token strings. Recover the intended hard-token
        # kind and multiplicity from the authoritative Japanese old key. In
        # particular, full-width Arabic digits are semantic number tokens, so an
        # NFKC-equivalent ASCII spelling remains valid in Korean.
        normalized = unicodedata.normalize("NFKC", token)
        if re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", normalized):
            kind = "number"
            occurrences = collections.Counter(
                NUMBER_RE.findall(unicodedata.normalize("NFKC", source_jp))
            )[normalized]
        elif RUNTIME_TAG_RE.fullmatch(token):
            kind = "renpy_text_tag"
            occurrences = source_jp.count(token)
        elif token in {"\\n", "\\r", "\\t", "\\\\"}:
            kind = "literal_escape"
            decoded = {"\\n": chr(10), "\\r": chr(13), "\\t": chr(9), "\\\\": chr(92)}[token]
            occurrences = source_jp.count(decoded)
        else:
            kind = "legacy_string"
            occurrences = source_jp.count(token)
        if occurrences < 1:
            findings.append(
                {
                    "kind": "legacy_protected_token_not_in_source",
                    "position": position,
                    "token": token,
                    "message": "legacy protected token does not occur in source_jp",
                }
            )
            continue
        hard_tokens.extend(
            {"kind": kind, "value": token, "severity": "hard"}
            for _ in range(occurrences)
        )

    expected_tags = collections.Counter(
        token.get("value") for token in hard_tokens if token.get("kind") == "renpy_text_tag"
    )
    actual_tags = collections.Counter(RUNTIME_TAG_RE.findall(target))
    invalid_tag_values = [value for value in expected_tags if not isinstance(value, str)]
    if invalid_tag_values:
        findings.append(
            {
                "kind": "invalid_renpy_text_tag_metadata",
                "expected": invalid_tag_values,
                "actual": [],
                "message": "non-string Ren'Py tag values in protected metadata",
            }
        )
    elif actual_tags != expected_tags:
        findings.append(
            {
                "kind": "renpy_text_tag_mismatch",
                "expected": dict(expected_tags),
                "actual": dict(actual_tags),
                "message": "Ren'Py text-tag multiset differs from the source hard-token set",
            }
        )

    number_values = [token.get("value") for token in hard_tokens if token.get("kind") == "number"]
    expected_arabic: collections.Counter[str] = collections.Counter()
    expected_roman: collections.Counter[str] = collections.Counter()
    if legacy_string_metadata:
        # Legacy UI metadata is a set, not a multiset. Compare the complete
        # source/target NFKC number multisets so circled and full-width digits
        # are neither omitted nor assigned the wrong multiplicity.
        expected_arabic.update(NUMBER_RE.findall(unicodedata.normalize("NFKC", source_jp)))
    else:
        for value in number_values:
            if not isinstance(value, str):
                findings.append(
                    {
                        "kind": "invalid_number_metadata",
                        "expected": value,
                        "actual": None,
                        "message": "non-string number value in protected metadata",
                    }
                )
                continue
            normalized = unicodedata.normalize("NFKC", value)
            if re.fullmatch(r"[0-9]+(?:\.[0-9]+)?", normalized):
                expected_arabic[normalized] += 1
            else:
                expected_roman[value] += 1
    if expected_arabic:
        actual_arabic = collections.Counter(NUMBER_RE.findall(unicodedata.normalize("NFKC", target)))
        if actual_arabic != expected_arabic:
            findings.append(
                {
                    "kind": "arabic_number_mismatch",
                    "expected": dict(expected_arabic),
                    "actual": dict(actual_arabic),
                    "message": "NFKC-equivalent Arabic-number multiset differs",
                }
            )
    for value, count in expected_roman.items():
        actual = target.count(value)
        if actual != count:
            findings.append(
                {
                    "kind": "roman_numeral_mismatch",
                    "token": value,
                    "expected": count,
                    "actual": actual,
                    "message": "Roman numeral count differs",
                }
            )

    literal_escapes = collections.Counter(
        token.get("value") for token in hard_tokens if token.get("kind") == "literal_escape"
    )
    decoded_escapes = {"\\n": "\n", "\\r": "\r", "\\t": "\t", "\\\\": "\\"}
    for value, count in literal_escapes.items():
        if not isinstance(value, str):
            findings.append(
                {
                    "kind": "invalid_literal_escape_metadata",
                    "expected": value,
                    "actual": None,
                    "message": "non-string literal escape in protected metadata",
                }
            )
            continue
        decoded = decoded_escapes.get(value, value)
        actual = target.count(decoded)
        if actual != count:
            findings.append(
                {
                    "kind": "literal_escape_mismatch",
                    "token": value,
                    "expected": count,
                    "actual": actual,
                    "message": "decoded literal-escape count differs",
                }
            )

    known_kinds = {"renpy_text_tag", "number", "literal_escape"}
    other_tokens = collections.Counter(
        (token.get("kind"), token.get("value"))
        for token in hard_tokens
        if token.get("kind") not in known_kinds
    )
    for (kind, value), count in other_tokens.items():
        if not isinstance(value, str):
            findings.append(
                {
                    "kind": "invalid_unknown_token_metadata",
                    "token_kind": kind,
                    "expected": value,
                    "actual": None,
                    "message": "non-string value in unknown protected-token kind",
                }
            )
            continue
        actual = target.count(value)
        if actual != count:
            findings.append(
                {
                    "kind": "protected_token_mismatch",
                    "token_kind": kind,
                    "token": value,
                    "expected": count,
                    "actual": actual,
                    "message": "protected-token count differs",
                }
            )

    expected_interpolation = collections.Counter(INTERPOLATION_RE.findall(source_jp))
    actual_interpolation = collections.Counter(INTERPOLATION_RE.findall(target))
    if actual_interpolation != expected_interpolation:
        findings.append(
            {
                "kind": "renpy_interpolation_mismatch",
                "expected": dict(expected_interpolation),
                "actual": dict(actual_interpolation),
                "message": "Ren'Py interpolation-token multiset differs from source",
            }
        )

    expected_percent = collections.Counter(PERCENT_FORMAT_RE.findall(source_jp))
    actual_percent = collections.Counter(PERCENT_FORMAT_RE.findall(target))
    if actual_percent != expected_percent:
        findings.append(
            {
                "kind": "percent_format_mismatch",
                "expected": dict(expected_percent),
                "actual": dict(actual_percent),
                "message": "percent-format token multiset differs from source",
            }
        )
    return findings


def replace_statement_text(statement: str, source_jp: str, target_ko: str) -> str:
    """Replace exactly the first decoded string literal and preserve prefix/tail."""
    if not isinstance(statement, str):
        raise ValueError("source_statement_code must be a string")
    start = statement.find('"')
    if start < 0:
        raise ValueError(f"no string literal in statement: {statement!r}")
    escaped = False
    end: int | None = None
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
    try:
        decoded = ast.literal_eval(literal)
    except (SyntaxError, ValueError) as exc:
        raise ValueError(f"cannot decode source literal {literal!r}") from exc
    if decoded != source_jp:
        raise ValueError(f"source literal mismatch: decoded={decoded!r}, expected={source_jp!r}")
    target_literal = json.dumps(target_ko, ensure_ascii=False)
    rendered = statement[:start] + target_literal + statement[end + 1 :]

    rendered_start = rendered.find('"')
    rendered_end: int | None = None
    escaped = False
    for position in range(rendered_start + 1, len(rendered)):
        character = rendered[position]
        if escaped:
            escaped = False
        elif character == "\\":
            escaped = True
        elif character == '"':
            rendered_end = position
            break
    if rendered_end is None or ast.literal_eval(rendered[rendered_start : rendered_end + 1]) != target_ko:
        raise ValueError("rendered target literal did not round trip")
    if rendered[:rendered_start] != statement[:start] or rendered[rendered_end + 1 :] != statement[end + 1 :]:
        raise ValueError("statement prefix or runtime tail changed during replacement")
    return rendered
