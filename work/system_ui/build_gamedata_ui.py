from __future__ import annotations

import ast
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\work\extracted\system\gamedata.rpy")
STYLE = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\style_guide.md")
GLOSSARY = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\glossary_draft.json")
CATALOG = HERE / "gamedata.catalog.jsonl"
CHARACTERS_DRAFT = HERE / "characters.draft.json"
DRAFT = HERE / "gamedata.draft.json"
RPY = HERE / "gamedata.ko.rpy"
AUDIT = HERE / "gamedata.structure_check.json"
SEEDS = [
    HERE / "scenes.seed.pydata",
    HERE / "locations.seed.pydata",
    HERE / "misc.seed.pydata",
    HERE / "plots_451_480.seed.pydata",
    HERE / "plots_481_510.seed.pydata",
    HERE / "plots_511_540.seed.pydata",
    HERE / "plots_541_559.seed.pydata",
]

SOURCE_SHA256 = "1aae56972a54511bc3e440431933f47eed4a2a44a4f0e138693ff78548a6d07f"
STYLE_SHA256 = "b2b87352fdfd9b25af688152b0ce8a7460ffeb88fc06ae6e45f1c5df2ae83891"
GLOSSARY_SHA256 = "d7b49d77fcde5da240cb816890c75f9f15a2e83544db34a6193b8e939906300e"
STATUS = "first_draft_unreviewed"
QA = "deferred_until_full_first_draft"
TOKEN_PATTERNS = {
    "renpy_text_tag": re.compile(r"\{[^{}\r\n]+\}"),
    "interpolation": re.compile(r"\[[^\[\]\r\n]+\]"),
    "printf": re.compile(r"%(?:\([^)]+\))?[#0 +\-]*\d*(?:\.\d+)?[diouxXeEfFgGcrsa%]"),
    "number": re.compile(r"(?:[0-9０-９]+(?:[.,．，][0-9０-９]+)*)|(?:[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]+)"),
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def digest_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def token_multiset(text: str) -> Counter[tuple[str, str]]:
    out: Counter[tuple[str, str]] = Counter()
    for kind, pattern in TOKEN_PATTERNS.items():
        out.update((kind, match.group(0)) for match in pattern.finditer(text))
    return out


def load_seeds() -> dict[int, str]:
    merged: dict[int, str] = {}
    for path in SEEDS:
        data = ast.literal_eval(path.read_text(encoding="utf-8-sig"))
        if not isinstance(data, dict):
            raise ValueError(f"seed is not dict: {path}")
        overlap = set(merged) & set(data)
        if overlap:
            raise ValueError(f"overlapping seed indices at {path}: {sorted(overlap)}")
        merged.update(data)
    expected = set(range(1, 570))
    if set(merged) != expected:
        raise ValueError(
            f"seed coverage mismatch missing={sorted(expected-set(merged))} "
            f"extra={sorted(set(merged)-expected)}"
        )
    if any(not isinstance(v, str) or not v.strip() for v in merged.values()):
        raise ValueError("empty or non-string seed")
    return merged


def main() -> None:
    if sha256(SOURCE) != SOURCE_SHA256:
        raise ValueError("gamedata source hash changed")
    if sha256(STYLE) != STYLE_SHA256 or sha256(GLOSSARY) != GLOSSARY_SHA256:
        raise ValueError("frozen style/glossary changed")

    rows = [json.loads(line) for line in CATALOG.read_text(encoding="utf-8").splitlines() if line]
    if [row["command_index"] for row in rows] != list(range(1, 570)):
        raise ValueError("catalog index/order changed")
    translations = load_seeds()

    draft_entries = []
    token_mismatches = []
    for row in rows:
        index = row["command_index"]
        draft_ko = translations[index]
        expected_tokens = token_multiset(row["source_jp"])
        actual_tokens = token_multiset(draft_ko)
        if expected_tokens != actual_tokens:
            token_mismatches.append({
                "command_index": index,
                "source_jp": row["source_jp"],
                "draft_ko": draft_ko,
                "expected": [[k, v, n] for (k, v), n in sorted(expected_tokens.items())],
                "actual": [[k, v, n] for (k, v), n in sorted(actual_tokens.items())],
            })
        semantic_basis = "Japanese current source only"
        if not row["current_source_present"]:
            semantic_basis = "technical old-key membership; Japanese key translated directly"
            if row["source_jp"] == "Death From In Flames":
                semantic_basis = "technical old-key passthrough; no semantic English interpretation"
        elif re.fullmatch(r"[\x00-\x7f]+", row["source_jp"]):
            semantic_basis = "canonical proper title in Japanese source file preserved verbatim"
        draft_entries.append({
            **{key: row[key] for key in (
                "stable_id", "command_index", "source_file", "section", "lane",
                "source_jp", "source_text_sha256", "key_origin",
                "official_old_key_present", "current_source_present",
                "occurrence_count", "occurrences", "protected_tokens",
            )},
            "draft_ko": draft_ko,
            "translation_basis": semantic_basis,
            "source_authority": row["source_authority"],
            "english_reference_used": False,
            "external_translation_api_used": False,
            "status": STATUS,
            "qa": QA,
        })

    if token_mismatches:
        (HERE / "gamedata.token_mismatches.json").write_text(
            json.dumps({"protected_token_mismatches": token_mismatches}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        print(json.dumps({"protected_token_mismatch_indices": [item["command_index"] for item in token_mismatches]}, ensure_ascii=True))
        raise SystemExit(2)

    characters = json.loads(CHARACTERS_DRAFT.read_text(encoding="utf-8"))
    shared_map = {e["source_jp"]: e["draft_ko"] for e in characters["entries"]}
    supplemental = [e for e in draft_entries if not e["official_old_key_present"]]
    shared_mismatches = [
        {"command_index": e["command_index"], "source_jp": e["source_jp"], "draft_ko": e["draft_ko"],
         "characters_mapping": shared_map.get(e["source_jp"])}
        for e in supplemental if shared_map.get(e["source_jp"]) != e["draft_ko"]
    ]
    if shared_mismatches:
        raise ValueError(f"supplemental global mappings mismatch: {shared_mismatches}")

    packet = {
        "schema_version": "fatal-twelve-system-ui-draft-v1",
        "packet_id": "system_ui_gamedata_all_display_keys",
        "source_file": "gamedata.rpy",
        "source_path": str(SOURCE),
        "source_sha256": SOURCE_SHA256,
        "catalog_path": str(CATALOG),
        "catalog_sha256": sha256(CATALOG),
        "entry_count": len(draft_entries),
        "current_source_occurrence_count": 556,
        "current_source_unique_count": 534,
        "official_old_key_count": 564,
        "catalog_union_count": 569,
        "technical_legacy_key_count": 35,
        "current_source_supplemental_count": 5,
        "shared_global_mapping_file": str(CHARACTERS_DRAFT),
        "source_language": "ja",
        "target_language": "ko",
        "source_authority": "Japanese source; official slot old-key membership only",
        "english_reference_used": False,
        "official_new_prose_parsed": False,
        "official_new_prose_stored": False,
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

    rpy_entries = [e for e in draft_entries if e["official_old_key_present"]]
    rpy_lines = [
        "# -*- coding: utf-8 -*-",
        "# Fatal Twelve gamedata.rpy Korean first draft.",
        "# Semantic/style source: Japanese current source only.",
        "# Official slot use: old-key membership only; new prose was not parsed, stored, or used.",
        "# Five current-source-only global name keys are supplied by characters.ko.rpy.",
        f"# status: {STATUS}",
        f"# qa: {QA}",
        "",
        "translate korean strings:",
        "",
    ]
    for entry in rpy_entries:
        rpy_lines.extend([
            f"    # {entry['stable_id']} | section={entry['section']} | occurrences={entry['occurrence_count']}",
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
            new_match = re.fullmatch(r"    new (.+)", lines[i + 1])
            if not new_match:
                raise ValueError("old without adjacent new")
            actual_pairs.append((ast.literal_eval(match.group(1)), ast.literal_eval(new_match.group(1))))
    expected_pairs = [(e["source_jp"], e["draft_ko"]) for e in rpy_entries]

    section_counts = Counter(e["section"] for e in draft_entries)
    lane_counts = Counter(e["lane"] for e in draft_entries)
    checks = {
        "source_hash": {"passed": sha256(SOURCE) == SOURCE_SHA256},
        "catalog_exact_union": {
            "passed": len(rows) == 569 and [r["command_index"] for r in rows] == list(range(1, 570)),
            "detail": {"catalog_entries": len(rows)},
        },
        "current_source_extraction": {
            "passed": (
                sum(e["occurrence_count"] for e in draft_entries if e["current_source_present"]) == 556
                and sum(e["current_source_present"] for e in draft_entries) == 534
            ),
            "detail": {"occurrences": 556, "unique": 534},
        },
        "official_old_key_coverage": {
            "passed": (
                len(rpy_entries) == 564 and len(actual_pairs) == 564
                and [p[0] for p in actual_pairs] == [e["source_jp"] for e in rpy_entries]
                and len({p[0] for p in actual_pairs}) == 564
            ),
            "detail": {"expected": 564, "actual": len(actual_pairs), "unique": len({p[0] for p in actual_pairs})},
        },
        "supplemental_current_keys_shared_mapping": {
            "passed": len(supplemental) == 5 and not shared_mismatches,
            "detail": {
                "count": len(supplemental),
                "keys": [e["source_jp"] for e in supplemental],
                "provided_by": str(CHARACTERS_DRAFT),
            },
        },
        "all_catalog_entries_drafted": {
            "passed": len(draft_entries) == 569 and all(e["draft_ko"].strip() for e in draft_entries),
        },
        "draft_flags": {
            "passed": all(
                e["english_reference_used"] is False
                and e["external_translation_api_used"] is False
                and e["status"] == STATUS and e["qa"] == QA
                for e in draft_entries
            ),
        },
        "protected_token_multisets": {
            "passed": not token_mismatches,
            "detail": {"mismatch_count": len(token_mismatches), "mismatches": token_mismatches},
        },
        "rpy_old_new_pairs": {
            "passed": actual_pairs == expected_pairs,
            "detail": {"pairs": len(actual_pairs)},
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
            "catalog_entries": len(rows),
            "draft_entries": len(draft_entries),
            "source_occurrences": 556,
            "source_unique_keys": 534,
            "official_old_unique_keys": 564,
            "rpy_strings_entries": len(actual_pairs),
            "technical_legacy_keys": 35,
            "supplemental_current_keys": 5,
            "sections": dict(sorted(section_counts.items())),
            "lanes": dict(sorted(lane_counts.items())),
        },
        "hashes": {
            "source_sha256": sha256(SOURCE),
            "style_guide_sha256": sha256(STYLE),
            "glossary_sha256": sha256(GLOSSARY),
            "catalog_sha256": sha256(CATALOG),
            "characters_shared_mapping_sha256": sha256(CHARACTERS_DRAFT),
            "draft_json_sha256": sha256(DRAFT),
            "draft_rpy_sha256": sha256(RPY),
        },
        "checks": checks,
    }
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(audit, ensure_ascii=True, indent=2))
    if not passed:
        sys.exit(1)


if __name__ == "__main__":
    main()
