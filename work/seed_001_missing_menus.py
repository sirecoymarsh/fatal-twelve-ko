from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\translations\draft\scenario")
JSON_OUT = ROOT / "001_missing_menus.json"
RPY_OUT = ROOT / "001_missing_menus.rpy"


ROWS = [
    (309, 1357, "scenario.rpa::scenario/001.rpy::menu::001:choice:02:1ae9c2adab467609", "001:choice:02:1ae9c2adab467609", "開いてみよう", "열어 보자", "narrative_choice"),
    (310, 1364, "scenario.rpa::scenario/001.rpy::menu::001:choice:03:21bbbb7d7d4c99e7", "001:choice:03:21bbbb7d7d4c99e7", "触らないでおこう", "건드리지 말자", "narrative_choice"),
    (506, 2232, "scenario.rpa::scenario/001.rpy::menu::002:choice:02:9c2d943d7000cde8", "002:choice:02:9c2d943d7000cde8", "売っちゃおう。", "팔아 버리자.", "narrative_choice"),
    (507, 2237, "scenario.rpa::scenario/001.rpy::menu::002:choice:03:913571c57537a6b2", "002:choice:03:913571c57537a6b2", "中を見てみよう。", "안을 살펴보자.", "narrative_choice"),
    (575, 2558, "scenario.rpa::scenario/001.rpy::menu::003:choice:02:42467f7e172d0ee1", "003:choice:02:42467f7e172d0ee1", "「恥ずかしいから……離して」", "「부끄러우니까…… 놓아 줘」", "spoken_choice"),
    (576, 2563, "scenario.rpa::scenario/001.rpy::menu::003:choice:03:dec59999ff9ca458", "003:choice:03:dec59999ff9ca458", "「わ、分かった」", "「아, 알겠어」", "spoken_choice"),
]


def q(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def main() -> None:
    entries = []
    for sequence, line, stable_id, menu_key, source_jp, draft_ko, lane in ROWS:
        entries.append(
            {
                "stable_id": stable_id,
                "sequence": sequence,
                "translation_id": None,
                "menu_key": menu_key,
                "translation_id_status": "exact_renpy_string_key",
                "source_file": "scenario/001.rpy",
                "source_line": line,
                "speaker": "narrator",
                "lane": lane,
                "source_jp": source_jp,
                "draft_ko": draft_ko,
                "source_authority": "Japanese only",
                "english_reference_used": False,
                "status": "first_draft_unreviewed",
                "qa": "deferred_until_full_first_draft",
            }
        )
    packet = {
        "packet_id": "scenario_001_missing_menus",
        "source_language": "Japanese",
        "target_language": "Korean",
        "entry_count": len(entries),
        "translation_id_alignment": "exact Ren'Py string old-key identity",
        "status": "first_draft_unreviewed",
        "qa_policy": "No translation QA until the complete first draft is finished; review once afterward.",
        "english_text_in_translator_packet": False,
        "entries": entries,
    }
    ROOT.mkdir(parents=True, exist_ok=True)
    JSON_OUT.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = ["# Japanese-source Korean first draft; unreviewed.", "translate korean strings:"]
    for row in entries:
        lines.extend(["", f"    old {q(row['source_jp'])}", f"    new {q(row['draft_ko'])}"])
    RPY_OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(entries)} exact menu-string drafts")
    print(JSON_OUT)
    print(RPY_OUT)


if __name__ == "__main__":
    main()
