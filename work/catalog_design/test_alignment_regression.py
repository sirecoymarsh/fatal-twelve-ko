#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ROWS = [json.loads(line) for line in (ROOT / "scenario_001.catalog.jsonl").read_text(encoding="utf-8").splitlines()]
META = json.loads((ROOT / "scenario_001.catalog.meta.json").read_text(encoding="utf-8"))

assert len(ROWS) == 844
assert [r["command_index"] for r in ROWS] == list(range(1, 845))
assert len({r["stable_id"] for r in ROWS}) == 844
assert sum(r["localization"]["translation_id"] is not None for r in ROWS) == 835
assert sum(r["localization"]["menu_key"] is not None for r in ROWS) == 9
assert sum(r["voice_call"] is not None for r in ROWS) == 372
assert all(r["alignment"]["sequence_alignment_used"] is False for r in ROWS)
assert all(r["alignment"]["reference_prose_used"] is False for r in ROWS)

# Regression lock: the first menu is a Ren'Py strings lane and must not shift
# later Say/translation IDs.
assert ROWS[307]["source"]["line"] == 1356
assert ROWS[307]["localization"]["translation_id"] is None
assert ROWS[307]["localization"]["menu_key"].startswith("001:prompt:")
assert ROWS[308]["localization"]["menu_key"].startswith("001:choice:")
assert ROWS[309]["localization"]["menu_key"].startswith("001:choice:")

row351 = ROWS[350]
assert row351["source"]["line"] == 1604
assert row351["source"]["text_ja"] == "思わず、声を上げていた。"
assert row351["speaker"] is None
assert row351["localization"]["translation_id"] == "f001_s1_end_4f5fe164"
assert row351["alignment"]["method"] == "renpy-6.99-ast-code-digest"
assert row351["alignment"]["confidence"] == "exact"

assert META["diagnostics"]["source_translation_ids_missing_reference"] == []
assert len(META["diagnostics"]["reference_orphan_translation_ids"]) == 9
assert META["diagnostics"]["source_old_keys_missing_reference_stable_ids"] == [
    "scenario.rpa::scenario/001.rpy::menu::003:spoken_prompt:01:2012275126270fff"
]
assert META["diagnostics"]["orphan_voice_calls"] == []

catalog_bytes = (ROOT / "scenario_001.catalog.jsonl").read_bytes()
assert hashlib.sha256(catalog_bytes).hexdigest() == META["catalog"]["sha256"]
json.loads((ROOT / "catalog.schema.json").read_text(encoding="utf-8"))
json.loads((ROOT / "catalog_contract.json").read_text(encoding="utf-8"))

scenario_index = json.loads((ROOT / "provenance/scenario.rpa.index.json").read_text(encoding="utf-8"))
tl_index = json.loads((ROOT / "provenance/tl.rpa.index.json").read_text(encoding="utf-8"))
assert scenario_index["archive"]["entry_count"] == 29
assert tl_index["archive"]["entry_count"] == 35
assert scenario_index["archive"]["sha256"] == META["inputs"]["source_archive"]["sha256"]
assert tl_index["archive"]["sha256"] == META["inputs"]["reference_archive"]["sha256"]

print("PASS: 844 records; menu boundary and sequence 351 remain hash-aligned.")
