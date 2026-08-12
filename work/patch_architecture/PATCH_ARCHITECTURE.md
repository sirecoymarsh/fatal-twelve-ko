# Fatal Twelve 한국어 슬롯 최소 가역 패치 설계

작성일: 2026-08-10  
조사 대상: `F:\DOWN\Fatal.Twelve.Incl.DLC\Fatal.Twelve.Incl.DLC\Fatal Twelve`  
엔진: Ren'Py `6.99.14.3.3347` / `game/script_version.txt = (6, 99, 14, 3)`

## 1. 범위와 현재 결론

- 일본어를 **유일한 의미·문체 원문**으로 사용한다.
- 영어는 번역 ID/파일 정렬과, 일본어 문맥을 먼저 확정한 뒤의 공식 로마자 표기 확인에만 쓴다.
- 영어 의성어·감탄사·문장 리듬을 한국어 번역에 가져오지 않는다.
- 일본어 기본 슬롯(`None`)과 영어 슬롯(`english`)은 그대로 보존한다.
- 기존 슬롯을 덮어쓰지 않고 새 `korean` 슬롯을 `game/tl/korean`에 추가한다.
- 라이브 설치본의 `localize.rpyc`, `system.rpa`, `scenario.rpa`, `tl.rpa`는 교체하거나 다시 패킹하지 않는다.
- 이번 산출물은 **설계와 소스 스켈레톤**뿐이다. 대사/UI 번역문, 릴리스 패키지, 라이브 설치는 포함하지 않는다.

## 2. 읽기 전용 기준선

| 파일 | 크기 | SHA-256 |
|---|---:|---|
| `fatal.exe` | 386,048 | `987B9A1D43E46B8665A0CC4C6280459EF3D13C365FBA8BA0B55A88E9F03F43BD` |
| `game/localize.rpyc` | 924 | `5BA31F69D3646990D42E7044D97BF4CFB07BC105619B4F220FDCF1AD374D1D2F` |
| `game/scenario.rpa` | 5,102,486 | `EA39387AE13432A79FFE4601AF7B50478D063432CE3B7BC4013C92E09F036D22` |
| `game/tl.rpa` | 78,290,069 | `AD628D5AA7B0601E69FA99C13D6F67C21854AE0A290599DC478A986CFC53AC5F` |
| `game/system.rpa` | 199,203,732 | `A298B88F12C98435B015A647B51F5A35987EA4D714B5BF92E90972F3FCF6B648` |
| `game/script_version.txt` | 14 | `D052A3281338FF0C8E8E28B48AC5375085553DF182CEB3F63400D946AD48E2D3` |

핵심 RPA 엔트리 해시:

| 엔트리 | SHA-256 |
|---|---|
| `system.rpa::options.rpyc` | `11C370A268EF21DE270C4CFF2DC20760B1B5856E89F8A77E195219ED5087490A` |
| `system.rpa::screens.rpyc` | `9C84D4EB92CB3421CBA5DC374244528508FCF17E519B7F39D1FBB570D50BEB39` |
| `system.rpa::gui.rpyc` | `54010C454CB26A201775AD363BBDC86BEB98E1B9716D889CE427B8D59F659FB5` |

RPA 인덱스는 객체 생성 opcode가 없는 원시 dict/list/tuple pickle임을 확인한 뒤 제한 파서로만 읽었다. RPYC는 실행/역직렬화하지 않고 zlib 블록의 pickle opcode와 심볼릭 AST만 조사했다.

## 3. 실제 언어 슬롯

| 표시 언어 | 내부 키 | 스크립트/문자열 | 선택 액션 | 보존 정책 |
|---|---|---|---|---|
| 일본어 | `None` | `scenario.rpa::scenario/*.rpyc`, `system.rpa` | `Language(None)` | 원문·기본 fallback, 변경 금지 |
| 영어 | `english` | `tl.rpa::tl/english/**` | `Language("english")` | 공식 번역 그대로 보존 |
| 한국어 | `korean` | 새 loose `game/tl/korean/**` | `F12PatchLanguage("korean", "korean")` | 새 슬롯 |

확인된 아카이브 구성:

- `scenario.rpa`: 일본어 시나리오 RPYCs 29개.
- `tl.rpa`: `tl/english/scenario/*.rpyc` 29개와 영어 `characters`, `gamedata`, `screens`, `script`, 일부 언어별 이미지/영상.
- `system.rpa`: 일본어/공통 `characters`, `gamedata`, `gui`, `options`, `screens`, `script` 및 폰트/GUI 자산.

Ren'Py의 누락 처리도 일본어 중심 계약과 맞는다.

- 대사 translation ID가 `korean`에 없으면 `renpy/translation/__init__.py:173-190`에 따라 기본 translate 블록, 즉 일본어로 돌아간다.
- UI 문자열이 없으면 같은 파일 `379-398`에 따라 원문 문자열을 반환한다.
- 자산은 `renpy/loader.py:517-555`에서 `tl/korean/<path>`를 먼저 찾고, 없으면 원본 `<path>`로 돌아간다.
- 따라서 부분 번역 중에도 영어를 경유하지 않는다.

## 4. 강제 영어와 언어 메뉴 은닉의 실제 원인

### 4.1 `localize.rpyc`

`game/localize.rpyc`의 두 RPY-C2 슬롯은 동일하며 다음 AST를 포함한다.

- `renpy.ast.Init.priority = -1000`
- Python source: `_preferences.language = "english"`

Persistent/preferences는 init 코드보다 먼저 로드된다(`renpy/main.py:380-447`). 따라서 이 코드는 단순 최초 기본값이 아니라 매 부팅 때 저장된 언어를 영어로 다시 덮는다.

### 4.2 `config.developer`

`system.rpa::options.rpyc`의 Python source에는 다음이 있다.

```renpy
config.developer = False
```

`system.rpa::screens.rpyc`의 심볼릭 AST에서 `preferences` 화면은 다음 구조다.

- 화면 원본 위치: `game/screens.rpy:516`
- 시스템 탭 내 언어 행 조건: `game/screens.rpy:604`, `if config.developer`
- 행 제목: `game/screens.rpy:606`, `_("言語")`
- 일본어 버튼: `game/screens.rpy:609`, `Language(None)` / `"日本語"`
- 영어 버튼: `game/screens.rpy:610`, `Language("english")` / `"English"`

즉 언어 선택 기능은 존재하지만 release 설정에서 숨겨져 있다.

### 4.3 `config.developer = True`를 쓰지 않는 이유

언어 행 하나를 보이려고 전역 developer 모드를 켜면 오류 처리, 중복 label 보고, 개발자 키맵과 여러 런타임 분기가 함께 변한다. 또한 게임의 `script.rpyc`도 achievement 로그 등에 `config.developer`를 사용한다. 패치는 이 값을 계속 `False`로 둔다.

## 5. 최소 add-only 설계

### 5.1 부팅·선택 보존

새 루트 스크립트 `game/f12_korean_bootstrap.rpyc`를 추가한다.

1. 기존 `localize.rpyc`보다 뒤인 init priority `-999`에서 실행한다.
2. patch-owned `persistent.fatal12_ko_language_v1` 값을 읽는다.
3. 최초 패치 부팅에는 `korean`을 기록하고 `_preferences.language = "korean"`으로 지정한다.
4. 이후 사용자가 일본어/영어/한국어를 고르면 marker와 Ren'Py language를 함께 바꾼다.
5. 다음 부팅에는 기존 `localize.rpyc`가 먼저 영어를 지정하더라도 `-999` 단계가 사용자의 마지막 선택을 복구한다.

원본 `localize.rpyc`를 교체하지 않으므로 제거 시 원래의 영어 고정 동작으로 바로 돌아간다. Patch-owned persistent 필드는 남아도 원본 게임에서 읽지 않는다.

### 5.2 설정 메뉴 노출

기존 `preferences` 화면을 통째로 복사/재정의하지 않는다. 대신 빈 여덟 번째 행에 새 화면을 명시적으로 표시한다.

확인된 원본 레이아웃:

- 옵션 frame: `(1200, 560)`, `align (0.5, 0.615)`, `xpadding 1`, `ypadding 10`.
- 각 행 style `preferences_options_frame`: `ysize 45`.
- vbox `spacing 10`.
- 원래 developer-only 언어 행은 음성 대기 행 다음의 여덟 번째 행이다.
- 계산된 전역 배치: `xpos 40`, `ypos 약 493`, `xsize 1200`, `ysize 45`.

스켈레톤은 해당 위치에 기존 `preferences_options_*` styles를 재사용하고 `日本語 / English / 한국어` 세 버튼을 둔다.

`config.overlay_screens`는 사용하지 않는다. 동봉 `renpy/common/00gamemenu.rpy:112`가 게임 메뉴에서 `suppress_overlay = True`로 설정하고, `renpy/display/screen.py:1303-1327`이 overlay screen을 숨기기 때문이다. 대신 `config.interact_callbacks`에서 현재 `preferences` screen의 `scope["current_tab"]`을 확인해 시스템 탭에서만 selector screen을 명시적으로 show/hide한다. `renpy.get_screen()`이 scope를 보유한 `ScreenDisplayable`을 반환한다는 근거는 `renpy/display/screen.py:321-345,959-999`이다. The bundled engine uses the same get_screen/show_screen/hide_screen synchronization pattern in renpy/common/00preferences.rpy:471-485.

### 5.3 새 한국어 슬롯 등록

`game/tl/korean/f12_slot.rpyc`에는 번역문 없이 `translate korean python:` 블록만 둔다.

- 이 노드 자체로 translator의 known language 집합에 `korean`이 등록된다(`renpy/translation/__init__.py:118-130`).
- 따라서 `Language("korean")` sensitivity 검사가 통과한다(`renpy/common/00action_other.rpy:333-359`).
- 향후 일본어 translation ID와 동일한 ID의 `translate korean <id>:` 블록을 `tl/korean/scenario/*.rpyc`에 추가한다.

## 6. 폰트 실측

모든 값은 `system.rpa` 안의 실제 font bytes에서 cmap format 4/12를 직접 읽고, glyph ID가 0(`.notdef`)이 아닌지 검사한 결과다.

| 폰트 | 현대 한글 음절 U+AC00-D7A3 | 한글 자모 U+1100-11FF | 호환 자모 U+3130-318F | 결론 |
|---|---:|---:|---:|---|
| `CharisSILR.ttf` | 0/11,172 | 0/256 | 0/96 | 한글 불가 |
| `MTLc3m.ttf` | 0/11,172 | 0/256 | 0/96 | 한글 불가 |
| `NotoSansCJKjp-Bold.otf` | 11,172/11,172 | 256/256 | 94/96 | 사용 가능 |
| `NotoSansCJKjp-Light.otf` | 11,172/11,172 | 256/256 | 94/96 | 사용 가능 |
| `NotoSansCJKjp-Medium.otf` | 11,172/11,172 | 256/256 | 94/96 | 사용 가능 |
| `NotoSansCJKjp-Regular.otf` | 11,172/11,172 | 256/256 | 94/96 | 사용 가능 |
| `NotoSansCJKjp-Thin.otf` | 11,172/11,172 | 256/256 | 94/96 | 사용 가능 |
| `NotoSerifCJKjp-Light.otf` | 11,172/11,172 | 256/256 | 94/96 | 사용 가능 |
| `NotoSerifCJKjp-Medium.otf` | 11,172/11,172 | 256/256 | 94/96 | 사용 가능 |
| `NotoSerifCJKjp-SemiBold.otf` | 11,172/11,172 | 256/256 | 94/96 | 사용 가능 |
| `ipaexm.ttf` | 0/11,172 | 0/256 | 0/96 | 한글 불가 |
| `mgenplus-2pp-regular.ttf` | 0/11,172 | 0/256 | 0/96 | 한글 불가 |

호환 자모 범위의 96 code point 중 `U+3130`, `U+318F`는 미할당이므로 Noto의 `94/96`은 모든 할당 문자를 포함한다.

원본 style/font 근거:

- `_default.font = MTLc3m.ttf` — 한글 없음.
- `default.font = NotoSansCJKjp-Regular.otf` — 한글 완전 지원.
- `say_label.font = NotoSansCJKjp-Bold.otf` — 한글 완전 지원.
- `say_dialogue.font = mgenplus-2pp-regular.ttf` — 한글 없음, **필수 override**.
- `menu_page_title_label_text.font = ipaexm.ttf` — 한글 없음, override.
- `game_menu_date_text.font = CharisSILR.ttf` — 한글 없음, 날짜/요일 번역 가능성 때문에 override.

한국어일 때만 다음을 적용한다.

- `_default`, `default`, `say_dialogue` → `NotoSansCJKjp-Regular.otf`
- `menu_page_title_label_text` → `NotoSansCJKjp-Medium.otf`
- `game_menu_date_text` → `NotoSansCJKjp-Regular.otf`
- `_default.language`, `default.language` → `korean-with-spaces`

`korean-with-spaces`는 이 엔진에 명시적으로 구현돼 있다(`renpy/text/text.py:614-629`). 언어 변경 시 Ren'Py는 base style backup을 먼저 복구한 뒤 선택 언어 블록을 적용한다(`renpy/translation/__init__.py:592-627`). 따라서 일본어/영어로 돌아갈 때 한국어 font override가 누출되지 않는다.

## 7. loose `.rpy/.rpyc` 우선순위와 `config.developer`

동봉 엔진 코드 기준:

1. `renpy/config.py:129`의 `force_archives = False`.
2. `renpy/loader.py:90-92,472-499`는 실제 파일을 archive보다 먼저 연다.
3. `renpy/loader.py:252-267`는 searchpath의 loose 파일을 먼저 `seen`에 넣고 그 뒤 archive 인덱스를 추가한다.
4. `renpy/script.py:232-254`는 loose `.rpy`와 loose/archive `.rpyc`를 스크립트 후보로 잡는다. archive 안 `.rpy`는 건너뛴다.
5. `renpy/script.py:660-744`:
   - archive 후보는 `.rpyc`만 읽는다.
   - loose `.rpy`와 `.rpyc`가 모두 있으면 source MD5와 RPY-C2 trailer를 비교한다.
   - 일치하면 `.rpyc`, 불일치하거나 compiled load 실패면 `.rpy`를 parse하고 `.rpyc` 쓰기를 시도한다.
   - `.rpyc`만 있으면 그대로 읽고, `.rpy`만 있으면 parse/compile한다.
6. 위 분기에는 `config.developer` 검사가 없다. `config.developer = False`여도 loose source는 로드/컴파일된다.

따라서:

- 개발/번역 작업물은 `.rpy`로 유지한다.
- 릴리스에는 staging에서 컴파일한 `.rpyc`만 넣어 첫 실행의 쓰기와 source 노출을 피한다.
- archive보다 우선하는 새 loose 경로만 사용한다.
- `screens.rpyc`나 기존 translation archive를 loose replacement로 덮는 설계는 쓰지 않는다.

## 8. 정확한 컴파일 방법과 검증 결과

동봉 CLI는 positional `basedir`, `command`를 받으며(`renpy/arguments.py:84-114`) `compile` 명령은 강제 컴파일을 건다(`140-155,193-200`). 컴파일 명령은 orphan RPYCs를 `.bak`로 바꿀 수 있으므로(`renpy/main.py:333-354`) 라이브 게임에서 실행하면 안 된다.

권장 명령:

```powershell
& 'F:\DOWN\Fatal.Twelve.Incl.DLC\Fatal.Twelve.Incl.DLC\Fatal Twelve\fatal.exe' `
  '<ISOLATED-STAGING-BASEDIR>' `
  compile `
  --keep-orphan-rpyc
```

검증 수행:

- 임시 basedir에 스켈레톤 두 파일과 최소 style fixture만 복사.
- 위 게임의 실제 `fatal.exe`/Ren'Py `6.99.14.3.3347`로 compile.
- exit code `0`.
- `errors.txt`, `traceback.txt` 없음.
- 두 source 모두 RPY-C2 `.rpyc` 생성 확인.
- compile 전후 라이브 `localize.rpyc`, `system.rpa`, `tl.rpa` SHA-256 동일.
- 임시 fixture 삭제 완료.

이는 **파싱·컴파일 검증**이다. 실제 Fatal Twelve 전체 화면에서 버튼 클릭, 언어 전환, 저장 후 재부팅, 레이아웃을 검증한 것은 아니다.

## 9. 최종 릴리스의 최소 파일 집합

초기 구조 패치:

```text
game/
  f12_korean_bootstrap.rpyc
  tl/
    korean/
      f12_slot.rpyc
```

번역이 진행되면 같은 루트 아래에만 누적한다.

```text
game/tl/korean/
  characters.rpyc
  gamedata.rpyc
  screens.rpyc
  script.rpyc
  scenario/*.rpyc
  <한국어화한 언어별 이미지 경로>
```

라이브 기준선에는 `game/f12_korean_bootstrap.*`, loose `game/tl`, `game/tl/korean`이 모두 존재하지 않음을 확인했다. 그러므로 manifest에 기록된 새 파일만 제거하면 원본 파일 byte를 복구할 필요 없이 되돌릴 수 있다.

## 10. 설치 전에 남은 필수 검증

1. 전체 번역 파일을 동일 엔진 staging에서 컴파일하고 translation ID 누락/중복 검사.
2. 최종 한국어 글자 집합 전체를 Noto cmap의 nonzero glyph ID와 대조.
3. 깨끗한 복사본에 compiled-only patch를 적용해 부팅.
4. 최초 부팅이 한국어인지 확인.
5. 설정 > 시스템에서 세 버튼 위치/hover/selected/click 확인.
6. 한국어 → 일본어 → 영어 → 한국어 전환 시 텍스트·font·이미지 누출 여부 확인.
7. 각 언어 선택 뒤 종료/재실행하여 patch-owned 선택 보존 확인.
8. 대표 대사, 긴 대사, 루비, 선택지, 저장/불러오기, 설정, 카드북, 우클릭 메뉴에서 tofu/잘림/줄바꿈 확인.
9. 일본어/영어 archive hashes가 기준선과 동일한지 재확인.
10. 설치/제거 manifest와 깨끗한 복사본 restore test 완료 후에만 배포.

## 11. 산출물

- `language_contract.json`: 일본어 원문·영어 제한·새 한국어 슬롯 계약 초안.
- `skeleton/game/f12_korean_bootstrap.rpy`: 강제 영어 후 선택 복원 + 설정 메뉴 세 언어 selector.
- `skeleton/game/tl/korean/f12_slot.rpy`: 한국어 슬롯 등록 + 한국어 전용 font/line-break override.

