from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from materialize_root_011_02_and_GH import (
    FW_TRANS,
    QUOTE_CHARS,
    ROMAN_RE,
    RUBY_TAG_RE,
    TAG_RE,
    load_jsonl,
    scope_structure_audit,
    sha256,
    validate_record,
    write_jsonl,
)


BASE = Path(__file__).resolve().parent
MASTER_PATH = BASE / "output" / "masters" / "scenario_012_01F.master.json"
SEED_PATH = BASE / "reviews" / "ROOT.corrections.jsonl"
OUTPUT_PATH = BASE / "reviews" / "ROOT.012_01F.consolidated.corrections.jsonl"
REPORT_PATH = BASE / "reviews" / "ROOT.012_01F.consolidated.report.json"
SCRIPT = "012_01F"
EXPECTED_CHECKED = 1190


# 일본어 source_jp만 의미 기준으로 삼아 확정한 수동 교정이다.
# tuple: (sequence, new_ko, category, reason)
MANUAL_DECISIONS = [
    (1, "「좋은 저녁. 아니면 좋은 아침. 안녕하세요……는 아니려나」", "명백한 부자연스러움", "こんにちは를 좋은 낮이라고 옮긴 부자연스러운 인사말 교정"),
    (6, "「너는 마침내 네게 가장 근원적인 조각을 손에 넣었다. 이제 그 조각을 끼우면 원풍경이 완성된다」", "용어", "原風景을 후반부의 원풍경 용례와 통일"),
    (30, "그리고 카드북에 새 카드가 생겨난 것을 알아차렸다.", "용어", "고정 용어 카드북의 띄어쓰기 통일"),
    (39, "하지만 오늘 아침만은 레테가 그대로 가게 두고 싶지 않았다.", "주체/의미", "そうはさせたくなかった의 대상과 저지 의도 복원"),
    (50, "레테가 아니라 린다 씨의 고양이 레오에게 있어야 할 상처다.", "의미", "レオが負っているはずの傷가 레오에게 있어야 하는 상처라는 모순 관계 복원"),
    (53, "레테가 어디선가 다쳤을 수도 있지만, 나는 그럴 가능성이 낮다고 생각했다.", "문법/중복", "가능성 표현의 중복과 조건 구조 교정"),
    (72, "그래서 시험 휴일 동안에는 아침과 저녁 시간대에 가게 문을 열 생각이었다.", "문법/의미", "朝と夕方から를 아침과 저녁부터라고 연결한 부자연스러운 시간 표현 교정"),
    (125, "「사람 같은 의지와 윤곽만 주어진 존재. 사람도 고양이도――물론 신도 아니지. 그게 바로 나다」", "용어/의미", "意思를 의사가 아닌 의지로 교정"),
    (136, "「파르카라는 존재에게서 인간 같은 의지가 사라지지 않을 아슬아슬한 선까지 말이야」", "조사", "存在から의 기점 조사를 존재에게로 옮긴 오류 교정"),
    (144, "「그렇기에 무자비하게 선정 관리자의 역할을 계속하며 자신의 존재를 유지해 왔지」", "문법/의미", "選定の管理者を続け의 역할 지속과 존재 유지 관계 자연화"),
    (163, "그리고 선정 기간에 태어나, 그 생명이 없던 일이 되지 않은…….", "문법/의미", "なかったことにならなかった의 없던 일이 되지 않았다는 구조 복원"),
    (194, "「마지막으로 하나 사과하지. 이번 ≪여신의 선정≫이 시작될 무렵 네 기억을 뽑아낸 것도 역시 나다」", "문법/중복", "始まった当初의 처음 시작되었다는 중복 표현 교정"),
    (197, "「――아니, 말을 바꾸지. 지금 내 주인은 너다. 네 친구들도 알고 있어. 네가 행복해지려면 둘 다 살아남는 것이 전제 조건이었잖아?」", "문법/어순", "君のご友人も私は知っている의 부자연스러운 주어·목적어 어순 교정"),
    (218, "우리가 살아 있을 가능성이 있는 바로 그날이다.", "문법/중복", "生きる可能性がある의 가능성이 존재한다는 중복 서술 교정"),
    (223, "나는 숨을 들이켜고 통화 버튼을 눌렀다.", "명백한 직역", "息を飲む를 숨을 삼키다로 옮긴 직역 교정"),
    (236, "과로로 쓰러졌다고 보기에는 상태가 달랐고, 의사도 그저 링거를 놓고 재우는 것 말고는 할 수 없는 모양이었다.", "의미/문법", "과로로 쓰러진 과거 사례처럼 바뀐 비교 구조를 원인 판단으로 복원"),
    (266, "「그리고 지금 우리가 해야 할 일은 ≪여신의 선정≫에 관해 생각하는 거야」", "조사", "대상을 직접 목적격으로 둔 부자연스러운 考える 조사 교정"),
    (270, "내가 초조해하니까 애써 침착하려는 것뿐이다.", "주체/문법", "冷静でいようとしてくれている의 배려 주체와 부자연스러운 보조 표현 교정"),
    (277, "그리고 나는 미하루에게 레테에게서 들은 이야기를 하기로 했다.", "조사", "미하루에게 레테에게라는 중복 조사에서 정보 출처 조사 복원"),
    (292, "그 원인을 알고 있을지도 모르고, 망각하게 할 수 있다면 기억을 어느 한쪽으로 통일하는 일도 가능할지 모른다.", "오역/문법", "知っているかもしれない를 알지 못한다는 뜻으로 읽히는 표현 교정"),
    (295, "그 부정의 뜻이 단순히 내 질문에 대한 대답만은 아니라는 사실을 곧 깨달았다.", "주체/문법", "否定の意志와 질문에 답한 행위의 잘못된 주어 관계 교정"),
    (319, "우리는 말 대신 한숨으로 대답했고, 마오는 나오미의 어머니에게 들은 이야기를 이어 갔다.", "명백한 직역", "言葉にならない吐息의 말이 되지 않는 한숨이라는 직역 교정"),
    (336, "오늘이 수요일이기도 해서 나는 갈수록 초조해지기 시작했다.", "시점/의미", "水曜日ということもあり의 이유 관계와 いよいよ의 고조 복원"),
    (353, "고개를 숙인 내 뺨에 강렬한 열기가 번졌다. 동시에 짝, 하는 소리가 방 안에 울렸다.", "명백한 부자연스러움", "뺨에 열기가 내달린다는 부자연스러운 신체 묘사 교정"),
    (363, "미하루는 입술을 떨며 뺨을 감싸고 있는 나를 내려다보고 있었다.", "주체/문법", "입술을 도구로 내려다보는 것처럼 된 수식 관계 교정"),
    (385, "둘 다 기억이라는 요소가 깊이 관련되어 있다는 점에서 무관하다고는 생각할 수 없다.", "문법/어휘", "기억이라는 말이 관련된다는 부자연스러운 결합 교정"),
    (416, "그 말투는 지금까지의 나오미와 달랐고 내 귀에 익은 것이었다.", "조사", "내게 귀에 익다는 이중 조사 교정"),
    (427, "그 가능성이 뇌리에 떠오르자 내 안에서 말로 표현하기 힘든 긴장감이 치솟았다.", "주체/문법", "나는 긴장감이 치솟는다는 주어 충돌 교정"),
    (454, "「슬슬 대학 입시도 생각해야 하고, 하아, 우울해」", "용어/자연스러움", "受験을 문맥상 대학 입시로 명확화하고 수험을 생각한다는 표현 교정"),
    (455, "우리 학교는 일단 진학 중심 학교라서 대부분의 학생은 고등학교에 입학할 때부터 대학 입시 공부를 시작한다.", "용어/자연스러움", "進学校의 일본식 직역을 자연스러운 학교 성격 표현으로 교정"),
    (458, "「괜찮아. 진학 중심 학교인 만큼 아메차의 정기시험은 수준이 높아. 우선 학교 공부부터 제대로 하면 입시 공부의 토대가 될 거야」", "용어/자연스러움", "進学校와 受験勉強의 일본식 직역을 문맥에 맞게 통일"),
    (499, "미하루의 질문은 나도 궁금했던 것이었다.", "명백한 부자연스러움", "질문을 품었다는 부자연스러운 결합 교정"),
    (522, "「나오미 님의 뇌 안에서 일어난 기억의 격류끼리 부딪치면서 생긴 부담으로 나오미 님은 의식을 잃었습니다」", "문법/오자", "부딪쳐 주는 부담이라는 잘못된 동사 연결을 인과 관계로 교정"),
    (591, "레테에게서는 힘이 다 빠진 듯한 희미한 울음소리만 들린다.", "문법/자연스러움", "쇠약해진이 소리를 직접 수식하는 잘못된 관계와 고양이 울음 표현 교정"),
    (606, "나오미의 몸을 빌리고 있는 다이아나에게 도쿄를 구경시켜 주기 위해서다.", "조사/의미", "ダイアナに東京を案内する의 안내 대상과 내용 관계 자연화"),
    (607, "레테를 쿠션에 눕히고 근처에 충분한 양의 물과 밥을 놔두었다.", "조사", "레테는 눕히고라는 목적어 조사 오류 교정"),
    (616, "그러고 보니 역에서 만난 뒤로도 자동 개찰구와 자동판매기, 잦은 전철 운행과 역 건물 등 눈에 들어오는 거의 모든 것에 놀랐다.", "문법/어휘", "전철 운행 횟수가 많다는 뜻의 부자연스러운 명사 수식 교정"),
    (631, "가미나리몬은 헤이안 시대에 만들어진 것으로 기억하고 있었기에, 다이아나의 말을 처음 들었을 때는 의문이 들었다.", "문법/자연스러움", "발언에 물음표가 떠올랐다는 직역과 시간 관계 교정"),
    (639, "「나도 자료 사진으로만 알지만…… 분명 잿더미에서 일어선 새빨간 탑은 단순한 전파탑 이상의 가치가 있었을 거야」", "용어", "ラジオ塔를 한국어 용례에 맞는 전파탑으로 교정"),
    (643, "그렇게 말하더니 다이아나는 창밖을 바라보며 눈을 가늘게 떴다.", "문법/직역", "窓の外を見る目を細めた를 창밖을 보는 눈으로 직역한 수식 관계 교정"),
    (650, "마지막 목적지인 신주쿠교엔으로 이동해 왔다.", "조사/자연스러움", "마지막으로 둘러볼 곳으로 이동한다는 부자연스러운 목적지 표현 교정"),
    (659, "「일본 정원과 영국 정원, 프랑스 정원. 가능하기만 했다면 정취가 서로 다른 이 풍경들을 계절마다 즐기고 싶었어요」", "문법/의미", "できることならば의 아쉬운 가정과 목적어·서술 관계 교정"),
    (666, "그럴 만도 하다.", "관용구/의미", "無理もない를 앞선 무응답이 당연하다는 관용 의미로 교정"),
    (674, "나오미와는 가 본 적이 있지만 다이아나는 가 본 적이 없다.", "문법/누락", "후반 절에 行ったこと가 생략되어 다이아나 자체가 없다는 문장이 된 오류 교정"),
    (692, "그래서 나는 무난하게 커피를, 다이아나는 코코아를 주문했다.", "주체 누락", "첫 번째 주문의 주체인 화자를 복원"),
    (707, "「하지만 말투를 흉내 내는 건 피곤하답니다. 그러니 지금은 제 모습 그대로 있게 해 주세요」", "명백한 직역", "自然体でいる를 자연스럽게 있게 해 달라고 옮긴 직역 교정"),
    (711, "안 그래도 지금 나오미의 모습으로 다이아나가 말하고 있는 것만 해도 조금 위화감이 드니까.", "의미/주체", "다이아나의 말투를 흉내 내는 나오미가 아니라 나오미의 몸으로 말하는 다이아나라는 주체 관계 복원"),
    (712, "「기다리게 해서 죄송합니다」", "문법/자연스러움", "접객 인사 お待たせいたしました의 자연스러운 한국어 표현 교정"),
    (717, "오후부터 시작한 빠듯한 일정이라 실제로는 상당히 서둘러 둘러봐야 했다.", "오역/문법", "急なスケジュール를 갑작스러운 일정으로 옮긴 의미와 이동 동작 복원"),
    (722, "「그보다 나오미 님을 여러 곳에 데려가 주세요. 그래요. 지금껏 응석을 참아 온 제 마지막 응석입니다」", "문법/의미", "我儘의 반복 의미와 부자연스러운 제멋대로인 부탁 표현 교정"),
    (727, "미하루, 다이아나의 기억이 겉으로 드러난 나오미, 나.", "명백한 직역", "記憶が表に出ている의 표면에 나왔다는 직역 교정"),
    (736, "나는 휘청이는 걸음으로 다가오는 고양이 한 마리를 발견했다.", "어휘/의미", "頼りない足取り를 불안한 감정이 아닌 불안정한 걸음으로 복원"),
    (739, "「이 아이도 이야기를 듣고 싶었던 거군요」", "조사", "이야기가 듣고 싶다는 주격 조사 오류 교정"),
    (741, "그 평온한 표정은 나오미가 한 번도 지은 적 없는 것이었다.", "문법", "표정과 얼굴을 동일시한 서술 관계 교정"),
    (759, "「≪여신의 선정≫이 시작됐을 때는 설마 이런 밤이 오리라고는 생각지도 못했어」", "문법", "선정이 시작했다는 타동사·주어 관계 교정"),
    (766, "나는 미하루의 아름다운 미소를 보며 힘주어 고개를 끄덕였다.", "명백한 직역", "しっかり를 확실히 고개를 끄덕였다고 옮긴 표현 교정"),
    (771, "나 같은 건 불안정한 존재다.", "뉘앙스 누락", "自分なんて의 자기 비하 뉘앙스 복원"),
    (778, "레테는 가느다란 울음소리를 낸다.", "문법/자연스러움", "고양이가 가느다란 목소리로 운다는 부자연스러운 鳴く 표현 교정"),
    (803, "끝없이 펼쳐진 어둠 속에서 나는 미하루와 마주 보고 있었다.", "문법/중복", "끝없는 넓은 어둠이라는 겹수식 교정"),
    (809, "그러나 여신 파르카와의 결판을 우리 손으로 내야 한다는 사실에는 아무런 변함이 없다.", "용어/문법", "決着をつける를 결말을 낸다고 옮긴 부자연스러운 결합 교정"),
    (821, "「제가 운명을 볼 때는 귀하와 같은 방식으로 인식하는 것이 아닙니다」", "문법/의미", "당신처럼 인식하며 본다는 중복 서술과 관측 방식의 비교 관계 교정"),
    (823, "「예를 들어 참가자 12명이 모두 계셨을 때, 저는 여러분이 각자 ≪운명의 종착점≫에 도달하는 미래를 따로따로 보고 있었습니다」", "문법/숫자", "12人の皆サマ의 어색한 배열과 문장 주어 관계 교정"),
    (829, "세계 입장에서는 오히려 지금이 비정상적인 상태다.", "조사/문법", "世界というものにとって의 관점 조사와 상태 서술 관계 교정"),
    (862, "여신은 드물게 얼굴을 일그러뜨리며 불쾌한 표정을 지었다.", "문법/중복", "표정을 일그러뜨리고 불쾌한 얼굴을 했다는 중복·결합 오류 교정"),
    (872, "레테가 내 기억을 차례로 되돌려 줄 때도 나름의 의미가 있었듯이.", "주체/문법", "記憶を戻していく의 수여 주체와 부자연스러운 진행 표현 교정"),
    (879, "「당신의 육체는 아무래도 저와 동질적입니다. 다른 어느 참가자와도 달리 친근감을 느꼈습니다」", "문법/의미", "불완전 명사문과 他の参加者の誰とも違った의 비교 관계 교정"),
    (884, "「후후, 후후. 그렇다면 이걸로 지명자는 아무도 없지 않습니까」", "문법", "지명자는 없는 것이라는 부자연스러운 존재 부정 교정"),
    (887, "파르카는 무자비하게 그렇게 말하고 회전하던 시계를 멈추더니 아무것도 없는 공간을 걸어간다.", "어휘/의미", "回る時計가 돌아가던 시계로 읽히는 모호한 이동 표현 교정"),
    (896, "파르카는 뒤돌아보며 경악에 찬 소리를 질렀다.", "명백한 부자연스러움", "경악한 목소리를 냈다는 부자연스러운 동작 표현 교정"),
    (924, "겉모습은 파르카였지만 풍기는 분위기는 지금까지와 달랐다.", "명백한 직역", "분위기를 몸에 두른다는 まとっている의 직역 교정"),
    (933, "잠시 뒤 그녀는 짧게 숨을 들이마시고는, 쥐어짜듯 힘겨운 목소리로 말했다.", "문법/자연스러움", "숨을 작게 들이마시고 목소리를 낸다는 부자연스러운 동작 연결 교정"),
    (934, "「그럼 Ⅰ번 님께서 저를 지명한 것으로 하죠」", "의미/문법", "Ⅰ番サマによるワタクシの指名을 앞으로 지명하게 한다는 사역 의미가 아니라 해당 지명을 집행하는 의미로 교정"),
    (935, "지금까지의 지명과 마찬가지로 Ⅰ번이라 적힌 바닥이 움직이기 시작한 건 그 직후였다.", "어휘/문법", "この直後를 바로 뒤라고 옮긴 시간 표현 교정"),
    (949, "「정말 그저 시스템이었다면 귀하를 차지하려고 생각하지는 않았을 테니까요」", "어휘/의미", "육체를 차지하는 頂戴する를 받는다고 약화한 표현 교정"),
    (958, "「귀하는 그 에너지를 사용해 귀하도 Ⅱ번 님도 살아 있는――죽음이 없던 일이 되어 있는――지금의 세계를 고정해 주세요」", "문법/의미", "死がなかったことになっている의 없었던 일이 되었다는 잘못된 관형 구조 교정"),
    (967, "「이곳은 어디까지나 꿈속. 귀하의 인식이 세계를 바꿉니다. 망설이지 말고 원하는 미래를 소망해 주세요」", "어휘/의미", "お望みの未来を願う가 바라보라는 뜻으로 읽히는 중의적 동사 교정"),
    (992, "「만약 인생을 다시 시작할 수 있다면――순순히 운명을 받아들이고 싶다. 저는 죽는 순간 그렇게 생각했습니다」", "오역/어휘", "素直に를 솔직하게로 옮긴 의미를 순순히 받아들인다는 뜻으로 복원"),
    (1009, "「어머, 입이 험한 본성이 나왔군요. 험한 건 눈매만으로 해 주세요」", "문법/말장난", "悪い의 입과 눈매를 잇는 반복을 자연스러운 한국어로 복원"),
    (1058, "여신이니까 예외다――그런 경우라면 분명 그 아이가 설명해 줬을 것이다.", "문법/누락", "なんてことがあれば의 가정 조건이 같은 일이었다면으로 붕괴한 부분 교정"),
    (1069, "파르카의 체구라면 업고 움직일 수도 있을 것이다.", "어휘/의미", "업을 수 있는 근거인 작은 체구를 키로 한정한 표현 교정"),
    (1101, "「즉 지금의 그녀는 그때 내가 빼앗지 않고 남겨 둔 기억이라고 보면 돼」", "문법/직역", "残りの記憶といえばいい의 설명 표현과 남겨 둔 기억의 관계를 자연화"),
    (1127, "그토록 쇠약한 검은 고양이가 되면서까지 우리를 위해 온 힘을 다해 주었다.", "문법/의미", "弱った黒猫になってしまってまで의 희생 정도를 되고도라고 약화한 표현 교정"),
    (1144, "「하지만 이제 시간이 없어. 이제는 네게 협력할 만큼 존재를 유지할 여력이 없지」", "문법/의미", "君に協力している存在の余裕의 존재 유지 여력과 협력 관계 자연화"),
    (1149, "「다시 여신이 되어 ≪인과의 때≫로 맺어진 12명을 골라 ≪여신의 선정≫을 열겠지」", "용어", "≪因果の刻≫의 고정 용어를 인과의 시간에서 인과의 때로 통일"),
    (1163, "「오히려 감사해야 할 쪽은 나야」", "명백한 직역", "お礼を言うのはこちらだ의 감사를 말할 쪽이라는 직역 교정"),
    (1177, "사실 짐작 가는 방법이 하나 있었다.", "조사/문법", "方法に心当たりがある의 방법에는 짚이는 데가 있다는 부자연스러운 결합 교정"),
    (1185, "그렇다면 당시 상황이 완전히 재현되지 않게 할 방법은 간단하다.", "문법/의미", "어떻게 해야 재현이 되지 않을지는 간단하다는 불완전한 의문절 교정"),
]


FULLWIDTH_DIGIT_RE = re.compile(r"[０-９]")
JP_RESIDUAL_RE = re.compile(r"[\u3041-\u3096\u30a1-\u30fa\u4e00-\u9fff]")


def apply_seed_mechanics(seed: dict, text: str) -> str:
    result = text
    if seed.get("category") == "typography":
        result = result.translate(FW_TRANS)
    if seed.get("category") == "term":
        replacements = (
            ("린카링", "리땅"),
            ("알란", "아란"),
            ("스콜피온", "스코피온"),
            ("다이애나", "다이아나"),
            ("운명의 대광장", "운명의 대회랑"),
        )
        for old, new in replacements:
            result = result.replace(old, new)
    return result


def main() -> None:
    master_hash_before = sha256(MASTER_PATH)
    seed_hash_before = sha256(SEED_PATH)
    master = json.loads(MASTER_PATH.read_text(encoding="utf-8-sig"))
    if master.get("script_key") != SCRIPT:
        raise SystemExit("script_key mismatch")
    entries = master["entries"]
    if len(entries) != EXPECTED_CHECKED:
        raise SystemExit(f"checked count mismatch: {len(entries)}")
    if [entry["sequence"] for entry in entries] != list(range(1, EXPECTED_CHECKED + 1)):
        raise SystemExit("non-contiguous master sequences")
    by_sequence = {entry["sequence"]: entry for entry in entries}
    by_id = {entry["stable_id"]: entry for entry in entries}
    if len(by_id) != len(entries):
        raise SystemExit("duplicate stable_id in master")

    manual_sequences = [decision[0] for decision in MANUAL_DECISIONS]
    if len(manual_sequences) != len(set(manual_sequences)):
        raise SystemExit("duplicate manual sequence")
    manual_rows = []
    for sequence, new_ko, category, reason in MANUAL_DECISIONS:
        entry = by_sequence.get(sequence)
        if entry is None:
            raise SystemExit(f"manual sequence missing: {sequence}")
        if entry["draft_ko"] == new_ko:
            raise SystemExit(f"manual no-op: {sequence}")
        manual_rows.append({
            "script": SCRIPT,
            "stable_id": entry["stable_id"],
            "sequence": sequence,
            "old_ko": entry["draft_ko"],
            "new_ko": new_ko,
            "category": category,
            "reason": reason,
            "reviewer": "ROOT",
        })

    all_seed_rows = load_jsonl(SEED_PATH)
    seed_rows = [row for row in all_seed_rows if row.get("script") == SCRIPT]
    if len(seed_rows) != 66:
        raise SystemExit(f"seed count mismatch: {len(seed_rows)}")
    for row in seed_rows:
        entry = by_id.get(row["stable_id"])
        if entry is None or row["sequence"] != entry["sequence"] or row["old_ko"] != entry["draft_ko"]:
            raise SystemExit(f"seed exact old guard failure: {row.get('sequence')}")

    final_by_id = {}
    provenance = {}
    for seed in seed_rows:
        final_by_id[seed["stable_id"]] = {
            "script": SCRIPT,
            "stable_id": seed["stable_id"],
            "sequence": seed["sequence"],
            "old_ko": by_id[seed["stable_id"]]["draft_ko"],
            "new_ko": seed["new_ko"],
            "category": seed["category"],
            "reason": seed["reason"],
            "reviewer": "ROOT",
        }
        provenance[seed["stable_id"]] = ["seed"]

    merges = []
    for manual in manual_rows:
        stable_id = manual["stable_id"]
        if stable_id in final_by_id:
            seed = final_by_id[stable_id]
            merged_new = apply_seed_mechanics(seed, manual["new_ko"])
            final_by_id[stable_id] = {
                "script": SCRIPT,
                "stable_id": stable_id,
                "sequence": manual["sequence"],
                "old_ko": manual["old_ko"],
                "new_ko": merged_new,
                "category": f"{seed['category']}+{manual['category']}",
                "reason": f"{seed['reason']}; manual QA: {manual['reason']}",
                "reviewer": "ROOT",
            }
            provenance[stable_id].append("manual")
            merges.append({
                "sequence": manual["sequence"],
                "stable_id": stable_id,
                "seed_new_ko": seed["new_ko"],
                "manual_new_ko": manual["new_ko"],
                "final_new_ko": merged_new,
            })
        else:
            final_by_id[stable_id] = manual
            provenance[stable_id] = ["manual"]

    final_rows = sorted(final_by_id.values(), key=lambda row: (row["sequence"], row["stable_id"]))
    if len(final_rows) != len({row["stable_id"] for row in final_rows}):
        raise SystemExit("duplicate stable_id in consolidated output")
    validations = [validate_record(by_id[row["stable_id"]], row) for row in final_rows]
    failures = [record for record in validations if not record["pass"]]
    if failures:
        raise SystemExit(f"validation failures: {failures}")

    width_failures = [
        {"sequence": row["sequence"], "stable_id": row["stable_id"], "characters": FULLWIDTH_DIGIT_RE.findall(row["new_ko"])}
        for row in final_rows if FULLWIDTH_DIGIT_RE.search(row["new_ko"])
    ]
    residual_failures = [
        {"sequence": row["sequence"], "stable_id": row["stable_id"], "characters": JP_RESIDUAL_RE.findall(row["new_ko"])}
        for row in final_rows if JP_RESIDUAL_RE.search(row["new_ko"])
    ]
    if width_failures or residual_failures:
        raise SystemExit(f"width/residual failures: {width_failures} {residual_failures}")

    write_jsonl(OUTPUT_PATH, final_rows)
    structure_audit = scope_structure_audit(entries)
    sequence_hash = hashlib.sha256(",".join(str(x) for x in range(1, EXPECTED_CHECKED + 1)).encode("ascii")).hexdigest()
    check_keys = (
        "exact_old_guard_pass",
        "protected_tokens_pass",
        "numbers_pass",
        "roman_numerals_pass",
        "quotes_pass",
        "renpy_tags_pass",
        "ruby_tags_pass",
        "newlines_pass",
    )
    summary_by_check = {
        key: {
            "pass_count": sum(record[key] for record in validations),
            "failure_count": sum(not record[key] for record in validations),
        }
        for key in check_keys
    }
    report = {
        "schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "script": SCRIPT,
        "reviewer": "ROOT",
        "source_policy": {
            "semantic_authority": "Japanese source_jp only",
            "official_english_new_prose_opened_or_used": False,
            "external_translation_api_used": False,
            "game_run": False,
            "master_modified": False,
            "existing_corrections_modified": False,
        },
        "exhaustive_review": {
            "sequence_start": 1,
            "sequence_end": EXPECTED_CHECKED,
            "checked": len(entries),
            "expected_checked": EXPECTED_CHECKED,
            "contiguous": True,
            "checked_sequences_sha256": sequence_hash,
            "manual_correction_count": len(manual_rows),
            "unchanged_after_semantic_review_count": len(entries) - len(manual_rows),
        },
        "inputs": {
            "master": {"path": str(MASTER_PATH), "sha256": master_hash_before},
            "seed": {"path": str(SEED_PATH), "sha256": seed_hash_before},
        },
        "output": {"path": str(OUTPUT_PATH), "sha256": sha256(OUTPUT_PATH)},
        "counts": {
            "checked": len(entries),
            "seed_rows": len(seed_rows),
            "seed_old_guard_pass_count": len(seed_rows),
            "manual_rows": len(manual_rows),
            "seed_manual_merge_count": len(merges),
            "final_unique_stable_id_count": len(final_rows),
            "final_duplicate_stable_id_count": len(final_rows) - len({row["stable_id"] for row in final_rows}),
            "exact_old_guard_pass_count": sum(record["exact_old_guard_pass"] for record in validations),
            "validation_pass_count": sum(record["pass"] for record in validations),
            "validation_failure_count": len(failures),
            "fullwidth_digit_failure_count": len(width_failures),
            "residual_japanese_failure_count": len(residual_failures),
        },
        "seed_manual_merges": sorted(merges, key=lambda item: item["sequence"]),
        "validation": {
            "all_pass": not failures and not width_failures and not residual_failures,
            "checks": [
                "exact_old_guard",
                "protected_tokens",
                "numeric_semantics_with_fullwidth_normalization",
                "Roman_numerals",
                "quotation_marks",
                "RenPy_tags",
                "ruby_tag_markers_including_standalone_rt",
                "newlines",
                "fullwidth_digit_residue",
                "Japanese_character_residue_in_new_ko",
            ],
            "summary_by_check": summary_by_check,
            "fullwidth_digit_failures": width_failures,
            "residual_japanese_failures": residual_failures,
            "failures": failures,
            "records": validations,
        },
        "full_checked_scope_structure_audit": structure_audit,
        "immutability_hash_check": {
            "master_unchanged": sha256(MASTER_PATH) == master_hash_before,
            "seed_unchanged": sha256(SEED_PATH) == seed_hash_before,
        },
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps({
        "checked": len(entries),
        "seed": len(seed_rows),
        "manual": len(manual_rows),
        "merges": len(merges),
        "final": len(final_rows),
        "validation_all_pass": report["validation"]["all_pass"],
        "output": str(OUTPUT_PATH),
        "output_sha256": sha256(OUTPUT_PATH),
        "report": str(REPORT_PATH),
        "report_sha256": sha256(REPORT_PATH),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
