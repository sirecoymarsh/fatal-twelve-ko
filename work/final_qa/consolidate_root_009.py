from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


BASE = Path(__file__).resolve().parent
MASTER_PATH = BASE / "output" / "masters" / "scenario_009.master.json"
SEED_PATH = BASE / "reviews" / "ROOT.corrections.jsonl"
HEAD_PATH = BASE / "reviews" / "ROOT.manual.009_001_0884.corrections.jsonl"
TAIL_PATH = BASE / "reviews" / "ROOT.manual.009_0885_1588.corrections.jsonl"
FINAL_PATH = BASE / "reviews" / "ROOT.009.consolidated.corrections.jsonl"
REPORT_PATH = BASE / "reviews" / "ROOT.009.consolidated.report.json"


# Japanese source was the only semantic authority.  The official English `new`
# prose was neither opened nor used.  Every tuple is:
# (sequence, new_ko, category, reason)
TAIL_DECISIONS = [
    (886, "이해하거나 공감할 수 있는지는 별문제지만, 어쨌든 그에게도 그만의 인생이 있었다는 것은 사실이다.", "문법/중복", "이중 소유 표현과 문장 연결 교정"),
    (887, "「미하루를 지명한 건 내 나약함 때문이야. 그녀가 내 정보를 금세 모을지도 모른다는 두려움이 있었어. 나는 그 두려움에 졌지. 그 순간 악에 빠졌어」", "문법/직역", "원인 표현과 悪に墜ちた 직역 교정"),
    (892, "분명 일본인인 우리 마음에 와닿을 방법을 그 나름대로 찾아본 것이겠지.", "명백한 부자연스러움", "마음에 울림을 주는 방법을 조사했다는 직역 교정"),
    (901, "나도 이런 목소리를 낼 수 있었구나 싶어 스스로도 의외였다.", "문법/부자연스러움", "意外に思う의 내면 서술 자연화"),
    (903, "나는 절반쯤 남은 믹스 주스를 단숨에 다 마셨다.", "용어/의미", "ミックスジュース를 일관된 명칭으로 고치고 飲み干した의 완결 의미 복원"),
    (905, "그리고 직원에게 이 주스의 가격을 물었다. 분위기에 걸맞게 비싸다고 생각하면서도, 1000엔짜리 지폐 한 장과 100엔짜리 동전 두 개를 건넸다.", "문법/숫자", "긴 문장 구조와 화폐 단위 표현 교정"),
    (908, "그는 말솜씨가 좋으니, 무슨 말이든 꺼내기 전에 자리를 뜨고 싶다는 생각도 있었다.", "주체/문법", "말을 꺼내는 주체와 떠나려는 의도 명확화"),
    (909, "대답은 정해져 있었지만, 그와 이야기를 나누다 보면 결심이 흔들릴지도 모른다.", "문법/의미", "鈍らないとも言い切れない의 이중 부정 의미 복원"),
    (910, "내 안에 흐르는 호인 기질이 그만큼 강하다는 건 나도 잘 알고 있다.", "명백한 직역", "お人好しの血를 한국어 성정 표현으로 자연화"),
    (915, "아란 스코피온은 하루 전, 스케일 존스에게 정보 교환을 제안받았다.", "문법/숫자", "１日前를 자연스러운 시간 표현으로 바꾸고 求められた 의미 교정"),
    (916, "깊은 밤 창고에 홀로 있으면서 그 일을 되짚어 본다.", "문법", "장소와 상태를 잇는 조사 오류 교정"),
    (923, "그는 지난번 여신의 선정이 존재했다는 사실 자체를 의심했지만, 결국 믿기로 했다.", "문법/의미", "前回の女神の選定という存在自体의 수식 관계 교정"),
    (925, "그리고 스케일이 그에게 한 가지 더 제안한 것이 있었다.", "문법/숫자", "수량 표현과 어순 자연화"),
    (928, "한 바퀴를 돌듯 차례대로 서로를 지명하고 방어해, 누구도 다른 사람을 지명할 수 없게 만드는 방법이다.", "조사/숫자", "誰も誰にも의 잘못된 조사와 중복 동작 표현 교정"),
    (930, "아홉 번째 선정이 시작되면, 그 정보로 린카를 지명한다――는 방법이다.", "문법/숫자", "선정을 타동사로 처리한 오류와 수치 표기 교정"),
    (932, "얼마 전까지의 자신이었다면, 혹은 상대가 시시마이 린카가 아니었다면 스케일의 제안을 받아들였을지도 모른다고 아란은 생각했다.", "시점/문법", "少し前の自分과 思い返していた의 의미 및 어순 교정"),
    (935, "아란은 카드 한 장을 꺼내 짧게 중얼거렸다.", "문법/숫자", "연결 어미와 수량 표현 자연화"),
    (937, "아란은 페데리코가 가지고 있던 반지를 조사해, 그것이 오래된 약혼반지임을 알아냈다.", "조사/의미", "반지로 사실을 조사했다는 잘못된 조사 관계 교정"),
    (947, "그가 소년이라 불안정하기 때문이라고 생각했지만, 가치관을 뒤흔들 정도의 일이 있다면 어른에게도 같은 현상이 일어날 수 있다.", "문법/의미", "무언가가 있다는 직역과 성인에게도 발생한다는 관계 교정"),
    (956, "정작 아란은 아직 카드 세 장을 모으지 못했지만, 지명당한 미하루가 살아남았다는 건 미하루가 스케일의 카드 세 장을 모았다는 뜻이다.", "문법/숫자", "어순과 문장 종결 및 수량 표현 교정"),
    (957, "그리고 린카도 이미 스케일의 카드 세 장을 모았을 것이라고 그는 확신하고 있었다.", "시제/숫자", "서술 시제와 수량 표현 교정"),
    (963, "오데트와 이 나라를 찾은 지 이제 곧 두 달이 되어 간다.", "문법/숫자", "경과 시간 구문과 수량 표현 교정"),
    (964, "여신의 선정도 순조롭게 진행된다면 이제 네 번 남았다.", "문법/숫자", "불완전한 명사문을 완결하고 수량 표현 교정"),
    (977, "어릴 때도, 어른이 된 뒤에도, 마피아가 된 뒤에도, 마피아에서 빠져나오려 했을 때도, ≪여신의 선정≫ 같은 것의 참가자가 되어 버린 뒤에도 나는 줄곧 패배하기만 했다.", "문법/병렬", "반복되는 생애 단계의 병렬 관계와 시제 교정"),
    (979, "계속 지고 있어도 나는 반드시 마지막에는 이길 거라고. 마지막에는 잘 풀릴 거라고. 마지막에 웃는 건 나라고 굳게 믿고 있었다.", "문법/시제", "간접 인용 종결과 思い込んでいた의 시제 복원"),
    (983, "아니, 그것도 아닌가.", "오역", "いや、違うか의 자기 정정 의미 복원"),
    (984, "나는 줄곧 알고 있었다. 내가 얼마나 보잘것없고 한심한 인간인지도.", "문법/의미", "명사 나열을 화자의 자기 인식으로 복원"),
    (993, "그는 하늘을 올려다보며 맑은 날 햇볕에 데워진 미지근한 공기를 폐 가득 들이마신 뒤 천천히 내뱉었다.", "오역/문법", "仰ぐ를 우러르다로 옮긴 오역과 호흡 동작 연결 교정"),
    (994, "「이제 당신과도 다시 만날 일은 없겠지」", "호칭/의미", "반지를 통해 떠올린 상대에게 쓰는 あんた의 호칭과 재회의 의미 복원"),
    (995, "그는 평생 한 번도 놓지 않았던 반지를 꺼내, 그저 어딘가 먼 곳을 향해 내던졌다.", "문법/의미", "これまでの人生でずっと手放さなかった의 지속 의미와 연결 교정"),
    (1002, "그는 자기 작전이 막힘없이 성공하리라 믿고 있었다.", "중복/의미", "淀みなくうまくいく의 중복 직역 교정"),
    (1004, "Ⅷ의 여성과 Ⅹ의 소녀, 잠시나마 후배의 목숨을 빼앗았던 Ⅳ의 유우, 그리고 유우의 보호자 역할을 했던 Ⅴ의 노인과도.", "주체/문법", "Ⅴ의 노인이 유우의 보호자 역할을 했다는 수식 관계 복원"),
    (1005, "그는 시시마이 린카가 타인에게 쉽게 공감하고, 사람을 발판으로 삼지 못할 만큼 물러터진 성격이라고 분석했다.", "오역/주체", "共感しやすい의 공감 주체가 뒤집힌 표현 교정"),
    (1013, "스케일은 협력 관계를 맺어 자신이 지명당하거나 다른 참가자에게 정보가 알려질 위험을 최소화한 뒤, 페데리코와 다시 연락할 생각이었다.", "문법/논리", "협력 관계와 위험 최소화의 수단 관계 명확화"),
    (1015, "스케일의 작전대로라면 아홉 번째 선정에서 스케일이 린카를, 페데리코가 미하루를, 아란이 페데리코를 지명할 터였다.", "문법/숫자", "작전 조건 표현과 서수 표기 자연화"),
    (1017, "유명인인 아란이라면 정보를 모을 수 있으리라 생각했다.", "주체 누락", "彼가 가리키는 아란을 복원"),
    (1019, "지명자가 사라졌을 때 여신이 어떻게 대응할지는 실제로 그 상황에 닥치면 대처할 생각이었다.", "문법/의미", "対応とやら와 直面したら의 관계 자연화"),
    (1025, "가만히 멈춰 있는 것을 무엇보다 두려워하고, 끈질기게 포기하지 않는 면도 일류다. 금세 포기해서야 사진 같은 건 찍을 수 없다.", "명백한 부자연스러움", "諦めの悪さ와 사진 촬영의 인과를 자연스럽게 복원"),
    (1026, "「……나는 정의의 편에 있어. 살기 위해서라는 이유보다 더 큰 이유는 없으니까」", "문법/의미", "生きるため以上の理由의 비교 관계 교정"),
    (1028, "후배를 구하려고 필사적이었던 사실은 한편으로, 가까운 사람을 위해서라면 앞뒤를 가리지 않는 위험성의 증거이기도 하다.", "문법/어휘", "危うさの裏付け를 자연스러운 한국어로 교정"),
    (1036, "격분한 그가 내게 폭력을 휘둘러 정보를 캐낼 가능성도 있다.", "중복/문법", "가능성을 생각할 수 있다는 중복 서술 제거"),
    (1043, "오늘의 커피는 단골 커피 가게의 오리지널 블렌드에 할머니가 살짝 손을 더한, 통칭 ≪할머니 블렌드≫다.", "오역/문법", "馴染み를 익숙하다고 옮긴 오역과 불완전 명사문 교정"),
    (1050, "「그래서 내가 커피를 내려 드리고 싶어. 맛있는 커피를 마시는 순간은 인생에서 가장 사치스러운 시간이라고――할머니가 입버릇처럼 말씀하셨거든. 그 사치스러운 시간을 선물하고 싶어」", "문법/인용", "인용문과 口癖의 잘못된 조사 연결 교정"),
    (1053, "돌이켜 보면, 이 관계는 나오미가 내 커피를 맛있다고 해 준 데서 시작되었다.", "조사/문법", "ことから의 기점 표현 교정"),
    (1059, "나는 목소리까지 뒤집혀 대답했다.", "문법/시제", "声を裏返して와 불필요한 진행형 교정"),
    (1060, "요즘 들어, 특히 내 일에는 이런 화제에 영 약하다는 걸 스스로도 알고 있었다.", "조사/문법", "最近と自分のことで의 수식·조사 관계 교정"),
    (1070, "게다가 나오미는 미하루나 마오와 달리 나처럼 고등학교 때 이 학교에 들어왔으니, 중학교 시절 친구일 가능성도 있다.", "명백한 직역", "高校からの入学組의 입학 시점 의미 복원"),
    (1075, "보통은 성별 같은 말부터 나오지 않을 테니, 나오미가 저런 반응을 보이는 것도 무리는 아니다.", "문법/의미", "性別なんて出てこない와 반응의 인과 자연화"),
    (1076, "「나도 잘 모르지만, 말로 하지 않으면 전해지지 않는다는 것만큼은 정말 맞는 말인 것 같아」", "문법/부자연스러움", "本当だと思う의 서술 자연화"),
    (1092, "두 시간쯤 빈둥거리며 보낸 뒤, 샤워를 하고 자기로 했다.", "어휘/숫자", "だらだら의 의미와 수량 표현 자연화"),
    (1105, "나는 나도 모르게 놀란 소리를 냈다.", "명백한 직역", "驚きの声を漏らす를 자연스러운 한국어 동작으로 교정"),
    (1107, "이유를 묻기도 전에 스케일 씨가 말을 꺼냈다.", "문법/의미", "聞くまでもなく의 시간 관계 자연화"),
    (1110, "그곳은 할머니의 고향이자, 4월부터 친척을 간병하려고 돌아가 머무는 곳이다.", "문법/숫자", "병렬 조사와 帰っている의 체류 의미 교정"),
    (1111, "『그리고 나는 지금 네 할머니 바로 옆에 있어――아니, 더 분명하게 말해 주지』", "어휘/의미", "隣의 위치와 はっきり言う의 발화 의도 복원"),
    (1113, "『연세 든 노인이야. 죽이는 건 쉬워. 하지만 내가 직접 죽였다가는, 네 후배 때처럼 내가 탈락하면 ≪죽지 않았던 일≫이 되어 버리지』", "주체/논리", "후배 사례와 스케일 탈락의 조건 관계 명확화"),
    (1114, "『그래서 차를 쓴 거야. 할머니는 수면제로 잠들어 있고, 여기에는 연탄이 있어. 잠깐 기다려』", "오역/문법", "だからこそ車だ의 수단 의미 복원"),
    (1125, "『5분이다. 네 스마트폰으로 네 ≪사인≫과 ≪미련≫ 카드, 그리고 각각의 배경 정보를 적어서 보내』", "문법/숫자", "카드와 배경 정보의 관계 및 전각 숫자 교정"),
    (1126, "『5분이 지나면 네 할머니를 죽인다. 첫 번째 시도에서 카드가 만들어지지 않아도 죽일 거야』", "문법/숫자", "두 조건을 분리하고 서수·전각 숫자 교정"),
    (1129, "『네가 할 수 있는 건 할머니를 버릴지 말지 선택하는 것뿐이지 않나?』", "문법", "선택지의 대등 구조와 종결 교정"),
    (1131, "『하지만 시간은 주지 않아. 아까 말한 그대로다. 5분 뒤에 올 이메일을 기대하고 있지…… 알겠나?』", "오역/숫자", "이메일을 기다리는 주체와 전각 숫자 교정"),
    (1134, "나는 참지 못하고 비명을 질렀다.", "중복/문법", "思わず와 叫ばずにはいられない의 중복 직역 교정"),
    (1137, "할머니가 목숨을 잃더라도 스케일을 탈락시키면 되살아날지도 모른다――그는 그렇게 말했다.", "문법/의미", "반복된 목숨 표현과 소생 가능성의 조건 교정"),
    (1142, "내가 죽으면 할머니는 확실히 살 수 있다.", "오역", "助かる를 되살아나다가 아닌 목숨을 건지다로 복원"),
    (1145, "믿어 주지 않을지도 모른다는 생각에 할머니에게 ≪여신의 선정≫ 이야기를 털어놓지 않은 내 탓이다.", "조사/의미", "相談しなかった의 털어놓지 않았다는 의미와 원인 조사 교정"),
    (1157, "10초다. 딱 그만큼만 통화하자.", "문법/발화", "それだけ会話する를 화자의 즉시 결정으로 자연화"),
    (1159, "만약 그렇다면 할머니를 구할 수 있을지도 모른다.", "중복/오역", "가능성 중복과 助かる의 구조 의미 교정"),
    (1171, "「난 지금 이야기할 여유 따윈 없어! 그러니까 나중에 해! 할머니가 큰일이야!」", "명백한 직역", "こっちには의 화자 지칭을 자연화"),
    (1172, "나는 마이크를 향해 다급하게 소리치고, 대답도 기다리지 않은 채 전화를 끊었다.", "오역/문법", "勢いよく를 긍정적인 기세로 옮긴 오역과 연결 교정"),
    (1173, "수화기 너머로 웃음소리 같은 숨소리가 들려와 짜증이 치밀었다.", "어휘/문법", "息遣い와 苛立ちを覚えた의 자연스러운 표현 복원"),
    (1174, "대체 무슨 용건이었던 거지.", "오역", "彼はなんだったんだ를 사람의 정체가 아닌 전화 용건에 대한 의문으로 복원"),
    (1176, "나는 할머니가 무사하기만을 빌며 이메일 문장을 입력하기 시작했다.", "조사/문법", "無事だけを祈る의 조사 관계 교정"),
    (1181, "『역시 아니었……나. 마지막 순간에라도 알게 되어 다행이라고 해야 하나』", "오역/문법", "やはり違う와 最後の最後의 의미 자연화"),
    (1183, "그는 자기 할 말만 마친 뒤, 이메일 이야기를 어떻게 알았는지도 설명하지 않고 전화를 끊었다.", "주체/문법", "一方的に言う와 이메일을 안 경위의 관계 교정"),
    (1188, "아슬아슬하게 5분을 맞춘 것 같다.", "의미/숫자", "ぎりぎり５分의 제한 시간 충족 의미와 전각 숫자 교정"),
    (1193, "『하지만 그 감정적인 면은 무척 닮았더군――정말로』", "문법/어순", "닮음의 정도를 나타내는 とても의 위치 교정"),
    (1199, "『――틀림없이 이 남자도 그대로 실행할 작정이었을 거다. 죽이겠다고 협박한 건 우선 너를 다급하게 만들어 정보를 빼앗기 위해서였지』", "시제/어휘", "실행 예정과 焦らせる의 다급함을 복원"),
    (1200, "그 목소리를 듣자, 나는 아무 대답도 할 수 없었다.", "중복/문법", "思わず와 できなくなった의 부자연스러운 중복 교정"),
    (1220, "하지만 그런 경계도 금세 무의미해졌다.", "명백한 부자연스러움", "警戒が無駄になる의 자연스러운 표현 복원"),
    (1223, "할머니 휴대전화에서 걸려 온 전화라 번호는 알 수 있었지만, 다시 걸어 보니 전원이 꺼져 있었다.", "문법/시제", "발신 번호 확인과 재통화 결과의 관계 교정"),
    (1226, "5분쯤 허송세월한 뒤, 나는 스마트폰으로 신칸센 예약 사이트를 열었다.", "어휘/숫자", "無為な時間의 의미와 전각 숫자 교정"),
    (1228, "정말 무사한지도 걱정이고, 무사하다 해도 몹시 무서운 일을 겪었음은 틀림없다.", "문법/의미", "두 우려의 병렬 관계와 恐い思い의 의미 복원"),
    (1229, "기가 센 분이지만, 갑자기 낯선 외국인에게 결박당해 억지로 수면제까지 먹은 적은 없을 것이다.", "누락/의미", "拘束과 飲まされる의 강제 의미 복원"),
    (1230, "아무리 강한 할머니라도 한동안은 공포를 떨치지 못할 것이다.", "문법/의미", "さすがのおばあちゃん의 양보 의미 자연화"),
    (1238, "『네 할머니는 이제 가까운 산에 차째로 방치할 거야. 수색하면 찾을 수 있겠지만…… 적어도 오늘 안에는 발견되지 않겠지』", "주체/의미", "車ごと와 발견의 피동 관계 복원"),
    (1239, "『월요일에 발견되면 다행이겠지만, 화요일이라면 어떨까. 사람은 며칠씩 아무것도 먹지 않고는 살아남을 수 없으니까. 게다가 꽤 연세도 많으시지』", "문법/의미", "발견 시점과 생존 조건의 문장 구조 교정"),
    (1244, "전화 너머로 들려오는 그의 말에, 나는 어금니가 부서질 듯 악물었다.", "문법/묘사", "奥歯を噛み砕きそう의 동작 주체와 비유 복원"),
    (1250, "『뭐라고 하든 마음대로 해. 나는 살기 위해 행동하고 있어. 적어도 내게는 내가 살아남는 것이 틀림없는 정의니까』", "문법/의미", "正義の側의 판단 주체와 서술 관계 교정"),
    (1255, "이제 나는 할머니 댁으로 간다. 근처 산을 샅샅이 뒤져서라도 찾아낼 것이다.", "명백한 직역", "駆け回ってやる의 수색 의지 복원"),
    (1264, "「나라면 이런 수를 쓰겠다고 곧바로 떠올릴 수 있다는 것도 얄궂군」", "문법/의미", "범행 수법을 떠올린다는 목적 관계 교정"),
    (1267, "아란은 지금껏 자신이 버려 온 것들을 하나씩 다시 주워 들며 그 자리까지 되돌아온 듯했다. 아니, 실제로 되돌아온 것이다.", "문법/비유", "拾い直す 비유와 戻っていた의 강조 복원"),
    (1273, "그가 되찾은 것들 속에는 그런 추억도 있었다.", "명백한 직역", "拾い直したもの의 비유적 의미 복원"),
    (1290, "여름 밤하늘 아래에서는 그도 그저 한 청년으로 돌아가 버리기 때문이다.", "문법/수량", "一人の青年의 불필요한 명수 단위 교정"),
    (1294, "첫차를 타고 나는 할머니가 있는 곳으로 향했다.", "조사/문법", "사람에게 향한다는 부자연스러운 목적지 표현 교정"),
    (1296, "연세가 있으니 삔 곳도 쉽게 낫지 않을 테고, 걱정이다.", "문법/의미", "捻挫でも治りが遅い의 양보와 회복 의미 복원"),
    (1298, "할머니는 누군가에게 습격당했다는 사실은 기억하고 있는 모양이었다. 또 누군가가 자신을 구해 줬다는 것도 기억하는 듯했다.", "시제/병렬", "두 기억에 공통된 추정 어조 복원"),
    (1302, "경찰에 가 보라는 권유도 받았지만, 할머니는 그러지 않았다.", "주체/문법", "권유를 받은 주체가 뒤집힐 수 있는 능동문 교정"),
    (1314, "하지만 그 정도 적자는 문제가 되지 않는 모양이다. 자세한 사정은 모르지만, 할머니는 부동산 수입이 있어 그 수익 일부로 적자를 메우고 있다고 했다.", "문법/중복", "아무래도 그래도라는 중복과 적자 상쇄 관계 교정"),
    (1315, "그런 의미에서도 역시 할머니에게는 못 당하겠다고 새삼 느꼈다.", "오역", "敵わない의 상대가 안 된다는 의미 복원"),
    (1325, "내일도 학교가 있다고 무심코 말했다가, 『그럼 학교에 늦지 않게 오늘 안으로 돌아가렴』 하고 단칼에 잘라 말하셨다.", "문법/발화", "직접 인용과 ばっさり言われた의 단호함 복원"),
    (1326, "여기서 할머니 댁까지는 신칸센을 타도 네 시간 넘게 걸리니, 그야말로 도착하자마자 되돌아온 셈이다.", "의미/숫자", "とんぼ帰り의 즉시 귀환 의미와 수량 표현 자연화"),
    (1327, "할머니가 다쳐서 다음 주에 잠시 돌아오려던 계획은 취소되었다. 할머니는 부상이 완전히 나을 때까지 돌아오지 않기로 했다.", "어휘/중복", "怪我를 상처로 한정한 표현과 예정 반복 교정"),
    (1348, "남은 참가자는 고작 다섯 명.", "문법/숫자", "불완전 주어 표현과 전각 숫자를 자연화"),
    (1356, "「정말, 실례네요. 저는 이야기 상대가 줄어들어서 쓸쓸하답니다」", "문법/부자연스러움", "寂しく思っています의 서술 자연화"),
    (1363, "스케일 씨가 그냥 말해 줬을 리는 없으니, 그 정보를 협상 재료로 삼았을 것이다.", "주체/문법", "彼가 스케일을 가리키는 문맥에서 대명사 모호성 제거"),
    (1366, "「마음에 들지 않으신다면 지금 당장 누군가에게 ≪자신의 카드≫를 넘기고 탈락하셔도 상관없답니다?」", "중복/문법", "貴方サマ自身의 이중 소유 표현 제거"),
    (1367, "「나는 그저 사실인지 확인하고 싶었을 뿐이다. ≪죽음의 운명≫을 뛰어넘어 12주가 지난 뒤에도 계속 살아남을 수 있다…… 그 사실은 변하지 않겠지?」", "문법/의미", "12週間後以降의 이후 지속 의미와 지시 대상 복원"),
    (1370, "정체된 나날이 이어지는 가운데 아홉 번째 선정이 시작됐다.", "숫자/표기", "전각 숫자를 자연스러운 한국어 서수로 교정"),
    (1395, "그런데도 내가 서 있는 바닥은 무자비하게 위층을 향해 올라갔다.", "문법/동사", "바닥의 위치 수식과 上層へ向かう의 상승 동작 복원"),
    (1400, "「이 반응을 보니, 아무래도 귀하를 제외한 분들은 이미 알고 계신 모양이군요」", "조사/문법", "貴方サマ以外의 제외 조사와 この様子의 반응 의미 교정"),
    (1407, "「그 녀석이 앞으로의 일을 들어 봐야 그저 허탈해질 뿐이라고 생각하지 않나?」", "어휘/문법", "先の話와 虚しくなる의 자연스러운 의미 복원"),
    (1434, "「나도 지명은 안 한다」", "의미 누락", "なし가 지명하지 않겠다는 뜻임을 명시"),
    (1445, "바늘은 아무 감정도 없이 나아가 아란 씨를 가리켰다.", "동사/주체", "針が向く를 바늘이 사람을 가리키는 동작으로 복원"),
    (1454, "내가 상층에 온 건 이번이 두 번째였다.", "조사/숫자", "장소 조사와 전각 숫자 자연화"),
    (1457, "「내가 밉나? 그럴 만도 하지. 난 네 할망구를 인질로 잡았어. 어디 한 군데쯤 다쳤을지도 모르고」", "문법/어휘", "無理もない와 怪我くらい의 자연스러운 발화 복원"),
    (1458, "「나를 지명한 건 그 복수라는 거군. 넌 정의의 편이야. 하지만 유감스럽게도 나 역시 정의의 편에 있거든」", "주체 오역", "おれの指名은 스케일이 한 지명이 아니라 스케일을 지명한 행위임"),
    (1460, "「네가 이제부터 죽일 상대는 틀림없이――한 인간이야」", "문법/의미", "紛れもなく人間의 서술 관계 자연화"),
    (1462, "스케일 씨는 눈을 번뜩이며 나를 노려보고 있었다.", "주어/어휘", "표정이 노려본다는 주어 오류와 ぎらぎら의 표현 교정"),
    (1463, "조금이라도 빈틈이 보이면 물어뜯고, 내가 동정심을 보이면 지금이라도 정보를 캐내려 든다는 게 느껴졌다.", "문법/병렬", "두 조건 행동의 끊어진 병렬 구조 교정"),
    (1470, "「당신에게 들은 당신의 삶을 잊지 않을게요. 당신이 어떤 사람이었는지, 이렇게 생의 마지막 순간까지 살아남으려 했다는 것도 잊지 않겠어요」", "문법/의미", "人格와 最期の最期의 목적어 병렬 및 의미 복원"),
    (1472, "「저는 그 저주까지도 기억하며――당신이라는 사람을 알아 갈 테니까요」", "명백한 부자연스러움", "その呪いも知って와 상대를 알아 간다는 관계 자연화"),
    (1483, "「귀하 같은 인간을 상대로 시험해 본 적은 없어서…… 어디까지나 추측이지만요」", "조사/문법", "사람으로 시험한다는 도구격 오역 교정"),
    (1487, "「자기 죽음을 순순히 받아들이라고…… 나는 그런 말은 하지 않을게요. 오히려 마지막까지 어떻게든 살아남으려는 당신이 옳을지도 몰라요」", "명백한 직역", "潔く死を受け入れる의 의미와 正解의 판단 표현 자연화"),
    (1498, "「파파라치가 된 것도 그쪽이 더 자유롭고 돈이 되기 때문이야. 미안하지만 사명감보다는 보람이 더 컸지」", "오역/어휘", "充実感을 충족감이 아닌 보람으로 복원"),
    (1499, "「하지만 이 말을 듣고도 넌 나에 대한 평가를 바꾸지 않겠지. 그마저도 살기 위한 노력이라 받아들이겠지」", "중복/문법", "나를 보는 평가라는 중복과 지시 대상 교정"),
    (1505, "성명・사인・미련 카드는 삼각형을 이루어 움직임을 멈추더니, 빛을 급격히 증폭시켰다.", "문법/동사", "두 연속 동작의 연결과 빛 증폭의 주체 교정"),
    (1508, "차선이 세 개 이상인 고가 고속도로.", "숫자/의미", "３車線以上를 세 차선을 넘는 것으로 좁힌 오역 교정"),
    (1509, "시속 100킬로미터가 넘는 속도로 달리는 차 안에서, 눈앞의 다른 차를 뒤쫓는 듯했다.", "문법/단위", "속도 단위와 추격 대상의 수식 관계 교정"),
    (1518, "그 사진 속 인물은 근거 없는 마약 의혹을 뒤집어쓴 뒤 주변의 불신과 배척을 견디지 못하고 자살한 대학 시절의 절친이었다.", "주체/오역", "사진과 인물의 관계 및 ありもしない疑惑의 허위 의미 복원"),
    (1520, "차와 운전자 모두 원형을 알아볼 수 없을 만큼 처참한 대형 사고였지만, 유일하게 목에 걸고 있던 카메라만은 사용할 수 있는 상태였다.", "피동/문법", "원형을 남기지 않았다는 능동 표현과 양보 구조 교정"),
    (1525, "나는 스케일 씨를 기억한다. 결코 잊지 않을 것이다. 그래도 이제부터는 내 길을 걸어가야 한다.", "중복/문법", "覚えてはいるけれど와 忘れはしない의 중복을 한국어 호흡으로 정리"),
    (1534, "파르카가 말을 마치자 내가 서 있던 바닥이 진동하며 아래층을 향해 움직였다.", "문법/중복", "움직이기 시작한다는 반복과 목적 표현 교정"),
    (1535, "이렇게 나의 두 번째 지명이 끝났다.", "숫자/표기", "전각 숫자를 자연스러운 한국어 서수로 교정"),
    (1540, "스케일 씨를 탈락시키기로 한 시점부터 미하루도 어느 정도 예상하고 있었을 것이다.", "조사/시점", "탈락시킨다는 시점이라는 직역과 선행 예상 관계 교정"),
    (1543, "나도 막상 손에 넣은 카드에 적힌 글자를 보고는 놀랐다.", "명백한 직역", "さすがの私も의 양보 뉘앙스 자연화"),
    (1548, "「그럼 오늘 밤의 탈락자는 한 명――」", "숫자/표기", "전각 숫자를 자연스러운 한국어 수량으로 교정"),
    (1550, "「으음. 제 멋진 마무리 대사였는데요」", "오역", "決め台詞를 결정 대사가 아닌 정해 둔 마무리 멘트로 복원"),
    (1560, "미하루에게 이미 이야기를 들은 나는 그 질문에 대한 답이 아니오라는 걸 알고 있었다.", "문법/의미", "답이 아니라는 잘못된 서술을 부정 응답의 의미로 교정"),
    (1563, "컴퓨터에 비유하면 내부 어딘가에 보안이 걸린 여신 폴더 하나가 생기는 셈이다.", "문법/비유", "불완전한 명사문과 컴퓨터 비유의 위치 관계 교정"),
    (1575, "「실례되는 말씀이군요. 저는 여신. 귀하께서 헤아릴 수조차 없는 세계에 존재하는 자랍니다. 귀하들의 운명이 어디로 향하든 제게는 오락에 불과해요」", "주체/문법", "측량할 수 없는 주체가 뒤집힌 문장과 불완전 명사문 교정"),
    (1576, "「……그렇군, 그건 재미있겠어. 방금 한 말은 취소하지. 내 안에 들어온다면 실컷 즐겁게 해 주마」", "문법/시제", "재미있어의 종결 오류와 前言撤回 및 조건 표현 교정"),
    (1582, "미하루는 나지막이 그렇게 중얼거렸다.", "명백한 부자연스러움", "口にした를 입에 담았다고 옮긴 부자연스러운 표현 교정"),
    (1584, "이 자리에서는 자세히 물을 수 없지만, 미하루에게는 자신도 모르는 사이 여신 파르카가 세계에 간섭하고 있었다고 짐작할 만한 일이 있는 걸까.", "문법/의미", "心当たり가 있는 주체와 추정 대상의 수식 관계 교정"),
]


CHECKED_RANGE = (885, 1588)
EXPECTED_CHECKED = 704
ROMAN_RE = re.compile(r"[ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩⅪⅫ]")
NUM_RE = re.compile(r"[0-9０-９]+")
TAG_RE = re.compile(r"\{[^{}\n]*\}|\[[^\[\]\n]*\]")
RUBY_TAG_RE = re.compile(r"\{/?(?:rb|rt)\}")
QUOTE_CHARS = "「」『』≪≫“”‘’\""
FW_TRANS = str.maketrans("０１２３４５６７８９", "0123456789")


NUMBER_WORD_OVERRIDES = {
    648: {"2": ["둘"]},
    905: {"2": ["두 개"]},
    915: {"1": ["하루"]},
    925: {"1": ["한 가지"]},
    928: {"1": ["한 바퀴"]},
    930: {"9": ["아홉 번째"]},
    935: {"1": ["한 장"]},
    956: {"3": ["세 장", "세 장"]},
    957: {"3": ["세 장"]},
    963: {"2": ["두 달"]},
    964: {"4": ["네 번"]},
    1015: {"9": ["아홉 번째"]},
    1092: {"2": ["두 시간"]},
    1126: {"1": ["첫 번째"]},
    1326: {"4": ["네 시간"]},
    1348: {"5": ["다섯 명"]},
    1370: {"9": ["아홉 번째"]},
    1454: {"2": ["두 번째"]},
    1508: {"3": ["세 개"]},
    1535: {"2": ["두 번째"]},
    1548: {"1": ["한 명"]},
}

PRIORITY_CANDIDATES = [
    903,905,909,910,915,925,928,930,932,935,937,956,957,963,964,977,979,983,984,993,995,
    1004,1005,1013,1015,1017,1019,1025,1026,1028,1043,1050,1053,1059,1070,1075,1076,
    1092,1105,1107,1110,1111,1113,1125,1126,1129,1131,1134,1137,1142,1145,1157,1159,
    1172,1173,1174,1181,1183,1188,1193,1199,1200,1220,1223,1226,1228,1229,1230,1239,
    1244,1250,1255,1267,1273,1290,1294,1296,1298,1302,1314,1315,1325,1326,1348,1356,
    1366,1367,1370,1395,1400,1407,1434,1445,1454,1457,1460,1462,1463,1470,1472,1483,
    1487,1491,1498,1499,1505,1508,1518,1520,1525,1534,1535,1540,1543,1548,1550,1560,
    1563,1575,1576,1582,1584,
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
        newline="\n",
    )


def normalized_numbers(text: str) -> list[str]:
    return [value.translate(FW_TRANS) for value in NUM_RE.findall(text)]


def numeric_validation(sequence: int, old_text: str, new_text: str) -> dict:
    old_counter = Counter(normalized_numbers(old_text))
    new_counter = Counter(normalized_numbers(new_text))
    evidence = []
    for value in sorted(set(old_counter) | set(new_counter)):
        common = min(old_counter[value], new_counter[value])
        if common:
            old_counter[value] -= common
            new_counter[value] -= common
            evidence.append({"value": value, "mode": "digit_exact_or_fullwidth_normalized", "count": common})
    phrase_uses = Counter()
    for value, phrases in NUMBER_WORD_OVERRIDES.get(sequence, {}).items():
        for phrase in phrases:
            available = new_text.count(phrase) - phrase_uses[phrase]
            if old_counter[value] > 0 and available > 0:
                old_counter[value] -= 1
                phrase_uses[phrase] += 1
                evidence.append({"value": value, "mode": "korean_number_word", "text": phrase})
            else:
                evidence.append({"value": value, "mode": "override_not_consumed", "text": phrase})
    old_remaining = list(old_counter.elements())
    new_remaining = list(new_counter.elements())
    return {
        "pass": not old_remaining and not new_remaining,
        "old_numbers_normalized": normalized_numbers(old_text),
        "new_numbers_normalized": normalized_numbers(new_text),
        "evidence": evidence,
        "old_remaining": old_remaining,
        "new_remaining": new_remaining,
    }


def validate_record(entry: dict, row: dict) -> dict:
    old_text = row["old_ko"]
    new_text = row["new_ko"]
    protected_differences = []
    for token in entry.get("protected_tokens") or []:
        if isinstance(token, dict):
            if token.get("kind") == "number":
                continue
            value = token.get("value")
        else:
            value = token
        if not value:
            continue
        old_count = old_text.count(value)
        new_count = new_text.count(value)
        if old_count != new_count:
            protected_differences.append({"token": value, "old_count": old_count, "new_count": new_count})

    number_result = numeric_validation(row["sequence"], old_text, new_text)
    old_roman = Counter(ROMAN_RE.findall(old_text))
    new_roman = Counter(ROMAN_RE.findall(new_text))
    old_quotes = Counter(ch for ch in old_text if ch in QUOTE_CHARS)
    new_quotes = Counter(ch for ch in new_text if ch in QUOTE_CHARS)
    old_tags = Counter(TAG_RE.findall(old_text))
    new_tags = Counter(TAG_RE.findall(new_text))
    old_ruby = Counter(RUBY_TAG_RE.findall(old_text))
    new_ruby = Counter(RUBY_TAG_RE.findall(new_text))
    checks = {
        "exact_old_guard_pass": entry["draft_ko"] == old_text,
        "protected_tokens_pass": not protected_differences,
        "numbers_pass": number_result["pass"],
        "roman_numerals_pass": old_roman == new_roman,
        "quotes_pass": old_quotes == new_quotes,
        "renpy_tags_pass": old_tags == new_tags,
        "ruby_tags_pass": old_ruby == new_ruby,
    }
    return {
        "sequence": row["sequence"],
        "stable_id": row["stable_id"],
        **checks,
        "pass": all(checks.values()),
        "protected_token_differences": protected_differences,
        "number_validation": number_result,
        "old_roman": dict(old_roman),
        "new_roman": dict(new_roman),
        "old_quotes": dict(old_quotes),
        "new_quotes": dict(new_quotes),
        "old_renpy_tags": dict(old_tags),
        "new_renpy_tags": dict(new_tags),
        "old_ruby_tags": dict(old_ruby),
        "new_ruby_tags": dict(new_ruby),
    }


def apply_seed_mechanics(seed: dict, manual_text: str) -> str:
    result = manual_text
    if seed.get("category") == "typography":
        result = result.translate(FW_TRANS)
    if seed.get("category") == "term":
        replacements = (
            ("꿈속 세상", "꿈의 세계"),
            ("운명의 대광장", "운명의 대회랑"),
            ("운명의 대전당", "운명의 대회랑"),
            ("알란", "아란"),
            ("스콜피온", "스코피온"),
        )
        for old, new in replacements:
            result = result.replace(old, new)
    return result


def main() -> None:
    if len(TAIL_DECISIONS) != 142 or len({row[0] for row in TAIL_DECISIONS}) != 142:
        raise SystemExit("tail decision count/uniqueness mismatch")
    if any(not (CHECKED_RANGE[0] <= row[0] <= CHECKED_RANGE[1]) for row in TAIL_DECISIONS):
        raise SystemExit("tail decision outside checked range")

    master = json.loads(MASTER_PATH.read_text(encoding="utf-8"))
    entries = master["entries"]
    scope_entries = [entry for entry in entries if CHECKED_RANGE[0] <= entry["sequence"] <= CHECKED_RANGE[1]]
    if len(scope_entries) != EXPECTED_CHECKED:
        raise SystemExit(f"checked range count mismatch: {len(scope_entries)}")
    if [entry["sequence"] for entry in scope_entries] != list(range(CHECKED_RANGE[0], CHECKED_RANGE[1] + 1)):
        raise SystemExit("checked range is not contiguous")
    by_sequence = {entry["sequence"]: entry for entry in entries}
    by_id = {entry["stable_id"]: entry for entry in entries}

    tail_rows = []
    for sequence, new_ko, category, reason in TAIL_DECISIONS:
        entry = by_sequence[sequence]
        if entry["draft_ko"] == new_ko:
            raise SystemExit(f"tail no-op at sequence {sequence}")
        tail_rows.append({
            "script": "009",
            "stable_id": entry["stable_id"],
            "sequence": sequence,
            "old_ko": entry["draft_ko"],
            "new_ko": new_ko,
            "category": category,
            "reason": reason,
            "reviewer": "ROOT",
        })
    write_jsonl(TAIL_PATH, tail_rows)

    all_seed_rows = [row for row in load_jsonl(SEED_PATH) if row.get("script") == "009"]
    head_rows = load_jsonl(HEAD_PATH)
    if len(head_rows) != 60:
        raise SystemExit(f"head manual count mismatch: {len(head_rows)}")
    if len(all_seed_rows) != 42:
        raise SystemExit(f"scenario009 seed count mismatch: {len(all_seed_rows)}")
    seed_tail_rows = [row for row in all_seed_rows if CHECKED_RANGE[0] <= row["sequence"] <= CHECKED_RANGE[1]]
    if len(seed_tail_rows) != 29:
        raise SystemExit(f"tail seed count mismatch: {len(seed_tail_rows)}")

    for source_name, rows in (("seed", all_seed_rows), ("head", head_rows), ("tail", tail_rows)):
        for row in rows:
            entry = by_id.get(row["stable_id"])
            if entry is None or entry["sequence"] != row["sequence"] or entry["draft_ko"] != row["old_ko"]:
                raise SystemExit(f"{source_name} old guard mismatch: {row.get('sequence')} {row.get('stable_id')}")

    final_by_id = {}
    provenance = {}
    for seed in all_seed_rows:
        stable_id = seed["stable_id"]
        final_by_id[stable_id] = {
            "script": "009",
            "stable_id": stable_id,
            "sequence": seed["sequence"],
            "old_ko": by_id[stable_id]["draft_ko"],
            "new_ko": seed["new_ko"],
            "category": seed["category"],
            "reason": seed["reason"],
            "reviewer": "ROOT",
        }
        provenance[stable_id] = ["seed"]

    merge_details = []
    for source_name, manual_rows in (("manual_head", head_rows), ("manual_tail", tail_rows)):
        for manual in manual_rows:
            stable_id = manual["stable_id"]
            if stable_id in final_by_id:
                seed = final_by_id[stable_id]
                merged_new = apply_seed_mechanics(seed, manual["new_ko"])
                final_by_id[stable_id] = {
                    "script": "009",
                    "stable_id": stable_id,
                    "sequence": manual["sequence"],
                    "old_ko": by_id[stable_id]["draft_ko"],
                    "new_ko": merged_new,
                    "category": f"{seed['category']}+{manual['category']}",
                    "reason": f"{seed['reason']}; manual QA: {manual['reason']}",
                    "reviewer": "ROOT",
                }
                provenance[stable_id].append(source_name)
                merge_details.append({
                    "sequence": manual["sequence"],
                    "stable_id": stable_id,
                    "sources": provenance[stable_id],
                    "seed_new_ko": seed["new_ko"],
                    "manual_new_ko": manual["new_ko"],
                    "final_new_ko": merged_new,
                })
            else:
                final_by_id[stable_id] = dict(manual)
                provenance[stable_id] = [source_name]

    final_rows = sorted(final_by_id.values(), key=lambda row: (row["sequence"], row["stable_id"]))
    if len(final_rows) != len({row["stable_id"] for row in final_rows}):
        raise SystemExit("duplicate stable_id in final rows")
    write_jsonl(FINAL_PATH, final_rows)

    validations = [validate_record(by_id[row["stable_id"]], row) for row in final_rows]
    failures = [row for row in validations if not row["pass"]]

    ruby_scope = []
    for entry in scope_entries:
        source_ruby = Counter(RUBY_TAG_RE.findall(entry["source_jp"]))
        draft_ruby = Counter(RUBY_TAG_RE.findall(entry["draft_ko"]))
        if source_ruby or draft_ruby:
            ruby_scope.append({
                "sequence": entry["sequence"],
                "stable_id": entry["stable_id"],
                "source_ruby_tags": dict(source_ruby),
                "draft_ruby_tags": dict(draft_ruby),
                "marker_pass": source_ruby == draft_ruby,
            })

    decision_sequences = {row[0] for row in TAIL_DECISIONS}
    priority_accepted = sorted(set(PRIORITY_CANDIDATES) & decision_sequences)
    priority_rejected = sorted(set(PRIORITY_CANDIDATES) - decision_sequences)
    checked_sequence_text = ",".join(str(entry["sequence"]) for entry in scope_entries)
    report = {
        "schema_version": 1,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "script": "009",
        "reviewer": "ROOT",
        "source_policy": {
            "semantic_authority": "Japanese source_jp in scenario_009.master.json",
            "official_english_new_prose_opened_or_used": False,
            "external_translation_api_used": False,
            "master_modified": False,
            "existing_seed_or_manual_files_modified": False,
        },
        "exhaustive_review": {
            "sequence_start": CHECKED_RANGE[0],
            "sequence_end": CHECKED_RANGE[1],
            "checked": len(scope_entries),
            "expected_checked": EXPECTED_CHECKED,
            "contiguous": True,
            "checked_sequences_sha256": hashlib.sha256(checked_sequence_text.encode("ascii")).hexdigest(),
            "manual_tail_correction_count": len(tail_rows),
            "unchanged_after_review_count": len(scope_entries) - len(tail_rows),
            "priority_candidate_count": len(PRIORITY_CANDIDATES),
            "priority_accepted_count": len(priority_accepted),
            "priority_accepted_sequences": priority_accepted,
            "priority_rejected": [
                {
                    "sequence": sequence,
                    "reason": "기존 한국어가 일본어 원문의 의미와 어조를 이미 보존하므로 변경하면 문체 취향 수정에 그친다.",
                }
                for sequence in priority_rejected
            ],
        },
        "inputs": {
            "master": str(MASTER_PATH),
            "master_sha256": sha256(MASTER_PATH),
            "seed": str(SEED_PATH),
            "seed_sha256": sha256(SEED_PATH),
            "manual_head": str(HEAD_PATH),
            "manual_head_sha256": sha256(HEAD_PATH),
        },
        "outputs": {
            "manual_tail": str(TAIL_PATH),
            "manual_tail_sha256": sha256(TAIL_PATH),
            "consolidated": str(FINAL_PATH),
            "consolidated_sha256": sha256(FINAL_PATH),
        },
        "counts": {
            "scenario009_seed_total": len(all_seed_rows),
            "scenario009_seed_in_885_1588": len(seed_tail_rows),
            "manual_head_1_884": len(head_rows),
            "manual_tail_885_1588": len(tail_rows),
            "seed_manual_merge_count": len(merge_details),
            "final_unique_stable_id_count": len(final_rows),
            "final_duplicate_stable_id_count": len(final_rows) - len({row["stable_id"] for row in final_rows}),
            "exact_old_guard_pass_count": sum(row["exact_old_guard_pass"] for row in validations),
            "validation_pass_count": sum(row["pass"] for row in validations),
            "validation_failure_count": len(failures),
        },
        "seed_manual_merges": merge_details,
        "validation": {
            "all_pass": not failures,
            "checks": [
                "exact_old_guard",
                "protected_tokens",
                "numbers_with_fullwidth_and_Korean_word_equivalence",
                "Roman_numerals",
                "quotation_marks",
                "RenPy_tags",
                "ruby_tag_markers",
            ],
            "summary_by_check": {
                key: {
                    "pass_count": sum(bool(row[key]) for row in validations),
                    "failure_count": sum(not bool(row[key]) for row in validations),
                }
                for key in (
                    "exact_old_guard_pass",
                    "protected_tokens_pass",
                    "numbers_pass",
                    "roman_numerals_pass",
                    "quotes_pass",
                    "renpy_tags_pass",
                    "ruby_tags_pass",
                )
            },
            "failure_count": len(failures),
            "failures": failures,
            "records": validations,
        },
        "full_checked_range_ruby_audit": {
            "record_count_with_ruby": len(ruby_scope),
            "all_source_to_draft_markers_preserved": all(row["marker_pass"] for row in ruby_scope),
            "records": ruby_scope,
        },
    }
    REPORT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")

    print(json.dumps({
        "checked": len(scope_entries),
        "manual_tail": len(tail_rows),
        "seed_total": len(all_seed_rows),
        "seed_tail": len(seed_tail_rows),
        "seed_manual_merges": len(merge_details),
        "final_unique": len(final_rows),
        "validation_failures": len(failures),
        "priority_rejected": priority_rejected,
        "tail_output": str(TAIL_PATH),
        "final_output": str(FINAL_PATH),
        "report": str(REPORT_PATH),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
