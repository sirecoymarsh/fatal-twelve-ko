from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

FINAL_QA = Path(__file__).resolve().parents[1]
if str(FINAL_QA) not in sys.path:
    sys.path.insert(0, str(FINAL_QA))
import audit_master as audit

def findings(source: str, target: str, **extra):
    ruby_map = extra.pop("ruby_map", {})
    entry = {
        "stable_id": extra.pop("stable_id", "fixture:1"),
        "sequence": extra.pop("sequence", 1),
        "source_jp": source,
        "draft_ko": target,
        **extra,
    }
    result = []
    audit.audit_entry(entry, "fixture", result, ruby_map=ruby_map)
    return result

def rule_ids(items):
    return [item["rule_id"] for item in items]

class LiteralAndLexerPolicyTests(unittest.TestCase):
    def test_decoded_literal_roundtrip(self):
        text = '「[name]」\n{{literal}} \\ path "quoted"'
        rendered = audit.render_renpy_literal(text)
        self.assertEqual(audit.decode_renpy_literal(rendered), text)
        self.assertTrue(audit.literal_roundtrip(text))
        with self.assertRaises((SyntaxError, ValueError)):
            audit.decode_renpy_literal('"unterminated')

    def test_lexer_recognizes_controls_and_literal_escapes(self):
        result = audit.lex_renpy_text(r"[[x {{y [name!q] {b}z{/b} %(count)d %s %% \n")
        self.assertEqual(result.errors, [])
        kinds = [token.kind for token in result.tokens]
        self.assertIn("interpolation", kinds)
        self.assertEqual(kinds.count("literal_escape"), 3)
        self.assertIn("percent_named", kinds)
        self.assertIn("percent_positional", kinds)
        self.assertIn("percent_escape", kinds)

    def test_raw_literal_mismatch_is_hard(self):
        items = findings("日本語", "한국어", target_literal_raw='"다른 문자열"')
        self.assertIn("RENPY_LITERAL_ROUNDTRIP_FAIL", rule_ids(items))

class ProtectedTokenPolicyTests(unittest.TestCase):
    def test_matching_interpolation_and_tags_pass(self):
        items = findings("[name]は{b}ここ{/b}", "[name]은 {b}여기{/b}")
        self.assertNotIn("INTERPOLATION_MISMATCH", rule_ids(items))
        self.assertNotIn("TEXT_TAG_MISMATCH", rule_ids(items))

    def test_missing_interpolation_and_closing_tag_are_hard(self):
        items = findings("[name]は{b}ここ{/b}", "여기는 {b}여기")
        self.assertIn("INTERPOLATION_MISMATCH", rule_ids(items))
        self.assertIn("TEXT_TAG_MISMATCH", rule_ids(items))

    def test_named_reorder_review_but_positional_reorder_hard(self):
        named = findings("%(a)s %(b)s", "%(b)s %(a)s")
        positional = findings("%s %d", "%d %s")
        self.assertIn("PERCENT_NAMED_REORDER", rule_ids(named))
        self.assertIn("PERCENT_POSITIONAL_MISMATCH", rule_ids(positional))

    def test_literal_escapes_are_exact(self):
        source = r"[[SAVE]] {{tag}} %% \n" + "\n"
        target = "[SAVE]] {tag}} % "
        ids = rule_ids(findings(source, target))
        self.assertIn("LITERAL_ESCAPE_MISMATCH", ids)
        self.assertIn("PERCENT_LITERAL_ESCAPE_MISMATCH", ids)
        self.assertIn("CONTROL_NEWLINE_MISMATCH", ids)

    def test_number_kind_is_semantic_not_exact_spelling(self):
        items = findings(
            "１７歳",
            "17살",
            protected_tokens=[{"kind": "number", "value": "１７"}],
        )
        self.assertNotIn("PROTECTED_TOKEN_MISMATCH", rule_ids(items))
        self.assertNotIn("NUM_SEMANTIC_MISMATCH", rule_ids(items))

    def test_legacy_string_number_is_nfkc_semantic_not_exact_spelling(self):
        items = findings("\uff11\uff17\u6b73", "17\uc0b4", protected_tokens=["\uff11\uff17"])
        self.assertNotIn("PROTECTED_TOKEN_MISMATCH", rule_ids(items))
        self.assertNotIn("NUM_SEMANTIC_MISMATCH", rule_ids(items))

class RubyRomanAndQuotePolicyTests(unittest.TestCase):
    def test_ruby_approved_map_passes(self):
        source = "{rb}蛇鉈{/rb}{rt}へびなた{/rt}"
        target = "{rb}헤비나타{/rb}{rt}헤비나타{/rt}"
        mapping = {("蛇鉈", "へびなた"): ("헤비나타", "헤비나타")}
        items = findings(source, target, ruby_map=mapping)
        self.assertNotIn("RUBY_STRUCTURE_MISMATCH", rule_ids(items))
        self.assertNotIn("RUBY_MAPPING_MISMATCH", rule_ids(items))
        self.assertNotIn("RUBY_UNMAPPED", rule_ids(items))

    def test_standalone_rt_ruby_approved_map_passes(self):
        source = "最後の刻{rt}とき{/rt}"
        target = "마지막 순간{rt}때{/rt}"
        mapping = {("刻", "とき"): ("순간", "때")}
        items = findings(source, target, ruby_map=mapping)
        self.assertNotIn("RUBY_MALFORMED", rule_ids(items))
        self.assertNotIn("RUBY_STRUCTURE_MISMATCH", rule_ids(items))
        self.assertNotIn("RUBY_MAPPING_MISMATCH", rule_ids(items))
        self.assertNotIn("RUBY_UNMAPPED", rule_ids(items))

    def test_ruby_missing_and_unmapped(self):
        source = "{rb}蛇鉈{/rb}{rt}へびなた{/rt}"
        missing = findings(source, "헤비나타")
        unmapped = findings(source, "{rb}헤비나타{/rb}{rt}헤비나타{/rt}")
        self.assertIn("RUBY_STRUCTURE_MISMATCH", rule_ids(missing))
        self.assertIn("RUBY_UNMAPPED", rule_ids(unmapped))

    def test_roman_codepoint_is_exact(self):
        self.assertNotIn("ROMAN_NUMERAL_CHANGED", rule_ids(findings("第Ⅻ章", "제Ⅻ장")))
        self.assertIn("ROMAN_NUMERAL_CHANGED", rule_ids(findings("第Ⅻ章", "제12장")))
        self.assertIn("ROMAN_NUMERAL_CHANGED", rule_ids(findings("第Ⅻ章", "제XII장")))

    def test_quote_skeleton_and_balance(self):
        self.assertNotIn("JP_QUOTE_STYLE", rule_ids(findings("「行く」", "「갈게」")))
        self.assertIn("JP_QUOTE_STYLE", rule_ids(findings("「行く」", "“갈게”")))
        self.assertIn("JP_QUOTE_STYLE", rule_ids(findings("『女神』", "「여신」")))
        self.assertIn("TARGET_QUOTE_UNBALANCED", rule_ids(findings("行く", "「갈게")))

class ResidualWidthAndGlossaryPolicyTests(unittest.TestCase):
    def test_middle_dot_and_latin_names_are_not_japanese(self):
        items = findings("名前", "린카・미하루 Diana BGM_01.ttf")
        self.assertNotIn("RESIDUAL_KANA", rule_ids(items))
        self.assertNotIn("RESIDUAL_HANJA", rule_ids(items))

    def test_actual_kana_and_hanja_are_hard(self):
        self.assertIn("RESIDUAL_KANA", rule_ids(findings("名前", "미ハ루")))
        self.assertIn("RESIDUAL_HANJA", rule_ids(findings("名前", "이름 名前")))

    def test_fullwidth_target_is_hard_even_when_number_equal(self):
        equal = findings("１７歳", "１７살")
        self.assertIn("KO_WIDTH_STYLE", rule_ids(equal))
        self.assertNotIn("NUM_SEMANTIC_MISMATCH", rule_ids(equal))
        self.assertIn("NUM_SEMANTIC_MISMATCH", rule_ids(findings("１７歳", "18살")))

    def test_chan_token_boundary(self):
        self.assertTrue(audit.source_contains_term("チャンさん", "チャン"))
        self.assertFalse(audit.source_contains_term("チャンス", "チャン"))
        self.assertFalse(audit.source_contains_term("チャンホ", "チャン"))
        self.assertFalse(audit.source_contains_term("チャンネル", "チャン"))
        self.assertIn("CHAN_GLOSSARY_MISMATCH", rule_ids(findings("チャンさん", "그 사람")))
        self.assertNotIn("CHAN_GLOSSARY_MISMATCH", rule_ids(findings("チャンス", "기회")))

class GateAndAggregatePolicyTests(unittest.TestCase):
    def test_open_review_blocks_gate(self):
        items = findings("普通の文です", "Plain English prose")
        gate = audit.build_open_gate(items)
        self.assertGreater(gate["review_open"], 0)
        self.assertFalse(gate["pass"])
        for item in items:
            item["status"] = "approved"
        self.assertTrue(audit.build_open_gate(items)["pass"])

    def test_ui_exact_old_conflict(self):
        rows = [
            ("system_ui", {"stable_id": "ui:1", "source_jp": "戻る", "draft_ko": "돌아가기"}),
            ("system_ui", {"stable_id": "ui:2", "source_jp": "戻る", "draft_ko": "뒤로"}),
        ]
        items = []
        audit.audit_ui_old_key_conflicts(rows, items)
        self.assertIn("UI_GLOBAL_OLD_CONFLICT", rule_ids(items))

    def test_report_keeps_legacy_fields_and_adds_gate(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            master = root / "fixture.master.json"
            out = root / "audit_policy_fixture.json"
            master.write_text(json.dumps({"entries": [{
                "stable_id": "fixture:1",
                "sequence": 1,
                "source_jp": "「行く」",
                "draft_ko": "「갈게」",
                "english_reference_used": False,
                "external_translation_api_used": False,
            }]}, ensure_ascii=False), encoding="utf-8")
            report = audit.audit_master_directory(root, out)
            self.assertEqual(report["schema_version"], "fatal-twelve-consolidated-static-qa-v1")
            self.assertIn("severity_counts", report)
            self.assertIn("policy_severity_counts", report)
            self.assertIn("gate", report)
            self.assertTrue(out.exists())
            self.assertTrue(out.with_suffix(".tsv").exists())

    def test_report_uses_document_script_key_over_filename_prefix(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            master = root / "scenario_001.master.json"
            out = root / "audit_script_key_fixture.json"
            master.write_text(json.dumps({"script_key": "001", "entries": [{
                "stable_id": "fixture:script-key",
                "sequence": 1,
                "source_jp": "\u300cgo\u300d",
                "draft_ko": "go",
                "english_reference_used": False,
                "external_translation_api_used": False,
            }]}, ensure_ascii=False), encoding="utf-8")
            report = audit.audit_master_directory(root, out)
            self.assertTrue(report["issues"])
            self.assertEqual({item["script"] for item in report["issues"]}, {"001"})

if __name__ == "__main__":
    unittest.main()