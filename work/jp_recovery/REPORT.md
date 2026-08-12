# Fatal Twelve 일본어 원문 Unicode 복원 보고서

## 결론

`scenario.rpa`와 `system.rpa`의 일본어는 손상되거나 Shift-JIS 바이트로 뭉개진 상태가 아니다. Ren'Py RPYC의 pickle 안에서 일본어가 `BINUNICODE`로 저장되어 있으며, unrpyc v2.0.3은 이를 **BOM 없는 UTF-8** `.rpy`로 정상 출력한다.

기존 모지바케는 원문이나 decompiler의 복원 실패가 아니라, UTF-8 출력 파일을 Windows ANSI/CP949·Latin-1로 열거나 콘솔 파이프의 입출력 인코딩이 서로 어긋나면서 생긴 **표시 계층의 오해석**이다.

영어 번역문은 일본어 복원·정렬·표현 판단에 사용하지 않았다.

## 신뢰 원본

라이브 게임 경로는 분석 중 읽기 전용으로만 사용했다.

| 파일 | 크기 | SHA-256 |
|---|---:|---|
| `F:\DOWN\Fatal.Twelve.Incl.DLC\Fatal.Twelve.Incl.DLC\Fatal Twelve\game\scenario.rpa` | 5,102,486 | `ea39387ae13432a79ffe4601af7b50478d063432ce3b7bc4013c92e09f036d22` |
| `F:\DOWN\Fatal.Twelve.Incl.DLC\Fatal.Twelve.Incl.DLC\Fatal Twelve\game\system.rpa` | 199,203,732 | `a298b88f12c98435b015a647b51f5a35987ea4d714b5bf92e90972f3fcf6b648` |

- 엔진: Ren'Py `6.99.14.3`
- 아카이브: `RPA-3.0`
- XOR 키: `42424242`
- `scenario.rpa` 인덱스: 29개, 모두 RPYC
- `system.rpa` 인덱스: 292개, 그중 RPYC 9개만 추출
- 원본 해시는 추출 전후 동일하며 `extraction_manifest.json`에 기록되어 있다.

## 재현 가능한 복원 절차

전체 절차는 다음 한 줄로 재실행할 수 있다.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc\work\jp_recovery\recover_japanese.ps1"
```

스크립트가 수행하는 단계는 다음과 같다.

1. `scenario.rpa`, `system.rpa`를 SHA-256으로 신뢰 원본과 대조한다.
2. `extract_rpa_readonly.py`가 원본을 `rb`로만 열어 RPYC를 작업 폴더로 추출한다.
3. unrpyc v2.0.3이 추출 사본 38개를 UTF-8 `.rpy`로 decompile한다.
4. `collect_japanese_strings.py`가 UTF-8 strict decode 후 일본어 문자열 카탈로그와 `scenario/001` 첫 30개 대사·내레이션 샘플을 만든다.
5. `inspect_rpyc_unicode.py`가 객체를 unpickle하지 않고 RPC2 slot 1의 zlib/pickle opcode를 검사해 Unicode 저장 방식을 검증한다.

사용 도구:

- Python `3.11.9`
- unrpyc `v2.0.3`
- unrpyc 커밋 `3ae8334ed71a05535927dcc559663d3aca51215b`
- `unrpyc.py` SHA-256 `66c1f014a1caa07e8372b0a36184ee8d24f0a88fa8084a69f92478e8f34ab05c`

## Unicode 증거

38개 RPYC 전체를 `pickletools`로 검사한 결과:

- 일본어를 담은 `BINUNICODE`: **18,273개**
- 일본어를 담은 `BINSTRING`/`SHORT_BINSTRING`: **0개**
- decompiled `.rpy`: **38/38개 UTF-8 strict decode 통과**
- U+FFFD replacement character: **0개**
- C1 제어문자(U+0080~U+009F): **0개**
- UTF-8 BOM: 없음

`scenario/001.rpyc`만 보면:

- RPYC SHA-256: `35218998032fd91e3ba60ed801cf6675526542e0f5ae348a0364c346699bce61`
- RPC2 slot 1 압축 크기: 106,207바이트
- AST pickle 비압축 크기: 346,018바이트
- `BINUNICODE`: 4,160개
- 그중 일본어 문자열: 834개
- 일본어 byte-string opcode: 0개
- 첫 일본어 opcode 위치: pickle offset 2,205
- 첫 값: `一つの結果に到達するまでの過程を、人は物語や人生と呼ぶ。`

`system.rpa`에서도 동일하다. 예를 들어 `characters.rpyc`의 `凛火`, `Ⅰの少女`, `黒髪の少女` 정의는 모두 `BINUNICODE`다.

## 모지바케 원인

unrpyc의 출력 코드는 `out_filename.open('w', encoding='utf-8')`이며, 실제 `scenario/001.rpy`도 UTF-8 strict decode에 성공한다. 다만 BOM이 없으므로 구형 도구가 자동 판별에 실패할 수 있다.

첫 글자 `一つ`의 실제 UTF-8 바이트는 다음과 같다.

```text
e4 b8 80 e3 81 a4
```

이를 UTF-8로 읽으면 `一つ`지만 Latin-1 계열로 잘못 읽으면 `ä¸€ã...` 형태가 되고, 한국어 Windows PowerShell 5.1의 기본 ANSI/CP949 또는 콘솔 캡처 변환을 거치면 다시 다른 모지바케가 된다. 따라서 이미 깨진 화면 문자열을 역변환하는 방식이 아니라 **원본 RPYC → Unicode AST → UTF-8 파일** 경로를 그대로 유지해야 한다.

안전한 읽기 예:

```powershell
$text = [IO.File]::ReadAllText($path, [Text.UTF8Encoding]::new($false, $true))
```

```python
text = Path(path).read_text(encoding="utf-8", errors="strict")
```

PowerShell 5.1의 `Get-Content` 기본 인코딩, Excel/메모장의 ANSI 자동 저장, 인코딩을 지정하지 않은 Python `open()`은 사용하지 않는다.

## 산출물

| 파일 | 용도 |
|---|---|
| `recover_japanese.ps1` | 해시 확인부터 추출·decompile·검증까지 전체 실행 |
| `extract_rpa_readonly.py` | RPA-3.0 읽기 전용 RPYC 추출 및 원본/페이로드 해시 기록 |
| `collect_japanese_strings.py` | UTF-8 일본어 문자열 카탈로그 및 30개 샘플 생성 |
| `inspect_rpyc_unicode.py` | RPC2/pickle Unicode opcode 증명 |
| `extraction_manifest.json` | 원본 및 추출 RPYC provenance |
| `unicode/japanese_strings.jsonl` | `scenario.rpa` 18,151개, `system.rpa` 653개 일본어 literal 토큰 |
| `unicode/unicode_catalog_summary.json` | 파일별 UTF-8·문자열 수·해시 요약 |
| `unicode/rpyc_unicode_evidence.json` | 38개 RPYC opcode/UTF-8 검증 증거 |
| `unicode/scenario_001_first_30.json` | 첫 30개 대사·내레이션 구조화 샘플 |
| `unicode/scenario_001_first_30.md` | 사람이 읽는 첫 30개 샘플 |
| `raw/` | 추출 RPYC와 정상 UTF-8 decompiled RPY 사본 |

카탈로그 token 수(18,151 + 653)와 pickle의 일본어 `BINUNICODE` 수(18,273)가 다른 이유는, 전자는 decompiled RPY의 문자열 literal만 세고 후자는 일본어가 포함된 Python expression/AST 메타데이터까지 센다는 점 때문이다.

이 산출물은 번역용 연구 사본이며 라이브 게임에 설치하거나 원본 RPA를 수정하지 않는다.
