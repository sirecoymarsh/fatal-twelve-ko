#!/usr/bin/env python3
"""Assemble a Japanese-catalog translation TSV range into exact JSON and RPY."""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import hashlib
import json
import re
import unicodedata
from pathlib import Path

from align_generic_source_only import render_rpy
from align_source_only_packets import catalog_speaker, file_info, read_jsonl, write_json

NUMBER_RE = re.compile(r'(?<![0-9])(?:[0-9]+(?:\.[0-9]+)?)(?![0-9])')


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_tsv(paths: list[Path]) -> dict[int, str]:
    result = {}
    for path in paths:
        for line_number, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
            if not line.strip():
                continue
            try:
                sequence_text, target = line.split('\t', 1)
            except ValueError as exc:
                raise ValueError(f'{path}:{line_number}: expected sequence TAB target') from exc
            # Some Say nodes contain simultaneous-speaker text with an embedded
            # newline. TSV cannot carry a physical newline in one record, so an
            # explicit JSON string payload is supported: json:"first\\nsecond".
            # Ordinary target strings remain byte-for-value values.
            if target.startswith('json:'):
                try:
                    decoded_target = json.loads(target[5:])
                except json.JSONDecodeError as exc:
                    raise ValueError(f'{path}:{line_number}: invalid json: target') from exc
                if not isinstance(decoded_target, str):
                    raise ValueError(f'{path}:{line_number}: json: target must decode to a string')
                target = decoded_target
            sequence = int(sequence_text)
            if sequence in result:
                raise ValueError(f'duplicate translation sequence {sequence}')
            if not target:
                raise ValueError(f'empty target at {path}:{line_number}')
            result[sequence] = target
    return result


def check_hard_tokens(record: dict, target: str) -> None:
    tags = collections.Counter(
        token['value'] for token in record['protected_tokens'] if token['severity'] == 'hard' and token['kind'] == 'renpy_text_tag'
    )
    for value, count in tags.items():
        if target.count(value) != count:
            raise ValueError(f"RenPy tag mismatch at {record['command_index']}: {value} expected {count}, got {target.count(value)}")
    number_values = [
        token['value'] for token in record['protected_tokens'] if token['severity'] == 'hard' and token['kind'] == 'number'
    ]
    arabic = collections.Counter()
    roman = collections.Counter()
    for value in number_values:
        normalized = unicodedata.normalize('NFKC', value)
        if re.fullmatch(r'[0-9]+(?:\.[0-9]+)?', normalized):
            arabic[normalized] += 1
        else:
            roman[value] += 1
    if arabic:
        target_numbers = collections.Counter(NUMBER_RE.findall(unicodedata.normalize('NFKC', target)))
        if arabic != target_numbers:
            raise ValueError(f"number token mismatch at {record['command_index']}: expected {arabic}, got {target_numbers}")
    for value, count in roman.items():
        if target.count(value) != count:
            raise ValueError(f"Roman numeral mismatch at {record['command_index']}: {value} expected {count}, got {target.count(value)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog', type=Path, required=True)
    parser.add_argument('--start', type=int, required=True)
    parser.add_argument('--end', type=int, required=True)
    parser.add_argument('--translations', type=Path, action='append', required=True)
    parser.add_argument('--output-json', type=Path, required=True)
    parser.add_argument('--output-rpy', type=Path, required=True)
    parser.add_argument('--style-guide', type=Path, required=True)
    parser.add_argument('--glossary', type=Path, required=True)
    args = parser.parse_args()

    catalog = read_jsonl(args.catalog)
    selected = [record for record in catalog if args.start <= record['command_index'] <= args.end]
    expected = list(range(args.start, args.end + 1))
    if [record['command_index'] for record in selected] != expected:
        raise ValueError('catalog range is not complete and contiguous')
    translations = read_tsv(args.translations)
    if sorted(translations) != expected:
        missing = sorted(set(expected) - set(translations))
        extra = sorted(set(translations) - set(expected))
        raise ValueError(f'translation range mismatch: missing={missing[:20]}, extra={extra[:20]}')

    entries = []
    for record in selected:
        sequence = record['command_index']
        target = translations[sequence]
        check_hard_tokens(record, target)
        entries.append(
            {
                'sequence': sequence,
                'command_index': sequence,
                'stable_id': record['stable_id'],
                'translation_id': record['localization']['translation_id'],
                'menu_key': record['localization']['menu_key'],
                'id_origin': record['localization']['id_origin'],
                'source_file': record['source']['script'],
                'source_line': record['source']['line'],
                'source_label': record['source']['label'],
                'lane': record['lane'],
                'speaker': catalog_speaker(record),
                'source_jp': record['source']['text_ja'],
                'source_statement_code': record['source']['statement_code'],
                'source_group_code': record['source']['group_code'],
                'source_text_sha256': record['source']['text_sha256'],
                'source_group_sha256': record['source']['group_sha256'],
                'voice_call': record['voice_call'],
                'protected_tokens': record['protected_tokens'],
                'draft_ko': target,
                'source_authority': 'Japanese only',
                'english_reference_used': False,
                'external_translation_api_used': False,
                'status': 'first_draft_unreviewed',
                'qa': 'deferred_until_full_first_draft',
            }
        )

    packet = {
        'schema_version': 'fatal-twelve-japanese-first-draft-v1',
        'packet_id': f"scenario_{Path(selected[0]['source']['script']).stem}_{args.start}_{args.end}",
        'source_file': selected[0]['source']['script'],
        'command_index_start': args.start,
        'command_index_end': args.end,
        'entry_count': len(entries),
        'source_language': 'Japanese',
        'target_language': 'Korean',
        'translation_basis': 'Codex internal model; Japanese source only',
        'source_authority': 'Japanese only',
        'english_reference_used': False,
        'external_translation_api_used': False,
        'translation_validation': 'not performed; full first-draft QA deferred',
        'structure_validation': 'exact AST IDs/menu keys; hard tokens; RPY group code',
        'status': 'first_draft_unreviewed',
        'qa': 'deferred_until_full_first_draft',
        'catalog': file_info(args.catalog),
        'style_guide': file_info(args.style_guide),
        'glossary': file_info(args.glossary),
        'translation_tsv_inputs': [file_info(path) for path in args.translations],
        'entries': entries,
    }
    write_json(args.output_json, packet)
    rpy_text, rpy_stats = render_rpy(entries, selected[0]['source']['script'])
    args.output_rpy.parent.mkdir(parents=True, exist_ok=True)
    args.output_rpy.write_text(rpy_text, encoding='utf-8')
    result = {
        'schema_version': 'fatal-twelve-range-assembly-result-v1',
        'generated_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
        'output_json': file_info(args.output_json),
        'output_rpy': file_info(args.output_rpy),
        'entries': len(entries),
        'range': [args.start, args.end],
        'translation_ids': sum(entry['translation_id'] is not None for entry in entries),
        'menu_keys': sum(entry['menu_key'] is not None for entry in entries),
        'rpy_structure': rpy_stats,
        'hard_token_check': 'passed',
        'source_authority': 'Japanese only',
        'English_prose_used': False,
        'translation_QA_performed': False,
    }
    result_path = args.output_json.with_suffix('.assembly.json')
    write_json(result_path, result)
    print(json.dumps({**result, 'assembly_report': str(result_path)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
