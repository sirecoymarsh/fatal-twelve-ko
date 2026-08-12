
from __future__ import annotations
import hashlib, json
from pathlib import Path

WS=Path(r"C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc")
ROOT=WS/"work"/"system_ui"/"runtime_application"
LIVE=Path(r"F:\DOWN\Fatal.Twelve.Incl.DLC\Fatal.Twelve.Incl.DLC\Fatal Twelve")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

baseline=load(ROOT/"staging_baseline"/"runtime_probe.json")
patched=load(ROOT/"staging_patched"/"runtime_probe.json")

expected_rpyc={
    "staging_baseline":[
        "game/base_none.rpyc","game/options.rpyc","game/screens.rpyc",
        "game/script.rpyc","game/tl/korean/under_test.rpyc",
    ],
    "staging_patched":[
        "game/base_none.rpyc","game/options.rpyc","game/screens.rpyc",
        "game/script.rpyc","game/tl/korean/under_test.rpyc",
        "game/tl/korean/numeral_composed_string_keys.ko.rpyc",
    ],
}
compile_stages={}
for stage, rels in expected_rpyc.items():
    files=[]
    for rel in rels:
        p=ROOT/stage/Path(rel)
        assert p.exists() and p.stat().st_size>0,p
        files.append({"path":rel.replace("\\","/"),"size":p.stat().st_size,"sha256":sha(p)})
    compile_stages[stage]={
        "command_exit_code":0,
        "compile_log":str(ROOT/stage/"compile.log"),
        "rpyc_count_expected":len(rels),
        "rpyc_files":files,
        "result":"PASS",
    }

decompiled_checks={
    "screen_direct_literals_preserved": all(x in (ROOT/"decompiled"/"baseline_screens.rpy").read_text(encoding="utf-8") for x in [
        'textbutton "日本語"','textbutton "English"','label "Numeral " + numeral','text " - "'
    ]),
    "python_text_expression_preserved": 'Text("to be continued...", size=50)' in (ROOT/"decompiled"/"baseline_script.rpy").read_text(encoding="utf-8"),
    "current_thirteen_entries_roundtrip": sum(1 for line in (ROOT/"decompiled"/"baseline_under_test.rpy").read_text(encoding="utf-8").splitlines() if line.strip().startswith("old "))==13,
    "supplement_twelve_entries_roundtrip": sum(1 for line in (ROOT/"decompiled"/"patched_numeral_composed.rpy").read_text(encoding="utf-8").splitlines() if line.strip().startswith("old "))==12,
}
assert all(decompiled_checks.values())
assert baseline["direct_exact_four_pass"] is True
assert baseline["base_eight_pass"] is True
assert baseline["direct_actual"]["label_numeral_composed"]=="Numeral I"
assert patched["direct_exact_four_pass"] is True
assert patched["base_eight_pass"] is True
assert patched["direct_actual"]["label_numeral_composed"]=="번호 I"
assert patched["all_pass"] is True

live_hashes={
    "scenario.rpa":sha(LIVE/"game"/"scenario.rpa"),
    "system.rpa":sha(LIVE/"game"/"system.rpa"),
}
assert live_hashes["scenario.rpa"]=="ea39387ae13432a79ffe4601af7b50478d063432ce3b7bc4013c92e09f036d22"
assert live_hashes["system.rpa"]=="a298b88f12c98435b015a647b51f5a35987ea4d714b5bf92e90972f3fcf6b648"

report={
    "result":"PASS",
    "engine":"Ren'Py 6.99.14.3.3347",
    "verdict":{
        "direct_literals":{
            "simple_entries_effective":4,
            "simple_entries_inert":1,
            "effective_keys":["日本語","English"," - ","to be continued..."],
            "inert_key":"Numeral ",
            "inert_reason":"The label expression is evaluated first and exact lookup sees Numeral I through Numeral XII.",
        },
        "base_translate_none_eight":{
            "simple_entries_effective":8,
            "runtime_probe_pass":True,
        },
    },
    "baseline_runtime":{
        "current_simple_entries_only":True,
        "direct_exact_four_pass":baseline["direct_exact_four_pass"],
        "base_eight_pass":baseline["base_eight_pass"],
        "numeral_actual":baseline["direct_actual"]["label_numeral_composed"],
        "numeral_remained_untranslated":baseline["direct_actual"]["label_numeral_composed"]=="Numeral I",
        "probe_file":"staging_baseline/runtime_probe.json",
    },
    "patched_runtime":{
        "minimal_add_only_supplement":"numeral_composed_string_keys.ko.rpy",
        "full_screen_override":False,
        "full_label_override":False,
        "composed_pairs_added":12,
        "direct_exact_four_pass":patched["direct_exact_four_pass"],
        "base_eight_pass":patched["base_eight_pass"],
        "numeral_actual":patched["direct_actual"]["label_numeral_composed"],
        "all_pass":patched["all_pass"],
        "probe_file":"staging_patched/runtime_probe.json",
    },
    "compile_stages":compile_stages,
    "compiled_ast_roundtrip":decompiled_checks,
    "engine_source_evidence_file":"runtime_application_static_audit.json",
    "live_original_hashes":live_hashes,
    "translation_quality_review_performed":False,
    "translation_wording_changed":False,
    "live_game_modified":False,
}
(ROOT/"runtime_compile_probe_report.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")

md="""# Fatal Twelve system UI runtime application audit

Result: **PASS**

## Verdict

- Direct display literals: four of five current string-table entries apply as written.
  - Effective: Japanese language label, English, separator, and to be continued.
  - Inert: Numeral prefix only. The label concatenates its suffix before Text performs exact lookup.
- All eight base translate-None technical keys apply through the Korean StringTranslator.
- Minimal fix: add the 12 exact composed keys Numeral I through Numeral XII.
- No screen override and no label override are required.
- Translation wording was copied unchanged; translation QA was not performed.

## Evidence

- Engine source excerpts and per-item paths: runtime_application_static_audit.json
- Baseline runtime probe: staging_baseline/runtime_probe.json
- Patched runtime probe: staging_patched/runtime_probe.json
- Isolated compile, AST, and hash report: runtime_compile_probe_report.json
- Add-only skeleton: numeral_composed_string_keys.ko.rpy

Both isolated projects compiled under Ren'Py 6.99.14.3.3347. The baseline left Numeral I unchanged; the patched stage produced 번호 I. All other audited direct literals and all eight base keys matched their existing first-draft values.
"""
(ROOT/"runtime_application_report.md").write_text(md,encoding="utf-8",newline="\n")

files=[
    "prepare_runtime_application.py","finalize_runtime_application.py",
    "runtime_application_static_audit.json","numeral_composed_string_keys.ko.rpy",
    "runtime_compile_probe_report.json","runtime_application_report.md","README.md",
    "staging_baseline/runtime_probe.json","staging_patched/runtime_probe.json",
]
manifest={rel:sha(ROOT/Path(rel)) for rel in files}
(ROOT/"runtime_application_hashes.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps(report,ensure_ascii=False,indent=2))
print(json.dumps(manifest,ensure_ascii=False,indent=2))
