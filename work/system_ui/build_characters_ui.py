from __future__ import annotations

import ast
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\work\extracted\system\characters.rpy")
OFFICIAL_SLOT = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\work\extracted\tl\tl\english\characters.rpy")
STYLE = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\style_guide.md")
GLOSSARY = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\glossary_draft.json")
CATALOG = HERE / "characters.catalog.jsonl"
DRAFT = HERE / "characters.draft.json"
RPY = HERE / "characters.ko.rpy"
AUDIT = HERE / "characters.structure_check.json"

SOURCE_SHA256 = "8e1e99a2bcac76e743086a15211cf32d888a621b3c0de0278f598a8bf5e76f37"
STYLE_SHA256 = "b2b87352fdfd9b25af688152b0ce8a7460ffeb88fc06ae6e45f1c5df2ae83891"
GLOSSARY_SHA256 = "d7b49d77fcde5da240cb816890c75f9f15a2e83544db34a6193b8e939906300e"
STATUS = "first_draft_unreviewed"
QA = "deferred_until_full_first_draft"

TRANSLATIONS = {
    "凛火": "린카",
    "Ⅰの少女": "Ⅰ번 소녀",
    "海晴": "미하루",
    "Ⅱの少女": "Ⅱ번 소녀",
    "聞き慣れた声": "익숙한 목소리",
    "直未": "나오미",
    "？？？": "???",
    "聞き慣れた声Ｂ": "익숙한 목소리 B",
    "真央": "마오",
    "聞き慣れた声Ａ": "익숙한 목소리 A",
    "ダイアナ": "다이아나",
    "パルカ": "파르카",
    "アラン": "아란",
    "Ⅻの男性": "Ⅻ번 남성",
    "見知らぬ男性の声": "낯선 남성의 목소리",
    "謎の男性": "수수께끼의 남성",
    "オデット": "오데트",
    "Ⅺの女性": "Ⅺ번 여성",
    "フェデリーコ": "페데리코",
    "Ⅲの男性": "Ⅲ번 남성",
    "ユウ": "유우",
    "少女？": "소녀?",
    "少女": "소녀",
    "Ⅳの少女？": "Ⅳ번 소녀?",
    "Ⅳの少年": "Ⅳ번 소년",
    "少年": "소년",
    "ソーニャ": "소냐",
    "謎の少女": "수수께끼의 소녀",
    "桂子": "게이코",
    "Ⅷの女性": "Ⅷ번 여성",
    "聞き覚えのある声": "낯익은 목소리",
    "スケイル": "스케일",
    "Ⅸの男性": "Ⅸ번 남성",
    "見知らぬ男性": "낯선 남성",
    "茂継": "시게쓰구",
    "チャン": "장",
    "Ⅵの女性": "Ⅵ번 여성",
    "昌鎬": "창호",
    "レテ": "레테",
    "近所の主婦": "이웃 주부",
    "凛火＆海晴": "린카 & 미하루",
    "黒髪の少女": "검은 머리 소녀",
    "聞き覚えのある男性の声": "낯익은 남성의 목소리",
    "屈強な男性": "건장한 남성",
    "スタッフ": "스태프",
    "スケール？": "스케일?",
    "長身の女性": "키 큰 여성",
    "外国人のお兄さん": "외국인 오빠",
    "長身の男性": "키 큰 남성",
    "影のある少女": "그늘진 소녀",
    "明るい少女": "밝은 소녀",
    "謎の女性": "수수께끼의 여성",
    "子供を抱いた女性": "아이를 안은 여성",
    "カメラを提げた男性": "카메라를 멘 남성",
    "おじいさん": "할아버지",
    "観光客の女性": "여성 관광객",
    "家族連れの男性": "가족과 함께 온 남성",
    "レテ（猫）": "레테(고양이)",
    "リンダ": "린다",
    "凛火＆直未": "린카 & 나오미",
    "スケール": "스케일",
}

LITERAL = r'(?:"""(?:(?!"{3})[\s\S]|\\.)*"""|"(?:\\.|[^"\\])*")'
SOURCE_RE = re.compile(r'_\(\s*(?P<literal>' + LITERAL + r')\s*\)')
OLD_RE = re.compile(r'(?m)^[ \t]*old[ \t]+(?P<literal>' + LITERAL + r')')
ROMAN_RE = re.compile(r"[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]+")


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


def extract_source_occurrences(text: str) -> list[dict]:
    lines = text.splitlines()
    out = []
    for ordinal, match in enumerate(SOURCE_RE.finditer(text), 1):
        value = literal_value(match)
        line = text.count("\n", 0, match.start()) + 1
        statement = lines[line - 1]
        var_match = re.match(r"\s*define\s+([A-Za-z_][A-Za-z0-9_]*)\s*=", statement)
        variable = var_match.group(1) if var_match else None
        out.append({
            "occurrence_ordinal": ordinal,
            "line": line,
            "column": match.start() - text.rfind("\n", 0, match.start()) - 1,
            "statement_code": statement,
            "variable": variable,
            "key_path": f"{variable}.name" if variable else None,
            "text_ja": value,
            "expression_code": match.group(0),
        })
    return out


def extract_official_old_keys(text: str) -> list[str]:
    # Only old literals are parsed. New prose is neither parsed nor stored.
    values = [literal_value(m) for m in OLD_RE.finditer(text)]
    return list(dict.fromkeys(values))


def protected_tokens(text: str) -> list[dict]:
    return [
        {"kind": "roman_numeral", "value": m.group(0), "severity": "hard"}
        for m in ROMAN_RE.finditer(text)
    ]


def main() -> None:
    if sha256(SOURCE) != SOURCE_SHA256:
        raise ValueError("characters.rpy source hash changed")
    if sha256(STYLE) != STYLE_SHA256 or sha256(GLOSSARY) != GLOSSARY_SHA256:
        raise ValueError("frozen style/glossary changed")

    source_text = SOURCE.read_text(encoding="utf-8")
    occurrences = extract_source_occurrences(source_text)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for occurrence in occurrences:
        grouped[occurrence["text_ja"]].append(occurrence)

    old_keys = extract_official_old_keys(OFFICIAL_SLOT.read_text(encoding="utf-8"))
    if len(old_keys) != 61 or len(set(old_keys)) != 61:
        raise ValueError(f"official old-key set changed: {len(old_keys)}")
    if set(TRANSLATIONS) != set(old_keys):
        raise ValueError(
            f"translation key mismatch missing={set(old_keys)-set(TRANSLATIONS)} "
            f"extra={set(TRANSLATIONS)-set(old_keys)}"
        )
    source_unique = list(dict.fromkeys(o["text_ja"] for o in occurrences))
    if set(source_unique) - set(old_keys):
        raise ValueError("current source display key absent from official old-key union")

    catalog_rows = []
    draft_entries = []
    for index, source_ja in enumerate(old_keys, 1):
        key_hash = digest_text(source_ja)
        source_occurrences = grouped.get(source_ja, [])
        stable_id = f"system.rpa::characters.rpy::strings::{index:03d}:{key_hash[:16]}"
        origin = "current-japanese-source+official-old-key"
        if not source_occurrences:
            origin = "official-old-key-legacy-membership"
        row = {
            "schema_version": "fatal-twelve-system-ui-catalog-v1",
            "stable_id": stable_id,
            "command_index": index,
            "source_file": "characters.rpy",
            "lane": "character_display_name",
            "source_language": "ja",
            "source_jp": source_ja,
            "source_text_sha256": key_hash,
            "key_origin": origin,
            "official_old_key_present": True,
            "current_source_present": bool(source_occurrences),
            "occurrence_count": len(source_occurrences),
            "occurrences": source_occurrences,
            "protected_tokens": protected_tokens(source_ja),
            "source_authority": "Japanese only",
            "english_reference_used": False,
            "translation": {
                "language": "ko",
                "draft_ko": None,
                "status": "untranslated",
                "qa": QA,
            },
        }
        catalog_rows.append(row)
        draft_entries.append({
            **{k: row[k] for k in (
                "stable_id", "command_index", "source_file", "lane", "source_jp",
                "source_text_sha256", "key_origin", "official_old_key_present",
                "current_source_present", "occurrence_count", "occurrences", "protected_tokens",
            )},
            "draft_ko": TRANSLATIONS[source_ja],
            "source_authority": "Japanese only",
            "english_reference_used": False,
            "external_translation_api_used": False,
            "status": STATUS,
            "qa": QA,
        })

    CATALOG.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in catalog_rows),
        encoding="utf-8",
        newline="\n",
    )
    old_key_index_sha = digest_text(json.dumps(old_keys, ensure_ascii=False, separators=(",", ":")))
    packet = {
        "schema_version": "fatal-twelve-system-ui-draft-v1",
        "packet_id": "system_ui_characters_all_display_keys",
        "source_file": "characters.rpy",
        "source_path": str(SOURCE),
        "source_sha256": SOURCE_SHA256,
        "catalog_path": str(CATALOG),
        "catalog_sha256": sha256(CATALOG),
        "entry_count": len(draft_entries),
        "current_source_occurrence_count": len(occurrences),
        "current_source_unique_count": len(source_unique),
        "official_old_key_count": len(old_keys),
        "technical_legacy_key_count": sum(not e["current_source_present"] for e in draft_entries),
        "official_old_key_index_sha256": old_key_index_sha,
        "source_language": "ja",
        "target_language": "ko",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "translation_validation": "not_performed",
        "structure_validation": "performed",
        "status": STATUS,
        "qa": QA,
        "style_guide": {"path": str(STYLE), "sha256": STYLE_SHA256},
        "glossary": {"path": str(GLOSSARY), "sha256": GLOSSARY_SHA256},
        "entries": draft_entries,
    }
    DRAFT.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    rpy_lines = [
        "# -*- coding: utf-8 -*-",
        "# Fatal Twelve characters.rpy Korean first draft.",
        "# Semantic/style source: Japanese only; official slot old membership only.",
        "# Official slot new prose was not parsed, stored, or used.",
        f"# status: {STATUS}",
        f"# qa: {QA}",
        "",
        "translate korean strings:",
        "",
    ]
    for entry in draft_entries:
        rpy_lines.extend([
            f"    # {entry['stable_id']} | occurrences={entry['occurrence_count']} | origin={entry['key_origin']}",
            "    old " + json.dumps(entry["source_jp"], ensure_ascii=False),
            "    new " + json.dumps(entry["draft_ko"], ensure_ascii=False),
            "",
        ])
    RPY.write_text("\n".join(rpy_lines).rstrip() + "\n", encoding="utf-8", newline="\n")

    actual_pairs = []
    lines = RPY.read_text(encoding="utf-8").splitlines()
    for i, line in enumerate(lines):
        match = re.fullmatch(r"    old (.+)", line)
        if match:
            next_match = re.fullmatch(r"    new (.+)", lines[i + 1])
            if not next_match:
                raise ValueError("old without new")
            actual_pairs.append((ast.literal_eval(match.group(1)), ast.literal_eval(next_match.group(1))))
    expected_pairs = [(e["source_jp"], e["draft_ko"]) for e in draft_entries]

    token_mismatches = []
    for entry in draft_entries:
        expected = Counter(t["value"] for t in entry["protected_tokens"])
        actual = Counter(m.group(0) for m in ROMAN_RE.finditer(entry["draft_ko"]))
        if expected != actual:
            token_mismatches.append(entry["command_index"])

    checks = {
        "source_hash": {"passed": sha256(SOURCE) == SOURCE_SHA256},
        "current_source_extraction": {
            "passed": len(occurrences) == 70 and len(source_unique) == 60,
            "detail": {"occurrences": len(occurrences), "unique": len(source_unique)},
        },
        "official_old_key_coverage": {
            "passed": len(old_keys) == 61 and [p[0] for p in actual_pairs] == old_keys,
            "detail": {"expected": 61, "actual": len(actual_pairs)},
        },
        "all_current_source_keys_covered": {
            "passed": not (set(source_unique) - {p[0] for p in actual_pairs}),
        },
        "draft_flags_and_nonempty": {
            "passed": all(
                e["draft_ko"].strip()
                and e["source_authority"] == "Japanese only"
                and e["english_reference_used"] is False
                and e["external_translation_api_used"] is False
                and e["status"] == STATUS and e["qa"] == QA
                for e in draft_entries
            )
        },
        "protected_tokens": {
            "passed": not token_mismatches,
            "detail": {"mismatch_commands": token_mismatches},
        },
        "rpy_old_new_pairs": {
            "passed": actual_pairs == expected_pairs,
            "detail": {"pairs": len(actual_pairs), "unique_old": len({p[0] for p in actual_pairs})},
        },
        "source_code_preservation": {
            "passed": sha256(SOURCE) == SOURCE_SHA256,
            "detail": "Source is read-only; output is a separate translate-korean strings file.",
        },
    }
    passed = all(item["passed"] for item in checks.values())
    audit = {
        "schema_version": "fatal-twelve-system-ui-structure-check-v1",
        "subject": str(DRAFT),
        "validation_scope": "structure_only",
        "translation_qa_performed": False,
        "translation_qa": QA,
        "passed": passed,
        "summary": {
            "catalog_entries": len(catalog_rows),
            "draft_entries": len(draft_entries),
            "source_occurrences": len(occurrences),
            "source_unique_keys": len(source_unique),
            "official_old_unique_keys": len(old_keys),
            "rpy_strings_entries": len(actual_pairs),
            "technical_legacy_keys": sum(not e["current_source_present"] for e in draft_entries),
        },
        "hashes": {
            "source_sha256": sha256(SOURCE),
            "style_guide_sha256": sha256(STYLE),
            "glossary_sha256": sha256(GLOSSARY),
            "official_old_key_index_sha256": old_key_index_sha,
            "catalog_sha256": sha256(CATALOG),
            "draft_json_sha256": sha256(DRAFT),
            "draft_rpy_sha256": sha256(RPY),
        },
        "checks": checks,
    }
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(audit, ensure_ascii=False, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
