#!/usr/bin/env python3
"""Exact-source align a complete source-only packet and render Korean RPY."""

from __future__ import annotations

import argparse
import ast
import copy
import datetime as dt
import json
from pathlib import Path

from align_source_only_packets import (
    CATALOG_SCHEMA,
    TRANSLATE_HEADER_RE,
    align_entry,
    aligned_document,
    build_index,
    catalog_speaker,
    file_info,
    match_catalog,
    normalize_source_file,
    normalize_speaker,
    read_json,
    read_jsonl,
    replace_statement_text,
    source_payload_hash,
    write_json,
)


def exact_or_unique_source_match(entry, catalog, index):
    try:
        return match_catalog(entry, index), 'source_file+source_line+speaker+exact Japanese source'
    except ValueError:
        candidates = [
            candidate
            for candidate in catalog
            if normalize_source_file(candidate['source']['script']) == normalize_source_file(entry['source_file'])
            and catalog_speaker(candidate) == normalize_speaker(entry.get('speaker'))
            and candidate['source']['text_ja'] == entry.get('source_jp')
        ]
        if len(candidates) != 1:
            raise ValueError(
                f"unique exact-source fallback returned {len(candidates)} records for "
                f"{entry.get('source_file')}:{entry.get('source_line')}"
            )
        return candidates[0], 'source_file+speaker+exact Japanese source unique fallback; packet line corrected'


def render_rpy(entries, script_name):
    lines = [
        f'# Fatal Twelve Korean aligned draft: {script_name}',
        '# Japanese source identity and RenPy 6.99 AST IDs; no English prose used.',
        '# draft_ko is copied value-for-value from source-only JSON; QA deferred.',
        '',
    ]
    say_ids = []
    menu_entries = []
    for entry in sorted(entries, key=lambda item: item['sequence']):
        translation_id = entry['translation_id']
        if translation_id is None:
            if entry['menu_key'] is None:
                raise ValueError(f"record has neither translation ID nor menu key: {entry['stable_id']}")
            menu_entries.append(entry)
            continue
        say_ids.append(translation_id)
        statement = entry['source_statement_code']
        group = entry['source_group_code']
        if statement not in group:
            raise ValueError(f"statement missing from group_code: {entry['stable_id']}")
        replaced = 0
        rendered_group = []
        for code_line in group:
            if code_line == statement:
                rendered_group.append(replace_statement_text(code_line, entry['source_jp'], entry['draft_ko']))
                replaced += 1
            else:
                rendered_group.append(code_line)
        if replaced != 1:
            raise ValueError(f"expected one statement replacement, got {replaced}: {entry['stable_id']}")
        lines.append(f'translate korean {translation_id}:')
        lines.append('')
        lines.extend(f'    {code_line}' for code_line in rendered_group)
        lines.append('')
        lines.append('')

    if menu_entries:
        lines.append('translate korean strings:')
        lines.append('')
        for entry in menu_entries:
            lines.append(f"    # {entry['menu_key']} | source line {entry['source_line']}")
            lines.append(f"    old {json.dumps(entry['source_jp'], ensure_ascii=False)}")
            lines.append(f"    new {json.dumps(entry['draft_ko'], ensure_ascii=False)}")
            lines.append('')

    text = '\n'.join(lines).rstrip() + '\n'
    parsed_ids = TRANSLATE_HEADER_RE.findall(text)
    if parsed_ids != say_ids or len(parsed_ids) != len(set(parsed_ids)):
        raise ValueError('rendered RPY translate IDs/order do not match aligned JSON')
    old_values = [ast.literal_eval(line.strip()[4:]) for line in text.splitlines() if line.strip().startswith('old ')]
    new_values = [ast.literal_eval(line.strip()[4:]) for line in text.splitlines() if line.strip().startswith('new ')]
    if old_values != [entry['source_jp'] for entry in menu_entries]:
        raise ValueError('rendered menu old strings/order mismatch')
    if new_values != [entry['draft_ko'] for entry in menu_entries]:
        raise ValueError('rendered menu new strings/order mismatch')
    return text, {
        'translate_blocks': len(say_ids),
        'strings_entries': len(menu_entries),
        'unique_translate_ids': len(set(say_ids)),
        'menu_lane_separate': True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--catalog', type=Path, required=True)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--rpy-output', type=Path, required=True)
    parser.add_argument('--coverage-output', type=Path, required=True)
    args = parser.parse_args()

    catalog = read_jsonl(args.catalog)
    index = build_index(catalog)
    source = read_json(args.input)
    original_entries = source['entries']
    before_draft = source_payload_hash(original_entries, 'draft_ko')
    before_source = source_payload_hash(original_entries, 'source_jp')
    aligned_entries = []
    matched_stable_ids = set()
    line_corrections = []
    for source_packet_ordinal, entry in enumerate(original_entries, 1):
        record, method = exact_or_unique_source_match(entry, catalog, index)
        stable_id = record['stable_id']
        if stable_id in matched_stable_ids:
            raise ValueError(f'duplicate source record in packet: {stable_id}')
        matched_stable_ids.add(stable_id)
        packet_line = int(entry['source_line'])
        catalog_line = int(record['source']['line'])
        normalized_entry = copy.deepcopy(entry)
        normalized_entry['source_line'] = catalog_line
        aligned_entry = align_entry(normalized_entry, record, source_packet_ordinal)
        aligned_entry['source_packet_source_line'] = packet_line
        aligned_entry['alignment']['join_evidence'].update(
            {
                'method': method,
                'source_packet_source_line': packet_line,
                'catalog_source_line': catalog_line,
                'source_line_exact_match': packet_line == catalog_line,
                'source_line_delta': catalog_line - packet_line,
            }
        )
        if packet_line != catalog_line:
            line_corrections.append(
                {
                    'source_packet_ordinal': source_packet_ordinal,
                    'source_packet_source_line': packet_line,
                    'catalog_source_line': catalog_line,
                    'delta': catalog_line - packet_line,
                    'stable_id': stable_id,
                }
            )
        aligned_entries.append(aligned_entry)

    catalog_stable_ids = {record['stable_id'] for record in catalog}
    missing = catalog_stable_ids - matched_stable_ids
    extra = matched_stable_ids - catalog_stable_ids
    if missing or extra:
        raise ValueError(f'packet is not complete for catalog: missing={len(missing)}, extra={len(extra)}')

    aligned = aligned_document(source, aligned_entries, args.catalog)
    aligned['complete_catalog_coverage'] = {
        'catalog_records': len(catalog),
        'matched_exact_source_records': len(matched_stable_ids),
        'missing_records': 0,
        'extra_records': 0,
    }
    aligned['source_line_alignment'] = {
        'exact_line_matches': len(aligned_entries) - len(line_corrections),
        'corrected_from_unique_exact_source': len(line_corrections),
        'corrections': line_corrections,
    }
    write_json(args.output, aligned)
    rpy_text, rpy_stats = render_rpy(aligned_entries, normalize_source_file(aligned_entries[0]['source_file']))
    args.rpy_output.parent.mkdir(parents=True, exist_ok=True)
    args.rpy_output.write_text(rpy_text, encoding='utf-8')

    reloaded = read_json(args.output)
    after_draft = source_payload_hash(reloaded['entries'], 'draft_ko')
    after_source = source_payload_hash(reloaded['entries'], 'source_jp')
    if before_draft != after_draft or before_source != after_source:
        raise ValueError('translation/source payload changed')

    line_summary = {
        'exact_line_matches': len(aligned_entries) - len(line_corrections),
        'corrected_from_unique_exact_source': len(line_corrections),
        'delta_counts': {
            str(delta): sum(item['delta'] == delta for item in line_corrections)
            for delta in sorted({item['delta'] for item in line_corrections})
        },
    }
    coverage = {
        'schema_version': 'fatal-twelve-generic-coverage-v1',
        'generated_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
        'catalog': file_info(args.catalog),
        'input': file_info(args.input),
        'aligned_json': file_info(args.output),
        'aligned_rpy': file_info(args.rpy_output),
        'catalog_records': len(catalog),
        'matched_exact_source_records': len(matched_stable_ids),
        'coverage_percent': 100.0,
        'missing_records': [],
        'extra_records': [],
        'translation_id_records': sum(entry['translation_id'] is not None for entry in aligned_entries),
        'menu_key_records': sum(entry['menu_key'] is not None for entry in aligned_entries),
        'menu_lane_separate': True,
        'source_line_alignment': line_summary,
        'rpy_structure': rpy_stats,
        'draft_ko_sha256_before': before_draft,
        'draft_ko_sha256_after': after_draft,
        'source_jp_sha256_before': before_source,
        'source_jp_sha256_after': after_source,
        'translation_text_modified': False,
        'translation_QA_performed': False,
    }
    write_json(args.coverage_output, coverage)
    manifest = {
        'schema_version': 'fatal-twelve-generic-alignment-result-v1',
        'created_at_utc': dt.datetime.now(dt.timezone.utc).isoformat(),
        'catalog_schema': CATALOG_SCHEMA,
        'catalog': file_info(args.catalog),
        'input': file_info(args.input),
        'output_json': file_info(args.output),
        'output_rpy': file_info(args.rpy_output),
        'coverage_report': file_info(args.coverage_output),
        'join': {
            'primary_keys': ['source_file', 'source_line', 'speaker'],
            'additional_assertion': 'source_jp exact equality',
            'unique_fallback': 'source_file+speaker+source_jp only when exactly one catalog record; source line corrected',
            'sequence_zip_used': False,
            'English_prose_used': False,
        },
        'records': len(aligned_entries),
        'draft_ko_sha256_before': before_draft,
        'draft_ko_sha256_after': after_draft,
        'source_jp_sha256_before': before_source,
        'source_jp_sha256_after': after_source,
        'translation_text_modified': False,
        'translation_QA_performed': False,
        'complete_catalog_coverage': True,
        'source_line_alignment': line_summary,
        'rpy_structure': rpy_stats,
    }
    manifest_path = args.output.with_suffix('.alignment.json')
    write_json(manifest_path, manifest)
    print(
        json.dumps(
            {
                'output_json': str(args.output),
                'output_rpy': str(args.rpy_output),
                'manifest': str(manifest_path),
                'coverage': str(args.coverage_output),
                'records': len(aligned_entries),
                'translation_text_modified': False,
                'translation_QA_performed': False,
                'rpy_structure': rpy_stats,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
