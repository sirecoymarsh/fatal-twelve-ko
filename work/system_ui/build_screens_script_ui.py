from __future__ import annotations

import ast
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any


WORKSPACE = Path(r"C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc")
PROJECT = Path(r"P:\AI\Codex\projects\fatal-twelve-ko")
OUT = WORKSPACE / "work" / "system_ui"
SYSTEM = PROJECT / "work" / "extracted" / "system"
OFFICIAL = PROJECT / "work" / "extracted" / "tl" / "tl" / "english"

SCREENS_SOURCE = SYSTEM / "screens.rpy"
SCRIPT_SOURCE = SYSTEM / "script.rpy"
SCREENS_MEMBERSHIP = OFFICIAL / "screens.rpy"
SCRIPT_MEMBERSHIP = OFFICIAL / "script.rpy"

STATUS = "first_draft_unreviewed"
QA = "deferred_until_full_first_draft"
SOURCE_AUTHORITY = "Japanese only"


SCREENS_AUTHORITATIVE = [
    "GALLERY",
    "MUSIC",
    "SCENE REPLAY",
    "CHARACTER INFO",
    "START",
    "CONTINUE",
    "LOAD",
    "SETTINGS",
    "EXTRA",
    "QUIT",
    "back",
    "close",
    "reset page",
    "reset all",
    "データ管理",
    "セーブ",
    "ロード",
    "移動",
    "コピー",
    "削除",
    "クイックセーブ",
    "クイックセーブ № ",
    "セーブ № ",
    "日付： ",
    "%Y/%m/%d - %H:%M",
    "総合プレイ時間： ",
    "環境設定",
    "システム",
    "メッセージ",
    "サウンド",
    "画面モード",
    "ウインドウ",
    "フルスクリーン",
    "メッセージ枠の透明度",
    "クイックメニューを固定",
    "スキップアイコンを表示",
    "オートモードアイコンを表示",
    "ロールバックメニューを表示",
    "言語",
    "未読メッセージの表示速度",
    "既読メッセージの表示速度",
    "オートモード時のウエイト速度",
    "スキップモード",
    "既読のみ",
    "全て",
    "オートモードは音声を待つ",
    "BGM",
    "効果音",
    "システム効果音",
    "ボイス",
    "ボイス再生を次のメッセージまで継続する",
    "はい",
    "いいえ",
    "AUTO",
    "SKIP",
    "QUICK SAVE",
    "ROLLBACK",
    "VOICE",
    "HIDE",
    "MENU",
    "Location",
    "Tip",
    "カードブック",
    "カードはありません",
    "BACK",
    "ロールバックモ－ド",
    "NEXT",
    "キーボード",
    "マウス",
    "Keyboard Help",
    "Mouse Help",
    "END REPLAY",
    "あらすじ",
    "エクストラ",
    "ギャラリー",
    "リプレイ",
    "エンディング",
]

SCREENS_KO = {
    "GALLERY": "갤러리",
    "MUSIC": "음악",
    "SCENE REPLAY": "장면 다시 보기",
    "CHARACTER INFO": "인물 정보",
    "START": "시작",
    "CONTINUE": "이어하기",
    "LOAD": "불러오기",
    "SETTINGS": "설정",
    "EXTRA": "특전",
    "QUIT": "종료",
    "back": "뒤로",
    "close": "닫기",
    "reset page": "이 페이지 초기화",
    "reset all": "모두 초기화",
    "データ管理": "데이터 관리",
    "セーブ": "저장",
    "ロード": "불러오기",
    "移動": "이동",
    "コピー": "복사",
    "削除": "삭제",
    "クイックセーブ": "빠른 저장",
    "クイックセーブ № ": "빠른 저장 № ",
    "セーブ № ": "저장 № ",
    "日付： ": "날짜: ",
    "%Y/%m/%d - %H:%M": "%Y/%m/%d - %H:%M",
    "総合プレイ時間： ": "총 플레이 시간: ",
    "環境設定": "환경 설정",
    "システム": "시스템",
    "メッセージ": "메시지",
    "サウンド": "사운드",
    "画面モード": "화면 모드",
    "ウインドウ": "창 모드",
    "フルスクリーン": "전체 화면",
    "メッセージ枠の透明度": "메시지 창 투명도",
    "クイックメニューを固定": "빠른 메뉴 고정",
    "スキップアイコンを表示": "건너뛰기 아이콘 표시",
    "オートモードアイコンを表示": "자동 모드 아이콘 표시",
    "ロールバックメニューを表示": "롤백 메뉴 표시",
    "言語": "언어",
    "未読メッセージの表示速度": "읽지 않은 메시지 표시 속도",
    "既読メッセージの表示速度": "읽은 메시지 표시 속도",
    "オートモード時のウエイト速度": "자동 모드 대기 속도",
    "スキップモード": "건너뛰기 모드",
    "既読のみ": "읽은 내용만",
    "全て": "모두",
    "オートモードは音声を待つ": "자동 모드에서 음성 재생 대기",
    "BGM": "BGM",
    "効果音": "효과음",
    "システム効果音": "시스템 효과음",
    "ボイス": "음성",
    "ボイス再生を次のメッセージまで継続する": "다음 메시지까지 음성 계속 재생",
    "はい": "예",
    "いいえ": "아니요",
    "AUTO": "자동",
    "SKIP": "건너뛰기",
    "QUICK SAVE": "빠른 저장",
    "ROLLBACK": "되돌리기",
    "VOICE": "음성",
    "HIDE": "숨기기",
    "MENU": "메뉴",
    "Location": "장소",
    "Tip": "도움말",
    "カードブック": "카드북",
    "カードはありません": "카드가 없습니다",
    "BACK": "뒤로",
    "ロールバックモ－ド": "롤백 모드",
    "NEXT": "다음",
    "キーボード": "키보드",
    "マウス": "마우스",
    "Keyboard Help": "키보드 도움말",
    "Mouse Help": "마우스 도움말",
    "END REPLAY": "다시 보기 종료",
    "あらすじ": "줄거리",
    "エクストラ": "특전",
    "ギャラリー": "갤러리",
    "リプレイ": "다시 보기",
    "エンディング": "엔딩",
    "Image [index] of [count] locked.": "[count]개 중 [index]번 이미지는 잠겨 있습니다.",
    "next": "다음",
    "prev": "이전",
    "return": "돌아가기",
    "slideshow": "슬라이드 쇼",
    "女神の選定": "여신의 선정",
    "日本語": "일본어",
    "English": "영어",
    "Numeral ": "번호 ",
    " - ": " - ",
}

SCREENS_SEMANTIC_JP = {
    "Image [index] of [count] locked.": "画像 [index] / [count] はロックされています。",
}

SCREENS_DIRECT = [
    ("日本語", 609, 'textbutton "日本語" action Language(None)'),
    ("English", 610, 'textbutton "English" action Language("english")'),
    ("Numeral ", 1062, 'label "Numeral " + character_info[current_character]["numeral"] style "cardbook_character_name_label":'),
    (" - ", 1239, 'text " - " style "cardbook_button_text"'),
]


# Display expressions whose actual text is supplied at runtime by scenario, gamedata,
# save metadata, or Ren'Py. They are audited here but not duplicated as translation keys.
SCREENS_DYNAMIC = [
    (26, "scenario_character_name"),
    (28, "scenario_dialogue"),
    (84, "scenario_menu_caption"),
    (435, "save_metadata_name"),
    (440, "renpy_save_timestamp"),
    (863, "system_confirmation_message"),
    (969, "screen_tooltip_value"),
    (976, "scenario_or_gamedata_save_name"),
    (984, "gamedata_date"),
    (989, "gamedata_bgm_title"),
    (997, "gamedata_location_name"),
    (1005, "gamedata_location_tip"),
    (1238, "gamedata_card_character_title"),
    (1240, "gamedata_card_type_title"),
    (1264, "gamedata_card_description"),
    (1334, "gamedata_plot_title"),
    (1360, "gamedata_plot_label"),
    (1391, "gamedata_plot_text"),
    (1467, "renpy_notification_message"),
    (1495, "gamedata_date"),
]

SCRIPT_AUTHORITATIVE = [
    "データをセーブ",
    "データをロード",
    "環境設定を変更",
    "あらすじを読む",
    "カードブックを調べる",
    "タイトルメニューへ戻る",
    "ゲームへ戻る",
    "ゲームを終了",
    "セーブデータを上書きコピーしますか？",
    "セーブデータをコピーしますか？",
    "セーブデータを移しますか？",
    "このページの環境設定を初期化しますか？",
    "全ての環境設定を初期化しますか？",
]

SCRIPT_KO = {
    "データをセーブ": "데이터 저장",
    "データをロード": "데이터 불러오기",
    "環境設定を変更": "환경 설정 변경",
    "あらすじを読む": "줄거리 보기",
    "カードブックを調べる": "카드북 살펴보기",
    "タイトルメニューへ戻る": "타이틀 메뉴로 돌아가기",
    "ゲームへ戻る": "게임으로 돌아가기",
    "ゲームを終了": "게임 종료",
    "セーブデータを上書きコピーしますか？": "저장 데이터를 덮어써서 복사하시겠습니까?",
    "セーブデータをコピーしますか？": "저장 데이터를 복사하시겠습니까?",
    "セーブデータを移しますか？": "저장 데이터를 이동하시겠습니까?",
    "このページの環境設定を初期化しますか？": "이 페이지의 환경 설정을 초기화하시겠습니까?",
    "全ての環境設定を初期化しますか？": "모든 환경 설정을 초기화하시겠습니까?",
}

SCRIPT_BASE_KO = {
    "Quick save complete.": "빠른 저장 완료",
    "Are you sure you want to delete this save?": "저장 데이터를 삭제하시겠습니까?",
    "Are you sure you want to overwrite your save?": "저장 데이터를 덮어쓰시겠습니까?",
    "Loading will lose unsaved progress.\nAre you sure you want to do this?": "저장 데이터를 불러오시겠습니까?",
    "Are you sure you want to quit?": "게임을 종료하시겠습니까?",
    "Are you sure you want to return to the main menu?\nThis will lose unsaved progress.": "타이틀 화면으로 돌아가시겠습니까?",
    "Image [index] of [count] locked.": "[count]개 중 [index]번 이미지는 잠겨 있습니다.",
    "Saved screenshot as %s.": "스크린샷을 %s에 저장했습니다.",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def stable_id(source_file: str, lane: str, lookup_key: str, ordinal: int) -> str:
    raw = f"{source_file}|{lane}|{lookup_key}|{ordinal}".encode("utf-8")
    return "sysui_" + hashlib.sha256(raw).hexdigest()[:20]


def literal_value(token: str) -> str:
    value = ast.literal_eval(token)
    if not isinstance(value, str):
        raise TypeError(token)
    return value


def parse_old_membership(path: Path) -> list[dict[str, Any]]:
    """Read only `old` membership lines; official `new` prose is never retained."""
    result: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            stripped = line.lstrip()
            if not stripped.startswith("old "):
                continue
            token = stripped[4:].strip()
            result.append({"key": literal_value(token), "line": line_no})
    return result


CALL_RE = re.compile(r"_\(\s*(?P<token>\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*')\s*\)")
STRING_RE = re.compile(r"(?P<token>\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*')")


def parse_translate_calls(path: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        for match in CALL_RE.finditer(line):
            out.append(
                {
                    "key": literal_value(match.group("token")),
                    "line": line_no,
                    "statement": line.strip(),
                }
            )
    return out


def parse_string_literal_hits(path: Path) -> dict[str, list[dict[str, Any]]]:
    """Index exact decoded string literals; never use substring matching."""
    out: dict[str, list[dict[str, Any]]] = {}
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        for match in STRING_RE.finditer(line):
            try:
                key = literal_value(match.group("token"))
            except (SyntaxError, ValueError):
                continue
            out.setdefault(key, []).append({"line": line_no, "statement": line.strip()})
    return out


def parse_base_none_strings(path: Path) -> list[dict[str, Any]]:
    """Extract technical old key + Japanese new only from `translate None strings`."""
    out: list[dict[str, Any]] = []
    in_none = False
    pending: dict[str, Any] | None = None
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            stripped = line.strip()
            if stripped == "translate None strings:":
                in_none = True
                continue
            if in_none and stripped.startswith("translate "):
                break
            if not in_none:
                continue
            if stripped.startswith("old "):
                pending = {"key": literal_value(stripped[4:].strip()), "old_line": line_no}
            elif stripped.startswith("new ") and pending is not None:
                pending["source_jp"] = literal_value(stripped[4:].strip())
                pending["new_line"] = line_no
                out.append(pending)
                pending = None
    return out


TOKEN_RE = re.compile(
    r"\{[^{}]+\}|\[[A-Za-z_][A-Za-z0-9_.!:\[\]'\" -]*\]|%(?:\([^)]+\))?[#0 +\-]?[0-9]*(?:\.[0-9]+)?[A-Za-z%]"
)


def tokens(text: str) -> list[str]:
    return TOKEN_RE.findall(text)


def line_hits(lines: list[str], key: str) -> list[dict[str, Any]]:
    hits: list[dict[str, Any]] = []
    quoted = json.dumps(key, ensure_ascii=False)
    for line_no, statement in enumerate(lines, 1):
        if key in statement or quoted in statement:
            hits.append({"line": line_no, "statement": statement.strip()})
    return hits


def make_record(
    *,
    command_index: int,
    source_file: str,
    source_hash: str,
    lane: str,
    lookup_key: str,
    source_jp: str,
    draft_ko: str,
    source_hits: list[dict[str, Any]],
    membership_line: int | None,
    authoritative: bool,
    origin: list[str],
    emitted_to_rpy: bool = True,
    duplicate_of: str | None = None,
) -> dict[str, Any]:
    source_token_counts = Counter(tokens(source_jp))
    draft_token_counts = Counter(tokens(draft_ko))
    source_line = source_hits[0]["line"] if source_hits else None
    source_statement = source_hits[0]["statement"] if source_hits else None
    if source_line is not None:
        exact_locator = {
            "kind": "base_source",
            "file": source_file,
            "line": source_line,
            "statement": source_statement,
        }
    elif membership_line is not None:
        membership_file = (
            "tl/tl/english/screens.rpy"
            if source_file.endswith("screens.rpy")
            else "tl/tl/english/script.rpy"
        )
        exact_locator = {
            "kind": "official_old_key_membership_only",
            "file": membership_file,
            "line": membership_line,
            "statement": f"old {json.dumps(lookup_key, ensure_ascii=False)}",
        }
    else:
        exact_locator = None
    return {
        "command_index": command_index,
        "stable_id": stable_id(source_file, lane, lookup_key, command_index),
        "source_file": source_file,
        "source_sha256": source_hash,
        "source_line": source_line,
        "source_lines": [item["line"] for item in source_hits],
        "statement": source_statement,
        "statements": source_hits,
        "exact_locator": exact_locator,
        "lane": lane,
        "lookup_key": lookup_key,
        "source_jp": source_jp,
        "draft_ko": draft_ko,
        "authoritative_old_key": authoritative,
        "official_membership_line": membership_line,
        "origin": origin,
        "exact_translation_id": None,
        "protected_tokens_source": list(source_token_counts.elements()),
        "protected_tokens_draft": list(draft_token_counts.elements()),
        "protected_tokens_preserved": source_token_counts == draft_token_counts,
        "emitted_to_rpy": emitted_to_rpy,
        "duplicate_of": duplicate_of,
        "status": STATUS,
        "qa": QA,
        "source_authority": SOURCE_AUTHORITY,
        "english_reference_used": False,
    }


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, records: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")


def rpy_quote(text: str) -> str:
    return json.dumps(text, ensure_ascii=False)


def write_rpy(path: Path, source_name: str, records: list[dict[str, Any]]) -> None:
    out = [
        "# Auto-generated first-draft Korean system UI strings.",
        "# Meaning/style source: Japanese base only; translation QA deferred.",
        f"# Source: system/{source_name}.rpy",
        "",
        "translate korean strings:",
    ]
    seen: set[str] = set()
    for record in records:
        if not record["emitted_to_rpy"]:
            continue
        key = record["lookup_key"]
        if key in seen:
            raise AssertionError(f"duplicate emitted lookup key: {key!r}")
        seen.add(key)
        out.extend(
            [
                "",
                f"    # {record['stable_id']} | {record['lane']} | source line {record['source_line']}",
                f"    old {rpy_quote(key)}",
                f"    new {rpy_quote(record['draft_ko'])}",
            ]
        )
    path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")


def build_screens() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    source_lines = SCREENS_SOURCE.read_text(encoding="utf-8").splitlines()
    calls = parse_translate_calls(SCREENS_SOURCE)
    literal_hits = parse_string_literal_hits(SCREENS_SOURCE)
    source_order: list[str] = []
    call_hits: dict[str, list[dict[str, Any]]] = {}
    for item in calls:
        call_hits.setdefault(item["key"], []).append(
            {"line": item["line"], "statement": item["statement"]}
        )
        if item["key"] not in source_order:
            source_order.append(item["key"])

    membership_rows = parse_old_membership(SCREENS_MEMBERSHIP)
    membership_line = {item["key"]: item["line"] for item in membership_rows}
    membership_keys = list(dict.fromkeys(item["key"] for item in membership_rows))
    assert membership_keys == SCREENS_AUTHORITATIVE, (
        len(membership_keys),
        set(membership_keys) ^ set(SCREENS_AUTHORITATIVE),
    )

    key_order = SCREENS_AUTHORITATIVE + [
        key for key in source_order if key not in set(SCREENS_AUTHORITATIVE)
    ]
    assert len(source_order) == 64
    assert len(key_order) == 83
    assert set(key_order) <= set(SCREENS_KO)

    records: list[dict[str, Any]] = []
    source_hash = sha256(SCREENS_SOURCE)
    for key in key_order:
        hits = call_hits.get(key) or literal_hits.get(key, [])
        origin = []
        if key in membership_line:
            origin.append("authoritative_old_key_membership")
        if key in call_hits:
            origin.append("base_source_translation_call")
        elif hits:
            origin.append("base_source_literal")
        records.append(
            make_record(
                command_index=len(records) + 1,
                source_file="system/screens.rpy",
                source_hash=source_hash,
                lane="strings",
                lookup_key=key,
                source_jp=SCREENS_SEMANTIC_JP.get(key, key),
                draft_ko=SCREENS_KO[key],
                source_hits=hits,
                membership_line=membership_line.get(key),
                authoritative=key in membership_line,
                origin=origin,
            )
        )

    for key, expected_line, statement in SCREENS_DIRECT:
        assert source_lines[expected_line - 1].strip() == statement
        records.append(
            make_record(
                command_index=len(records) + 1,
                source_file="system/screens.rpy",
                source_hash=source_hash,
                lane="direct_literal",
                lookup_key=key,
                source_jp=key,
                draft_ko=SCREENS_KO[key],
                source_hits=[{"line": expected_line, "statement": statement}],
                membership_line=None,
                authoritative=False,
                origin=["base_source_direct_display_literal"],
            )
        )

    assert len(records) == 87
    dynamic_consumers = [
        {
            "line": line_no,
            "statement": source_lines[line_no - 1].strip(),
            "runtime_text_provider": provider,
            "translation_ownership": "external_string_store_or_runtime",
        }
        for line_no, provider in SCREENS_DYNAMIC
    ]
    return records, {
        "source_translate_call_occurrences": len(calls),
        "source_translate_call_unique": len(source_order),
        "authoritative_old_occurrences": len(membership_rows),
        "authoritative_old_unique": len(membership_keys),
        "union_translation_keys": len(key_order),
        "direct_display_literals": len(SCREENS_DIRECT),
        "dynamic_display_consumer_count": len(dynamic_consumers),
        "dynamic_display_consumers": dynamic_consumers,
    }


def build_script() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    source_lines = SCRIPT_SOURCE.read_text(encoding="utf-8").splitlines()
    literal_hits = parse_string_literal_hits(SCRIPT_SOURCE)
    membership_rows = parse_old_membership(SCRIPT_MEMBERSHIP)
    membership_line = {item["key"]: item["line"] for item in membership_rows}
    membership_keys = list(dict.fromkeys(item["key"] for item in membership_rows))
    assert membership_keys == SCRIPT_AUTHORITATIVE
    base_rows = parse_base_none_strings(SCRIPT_SOURCE)
    assert len(base_rows) == 8
    assert [item["key"] for item in base_rows] == list(SCRIPT_BASE_KO)
    source_hash = sha256(SCRIPT_SOURCE)

    records: list[dict[str, Any]] = []
    for key in SCRIPT_AUTHORITATIVE:
        hits = literal_hits.get(key, [])
        records.append(
            make_record(
                command_index=len(records) + 1,
                source_file="system/script.rpy",
                source_hash=source_hash,
                lane="strings",
                lookup_key=key,
                source_jp=key,
                draft_ko=SCRIPT_KO[key],
                source_hits=hits,
                membership_line=membership_line[key],
                authoritative=True,
                origin=["authoritative_old_key_membership"]
                + (["base_source_literal"] if hits else []),
            )
        )

    for item in base_rows:
        key = item["key"]
        duplicate = key == "Image [index] of [count] locked."
        records.append(
            make_record(
                command_index=len(records) + 1,
                source_file="system/script.rpy",
                source_hash=source_hash,
                lane="base_none_strings",
                lookup_key=key,
                source_jp=item["source_jp"],
                draft_ko=SCRIPT_BASE_KO[key],
                source_hits=[
                    {
                        "line": item["new_line"],
                        "statement": source_lines[item["new_line"] - 1].strip(),
                    }
                ],
                membership_line=None,
                authoritative=False,
                origin=["base_source_translate_none_japanese_value"],
                emitted_to_rpy=not duplicate,
                duplicate_of=(
                    "system/screens.rpy:Image [index] of [count] locked."
                    if duplicate
                    else None
                ),
            )
        )

    direct_line = 1751
    direct_statement = 'show expression Text("to be continued...", size=50, font="gui/fonts/CharisSILR.ttf") at align(0.95, 0.95)'
    assert source_lines[direct_line - 1].strip() == direct_statement
    records.append(
        make_record(
            command_index=len(records) + 1,
            source_file="system/script.rpy",
            source_hash=source_hash,
            lane="direct_literal",
            lookup_key="to be continued...",
            source_jp="to be continued...",
            draft_ko="계속됩니다...",
            source_hits=[{"line": direct_line, "statement": direct_statement}],
            membership_line=None,
            authoritative=False,
            origin=["base_source_direct_display_literal"],
        )
    )
    assert len(records) == 22
    return records, {
        "authoritative_old_occurrences": len(membership_rows),
        "authoritative_old_unique": len(membership_keys),
        "base_none_japanese_entries": len(base_rows),
        "direct_display_literals": 1,
        "cross_source_duplicate_entries_not_emitted": 1,
    }


def structure_report(
    source_name: str,
    records: list[dict[str, Any]],
    extraction: dict[str, Any],
) -> dict[str, Any]:
    authoritative_expected = 77 if source_name == "screens" else 13
    authoritative_records = [r for r in records if r["authoritative_old_key"]]
    emitted = [r for r in records if r["emitted_to_rpy"]]
    emitted_keys = [r["lookup_key"] for r in emitted]
    failures = [r["stable_id"] for r in records if not r["protected_tokens_preserved"]]
    missing_line = [r["stable_id"] for r in records if r["source_line"] is None]
    missing_locator = [r["stable_id"] for r in records if r["exact_locator"] is None]
    checks = {
        "record_count_matches": len(records) == (87 if source_name == "screens" else 22),
        "authoritative_old_key_coverage_matches": len(authoritative_records)
        == authoritative_expected,
        "authoritative_old_key_unique": len(
            {r["lookup_key"] for r in authoritative_records}
        )
        == authoritative_expected,
        "emitted_lookup_keys_unique": len(emitted_keys) == len(set(emitted_keys)),
        "protected_tokens_preserved": not failures,
        "status_uniform": {r["status"] for r in records} == {STATUS},
        "qa_uniform": {r["qa"] for r in records} == {QA},
        "english_reference_used_false": all(
            r["english_reference_used"] is False for r in records
        ),
        "source_authority_japanese_only": all(
            r["source_authority"] == SOURCE_AUTHORITY for r in records
        ),
        "exact_locator_present": not missing_locator,
    }
    return {
        "source_file": f"system/{source_name}.rpy",
        "source_sha256": records[0]["source_sha256"],
        "catalog_records": len(records),
        "emitted_rpy_entries": len(emitted),
        "authoritative_old_key_target": authoritative_expected,
        "authoritative_old_key_covered": len(authoritative_records),
        "extraction": extraction,
        "missing_base_source_line_count": len(missing_line),
        "missing_base_source_line_stable_ids": missing_line,
        "missing_exact_locator_count": len(missing_locator),
        "missing_exact_locator_stable_ids": missing_locator,
        "protected_token_failure_count": len(failures),
        "protected_token_failure_stable_ids": failures,
        "checks": checks,
        "result": "PASS" if all(checks.values()) else "FAIL",
        "translation_quality_review_performed": False,
        "status": STATUS,
        "qa": QA,
        "source_authority": SOURCE_AUTHORITY,
        "english_reference_used": False,
        "official_membership_handling": "Only old keys were mechanically retained; official new prose was skipped.",
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    screens, screens_extraction = build_screens()
    script, script_extraction = build_script()

    payloads = {"screens": screens, "script": script}
    reports: dict[str, dict[str, Any]] = {}
    for name, records in payloads.items():
        extraction = screens_extraction if name == "screens" else script_extraction
        write_jsonl(OUT / f"{name}.catalog.jsonl", records)
        write_json(
            OUT / f"{name}.draft.json",
            {
                "source_file": f"system/{name}.rpy",
                "source_sha256": records[0]["source_sha256"],
                "record_count": len(records),
                "status": STATUS,
                "qa": QA,
                "source_authority": SOURCE_AUTHORITY,
                "english_reference_used": False,
                "records": records,
            },
        )
        write_rpy(OUT / f"{name}.ko.rpy", name, records)
        reports[name] = structure_report(name, records, extraction)
        write_json(OUT / f"{name}.structure_check.json", reports[name])

    emitted_all = [
        record
        for records in payloads.values()
        for record in records
        if record["emitted_to_rpy"]
    ]
    all_keys = [record["lookup_key"] for record in emitted_all]
    assert len(all_keys) == len(set(all_keys))
    assert reports["screens"]["result"] == "PASS"
    assert reports["script"]["result"] == "PASS"

    summary = {
        "scope": ["system/screens.rpy", "system/script.rpy"],
        "source_hashes": {
            "screens.rpy": sha256(SCREENS_SOURCE),
            "script.rpy": sha256(SCRIPT_SOURCE),
        },
        "membership_file_hashes": {
            "screens.rpy": sha256(SCREENS_MEMBERSHIP),
            "script.rpy": sha256(SCRIPT_MEMBERSHIP),
        },
        "catalog_records": {
            "screens": len(screens),
            "script": len(script),
            "total": len(screens) + len(script),
        },
        "authoritative_old_key_coverage": {
            "screens": "77/77",
            "script": "13/13",
        },
        "emitted_rpy_entries": {
            "screens": sum(r["emitted_to_rpy"] for r in screens),
            "script": sum(r["emitted_to_rpy"] for r in script),
            "total_unique": len(all_keys),
        },
        "cross_source_duplicates_omitted": [
            "Image [index] of [count] locked. (script copy; emitted in screens.ko.rpy)"
        ],
        "dynamic_display_consumers_audited": {
            "screens": len(SCREENS_DYNAMIC),
            "script": 0,
            "note": "Runtime text is owned by scenario, gamedata, save metadata, or Ren'Py and is not duplicated into this strings lane.",
        },
        "structure_results": {name: report["result"] for name, report in reports.items()},
        "translation_quality_review_performed": False,
        "status": STATUS,
        "qa": QA,
        "source_authority": SOURCE_AUTHORITY,
        "english_reference_used": False,
        "official_membership_handling": "Only old keys were mechanically retained; official new prose was skipped.",
    }
    write_json(OUT / "system_ui_summary.json", summary)

    output_hashes = {
        path.name: sha256(path)
        for path in sorted(OUT.glob("screens.*")) + sorted(OUT.glob("script.*"))
    }
    output_hashes["system_ui_summary.json"] = sha256(OUT / "system_ui_summary.json")
    output_hashes[Path(__file__).name] = sha256(Path(__file__))
    write_json(OUT / "screens_script_output_hashes.json", output_hashes)

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(json.dumps(output_hashes, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
