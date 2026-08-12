
from __future__ import annotations
import hashlib, json, re, shutil
from pathlib import Path

WS = Path(r"C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc")
OUT = WS / "work" / "system_ui" / "runtime_application"
SYSUI = WS / "work" / "system_ui"
PROJECT = Path(r"P:\AI\Codex\projects\fatal-twelve-ko")
ENGINE = Path(r"F:\DOWN\Fatal.Twelve.Incl.DLC\Fatal.Twelve.Incl.DLC\Fatal Twelve")
REN = ENGINE / "renpy"
GAMEDATA = PROJECT / "work" / "extracted" / "system" / "gamedata.rpy"

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def load_jsonl(path):
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]

def q(s):
    return json.dumps(s, ensure_ascii=False)

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")

def evidence(rel, start, end, purpose):
    path = REN / rel
    lines = path.read_text(encoding="utf-8").splitlines()
    return {
        "engine_file": "renpy/" + rel.replace("\\", "/"),
        "engine_sha256": sha(path),
        "line_start": start,
        "line_end": end,
        "purpose": purpose,
        "excerpt": [{"line": i, "text": lines[i-1]} for i in range(start, end + 1)],
    }

screens = load_jsonl(SYSUI / "screens.catalog.jsonl")
script = load_jsonl(SYSUI / "script.catalog.jsonl")
all_rows = screens + script

def getrow(key, lane=None):
    hits = [r for r in all_rows if r["lookup_key"] == key and (lane is None or r["lane"] == lane)]
    if not hits:
        raise KeyError((key, lane))
    return hits[0]

direct_keys = ["日本語", "English", "Numeral ", " - ", "to be continued..."]
base_rows = [r for r in script if r["lane"] == "base_none_strings"]
assert len(base_rows) == 8
translation_rows, seen = [], set()
for key in direct_keys:
    r = getrow(key)
    if key not in seen:
        translation_rows.append((key, r["draft_ko"]))
        seen.add(key)
for r in base_rows:
    if r["lookup_key"] not in seen:
        translation_rows.append((r["lookup_key"], r["draft_ko"]))
        seen.add(r["lookup_key"])
assert len(translation_rows) == 13

gm = GAMEDATA.read_text(encoding="utf-8")
m = re.search(r"define card_rnumbers\s*=\s*\{(?P<body>.*?)\}\s*\n\s*\ndefine character_info", gm, re.S)
assert m
number_map = dict(re.findall(r'"(\d+)"\s*:\s*"([^"]+)"', m.group("body")))
cm = re.search(r"define character_info\s*=\s*\{(?P<body>.*?)\}\s*\n\s*\ndefine cards", gm, re.S)
assert cm
used_numbers = sorted(set(re.findall(r'card_rnumbers\["(\d+)"\]', cm.group("body"))), key=int)
assert used_numbers == [str(i) for i in range(1, 13)]
suffixes = [number_map[i] for i in used_numbers]
numeral_row = getrow("Numeral ", "direct_literal")
prefix_ko = numeral_row["draft_ko"]
supplemental_pairs = [("Numeral " + s, prefix_ko + s) for s in suffixes]

skeleton = [
    "# Add-only runtime supplement for the composed Numeral label.",
    "# Existing code evaluates the prefix plus numeral before exact Text lookup.",
    "# Wording is copied unchanged from screens.draft.json.",
    "",
    "translate korean strings:",
]
for old, new in supplemental_pairs:
    skeleton += ["", "    old " + q(old), "    new " + q(new)]
write(OUT / "numeral_composed_string_keys.ko.rpy", "\n".join(skeleton) + "\n")

under_test = [
    "# Exact first-draft entries under runtime audit.",
    "",
    "translate korean strings:",
]
for old, new in translation_rows:
    under_test += ["", "    old " + q(old), "    new " + q(new)]
under_test_text = "\n".join(under_test) + "\n"

base_none = ["# Japanese base mappings from system/script.rpy.", "", "translate None strings:"]
for r in base_rows:
    base_none += ["", "    old " + q(r["lookup_key"]), "    new " + q(r["source_jp"])]
base_none_text = "\n".join(base_none) + "\n"

screen_source = """screen audit_directs(numeral=\"I\"):

    vbox:
        textbutton \"日本語\" action NullAction()
        textbutton \"English\" action NullAction()
        label \"Numeral \" + numeral
        text \" - \"
"""

direct_expected = {
    "textbutton_japanese": getrow("日本語")["draft_ko"],
    "textbutton_english": getrow("English")["draft_ko"],
    "text_separator": getrow(" - ")["draft_ko"],
    "python_text_continued": getrow("to be continued...")["draft_ko"],
}
base_expected = {r["lookup_key"]: r["draft_ko"] for r in base_rows}
numeral_old = "Numeral " + suffixes[0]
numeral_new = prefix_ko + suffixes[0]

def probe_script(expect_numeral):
    return """label audit_show_expression:

    show expression Text(\"to be continued...\", size=50)
    return

label start:

    python:
        import json
        import os
        import traceback

        renpy.game.preferences.language = \"korean\"

        def audit_text(value, substitute):
            d = renpy.text.text.Text(value, substitute=substitute)
            return unicode(d.text[0])

        direct_actual = {
            \"textbutton_japanese\": audit_text(%s, True),
            \"textbutton_english\": audit_text(%s, True),
            \"text_separator\": audit_text(%s, None),
            \"python_text_continued\": audit_text(%s, None),
            \"label_numeral_composed\": audit_text(%s, True),
        }

        direct_expected = %s
        base_expected = %s
        base_actual = { }
        for k in base_expected:
            base_actual[k] = unicode(renpy.translation.translate_string(k))

        result = {
            \"engine_version\": unicode(renpy.version),
            \"language\": unicode(renpy.game.preferences.language),
            \"direct_actual\": direct_actual,
            \"direct_expected\": direct_expected,
            \"base_actual\": base_actual,
            \"base_expected\": base_expected,
            \"direct_exact_four_pass\": all(direct_actual[k] == direct_expected[k] for k in direct_expected),
            \"numeral_composed_pass\": direct_actual[\"label_numeral_composed\"] == %s,
            \"base_eight_pass\": all(base_actual[k] == base_expected[k] for k in base_expected),
        }
        result[\"all_pass\"] = result[\"direct_exact_four_pass\"] and result[\"numeral_composed_pass\"] and result[\"base_eight_pass\"]

        fn = os.path.join(config.basedir, \"runtime_probe.json\")
        f = open(fn, \"wb\")
        try:
            payload = json.dumps(result, ensure_ascii=True, indent=2)
        except Exception:
            payload = json.dumps({ \"probe_exception\": traceback.format_exc() })
        f.write(payload)
        f.write(\"\\n\")
        f.close()

    $ renpy.quit()
""" % (
        repr("日本語"), repr("English"), repr(" - "), repr("to be continued..."),
        repr(numeral_old), repr(direct_expected), repr(base_expected), repr(expect_numeral),
    )

options = """define config.name = \"Fatal Twelve KO Runtime Application Audit\"
define config.version = \"audit\"
define config.save_directory = None
define config.developer = True
"""

for stage_name, patched in [("staging_baseline", False), ("staging_patched", True)]:
    game = OUT / stage_name / "game"
    tl = game / "tl" / "korean"
    tl.mkdir(parents=True, exist_ok=True)
    write(game / "options.rpy", options)
    write(game / "screens.rpy", screen_source)
    write(game / "base_none.rpy", base_none_text)
    write(game / "script.rpy", probe_script(numeral_new if patched else numeral_old))
    write(tl / "under_test.rpy", under_test_text)
    supplement_path = tl / "numeral_composed_string_keys.ko.rpy"
    if patched:
        shutil.copy2(OUT / "numeral_composed_string_keys.ko.rpy", supplement_path)
    elif supplement_path.exists():
        supplement_path.unlink()

direct_audit = [
    {
        "lookup_key": "日本語", "source": "system/screens.rpy:609",
        "simple_strings_entry_applies": True,
        "reason": "_textbutton defaults substitute=True; exact evaluated label is translated.",
        "minimal_add_only_action": "none",
    },
    {
        "lookup_key": "English", "source": "system/screens.rpy:610",
        "simple_strings_entry_applies": True,
        "reason": "_textbutton defaults substitute=True; exact evaluated label is translated.",
        "minimal_add_only_action": "none",
    },
    {
        "lookup_key": "Numeral ", "source": "system/screens.rpy:1062",
        "simple_strings_entry_applies": False,
        "reason": "_label translates after expression evaluation, so the exact key is Numeral I through Numeral XII, not the prefix.",
        "minimal_add_only_action": "add 12 exact composed pairs without overriding the screen",
        "supplement_file": "numeral_composed_string_keys.ko.rpy",
    },
    {
        "lookup_key": " - ", "source": "system/screens.rpy:1239",
        "simple_strings_entry_applies": True,
        "reason": "Text default substitute=None is not False, so Text invokes translation; source and draft happen to be identical.",
        "minimal_add_only_action": "none",
    },
    {
        "lookup_key": "to be continued...", "source": "system/script.rpy:1751",
        "simple_strings_entry_applies": True,
        "reason": "Python Text default substitute=None still invokes exact translation lookup.",
        "minimal_add_only_action": "none",
    },
]

consumer_map = {
    "Quick save complete.": ["renpy/common/00action_file.rpy:858", "renpy/common/00action_other.rpy:572"],
    "Are you sure you want to delete this save?": ["renpy/common/00gui.rpy:371", "Text translation path"],
    "Are you sure you want to overwrite your save?": ["renpy/common/00gui.rpy:372", "Text translation path"],
    "Loading will lose unsaved progress.\nAre you sure you want to do this?": ["renpy/common/00gui.rpy:373", "Text translation path"],
    "Are you sure you want to quit?": ["renpy/common/00gui.rpy:374", "Text translation path"],
    "Are you sure you want to return to the main menu?\nThis will lose unsaved progress.": ["renpy/common/00gui.rpy:375", "Text translation path"],
    "Image [index] of [count] locked.": ["system/screens.rpy:1873 explicit _()"],
    "Saved screenshot as %s.": ["renpy/common/00keymap.rpy:270 explicit __()"],
}
base_audit = []
for r in base_rows:
    base_audit.append({
        "lookup_key": r["lookup_key"], "source_jp": r["source_jp"], "draft_ko": r["draft_ko"],
        "simple_strings_entry_applies": True,
        "consumer_evidence": consumer_map[r["lookup_key"]],
        "reason": "Korean TranslateString registers and the runtime consumer translates the exact technical old key.",
    })

static = {
    "engine": {"version": "Ren'Py 6.99.14.3.3347", "root": str(ENGINE), "read_only": True},
    "source_hashes": {
        "screens.rpy": getrow("日本語")["source_sha256"],
        "script.rpy": getrow("to be continued...")["source_sha256"],
        "gamedata.rpy": sha(GAMEDATA),
        "screens.ko.rpy": sha(SYSUI / "screens.ko.rpy"),
        "script.ko.rpy": sha(SYSUI / "script.ko.rpy"),
    },
    "direct_literal_audit": direct_audit,
    "base_none_eight_audit": base_audit,
    "supplemental_composed_pairs": [{"old": a, "new": b} for a, b in supplemental_pairs],
    "engine_source_evidence": [
        evidence("translation\\__init__.py", 437, 447, "language-specific exact lookup"),
        evidence("substitutions.py", 204, 227, "substitution translates by default"),
        evidence("text\\text.py", 1444, 1467, "only substitute=False skips Text translation"),
        evidence("ui.py", 949, 988, "textbutton and label Text construction"),
        evidence("sl2\\sldisplayables.py", 115, 116, "screen text positional expression"),
        evidence("sl2\\sldisplayables.py", 196, 212, "screen textbutton and label expressions"),
        evidence("ast.py", 2207, 2237, "TranslateString registration"),
    ],
    "quality_review_performed": False,
    "translation_text_modified": False,
    "live_game_modified": False,
}
write(OUT / "runtime_application_static_audit.json", json.dumps(static, ensure_ascii=False, indent=2) + "\n")
write(OUT / "README.md", """# Ren'Py 6.99 Runtime Application Audit

Technical-only audit; translation wording was not reviewed or changed.

Files:
- runtime_application_static_audit.json: engine and AST evidence with verdicts.
- numeral_composed_string_keys.ko.rpy: minimal add-only supplement.
- staging_baseline: current simple entries only.
- staging_patched: current entries plus composed numeral keys.
- runtime_compile_probe_report.json: written after compile/runtime probes.

The live Fatal Twelve directory remains read-only.
""")
print(json.dumps({"prepared": True, "direct_entries": 5, "base_entries": 8, "supplemental_pairs": 12, "stages": 2}, indent=2))
