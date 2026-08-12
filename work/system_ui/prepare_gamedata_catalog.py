from __future__ import annotations

import ast
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\work\extracted\system\gamedata.rpy")
OFFICIAL_SLOT = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\work\extracted\tl\tl\english\gamedata.rpy")
CATALOG = HERE / "gamedata.catalog.jsonl"
INDEX = HERE / "gamedata.translation_index.json"
SOURCE_SHA256 = "1aae56972a54511bc3e440431933f47eed4a2a44a4f0e138693ff78548a6d07f"
QA = "deferred_until_full_first_draft"

LITERAL = r'(?:"""(?:(?!"{3})[\s\S]|\\.)*"""|"(?:\\.|[^"\\])*")'
SOURCE_RE = re.compile(r'_\(\s*(?P<literal>' + LITERAL + r')\s*\)')
OLD_RE = re.compile(r'(?m)^[ \t]*old[ \t]+(?P<literal>' + LITERAL + r')')
TOKEN_PATTERNS = {
    "renpy_text_tag": re.compile(r"\{[^{}\r\n]+\}"),
    "interpolation": re.compile(r"\[[^\[\]\r\n]+\]"),
    "printf": re.compile(r"%(?:\([^)]+\))?[#0 +\-]*\d*(?:\.\d+)?[diouxXeEfFgGcrsa%]"),
    "number": re.compile(r"(?:[0-9０-９]+(?:[.,．，][0-9０-９]+)*)|(?:[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]+)"),
}
SECTIONS = [
    (4, 212, "scenes"),
    (213, 259, "locations"),
    (260, 307, "bgm_titles"),
    (308, 313, "card_types"),
    (314, 329, "card_rnumbers"),
    (330, 391, "character_info"),
    (392, 573, "cards"),
    (574, 600, "plot_titles"),
    (601, 628, "plot_labels"),
    (629, 1864, "plots"),
    (1865, 999999, "times"),
]
LANES = {
    "scenes": "scene_title",
    "locations": "location_display",
    "bgm_titles": "bgm_title",
    "card_types": "card_type",
    "card_rnumbers": "card_roman_number",
    "character_info": "character_profile_name",
    "cards": "card_description",
    "plot_titles": "plot_title",
    "plot_labels": "plot_label",
    "plots": "plot_summary",
    "times": "time_label",
    "bgm_titles_legacy": "bgm_title_legacy",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def digest_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def literal_value(match: re.Match[str]) -> str:
    return ast.literal_eval(match.group("literal"))


def section_for_line(line: int) -> str:
    for start, end, name in SECTIONS:
        if start <= line <= end:
            return name
    return "unknown"


def context_key(text: str, match_start: int, line_start: int, section: str) -> tuple[str | None, str | None]:
    before = text[max(0, match_start - 700):match_start]
    line_prefix = text[line_start:match_start]
    role = None
    if section == "locations":
        if re.search(r'"name"\s*:\s*$', line_prefix):
            role = "name"
        elif re.search(r'"tip"\s*:\s*$', line_prefix):
            role = "tip"
    key_matches = list(re.finditer(r'"([^"\r\n]+)"\s*:', before))
    key = key_matches[-1].group(1) if key_matches else None
    if section == "locations" and role:
        entry_matches = list(re.finditer(r'^\s*"([^"]+)"\s*:', before, re.M))
        entry_key = entry_matches[-1].group(1) if entry_matches else key
        return entry_key, role
    if section == "times":
        time_matches = list(re.finditer(r'"([^"]+)"\s*:\s*\{[^{}]*"label"\s*:\s*$', before))
        if time_matches:
            return time_matches[-1].group(1), "label"
    return key, role


def extract_source_occurrences(text: str) -> list[dict]:
    out = []
    for ordinal, match in enumerate(SOURCE_RE.finditer(text), 1):
        value = literal_value(match)
        line_start = text.rfind("\n", 0, match.start()) + 1
        line = text.count("\n", 0, match.start()) + 1
        end_line = text.count("\n", 0, match.end()) + 1
        section = section_for_line(line)
        key, role = context_key(text, match.start(), line_start, section)
        lane = LANES[section]
        if section == "locations":
            lane = "location_name" if role == "name" else "location_tip"
        out.append({
            "occurrence_ordinal": ordinal,
            "line_start": line,
            "line_end": end_line,
            "column": match.start() - line_start,
            "section": section,
            "lane": lane,
            "entry_key": key,
            "field_role": role,
            "text_ja": value,
            "expression_code": match.group(0),
            "expression_sha256": digest_text(match.group(0)),
        })
    return out


def extract_official_old_keys(text: str) -> list[str]:
    # Only old literals are parsed. New prose is neither parsed nor stored.
    values = [literal_value(m) for m in OLD_RE.finditer(text)]
    return list(dict.fromkeys(values))


def protected_tokens(text: str) -> list[dict]:
    tokens = []
    for kind, pattern in TOKEN_PATTERNS.items():
        for m in pattern.finditer(text):
            tokens.append({
                "kind": kind,
                "value": m.group(0),
                "start": m.start(),
                "end": m.end(),
                "severity": "hard",
            })
    return tokens


def main() -> None:
    if sha256(SOURCE) != SOURCE_SHA256:
        raise ValueError("gamedata.rpy source hash changed")
    source_text = SOURCE.read_text(encoding="utf-8")
    occurrences = extract_source_occurrences(source_text)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for occurrence in occurrences:
        grouped[occurrence["text_ja"]].append(occurrence)
    source_unique = list(dict.fromkeys(o["text_ja"] for o in occurrences))

    old_keys = extract_official_old_keys(OFFICIAL_SLOT.read_text(encoding="utf-8"))
    if len(old_keys) != 564 or len(set(old_keys)) != 564:
        raise ValueError(f"official old-key set changed: {len(old_keys)}")
    union_keys = old_keys + [key for key in source_unique if key not in set(old_keys)]
    if len(union_keys) != 569:
        raise ValueError(f"unexpected union count: {len(union_keys)}")

    rows = []
    for index, key in enumerate(union_keys, 1):
        source_occurrences = grouped.get(key, [])
        official = key in set(old_keys)
        if source_occurrences:
            section = source_occurrences[0]["section"]
            lane = source_occurrences[0]["lane"]
            origin = "current-japanese-source"
            if official:
                origin += "+official-old-key"
        else:
            section = "bgm_titles_legacy"
            lane = LANES[section]
            origin = "official-old-key-legacy-membership"
        key_hash = digest_text(key)
        stable_id = f"system.rpa::gamedata.rpy::strings::{index:03d}:{key_hash[:16]}"
        rows.append({
            "schema_version": "fatal-twelve-system-ui-catalog-v1",
            "stable_id": stable_id,
            "command_index": index,
            "source_file": "gamedata.rpy",
            "section": section,
            "lane": lane,
            "source_language": "ja",
            "source_jp": key,
            "source_text_sha256": key_hash,
            "key_origin": origin,
            "official_old_key_present": official,
            "current_source_present": bool(source_occurrences),
            "occurrence_count": len(source_occurrences),
            "occurrences": source_occurrences,
            "protected_tokens": protected_tokens(key),
            "source_authority": "Japanese only" if source_occurrences else "technical old-key membership only",
            "english_reference_used": False,
            "translation": {
                "language": "ko",
                "draft_ko": None,
                "status": "untranslated",
                "qa": QA,
            },
        })

    CATALOG.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
        newline="\n",
    )
    sections = Counter(row["section"] for row in rows)
    lanes = Counter(row["lane"] for row in rows)
    index = {
        "schema_version": "fatal-twelve-system-ui-translation-index-v1",
        "source_file": "gamedata.rpy",
        "source_sha256": SOURCE_SHA256,
        "catalog_path": str(CATALOG),
        "catalog_sha256": sha256(CATALOG),
        "source_occurrence_count": len(occurrences),
        "source_unique_count": len(source_unique),
        "official_old_key_count": len(old_keys),
        "union_key_count": len(union_keys),
        "official_old_only_count": len([k for k in old_keys if k not in set(source_unique)]),
        "current_source_only_count": len([k for k in source_unique if k not in set(old_keys)]),
        "section_counts": dict(sorted(sections.items())),
        "lane_counts": dict(sorted(lanes.items())),
        "section_ranges": {
            section: [
                min(row["command_index"] for row in rows if row["section"] == section),
                max(row["command_index"] for row in rows if row["section"] == section),
            ]
            for section in sections
        },
        "english_reference_usage": "official old-key membership only; new prose not parsed or stored",
        "rows": [
            {
                "command_index": row["command_index"],
                "stable_id": row["stable_id"],
                "section": row["section"],
                "lane": row["lane"],
                "source_jp": row["source_jp"],
                "current_source_present": row["current_source_present"],
                "official_old_key_present": row["official_old_key_present"],
                "protected_tokens": row["protected_tokens"],
            }
            for row in rows
        ],
    }
    INDEX.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({k: v for k, v in index.items() if k != "rows"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
