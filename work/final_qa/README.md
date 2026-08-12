# Fatal Twelve 통합 구조·리뷰·교정 파이프라인

이 디렉터리의 도구는 exact Ren'Py 카탈로그와 일본어 원문을 구조 기준으로 사용한다. 명시적인 correction JSONL 이외에는 한국어 번역문을 수정하지 않는다.

## 1. Master draft 생성

```powershell
python .\work\final_qa\build_master_draft.py --require-complete
```

`packet_manifest.json`에 29개 카탈로그와 모든 초벌 패킷 경로가 명시되어 있다. `path`가 `null`인 패킷은 pending placeholder이며, 완성 후 경로만 채워도 읽을 수 있다.

검증 항목:

- 카탈로그 29개, 총 18,184개 레코드
- command index 연속성, stable ID 유일성
- source Japanese, translation ID, menu key, protected-token 메타데이터
- packet occurrence 중복·누락
- 한국어 초벌의 hard token

산출물:

- `output/masters/scenario_*.master.json`
- `output/master_index.json`
- `output/coverage_report.json`
- `output/conflict_report.json`

scenario/001 L1604 중복은 manifest의 exact 패킷 경로와 번역 문자열 SHA-256이 모두 맞을 때만 선택한다. 두 후보는 충돌 보고서에 모두 보존한다.

## 2. 읽기 전용 reviewer 패킷

```powershell
python .\work\final_qa\export_review_packets.py
```

그룹 배정은 `review_group_manifest.json`에 고정되어 있다.

- A: `001`, `002`, `003`, `004`, BAD END 4개, `MIHARU_END`, `TRUE_END`, `UNHAPPY_END`
- B: `005_1`, `005_2`, `006`, `011_01`, `011_01F`, `011_01G`, `011_01H`
- C: `007_1`, `007_2`, `008`, `NG_plus`
- ROOT: `009`, `010`, `011_02`, `011_02GH`, `012_01F`, `012_01GH`, `012_02`

각 TSV는 한 스크립트 안에서 sequence가 연속인 context chunk다. 가능한 경우 150–220개, 목표 약 185개로 균형 분할한다. 전체 스크립트가 150개 미만일 때만 하나의 short-script chunk를 허용한다. 서로 다른 스크립트는 같은 chunk에 넣지 않는다.

TSV는 UTF-8 BOM과 표준 인용 규칙을 사용한다. 필드는 다음을 포함한다.

- `sequence`, `stable_id`, `source_line`, `speaker`
- `source_jp`, `draft_ko`, `protected_tokens`
- `lane`, source/draft SHA-256

산출물:

- `review_packets/A`, `B`, `C`, `ROOT`
- `review_packets/review_packet_index.json`
- `review_packets/review_packet_coverage.json`

Exporter는 모든 TSV를 다시 읽어 source Japanese, Korean draft, protected tokens의 exact round trip과 레코드별 정확히 한 그룹·한 chunk 배정을 검사한다. 번역 검수는 수행하지 않는다.

## 3. Reviewer correction 적용

`apply_corrections.py`는 원본 master를 덮어쓰지 않고 별도의 working copy를 만든다. Reviewer별 JSONL 한 줄은 다음 형태다.

```json
{"stable_id":"...","old_ko":"현재 master와 정확히 같은 문자열","new_ko":"수정 문자열","script_key":"001","sequence":123,"note":"선택 메모"}
```

필수 필드는 `stable_id`, `old_ko`, `new_ko`다. `script_key`와 `sequence`는 선택적인 추가 exact guard다.

- `old_ko`는 공백 제거·Unicode 정규화 없이 현재 master와 완전히 같아야 한다.
- 같은 stable ID를 둘 이상의 reviewer 파일이나 줄에서 수정하면 수정안이 같아도 전체 실행을 거부한다.
- Reviewer는 자기 그룹에 배정된 스크립트만 수정할 수 있다.
- `new_ko`는 hard token, Ren'Py text tag, interpolation, percent-format token을 보존해야 한다.
- 모든 correction을 먼저 검증한 뒤에만 working copy를 기록한다.

```powershell
python .\work\final_qa\apply_corrections.py `
  --master-index .\work\final_qa\output\master_index.json `
  --review-groups .\work\final_qa\review_group_manifest.json `
  --correction A=.\reviews\A.jsonl `
  --correction B=.\reviews\B.jsonl `
  --correction C=.\reviews\C.jsonl `
  --correction ROOT=.\reviews\ROOT.jsonl `
  --output-root .\work\final_qa\corrected
```

Correction이 없는 reviewer 파일은 인수에서 생략할 수 있다. 단, 전체 실행에는 하나 이상의 correction JSONL이 필요하다.

산출물:

- `corrected/masters/*.master.json`: correction을 적용한 별도 working copy
- `corrected/correction_audit.json`: old/new 문자열·해시·reviewer·입력 줄·출력 master 해시
- `corrected/corrected_master_index.json`: 최종 renderer 입력 index

## 4. 최종 scenario RPY 렌더

```powershell
python .\work\final_qa\render_final_scenario.py `
  --master-index .\work\final_qa\corrected\corrected_master_index.json `
  --output-root .\work\final_qa\final_rpy
```

Renderer는 모든 corrected target의 runtime/protected token을 다시 검사한다. Dialogue와 narration은 다음 조건을 모두 만족해야 한다.

- `source_statement_code`가 `source_group_code`에 정확히 한 번 존재한다.
- 원문 string literal을 decoding한 값이 `source_jp`와 정확히 같다.
- string literal만 `draft_ko`로 교체한다.
- voice 호출, 다른 group command, statement tail은 그대로 보존한다.

Menu lane은 모든 스크립트에서 전역 수집해 `final_rpy/strings/scenario_strings.rpy` 하나로 만든다. 동일 old 문자열의 target이 exact 일치하면 한 번만 출력하고 모든 occurrence를 manifest에 기록한다. Target이 하나라도 다르면 전체 렌더를 거부한다.

산출물:

- `final_rpy/scenario/scenario_*.rpy`
- `final_rpy/strings/scenario_strings.rpy`
- `final_rpy/render_manifest.json`

## 5. Synthetic 테스트

실제 29개 master와 실제 번역문을 사용하지 않는 임시 fixture 테스트:

```powershell
python .\work\final_qa\tests\test_correction_render_pipeline.py
```

검사 범위:

- 정상 correction, working-copy 불변성, 최종 RPY 렌더
- stale `old_ko` exact guard 거부
- stable ID 중복 correction 거부
- 숫자 및 Ren'Py runtime tag 유실 거부
- source statement/group identity 불일치 거부
- 동일 global menu old key의 target 충돌 거부
- 동일 target menu occurrence의 정상 전역 deduplication

현재 결과:

- `tests/synthetic_test_report.json`
- `tests/synthetic_test_output.txt`

실제 correction 적용과 실제 최종 RPY 렌더는 reviewer correction이 준비된 뒤에만 실행한다.

## 6. Optional system UI master

`system_ui.master.json`을 scenario master index와 결합할 때는 corrected index reference의 `script_key`를 `system_ui`, `kind`를 `system_ui_strings`로 사용한다. Reviewer group manifest에서는 `system_ui`를 A에 배정한다.

Correction 도구는 system UI도 같은 `stable_id` + exact `old_ko` guard와 runtime/protected-token 검사를 적용해 별도 working copy로 만든다. Renderer는 system UI에 per-script RPY를 만들지 않고 732개 unique old key를 scenario menu와 함께 global strings lane에 수집한다. Scenario menu와 system UI 사이에서도 동일 old key의 target이 다르면 전체 렌더를 거부한다.
