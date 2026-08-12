# Fatal Twelve 한국어 패치

Fatal Twelve 본편·DLC를 위한 비공식 한국어화 프로젝트입니다.

번역은 **일본어 원문을 기준**으로 진행했으며, 공식 영어 번역문은 번역 입력으로 사용하지 않았습니다. 일본어·영어 언어 슬롯은 수정하지 않고 별도의 한국어 슬롯을 추가합니다.

## 현재 릴리스

- 버전: `1.0.0`
- 패치: `release/FatalTwelve_KoreanPatch_1.0.0.zip`
- SHA-256: `dae1890ffdad3010c16e4079fbd02424145b1e55ca8f76e475a1c45cdbdbb872`
- 구성: 컴파일된 `.rpyc` 32개와 해시 검증형 설치·복원 스크립트
- 원본 게임 실행 파일·아카이브·음원·이미지: **미포함**

## 설치

1. 게임을 완전히 종료합니다.
2. `release/FatalTwelve_KoreanPatch_1.0.0.zip`을 원하는 폴더에 풉니다.
3. Windows PowerShell 5.1에서 아래 명령을 실행합니다.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Install-KoreanPatch.ps1 -GameRoot "Fatal Twelve 게임 폴더"
```

4. `INSTALL PASS`가 표시되었는지 확인합니다.
5. 게임 환경 설정의 언어 항목에서 **한국어**를 선택합니다.

## 원상 복원

게임을 종료한 뒤 패치 폴더에서 실행합니다.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\Restore-KoreanPatch.ps1 -GameRoot "Fatal Twelve 게임 폴더"
```

`RESTORE PASS`가 표시되었는지 확인합니다.

설치기는 패치와 지원 대상 원본의 SHA-256을 먼저 검사합니다. 백업·상태·복구 사본은 기본적으로 LocalAppData의 별도 폴더에 보관됩니다. 알려진 원본과 다르면 설치 또는 복원을 시작하지 않습니다.

## 번역 및 검증 범위

- 시나리오 스크립트: 29개
- 시나리오 레코드: 18,184개
- 시스템 UI 레코드: 732개
- 최종 마스터 레코드: 18,916개
- 최종 전역 문자열 키: 797개
- 보호 토큰, 숫자, 로마 숫자, 루비 태그, Ren'Py 태그·보간, 인용부호 검사
- 한국어 글리프 커버리지 검사
- 격리 복사본에서 무음 컴파일
- 설치·복원·중단 복구 fixture 및 Windows Defender 검사
- 사용자 화면 검수 반영: 환경 설정 버튼을 `페이지 초기화`로 조정

## 저장소 구조

| 경로 | 내용 |
|---|---|
| `catalog/` | 일본어 권위 카탈로그와 구조 메타데이터 |
| `translations/` | 일본어 원문 기반 초벌·정렬 번역 |
| `work/final_qa/output/masters/` | QA 입력 마스터 |
| `work/final_qa/reviews/` | 최종 교정 매니페스트와 교정 레코드 |
| `work/final_qa/final_text_build_ui_feedback_v2/` | 사용자 UI 피드백까지 반영한 최종 텍스트 빌드 |
| `work/release_pipeline/` | 결정론적 패키지 빌더·설치/복원 테스트 |
| `release/evidence/` | v2 컴파일·패키지·Defender 검증 증거 |
| `release/` | 배포용 ZIP과 SHA-256 |

## 재현 관련 안내

텍스트 최종 적용의 중심 진입점은 다음과 같습니다.

```powershell
python .\work\final_qa\run_final_apply.py `
  --manifest .\work\final_qa\reviews\global_correction_manifest.json `
  --output-root .\work\final_qa\final_text_build_ui_feedback_v2
```

릴리스 컴파일에는 사용자가 합법적으로 보유한 지원 버전의 게임 설치본이 필요합니다. 엔진과 원본 게임 데이터는 저장소에 포함하지 않습니다.

## 권리 고지

Fatal Twelve와 원본 자산의 권리는 각 권리자에게 있습니다. 이 저장소는 원본 게임을 대체하지 않으며, 플레이하려면 정품 게임이 필요합니다. 별도 라이선스가 명시되지 않은 번역·도구·데이터의 이용 허가를 추정하지 마십시오.
