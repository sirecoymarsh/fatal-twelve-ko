#!/usr/bin/env python3
"""Synthetic-only tests for correction guards and final RPY rendering."""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


FINAL_QA = Path(__file__).resolve().parents[1]
APPLY = FINAL_QA / "apply_corrections.py"
RENDER = FINAL_QA / "render_final_scenario.py"


def sha_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha_text(value: str) -> str:
    return sha_bytes(value.encode("utf-8"))


def sha_file(path: Path) -> str:
    return sha_bytes(path.read_bytes())


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def say_entry(
    *,
    stable_id: str,
    sequence: int,
    source_jp: str,
    draft_ko: str,
    translation_id: str,
    statement: str,
    group: list[str],
    protected_tokens: list[dict] | None = None,
) -> dict:
    return {
        "stable_id": stable_id,
        "sequence": sequence,
        "command_index": sequence,
        "source_file": "scenario/fixture.rpy",
        "source_line": 10 + sequence,
        "source_label": "fixture",
        "lane": "dialogue" if statement.startswith("alice ") else "narration",
        "speaker": "alice" if statement.startswith("alice ") else None,
        "source_jp": source_jp,
        "source_text_sha256": sha_text(source_jp),
        "source_group_sha256": sha_text(json.dumps(group, ensure_ascii=False, separators=(",", ":"))),
        "source_statement_code": statement,
        "source_group_code": group,
        "translation_id": translation_id,
        "id_origin": "synthetic",
        "menu_key": None,
        "voice_call": None,
        "protected_tokens": protected_tokens or [],
        "draft_ko": draft_ko,
        "draft_ko_sha256": sha_text(draft_ko),
        "status": "synthetic_first_draft",
        "qa": "synthetic_only",
    }


def menu_entry(*, stable_id: str, sequence: int, source_jp: str, draft_ko: str, menu_key: str) -> dict:
    return {
        "stable_id": stable_id,
        "sequence": sequence,
        "command_index": sequence,
        "source_file": "scenario/fixture.rpy",
        "source_line": 30 + sequence,
        "source_label": "fixture",
        "lane": "menu",
        "speaker": None,
        "source_jp": source_jp,
        "source_text_sha256": sha_text(source_jp),
        "source_group_sha256": sha_text(source_jp),
        "source_statement_code": json.dumps(source_jp, ensure_ascii=False),
        "source_group_code": [json.dumps(source_jp, ensure_ascii=False)],
        "translation_id": None,
        "id_origin": "menu-key",
        "menu_key": menu_key,
        "voice_call": None,
        "protected_tokens": [],
        "draft_ko": draft_ko,
        "draft_ko_sha256": sha_text(draft_ko),
        "status": "synthetic_first_draft",
        "qa": "synthetic_only",
    }


class SyntheticPipelineTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent)
        self.root = Path(self.temporary.name)
        self.masters_dir = self.root / "base" / "masters"
        self.script_one = self.masters_dir / "scenario_fixture_one.master.json"
        self.script_two = self.masters_dir / "scenario_fixture_two.master.json"

        one_entries = [
            say_entry(
                stable_id="fixture::one::tid::line1",
                sequence=1,
                source_jp="日本語。",
                draft_ko="한국어.",
                translation_id="fixture_one_line1",
                statement='"日本語。"',
                group=['"日本語。"'],
            ),
            say_entry(
                stable_id="fixture::one::tid::line2",
                sequence=2,
                source_jp="「値は１」",
                draft_ko="「값은 1」",
                translation_id="fixture_one_line2",
                statement='alice "「値は１」" with dissolve',
                group=['voice get_voice_filename("tst", 1)', 'alice "「値は１」" with dissolve'],
                protected_tokens=[
                    {"kind": "number", "value": "１", "start": 3, "end": 4, "severity": "hard"}
                ],
            ),
            menu_entry(
                stable_id="fixture::one::menu::yes",
                sequence=3,
                source_jp="はい",
                draft_ko="네",
                menu_key="fixture-one-yes",
            ),
        ]
        two_entries = [
            say_entry(
                stable_id="fixture::two::tid::line1",
                sequence=1,
                source_jp="{i}強調{/i}",
                draft_ko="{i}강조{/i}",
                translation_id="fixture_two_line1",
                statement='alice "{i}強調{/i}"',
                group=['show alice', 'alice "{i}強調{/i}"'],
                protected_tokens=[
                    {"kind": "renpy_text_tag", "value": "{i}", "start": 0, "end": 3, "severity": "hard"},
                    {"kind": "renpy_text_tag", "value": "{/i}", "start": 5, "end": 9, "severity": "hard"},
                ],
            ),
            menu_entry(
                stable_id="fixture::two::menu::yes",
                sequence=2,
                source_jp="はい",
                draft_ko="네",
                menu_key="fixture-two-yes",
            ),
        ]
        write_json(
            self.script_one,
            {"schema_version": "synthetic-master-v1", "script_key": "fixture_one", "entries": one_entries},
        )
        write_json(
            self.script_two,
            {"schema_version": "synthetic-master-v1", "script_key": "fixture_two", "entries": two_entries},
        )
        self.base_index = self.root / "base" / "master_index.json"
        write_json(
            self.base_index,
            {
                "schema_version": "synthetic-master-index-v1",
                "summary": {"selected_unique_records": 5},
                "masters": [
                    {
                        "script_key": "fixture_one",
                        "path": str(self.script_one),
                        "sha256": sha_file(self.script_one),
                        "selected_unique_records": 3,
                    },
                    {
                        "script_key": "fixture_two",
                        "path": str(self.script_two),
                        "sha256": sha_file(self.script_two),
                        "selected_unique_records": 2,
                    },
                ],
            },
        )
        self.review_groups = self.root / "review_groups.json"
        write_json(
            self.review_groups,
            {
                "schema_version": "fatal-twelve-review-group-manifest-v1",
                "groups": [
                    {"group_id": "A", "scripts": [{"script_key": "fixture_one"}]},
                    {"group_id": "ROOT", "scripts": [{"script_key": "fixture_two"}]},
                ],
            },
        )
        self.base_hashes = {self.script_one: sha_file(self.script_one), self.script_two: sha_file(self.script_two)}

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_tool(self, script: Path, *arguments: object) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment["PYTHONIOENCODING"] = "utf-8"
        return subprocess.run(
            [sys.executable, str(script), *(str(argument) for argument in arguments)],
            text=True,
            encoding="utf-8",
            capture_output=True,
            env=environment,
            check=False,
        )

    def correction_file(self, name: str, records: list[dict]) -> Path:
        path = self.root / name
        path.write_text(
            "".join(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n" for record in records),
            encoding="utf-8",
        )
        return path

    def apply_success(self, output_name: str = "corrected") -> Path:
        corrections = self.correction_file(
            "A.jsonl",
            [
                {
                    "stable_id": "fixture::one::tid::line1",
                    "old_ko": "한국어.",
                    "new_ko": "고친 한국어.",
                    "script_key": "fixture_one",
                    "sequence": 1,
                    "note": "synthetic success",
                }
            ],
        )
        output = self.root / output_name
        result = self.run_tool(
            APPLY,
            "--master-index",
            self.base_index,
            "--review-groups",
            self.review_groups,
            "--correction",
            f"A={corrections}",
            "--output-root",
            output,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr + result.stdout)
        return output / "corrected_master_index.json"

    def assert_base_unchanged(self) -> None:
        for path, expected_hash in self.base_hashes.items():
            self.assertEqual(sha_file(path), expected_hash)

    def test_successful_apply_and_render_with_global_menu_deduplication(self) -> None:
        corrected_index = self.apply_success()
        corrected = json.loads(corrected_index.read_text(encoding="utf-8"))
        self.assertEqual(corrected["summary"]["corrections_applied"], 1)
        self.assertEqual(corrected["summary"]["remaining_runtime_or_protected_token_failed_records"], 0)
        corrected_one = json.loads(Path(corrected["masters"][0]["path"]).read_text(encoding="utf-8"))
        self.assertEqual(corrected_one["entries"][0]["draft_ko"], "고친 한국어.")
        self.assertEqual(corrected_one["entries"][1]["draft_ko"], "「값은 1」")
        self.assert_base_unchanged()

        rendered_root = self.root / "rendered"
        result = self.run_tool(
            RENDER,
            "--master-index",
            corrected_index,
            "--output-root",
            rendered_root,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr + result.stdout)
        manifest = json.loads((rendered_root / "render_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["summary"]["scripts"], 2)
        self.assertEqual(manifest["summary"]["records"], 5)
        self.assertEqual(manifest["summary"]["translate_blocks"], 3)
        self.assertEqual(manifest["summary"]["menu_occurrences"], 2)
        self.assertEqual(manifest["summary"]["unique_global_menu_old_keys"], 1)
        self.assertEqual(manifest["summary"]["deduplicated_same_target_menu_occurrences"], 1)
        strings = (rendered_root / "strings" / "scenario_strings.rpy").read_text(encoding="utf-8")
        self.assertEqual(strings.count("    old "), 1)
        rendered_one = (rendered_root / "scenario" / "scenario_fixture_one.rpy").read_text(
            encoding="utf-8"
        )
        self.assertIn('voice get_voice_filename("tst", 1)', rendered_one)
        self.assertIn('alice "「값은 1」" with dissolve', rendered_one)
        self.assert_base_unchanged()

    def test_optional_system_ui_master_is_collected_into_global_strings(self) -> None:
        ui_entry = menu_entry(
            stable_id="system-ui::synthetic::settings",
            sequence=1,
            source_jp="\u8a2d\u5b9a\uff11\n\u78ba\u8a8d",
            draft_ko="\uc124\uc815 1\n\ud655\uc778",
            menu_key="\u8a2d\u5b9a\uff11\n\u78ba\u8a8d",
        )
        # Real system_ui.master.json uses legacy string-form protected tokens.
        # Full-width source digits may be rendered as NFKC-equivalent ASCII.
        ui_entry["protected_tokens"] = ["\uff11"]
        ui_entry.pop("source_statement_code")
        ui_entry.pop("source_group_code")
        ui_entry["source_file"] = "system-ui/global-strings"
        ui_master = self.root / "base" / "masters" / "system_ui.master.json"
        write_json(
            ui_master,
            {
                "schema_version": "fatal-twelve-system-ui-master-v1",
                "unique_runtime_string_keys": 1,
                "entries": [ui_entry],
            },
        )
        combined_index = json.loads(self.base_index.read_text(encoding="utf-8"))
        combined_index["summary"]["selected_unique_records"] = 6
        combined_index["masters"].append(
            {
                "script_key": "system_ui",
                "path": str(ui_master),
                "sha256": sha_file(ui_master),
                "selected_unique_records": 1,
            }
        )
        combined_index_path = self.root / "combined_master_index.json"
        write_json(combined_index_path, combined_index)
        groups = json.loads(self.review_groups.read_text(encoding="utf-8"))
        groups["groups"][0]["scripts"].append({"script_key": "system_ui"})
        groups_path = self.root / "combined_review_groups.json"
        write_json(groups_path, groups)
        corrections = self.correction_file(
            "combined_A.jsonl",
            [
                {
                    "stable_id": "fixture::one::tid::line1",
                    "old_ko": "\ud55c\uad6d\uc5b4.",
                    "new_ko": "\uace0\uce5c \ud55c\uad6d\uc5b4.",
                }
            ],
        )
        corrected_root = self.root / "combined-corrected"
        applied = self.run_tool(
            APPLY,
            "--master-index",
            combined_index_path,
            "--review-groups",
            groups_path,
            "--correction",
            f"A={corrections}",
            "--output-root",
            corrected_root,
        )
        self.assertEqual(applied.returncode, 0, msg=applied.stderr + applied.stdout)
        corrected_index_path = corrected_root / "corrected_master_index.json"
        corrected_index = json.loads(corrected_index_path.read_text(encoding="utf-8"))
        ui_reference = next(item for item in corrected_index["masters"] if item["script_key"] == "system_ui")
        self.assertEqual(ui_reference["kind"], "system_ui_strings")

        rendered_root = self.root / "combined-rendered"
        rendered = self.run_tool(
            RENDER,
            "--master-index",
            corrected_index_path,
            "--output-root",
            rendered_root,
        )
        self.assertEqual(rendered.returncode, 0, msg=rendered.stderr + rendered.stdout)
        manifest = json.loads((rendered_root / "render_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["summary"]["input_masters"], 3)
        self.assertEqual(manifest["summary"]["scripts"], 2)
        self.assertEqual(manifest["summary"]["system_ui_string_masters"], 1)
        self.assertEqual(manifest["summary"]["records"], 6)
        self.assertEqual(manifest["summary"]["menu_occurrences"], 3)
        self.assertEqual(manifest["summary"]["unique_global_menu_old_keys"], 2)
        strings = (rendered_root / "strings" / "scenario_strings.rpy").read_text(encoding="utf-8")
        self.assertIn("\uc124\uc815 1\\n\ud655\uc778", strings)
        self.assertIn("\u8a2d\u5b9a\uff11\\n\u78ba\u8a8d system-ui::synthetic::settings", strings)
        self.assertNotIn("\n\u78ba\u8a8d system-ui::synthetic::settings", strings)
        for line in strings.splitlines():
            if line.strip() and not line.lstrip().startswith("#"):
                self.assertTrue(
                    line == "translate korean strings:" or line.lstrip().startswith(("old ", "new ")),
                    msg=f"bare executable line leaked from provenance comment: {line!r}",
                )
        self.assertEqual(sha_file(ui_master), combined_index["masters"][-1]["sha256"])
        self.assert_base_unchanged()

    def test_supplemental_strings_are_merged_and_manifested(self) -> None:
        corrected_index = self.apply_success("supplement-corrected")
        supplement = self.root / "numeral.ko.rpy"
        supplement.write_text(
            "# add-only fixture\n\n"
            "translate korean strings:\n\n"
            "    old \"Numeral I\"\n"
            "    new \"\ubc88\ud638 I\"\n",
            encoding="utf-8",
        )
        supplement_hash = sha_file(supplement)
        rendered_root = self.root / "supplement-rendered"
        result = self.run_tool(
            RENDER,
            "--master-index",
            corrected_index,
            "--supplemental-strings",
            supplement,
            "--output-root",
            rendered_root,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr + result.stdout)
        manifest = json.loads((rendered_root / "render_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["summary"]["supplemental_string_inputs"], 1)
        self.assertEqual(manifest["summary"]["supplemental_string_pairs"], 1)
        self.assertEqual(manifest["summary"]["supplemental_old_key_conflicts"], 0)
        self.assertEqual(manifest["summary"]["total_unique_global_old_keys"], 2)
        strings = (rendered_root / "strings" / "scenario_strings.rpy").read_text(encoding="utf-8")
        self.assertIn('old "Numeral I"', strings)
        self.assertIn('new "\ubc88\ud638 I"', strings)
        self.assertEqual(sha_file(supplement), supplement_hash)
        self.assert_base_unchanged()

    def test_supplemental_old_key_collision_is_rejected(self) -> None:
        corrected_index = self.apply_success("supplement-conflict-corrected")
        first = json.loads(self.script_one.read_text(encoding="utf-8"))
        old = first["entries"][2]["source_jp"]
        supplement = self.root / "collision.ko.rpy"
        supplement.write_text(
            "translate korean strings:\n\n"
            f"    old {json.dumps(old, ensure_ascii=False)}\n"
            f"    new {json.dumps('different target', ensure_ascii=False)}\n",
            encoding="utf-8",
        )
        result = self.run_tool(
            RENDER,
            "--master-index",
            corrected_index,
            "--supplemental-strings",
            supplement,
            "--output-root",
            self.root / "supplement-conflict-rendered",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("supplemental old-key collision", result.stderr)
        self.assert_base_unchanged()

    def test_old_ko_exact_guard_rejects_stale_review(self) -> None:
        corrections = self.correction_file(
            "stale.jsonl",
            [{"stable_id": "fixture::one::tid::line1", "old_ko": "다른 값", "new_ko": "고침"}],
        )
        output = self.root / "stale-output"
        result = self.run_tool(
            APPLY,
            "--master-index",
            self.base_index,
            "--review-groups",
            self.review_groups,
            "--correction",
            f"A={corrections}",
            "--output-root",
            output,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("old_ko exact guard failed", result.stderr)
        self.assertFalse((output / "corrected_master_index.json").exists())
        self.assert_base_unchanged()

    def test_duplicate_stable_id_correction_is_forbidden(self) -> None:
        record = {"stable_id": "fixture::one::tid::line1", "old_ko": "한국어.", "new_ko": "고침"}
        a_file = self.correction_file("duplicate_A.jsonl", [record])
        root_file = self.correction_file("duplicate_ROOT.jsonl", [record])
        result = self.run_tool(
            APPLY,
            "--master-index",
            self.base_index,
            "--review-groups",
            self.review_groups,
            "--correction",
            f"A={a_file}",
            "--correction",
            f"ROOT={root_file}",
            "--output-root",
            self.root / "duplicate-output",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("duplicate correction stable_id", result.stderr)
        self.assert_base_unchanged()

    def test_new_ko_protected_number_loss_is_rejected(self) -> None:
        corrections = self.correction_file(
            "token-loss.jsonl",
            [
                {
                    "stable_id": "fixture::one::tid::line2",
                    "old_ko": "「값은 1」",
                    "new_ko": "「값은 하나」",
                }
            ],
        )
        result = self.run_tool(
            APPLY,
            "--master-index",
            self.base_index,
            "--review-groups",
            self.review_groups,
            "--correction",
            f"A={corrections}",
            "--output-root",
            self.root / "token-output",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("runtime/protected-token validation failed", result.stderr)
        self.assertIn("arabic_number_mismatch", result.stderr)
        self.assert_base_unchanged()

    def test_new_ko_runtime_tag_loss_is_rejected(self) -> None:
        corrections = self.correction_file(
            "tag-loss.jsonl",
            [
                {
                    "stable_id": "fixture::two::tid::line1",
                    "old_ko": "{i}\uac15\uc870{/i}",
                    "new_ko": "\uac15\uc870",
                }
            ],
        )
        result = self.run_tool(
            APPLY,
            "--master-index",
            self.base_index,
            "--review-groups",
            self.review_groups,
            "--correction",
            f"ROOT={corrections}",
            "--output-root",
            self.root / "tag-output",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("runtime/protected-token validation failed", result.stderr)
        self.assertIn("renpy_text_tag_mismatch", result.stderr)
        self.assert_base_unchanged()

    def test_global_menu_same_old_different_target_is_rejected(self) -> None:
        corrected_index_path = self.apply_success("menu-conflict-corrected")
        corrected_index = json.loads(corrected_index_path.read_text(encoding="utf-8"))
        second_ref = next(item for item in corrected_index["masters"] if item["script_key"] == "fixture_two")
        second_path = Path(second_ref["path"])
        second = json.loads(second_path.read_text(encoding="utf-8"))
        second["entries"][1]["draft_ko"] = "예"
        second["entries"][1]["draft_ko_sha256"] = sha_text("예")
        write_json(second_path, second)
        second_ref["sha256"] = sha_file(second_path)
        write_json(corrected_index_path, corrected_index)
        result = self.run_tool(
            RENDER,
            "--master-index",
            corrected_index_path,
            "--output-root",
            self.root / "menu-conflict-render",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("global menu old-key target conflict", result.stderr)
        self.assert_base_unchanged()

    def test_source_statement_group_identity_is_enforced(self) -> None:
        corrected_index_path = self.apply_success("statement-mismatch-corrected")
        corrected_index = json.loads(corrected_index_path.read_text(encoding="utf-8"))
        first_ref = next(item for item in corrected_index["masters"] if item["script_key"] == "fixture_one")
        first_path = Path(first_ref["path"])
        first = json.loads(first_path.read_text(encoding="utf-8"))
        first["entries"][0]["source_statement_code"] = '"別の原文"'
        write_json(first_path, first)
        first_ref["sha256"] = sha_file(first_path)
        write_json(corrected_index_path, corrected_index)
        result = self.run_tool(
            RENDER,
            "--master-index",
            corrected_index_path,
            "--output-root",
            self.root / "statement-mismatch-render",
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("source_statement_code must occur exactly once", result.stderr)
        self.assert_base_unchanged()


if __name__ == "__main__":
    unittest.main(verbosity=2)
