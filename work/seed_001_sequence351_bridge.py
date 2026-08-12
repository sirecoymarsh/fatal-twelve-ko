from __future__ import annotations

import json
from pathlib import Path


out = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\translations\draft\scenario\001_sequence351_bridge.json")
entry = {
    "stable_id": "scenario/001.rpy::L1604",
    "sequence": 351,
    "translation_id": "f001_s1_end_4f5fe164",
    "translation_id_status": "exact_renpy_699_ast_hash",
    "source_file": "scenario/001.rpy",
    "source_line": 1604,
    "speaker": "narrator",
    "source_jp": "思わず、声を上げていた。",
    "draft_ko": "나도 모르게 목소리를 높였다.",
    "source_authority": "Japanese only",
    "english_reference_used": False,
    "status": "first_draft_unreviewed",
    "qa": "deferred_until_full_first_draft",
}
packet = {
    "packet_id": "scenario_001_sequence351_bridge",
    "source_language": "Japanese",
    "target_language": "Korean",
    "entry_count": 1,
    "translation_id_alignment": "exact Ren'Py 6.99 AST-derived ID",
    "status": "first_draft_unreviewed",
    "qa_policy": "No translation QA until the complete first draft is finished; review once afterward.",
    "english_text_in_translator_packet": False,
    "entries": [entry],
}
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(out)
