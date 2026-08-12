#!/usr/bin/env python3
"""Independent final-RPY and Korean language-selector contract verifier."""

from __future__ import annotations

import ast
import collections
import copy
import io
import json
import re
import textwrap
import tokenize
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

from final_qa_common import file_sha256, read_json, text_sha256, write_json
from render_final_scenario import parse_supplemental_strings


HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
BUILD = HERE / "final_text_build_ui_feedback_v2"
FINAL_RPY = BUILD / "final_rpy"
RESULT = BUILD / "final_text_pipeline_result.json"
RENDER_MANIFEST = FINAL_RPY / "render_manifest.json"
BOOTSTRAP = REPO_ROOT / "work" / "patch_architecture" / "skeleton" / "game" / "f12_korean_bootstrap.rpy"
SLOT = REPO_ROOT / "work" / "patch_architecture" / "skeleton" / "game" / "tl" / "korean" / "f12_slot.rpy"
SUPPLEMENT = REPO_ROOT / "work" / "system_ui" / "runtime_application" / "numeral_composed_string_keys.ko.rpy"
OUT = HERE / "technical_qa" / "final_rpy_static_contract.json"

HEADER_RE = re.compile(r"^translate korean ([A-Za-z0-9_]+):$")
ANY_TRANSLATE_RE = re.compile(r"^\s*translate\s+(\S+)\s+([^:]+):\s*$", re.MULTILINE)
OLD_RE = re.compile(r"^\s*old\s+(.+?)\s*$")
NEW_RE = re.compile(r"^\s*new\s+(.+?)\s*$")


def strict_text(path: Path) -> tuple[bytes, str]:
    raw = path.read_bytes()
    text = raw.decode("utf-8", "strict")
    if raw.startswith(b"\xef\xbb\xbf"):
        raise ValueError(f"UTF-8 BOM is not allowed: {path}")
    if b"\r" in raw:
        raise ValueError(f"non-LF newline in generated RPY: {path}")
    return raw, text


def string_tokens(line: str) -> list[tuple[int, int, str, str]]:
    result = []
    try:
        tokens = tokenize.generate_tokens(io.StringIO(line).readline)
        for token in tokens:
            if token.type != tokenize.STRING:
                continue
            if token.start[0] != 1 or token.end[0] != 1:
                raise ValueError("multiline string token is not allowed")
            value = ast.literal_eval(token.string)
            if not isinstance(value, str):
                raise ValueError("generated literal did not decode to string")
            if ast.literal_eval(repr(value)) != value or json.loads(json.dumps(value, ensure_ascii=False)) != value:
                raise ValueError("literal round-trip mismatch")
            result.append((token.start[1], token.end[1], token.string, value))
    except (IndentationError, tokenize.TokenError):
        # Ren'Py statement syntax is not always a complete Python statement.
        # The generated dialogue/menu literals are still standard JSON/Python
        # double-quoted strings, so scan those independently as a fallback.
        for match in re.finditer(r'"(?:\\.|[^"\\])*"', line):
            value = ast.literal_eval(match.group(0))
            if not isinstance(value, str) or json.loads(json.dumps(value, ensure_ascii=False)) != value:
                raise ValueError("fallback literal round-trip mismatch")
            result.append((match.start(), match.end(), match.group(0), value))
    return result


def replace_semantic_literal(statement: str, source: str, target: str) -> str:
    matches = [item for item in string_tokens(statement) if item[3] == source]
    if len(matches) != 1:
        raise ValueError(f"source statement has {len(matches)} exact semantic literals, expected 1")
    start, end, _, _ = matches[0]
    rendered_literal = json.dumps(target, ensure_ascii=False)
    if ast.literal_eval(rendered_literal) != target:
        raise ValueError("target literal failed pre-render round-trip")
    return statement[:start] + rendered_literal + statement[end:]


def parse_translate_blocks(text: str) -> list[tuple[str, list[str]]]:
    lines = text.splitlines()
    headers = [(index, match.group(1)) for index, line in enumerate(lines) if (match := HEADER_RE.fullmatch(line))]
    blocks = []
    for position, (index, translation_id) in enumerate(headers):
        end = headers[position + 1][0] if position + 1 < len(headers) else len(lines)
        body = lines[index + 1:end]
        while body and body[0] == "":
            body.pop(0)
        while body and body[-1] == "":
            body.pop()
        if any(not line.startswith("    ") for line in body):
            raise ValueError(f"{translation_id}: non-indented generated block line")
        blocks.append((translation_id, [line[4:] for line in body]))
    return blocks


def parse_global_strings(path: Path) -> tuple[list[tuple[str, str]], int]:
    _, text = strict_text(path)
    if len(re.findall(r"^translate korean strings:$", text, flags=re.MULTILINE)) != 1:
        raise ValueError("global strings file must contain exactly one Korean strings header")
    pending = None
    pairs = []
    literal_count = 0
    for line_no, line in enumerate(text.splitlines(), 1):
        old_match, new_match = OLD_RE.fullmatch(line), NEW_RE.fullmatch(line)
        if old_match:
            if pending is not None:
                raise ValueError(f"global strings:{line_no}: old without prior new")
            old = ast.literal_eval(old_match.group(1))
            if not isinstance(old, str) or ast.literal_eval(repr(old)) != old:
                raise ValueError(f"global strings:{line_no}: old literal round-trip")
            pending = old
            literal_count += 1
        elif new_match:
            if pending is None:
                raise ValueError(f"global strings:{line_no}: new without old")
            new = ast.literal_eval(new_match.group(1))
            if not isinstance(new, str) or ast.literal_eval(repr(new)) != new:
                raise ValueError(f"global strings:{line_no}: new literal round-trip")
            pairs.append((pending, new))
            pending = None
            literal_count += 1
        elif line.strip() and not line.lstrip().startswith("#") and line != "translate korean strings:":
            raise ValueError(f"global strings:{line_no}: unsupported executable line")
    if pending is not None:
        raise ValueError("global strings ends with unmatched old")
    return pairs, literal_count


class MockAction:
    pass


class MockDictEquality:
    pass


class MockPersistent:
    pass


class MockRenpy:
    def __init__(self, preferences, languages=("english", "korean")):
        self.preferences = preferences
        self.languages = set(languages)
        self.screens = {}
        self.change_calls = []
        self.show_calls = []
        self.hide_calls = []

    def change_language(self, language):
        self.change_calls.append(language)
        self.preferences.language = language

    def known_languages(self):
        return set(self.languages)

    def get_screen(self, name):
        return self.screens.get(name)

    def show_screen(self, name):
        self.show_calls.append(name)
        self.screens[name] = SimpleNamespace(scope={})

    def hide_screen(self, name):
        self.hide_calls.append(name)
        self.screens.pop(name, None)


def bootstrap_python(text: str) -> str:
    marker = "init -999 python:\n"
    if text.count(marker) != 1 or text.count("\nscreen f12_patch_language_selector:") != 1:
        raise ValueError("bootstrap init/screen boundaries changed")
    remainder = text.split(marker, 1)[1]
    indented = []
    for line in remainder.splitlines():
        if line and not line.startswith((" ", "\t")):
            break
        indented.append(line)
    return textwrap.dedent("\n".join(indented))


def execute_bootstrap(body: str, persistent, initial_language="english"):
    preferences = SimpleNamespace(language=initial_language)
    renpy = MockRenpy(preferences)
    config = SimpleNamespace(interact_callbacks=[])
    namespace = {
        "persistent": persistent,
        "_preferences": preferences,
        "renpy": renpy,
        "config": config,
        "Action": MockAction,
        "DictEquality": MockDictEquality,
    }
    exec(compile(body, str(BOOTSTRAP), "exec"), namespace, namespace)
    return namespace, preferences, renpy, config


def verify_selector_contract(bootstrap_text: str, slot_text: str) -> dict:
    required = [
        'label "언어":',
        'textbutton "日本語":',
        'action F12PatchLanguage("japanese", None)',
        'textbutton "English":',
        'action F12PatchLanguage("english", "english")',
        'textbutton "한국어":',
        'action F12PatchLanguage("korean", "korean")',
        'getattr(persistent, "fatal12_ko_language_v1", None)',
        'if _f12_language_marker not in ("japanese", "english", "korean"):',
    ]
    missing = [item for item in required if item not in bootstrap_text]
    if missing:
        raise ValueError(f"bootstrap required selector contract missing: {missing}")
    if "translate english" in bootstrap_text or "translate japanese" in bootstrap_text:
        raise ValueError("bootstrap unexpectedly defines English/Japanese translation blocks")
    if not slot_text.startswith("# Fatal Twelve Korean language-slot") or slot_text.count("translate korean python:") != 1:
        raise ValueError("Korean slot must contain exactly one Korean python translation block")
    if re.search(r"^translate\s+(?:english|japanese)\b", slot_text, flags=re.MULTILINE):
        raise ValueError("Korean slot modifies English/Japanese translation blocks")
    if "persistent" in slot_text or "_preferences.language" in slot_text:
        raise ValueError("Korean slot contains a global language/persistence mutation")
    body = bootstrap_python(bootstrap_text)

    init_matrix = []
    sentinel = object()
    for marker, expected_marker, expected_language in [
        (sentinel, "korean", "korean"),
        ("invalid", "korean", "korean"),
        ("japanese", "japanese", None),
        ("english", "english", "english"),
        ("korean", "korean", "korean"),
    ]:
        persistent = MockPersistent()
        if marker is not sentinel:
            persistent.fatal12_ko_language_v1 = marker
        namespace, preferences, _, config = execute_bootstrap(body, persistent)
        actual_marker = persistent.fatal12_ko_language_v1
        if (actual_marker, preferences.language, len(config.interact_callbacks)) != (expected_marker, expected_language, 1):
            raise ValueError(f"bootstrap init matrix failed for marker {marker!r}")
        init_matrix.append({"input_marker": None if marker is sentinel else marker,
                            "output_marker": actual_marker, "output_language": preferences.language})

    persistent = MockPersistent()
    namespace, preferences, renpy, _ = execute_bootstrap(body, persistent)
    action_type = namespace["F12PatchLanguage"]
    transitions = []
    for marker, language in [("japanese", None), ("english", "english"), ("korean", "korean")]:
        action = action_type(marker, language)
        if not action.get_sensitive():
            raise ValueError(f"selector action unexpectedly insensitive: {marker}")
        action()
        if persistent.fatal12_ko_language_v1 != marker or preferences.language != language or renpy.change_calls[-1] != language:
            raise ValueError(f"selector transition failed: {marker}")
        if not action.get_selected():
            raise ValueError(f"selector selected state failed: {marker}")
        # Simulate the next engine boot after shipped localize.rpyc resets the
        # in-memory preference to English. The patch-owned persistent marker
        # must restore the exact selected slot.
        namespace, preferences, renpy, _ = execute_bootstrap(body, persistent, initial_language="english")
        expected = None if marker == "japanese" else marker
        if preferences.language != expected:
            raise ValueError(f"restart persistence simulation failed: {marker}")
        action_type = namespace["F12PatchLanguage"]
        transitions.append({"marker": marker, "language_argument": language,
                            "language_after_simulated_restart": preferences.language})

    preferences_screen = SimpleNamespace(scope={"current_tab": "system"})
    renpy.screens["preferences"] = preferences_screen
    namespace["_f12_sync_language_selector"]()
    if renpy.show_calls != ["f12_patch_language_selector"]:
        raise ValueError("selector screen did not show on Preferences/System")
    preferences_screen.scope["current_tab"] = "display"
    namespace["_f12_sync_language_selector"]()
    if renpy.hide_calls != ["f12_patch_language_selector"]:
        raise ValueError("selector screen did not hide outside Preferences/System")

    return {
        "bootstrap_init_priority": -999,
        "default_marker": "korean",
        "marker_domain": ["japanese", "english", "korean"],
        "japanese_runtime_language": None,
        "english_runtime_language": "english",
        "korean_runtime_language": "korean",
        "init_matrix": init_matrix,
        "action_restart_transitions": transitions,
        "selector_visibility_callback": "PASS",
        "korean_font_overrides_scoped_to_translate_korean_python": True,
        "english_japanese_translation_blocks_added": False,
        "verdict": "PASS",
    }


def main() -> None:
    result = read_json(RESULT)
    manifest = read_json(RENDER_MANIFEST)
    corrected_index_path = Path(result["corrected_master_index"]["path"])
    if file_sha256(corrected_index_path) != result["corrected_master_index"]["sha256"]:
        raise SystemExit("corrected master index hash mismatch")
    corrected_index = read_json(corrected_index_path)
    refs = corrected_index["masters"]
    scenario_refs = [ref for ref in refs if ref.get("script_key") != "system_ui"]
    ui_refs = [ref for ref in refs if ref.get("script_key") == "system_ui"]
    if len(scenario_refs) != 29 or len(ui_refs) != 1:
        raise SystemExit("corrected master universe must be 29 scenario + 1 system UI")

    manifest_scripts = {row["script_key"]: row for row in manifest["scripts"]}
    all_ids = []
    all_literal_count = 0
    file_reports = []
    expected_global = {}
    menu_occurrences = 0
    for ref in refs:
        master_path = Path(ref["path"])
        if file_sha256(master_path) != ref["sha256"]:
            raise SystemExit(f"corrected master hash mismatch: {master_path}")
        master = read_json(master_path)
        for entry in master["entries"]:
            if entry.get("menu_key") is not None:
                menu_occurrences += 1
                old, target = entry["source_jp"], entry["draft_ko"]
                if old in expected_global and expected_global[old] != target:
                    raise SystemExit(f"master menu old-key target conflict: {old!r}")
                expected_global[old] = target
        if ref["script_key"] == "system_ui":
            continue
        script_key = ref["script_key"]
        render_ref = manifest_scripts[script_key]
        output_path = Path(render_ref["path"])
        raw, text = strict_text(output_path)
        if file_sha256(output_path) != render_ref["sha256"] or len(raw) != render_ref["bytes"]:
            raise SystemExit(f"render manifest file binding mismatch: {script_key}")
        languages = {language for language, _ in ANY_TRANSLATE_RE.findall(text)}
        if languages != {"korean"}:
            raise SystemExit(f"non-Korean translation namespace emitted: {script_key}:{languages}")
        actual_blocks = parse_translate_blocks(text)
        expected_entries = [entry for entry in master["entries"] if entry["translation_id"] is not None]
        if len(actual_blocks) != len(expected_entries):
            raise SystemExit(f"translate-block count mismatch: {script_key}")
        for (translation_id, actual_group), entry in zip(actual_blocks, expected_entries):
            if translation_id != entry["translation_id"]:
                raise SystemExit(f"translate ID/order mismatch: {script_key}:{translation_id}")
            expected_group = copy.deepcopy(entry["source_group_code"])
            statement = entry["source_statement_code"]
            if expected_group.count(statement) != 1:
                raise SystemExit(f"source statement multiplicity mismatch: {entry['stable_id']}")
            rendered_statement = replace_semantic_literal(statement, entry["source_jp"], entry["draft_ko"])
            expected_group[expected_group.index(statement)] = rendered_statement
            if actual_group != expected_group:
                raise SystemExit(f"generated group differs outside exact target literal: {entry['stable_id']}")
            for code_line in actual_group:
                all_literal_count += len(string_tokens(code_line))
            all_ids.append(translation_id)
        file_reports.append({
            "script_key": script_key,
            "path": str(output_path.resolve()),
            "sha256": file_sha256(output_path),
            "bytes": len(raw),
            "strict_utf8": True,
            "lf_only": True,
            "translate_blocks": len(actual_blocks),
            "literal_round_trip": "PASS",
            "exact_source_group_reconstruction": "PASS",
        })

    if len(all_ids) != 18126 or len(set(all_ids)) != 18126:
        raise SystemExit(f"global translate-ID uniqueness/count failure: {len(all_ids)}/{len(set(all_ids))}")

    supplement_pairs, supplement_report = parse_supplemental_strings(SUPPLEMENT)
    for row in supplement_pairs:
        if row["old"] in expected_global:
            raise SystemExit(f"supplement old key collision: {row['old']!r}")
        expected_global[row["old"]] = row["target"]
    global_path = Path(manifest["global_strings"]["path"])
    pairs, global_literal_count = parse_global_strings(global_path)
    actual_global = dict(pairs)
    if len(pairs) != len(actual_global) or actual_global != expected_global:
        raise SystemExit("global old/new mapping differs from corrected masters + supplement")
    if (menu_occurrences, len(expected_global) - len(supplement_pairs), len(supplement_pairs), len(actual_global)) != (790, 785, 12, 797):
        raise SystemExit("global string exact count gate failed")

    bootstrap_raw, bootstrap_text = strict_text(BOOTSTRAP)
    slot_raw, slot_text = strict_text(SLOT)
    selector = verify_selector_contract(bootstrap_text, slot_text)
    approved_audit = read_json(Path(result["approved_static_audit"]["path"]))
    all_master_gate = approved_audit["gate"]
    scenario_gate = approved_audit["scenario_gate"]
    system_ui_gate = approved_audit["system_ui_gate"]
    if not all_master_gate["pass"] or not scenario_gate["pass"] or not system_ui_gate["pass"]:
        raise SystemExit("recomputed approved audit gate is open")

    report = {
        "schema_version": "fatal-twelve-final-rpy-static-runtime-contract-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "inputs": {
            "pipeline_result": {"path": str(RESULT.resolve()), "sha256": file_sha256(RESULT)},
            "render_manifest": {"path": str(RENDER_MANIFEST.resolve()), "sha256": file_sha256(RENDER_MANIFEST)},
            "corrected_master_index": {"path": str(corrected_index_path.resolve()), "sha256": file_sha256(corrected_index_path)},
            "bootstrap": {"path": str(BOOTSTRAP.resolve()), "sha256": file_sha256(BOOTSTRAP), "bytes": len(bootstrap_raw)},
            "korean_slot": {"path": str(SLOT.resolve()), "sha256": file_sha256(SLOT), "bytes": len(slot_raw)},
            "numeral_supplement": {"path": str(SUPPLEMENT.resolve()), "sha256": file_sha256(SUPPLEMENT), "pairs": len(supplement_pairs)},
        },
        "rpy_validation": {
            "scenario_files": len(file_reports),
            "strict_utf8_files": len(file_reports) + 3,
            "lf_only_generated_files": len(file_reports) + 1,
            "translate_blocks": len(all_ids),
            "globally_unique_translate_ids": len(set(all_ids)),
            "parsed_scenario_literal_tokens": all_literal_count,
            "global_string_literal_tokens": global_literal_count,
            "menu_occurrences": menu_occurrences,
            "unique_master_old_keys": len(actual_global) - len(supplement_pairs),
            "supplemental_old_keys": len(supplement_pairs),
            "total_unique_global_old_keys": len(actual_global),
            "duplicate_global_old_keys": len(pairs) - len(actual_global),
            "global_target_conflicts": 0,
            "exact_master_and_source_group_match": True,
            "verdict": "PASS",
        },
        "language_selector_contract": selector,
        "approved_static_gates": {
            "all_master_gate": all_master_gate,
            "scenario_gate": scenario_gate,
            "system_ui_gate": system_ui_gate,
            "record_bound_approvals": approved_audit["record_bound_approval_count"],
            "verdict": "PASS",
        },
        "scenario_files": file_reports,
        "global_strings": {
            "path": str(global_path.resolve()),
            "sha256": file_sha256(global_path),
            "pairs": len(pairs),
            "unique_old_keys": len(actual_global),
            "exact_corrected_master_plus_supplement_match": True,
        },
        "source_contract": {
            "semantic_authority": "Japanese only",
            "generated_translation_namespaces": ["korean"],
            "japanese_slot_mapping": None,
            "english_slot_mapping": "english",
            "korean_slot_mapping": "korean",
            "english_japanese_translation_payloads_modified": False,
            "game_executed": False,
        },
        "verdict": "PASS",
    }
    write_json(OUT, report)
    print(json.dumps({
        "report": str(OUT.resolve()),
        "report_sha256": file_sha256(OUT),
        "translate_blocks": len(all_ids),
        "global_old_keys": len(actual_global),
        "selector_contract": selector["verdict"],
        "verdict": "PASS",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
