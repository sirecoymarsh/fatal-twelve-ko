from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


STYLE_PATH = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\style_guide.md")
STYLE_SHA = "b2b87352fdfd9b25af688152b0ce8a7460ffeb88fc06ae6e45f1c5df2ae83891"
GLOSSARY_PATH = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\glossary_draft.json")
GLOSSARY_SHA = "d7b49d77fcde5da240cb816890c75f9f15a2e83544db34a6193b8e939906300e"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build an exact-ID Japanese-only Korean first-draft packet."
    )
    parser.add_argument("--catalog", type=Path, required=True)
    parser.add_argument("--source-rpy", type=Path, required=True)
    parser.add_argument("--translations", type=Path, required=True)
    parser.add_argument("--out-json", type=Path, required=True)
    parser.add_argument("--packet-id", required=True)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records = [
        json.loads(line)
        for line in args.catalog.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    raw_translations = json.loads(args.translations.read_text(encoding="utf-8"))
    if isinstance(raw_translations, list):
        translations = {i + 1: value for i, value in enumerate(raw_translations)}
    else:
        translations = {int(key): value for key, value in raw_translations.items()}

    command_indices = [record["command_index"] for record in records]
    assert command_indices == list(range(1, len(records) + 1))
    assert set(translations) == set(command_indices)
    assert all(isinstance(value, str) and value for value in translations.values())
    assert len({record["stable_id"] for record in records}) == len(records)

    entries = []
    lane_counts: Counter[str] = Counter()
    voice_count = 0
    menu_count = 0
    rpy_blocks: list[str] = [
        f"# Auto-generated Korean first draft: {args.packet_id}",
        "# Semantic source: Japanese only. Prose QA is deferred.",
        "# Translation engine: Codex internal model; no external translation API.",
        "# status: first_draft_unreviewed",
        "# qa: deferred_until_full_first_draft",
        "",
    ]
    menu_pairs: list[tuple[str, str, int]] = []

    for record in records:
        sequence = record["command_index"]
        source = record["source"]
        target = translations[sequence]
        speaker = record["speaker"]["code"] if record["speaker"] else None
        voice = record["voice_call"]
        protected = record["protected_tokens"]
        for token in protected:
            value = token["value"]
            assert source["text_ja"].count(value) == target.count(value), (
                sequence,
                value,
                source["text_ja"],
                target,
            )
        layout = record["layout"]
        if layout["starts_with_corner_quote"]:
            assert target.startswith("「"), (sequence, target)
        if layout["ends_with_corner_quote"]:
            assert target.endswith("」"), (sequence, target)

        lane_counts[record["lane"]] += 1
        if voice:
            voice_count += 1
        menu_key = record["localization"]["menu_key"]
        if menu_key:
            menu_count += 1
            menu_pairs.append((source["text_ja"], target, sequence))

        entry = {
            "sequence": sequence,
            "stable_id": record["stable_id"],
            "translation_id": record["localization"]["translation_id"],
            "translation_id_origin": record["localization"]["id_origin"],
            "translation_id_exactness": (
                "exact_japanese_string_identity"
                if menu_key
                else "exact_recomputed_renpy_6_99_japanese_canonical_code"
            ),
            "menu_key": menu_key,
            "source_file": source["script"],
            "source_line": source["line"],
            "source_label": source["label"],
            "item_type": record["lane"],
            "speaker": speaker or "narrator",
            "speaker_name_jp": (
                record["speaker"]["display_name_ja"] if record["speaker"] else None
            ),
            "source_jp": source["text_ja"],
            "source_statement": source["statement_code"],
            "source_group_code": source["group_code"],
            "voice_call": voice["statement"] if voice else "",
            "voice_line": voice["line"] if voice else None,
            "menu_context": record["menu_context"],
            "protected_tokens": protected,
            "draft_ko": target,
            "source_authority": "Japanese only",
            "english_reference_used": False,
            "external_translation_api_used": False,
            "translation_engine": "Codex internal model",
            "status": "first_draft_unreviewed",
            "qa": "deferred_until_full_first_draft",
        }
        entries.append(entry)

        if not menu_key:
            rpy_blocks.extend(
                [
                    f"# sequence: {sequence}",
                    f"# source: {source['script']}:{source['line']}",
                    f"# source_jp: {source['text_ja']}",
                    f"translate korean {entry['translation_id']}:",
                ]
            )
            if voice:
                rpy_blocks.append(f"    {voice['statement']}")
            statement = json.dumps(target, ensure_ascii=False)
            rpy_blocks.append(f"    {speaker + ' ' if speaker else ''}{statement}")
            rpy_blocks.append("")

    if menu_pairs:
        rpy_blocks.extend(["translate korean strings:", ""])
        for old, new, sequence in menu_pairs:
            rpy_blocks.extend(
                [
                    f"    # sequence: {sequence}",
                    f"    old {json.dumps(old, ensure_ascii=False)}",
                    f"    new {json.dumps(new, ensure_ascii=False)}",
                    "",
                ]
            )

    packet = {
        "packet_id": args.packet_id,
        "source_file": records[0]["source"]["script"],
        "sequence_start": command_indices[0],
        "sequence_end": command_indices[-1],
        "source_line_start": records[0]["source"]["line"],
        "source_line_end": records[-1]["source"]["line"],
        "entry_count": len(entries),
        "item_counts": dict(sorted(lane_counts.items())),
        "voice_count": voice_count,
        "menu_count": menu_count,
        "semantic_source_language": "Japanese",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "translation_engine": "Codex internal model",
        "translation_id_method": (
            "Ren'Py 6.99 canonical Japanese AST digest; menus use exact Japanese string identity"
        ),
        "status": "first_draft_unreviewed",
        "qa": "deferred_until_full_first_draft",
        "style_guide": {"path": str(STYLE_PATH), "sha256": STYLE_SHA},
        "glossary": {"path": str(GLOSSARY_PATH), "sha256": GLOSSARY_SHA},
        "inputs": {
            "japanese_rpy": {
                "path": str(args.source_rpy),
                "sha256": sha256(args.source_rpy),
            },
            "japanese_only_catalog": {
                "path": str(args.catalog),
                "sha256": sha256(args.catalog),
            },
            "translation_seed": {
                "path": str(args.translations),
                "sha256": sha256(args.translations),
            },
        },
        "entries": entries,
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(
        json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    out_rpy = args.out_json.with_suffix(".rpy")
    out_rpy.write_text("\n".join(rpy_blocks), encoding="utf-8")
    print(
        json.dumps(
            {
                "json": str(args.out_json),
                "rpy": str(out_rpy),
                "entries": len(entries),
                "lanes": dict(lane_counts),
                "voices": voice_count,
                "menus": menu_count,
                "json_sha256": sha256(args.out_json),
                "rpy_sha256": sha256(out_rpy),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
