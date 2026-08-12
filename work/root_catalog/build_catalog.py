#!/usr/bin/env python3
"""Build a Japanese-first Ren'Py 6.99 contextual translation catalog.

The optional English translation file is deliberately treated as an index only:
this program reads translation identifiers and the Japanese ``old`` keys in a
``translate ... strings`` block, but never parses or stores ``new`` text.

The parser targets the normalized .rpy emitted by unrpyc for Fatal Twelve.  It
also reproduces Ren'Py 6.99's translation-id digest for Say blocks, including a
preceding ``voice`` statement and duplicate-id suffixes.
"""

from __future__ import annotations

import argparse
import ast
import collections
import datetime as dt
import hashlib
import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator, Sequence


SCHEMA_VERSION = "fatal-twelve-renpy-catalog-v1"

LABEL_RE = re.compile(r"^label\s+([A-Za-z0-9_.]+)\s*:")
CHARACTER_RE = re.compile(
    r"^\s*define\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*Character\s*\((.*)\)\s*$"
)
TRANSLATE_RE = re.compile(
    r"^\s*translate\s+([A-Za-z_][A-Za-z0-9_]*)\s+(\S+)\s*:\s*$"
)

# Prefix + Python-style double quoted literal + suffix.  Commands such as
# ``play se \"x\"`` are rejected later because their first word is not a known
# Character expression.
QUOTED_RE = re.compile(
    r'^(?:(?P<prefix>[A-Za-z_][A-Za-z0-9_]*(?:\s+[A-Za-z_][A-Za-z0-9_]*)*)\s+)?'
    r'(?P<literal>"(?:\\.|[^"\\])*")(?P<suffix>.*)$'
)

VOICE_RE = re.compile(
    r'^voice\s+get_voice_filename\(\s*"(?P<tag>[A-Za-z0-9_]+)"'
    r'(?:\s*,\s*(?P<count>\d+))?\s*\)\s*$'
)

INFO_PATTERNS = {
    "scene_id": re.compile(r'(?:^|\s)set_info_scene\(\s*(?P<value>"(?:\\.|[^"\\])*")\s*\)'),
    "time_id": re.compile(r'(?:^|\s)set_info_time\(\s*(?P<value>None|"(?:\\.|[^"\\])*")\s*\)'),
    "location_id": re.compile(r'(?:^|\s)set_info_location\(\s*(?P<value>"(?:\\.|[^"\\])*")\s*\)'),
    "date": re.compile(r'(?:^|\s)set_info_date\(\s*(?P<value>[^)]*)\)'),
}

TAG_RE = re.compile(r"\{[^{}\r\n]+\}")
INTERPOLATION_RE = re.compile(r"\[[^\[\]\r\n]+\]")
PRINTF_RE = re.compile(
    r"%(?:\([^)]+\))?[#0 +\-]*\d*(?:\.\d+)?[diouxXeEfFgGcrsa%]"
)
NUMBER_RE = re.compile(
    r"(?:[0-9０-９]+(?:[.,．，][0-9０-９]+)*)|"
    r"(?:[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]+)"
)
LITERAL_ESCAPE_RE = re.compile(
    r"\\(?:[abfnrtv\\\"']|x[0-9A-Fa-f]{2}|u[0-9A-Fa-f]{4}|"
    r"U[0-9A-Fa-f]{8}|N\{[^}]+\}|[0-7]{1,3})"
)
JA_RE = re.compile(r"[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")

BUILTIN_SAYERS = {"centered", "extend", "narrator", "nvl"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_text(text: str) -> str:
    return sha256_bytes(text.encode("utf-8"))


def file_info(path: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    return {
        "path": str(path.resolve()),
        "size": len(raw),
        "sha256": sha256_bytes(raw),
    }


def decode_utf8_strict(path: Path) -> tuple[str, dict[str, Any]]:
    raw = path.read_bytes()
    # utf-8-sig makes the input contract tolerant of a BOM without silently
    # accepting a legacy locale encoding.
    text = raw.decode("utf-8-sig", errors="strict")
    if "\ufffd" in text:
        raise ValueError(f"replacement character found in strict UTF-8 source: {path}")
    info = file_info(path)
    info.update(
        {
            "encoding": "utf-8-sig" if raw.startswith(b"\xef\xbb\xbf") else "utf-8",
            "replacement_characters": 0,
            "japanese_codepoints": len(JA_RE.findall(text)),
        }
    )
    return text, info


def literal_value(literal: str) -> str:
    try:
        value = ast.literal_eval(literal)
    except (SyntaxError, ValueError) as exc:
        raise ValueError(f"invalid quoted Ren'Py string: {literal!r}") from exc
    if not isinstance(value, str):
        raise ValueError(f"quoted value is not text: {literal!r}")
    return value


def parse_character_definitions(path: Path | None) -> tuple[dict[str, dict[str, Any]], dict[str, Any] | None]:
    if path is None:
        return {}, None

    text, info = decode_utf8_strict(path)
    result: dict[str, dict[str, Any]] = {}
    for line_no, line in enumerate(text.splitlines(), 1):
        match = CHARACTER_RE.match(line)
        if not match:
            continue
        code, args = match.groups()
        name_match = re.search(
            r"\bname\s*=\s*_\(\s*(\"(?:\\.|[^\"\\])*\")\s*\)", args
        )
        if not name_match:
            name_match = re.search(r"^\s*_\(\s*(\"(?:\\.|[^\"\\])*\")\s*\)", args)
        kind_match = re.search(r"\bkind\s*=\s*([A-Za-z_][A-Za-z0-9_]*)", args)
        voice_match = re.search(r"\bvoice_tag\s*=\s*(\"(?:\\.|[^\"\\])*\")", args)
        result[code] = {
            "code": code,
            "display_name_ja": literal_value(name_match.group(1)) if name_match else None,
            "kind": kind_match.group(1) if kind_match else None,
            "voice_tag": literal_value(voice_match.group(1)) if voice_match else None,
            "definition_file": str(path.resolve()),
            "definition_line": line_no,
        }

    # Resolve inherited names/voice tags conservatively.
    for _ in range(len(result) + 1):
        changed = False
        for entry in result.values():
            parent = result.get(entry.get("kind"))
            if not parent:
                continue
            for key in ("display_name_ja", "voice_tag"):
                if entry.get(key) is None and parent.get(key) is not None:
                    entry[key] = parent[key]
                    changed = True
        if not changed:
            break

    info["character_definitions"] = len(result)
    return result, info


@dataclass
class ReferenceIndex:
    language: str
    translation_ids: list[str] = field(default_factory=list)
    old_strings: list[str] = field(default_factory=list)
    duplicate_ids: list[str] = field(default_factory=list)
    duplicate_old_strings: list[str] = field(default_factory=list)
    input_info: dict[str, Any] | None = None


def parse_reference_index(path: Path | None, language: str = "english") -> ReferenceIndex:
    """Read only identity/missingness data from a Ren'Py translation file.

    Translation block bodies and ``new`` values are intentionally ignored.  The
    returned object therefore cannot be used as a prose reference.
    """

    result = ReferenceIndex(language=language)
    if path is None:
        return result

    text, info = decode_utf8_strict(path)
    result.input_info = info
    inside_strings = False
    id_counts: collections.Counter[str] = collections.Counter()
    old_counts: collections.Counter[str] = collections.Counter()

    for line in text.splitlines():
        header = TRANSLATE_RE.match(line)
        if header:
            block_language, identifier = header.groups()
            inside_strings = block_language == language and identifier == "strings"
            if block_language == language and identifier != "strings":
                result.translation_ids.append(identifier)
                id_counts[identifier] += 1
            continue

        if not inside_strings:
            continue

        stripped = line.strip()
        if not stripped.startswith("old "):
            # This explicitly skips every ``new`` line.
            continue
        literal = stripped[4:].strip()
        value = literal_value(literal)
        result.old_strings.append(value)
        old_counts[value] += 1

    result.duplicate_ids = sorted(k for k, v in id_counts.items() if v > 1)
    result.duplicate_old_strings = sorted(k for k, v in old_counts.items() if v > 1)
    return result


def split_quoted_statement(code: str) -> dict[str, str | None] | None:
    match = QUOTED_RE.match(code)
    if not match:
        return None
    suffix = match.group("suffix").strip()
    return {
        "prefix": match.group("prefix"),
        "literal": match.group("literal"),
        "suffix": suffix,
    }


def is_say_suffix(suffix: str) -> bool:
    if not suffix:
        return True
    return bool(
        re.match(
            r"^(?:nointeract(?:\s+with\s+.+)?|with\s+.+)$",
            suffix,
        )
    )


def is_choice_suffix(suffix: str) -> bool:
    return suffix.endswith(":") and bool(
        re.match(r"^(?:(?:if\s+.+)?:|:)$", suffix)
    )


def protected_tokens(text: str, literal: str) -> list[dict[str, Any]]:
    tokens: list[dict[str, Any]] = []

    def add(kind: str, match: re.Match[str], severity: str = "hard") -> None:
        tokens.append(
            {
                "kind": kind,
                "value": match.group(0),
                "start": match.start(),
                "end": match.end(),
                "severity": severity,
            }
        )

    for match in TAG_RE.finditer(text):
        add("renpy_text_tag", match)
    for match in INTERPOLATION_RE.finditer(text):
        add("interpolation", match)
    for match in PRINTF_RE.finditer(text):
        add("printf", match)
    for match in NUMBER_RE.finditer(text):
        add("number", match)

    # Literal escapes are located in source-code coordinates, not decoded-text
    # coordinates, and are recorded separately to keep that distinction clear.
    for match in LITERAL_ESCAPE_RE.finditer(literal[1:-1]):
        tokens.append(
            {
                "kind": "literal_escape",
                "value": match.group(0),
                "start": match.start() + 1,
                "end": match.end() + 1,
                "severity": "hard",
                "coordinate_space": "source_literal",
            }
        )

    tokens.sort(key=lambda item: (item.get("coordinate_space", "decoded_text"), item["start"], item["end"], item["kind"]))
    return tokens


def hard_token_multiset(tokens: Iterable[dict[str, Any]]) -> dict[str, int]:
    counter: collections.Counter[str] = collections.Counter()
    for token in tokens:
        if token.get("severity") != "hard":
            continue
        # Literal escaping is an encoding detail of the source statement; the
        # decoded Korean target is checked against semantic tokens instead.
        if token.get("kind") == "literal_escape":
            continue
        counter[f"{token['kind']}\u0000{token['value']}"] += 1
    return dict(sorted(counter.items()))


def parse_voice(code: str, line: int) -> dict[str, Any]:
    match = VOICE_RE.match(code)
    if not match:
        return {
            "statement": code,
            "line": line,
            "function": None,
            "tag": None,
            "start_count": None,
            "resolution": {
                "mode": "unparsed",
                "file_prefix": "sounds/voice/",
                "file_suffix": ".ogg",
            },
        }

    tag = match.group("tag")
    count = int(match.group("count")) if match.group("count") else None
    exact = f"sounds/voice/{tag}_{count:05d}.ogg" if count is not None else None
    return {
        "statement": code,
        "line": line,
        "function": "get_voice_filename",
        "tag": tag,
        "start_count": count,
        "resolution": {
            "mode": "explicit_counter" if count is not None else "dynamic_runtime_counter",
            "return_pattern": "{tag}_{counter:05d}",
            "file_prefix": "sounds/voice/",
            "file_suffix": ".ogg",
            "exact_file_when_static": exact,
        },
    }


def parse_info_value(raw: str) -> Any:
    raw = raw.strip()
    if raw == "None":
        return None
    if raw.startswith('"'):
        # set_info_date passes three quoted arguments; keep them as a
        # JSON-friendly list while preserving the usual single-string case.
        try:
            value = ast.literal_eval(raw)
        except (SyntaxError, ValueError) as exc:
            raise ValueError(f"invalid runtime info value: {raw!r}") from exc
        if isinstance(value, str):
            return value
        if isinstance(value, tuple) and all(isinstance(item, str) for item in value):
            return list(value)
        raise ValueError(f"unsupported runtime info value: {raw!r}")
    return raw


def update_runtime_state(code: str, state: dict[str, Any]) -> None:
    for key, pattern in INFO_PATTERNS.items():
        match = pattern.search(code)
        if match:
            state[key] = parse_info_value(match.group("value"))
    if code.startswith("scene "):
        state["scene_statement"] = code


@dataclass
class PendingVoice:
    line: int
    indent: int
    code: str


@dataclass
class MenuScope:
    line: int
    indent: int
    ordinal: int
    label: str | None
    voice: PendingVoice | None = None
    direct_item_ordinal: int = 0


def make_stable_id(script_path: str, translation_id: str | None, menu_key: str | None = None) -> str:
    namespace = f"scenario.rpa::{script_path}"
    if translation_id:
        return f"{namespace}::tid::{translation_id}"
    if menu_key:
        return f"{namespace}::menu::{menu_key}"
    raise ValueError("stable id needs a translation id or menu key")


def compact_context(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "stable_id": record["stable_id"],
        "line": record["source"]["line"],
        "label": record["source"]["label"],
        "lane": record["lane"],
        "speaker_code": record["speaker"]["code"] if record["speaker"] else None,
        "source_text_ja": record["source"]["text_ja"],
    }


def build_records(
    source_text: str,
    *,
    script_path: str,
    characters: dict[str, dict[str, Any]],
    reference: ReferenceIndex,
    context_radius: int = 2,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    lines = source_text.splitlines()
    known_sayers = set(characters) | BUILTIN_SAYERS
    reference_ids = set(reference.translation_ids)
    reference_old = set(reference.old_strings)

    records: list[dict[str, Any]] = []
    used_translation_ids: set[str] = set()
    menu_stack: list[MenuScope] = []
    current_label: str | None = None
    pending_voice: PendingVoice | None = None
    menu_ordinal = 0
    recent_commands: list[dict[str, Any]] = []
    runtime_state: dict[str, Any] = {
        "scene_id": None,
        "time_id": None,
        "location_id": None,
        "date": None,
        "scene_statement": None,
    }
    diagnostics: dict[str, Any] = {
        "non_display_quoted_commands": [],
        "orphan_voice_calls": [],
    }

    def append_record(
        *,
        line_no: int,
        indent: int,
        label: str | None,
        lane: str,
        text_ja: str,
        literal: str,
        statement_code: str,
        speaker_code: str | None,
        speaker_attributes: list[str],
        voice: PendingVoice | None,
        translation_id: str | None,
        digest: str | None,
        group_code: list[str],
        menu_key: str | None,
        english_mode: str,
        english_present: bool,
        menu: MenuScope | None,
    ) -> None:
        tokens = protected_tokens(text_ja, literal)
        speaker = None
        if speaker_code is not None:
            speaker = dict(characters.get(speaker_code, {"code": speaker_code}))
            speaker["code"] = speaker_code
            speaker["attributes"] = speaker_attributes

        stable_id = make_stable_id(script_path, translation_id, menu_key)
        group_blob = "".join(code + "\r\n" for code in group_code)
        record: dict[str, Any] = {
            "schema_version": SCHEMA_VERSION,
            "stable_id": stable_id,
            "command_index": len(records) + 1,
            "lane": lane,
            "visibility": {"verdict": "visible", "exclusion_reason": None},
            "source": {
                "language": "ja",
                "archive": "scenario.rpa",
                "script": script_path,
                "line": line_no,
                "indent": indent,
                "label": label,
                "statement_code": statement_code,
                "group_code": group_code,
                "text_ja": text_ja,
                "text_sha256": sha256_text(text_ja),
                "group_sha256": sha256_text(group_blob),
                "renpy_digest": digest,
            },
            "localization": {
                "translation_id": translation_id,
                "id_origin": "renpy-6.99-recomputed" if translation_id else "renpy-string-key",
                "menu_key": menu_key,
            },
            "alignment": {
                "method": (
                    "renpy-6.99-ast-code-digest"
                    if translation_id
                    else (
                        "renpy-string-old-key-exact-match"
                        if english_present
                        else "source-menu-identity-no-reference"
                    )
                ),
                "confidence": "exact" if english_present else "unmatched-reference",
                "sequence_alignment_used": False,
                "reference_prose_used": False,
                "evidence": {
                    "computed_translation_id": translation_id,
                    "renpy_digest": digest,
                    "source_group_sha256": sha256_text(group_blob),
                    "source_text_sha256": sha256_text(text_ja),
                    "reference_key_present": english_present,
                },
            },
            "speaker": speaker,
            "voice_call": parse_voice(voice.code, voice.line) if voice else None,
            "runtime_context": dict(runtime_state),
            "prelude_commands": recent_commands[-8:],
            "menu_context": (
                {
                    "menu_ordinal": menu.ordinal,
                    "menu_line": menu.line,
                    "direct_item_ordinal": menu.direct_item_ordinal,
                }
                if menu
                else None
            ),
            "protected_tokens": tokens,
            "protected_token_multiset": hard_token_multiset(tokens),
            "layout": {
                "codepoints": len(text_ja),
                "line_breaks": text_ja.count("\n"),
                "contains_ruby": "{rb}" in text_ja or "{rt}" in text_ja,
                "starts_with_corner_quote": text_ja.startswith("「"),
                "ends_with_corner_quote": text_ja.endswith("」"),
            },
            "english_alignment": {
                "mode": english_mode,
                "key_present": english_present,
                "prose_imported": False,
            },
            "context": {"previous": [], "next": []},
            "translation": {
                "language": "ko",
                "text_ko": None,
                "status": "untranslated",
                "provenance": "japanese-source-only",
                "notes": [],
            },
        }
        records.append(record)
        recent_commands.clear()

    for line_no, raw_line in enumerate(lines, 1):
        code = raw_line.strip()
        indent = len(raw_line) - len(raw_line.lstrip(" "))

        if code:
            while menu_stack and indent <= menu_stack[-1].indent and code != "menu:":
                menu_stack.pop()

        label_match = LABEL_RE.match(code)
        if label_match:
            if pending_voice is not None:
                diagnostics["orphan_voice_calls"].append(
                    {"line": pending_voice.line, "statement": pending_voice.code}
                )
                pending_voice = None
            current_label = label_match.group(1)
            recent_commands.append({"line": line_no, "code": code})
            continue

        if not code or code.startswith("#"):
            continue

        update_runtime_state(code, runtime_state)

        if code == "menu:":
            menu_ordinal += 1
            menu_voice = None
            if pending_voice is not None and pending_voice.indent == indent:
                menu_voice = pending_voice
                pending_voice = None
            menu_stack.append(
                MenuScope(
                    line=line_no,
                    indent=indent,
                    ordinal=menu_ordinal,
                    label=current_label,
                    voice=menu_voice,
                )
            )
            recent_commands.append({"line": line_no, "code": code})
            continue

        if code.startswith("voice "):
            if pending_voice is not None:
                diagnostics["orphan_voice_calls"].append(
                    {"line": pending_voice.line, "statement": pending_voice.code}
                )
            pending_voice = PendingVoice(line=line_no, indent=indent, code=code)
            continue

        direct_menu = bool(menu_stack and indent == menu_stack[-1].indent + 4)
        quoted = split_quoted_statement(code)

        if direct_menu and quoted is not None:
            prefix = quoted["prefix"]
            suffix = quoted["suffix"] or ""
            first = prefix.split()[0] if prefix else None
            recognized_prefix = first is None or first in known_sayers
            if recognized_prefix and (is_choice_suffix(suffix) or is_say_suffix(suffix)):
                menu = menu_stack[-1]
                menu.direct_item_ordinal += 1
                text_ja = literal_value(str(quoted["literal"]))
                text_hash = sha256_text(text_ja)[:16]
                if is_choice_suffix(suffix):
                    lane = "spoken_choice" if text_ja.startswith("「") and text_ja.endswith("」") else "narrative_choice"
                    role = "choice"
                    speaker_code = first
                    voice = None
                else:
                    lane = "dialogue_choice_prompt" if first else "choice_prompt"
                    role = "spoken_prompt" if first else "prompt"
                    speaker_code = first
                    voice = menu.voice if first else None
                    menu.voice = None

                menu_key = f"{menu.ordinal:03d}:{role}:{menu.direct_item_ordinal:02d}:{text_hash}"
                append_record(
                    line_no=line_no,
                    indent=indent,
                    label=current_label,
                    lane=lane,
                    text_ja=text_ja,
                    literal=str(quoted["literal"]),
                    statement_code=code,
                    speaker_code=speaker_code,
                    speaker_attributes=(prefix.split()[1:] if prefix else []),
                    voice=voice,
                    translation_id=None,
                    digest=None,
                    group_code=([voice.code] if voice else []) + [code],
                    menu_key=menu_key,
                    english_mode="old_key_presence_only",
                    english_present=text_ja in reference_old,
                    menu=menu,
                )
                continue

        say = None
        if quoted is not None and is_say_suffix(str(quoted["suffix"] or "")):
            prefix = quoted["prefix"]
            first = prefix.split()[0] if prefix else None
            if first is None or first in known_sayers:
                say = quoted

        if say is not None:
            prefix = say["prefix"]
            speaker_code = prefix.split()[0] if prefix else None
            attributes = prefix.split()[1:] if prefix else []
            voice = None
            if pending_voice is not None and pending_voice.indent == indent:
                voice = pending_voice
                pending_voice = None

            group_code = ([voice.code] if voice else []) + [code]
            digest_blob = "".join(item + "\r\n" for item in group_code).encode("utf-8")
            digest = hashlib.md5(digest_blob).hexdigest()[:8]
            base = f"{current_label.replace('.', '_')}_{digest}" if current_label else digest
            translation_id = base
            suffix_index = 0
            while translation_id in used_translation_ids:
                suffix_index += 1
                translation_id = f"{base}_{suffix_index}"
            used_translation_ids.add(translation_id)

            text_ja = literal_value(str(say["literal"]))
            append_record(
                line_no=line_no,
                indent=indent,
                label=current_label,
                lane="dialogue" if speaker_code else "narration",
                text_ja=text_ja,
                literal=str(say["literal"]),
                statement_code=code,
                speaker_code=speaker_code,
                speaker_attributes=attributes,
                voice=voice,
                translation_id=translation_id,
                digest=digest,
                group_code=group_code,
                menu_key=None,
                english_mode="translation_id_only",
                english_present=translation_id in reference_ids,
                menu=None,
            )
            continue

        # Any real node between a voice statement and a Say node flushes the
        # translatable group under Ren'Py's Restructurer.
        if pending_voice is not None:
            diagnostics["orphan_voice_calls"].append(
                {"line": pending_voice.line, "statement": pending_voice.code}
            )
            pending_voice = None

        if '"' in code and quoted is not None:
            diagnostics["non_display_quoted_commands"].append({"line": line_no, "code": code})
        recent_commands.append({"line": line_no, "code": code})

    if pending_voice is not None:
        diagnostics["orphan_voice_calls"].append(
            {"line": pending_voice.line, "statement": pending_voice.code}
        )

    for index, record in enumerate(records):
        before = records[max(0, index - context_radius) : index]
        after = records[index + 1 : index + 1 + context_radius]
        record["context"] = {
            "previous": [compact_context(item) for item in before],
            "next": [compact_context(item) for item in after],
        }

    current_ids = {
        record["localization"]["translation_id"]
        for record in records
        if record["localization"]["translation_id"] is not None
    }
    source_old_keys = {
        record["source"]["text_ja"]
        for record in records
        if record["english_alignment"]["mode"] == "old_key_presence_only"
    }
    diagnostics["reference_orphan_translation_ids"] = sorted(reference_ids - current_ids)
    diagnostics["source_translation_ids_missing_reference"] = sorted(current_ids - reference_ids)
    diagnostics["reference_orphan_old_key_hashes"] = sorted(
        sha256_text(value) for value in reference_old - source_old_keys
    )
    diagnostics["source_old_keys_missing_reference_stable_ids"] = [
        record["stable_id"]
        for record in records
        if record["english_alignment"]["mode"] == "old_key_presence_only"
        and not record["english_alignment"]["key_present"]
    ]
    return records, diagnostics


def write_jsonl(path: Path, records: Sequence[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")))
            handle.write("\n")


def summarize_records(records: Sequence[dict[str, Any]]) -> dict[str, Any]:
    lanes = collections.Counter(record["lane"] for record in records)
    speakers = collections.Counter(
        record["speaker"]["code"] if record["speaker"] else "<narrator>"
        for record in records
    )
    labels = collections.Counter(record["source"]["label"] or "<none>" for record in records)
    token_kinds = collections.Counter(
        token["kind"] for record in records for token in record["protected_tokens"]
    )
    return {
        "records": len(records),
        "lanes": dict(sorted(lanes.items())),
        "voiced_records": sum(record["voice_call"] is not None for record in records),
        "translation_id_records": sum(
            record["localization"]["translation_id"] is not None for record in records
        ),
        "menu_key_records": sum(record["localization"]["menu_key"] is not None for record in records),
        "reference_present": sum(record["english_alignment"]["key_present"] for record in records),
        "reference_missing": sum(not record["english_alignment"]["key_present"] for record in records),
        "speakers": dict(sorted(speakers.items())),
        "labels": dict(sorted(labels.items())),
        "protected_token_kinds": dict(sorted(token_kinds.items())),
        "japanese_codepoints_in_source_text": sum(
            len(JA_RE.findall(record["source"]["text_ja"])) for record in records
        ),
        "untranslated": sum(record["translation"]["status"] == "untranslated" for record in records),
    }


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-rpy", required=True, type=Path)
    parser.add_argument("--script-path", required=True, help="Archive-relative script identity, e.g. scenario/001.rpy")
    parser.add_argument("--characters-rpy", type=Path)
    parser.add_argument("--reference-rpy", type=Path, help="Official English .rpy; identifiers/old keys only")
    parser.add_argument("--reference-language", default="english")
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--meta-output", type=Path)
    parser.add_argument("--context-radius", type=int, default=2)
    parser.add_argument("--source-rpyc", type=Path)
    parser.add_argument("--reference-rpyc", type=Path)
    parser.add_argument("--source-archive", type=Path)
    parser.add_argument("--reference-archive", type=Path)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    if args.context_radius < 0 or args.context_radius > 10:
        raise SystemExit("--context-radius must be between 0 and 10")

    source_text, source_info = decode_utf8_strict(args.source_rpy)
    if not JA_RE.search(source_text):
        raise SystemExit("source does not contain Japanese characters; refusing a Japanese-first catalog")

    characters, characters_info = parse_character_definitions(args.characters_rpy)
    reference = parse_reference_index(args.reference_rpy, args.reference_language)
    records, diagnostics = build_records(
        source_text,
        script_path=args.script_path.replace("\\", "/"),
        characters=characters,
        reference=reference,
        context_radius=args.context_radius,
    )

    write_jsonl(args.output, records)
    meta_path = args.meta_output or args.output.with_suffix(".meta.json")
    metadata: dict[str, Any] = {
        "schema_version": SCHEMA_VERSION,
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "policy": {
            "semantic_source_language": "ja",
            "target_language": "ko",
            "reference_language": args.reference_language if args.reference_rpy else None,
            "reference_usage": "translation identifiers and missingness only",
            "reference_prose_parsed": False,
            "reference_prose_stored": False,
            "live_game_modified": False,
        },
        "inputs": {
            "source_rpy": source_info,
            "characters_rpy": characters_info,
            "reference_rpy_index_only": reference.input_info,
            "source_rpyc": file_info(args.source_rpyc) if args.source_rpyc else None,
            "reference_rpyc": file_info(args.reference_rpyc) if args.reference_rpyc else None,
            "source_archive": file_info(args.source_archive) if args.source_archive else None,
            "reference_archive": file_info(args.reference_archive) if args.reference_archive else None,
        },
        "stable_id": {
            "translation_blocks": "scenario.rpa::<script>::tid::<renpy_translation_id>",
            "menu_strings": "scenario.rpa::<script>::menu::<menu ordinal>:<role>:<direct item ordinal>:<source sha256 prefix>",
            "renpy_id_algorithm": "md5(concat(AST.get_code UTF-8 + CRLF))[:8], prefixed by label with dots replaced by underscores, duplicate suffix _N",
        },
        "reference_index": {
            "translation_ids": len(reference.translation_ids),
            "old_string_keys": len(reference.old_strings),
            "duplicate_translation_ids": reference.duplicate_ids,
            "duplicate_old_strings_sha256": [
                sha256_text(value) for value in reference.duplicate_old_strings
            ],
        },
        "statistics": summarize_records(records),
        "diagnostics": diagnostics,
        "catalog": file_info(args.output),
    }
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({"catalog": str(args.output), "meta": str(meta_path), **metadata["statistics"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
