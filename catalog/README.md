# Fatal Twelve 일본어 원문 카탈로그 도구

이 폴더는 라이브 게임을 수정하지 않고 `scenario/001`을 일본어 원문 기준으로 카탈로그화한 연구 산출물이다.

## 고정 원칙

- 의미·문체의 유일한 번역 원문은 일본어다.
- 공식 영어 파일에서는 `translate english <ID>:`의 ID와 `translate english strings:`의 일본어 `old` 키 존재 여부만 읽는다.
- 영어 `new` 문장은 파싱·저장하지 않는다. 의성어, 감탄사, 문장부호 리듬, 캐릭터 말투 자료로 쓰지 않는다.
- 원문과 영어 블록을 순서대로 `zip`하지 않는다.
- 라이브 게임 `F:\DOWN\Fatal.Twelve.Incl.DLC\Fatal.Twelve.Incl.DLC\Fatal Twelve`는 읽기만 했고 수정하지 않았다.

## 정확한 ID 정렬

게임에 포함된 Ren'Py 6.99 코드의 알고리즘을 그대로 재현한다.

```text
Ren'Py digest = md5(concat(AST.get_code().encode("utf-8") + CRLF))[:8]
translation ID = current_label.replace(".", "_") + "_" + digest
```

대사 직전의 `voice get_voice_filename(...)`은 같은 AST 번역 그룹에 포함한다. 동일 ID가 다시 나오면 Ren'Py 규칙대로 `_1`, `_2`를 붙인다. 선택지와 메뉴 캡션은 Say ID 순서에서 제외하고, 일본어 `old` 키의 정확 일치만 확인한 뒤 별도 menu stable ID를 부여한다.

이 방식으로 `scenario/001`의 현재 Say ID 835개가 공식 ID 집합에 **835/835 정확히 존재**한다. 공식 영어 쪽에만 남은 orphan ID 9개는 이후 행을 밀지 않고 별도 진단한다.

첫 메뉴는 카탈로그 308–310번이다. 그러므로 단순 순서 정렬이라면 어긋나는 351번도 다음처럼 고정된다.

- catalog 350: `rinka`, `f001_s1_end_1db4df46`
- catalog 351: narrator, `f001_s1_end_4f5fe164`, `思わず、声を上げていた。`
- catalog 352: narrator, `f001_s1_end_6972cae2`
- catalog 353: `rinka`, `f001_s1_end_83c28cd0`

상세 근거는 `sequence_351_alignment_evidence.json`에 있다. 각 JSONL 행에도 `alignment.method`, `alignment.confidence`, source/group SHA-256, Ren'Py digest, `sequence_alignment_used=false`가 들어 있다.

## JSONL 핵심 필드

- `stable_id`: `scenario.rpa::scenario/001.rpy::tid::<translation_id>` 또는 source-stable menu ID
- `source`: 일본어, 원본 라인, label, statement/group code, SHA-256, Ren'Py digest
- `speaker`: 화자 코드, 일본어 표시명, 상속 정보, voice tag, 정의 위치
- `voice_call`: 호출문, tag, 명시 start count, 동적 파일 패턴 `sounds/voice/{tag}_{counter:05d}.ogg`
- `runtime_context`: `set_info_*`와 마지막 `scene` 상태
- `context`: 앞뒤 일본어 표시문 2개
- `protected_tokens`: Ren'Py 태그, 보간, printf, 숫자, 소스 escape
- `alignment`: AST 해시 또는 old-key 정확 일치의 증거와 confidence
- `translation.text_ko`: 현재 `null`; 번역기가 일본어만 보고 채울 자리

## 생성 명령

```powershell
python .\build_catalog.py `
  --source-rpy "P:\AI\Codex\projects\fatal-twelve-ko-audit\work\extracted\scenario\scenario\001.rpy" `
  --script-path "scenario/001.rpy" `
  --characters-rpy "P:\AI\Codex\projects\fatal-twelve-ko-audit\work\extracted\system\characters.rpy" `
  --reference-rpy "P:\AI\Codex\projects\fatal-twelve-ko-audit\work\extracted\tl\tl\english\scenario\001.rpy" `
  --output .\scenario_001.catalog.jsonl `
  --meta-output .\scenario_001.catalog.meta.json
```

## 검증 명령

```powershell
python .\validate_catalog.py .\scenario_001.catalog.jsonl `
  --meta .\scenario_001.catalog.meta.json `
  --source-rpy "P:\AI\Codex\projects\fatal-twelve-ko-audit\work\extracted\scenario\scenario\001.rpy" `
  --script-path "scenario/001.rpy" `
  --characters-rpy "P:\AI\Codex\projects\fatal-twelve-ko-audit\work\extracted\system\characters.rpy" `
  --reference-rpy "P:\AI\Codex\projects\fatal-twelve-ko-audit\work\extracted\tl\tl\english\scenario\001.rpy" `
  --output .\scenario_001.validation.json

python .\test_alignment_regression.py
```

`validate_catalog.py`는 원문에서 844개 행을 다시 만들어 stable ID, 화자, 음성, 문맥, 태그, 해시, 영어 미유입 정책을 대조한다. 번역 후에는 `--require-translated`를 추가하면 빈 한국어를 실패 처리한다. 영문식 SFX 후보(`ba-dump`, `clunk`, `whoosh`, `tch`, `heh`, `waugh`)는 경고한다.

## RPA provenance

`rpa_read.py`는 클래스 로딩을 금지한 restricted unpickler로 RPA-3.0 인덱스를 읽고 지정 항목만 연구 폴더로 추출한다. 경로 탈출, 중복 정규화 경로, 범위 밖 offset/length를 거부한다.

- `scenario.rpa`: 29 entries, SHA-256 `ea39387ae13432a79ffe4601af7b50478d063432ce3b7bc4013c92e09f036d22`
- `tl.rpa`: 35 entries, SHA-256 `ad628d5aa7b0601e69fa99c13d6f67c21854ae0a290599dc478a986cfc53ac5f`
- `scenario/001.rpyc`: SHA-256 `35218998032fd91e3ba60ed801cf6675526542e0f5ae348a0364c346699bce61`
- `tl/english/scenario/001.rpyc`: SHA-256 `c816af99c053dfa6bf90cc334d7b48e6aca7cae8d3c3c4057c2a029180a041ed`

## 현재 결과

- 총 844 records
- narration 461, dialogue 374, dialogue choice prompt 1
- choice prompt 2, narrative choice 4, spoken choice 2
- voice calls 372
- 보호 토큰: Ren'Py tags 48, numbers 99, source literal escape 1
- 공식 reference presence 843, missing 1
- source Say ID missing in official reference 0
- official orphan translation IDs 9
- 검증: errors 0, warnings 0

남은 reference missing 1건은 세 번째 메뉴의 voiced speaker prompt `「いいよ。このままで、もうしばらく」`이다. 공식 영어 `strings`에도 없지만 일본어 원문에는 보이므로 번역 대상에서 제외하지 않았다.
