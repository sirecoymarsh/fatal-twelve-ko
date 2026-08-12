# Fatal Twelve 통합 번역 QA 프로토콜

## 적용 시점

- 29개 시나리오와 시스템 UI 초벌이 모두 완성된 뒤 한 번만 시행한다.
- 패킷별 초벌 검수와 영어 번역 대조는 하지 않는다.

## 번역 출처 계약

- 의미, 말투, 의성어·의태어, 문장 리듬의 유일한 기준은 일본어 `source_jp`다.
- 공식 영어 `new` 문장은 열거나 참조하지 않는다.
- 영어 리소스는 `old` 일본어 키 및 translation-ID membership 같은 기술 구조에만 사용할 수 있다.
- 외부 번역 API를 사용하지 않는다.

## 전수 확인 항목

1. 일본어 의미의 누락·추가·반전·주체 오인·시제 오인
2. 화자 관계에 맞는 존댓말/반말, 인물별 말버릇과 호칭
3. 자연스러운 한국어 어순·조사·띄어쓰기·대화 리듬
4. 일본어 의성어·의태어의 직접 해석; 영어식 `whoosh`, `ba-dump`, `tch`, `heh` 금지
5. 이름·지명·작품 고유 개념·에피소드 제목의 전역 일관성
6. 잔여 일본어, 빈 번역, 원문 복사, 깨진 문자, 과도한 직역
7. `「」`, `……`, 반복, 더듬거림, 문장 중단 등 연기 정보
8. `{rb}/{rt}` 등 태그, `[variable]`, `%` 치환, 이스케이프, 개행, 숫자·로마 숫자
9. 선택지 `old/new` 키, translation ID, voice/control/display tail 보존
10. 긴 문장·선택지·UI 레이블의 화면 길이 위험

## 수정 기록 형식

각 수정은 JSONL 한 줄로 기록한다.

```json
{"script":"001","stable_id":"...","sequence":1,"old_ko":"...","new_ko":"...","category":"meaning|tone|naturalness|term|sfx|typo|runtime|layout","reason":"일본어 원문 근거를 짧게 기술","reviewer":"..."}
```

- `old_ko`가 현재 master 값과 정확히 같을 때만 적용한다.
- 수정하지 않은 항목도 reviewer별 checked count로 전수 확인 사실을 보고한다.
- 구조 토큰을 바꾸는 수정은 별도 `runtime` 사유가 없으면 금지한다.

## 완료 판정

- 모든 master 레코드가 한 reviewer의 범위에 정확히 한 번 속한다.
- 모든 correction이 old-value guard를 통과한다.
- 수정 후 catalog coverage, ID, old-key, 보호 토큰, 일본어 잔존, 영어식 의성어 검사를 다시 수행한다.
- Ren'Py 6.99.14.3 staging compile 및 원본 archive 재해시까지 통과해야 최종 QA 완료로 본다.
