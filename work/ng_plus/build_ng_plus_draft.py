from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


CATALOG = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\catalog\scenario_NG_plus.catalog.jsonl")
SOURCE_RPY = Path(
    r"C:\Users\CadriacLord\Documents\Codex\2026-08-10\f-down-fatal-twelve-incl-dlc"
    r"\work\jp_recovery\raw\scenario\NG_plus.rpy"
)
OUT_JSON = Path(
    r"P:\AI\Codex\projects\fatal-twelve-ko\translations\draft\scenario"
    r"\NG_plus_exact_first_draft.json"
)
OUT_RPY = OUT_JSON.with_suffix(".rpy")


# Japanese-source-only first draft.  These strings have intentionally not
# received a prose QA/correction pass; that pass is deferred until every
# scenario has a complete first draft.
T = {
    1: "불길한 예감이 들었기 때문일까.",
    2: "코구마 마오의 불길한 예감은 얄궂게도 대부분 맞아떨어진다.",
    3: "그것은 마오가 스마트폰에 깔아 둔 운세 앱보다도 훨씬 정확했다.",
    4: "「……아침부터 우울하네」",
    5: "오늘은 분명 무슨 안 좋은 일이 생길 거다.",
    6: "그렇게 생각했기 때문일까.",
    7: "마오는 문득 옛일을 떠올렸다.",
    8: "마오가 미하루와 처음 만났을 때의 일이었다.",
    9: "중학교 ２학년이 된 봄, 반 배정이 이뤄지고 약 일주일이 지났을 무렵.",
    10: "마오는 아직 새 반에 녹아들지 못했다.",
    11: "반 친구가 말을 걸면 방긋 웃으며 이야기를 나눴고, 마오가 먼저 말을 걸어도 무시당하는 일은 없었다.",
    12: "그저 함께 어딜 놀러 가거나 점심을 먹는 일이 없었을 뿐이다.",
    13: "새 반이 된 지 얼마 안 됐으니 딱히 이상한 일도 아니었다.",
    14: "하지만 마오는 그때 이미 혼자라도 상관없다고 마음을 정한 상태였다.",
    15: "「……재미없네」",
    16: "모두 같은 곳을 바라보고, 같은 자세로 수업을 듣는다.",
    17: "잡지에 유행하는 옷이나 액세서리가 소개되면 똑같은 것을 걸친다.",
    18: "TV에서 하라주쿠의 크레페나 오모테산도의 팬케이크를 소개하면 똑같은 것을 먹으러 간다.",
    19: "군중 속에 파묻힌 반 친구들을 보며 마오는 지루함을 느꼈다.",
    20: "좀 자기가 좋아하는 걸 하면 되잖아.",
    21: "그 마음의 정체는 바로 이것이었다.",
    22: "누군가와 뜻을 맞추지 않으면 무언가를 좋아하거나 싫어하는 것, 즐겁다거나 지루하다고 느끼는 것조차――입에 담지 못하는 아이들이 싫기까지 했다.",
    23: "SNS도 마오는 전혀 하지 않았다.",
    24: "그런 곳에 있는 거라곤 겉치레 감정이나 전자레인지로 뚝딱 만들어질 법한 즉석 고민뿐이다.",
    25: "전부 아무래도 좋았다.",
    26: "그래서 마오는 빨리 고등학생이 되고 싶었다.",
    27: "그러면 아르바이트를 할 수 있다. 학교 밖 공동체에 속할 수 있다.",
    28: "밖에 나가면 분명 자신이 싫어지지 않을 사람이 있을 거라고.",
    29: "「하아……」",
    30: "이날도 평소처럼 혼자 등교하고 혼자 하교할 생각이었지만, 이를 가로막듯 반 친구들이 말을 걸어왔다.",
    31: "비교적 외모가 괜찮아 교실 내 서열 상위권에 자리한 ３인조였다.",
    32: "――미시마 씨 알아?",
    33: "이름만 아는 것도 안다고 친다면, 같은 반이니 마오도 안다고 할 수 있었다.",
    34: "미시마 미하루.",
    35: "사립 아메차여자대학 부속중학교의 특기생이며, 성숙한 외모는 연예 기획사에서 스카우트 제의를 받을 정도였다.",
    36: "마오는 질문을 던진 반 친구의 표정만 보고도 다음에 무슨 말이 나올지 쉽게 짐작했다.",
    37: "――왠지 좀 짜증 나지 않아?",
    38: "「네, 정답」",
    39: "그 말에 놀란 듯한 반 친구에게 마오는 「아무것도 아냐」라고 답했다.",
    40: "요약하면 단순한 이야기였다.",
    41: "눈에 거슬리고 짜증 나니 반 모두가 무시하자는 것이었다.",
    42: "당사자가 교실 안에 있는데도 용케 그런 말을 한다며 마오는 감탄했다.",
    43: "「난 패스」",
    44: "그래도 마오는 무난하게 대답했다.",
    45: "가담하지도, 말리지도 않고, 그저 거리를 둘 뿐.",
    46: "――코구마 씨는 냉정하니까. 뭐, 원래 미시마 씨랑 얘기한 것도 아니니 상관없나.",
    47: "반 친구는 그렇게 말하고는 마오를 따돌림 패거리에 끌어들이는 걸 포기한 모양이었다.",
    48: "듣고 보니 마오는 애초 미하루와 대화를 나눈 적도 없었고, 말할 일도 없었다.",
    49: "평소대로 있기만 해도 그 아이들이 바라는 대로 되는 셈이다.",
    50: "「냉정하다, 이거지」",
    51: "반 친구들 눈에는 자신이 그렇게 보인다는 사실을 마오는 하나 배웠다.",
    52: "자기들의 제안을 매몰차게 거절하니 냉정하다.",
    53: "그 아이들 입장에서는 가담하면 같은 무리에 끼워 줘도 좋다는 식으로 생각하는 듯하다고 마오는 짐작했다.",
    54: "그 아이들은 어째서인지 조그만 도시의 조그만 학교, 그 안에서도 더 조그만 반에서 서열 상위에 있다는 걸 진지하게 지위로 여겼다.",
    55: "「저런 걸 보고 꼴사납다고 하나?」",
    56: "마오는 턱을 괸 채 어이없다는 듯 중얼거렸다.",
    57: "그때 마오는 문득 생각했다.",
    58: "그러고 보니 미시마 미하루는 무슨 생각을 하고 있을까.",
    59: "아무렇지도 않게 따돌림을 제안하는 반 친구들과 다른 생각을 품은 건 틀림없었다.",
    60: "반을 포기하고 자신의 자리를 밖에서 찾기에는 아직 이를지도 모른다고 생각했다.",
    61: "그래서 행동에 나서기까지는 순식간이었다.",
    62: "「있잖아, 옥상에서 밥 먹지 않을래?」",
    63: "마오는 미하루 자리까지 가서 그렇게 물었다.",
    64: "반 친구들은 기겁한 눈으로 마오를 바라봤지만, 마오는 전부 무시했다.",
    65: "그러자 시선이 더욱 집중됐다.",
    66: "「너와 식사한다고 해서 나한테 뭐 좋은 일이 있나? 아무리 생각해도 없을 것 같은데」",
    67: "미하루는 책상 위에 펼쳐 둔 참고서에서 한 번도 눈을 떼지 않은 채, 천천히 또렷한 말투로 그렇게 말했다.",
    68: "마오는 얼굴이 새빨개진 채 그 자리에 얼어붙었다.",
    69: "설마 자신이 그런 말을 들을 줄은 몰랐기 때문이다.",
    70: "마오는 다른 반 친구들에게 킥킥대는 비웃음을 받으며 자기 자리로 돌아갔다.",
    71: "하지만 웃고 있기는 마오도 마찬가지였다.",
    72: "아, 이거 좋다.",
    73: "이해할 수 없는 게 있다는 건 재미있다――그렇게 생각했기 때문이다.",
    74: "코구마 마오는 초등학생 때 우수한 아이였다.",
    75: "학교 시험에서는 늘 만점을 받았다.",
    76: "부모님이 시험 삼아 학원에 보내 보니 곧바로 중학교 입시를 권유받았다.",
    77: "코구마 집안은 경제적으로 여유가 있었다.",
    78: "마오는 시키는 대로 공부했다.",
    79: "성적 향상세를 보면 국내 최상위권 여학교나 국립중학교에 들어가는 것도 꿈은 아니라고 마오의 부모님은 믿었다.",
    80: "하지만 많은 아이가 그렇듯, 마오에게 공부만 하는 나날은 동시에 그 밖의 나날을 잃는 것과 같았다.",
    81: "그때부터였다.",
    82: "친구가 놀자고 하거나 보고 싶은 TV 프로그램이 있을 때면, 마오는 공부를 거부하고 자기 뜻을 우선하기 시작했다.",
    83: "마오는 자신이 하기 싫은 일에 분명히 싫다고 주장하기 시작했다.",
    84: "그러자 주변을 보는 눈도 달라졌다.",
    85: "――왜 다들 자기가 하고 싶은 걸 하지 않는 걸까.",
    86: "그런 나날을 보내고도 결국 마오는 아메차에 합격했다.",
    87: "학원 교사와 부모님은 편차치가 더 높은 곳도 노릴 수 있는데 하며 한탄하기도 했다.",
    88: "아메차보다 편차치가 높은 학교라 해 봐야 손에 꼽을 정도인데도.",
    89: "기대와 짐이 마오에게 같은 뜻이라는 걸 깨닫는 것은 훨씬 더 먼 훗날의 일이었다.",
    90: "그렇게 마오는 어떤 의미에서는 중학생다운 방식으로 비뚤어졌다.",
    91: "「미시마 씨?」",
    92: "하굣길에 마오는 미하루를 불러 세웠다.",
    93: "마오는 사람을 불편하게 대하는 성격은 아니었다. 따돌림 제안에는 차분히 대답했지만, 일상적인 대화라면 별문제 없이 말을 주고받았다.",
    94: "그래서 그렇게 매몰차게 대접받은 게 재미있었다.",
    95: "귀찮게 여겨도 좋고, 싫어해도 좋았다.",
    96: "미시마 미하루를 알고 싶다고 생각한 것이다.",
    97: "「……난 서둘러 돌아가야 해. 지금은 너와 이야기할 시간이 없어」",
    98: "역시나라고 해야 할까, 미하루의 대답은 이랬다.",
    99: "마오는 아하하, 하고 쓴웃음을 지으며 이날은 미하루의 뒷모습을 배웅했다.",
    100: "며칠이 지나도 마오와 미하루의 관계는 전혀 달라지지 않았다.",
    101: "이 무렵 마오는 아직 사람과 거리를 조절하는 데 서툴렀다.",
    102: "그래서 마오가 할 수 있는 일이라곤 끈질기게 미시마 미하루에게 말을 거는 것뿐이었다.",
    103: "미하루의 대답은 대개 늘 같았다.",
    104: "「그래도……」",
    105: "지난 며칠 사이 마오의 마음에는 한 가지 의문이 떠올랐다.",
    106: "「왜 무시하지 않는 걸까」",
    107: "귀찮다면 자신 따위 무시하면 될 텐데, 하고 마오는 생각했다.",
    108: "이 의문의 답을 알고 싶다는 마음도 마오 안에서 피어났다.",
    109: "그러던 중 반에 한 가지 소문이 퍼졌다.",
    110: "――미시마 미하루는 손목을 긋는다.",
    111: "통계상 수치로 보면 자해하는 여중생은 전혀 드물지 않을 것이다.",
    112: "마오도 어디선가 11명 중 １명 정도는 경험이 있다고 들은 적이 있었다.",
    113: "하지만 다행인지 불행인지 이 학교에는 자해 경험자가 적었다.",
    114: "게다가 원래 여러모로 질투의 대상이던 미하루의 어두운 면이 드러났기에 소문이 퍼진 것이었다.",
    115: "미하루를 무시하자고 제안했던 반 친구는 다시 마오에게 말을 걸었다.",
    116: "――미시마 씨가 왜 계속 긴팔 입는지 알아?",
    117: "――손목 긋는다더라.",
    118: "――자기가 힘들다는 티를 내는 건가? 진짜 역겹지 않아?",
    119: "마오는 한 치의 망설임도 없이 대답했다.",
    120: "「뭐가?」",
    121: "그 말은 진심에서 나온 것이었다.",
    122: "반 친구가 하는 말을 이해할 수 없었기 때문이다.",
    123: "시간을 두고 생각하면 마오는 그 아이가 왜 「역겹다」고 느끼는지 이유는 알 수 있었을 것이다.",
    124: "그래도 마오는 그 순간 상대를 전혀 이해할 수 없었다.",
    125: "「그야 자기 일이잖아. 하고 싶은 대로 하면 되는 거 아냐?」",
    126: "빈정거림 없는 말투로 그렇게 대답했다.",
    127: "반 친구는 「뭐어?!」 하고 놀란 소리를 질렀다.",
    128: "그 뒤로 대화는 이어지지 않았고, 「마오야, 이상해」라는 말만 남기고 그 아이는 떠났다.",
    129: "마오에게는 아무래도 좋은 일 중 하나였다.",
    130: "다음 날 마오가 등교하자, 미하루가 또각또각 발소리를 내며 마오 쪽으로 다가왔다.",
    131: "의외라고 마오는 생각했다.",
    132: "「……코구마 씨」",
    133: "지금까지 미하루 쪽에서 먼저 마오에게 말을 건 적은 없었기 때문이다.",
    134: "「이번에는 내가 제안을 받았어. 코구마 씨를 무시하지 않겠냐고」",
    135: "애초 미하루를 무시해 봤자 미하루는 그 아이들에게 말을 걸지 않는다.",
    136: "그렇다면 다 같이 무시해도 효과가 없다.",
    137: "어제 마오가 그 아이들에게 동조하지 않은 일을 계기로 표적이 마오 쪽으로 바뀐 것이다.",
    138: "마오는 그 아이들과 아주 친하게 지내지는 않아도, 미하루처럼 벽을 쌓지는 않았다.",
    139: "――우리한테 대든 마오를 괴롭혀 주자.",
    140: "그 아이들의 사고방식은 단순명료했다.",
    141: "미하루는 마오가 말을 걸어도 벽을 친 채지만 무시하지는 않는다.",
    142: "그런 미하루가 갑자기 마오를 무시하기 시작하면 통쾌하리라고 그 아이들은 생각했다.",
    143: "「그래서 내가 먼저 그 아이들을 무시해 줬지. 그때 분해하던 표정은 정말 통쾌했어」",
    144: "미하루는 당당히 그렇게 말해 버리고는 교실로 돌아갔다.",
    145: "마오는 그런 미하루를 보고 묘한 기분이 들었다.",
    146: "마오가 자기 자리에 앉아 있자 그 반 친구가 말을 걸어왔다.",
    147: "――있잖아, 내 말 좀 들어 봐. 미시마 씨가 말이야.",
    148: "이야기는 그런 식으로 시작됐다.",
    149: "마오를 무시하자는 제안을 해 놓고도 곧장 자신에게 말을 거는 게 대단하다고 마오는 생각했다.",
    150: "물론 그 아이들은 미하루에게 했던 말은 숨긴 채, 미하루가 자기들을 무시했다는 이야기만 마오에게 했다.",
    151: "미하루에게 무시당한 게 분했던 듯 이번에는 무시가 아니라 괴롭혀 주겠다――두서없는 이야기를 요약하면 그런 뜻이었다.",
    152: "「아, 진짜. 싫어, 싫어!」",
    153: "마오는 참지 못하고 양손을 치켜들며 그렇게 외쳤다.",
    154: "반 친구는 어리둥절한 얼굴로 마오를 바라봤다.",
    155: "「그런 거 전부 귀찮아」",
    156: "「날 무시할 거면 무시해도 되니까, 나까지 끌어들이지 마」",
    157: "마오는 일부러 힘차게 윙크하며 그렇게 대답해 보았다.",
    158: "그러자 그 아이들은 소리치는 것조차 잊을 만큼 화가 나, 이내 마오 앞에서 사라졌다.",
    159: "「아, 속 시원해」",
    160: "마오는 그렇게 말하고 기지개를 켠 뒤 태연히 하루를 보냈다.",
    161: "그 뒤 마오와 미하루가 함께 점심을 먹게 되기까지는 조금 더 시간이 걸렸다.",
    162: "거기에 극적인 사건 같은 건 없었다. 반에서 겉돌게 된 두 사람이 자연스레 붙어 다닌다는, 굳이 말하면 부정적인 방식으로 거리가 가까워졌다.",
    163: "반에서는 그 반 친구의 SNS 뒷계정이 들통나 무리에서 쫓겨나거나, 그 틈에 다른 무리가 끼어들어 자리를 차지하는 등 갖가지 인간관계 변화가 일어났다.",
    164: "그러는 사이 그 아이들의 괴롭힘 대상이 될까 두려워하던 다른 반 친구들도 차츰 이 모든 게 바보 같다고 여기게 됐다.",
    165: "마오는 반에서 적당히 대화를 나누는 위치가 되었고, 미하루는 여전히 기피됐다――즉, 원래대로 돌아온 것이다.",
    166: "하지만 달라진 점도 있었다.",
    167: "마오와 미하루가 남에서 친구가 되었다는 사실만큼은 원래대로 돌아가지 않았다.",
    168: "「있잖아, 마오」",
    169: "「왜 그래, 미하룽?」",
    170: "「싫은 건 싫다고 해도 되는 거구나」",
    171: "「난 그렇게 생각해」",
    172: "한숨을 쉬며 마오는 그렇게 대답했다.",
    173: "그리고 젓가락으로 도시락의 가지 절임을 집어 미하루 입속에 넣었다.",
    174: "「난 가지가 싫으니까, 이래도 되는 거야」",
    175: "「정말이지, 너는……」",
    176: "미하루도 한숨을 쉬면서, 뱉을 수도 없어 절임을 꼭꼭 씹어 삼켰다.",
    177: "옥상의 메마른 공기는 마오도 미하루도 좋아하게 되었다.",
    178: "「흐아, 그립네」",
    179: "마오는 하품하며 마음속으로 중얼거렸다.",
    180: "미하루와의 첫 만남을 떠올린 뒤, 이번에는 린카와 처음 만났을 때를 떠올리려 했다.",
    181: "하지만 마오는 도중에 그만뒀다.",
    182: "과거에 생각이 미치는 건 으레 무슨 일이 있을 때였다.",
    183: "불길한 예감은 맞지 않는 편이 좋다.",
    184: "「뭐가 있더라도 기껏해야 불시 쪽지시험 정도면 좋겠네」",
    185: "소원을 빌듯 그렇게 말하고 마오는 전철에 올라탔다.",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    records = [
        json.loads(line)
        for line in CATALOG.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    expected = set(range(1, 186))
    assert {r["command_index"] for r in records} == expected
    assert set(T) == expected
    assert len({r["stable_id"] for r in records}) == 185
    assert len({r["localization"]["translation_id"] for r in records}) == 185

    entries = []
    rpy = [
        "# Auto-generated Korean first draft for scenario/NG_plus items 1..185.",
        "# Semantic source: Japanese only. Prose QA is deferred.",
        "# Translation engine: Codex internal model; no external translation API.",
        "# status: first_draft_unreviewed",
        "# qa: deferred_until_full_first_draft",
        "",
    ]
    lane_counts: Counter[str] = Counter()
    voice_count = 0
    for rec in records:
        seq = rec["command_index"]
        source = rec["source"]
        target = T[seq]
        speaker = rec["speaker"]["code"] if rec["speaker"] else None
        voice = rec["voice_call"]
        protected = rec["protected_tokens"]
        for token in protected:
            value = token["value"]
            assert source["text_ja"].count(value) == target.count(value), (
                seq,
                value,
                source["text_ja"],
                target,
            )
        layout = rec["layout"]
        if layout["starts_with_corner_quote"]:
            assert target.startswith("「"), (seq, target)
        if layout["ends_with_corner_quote"]:
            assert target.endswith("」"), (seq, target)

        lane_counts[rec["lane"]] += 1
        if voice:
            voice_count += 1
        entry = {
            "sequence": seq,
            "stable_id": rec["stable_id"],
            "translation_id": rec["localization"]["translation_id"],
            "translation_id_origin": rec["localization"]["id_origin"],
            "translation_id_exactness": "exact_recomputed_renpy_6_99_japanese_canonical_code",
            "menu_key": rec["localization"]["menu_key"],
            "source_file": source["script"],
            "source_line": source["line"],
            "source_label": source["label"],
            "item_type": rec["lane"],
            "speaker": speaker or "narrator",
            "speaker_name_jp": rec["speaker"]["display_name_ja"] if rec["speaker"] else None,
            "source_jp": source["text_ja"],
            "source_statement": source["statement_code"],
            "source_group_code": source["group_code"],
            "voice_call": voice["statement"] if voice else "",
            "voice_line": voice["line"] if voice else None,
            "protected_tokens": protected,
            "draft_ko": target,
            "source_authority": "Japanese only",
            "english_reference_used": False,
            "external_translation_api_used": False,
            "translation_engine": "Codex internal model",
            "status": "first_draft_unreviewed",
            "qa": "deferred_until_full_first_draft",
        }
        entries.append(entry)

        rpy.extend(
            [
                f"# sequence: {seq}",
                f"# source: {source['script']}:{source['line']}",
                f"# source_jp: {source['text_ja']}",
                f"translate korean {entry['translation_id']}:",
            ]
        )
        if voice:
            rpy.append(f"    {voice['statement']}")
        statement = json.dumps(target, ensure_ascii=False)
        rpy.append(f"    {speaker + ' ' if speaker else ''}{statement}")
        rpy.append("")

    packet = {
        "packet_id": "scenario_NG_plus_exact_first_draft",
        "source_file": "scenario/NG_plus.rpy",
        "sequence_start": 1,
        "sequence_end": 185,
        "source_line_start": records[0]["source"]["line"],
        "source_line_end": records[-1]["source"]["line"],
        "entry_count": len(entries),
        "item_counts": dict(sorted(lane_counts.items())),
        "voice_count": voice_count,
        "semantic_source_language": "Japanese",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "translation_engine": "Codex internal model",
        "translation_id_method": "Ren'Py 6.99 canonical Japanese AST digest",
        "status": "first_draft_unreviewed",
        "qa": "deferred_until_full_first_draft",
        "style_guide": {
            "path": r"P:\AI\Codex\projects\fatal-twelve-ko\style_guide.md",
            "sha256": "b2b87352fdfd9b25af688152b0ce8a7460ffeb88fc06ae6e45f1c5df2ae83891",
        },
        "glossary": {
            "path": r"P:\AI\Codex\projects\fatal-twelve-ko\glossary_draft.json",
            "sha256": "d7b49d77fcde5da240cb816890c75f9f15a2e83544db34a6193b8e939906300e",
        },
        "inputs": {
            "japanese_rpy": {"path": str(SOURCE_RPY), "sha256": sha256(SOURCE_RPY)},
            "japanese_only_catalog": {"path": str(CATALOG), "sha256": sha256(CATALOG)},
        },
        "entries": entries,
    }
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(
        json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    OUT_RPY.write_text("\n".join(rpy), encoding="utf-8")
    print(json.dumps({
        "json": str(OUT_JSON),
        "rpy": str(OUT_RPY),
        "entries": len(entries),
        "lanes": dict(lane_counts),
        "voices": voice_count,
        "json_sha256": sha256(OUT_JSON),
        "rpy_sha256": sha256(OUT_RPY),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
