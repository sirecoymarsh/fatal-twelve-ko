# Fatal Twelve 한국어 패치

Fatal Twelve 본편·DLC를 위한 비공식 한국어화 프로젝트입니다.

번역은 **일본어 원문을 기준**으로 진행했으며, 공식 영어 번역문은 번역 입력으로 사용하지 않았습니다. 일본어·영어 언어 슬롯은 수정하지 않고 별도의 한국어 슬롯을 추가합니다.

## 현재 릴리스

- 버전: `1.0.0`
- 패치: `release/FatalTwelve_KoreanPatch_1.0.0.zip`
- SHA-256: `dae1890ffdad3010c16e4079fbd02424145b1e55ca8f76e475a1c45cdbdbb872`
- 구성: 컴파일된 `.rpyc` 32개와 해시 검증형 설치·복원 스크립트
- 원본 게임 실행 파일·아카이브·음원·이미지: **미포함**

## 추가·변경 사항

이 절은 원판 Fatal Twelve(DLC 포함 PC판, Ren'Py 6.99.14.3) 대비 이 패치가 더하거나 바꾼 것을 커밋·소스·기록 파일에서 찾아 정리한 것입니다. 괄호 안은 근거(커밋 해시, 파일 이름)이고, 확실하지 않은 것은 「(추정)」으로 표시했습니다.

> 중요: 아래 내용은 두 묶음으로 나뉩니다. **v1.0.0 ZIP**(`release/`)에는 시나리오·문자열 번역과 언어 선택기만 들어 있습니다. 플로우 차트, 특전 개방, 그림 글자·영상 한국어화, 11월 재번역은 `latest/` 폴더에 **설치본에서 가져온 소스로만** 올라와 있고, 아직 배포 ZIP으로 묶이지 않았습니다(1d7663b, a8cb692).

### 번역 범위

- **번역 원문**: 일본어 원문만 의미·문체의 기준으로 삼았습니다. 공식 영어판은 번역 ID·파일 정렬과 로마자 표기 확인에만 썼습니다(`reports/architecture/PATCH_ARCHITECTURE.md`).
- **본문·선택지**: 시나리오 스크립트 29개, 레코드 18,184개 전부입니다. 본편 1~12주차, 배드 엔딩 4종, 미하루 엔딩, 언해피 엔딩, 트루 엔딩, NG+(2회차) 시나리오를 포함합니다(`catalog/`, `latest/game/tl/korean/scenario/`).
- **시스템 UI**: v1.0.0에는 UI 레코드 732개와 전역 문자열 797개가 들어갔습니다. 설치본 기준 최신 UI 문자열 파일에는 744개 항목이 있습니다(`latest/game/tl/korean/ui_complete_strings.rpy`). 인물·장소·줄거리(plots) 데이터도 번역했습니다(`work/system_ui/`).
- **날짜 표시**: 화면의 `MM/DD (MON)` 형식 요일을 한국어일 때만 `(월)`처럼 바꿉니다. 일본어·영어에서는 원래 영어 요일을 그대로 씁니다(`latest/game/f12_ui_date_localization.rpy`).
- **그림 글자(이미지)**: 90장을 한국어로 다시 그렸습니다(a8cb692).
  - 엔딩 화면 7장(BADEND_01~04, MIHARUEND, TRUEEND, UNHAPPYEND), 엔딩 선택 버튼(bad01~04, good01~03의 idle/hover), 회상(다시보기) 썸네일 32장, 우클릭 메뉴의 시간대 표시 6장(이른 아침·아침·낮·저녁·밤·심야), NEW 아이콘, 타이틀 그림 `title_015`, `demo_last_bg`(추정: 체험판 끝 화면).
  - 배경 26장(병원 라운지, `lion02` 가게, 학교 복도·교문, 목욕탕, 역, 도쿄 타워, 전철 등의 간판·글자)과 이벤트 CG 2장(커피 우유 팩 `ecg coffee ole`, 린다의 일기 `ecg lindadiary op1`).
  - 우유 팩 CG는 흰 라벨과 파란 옆면만 한국어로 바꾸고, 아래쪽 작은 글씨는 원본 그대로 두었습니다(`latest/qol_opening_20261116/PROGRESS.json`).
- **영상**(영상 파일은 저장소에 없음, 기록만 있음):
  - 오프닝(OP): 일본어·영어 가사 아래에 한국어 가사 자막을 함께 넣었습니다. 영상 속 스태프 크레디트 17묶음을 검토해 8묶음은 원본 프레임에서 배경을 다시 복원한 뒤 한국어 크레디트를 넣었습니다. 전체 3,057프레임 중 813프레임을 고쳤습니다(`latest/qol_opening_20261116/opening_repair.json`, `render_opening.py`, `delivery/OP.ass`).
  - 엔딩 영상 3종(배드 엔딩 ED_BAD, 미하루·언해피 엔딩 ED_MHR_UNH, 트루 엔딩 ED_TRUE): 흘러가는 출연진·스태프 크레디트를 한국어(아래 작게 영어 병기)로, 주제가 가사를 일본어+한국어 2단 자막으로 넣었습니다(`latest/ending_localization/`).
  - 트루 엔딩 주제가 제목 「硝子の糸」는 사용자 지시로 「유리실」에서 「유리의 실」로 고쳤습니다(`TITLE_DECISION_v3.json`, 2026-10-04).
  - 오프닝·ED_MHR_UNH의 영어 가사 "I won't to live, In a limited time."는 사용자가 정한 문구 「남이 정한 시간 속에선 살고 싶지 않아」로 통일했습니다(OP 1곳, ED_MHR_UNH 3곳, `delivery/lyrics.json`).
  - 한국어 영상은 `game/tl/korean/movies/`에 따로 두어, 한국어일 때만 쓰이고 원본 `movies.rpa`는 건드리지 않습니다.
- **용어 통일**: 인명·지명·작품 용어표를 두고 번역했습니다(`glossary_draft.json`, `style_guide.md`, 아르곤 번역 프롬프트).

### 편의 기능 (원판에 없던 것)

- **언어 선택기**: 원판은 실행할 때마다 `localize.rpyc`가 언어를 영어로 되돌리고, 개발자 모드가 꺼져 있어 언어 메뉴가 숨겨져 있습니다. 패치는 환경 설정 → System 탭 여덟째 줄에 `언어 / 日本語 / English / 한국어` 행을 덧붙이고, 고른 언어를 따로 기억해 다시 실행해도 유지되게 했습니다. 처음 실행하면 한국어로 시작합니다(`f12_korean_bootstrap.rpy`).
- **플로우 차트**(v2, 2026-10-02 / 2026-11-16 수정, `latest/game/f12_flowchart.rpy`):
  - 특전(EXTRA) 화면에 갤러리·다시보기 옆 셋째 탭으로 들어갑니다. 1~12주차와 갈래(배드·미하루·언해피·트루 엔딩 줄기)를 색깔 띠로 나눈 장면 목록 228개입니다.
  - 게임 중 빠른 메뉴(자동·건너뛰기 옆)에 「플로우 차트」 버튼이 생겨, 지금 읽는 장면과 이번 회차에 고른 선택지를 보여 줍니다. 선택 기록은 세이브에 들어가 되감기하면 같이 되돌아갑니다. 차트 도입 전 세이브는 줄기 깃발로 확실한 것만 추정해 ▷ 표시합니다.
  - 읽은 장면을 골라 그 장면부터 다시보기할 수 있습니다. 다시보기는 격리 실행되어 다음 장면에서 끝나고, 진행 기록을 바꾸지 않습니다. 다시보기 중 다른 장면을 고르면 그 장면으로 옮겨 갑니다.
  - 차트에서 오프닝·엔딩 영상을 바로 재생할 수 있고, 클릭하면 건너뜁니다.
  - 장면 해금 기준은 그 장면의 마지막 줄을 읽었는지입니다.
- **특전 개방**(2026-11-16, `latest/game/f12_bonus_access.rpy`): 환경 설정에 `특전 / 특전 개방 / 개방 취소` 행을 추가했습니다. 켜면 갤러리 56묶음(138장), 회상 23개, 플로우 차트를 진행과 상관없이 미리 볼 수 있습니다. 미리 보는 동안에는 읽음 기록·엔딩 기록·선택 기록이 저장되지 않고 도전 과제도 주어지지 않습니다. 끄면 원래 해금 상태로 돌아갑니다.

### 단축키·조작

| 조작 | 동작 |
|---|---|
| 빠른 메뉴 「플로우 차트」 클릭 | 게임 중 플로우 차트 열기(대사창이 있을 때만) |
| 플로우 차트에서 마우스 휠 위/아래 | 주차 띠를 왼쪽/오른쪽으로 한 칸씩 이동 |
| 영상 재생 중 클릭 | 영상 건너뛰고 차트로 돌아가기 |

새 키보드 단축키는 추가하지 않았습니다(소스에서 찾은 키 바인딩은 마우스 휠뿐).

### 화면·글꼴

- 원판 대사 글꼴(mgenplus)과 메뉴 제목·날짜 글꼴(IPAex 명조, Charis SIL)에는 한글이 없어, 한국어일 때만 게임에 들어 있는 Noto Sans/Serif CJK로 바꿉니다. 줄바꿈 규칙도 한국어(띄어쓰기 기준)로 바꿉니다(`latest/game/tl/korean/f12_slot.rpy`).
- 한국어 글리프 누락 검사를 거쳤습니다(`work/final_qa/font_audit/`).
- 해상도·와이드·전체화면 관련 변경은 없습니다.

### 버그 수정

- 원판의 언어 강제(매 실행 영어로 고정)와 숨겨진 언어 메뉴를 우회했습니다(위 언어 선택기, `PATCH_ARCHITECTURE.md` 4장).
- 사용자 화면 검수: 환경 설정의 버튼 문구를 `페이지 초기화`로 고쳤습니다(`work/final_qa/final_text_build_ui_feedback_v2/`).
- 특전 「개방 취소」 뒤에도 플로우 차트가 계속 열려 있던 문제를 고쳤습니다. 옛 세이브에서도 처음 실행할 때 바로잡힙니다(2026-11-16, `latest/qol_opening_20261116/flowchart_cancel_fix/`).
- 작업용 1회성 보정 두 가지가 `latest/game/`에 있습니다. 배포본에는 넣지 않는 것입니다.
  - `f12_local_restore_skip_unseen_20261002.rpy`: 차트 시험 중 켜진 「안 읽은 글도 건너뛰기」를 한 번 끕니다(파일 안에 「배포본에 넣지 말 것」이라고 적혀 있음).
  - `f12_audio_restore_once.rpy`: 검수용 무음 설정을 한 번 되돌립니다(추정: 검수 빌드 전용).

### 설치·제거 방식

- 원본 파일을 바꾸지 않고 `game/tl/korean/` 등에 **파일을 더하는 방식**입니다. `scenario.rpa`, `system.rpa`, `tl.rpa`, `localize.rpyc`는 교체·재압축하지 않습니다. 번역이 빠진 줄은 영어가 아니라 일본어 원문으로 표시됩니다.
- v1.0.0 ZIP은 PowerShell 5.1 설치·복원 스크립트(`Install-KoreanPatch.ps1`, `Restore-KoreanPatch.ps1`)로 설치합니다. 먼저 `fatal.exe`와 rpa 4개의 SHA-256을 확인해 지원 원본(`fatal.exe` 386,048바이트)이 아니면 멈춥니다. 백업·상태 기록은 LocalAppData의 별도 폴더에 두며, 중단된 설치도 복구할 수 있습니다.
- ZIP은 두 번 빌드해 바이트 단위로 같은지 확인했고, Windows Defender 검사를 통과했습니다(`release/evidence/`).
- `latest/`의 플로우 차트·특전·그림·영상은 아직 설치 스크립트가 없습니다. 지금은 설치본 폴더(`game/`)에 같은 경로로 직접 넣는 형태입니다(추정).

### 판(버전)별 변경 기록

| 날짜 | 내용 | 근거 |
|---|---|---|
| 2026-08-10 | 원판 분석, 한국어 슬롯 추가 설계 | `reports/architecture/PATCH_ARCHITECTURE.md` |
| 2026-08-12 | **v1.0.0**: 시나리오 29개·UI 번역, 언어 선택기, 한국어 글꼴, 해시 검증 설치·복원 ZIP | 48af51d |
| 2026-09-27 | 그림 글자(배경·GUI) 한국어화 작업 시작(추정) | `build_fatal_endings.py` 안의 `raster_localization_20260927` 경로 |
| 2026-10-02 | 플로우 차트 v2, 오프닝 한국어 가사·크레디트 영상(v62) | `f12_flowchart.rpy` 머리말, `install/previous_opening_*.json` |
| 2026-10-03~04 | 엔딩 영상 3종 크레디트·가사 자막(v2→v3), 「유리의 실」 제목 수정 | `ending_localization/` |
| 2026-11-15~16 | 시나리오 18,184줄 전체 재번역(아르곤 16,919줄 + 카본 1,265줄). 설치본의 한국어 시나리오는 이 재번역본입니다(추정, 문장 대조 결과) | `latest/argon_retranslation_20261116/` |
| 2026-11-16 | 오프닝 크레디트 배경 재복원, 가사 문구 통일, 특전 개방, 플로우 차트 개방 취소 버그 수정 | `latest/qol_opening_20261116/` |
| 2026-11-17 | 엔딩 가사 전면 개역(기록상 "Clockwork Gothic 2-tier", 추정: 자막 표기 방식 변경) | `ending_localization/LATEST_INSTALL.json` |
| 2026-11-25 | 설치본의 최신 rpy·그림을 저장소에 올림 | 1d7663b, a8cb692 |

### 알려진 문제

- 11월 재번역·플로우 차트·특전 개방·그림·영상은 **배포 ZIP에 없습니다**. v1.0.0 ZIP만 설치하면 8월 번역본과 언어 선택기만 들어갑니다.
- 한국어 영상(mkv)은 용량과 원본 자산 문제로 저장소에 올리지 않았습니다.
- 엔딩 영상은 설치 확인만 하고 게임 안에서 실제 재생은 확인하지 않았습니다(`runtime_playback_verified: false`).
- 트루 엔딩 가사 일부는 사용자 음원·부클릿에서 옮긴 초안이며, 타이밍을 귀로 듣고 맞추지 않았습니다(`ED_TRUE_LYRICS.json`의 `source_status`, `timing_status`).
- 원본 영어 가사의 문법 오류(`I won't to …`)는 원본 표기로 그대로 둡니다.
- 우유 팩 CG 아래쪽 작은 글씨는 원문 그대로입니다.
- `latest/` 안의 일부 JSON 기록에는 작업 PC의 경로가 남아 있습니다.

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
