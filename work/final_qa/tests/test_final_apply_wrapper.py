from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path

FINAL_QA = Path(__file__).resolve().parents[1]
ROOT = FINAL_QA.parents[1]
if str(FINAL_QA) not in sys.path:
    sys.path.insert(0, str(FINAL_QA))

import run_final_apply as final_apply
from final_qa_common import file_sha256, text_sha256


class FinalApplyWrapperTests(unittest.TestCase):
    def test_real_base_inventory_includes_ui_without_mutation(self):
        master_index = FINAL_QA / "output" / "master_index.json"
        groups = FINAL_QA / "review_group_manifest.json"
        ui = FINAL_QA / "output" / "masters" / "system_ui.master.json"
        before = {
            master_index: file_sha256(master_index),
            groups: file_sha256(groups),
            ui: file_sha256(ui),
        }
        index, combined_groups, docs, stable, base_target, assignment, order = final_apply.load_bases(
            master_index, groups, ui
        )
        self.assertEqual(len(index["masters"]), 30)
        self.assertEqual(len(docs), 30)
        self.assertEqual(len(stable), 18916)
        self.assertEqual(len(base_target), 18916)
        self.assertEqual(assignment["system_ui"], "A")
        self.assertEqual(order["system_ui"], 29)
        self.assertEqual(
            next(g for g in combined_groups["groups"] if g["group_id"] == "A")["scripts"][-1],
            {"script_key": "system_ui", "expected_records": 732},
        )
        for path, expected in before.items():
            self.assertEqual(file_sha256(path), expected)

    def test_real_numeral_supplement_is_exact_twelve_pairs(self):
        supplement = ROOT / "work" / "system_ui" / "runtime_application" / "numeral_composed_string_keys.ko.rpy"
        with tempfile.TemporaryDirectory(dir=FINAL_QA / "tests") as temp:
            manifest = Path(temp) / "manifest.json"
            manifest.write_text("{}\n", encoding="utf-8")
            paths, reports = final_apply.load_supplement(
                {
                    "supplemental_strings": [
                        {"path": str(supplement), "sha256": file_sha256(supplement), "pairs": 12}
                    ]
                },
                manifest,
            )
        self.assertEqual(paths, [supplement.resolve()])
        self.assertEqual(reports[0]["pairs"], 12)
        self.assertTrue(reports[0]["expected_numeral_pairs_exact"])

    def test_bootstrap_is_strict_utf8_with_exact_language_literals(self):
        bootstrap = ROOT / "work" / "patch_architecture" / "skeleton" / "game" / "f12_korean_bootstrap.rpy"
        result = final_apply.validate_bootstrap(bootstrap)
        self.assertTrue(result["strict_utf8"])
        self.assertEqual(result["language_label"], "\uc5b8\uc5b4")
        self.assertEqual(result["japanese_button"], "\u65e5\u672c\u8a9e")
        self.assertEqual(result["korean_button"], "\ud55c\uad6d\uc5b4")

    def test_record_bound_approval_requires_source_and_target_hashes(self):
        issue = {
            "script": "001",
            "stable_id": "fixture::1",
            "rule_id": "GLOSSARY_MISMATCH",
            "source_jp": "\u51db\u706b",
            "draft_ko": "\ubbf8\ud558\ub8e8",
            "finding_id": "fixture-finding",
            "policy_severity": "REVIEW",
            "status": "open",
        }
        report = {"issues": [issue]}
        approval = {
            "scope": "scenario",
            "stable_id": "fixture::1",
            "rule_id": "GLOSSARY_MISMATCH",
            "source_sha256": text_sha256(issue["source_jp"]),
            "target_sha256": text_sha256(issue["draft_ko"]),
            "reviewer": "ROOT",
            "reason": "narrow source anomaly",
            "status": "approved",
        }
        approved = final_apply.apply_approvals(
            report, [approval], {"path": "fixture.json", "sha256": "0" * 64, "records": 1}
        )
        self.assertTrue(approved["scenario_gate"]["pass"])
        self.assertEqual(approved["issues"][0]["status"], "approved")
        bad = copy.deepcopy(approval)
        bad["target_sha256"] = "f" * 64
        with self.assertRaises(final_apply.FinalApplyError):
            final_apply.apply_approvals(
                report, [bad], {"path": "fixture.json", "sha256": "0" * 64, "records": 1}
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)