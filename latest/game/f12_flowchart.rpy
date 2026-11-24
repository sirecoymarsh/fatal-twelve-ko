# Fatal Twelve 한국어 패치 — 플로우 차트 (v2, 2026-10-02)
# 추가 파일 하나. system.rpa / scenario.rpa / 다른 f12_*.rpy 는 바꾸지 않는다. 생성: P:\AI\ft-compare\flow\gen_fc_rpy_v2.py
#
# 화면 셋
#   f12_flowchart          특전(EXTRA) 세 번째 탭. 갤러리·다시보기 탭과 함께.
#   f12_flowchart_ingame   인게임 빠른 메뉴 「플로우 차트」. 탭 없음. 지금 읽는 장면과 이번 회차에 고른 선택지를 표시.
#   f12_flowchart_replay   플로우 차트 다시보기 중 빠른 메뉴 「플로우 차트」. 다른 장면을 고르면 지금 다시보기를 끝내고 그 장면으로.
# 판정
#   장면 해금 = 그 장면의 끝 줄(줄기별, 갈래가 있으면 어느 하나)을 읽었는지. persistent._seen_translates 기준.
#   끝 줄·줄기 배정은 게임 안 흐름 분석(줄기 깃발 추적)으로 미리 뽑아 아래 자료에 넣었다.
#   이번 회차 선택 = 메뉴를 고르는 순간 세이브 변수 f12_fc_picks 에 기록(되감기하면 같이 되돌아감). 옛 세이브는 줄기 깃발로 확실한 것만 추정(▷).
#   다시보기 = Ren'Py Replay(격리) + 다음 장면 표식에서 종료 + persistent 되돌림(읽음 기록·환경설정·이 차트 설정 제외).

default f12_fc_cur = None
default f12_fc_picks = {}

init -1 python:
    import re as _f12_fc_re
    import copy as _f12_fc_copy

    F12_FC_COLS = [{u"key": u"1주차", u"week": u"1주차", u"short": u"1주차", u"wn": 1, u"colk": u"S", u"sub": u"자각 없는 평온", u"cg": u"01", u"chips": [{u"file": u"001", u"sid": u"00", u"name": u"프롤로그", u"ends": [u"f001_eb489c3e"], u"menus": [], u"excl": [u"f001_eb489c3e"]}, {u"file": u"001", u"sid": u"01", u"name": u"귀갓길", u"ends": [u"f001_772c32ef"], u"menus": [], u"excl": [u"f001_772c32ef"]}, {u"file": u"001", u"sid": u"02", u"name": u"옮겨 적기", u"ends": [u"f001_bed658dc"], u"menus": [], u"excl": [u"f001_bed658dc"]}, {u"file": u"001", u"sid": u"03", u"name": u"걸즈 토크", u"ends": [u"f001_e1fe7db2"], u"menus": [], u"excl": [u"f001_e1fe7db2"]}, {u"file": u"001", u"sid": u"04", u"name": u"기묘한 책", u"ends": [u"f001_s1_end_b97197e2"], u"menus": [{u"key": u"001:1355", u"opts": [[u"펼쳐 보자", u"+1", u"", u"", u"開いてみよう", [], u""], [u"건드리지 말자", u"", u"", u"", u"触らないでおこう", [], u""]], u"infer": []}], u"excl": [u"f001_s1_end_b97197e2"]}, {u"file": u"001", u"sid": u"05", u"name": u"선잠 속에서", u"ends": [u"f001_s1_end_244dd4e3"], u"menus": [], u"excl": [u"f001_s1_end_244dd4e3"]}, {u"file": u"001", u"sid": u"06", u"name": u"불꽃의 기억", u"ends": [u"f001_s1_end_6d6025e2"], u"menus": [], u"excl": [u"f001_s1_end_6d6025e2"]}, {u"file": u"001", u"sid": u"07", u"name": u"악몽을 꾼 아침", u"ends": [u"f001_s2_end_2954c456"], u"menus": [{u"key": u"001:2230", u"opts": [[u"팔아 버리자.", u"", u"", u"", u"売っちゃおう。", [], u""], [u"안을 확인해 보자.", u"+1", u"", u"", u"中を見てみよう。", [], u""]], u"infer": []}], u"excl": [u"f001_s2_end_2954c456"]}, {u"file": u"001", u"sid": u"08", u"name": u"왁자지껄 놀이공원", u"ends": [u"f001_s3_end_2f4f6b9d"], u"menus": [{u"key": u"001:2556", u"opts": [[u"「부끄러우니까…… 놔줘」", u"", u"", u"", u"「恥ずかしいから……離して」", [], u""], [u"「아, 알겠어」", u"+1", u"", u"", u"「わ、分かった」", [], u""]], u"infer": []}], u"excl": [u"f001_s3_end_2f4f6b9d"]}, {u"file": u"001", u"sid": u"09", u"name": u"치유의 시간", u"ends": [u"f001_s3_end_2cb0d9ef"], u"menus": [], u"excl": [u"f001_s3_end_2cb0d9ef"]}, {u"file": u"001", u"sid": u"10", u"name": u"여신의 선정", u"ends": [u"sentei1_88c8dbc1"], u"menus": [], u"excl": [u"sentei1_88c8dbc1"]}], u"ends": [[u"M", u"오프닝 영상", u"chip:S|001|02", u"movies/OP.mkv", u"오프닝 영상"]], u"movies": [{u"label": u"오프닝 영상", u"label_open": u"오프닝 영상", u"path": u"movies/OP.mkv", u"unlock": u"chip:S|001|02", u"after": u"02"}]}, {u"key": u"2주차", u"week": u"2주차", u"short": u"2주차", u"wn": 2, u"colk": u"S", u"sub": u"이룰 수 없는 소망", u"cg": u"07", u"chips": [{u"file": u"002", u"sid": u"11", u"name": u"우울한 아침", u"ends": [u"f002_28ba141b"], u"menus": [], u"excl": [u"f002_28ba141b"]}, {u"file": u"002", u"sid": u"12", u"name": u"연휴가 끝난 뒤의 학교", u"ends": [u"f002_8bdfe06c"], u"menus": [], u"excl": [u"f002_8bdfe06c"]}, {u"file": u"002", u"sid": u"13", u"name": u"메이드 카페 첫 방문!", u"ends": [u"f002_43176367"], u"menus": [], u"excl": [u"f002_43176367"]}, {u"file": u"002", u"sid": u"14", u"name": u"엇갈림", u"ends": [u"f002_dddb68ce"], u"menus": [], u"excl": [u"f002_dddb68ce"]}, {u"file": u"002", u"sid": u"15", u"name": u"위험한 두 사람", u"ends": [u"f002_a065e450"], u"menus": [], u"excl": [u"f002_a065e450"]}, {u"file": u"002", u"sid": u"16", u"name": u"미행 후", u"ends": [u"f002_625b2493"], u"menus": [], u"excl": [u"f002_625b2493"]}, {u"file": u"002", u"sid": u"17", u"name": u"여유로운 야회", u"ends": [u"f002_3ddd7ce8"], u"menus": [], u"excl": [u"f002_3ddd7ce8"]}, {u"file": u"002", u"sid": u"18", u"name": u"미행과 추적", u"ends": [u"f002_9e40ed28"], u"menus": [], u"excl": [u"f002_9e40ed28"]}, {u"file": u"002", u"sid": u"19", u"name": u"어이없을 만큼 경솔", u"ends": [u"f002_b6903521"], u"menus": [], u"excl": [u"f002_b6903521"]}, {u"file": u"002", u"sid": u"20", u"name": u"공백의 며칠", u"ends": [u"f002_s1_end_dbd92ff8"], u"menus": [{u"key": u"002:2382", u"opts": [[u"나오미와의 관계는…….", u"", u"", u"", u"直未との関係は……。", [], u""], [u"미하루와의 관계는…….", u"+1", u"", u"", u"海晴との関係は……。", [], u""]], u"infer": []}], u"excl": [u"f002_s1_end_dbd92ff8"]}, {u"file": u"002", u"sid": u"21", u"name": u"2번째 선정, 시작", u"ends": [u"sentei2_67693141"], u"menus": [], u"excl": [u"sentei2_67693141"]}], u"ends": [], u"movies": []}, {u"key": u"3주차", u"week": u"3주차", u"short": u"3주차", u"wn": 3, u"colk": u"S", u"sub": u"부모와 자식을 잇는 희망", u"cg": u"13", u"chips": [{u"file": u"003", u"sid": u"22", u"name": u"지명의 진상", u"ends": [u"f003_5d56d749"], u"menus": [], u"excl": [u"f003_5d56d749"]}, {u"file": u"003", u"sid": u"23", u"name": u"계속되는 악몽", u"ends": [u"f003_dc43d539"], u"menus": [], u"excl": [u"f003_dc43d539"]}, {u"file": u"003", u"sid": u"24", u"name": u"오늘 밥", u"ends": [u"f003_7d99f189"], u"menus": [], u"excl": [u"f003_7d99f189"]}, {u"file": u"003", u"sid": u"25", u"name": u"방과 후에 뭐 할래?", u"ends": [u"f003_s1_end_fdc4164d"], u"menus": [{u"key": u"003:991", u"opts": [[u"「미하루도 올래?」", u"+1", u"", u"", u"「海晴も来る？」", [], u""], [u"「미하루는 알바 가?」", u"", u"", u"", u"「海晴はバイト？」", [], u""]], u"infer": []}], u"excl": [u"f003_s1_end_fdc4164d"]}, {u"file": u"003", u"sid": u"26", u"name": u"멀어진 등", u"ends": [u"f003_s1_end_d954c8eb"], u"menus": [], u"excl": [u"f003_s1_end_d954c8eb"]}, {u"file": u"003", u"sid": u"27", u"name": u"잠식하는 꿈", u"ends": [u"f003_s1_end_01baea61"], u"menus": [], u"excl": [u"f003_s1_end_01baea61"]}, {u"file": u"003", u"sid": u"28", u"name": u"싹트는 유대", u"ends": [u"f003_s1_end_042913e9"], u"menus": [], u"excl": [u"f003_s1_end_042913e9"]}, {u"file": u"003", u"sid": u"29", u"name": u"여성과 병원", u"ends": [u"f003_s1_end_2508f79c"], u"menus": [], u"excl": [u"f003_s1_end_2508f79c"]}, {u"file": u"003", u"sid": u"30", u"name": u"독서는 좋아? 싫어?", u"ends": [u"f003_s1_end_f58caa86"], u"menus": [], u"excl": [u"f003_s1_end_f58caa86"]}, {u"file": u"003", u"sid": u"31", u"name": u"사인에 도달하다", u"ends": [u"f003_s1_end_eb20f7a9"], u"menus": [], u"excl": [u"f003_s1_end_eb20f7a9"]}, {u"file": u"003", u"sid": u"32", u"name": u"마주한 마음", u"ends": [u"f003_s1_end_c2524565"], u"menus": [], u"excl": [u"f003_s1_end_c2524565"]}, {u"file": u"003", u"sid": u"33", u"name": u"왜 내가?", u"ends": [u"f003_s1_end_84732f00"], u"menus": [], u"excl": [u"f003_s1_end_84732f00"]}, {u"file": u"003", u"sid": u"34", u"name": u"그 이름", u"ends": [u"f003_s1_end_9c0693da"], u"menus": [], u"excl": [u"f003_s1_end_9c0693da"]}, {u"file": u"003", u"sid": u"35", u"name": u"편지", u"ends": [u"f003_s1_end_c78905c7"], u"menus": [], u"excl": [u"f003_s1_end_c78905c7"]}, {u"file": u"003", u"sid": u"36", u"name": u"사람을 옭아매는 사슬", u"ends": [u"sentei3_9ae20a64"], u"menus": [], u"excl": [u"sentei3_9ae20a64"]}, {u"file": u"003", u"sid": u"37", u"name": u"빼앗긴 카드", u"ends": [u"sentei3_ce50179b"], u"menus": [], u"excl": [u"sentei3_ce50179b"]}], u"ends": [], u"movies": []}, {u"key": u"4주차", u"week": u"4주차", u"short": u"4주차", u"wn": 4, u"colk": u"S", u"sub": u"세상을 보기 위한 여행", u"cg": u"17", u"chips": [{u"file": u"004", u"sid": u"38", u"name": u"변화와 변화", u"ends": [u"f004_00521f00"], u"menus": [], u"excl": [u"f004_00521f00"]}, {u"file": u"004", u"sid": u"39", u"name": u"희미한 구원", u"ends": [u"f004_8d7816f1"], u"menus": [], u"excl": [u"f004_8d7816f1"]}, {u"file": u"004", u"sid": u"40", u"name": u"흰 방문자", u"ends": [u"f004_s1_end_2ee3d1b9"], u"menus": [{u"key": u"004:303", u"opts": [[u"말을 건다", u"+1", u"", u"", u"声をかける", [], u""], [u"말을 걸지 않는다", u"", u"", u"", u"声をかけない", [], u""]], u"infer": []}], u"excl": [u"f004_s1_end_2ee3d1b9"]}, {u"file": u"004", u"sid": u"41", u"name": u"접근", u"ends": [u"f004_s1_end_84f0768a"], u"menus": [], u"excl": [u"f004_s1_end_84f0768a"]}, {u"file": u"004", u"sid": u"42", u"name": u"평온한 학교생활", u"ends": [u"f004_s2_end_53c2f712"], u"menus": [{u"key": u"004:1602", u"opts": [[u"기쁘다", u"+1", u"", u"", u"嬉しい", [], u""], [u"마음이 불편하다", u"", u"", u"", u"気まずい", [], u""]], u"infer": []}], u"excl": [u"f004_s2_end_53c2f712"]}, {u"file": u"004", u"sid": u"43", u"name": u"일본의 문화", u"ends": [u"f004_s2_end_25a636d6"], u"menus": [], u"excl": [u"f004_s2_end_25a636d6"]}, {u"file": u"004", u"sid": u"44", u"name": u"세상의 넓이", u"ends": [u"f004_s2_end_bd790af0"], u"menus": [], u"excl": [u"f004_s2_end_bd790af0"]}, {u"file": u"004", u"sid": u"45", u"name": u"여행자가 남기는 것", u"ends": [u"f004_s2_end_e308a91b"], u"menus": [], u"excl": [u"f004_s2_end_e308a91b"]}, {u"file": u"004", u"sid": u"46", u"name": u"의외×예상 밖", u"ends": [u"sentei4_e2d51b40"], u"menus": [], u"excl": [u"sentei4_e2d51b40"]}, {u"file": u"004", u"sid": u"47", u"name": u"여행자의 기도", u"ends": [u"sentei4_95fc5688"], u"menus": [], u"excl": [u"sentei4_95fc5688"]}, {u"file": u"004", u"sid": u"48", u"name": u"그의 기쁨", u"ends": [u"sentei4_1264379b"], u"menus": [], u"excl": [u"sentei4_1264379b"]}], u"ends": [], u"movies": []}, {u"key": u"5주차", u"week": u"5주차", u"short": u"5주차", u"wn": 5, u"colk": u"S", u"sub": u"뒤틀린 가족애", u"cg": u"20", u"chips": [{u"file": u"005_1", u"sid": u"49", u"name": u"남의 불행은 무슨 맛?", u"ends": [u"f005_1_5615ea4d"], u"menus": [], u"excl": [u"f005_1_5615ea4d"]}, {u"file": u"005_1", u"sid": u"50", u"name": u"카레와 숟가락", u"ends": [u"f005_1_3dbd4fbf"], u"menus": [], u"excl": [u"f005_1_3dbd4fbf"]}, {u"file": u"005_1", u"sid": u"51", u"name": u"떡은 떡집에, 커피는 카페에", u"ends": [u"f005_1_367e0594"], u"menus": [], u"excl": [u"f005_1_367e0594"]}, {u"file": u"005_1", u"sid": u"52", u"name": u"탐문 조사", u"ends": [u"f005_1_c5d60687"], u"menus": [], u"excl": [u"f005_1_c5d60687"]}, {u"file": u"005_1", u"sid": u"53", u"name": u"답 맞추기", u"ends": [u"f005_1_s1_end_37cca6c1"], u"menus": [{u"key": u"005_1:1544", u"opts": [[u"「응, 그럼 내일 학교에서 봐」", u"+1", u"", u"", u"「うん、じゃあまた明日学校で」", [], u""], [u"「응, 그럼 조심해서 가」", u"", u"", u"", u"「うん、じゃあ気を付けてね」", [], u""]], u"infer": []}], u"excl": [u"f005_1_s1_end_37cca6c1"]}, {u"file": u"005_1", u"sid": u"54", u"name": u"우시즈카 시게쓰구", u"ends": [u"f005_1_s1_end_937edcb5"], u"menus": [], u"excl": [u"f005_1_s1_end_937edcb5"]}, {u"file": u"005_1", u"sid": u"55", u"name": u"고독과 아사", u"ends": [u"f005_1_s1_end_03eb3c46"], u"menus": [], u"excl": [u"f005_1_s1_end_03eb3c46"]}, {u"file": u"005_1", u"sid": u"56", u"name": u"통찰", u"ends": [u"f005_1_s1_end_76aa9660"], u"menus": [], u"excl": [u"f005_1_s1_end_76aa9660"]}, {u"file": u"005_1", u"sid": u"57", u"name": u"할 수 있는 일", u"ends": [u"f005_1_s1_end_0dc22f99"], u"menus": [], u"excl": [u"f005_1_s1_end_0dc22f99"]}, {u"file": u"005_1", u"sid": u"58", u"name": u"그날", u"ends": [u"f005_1_s1_end_36583388"], u"menus": [], u"excl": [u"f005_1_s1_end_36583388"]}, {u"file": u"005_1", u"sid": u"59", u"name": u"그 장소", u"ends": [u"f005_1_s1_end_797b0282"], u"menus": [], u"excl": [u"f005_1_s1_end_797b0282"]}, {u"file": u"005_1", u"sid": u"60", u"name": u"싸움의 기억", u"ends": [u"f005_1_s1_end_2464f765"], u"menus": [], u"excl": [u"f005_1_s1_end_2464f765"]}, {u"file": u"005_1", u"sid": u"61", u"name": u"인자한 노인", u"ends": [u"f005_1_s1_end_16cf6086"], u"menus": [], u"excl": [u"f005_1_s1_end_16cf6086"]}, {u"file": u"005_1", u"sid": u"62", u"name": u"느긋한 목욕", u"ends": [u"f005_1_s1_end_5170395d"], u"menus": [], u"excl": [u"f005_1_s1_end_5170395d"]}, {u"file": u"005_1", u"sid": u"63", u"name": u"서랍 속 기억", u"ends": [u"f005_1_s1_end_262abf9f"], u"menus": [], u"excl": [u"f005_1_s1_end_262abf9f"]}, {u"file": u"005_2", u"sid": u"64", u"name": u"심야의 습격, 계속", u"ends": [u"f005_2_s1_end_1a4a5fae"], u"menus": [{u"key": u"005_2:54", u"opts": [[u"말을 건다", u"", u"", u"", u"声をかける", [], u""], [u"말을 걸지 않는다", u"+1", u"", u"", u"声をかけない", [], u""]], u"infer": []}], u"excl": [u"f005_2_s1_end_1a4a5fae"]}, {u"file": u"005_2", u"sid": u"65", u"name": u"카레라이스", u"ends": [u"f005_2_s1_end_7e1b27d8"], u"menus": [], u"excl": [u"f005_2_s1_end_7e1b27d8"]}, {u"file": u"005_2", u"sid": u"66", u"name": u"이어받는다는 것", u"ends": [u"f005_2_s1_end_23d01fb8"], u"menus": [], u"excl": [u"f005_2_s1_end_23d01fb8"]}, {u"file": u"005_2", u"sid": u"67", u"name": u"주어진 이름", u"ends": [u"f005_2_s1_end_b6d8e43a"], u"menus": [], u"excl": [u"f005_2_s1_end_b6d8e43a"]}, {u"file": u"005_2", u"sid": u"68", u"name": u"소극적인 조의 계획", u"ends": [u"f005_2_s2_1_deaec8df", u"f005_2_s2_2_c0f8eacf"], u"menus": [{u"key": u"005_2:3188", u"opts": [[u"「혼자 돌아갈게」", u"0으로 초기화", u"", u"", u"「一人で帰る」", [], u""], [u"「같이 돌아가자」", u"+1", u"", u"", u"「一緒に帰る」", [], u""]], u"infer": []}], u"excl": [u"f005_2_s2_1_deaec8df", u"f005_2_s2_2_c0f8eacf"]}, {u"file": u"005_2", u"sid": u"69", u"name": u"약속 앞에서, 머뭇거림", u"ends": [u"f005_2_s2_end_0d0bbcb7"], u"menus": [], u"excl": [u"f005_2_s2_end_0d0bbcb7"]}, {u"file": u"005_2", u"sid": u"70", u"name": u"적어도", u"ends": [u"f005_2_s2_end_015c723c"], u"menus": [], u"excl": [u"f005_2_s2_end_015c723c"]}, {u"file": u"005_2", u"sid": u"71", u"name": u"잠시의…", u"ends": [u"f005_2_s2_end_83a895a3"], u"menus": [], u"excl": [u"f005_2_s2_end_83a895a3"]}, {u"file": u"005_2", u"sid": u"72", u"name": u"5번째 선정, 시작", u"ends": [u"sentei5_14315fba"], u"menus": [], u"excl": [u"sentei5_14315fba"]}, {u"file": u"005_2", u"sid": u"73", u"name": u"망설임 없는 탈락", u"ends": [u"sentei5_9b6e8198"], u"menus": [], u"excl": [u"sentei5_9b6e8198"]}, {u"file": u"005_2", u"sid": u"74", u"name": u"소멸·충격", u"ends": [u"sentei5_7c1283f2"], u"menus": [], u"excl": [u"sentei5_7c1283f2"]}], u"ends": [], u"movies": []}, {u"key": u"6주차", u"week": u"6주차", u"short": u"6주차", u"wn": 6, u"colk": u"S", u"sub": u"움직이기 시작한 허무", u"cg": u"23", u"chips": [{u"file": u"006", u"sid": u"75", u"name": u"깃발?", u"ends": [u"f006_760e7790"], u"menus": [], u"excl": [u"f006_760e7790"]}, {u"file": u"006", u"sid": u"76", u"name": u"저주의 말", u"ends": [u"f006_c2eb3e51"], u"menus": [], u"excl": [u"f006_c2eb3e51"]}, {u"file": u"006", u"sid": u"77", u"name": u"자성", u"ends": [u"f006_f97ef1c3"], u"menus": [], u"excl": [u"f006_f97ef1c3"]}, {u"file": u"006", u"sid": u"78", u"name": u"도서실에서 첫 만남", u"ends": [u"f006_e2d66e11"], u"menus": [], u"excl": [u"f006_e2d66e11"]}, {u"file": u"006", u"sid": u"79", u"name": u"종이컵과 커피", u"ends": [u"f006_9fd919f3"], u"menus": [], u"excl": [u"f006_9fd919f3"]}, {u"file": u"006", u"sid": u"80", u"name": u"짐승과 소녀", u"ends": [u"f006_bad5bf6a"], u"menus": [], u"excl": [u"f006_bad5bf6a"]}, {u"file": u"006", u"sid": u"81", u"name": u"소녀와 짐승", u"ends": [u"f006_e48c1667"], u"menus": [], u"excl": [u"f006_e48c1667"]}, {u"file": u"006", u"sid": u"82", u"name": u"자신의 죽음, 그때", u"ends": [u"f006_020dbfad"], u"menus": [], u"excl": [u"f006_020dbfad"]}, {u"file": u"006", u"sid": u"83", u"name": u"장마 시작", u"ends": [u"f006_5af0a2b2"], u"menus": [], u"excl": [u"f006_5af0a2b2"]}, {u"file": u"006", u"sid": u"84", u"name": u"기이함", u"ends": [u"sentei6_42b5ecd9"], u"menus": [], u"excl": [u"sentei6_42b5ecd9"]}], u"ends": [], u"movies": []}, {u"key": u"7주차①", u"week": u"7주차①", u"short": u"7주차①", u"wn": 7, u"colk": u"S", u"sub": u"슬픔의 비", u"cg": u"25", u"chips": [{u"file": u"007_1", u"sid": u"85", u"name": u"작별하는 법", u"ends": [u"f007_1_453f1d15"], u"menus": [], u"excl": [u"f007_1_453f1d15"]}, {u"file": u"007_1", u"sid": u"86", u"name": u"혼자서", u"ends": [u"f007_1_5a4c1cd1"], u"menus": [], u"excl": [u"f007_1_5a4c1cd1"]}, {u"file": u"007_1", u"sid": u"87", u"name": u"Ⅸ번째 남자", u"ends": [u"f007_1_ba08040e"], u"menus": [], u"excl": [u"f007_1_ba08040e"]}, {u"file": u"007_1", u"sid": u"88", u"name": u"기묘한 4명", u"ends": [u"f007_1_0f1a15a7"], u"menus": [], u"excl": [u"f007_1_0f1a15a7"]}, {u"file": u"007_1", u"sid": u"89", u"name": u"그 이면에서, 그들은", u"ends": [u"f007_1_5a5d9dc5"], u"menus": [], u"excl": [u"f007_1_5a5d9dc5"]}, {u"file": u"007_1", u"sid": u"90", u"name": u"대활극", u"ends": [u"f007_1_702cf5c8"], u"menus": [], u"excl": [u"f007_1_702cf5c8"]}, {u"file": u"007_1", u"sid": u"91", u"name": u"비 오는 날은 아직 이어진다", u"ends": [u"f007_1_e880f632"], u"menus": [], u"excl": [u"f007_1_e880f632"]}, {u"file": u"007_1", u"sid": u"92", u"name": u"신속의 사수", u"ends": [u"f007_1_3d28abca"], u"menus": [], u"excl": [u"f007_1_3d28abca"]}, {u"file": u"007_1", u"sid": u"93", u"name": u"비와 후회", u"ends": [u"f007_1_333b3a13"], u"menus": [], u"excl": [u"f007_1_333b3a13"]}, {u"file": u"007_1", u"sid": u"94", u"name": u"정의인가 악인가", u"ends": [u"f007_1_25e2d2c6"], u"menus": [], u"excl": [u"f007_1_25e2d2c6"]}, {u"file": u"007_1", u"sid": u"95", u"name": u"빗방울", u"ends": [u"f007_1_26b906cc"], u"menus": [], u"excl": [u"f007_1_26b906cc"]}, {u"file": u"007_1", u"sid": u"96", u"name": u"해후와 분기점", u"ends": [u"f007_1_s1_end_A_0b4c554f", u"f007_1_s1_end_B_bb28d70a"], u"menus": [{u"key": u"007_1:4144", u"opts": [[u"조건을 받아들인다.", u"", u"→ 7주차③", u"B", u"条件を飲む。", [u"7주차③"], u"→ 7주차③"], [u"조건을 받아들이지 않는다.", u"", u"→ 7주차②", u"A", u"条件を飲まない", [u"7주차②"], u"→ 7주차②"]], u"infer": [[1, u"A"]]}], u"excl": [u"f007_1_s1_end_A_0b4c554f", u"f007_1_s1_end_B_bb28d70a"]}], u"ends": [], u"movies": []}, {u"key": u"7주차②", u"week": u"7주차②", u"short": u"7주차②", u"wn": 7, u"colk": u"A", u"sub": u"온갖 부조리에 대한 도전", u"cg": u"29", u"chips": [{u"file": u"007_2", u"sid": u"97", u"name": u"출발", u"ends": [u"f007_2_2b3e6643"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"98", u"name": u"말도 안 돼!", u"ends": [u"f007_2_bebd0e1a"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"99", u"name": u"잠 못 드는 밤", u"ends": [u"f007_2_95579d20"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"100", u"name": u"사건의 전조", u"ends": [u"f007_2_449410e3"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"101", u"name": u"내 이야기를 하자", u"ends": [u"f007_2_5ac662c5"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"102", u"name": u"세상을 향한 메시지", u"ends": [u"f007_2_0565aa2e"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"103", u"name": u"공방·전", u"ends": [u"f007_2_f138d5e7"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"104", u"name": u"공방·후", u"ends": [u"f007_2_74072a1f"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"105", u"name": u"걱정", u"ends": [u"f007_2_8db7ef00"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"106", u"name": u"잠깐의 휴식", u"ends": [u"f007_2_07dacdcc"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"107", u"name": u"그의 진의", u"ends": [u"f007_2_9498146e"], u"menus": [], u"excl": [u"f007_2_9498146e"]}, {u"file": u"007_2", u"sid": u"108", u"name": u"결착, 그리고", u"ends": [u"f007_2_25d27aea"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"109", u"name": u"7번째 선정, 시작", u"ends": [u"sentei7_b9ae470f"], u"menus": [], u"excl": [u"sentei7_b9ae470f"]}, {u"file": u"007_2", u"sid": u"110", u"name": u"그때", u"ends": [u"sentei7_9bf6ab5e"], u"menus": [], u"excl": [u"sentei7_9bf6ab5e"]}], u"ends": [], u"movies": []}, {u"key": u"7주차③", u"week": u"7주차③", u"short": u"7주차③", u"wn": 7, u"colk": u"B", u"sub": u"맞바꾼 것", u"cg": u"28", u"chips": [{u"file": u"007_2", u"sid": u"97", u"name": u"출발", u"ends": [u"f007_2_2b3e6643"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"98", u"name": u"말도 안 돼!", u"ends": [u"f007_2_bebd0e1a"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"99", u"name": u"잠 못 드는 밤", u"ends": [u"f007_2_95579d20"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"100", u"name": u"사건의 전조", u"ends": [u"f007_2_449410e3"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"101", u"name": u"내 이야기를 하자", u"ends": [u"f007_2_5ac662c5"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"102", u"name": u"세상을 향한 메시지", u"ends": [u"f007_2_0565aa2e"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"103", u"name": u"공방·전", u"ends": [u"f007_2_f138d5e7"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"104", u"name": u"공방·후", u"ends": [u"f007_2_74072a1f"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"105", u"name": u"걱정", u"ends": [u"f007_2_8db7ef00"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"106", u"name": u"잠깐의 휴식", u"ends": [u"f007_2_07dacdcc"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"107", u"name": u"그의 진의", u"ends": [u"f007_2_bbb1b2f2"], u"menus": [], u"excl": [u"f007_2_bbb1b2f2"]}, {u"file": u"007_2", u"sid": u"108", u"name": u"결착, 그리고", u"ends": [u"f007_2_25d27aea"], u"menus": [], u"excl": []}, {u"file": u"007_2", u"sid": u"109", u"name": u"7번째 선정, 시작", u"ends": [u"sentei7_901a7c04"], u"menus": [], u"excl": [u"sentei7_901a7c04"]}, {u"file": u"007_2", u"sid": u"110", u"name": u"그때", u"ends": [u"sentei7_6401ddfe"], u"menus": [], u"excl": [u"sentei7_6401ddfe"]}], u"ends": [[u"B", u"결말 1", u"BAD01_clear", u"movies/ED_BAD.mkv", u"나쁜 결말 ①"]], u"movies": [{u"label": u"엔딩 영상 · 결말 1", u"label_open": u"엔딩 영상 · 나쁜 결말 ①", u"path": u"movies/ED_BAD.mkv", u"unlock": u"BAD01_clear", u"after": u""}]}, {u"key": u"8주차", u"week": u"8주차", u"short": u"8주차", u"wn": 8, u"colk": u"A", u"sub": u"생명을 잇는다는 것", u"cg": u"34", u"chips": [{u"file": u"008", u"sid": u"111", u"name": u"답 맞추기", u"ends": [u"f008_s1_end_0d3d48ed"], u"menus": [{u"key": u"008:32", u"opts": [[u"「……나오미?」", u"", u"", u"", u"「……直未？」", [], u""], [u"「……미하루?」", u"", u"", u"", u"「……海晴？」", [], u""], [u"「……마오?」", u"", u"", u"", u"「……真央？」", [], u""]], u"infer": []}], u"excl": [u"f008_s1_end_0d3d48ed"]}, {u"file": u"008", u"sid": u"112", u"name": u"안도", u"ends": [u"f008_s1_end_1e344ac7"], u"menus": [], u"excl": [u"f008_s1_end_1e344ac7"]}, {u"file": u"008", u"sid": u"113", u"name": u"믿고 있어", u"ends": [u"f008_s1_end_ddabdab8"], u"menus": [], u"excl": [u"f008_s1_end_ddabdab8"]}, {u"file": u"008", u"sid": u"114", u"name": u"그녀의 빈틈", u"ends": [u"f008_s1_end_9c5c57e4"], u"menus": [], u"excl": [u"f008_s1_end_9c5c57e4"]}, {u"file": u"008", u"sid": u"115", u"name": u"되새기며", u"ends": [u"f008_s1_end_e4c6e75c"], u"menus": [], u"excl": [u"f008_s1_end_e4c6e75c"]}, {u"file": u"008", u"sid": u"116", u"name": u"험난한 길로", u"ends": [u"f008_s1_end_6d6025e2"], u"menus": [], u"excl": [u"f008_s1_end_6d6025e2"]}, {u"file": u"008", u"sid": u"117", u"name": u"불꽃의 기억, 다시", u"ends": [u"f008_s1_end_16ae6320"], u"menus": [], u"excl": [u"f008_s1_end_16ae6320"]}, {u"file": u"008", u"sid": u"118", u"name": u"그만두자", u"ends": [u"f008_s1_end_beaf9ce0"], u"menus": [], u"excl": [u"f008_s1_end_beaf9ce0"]}, {u"file": u"008", u"sid": u"119", u"name": u"서로 끌리는 나약함", u"ends": [u"f008_s1_end_f6474069"], u"menus": [], u"excl": [u"f008_s1_end_f6474069"]}, {u"file": u"008", u"sid": u"120", u"name": u"소매 안쪽", u"ends": [u"f008_s1_end_cb0f814b"], u"menus": [], u"excl": [u"f008_s1_end_cb0f814b"]}, {u"file": u"008", u"sid": u"121", u"name": u"술맛", u"ends": [u"f008_s1_end_22eb2470"], u"menus": [], u"excl": [u"f008_s1_end_22eb2470"]}, {u"file": u"008", u"sid": u"122", u"name": u"긍정적으로", u"ends": [u"f008_s1_end_19772338"], u"menus": [], u"excl": [u"f008_s1_end_19772338"]}, {u"file": u"008", u"sid": u"123", u"name": u"오데트 말랑송", u"ends": [u"f008_s1_end_87411d79"], u"menus": [], u"excl": [u"f008_s1_end_87411d79"]}, {u"file": u"008", u"sid": u"124", u"name": u"조금이라도", u"ends": [u"f008_s1_end_533723ab"], u"menus": [], u"excl": [u"f008_s1_end_533723ab"]}, {u"file": u"008", u"sid": u"125", u"name": u"말라 시들어", u"ends": [u"f008_s1_end_a16c9e33"], u"menus": [], u"excl": [u"f008_s1_end_a16c9e33"]}, {u"file": u"008", u"sid": u"126", u"name": u"격전", u"ends": [u"f008_s1_end_8f4158c2"], u"menus": [], u"excl": [u"f008_s1_end_8f4158c2"]}, {u"file": u"008", u"sid": u"127", u"name": u"그저, 기다린다", u"ends": [u"f008_s1_end_9d3b85d7"], u"menus": [], u"excl": [u"f008_s1_end_9d3b85d7"]}, {u"file": u"008", u"sid": u"128", u"name": u"서 있던 것은――", u"ends": [u"f008_s1_end_53b71b5a"], u"menus": [], u"excl": [u"f008_s1_end_53b71b5a"]}, {u"file": u"008", u"sid": u"129", u"name": u"그의 꿈", u"ends": [u"f008_s1_end_3bf8a746"], u"menus": [], u"excl": [u"f008_s1_end_3bf8a746"]}, {u"file": u"008", u"sid": u"130", u"name": u"싸움을 끝내고", u"ends": [u"f008_s1_end_8b27eec9"], u"menus": [], u"excl": [u"f008_s1_end_8b27eec9"]}, {u"file": u"008", u"sid": u"131", u"name": u"그러니까, 괜찮아", u"ends": [u"f008_s1_end_a065e2a1"], u"menus": [], u"excl": [u"f008_s1_end_a065e2a1"]}, {u"file": u"008", u"sid": u"132", u"name": u"8번째 선정, 시작", u"ends": [u"sentei8_98f817c5"], u"menus": [], u"excl": [u"sentei8_98f817c5"]}, {u"file": u"008", u"sid": u"133", u"name": u"대파란", u"ends": [u"sentei8_ff79acd2"], u"menus": [], u"excl": [u"sentei8_ff79acd2"]}], u"ends": [], u"movies": []}, {u"key": u"9주차①", u"week": u"9주차①", u"short": u"9주차①", u"wn": 9, u"colk": u"A", u"sub": u"여신의 선정에 얽힌 진실", u"cg": u"36", u"chips": [{u"file": u"009", u"sid": u"134", u"name": u"버리지 못한 것", u"ends": [u"f009_f0713d30"], u"menus": [], u"excl": [u"f009_f0713d30"]}, {u"file": u"009", u"sid": u"135", u"name": u"가능과 불가능", u"ends": [u"f009_7910b038"], u"menus": [], u"excl": [u"f009_7910b038"]}, {u"file": u"009", u"sid": u"136", u"name": u"끊이지 않네요", u"ends": [u"f009_24380909"], u"menus": [], u"excl": [u"f009_24380909"]}, {u"file": u"009", u"sid": u"137", u"name": u"패배자의 밤", u"ends": [u"f009_f8a6902e"], u"menus": [], u"excl": [u"f009_f8a6902e"]}, {u"file": u"009", u"sid": u"138", u"name": u"반지", u"ends": [u"f009_0b046421"], u"menus": [], u"excl": [u"f009_0b046421"]}, {u"file": u"009", u"sid": u"139", u"name": u"균열", u"ends": [u"f009_5d9d2cff"], u"menus": [], u"excl": [u"f009_5d9d2cff"]}, {u"file": u"009", u"sid": u"140", u"name": u"미하루에게――", u"ends": [u"f009_s1_1_96cb0b46", u"f009_s1_2_ad45a7dd"], u"menus": [{u"key": u"009:1911", u"opts": [[u"미하루에게 연락한다", u"", u"→ 9주차②", u"C", u"海晴に連絡をする", [u"9주차②"], u"→ 9주차②"], [u"미하루에게 연락하지 않는다", u"", u"→ 9주차③", u"D", u"海晴に連絡をしない", [u"9주차③"], u"→ 9주차③"]], u"infer": [[0, u"C"], [1, u"D"]]}], u"excl": [u"f009_s1_1_96cb0b46", u"f009_s1_2_ad45a7dd"]}], u"ends": [], u"movies": []}, {u"key": u"9주차②", u"week": u"9주차②", u"short": u"9주차②", u"wn": 9, u"colk": u"C", u"sub": u"정의로워라", u"cg": u"38", u"chips": [{u"file": u"009", u"sid": u"141", u"name": u"고백", u"ends": [u"f009_s1_end_1_1149574d"], u"menus": [], u"excl": [u"f009_s1_end_1_1149574d"]}, {u"file": u"009", u"sid": u"142", u"name": u"뒤숭숭한 아침", u"ends": [u"f009_s1_end_1_052f71ea"], u"menus": [], u"excl": [u"f009_s1_end_1_052f71ea"]}, {u"file": u"009", u"sid": u"144", u"name": u"결의, 다시금", u"ends": [u"f009_s1_end_2_b36c9a8a"], u"menus": [], u"excl": [u"f009_s1_end_2_b36c9a8a"]}, {u"file": u"009", u"sid": u"145", u"name": u"스케일 존스", u"ends": [u"f009_s1_end_2_365a7ac9"], u"menus": [], u"excl": [u"f009_s1_end_2_365a7ac9"]}, {u"file": u"009", u"sid": u"146", u"name": u"과거라는 속박", u"ends": [u"f009_s1_end_2_a3cf8870"], u"menus": [], u"excl": [u"f009_s1_end_2_a3cf8870"]}, {u"file": u"009", u"sid": u"147", u"name": u"내/그의 각오", u"ends": [u"f009_s1_end_2_24c9da39"], u"menus": [], u"excl": [u"f009_s1_end_2_24c9da39"]}, {u"file": u"009", u"sid": u"148", u"name": u"어느 쪽?", u"ends": [u"f009_s1_end_2_6d47dd71"], u"menus": [], u"excl": [u"f009_s1_end_2_6d47dd71"]}, {u"file": u"009", u"sid": u"149", u"name": u"동경", u"ends": [u"f009_s1_end_2_e02b3266"], u"menus": [], u"excl": [u"f009_s1_end_2_e02b3266"]}, {u"file": u"009", u"sid": u"150", u"name": u"필사의 결단", u"ends": [u"f009_root_E_f93cb1d5", u"f009_s3_end_71a76b4f"], u"menus": [{u"key": u"009:4340", u"opts": [[u"받지 않는다", u"", u"→ 9주차④", u"E", u"出ない", [u"9주차④"], u"→ 9주차④"], [u"받는다", u"", u"", u"", u"出る", [], u""]], u"infer": []}, {u"key": u"009:4412", u"opts": [[u"끊는다", u"", u"", u"", u"切る", [], u""], [u"끊지 않는다", u"", u"→ 9주차④", u"E", u"切らない", [u"9주차④"], u"→ 9주차④"]], u"infer": []}], u"excl": [u"f009_root_E_f93cb1d5", u"f009_s3_end_71a76b4f"]}, {u"file": u"009", u"sid": u"151", u"name": u"스타게이저", u"ends": [u"f009_root_E_e0afe145"], u"menus": [], u"excl": [u"f009_root_E_e0afe145"]}, {u"file": u"009", u"sid": u"152", u"name": u"오랜만의 할머니", u"ends": [u"f009_root_E_576c7a72"], u"menus": [], u"excl": [u"f009_root_E_576c7a72"]}, {u"file": u"009", u"sid": u"154", u"name": u"9번째 선정, 시작", u"ends": [u"sentei9_f735ab2a"], u"menus": [], u"excl": [u"sentei9_f735ab2a"]}, {u"file": u"009", u"sid": u"155", u"name": u"여신의 그릇", u"ends": [u"sentei9_409df633"], u"menus": [], u"excl": [u"sentei9_409df633"]}], u"ends": [], u"movies": []}, {u"key": u"9주차③", u"week": u"9주차③", u"short": u"9주차③", u"wn": 9, u"colk": u"D", u"sub": u"소녀의 어둠", u"cg": u"12", u"chips": [{u"file": u"009", u"sid": u"143", u"name": u"들뜬 낮", u"ends": [u"f009_s1_end_2_e5d366a3"], u"menus": [], u"excl": [u"f009_s1_end_2_e5d366a3"]}, {u"file": u"009", u"sid": u"153", u"name": u"끝을 향해", u"ends": [u"f009_route_D_3116d973"], u"menus": [], u"excl": [u"f009_route_D_3116d973"]}, {u"file": u"009", u"sid": u"154", u"name": u"9번째 선정, 시작", u"ends": [u"sentei9_1700c9e0"], u"menus": [], u"excl": [u"sentei9_1700c9e0"]}], u"ends": [[u"D", u"결말 2", u"BAD02_clear", u"movies/ED_BAD.mkv", u"나쁜 결말 ②"]], u"movies": [{u"label": u"엔딩 영상 · 결말 2", u"label_open": u"엔딩 영상 · 나쁜 결말 ②", u"path": u"movies/ED_BAD.mkv", u"unlock": u"BAD02_clear", u"after": u""}]}, {u"key": u"9주차④", u"week": u"9주차④ → 나쁜 결말 ③", u"short": u"9주차④", u"wn": 9, u"colk": u"E", u"sub": u"실패", u"cg": u"bad03", u"chips": [], u"ends": [[u"E", u"결말 3", u"BAD03_clear", u"movies/ED_BAD.mkv", u"나쁜 결말 ③"]], u"movies": [{u"label": u"엔딩 영상 · 결말 3", u"label_open": u"엔딩 영상 · 나쁜 결말 ③", u"path": u"movies/ED_BAD.mkv", u"unlock": u"BAD03_clear", u"after": u""}]}, {u"key": u"10주차", u"week": u"10주차", u"short": u"10주차", u"wn": 10, u"colk": u"C", u"sub": u"남자의 세계", u"cg": u"40", u"chips": [{u"file": u"010", u"sid": u"156", u"name": u"멀리", u"ends": [u"f010_f5b30eda"], u"menus": [], u"excl": [u"f010_f5b30eda"]}, {u"file": u"010", u"sid": u"157", u"name": u"사실", u"ends": [u"f010_6af7654f"], u"menus": [], u"excl": [u"f010_6af7654f"]}, {u"file": u"010", u"sid": u"158", u"name": u"겨우 이것뿐", u"ends": [u"f010_7ae23944"], u"menus": [], u"excl": [u"f010_7ae23944"]}, {u"file": u"010", u"sid": u"159", u"name": u"움직이기 시작한 톱니바퀴", u"ends": [u"f010_d5ec2e50"], u"menus": [], u"excl": [u"f010_d5ec2e50"]}, {u"file": u"010", u"sid": u"160", u"name": u"멈추지 않아", u"ends": [u"f010_14fc8ddd"], u"menus": [], u"excl": [u"f010_14fc8ddd"]}, {u"file": u"010", u"sid": u"161", u"name": u"항거하는 삶", u"ends": [u"f010_a953b312"], u"menus": [], u"excl": [u"f010_a953b312"]}, {u"file": u"010", u"sid": u"162", u"name": u"필사적", u"ends": [u"f010_6c32e3a4"], u"menus": [], u"excl": [u"f010_6c32e3a4"]}, {u"file": u"010", u"sid": u"163", u"name": u"비장의 패", u"ends": [u"f010_0c63c81d"], u"menus": [], u"excl": [u"f010_0c63c81d"]}, {u"file": u"010", u"sid": u"164", u"name": u"의외로 힘들어", u"ends": [u"f010_904d29b5"], u"menus": [], u"excl": [u"f010_904d29b5"]}, {u"file": u"010", u"sid": u"65", u"name": u"카레라이스", u"ends": [u"f010_09907dbb"], u"menus": [], u"excl": [u"f010_09907dbb"]}, {u"file": u"010", u"sid": u"166", u"name": u"칠석", u"ends": [u"f010_0cde7373"], u"menus": [], u"excl": [u"f010_0cde7373"]}, {u"file": u"010", u"sid": u"167", u"name": u"옛 모습", u"ends": [u"f010_7704f9d6"], u"menus": [], u"excl": [u"f010_7704f9d6"]}, {u"file": u"010", u"sid": u"168", u"name": u"10번째 선정, 시작", u"ends": [u"sentei10_9c13d417"], u"menus": [], u"excl": [u"sentei10_9c13d417"]}, {u"file": u"010", u"sid": u"169", u"name": u"기도", u"ends": [u"sentei10_19646e07"], u"menus": [], u"excl": [u"sentei10_19646e07"]}], u"ends": [], u"movies": []}, {u"key": u"11주차①", u"week": u"11주차①", u"short": u"11주차①", u"wn": 11, u"colk": u"C", u"sub": u"매듭짓기까지", u"cg": u"41", u"chips": [{u"file": u"011_01", u"sid": u"170", u"name": u"엇갈린 운명", u"ends": [u"f011_01_caea79b0"], u"menus": [], u"excl": [u"f011_01_caea79b0"]}, {u"file": u"011_01", u"sid": u"171", u"name": u"답", u"ends": [u"f011_01_46030be5"], u"menus": [], u"excl": [u"f011_01_46030be5"]}, {u"file": u"011_01", u"sid": u"172", u"name": u"두 사람의 앞날", u"ends": [u"f011_01_s1_2_e510a74b", u"f011_01_s2_1_b0a7dfed", u"f011_01_s2_2_b91768be"], u"menus": [{u"key": u"011_01:1088", u"opts": [[u"대답을 한다", u"", u"→ 11주차③/④", u"G", u"返事をする", [u"11주차③", u"11주차④"], u"→ 11주차③/④"], [u"대답은 할 수 없다", u"", u"→ 11주차②", u"F", u"返事はできない", [u"11주차②"], u"→ 11주차②"]], u"infer": [[0, u"GH"], [1, u"F"]]}, {u"key": u"011_01:1113", u"opts": [[u"미하루와 사귄다", u"", u"→ 11주차③", u"G", u"海晴と付き合う", [u"11주차③"], u"→ 11주차③"], [u"미하루와는 사귈 수 없다", u"", u"→ 11주차④", u"H", u"海晴とは付き合えない", [u"11주차④"], u"→ 11주차④"]], u"infer": [[0, u"G"], [1, u"H"]]}], u"excl": [u"f011_01_s1_2_e510a74b", u"f011_01_s2_1_b0a7dfed", u"f011_01_s2_2_b91768be"]}], u"ends": [], u"movies": []}, {u"key": u"11주차②", u"week": u"11주차②", u"short": u"11주차②", u"wn": 11, u"colk": u"F", u"sub": u"밝혀지는 진실들", u"cg": u"42", u"chips": [{u"file": u"011_01", u"sid": u"173", u"name": u"혼자 보내는 밤", u"ends": [u"f011_01_s2_end_7a5257d8"], u"menus": [], u"excl": []}, {u"file": u"011_01", u"sid": u"174", u"name": u"하룻밤이 지나고…", u"ends": [u"f011_01_s2_end_42152852"], u"menus": [], u"excl": []}, {u"file": u"011_01F", u"sid": u"175", u"name": u"다이아나 해리슨", u"ends": [u"f011_01F_8489982c"], u"menus": [], u"excl": [u"f011_01F_8489982c"]}, {u"file": u"011_01F", u"sid": u"176", u"name": u"소녀의 죽음", u"ends": [u"f011_01F_a7af9748"], u"menus": [], u"excl": [u"f011_01F_a7af9748"]}, {u"file": u"011_02", u"sid": u"182", u"name": u"11번째 선정, 시작", u"ends": [u"sentei11_909e2717"], u"menus": [], u"excl": []}, {u"file": u"011_02", u"sid": u"183", u"name": u"세계의 큰 강", u"ends": [u"sentei11_4d222207"], u"menus": [], u"excl": [u"sentei11_4d222207"]}], u"ends": [], u"movies": []}, {u"key": u"11주차③", u"week": u"11주차③", u"short": u"11주차③", u"wn": 11, u"colk": u"G", u"sub": u"가까워진 거리", u"cg": u"44", u"chips": [{u"file": u"011_01", u"sid": u"173", u"name": u"혼자 보내는 밤", u"ends": [u"f011_01_s2_end_7a5257d8"], u"menus": [], u"excl": []}, {u"file": u"011_01", u"sid": u"174", u"name": u"하룻밤이 지나고…", u"ends": [u"f011_01_s2_end_42152852"], u"menus": [], u"excl": []}, {u"file": u"011_01G", u"sid": u"177", u"name": u"첫 데이트", u"ends": [u"f011_01G_1244cf91"], u"menus": [], u"excl": [u"f011_01G_1244cf91"]}, {u"file": u"011_01G", u"sid": u"178", u"name": u"레몬빛", u"ends": [u"f011_01G_5f6482ec"], u"menus": [], u"excl": [u"f011_01G_5f6482ec"]}, {u"file": u"011_01G", u"sid": u"179", u"name": u"평생의 추억", u"ends": [u"f011_01G_c5dcfd51"], u"menus": [], u"excl": [u"f011_01G_c5dcfd51"]}, {u"file": u"011_02", u"sid": u"182", u"name": u"11번째 선정, 시작", u"ends": [u"sentei11_909e2717"], u"menus": [], u"excl": []}, {u"file": u"011_02GH", u"sid": u"184", u"name": u"지켜야 할 것", u"ends": [u"f011_02GH_ea5f8e7c"], u"menus": [], u"excl": []}, {u"file": u"011_02GH", u"sid": u"185", u"name": u"진의", u"ends": [u"f011_02GH_13203090"], u"menus": [], u"excl": [u"f011_02GH_13203090"]}], u"ends": [], u"movies": []}, {u"key": u"11주차④", u"week": u"11주차④", u"short": u"11주차④", u"wn": 11, u"colk": u"H", u"sub": u"엇갈린 마음", u"cg": u"43", u"chips": [{u"file": u"011_01", u"sid": u"173", u"name": u"혼자 보내는 밤", u"ends": [u"f011_01_s2_end_7a5257d8"], u"menus": [], u"excl": []}, {u"file": u"011_01", u"sid": u"174", u"name": u"하룻밤이 지나고…", u"ends": [u"f011_01_s2_end_42152852"], u"menus": [], u"excl": []}, {u"file": u"011_01H", u"sid": u"180", u"name": u"함께", u"ends": [u"f011_01H_2147325e"], u"menus": [], u"excl": [u"f011_01H_2147325e"]}, {u"file": u"011_01H", u"sid": u"181", u"name": u"밤을 음미하다", u"ends": [u"f011_01H_30a1f10a"], u"menus": [], u"excl": [u"f011_01H_30a1f10a"]}, {u"file": u"011_02", u"sid": u"182", u"name": u"11번째 선정, 시작", u"ends": [u"sentei11_909e2717"], u"menus": [], u"excl": []}, {u"file": u"011_02GH", u"sid": u"184", u"name": u"지켜야 할 것", u"ends": [u"f011_02GH_ea5f8e7c"], u"menus": [], u"excl": []}, {u"file": u"011_02GH", u"sid": u"185", u"name": u"진의", u"ends": [u"f011_02GH_aa04a0af"], u"menus": [], u"excl": [u"f011_02GH_aa04a0af"]}], u"ends": [], u"movies": []}, {u"key": u"12주차①", u"week": u"12주차①", u"short": u"12주차①", u"wn": 12, u"colk": u"F", u"sub": u"당연한 소원", u"cg": u"47", u"chips": [{u"file": u"012_01F", u"sid": u"186", u"name": u"망각 너머", u"ends": [u"f012_01F_3d5a5550"], u"menus": [], u"excl": [u"f012_01F_3d5a5550"]}, {u"file": u"012_01F", u"sid": u"187", u"name": u"이어지는 마음", u"ends": [u"f012_01F_554cf6b0"], u"menus": [], u"excl": [u"f012_01F_554cf6b0"]}, {u"file": u"012_01F", u"sid": u"188", u"name": u"급전직하", u"ends": [u"f012_01F_ed114b77"], u"menus": [], u"excl": [u"f012_01F_ed114b77"]}, {u"file": u"012_01F", u"sid": u"189", u"name": u"정체", u"ends": [u"f012_01F_2d2a6835"], u"menus": [], u"excl": [u"f012_01F_2d2a6835"]}, {u"file": u"012_01F", u"sid": u"190", u"name": u"각오하고 있어", u"ends": [u"f012_01F_966d9a26"], u"menus": [], u"excl": [u"f012_01F_966d9a26"]}, {u"file": u"012_01F", u"sid": u"191", u"name": u"안녕", u"ends": [u"f012_01F_acf712d2"], u"menus": [], u"excl": [u"f012_01F_acf712d2"]}, {u"file": u"012_01F", u"sid": u"192", u"name": u"저마다의 소원", u"ends": [u"f012_01F_56c21568"], u"menus": [], u"excl": [u"f012_01F_56c21568"]}, {u"file": u"012_01F", u"sid": u"193", u"name": u"과거와 현재", u"ends": [u"f012_01F_ad2a4c49"], u"menus": [], u"excl": [u"f012_01F_ad2a4c49"]}, {u"file": u"012_01F", u"sid": u"194", u"name": u"언젠가, 다시", u"ends": [u"f012_01F_d5e3d463"], u"menus": [], u"excl": [u"f012_01F_d5e3d463"]}, {u"file": u"012_01F", u"sid": u"195", u"name": u"전야", u"ends": [u"f012_01F_33ceb2f1"], u"menus": [], u"excl": [u"f012_01F_33ceb2f1"]}, {u"file": u"012_01F", u"sid": u"196", u"name": u"마지막 선정, 시작", u"ends": [u"sentei12_109c3c25"], u"menus": [], u"excl": [u"sentei12_109c3c25"]}, {u"file": u"012_01F", u"sid": u"197", u"name": u"끌어안고", u"ends": [u"sentei12_0396e8f4"], u"menus": [], u"excl": [u"sentei12_0396e8f4"]}], u"ends": [], u"movies": []}, {u"key": u"12주차②", u"week": u"12주차②", u"short": u"12주차②", u"wn": 12, u"colk": u"G", u"sub": u"미하루", u"cg": u"45", u"chips": [{u"file": u"012_01GH", u"sid": u"200", u"name": u"거짓", u"ends": [u"f012_01GH_34843ac4"], u"menus": [], u"excl": []}, {u"file": u"012_01GH", u"sid": u"201", u"name": u"나만의, 나", u"ends": [u"f012_01GH_ef1e2db3"], u"menus": [], u"excl": [u"f012_01GH_ef1e2db3"]}, {u"file": u"012_01GH", u"sid": u"202", u"name": u"존재의 증명", u"ends": [u"f012_01GH_30e6d495"], u"menus": [], u"excl": [u"f012_01GH_30e6d495"]}, {u"file": u"012_01GH", u"sid": u"203", u"name": u"권리", u"ends": [u"f012_01GH_s2_1_663a9cba", u"f012_01GH_s2_2_bf3a97f6"], u"menus": [{u"key": u"012_01GH:969", u"opts": [[u"눈치채고 있다", u"", u"", u"", u"気付いている", [], u""], [u"눈치채지 못했다", u"", u"", u"", u"気付いていない", [], u""]], u"infer": []}, {u"key": u"012_01GH:1125", u"opts": [[u"운명을 바꾼다", u"", u"→ 12주차③", u"U", u"運命を変える", [u"12주차③"], u"→ 12주차③"], [u"아무것도 하지 않는다", u"", u"→ 결말 4", u"G", u"何もしない", [u"MIHARU_clear"], u"→ 미하루 결말"]], u"infer": []}], u"excl": [u"f012_01GH_s2_1_663a9cba", u"f012_01GH_s2_2_bf3a97f6"]}], u"ends": [[u"G", u"결말 4", u"MIHARU_clear", u"movies/ED_MHR_UNH.mkv", u"미하루 결말"]], u"movies": [{u"label": u"엔딩 영상 · 결말 4", u"label_open": u"엔딩 영상 · 미하루 결말", u"path": u"movies/ED_MHR_UNH.mkv", u"unlock": u"MIHARU_clear", u"after": u""}]}, {u"key": u"12주차③", u"week": u"12주차③", u"short": u"12주차③", u"wn": 12, u"colk": u"U", u"sub": u"업", u"cg": u"good03", u"chips": [], u"ends": [[u"U", u"결말 5", u"UNHAPPY_clear", u"movies/ED_MHR_UNH.mkv", u"불행한 결말"]], u"movies": [{u"label": u"엔딩 영상 · 결말 5", u"label_open": u"엔딩 영상 · 불행한 결말", u"path": u"movies/ED_MHR_UNH.mkv", u"unlock": u"UNHAPPY_clear", u"after": u""}]}, {u"key": u"12주차④", u"week": u"12주차 → 나쁜 결말 ④", u"short": u"12주차", u"wn": 12, u"colk": u"H", u"sub": u"", u"cg": u"bad04", u"chips": [{u"file": u"012_01GH", u"sid": u"200", u"name": u"거짓", u"ends": [u"f012_01GH_34843ac4"], u"menus": [], u"excl": []}], u"ends": [[u"H", u"결말 6", u"BAD04_clear", u"movies/ED_BAD.mkv", u"나쁜 결말 ④"]], u"movies": [{u"label": u"엔딩 영상 · 결말 6", u"label_open": u"엔딩 영상 · 나쁜 결말 ④", u"path": u"movies/ED_BAD.mkv", u"unlock": u"BAD04_clear", u"after": u""}]}, {u"key": u"13주차", u"week": u"13주차, 그리고……", u"short": u"13주차+", u"wn": 13, u"colk": u"F", u"sub": u"미래", u"cg": u"50", u"chips": [{u"file": u"012_02", u"sid": u"198", u"name": u"목소리", u"ends": [u"f012_02_2cd0dd51"], u"menus": [], u"excl": [u"f012_02_2cd0dd51"]}, {u"file": u"012_02", u"sid": u"199", u"name": u"고마워", u"ends": [u"f012_02_5f93f4f4"], u"menus": [], u"excl": [u"f012_02_5f93f4f4"]}], u"ends": [[u"F", u"결말 7", u"TRUE_clear", u"movies/ED_TRUE.mkv", u"진 결말"], [u"S", u"2회차 서장", u"ANY_GOOD", u"", u"2회차 서장"]], u"movies": [{u"label": u"엔딩 영상 · 결말 7", u"label_open": u"엔딩 영상 · 진 결말", u"path": u"movies/ED_TRUE.mkv", u"unlock": u"TRUE_clear", u"after": u""}]}]
    F12_FC_LINKS = [[u"1주차", u"2주차", u"S", u""], [u"2주차", u"3주차", u"S", u""], [u"3주차", u"4주차", u"S", u""], [u"4주차", u"5주차", u"S", u""], [u"5주차", u"6주차", u"S", u""], [u"6주차", u"7주차①", u"S", u""], [u"7주차①", u"7주차②", u"A", u"받아들이지 않는다 (호감도 6 이상)"], [u"7주차①", u"7주차③", u"B", u"받아들인다 / 호감도 6 미만"], [u"7주차②", u"8주차", u"A", u""], [u"8주차", u"9주차①", u"A", u""], [u"9주차①", u"9주차②", u"C", u"연락한다"], [u"9주차①", u"9주차③", u"D", u"연락하지 않는다"], [u"9주차②", u"9주차④", u"E", u"받지 않는다 / 받고 끊지 않는다"], [u"9주차②", u"10주차", u"C", u"받고 끊는다"], [u"10주차", u"11주차①", u"C", u""], [u"11주차①", u"11주차②", u"F", u"대답은 할 수 없다"], [u"11주차①", u"11주차③", u"G", u"대답한다 → 사귄다"], [u"11주차①", u"11주차④", u"H", u"대답한다 → 사귈 수 없다"], [u"11주차②", u"12주차①", u"F", u""], [u"11주차③", u"12주차②", u"G", u""], [u"11주차④", u"12주차④", u"H", u""], [u"12주차②", u"12주차③", u"U", u"운명을 바꾼다"], [u"12주차①", u"13주차", u"F", u""]]
    F12_FC_LANE_FLAGS = {u"S": u"", u"A": u"A", u"B": u"B", u"C": u"AC", u"D": u"AD", u"E": u"ACE", u"F": u"ACF", u"G": u"ACG", u"H": u"ACH", u"U": u"ACG"}
    F12_FC_LANE_COLOR = {u"S": u"#8d8d8d", u"A": u"#d9b65c", u"B": u"#c0392b", u"C": u"#d9b65c", u"D": u"#c0392b", u"E": u"#c0392b",
                         u"F": u"#efe6d2", u"G": u"#e0a050", u"H": u"#c0392b", u"U": u"#e0a050", u"M": u"#d9b65c"}
    F12_FC_GOLD = u"#d9b65c"
    F12_FC_UNKNOWN = u"#c4c4c4"
    # 줄기 성격이 드러나는 때: 갈래는 그 결말을 봤을 때, 본편은 다음 칸까지 가 봤을 때
    F12_FC_LANE_ENDFLAGS = {u"B": (u"BAD01_clear",), u"D": (u"BAD02_clear",), u"E": (u"BAD03_clear",), u"H": (u"BAD04_clear",),
                            u"G": (u"MIHARU_clear", u"UNHAPPY_clear"), u"U": (u"UNHAPPY_clear",), u"F": (u"TRUE_clear",)}
    F12_FC_LANE_PASS = {u"A": u"8주차", u"C": u"10주차"}
    F12_FC_ROMAN = [u"Ⅰ", u"Ⅱ", u"Ⅲ", u"Ⅳ", u"Ⅴ", u"Ⅵ", u"Ⅶ", u"Ⅷ", u"Ⅸ", u"Ⅹ", u"Ⅺ", u"Ⅻ", u"ⅩⅢ"]
    F12_FC_CW = 166
    F12_FC_TW = 150
    F12_FC_TH = 84
    F12_FC_TY = 80
    F12_FC_VIEW_W = 1001
    F12_FC_ENDING_CG = (u"bad03", u"bad04", u"good03")

    F12_FC_CHIPMAP = {}
    for _c in F12_FC_COLS:
        for _ch in _c["chips"]:
            F12_FC_CHIPMAP[(_c["colk"], _ch["file"], _ch["sid"])] = _ch

    class _F12FCState(object):
        # 스토어 밖 상태 (Replay 의 스토어 초기화를 견딘다)
        target = None
        target_colk = None
        pending = None
        index = None
        thumbs = {}
        movie = None

    def _f12_fc_base(fn):
        fn = (fn or "").replace("\\", "/")
        return fn.rsplit("/", 1)[-1].rsplit(".", 1)[0]

    def f12_fc_index():
        """(파일, 장면 id) → set_info_scene 을 담은 python 문 노드 (시나리오 파일만)."""
        if _F12FCState.index is None:
            idx = {}
            for node in renpy.game.script.all_stmts:
                if isinstance(node, renpy.ast.Python) and "scenario/" in (node.filename or "").replace("\\", "/"):
                    src = node.code.source
                    if u"set_info_scene(" in src:
                        for m in _f12_fc_re.finditer(r'set_info_scene\("(\w+)"\)', src):
                            idx.setdefault((_f12_fc_base(node.filename), m.group(1)), node)
            _F12FCState.index = idx
        return _F12FCState.index

    def f12_fc_done(ch):
        if not ch:
            return False
        seen = renpy.game.persistent._seen_translates
        for t in ch["ends"]:
            if t in seen:
                return True
        return False

    def f12_fc_flags_now():
        rv = set()
        for k in u"ABCDEFGH":
            if getattr(store, "flags_route_" + k, False):
                rv.add(k)
        return rv

    def f12_fc_lane_of(flags):
        for k in u"FGH":
            if k in flags:
                return k
        if u"E" in flags:
            return u"E"
        for k in u"CD":
            if k in flags:
                return k
        if u"A" in flags:
            return u"A"
        if u"B" in flags:
            return u"B"
        return u"S"

    def f12_fc_compat(colk, flags):
        return colk == u"S" or colk in flags or (colk == u"U" and u"G" in flags)

    def f12_fc_revealed():
        # Existing saves may have an explicit chart choice, including False.
        choice = renpy.game.persistent.f12_fc_reveal
        if choice is None:
            return f12_bonus_enabled()
        return bool(choice)

    def f12_fc_set_revealed(reveal):
        renpy.game.persistent.f12_fc_reveal = bool(reveal)
        renpy.save_persistent()

    def f12_fc_bonus_preview():
        return f12_bonus_enabled() and f12_fc_revealed()

    def f12_fc_end_open(e):
        if f12_fc_bonus_preview():
            return True
        p = renpy.game.persistent
        if e[2].startswith(u"chip:"):
            return f12_fc_done(F12_FC_CHIPMAP.get(tuple(e[2][5:].split(u"|"))))
        if e[2] == u"ANY_GOOD":
            return bool(getattr(p, "TRUE_clear", False) or getattr(p, "UNHAPPY_clear", False) or getattr(p, "MIHARU_clear", False))
        return bool(getattr(p, e[2], False))

    def f12_fc_play_movie(path):
        """오프닝·엔딩 영상을 새 컨텍스트에서 재생. 클릭하면 건너뛰고, 끝나면 차트로 돌아온다."""
        if not path:
            return
        _F12FCState.movie = path
        try:
            renpy.call_in_new_context("f12_fc_play_movie_label")
        finally:
            # 컨텍스트마다 음악 상태를 따로 가지므로 바깥에서도 멈춘다(안 하면 전체 화면 영상이 차트 위에 남는다)
            renpy.music.stop(channel="movie", fadeout=0)

    def f12_fc_lane_known(k, opened, reveal):
        if reveal or k in (u"S", u"M"):
            return True
        if k in F12_FC_LANE_PASS:
            return bool(opened.get(F12_FC_LANE_PASS[k]))
        p = renpy.game.persistent
        for f in F12_FC_LANE_ENDFLAGS.get(k, ()):
            if getattr(p, f, False):
                return True
        return False

    def f12_fc_color(k, opened, reveal):
        if f12_fc_lane_known(k, opened, reveal):
            return F12_FC_LANE_COLOR.get(k, F12_FC_GOLD)
        return F12_FC_UNKNOWN

    def f12_fc_dest_open(dest, opened, reveal):
        if reveal:
            return True
        p = renpy.game.persistent
        for d in dest:
            if d.endswith(u"_clear"):
                if getattr(p, d, False):
                    return True
            elif opened.get(d):
                return True
        return False

    def f12_fc_legend(opened, reveal):
        """지금 화면에 쓰인 색만, 드러난 것만 설명한다."""
        used = set()
        for a, b, ck, label in F12_FC_LINKS:
            if opened.get(b):
                used.add(ck)
        for col in F12_FC_COLS:
            if opened.get(col["key"]):
                used.add(col["colk"])
        used.discard(u"S")
        known = set([k for k in used if f12_fc_lane_known(k, opened, reveal)])
        rv = []
        if known & set([u"A", u"C"]):
            rv.append((F12_FC_LANE_COLOR[u"A"], u"본편 줄기"))
        if used - known:
            rv.append((F12_FC_UNKNOWN, u"아직 모르는 줄기"))
        p = renpy.game.persistent
        if known & set([u"B", u"D", u"E", u"H"]):
            anybad = [f for f in (u"BAD01_clear", u"BAD02_clear", u"BAD03_clear", u"BAD04_clear") if getattr(p, f, False)]
            rv.append((F12_FC_LANE_COLOR[u"B"], u"나쁜 결말" if anybad else u"결말 1·2·3·6 줄기"))
        if known & set([u"G", u"U"]):
            rv.append((F12_FC_LANE_COLOR[u"G"], u"미하루·불행" if getattr(p, "MIHARU_clear", False) else u"결말 4·5 줄기"))
        if u"F" in known:
            rv.append((F12_FC_LANE_COLOR[u"F"], u"진 결말 줄기" if getattr(p, "TRUE_clear", False) else u"결말 7 줄기"))
        return rv

    def f12_fc_col_state(col):
        rd = 0
        for ch in col["chips"]:
            if f12_fc_done(ch):
                rd += 1
        return rd, len(col["chips"])

    def f12_fc_col_colored(col, state):
        """칸이 드러났는지: 그 줄기에만 있는 끝 줄을 읽었거나 그 칸의 결말을 봤을 때. 다른 줄기와 같이 쓰는 장면만 읽어서는 안 열린다."""
        seen = renpy.game.persistent._seen_translates
        for ch in col["chips"]:
            for t in ch.get("excl", ()):
                if t in seen:
                    return True
        p = renpy.game.persistent
        for e in col["ends"]:
            if e[2] == u"ANY_GOOD" or e[2].startswith(u"chip:"):
                continue
            if getattr(p, e[2], False):
                return True
        return False

    def f12_fc_current(mode):
        """(열 번호, 장면 번호) 또는 None. ingame=지금 읽는 장면, replay=지금 다시 보는 장면."""
        if mode == u"replay":
            tgt = _F12FCState.target
            if tgt is None:
                return None
            for i, col in enumerate(F12_FC_COLS):
                if col["colk"] != _F12FCState.target_colk:
                    continue
                for j, ch in enumerate(col["chips"]):
                    if (ch["file"], ch["sid"]) == tgt:
                        return (i, j)
            return None
        if mode != u"ingame" or main_menu:
            return None
        cur = getattr(store, "f12_fc_cur", None)
        cands = []
        if cur:
            for i, col in enumerate(F12_FC_COLS):
                for j, ch in enumerate(col["chips"]):
                    if (ch["file"], ch["sid"]) == tuple(cur) or (cur[0] is None and ch["sid"] == cur[1]):
                        cands.append((i, j))
        else:
            # 이 차트를 넣기 전 세이브: 세이브 이름으로 장면 id 를 거꾸로 찾는다
            sname = getattr(store, "save_name", None)
            sids = [k for k, v in getattr(store, "scenes", {}).items() if v == sname] if sname else []
            for i, col in enumerate(F12_FC_COLS):
                for j, ch in enumerate(col["chips"]):
                    if ch["sid"] in sids:
                        cands.append((i, j))
        if not cands:
            return None
        flags = f12_fc_flags_now()
        lane = f12_fc_lane_of(flags)
        for i, j in cands:
            if F12_FC_COLS[i]["colk"] == lane:
                return (i, j)
        for i, j in cands:
            if f12_fc_compat(F12_FC_COLS[i]["colk"], flags):
                return (i, j)
        return cands[0]

    def f12_fc_default_sel(mode):
        cur = f12_fc_current(mode)
        if cur:
            return cur[0]
        best = 0
        for i, col in enumerate(F12_FC_COLS):
            if f12_fc_col_colored(col, f12_fc_col_state(col)):
                best = i
        return best

    def f12_fc_scroll(adj, idx):
        total = len(F12_FC_COLS) * F12_FC_CW + 24
        adj.range = max(0, total - F12_FC_VIEW_W)
        adj.change(int(max(0, min(idx * F12_FC_CW - F12_FC_VIEW_W // 2 + F12_FC_TW // 2 + 12, adj.range))))

    def f12_fc_scroll_by(adj, delta):
        adj.change(adj.value + delta)

    def f12_fc_thumb(col, opened, colored, reveal):
        cg = col["cg"]
        ending = cg in F12_FC_ENDING_CG
        show = opened and (not ending or colored or reveal)
        key = (col["key"], show, colored)
        img = _F12FCState.thumbs.get(key)
        if img is None:
            if not show:
                img = im.Scale("gui/thumb_ecg_nodata.png", F12_FC_TW, F12_FC_TH)
            else:
                if ending:
                    w, h = (368, 266) if cg.startswith(u"good") else (270, 200)
                    ch_ = int(w * F12_FC_TH / F12_FC_TW)
                    img = im.Scale(im.Crop("gui/%s_idle.png" % cg, (0, (h - ch_) // 2, w, ch_)), F12_FC_TW, F12_FC_TH)
                else:
                    img = im.Scale("gui/thumb_ecg_%s.png" % cg, F12_FC_TW, F12_FC_TH)
                if not colored:
                    img = im.MatrixColor(img, im.matrix.desaturate() * im.matrix.brightness(-0.3))
            _F12FCState.thumbs[key] = img
        return img

    F12_FC_GEAR_READ = im.Scale(im.MatrixColor("gui/right_click_menu_frame_03.png", im.matrix.colorize(u"#6a5420", u"#ffe29a")), 13, 13)
    F12_FC_GEAR_UNREAD = im.Scale(im.MatrixColor("gui/right_click_menu_frame_03.png", im.matrix.colorize(u"#2a2a2a", u"#8a8a8a")), 13, 13)
    F12_FC_NUM_SEL = im.MatrixColor("gui/num_hover.png", im.matrix.colorize(u"#000000", F12_FC_GOLD))

    def f12_fc_ribbon_ops(opened, reveal):
        ops = []
        TY = F12_FC_TY
        colx = {}
        for i, col in enumerate(F12_FC_COLS):
            colx[col["key"]] = 12 + i * F12_FC_CW
        tracks = []
        arcs = []
        for a, b, ck, label in F12_FC_LINKS:
            if not opened.get(b):
                continue
            color = f12_fc_color(ck, opened, reveal)
            xa = colx[a] + F12_FC_TW // 2
            xb = colx[b] + F12_FC_TW // 2
            if abs(xb - xa) <= F12_FC_CW + 1 and not label:
                ops.append((u"r", colx[a] + F12_FC_TW, TY + F12_FC_TH // 2 - 1, F12_FC_CW - F12_FC_TW, 2, color))
                continue
            lo = min(xa, xb) - 4
            hi = max(xa, xb) + 4
            ti = None
            for t, tr in enumerate(tracks):
                ok = True
                for l, h in tr:
                    if not (hi < l or lo > h):
                        ok = False
                        break
                if ok:
                    tr.append((lo, hi))
                    ti = t
                    break
            if ti is None:
                tracks.append([(lo, hi)])
                ti = len(tracks) - 1
            arcs.append((xa, xb, ti, color, label))
        for xa, xb, ti, color, label in arcs:
            h = 14 + 15 * ti
            ops.append((u"r", xa - 1, TY - h, 2, h, color))
            ops.append((u"r", xb - 1, TY - h, 2, h, color))
            ops.append((u"r", min(xa, xb), TY - h - 1, abs(xb - xa), 2, color))
            if label:
                ops.append((u"t", (xa + xb) // 2, TY - h, label, color, 9))
        return ops

    def f12_fc_pick(menu, col, mode):
        """이번 회차에 고른 선택지 (순번, 추정 여부) 또는 None. 인게임 화면에서만."""
        if mode != u"ingame" or main_menu:
            return None
        flags = f12_fc_flags_now()
        if not f12_fc_compat(col["colk"], flags):
            return None
        picks = getattr(store, "f12_fc_picks", None) or {}
        rec = picks.get(menu["key"])
        if rec is not None:
            for i, o in enumerate(menu["opts"]):
                if o[4] == rec:
                    return (i, False)
        for i, letters in menu["infer"]:
            for k in letters:
                if k in flags:
                    return (i, True)
        return None

    def f12_fc_grid(col, reveal, mode, cur_chip, opened):
        """고른 열을 4열로. 행: ('c', 장면, 읽음, 지금) / ('o', 글, 효과, 갈래글, 갈래색, 보임, 읽음, 고름, 추정)"""
        units = []
        for j, ch in enumerate(col["chips"]):
            rd = f12_fc_done(ch)
            now = (j == cur_chip)
            rows = [(u"c", ch, rd, now)]
            for m in ch["menus"]:
                pk = f12_fc_pick(m, col, mode)
                show = rd or reveal or (pk is not None)
                for i, o in enumerate(m["opts"]):
                    chosen = pk is not None and pk[0] == i
                    dest = o[5] if len(o) > 5 else []
                    tag = u""
                    if o[2] and f12_fc_dest_open(dest, opened, reveal):
                        seen_end = [d for d in dest if d.endswith(u"_clear") and getattr(renpy.game.persistent, d, False)]
                        tag = o[6] if (seen_end and len(o) > 6 and o[6]) else o[2]
                    tagc = f12_fc_color(o[3], opened, reveal) if o[3] else F12_FC_GOLD
                    rows.append((u"o", o[0], o[1], tag, tagc, show, rd or (pk is not None), chosen, chosen and pk[1]))
            units.append(rows)
            for mv in col.get("movies", []):
                if mv["after"] and mv["after"] == ch["sid"] and (reveal or f12_fc_end_open([u"", u"", mv["unlock"]])):
                    units.append([(u"m", mv)])
        if not col["chips"]:
            units.append([(u"n", u"이 칸은 장면 없이 결말로 바로 이어집니다.")])
        for mv in col.get("movies", []):
            if not mv["after"] and (reveal or f12_fc_end_open([u"", u"", mv["unlock"]])):
                units.append([(u"m", mv)])
        total = sum([len(u) for u in units])
        per = max(1, -(-total // 4))
        grid = [[], [], [], []]
        ci = 0
        for rows in units:
            if len(grid[ci]) + len(rows) > per and len(grid[ci]) > 0 and ci < 3:
                ci += 1
            grid[ci].extend(rows)
        return grid

    def _f12_fc_persist_keep(k):
        return k.startswith("_seen") or k.startswith("_chosen") or k.startswith("f12_fc_") or k in ("_preferences", "_changed", "_version", "f12_bonus_open")

    def f12_fc_persist_snapshot():
        snap = {}
        for k, v in renpy.game.persistent.__dict__.items():
            if _f12_fc_persist_keep(k):
                continue
            try:
                snap[k] = _f12_fc_copy.deepcopy(v)
            except Exception:
                snap[k] = v
        return snap

    def f12_fc_persist_restore(snap):
        dd = renpy.game.persistent.__dict__
        for k in list(dd.keys()):
            if _f12_fc_persist_keep(k):
                continue
            if k in snap:
                dd[k] = snap[k]
            else:
                del dd[k]
        for k, v in snap.items():
            if k not in dd:
                dd[k] = v

    def _f12_fc_scope(colk):
        rv = {}
        for k in F12_FC_LANE_FLAGS.get(colk, u""):
            rv["flags_route_" + k] = True
        return rv

    class F12FCReplay(Action, DictEquality):
        """끝까지 읽은 장면 하나를 격리 Replay 로 다시 본다. 다시보기 중 차트에서 다른 장면을 고르면 이어서 그 장면을 연다."""
        def __init__(self, file, sid, colk):
            self.file = file
            self.sid = sid
            self.colk = colk

        def __call__(self):
            if not self.get_sensitive():
                return
            return f12_bonus_run_preview(self.play_scene)

        def play_scene(self):
            snap = f12_fc_persist_snapshot()
            nxt = (self.file, self.sid, self.colk)
            _F12FCState.pending = None
            try:
                while nxt is not None:
                    node = f12_fc_index().get((nxt[0], nxt[1]))
                    if node is None:
                        break
                    _F12FCState.target = (nxt[0], nxt[1])
                    _F12FCState.target_colk = nxt[2]
                    _F12FCState.pending = None
                    if config.enter_replay_transition:
                        renpy.transition(config.enter_replay_transition)
                    renpy.call_replay(node.name, _f12_fc_scope(nxt[2]))
                    nxt = _F12FCState.pending
                    f12_fc_persist_restore(snap)
                if config.exit_replay_transition:
                    renpy.transition(config.exit_replay_transition)
            finally:
                _F12FCState.target = None
                _F12FCState.target_colk = None
                _F12FCState.pending = None
                f12_fc_persist_restore(snap)

        def get_sensitive(self):
            return f12_fc_bonus_preview() or f12_fc_done(F12_FC_CHIPMAP.get((self.colk, self.file, self.sid)))

    class F12FCChain(Action, DictEquality):
        """다시보기 중 차트: 다음에 볼 장면을 정하고 지금 다시보기를 끝낸다."""
        def __init__(self, file, sid, colk):
            self.file = file
            self.sid = sid
            self.colk = colk

        def __call__(self):
            if not self.get_sensitive():
                return
            _F12FCState.pending = (self.file, self.sid, self.colk)
            renpy.end_replay()

        def get_sensitive(self):
            return bool(store._in_replay) and _F12FCState.target is not None and (f12_fc_bonus_preview() or f12_fc_done(F12_FC_CHIPMAP.get((self.colk, self.file, self.sid))))

    class F12FCSelected(Action, DictEquality):
        def __call__(self):
            return
        def get_selected(self):
            return True

    def _f12_fc_sync_tab():
        extra = renpy.get_screen("extra")
        tab = renpy.get_screen("f12_fc_extra_tab")
        if extra is not None and tab is None:
            renpy.show_screen("f12_fc_extra_tab")
        elif extra is None and tab is not None:
            renpy.hide_screen("f12_fc_extra_tab")

    if _f12_fc_sync_tab not in config.interact_callbacks:
        config.interact_callbacks.append(_f12_fc_sync_tab)


init 999 python:
    # 장면 표식: 지금 장면 기록 + 플로우 차트 다시보기는 다음 표식에서 끝낸다.
    _f12_fc_orig_set_info_scene = set_info_scene

    def set_info_scene(scene_id):
        global f12_fc_cur
        _f12_fc_orig_set_info_scene(scene_id)
        fb = None
        try:
            node = renpy.game.script.namemap.get(renpy.game.context().current)
            if node is not None:
                fb = _f12_fc_base(node.filename)
        except Exception:
            fb = None
        f12_fc_cur = (fb, scene_id)
        tgt = _F12FCState.target
        if tgt is not None and _in_replay and (fb, scene_id) != tgt:
            renpy.end_replay()

    # 메뉴: 이번 회차에 고른 선택지를 세이브 변수에 기록한다.
    if not hasattr(renpy.exports, "_f12_fc_orig_menu"):
        renpy.exports._f12_fc_orig_menu = renpy.exports.menu

    def _f12_fc_menu(items, set_expr, *args, **kwargs):
        rv = renpy.exports._f12_fc_orig_menu(items, set_expr, *args, **kwargs)
        try:
            if rv is not None and not renpy.store._in_replay:
                node = renpy.game.script.namemap.get(renpy.game.context().current)
                if isinstance(node, renpy.ast.Menu) and "scenario/" in (node.filename or "").replace("\\", "/"):
                    picks = getattr(renpy.store, "f12_fc_picks", None)
                    if picks is not None:
                        picks["%s:%d" % (_f12_fc_base(node.filename), node.linenumber)] = node.items[rv][0]
        except Exception:
            pass
        return rv

    renpy.exports.menu = _f12_fc_menu

    if "f12_fc_quick" not in config.overlay_screens:
        config.overlay_screens.append("f12_fc_quick")


# 빠른 메뉴(자동·건너뛰기…) 왼쪽 「플로우 차트」. 대사창이 있을 때만. 플로우 차트 다시보기 중이면 다시보기용 차트.
screen f12_fc_quick():
    zorder 100
    if (renpy.get_screen("say") is not None) and (not _windows_hidden) and (not main_menu):
        if not _in_replay:
            frame:
                style_prefix "quick"
                background None
                xpadding 0
                top_padding 20
                bottom_padding 10
                xpos 88
                yalign 1.0
                textbutton u"플로우 차트" action ShowMenu("f12_flowchart_ingame")
        elif _F12FCState.target is not None:
            frame:
                style_prefix "quick"
                background None
                xpadding 0
                top_padding 20
                bottom_padding 10
                xpos 88
                yalign 1.0
                textbutton u"플로우 차트" action ShowMenu("f12_flowchart_replay")


# 오프닝·엔딩 영상 재생 (f12_fc_play_movie 가 새 컨텍스트로 부른다)
label f12_fc_play_movie_label:
    scene black
    $ renpy.movie_cutscene(_F12FCState.movie)
    $ renpy.music.stop(channel="movie", fadeout=0)
    return


# 특전 화면 위에 얹는 세 번째 탭
screen f12_fc_extra_tab():
    zorder 250
    frame:
        style_prefix "extra_manager_mode"
        xpos 289
        ypos 60
        has hbox
        textbutton u"플로우 차트" action ShowMenu("f12_flowchart")


screen f12_flowchart():
    tag menu

    default sel = f12_fc_default_sel(u"extra")
    default fc_adj = ui.adjustment()

    python:
        fc_mode = u"extra"
        fc_reveal = f12_fc_revealed()
        fc_cols = F12_FC_COLS
        fc_cur = f12_fc_current(fc_mode)
        fc_cur_col = fc_cur[0] if fc_cur else None
        fc_states = [f12_fc_col_state(c) for c in fc_cols]
        fc_colored = {}
        fc_opened = {}
        for fc_i, fc_c in enumerate(fc_cols):
            fc_colored[fc_c["key"]] = f12_fc_col_colored(fc_c, fc_states[fc_i])
            fc_opened[fc_c["key"]] = fc_reveal or fc_colored[fc_c["key"]] or fc_i == fc_cur_col
        if not fc_opened[fc_cols[sel]["key"]]:
            fc_fallback = f12_fc_default_sel(fc_mode)
            if fc_fallback != sel:
                sel = fc_fallback
                f12_fc_scroll(fc_adj, sel)
        fc_selcol = fc_cols[sel]
        fc_ops = f12_fc_ribbon_ops(fc_opened, fc_reveal)
        fc_grid = f12_fc_grid(fc_selcol, fc_reveal, fc_mode, (fc_cur[1] if (fc_cur and fc_cur[0] == sel) else None), fc_opened)
        fc_legend = f12_fc_legend(fc_opened, fc_reveal)
        fc_sel_rd, fc_sel_total = fc_states[sel]
        fc_now_tag = u"다시보기 중" if fc_mode == u"replay" else u"진행 중"
        fc_weeks = []
        for fc_wn in range(1, 14):
            fc_wcols = [fc_j for fc_j, fc_cc in enumerate(fc_cols) if fc_cc["wn"] == fc_wn]
            fc_wopencols = [fc_j for fc_j in fc_wcols if fc_opened[fc_cols[fc_j]["key"]]]
            fc_wnow = fc_cur_col is not None and fc_cur_col in fc_wcols
            fc_wtarget = fc_cur_col if fc_wnow else (fc_wopencols or fc_wcols)[0]
            fc_wrd = bool([fc_j for fc_j in fc_wcols if fc_colored[fc_cols[fc_j]["key"]]])
            fc_weeks.append((fc_wn, bool(fc_wopencols), fc_wrd, fc_wnow, fc_wtarget))

    if main_menu:
        add "title_art"
    add "gui/right_click_bg.png"

    if fc_mode == u"extra":
        use menu_page_title(_("エクストラ"), (1.0, 0.00))
        frame:
            style_prefix "extra_manager_mode"
            has hbox
            textbutton _("ギャラリー") action ShowMenu("extra", "gallery")
            textbutton _("リプレイ") action ShowMenu("extra", "replay")
            textbutton u"플로우 차트" action F12FCSelected()
    else:
        add "gui/headline_bg.png" pos (968, 0)
        text u"플로우 차트" xanchor 1.0 yanchor 0.5 pos (1166, 61) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 32 color "#fff"

    # ---- 왼쪽: 주차 목록 (줄거리 화면의 장 목록과 같은 틀)
    frame:
        pos (40, 98)
        xysize (160, 560)
        background Frame("gui/frame.png", 4, 4)
        padding (0, 0)

        fixed:
            xysize (160, 560)
            for fc_wn, fc_wopen, fc_wrd, fc_wnow, fc_wtarget in fc_weeks:
                $ fc_won = fc_selcol["wn"] == fc_wn
                button:
                    pos (1, 20 + (fc_wn - 1) * 40)
                    xysize (158, 40)
                    background None
                    hover_background "#74040488"
                    selected_background "#4b4b4b88"
                    selected fc_won
                    sensitive fc_wopen
                    action [SetScreenVariable("sel", fc_wtarget), Function(f12_fc_scroll, fc_adj, fc_wtarget)]
                    text ((u"%d주차" % fc_wn) if fc_wopen else u"？？？") align (0.5, 0.5) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 16 color ("#fff" if fc_wopen else "#6e6e6e")
                    if fc_wnow:
                        text (u"다시보기" if fc_mode == u"replay" else u"지금") xanchor 1.0 yanchor 0.5 pos (150, 20) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 9 color F12_FC_GOLD

    # ---- 오른쪽: 리본 + 장면 목록
    frame:
        pos (215, 98)
        xysize (1025, 560)
        background Frame("gui/frame.png", 4, 4)
        padding (0, 0)

        fixed:
            xysize (1025, 560)

            text u"여신의 선정 — 선택이 어느 줄기로 이어지는지" pos (20, 12) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 15 color "#fff"
            if fc_reveal:
                text u"스포일러 주의: 모든 주차·장면·줄기 표시" xanchor 1.0 pos (818, 16) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#c0392b"
            button:
                pos (830, 8)
                xysize (175, 30)
                background Frame("gui/tab_idle.png", 4, 4)
                selected_background Frame("gui/tab_selected.png", 4, 4)
                hover_background Frame("gui/tab_hover.png", 4, 4)
                id "f12_fc_reveal_toggle"
                selected fc_reveal
                action Function(f12_fc_set_revealed, not fc_reveal)
                text (u"전체 개방 취소" if fc_reveal else u"플로우 차트 전체 개방") align (0.5, 0.5) font "gui/fonts/NotoSansCJKjp-Regular.otf" size 13 color (F12_FC_GOLD if fc_reveal else "#fff")

            if fc_mode == u"ingame":
                text u"금색 톱니: 끝까지 읽은 장면 · 금빛 줄: 지금 읽는 장면 · ▶ 이번 회차에 고른 선택지 (흐린 ▶: 깃발로 추정)" pos (20, 44) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            elif fc_mode == u"replay":
                text u"금색 톱니: 끝까지 읽은 장면 · 금빛 줄: 지금 다시 보는 장면" pos (20, 44) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            else:
                text u"금색 톱니: 끝까지 읽은 장면 · 회색: 아직 · 그림: 채색=읽음, 흑백=아직, 시계=미도달" pos (20, 44) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            hbox:
                xanchor 1.0
                pos (1005, 44)
                spacing 8
                for fc_lc, fc_lab in fc_legend:
                    add Solid(fc_lc, xsize=12, ysize=4) yoffset 7
                    text fc_lab font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"

            viewport:
                pos (12, 58)
                xysize (F12_FC_VIEW_W, 228)
                xadjustment fc_adj
                draggable True
                fixed:
                    xsize (len(fc_cols) * F12_FC_CW + 24)
                    ysize 228
                    for op in fc_ops:
                        if op[0] == u"r":
                            add Solid(op[5], xsize=op[3], ysize=op[4]) pos (op[1], op[2])
                        else:
                            frame:
                                xanchor 0.5
                                yanchor 0.5
                                pos (op[1], op[2])
                                background "#080808eb"
                                xpadding 4
                                ypadding 0
                                text op[3] font "gui/fonts/NotoSansCJKjp-Regular.otf" size op[5] color op[4]
                    for fc_i, fc_c in enumerate(fc_cols):
                        $ fc_x = 12 + fc_i * F12_FC_CW
                        $ fc_open = fc_opened[fc_c["key"]]
                        $ fc_rd = fc_colored[fc_c["key"]]
                        $ fc_lane_col = f12_fc_color(fc_c["colk"], fc_opened, fc_reveal)
                        if fc_i == sel:
                            add Solid(F12_FC_GOLD, xsize=F12_FC_TW + 6, ysize=F12_FC_TH + 6) pos (fc_x - 3, F12_FC_TY - 3)
                            add Solid("#000", xsize=F12_FC_TW + 2, ysize=F12_FC_TH + 2) pos (fc_x - 1, F12_FC_TY - 1)
                        elif fc_open and fc_c["colk"] != u"S":
                            add Solid(fc_lane_col, xsize=F12_FC_TW + 2, ysize=F12_FC_TH + 2) pos (fc_x - 1, F12_FC_TY - 1)
                        button:
                            pos (fc_x, F12_FC_TY)
                            xysize (F12_FC_TW, F12_FC_TH)
                            background f12_fc_thumb(fc_c, fc_open, fc_rd, fc_reveal)
                            action [SetScreenVariable("sel", fc_i), Function(f12_fc_scroll, fc_adj, fc_i)]
                            sensitive fc_open
                            add Solid("#000000af", xsize=F12_FC_TW, ysize=20) pos (0, F12_FC_TH - 20)
                            text (fc_c["short"] if fc_open else u"？？？") xanchor 0.5 yanchor 0.5 pos (F12_FC_TW // 2, F12_FC_TH - 10) font "gui/fonts/NotoSerifCJKjp-Medium.otf" size 12 color ("#fff" if fc_rd else ("#bdbdbd" if fc_open else "#6e6e6e"))
                            if fc_i == fc_cur_col:
                                frame:
                                    pos (0, 0)
                                    background Solid(F12_FC_GOLD)
                                    xpadding 5
                                    ypadding 1
                                    text (u"다시보기" if fc_mode == u"replay" else u"지금") font "gui/fonts/NotoSansCJKjp-Medium.otf" size 10 color "#000"
                        if fc_open and fc_c["sub"]:
                            text fc_c["sub"][:12] xanchor 0.5 yanchor 0.5 pos (fc_x + F12_FC_TW // 2, F12_FC_TY + F12_FC_TH + 9) font "gui/fonts/NotoSansCJKjp-Light.otf" size 9 color ("#bdbdbd" if fc_rd else "#8a8a8a")
                        for fc_ei, fc_end in enumerate([fc_e for fc_e in fc_c["ends"] if fc_reveal or (fc_open and f12_fc_end_open(fc_e))]):
                            $ fc_ey = F12_FC_TY + F12_FC_TH + 20 + fc_ei * 18
                            $ fc_eok = f12_fc_end_open(fc_end)
                            $ fc_eopen = fc_reveal or fc_eok
                            $ fc_eplay = bool(fc_end[3]) and fc_eok
                            $ fc_ecol = F12_FC_LANE_COLOR[fc_end[0]] if fc_eopen else u"#5a5a5a"
                            button:
                                pos (fc_x + 10, fc_ey)
                                xysize (F12_FC_TW - 20, 15)
                                background Solid(fc_ecol)
                                hover_background Solid(u"#f0d890")
                                padding (0, 0)
                                action Function(f12_fc_play_movie, fc_end[3])
                                sensitive fc_eplay
                                add Solid("#000000c8", xsize=F12_FC_TW - 22, ysize=13) pos (1, 1)
                                text ((u"▶ " if fc_eplay else u"") + (fc_end[4] if fc_eok else fc_end[1])) align (0.5, 0.5) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 9 color (F12_FC_LANE_COLOR[fc_end[0]] if fc_eopen else "#6e6e6e")

            textbutton u"◀" pos (0, 165) xysize (14, 30) background None text_size 13 text_color "#bbb" action Function(f12_fc_scroll_by, fc_adj, -F12_FC_CW)
            textbutton u"▶" pos (1011, 165) xysize (14, 30) background None text_size 13 text_color "#bbb" action Function(f12_fc_scroll_by, fc_adj, F12_FC_CW)

            text (fc_selcol["short"] if fc_opened[fc_selcol["key"]] else u"？？？") pos (20, 290) font "gui/fonts/NotoSerifCJKjp-Medium.otf" size 20 color "#fff"
            text (fc_selcol["sub"] if fc_opened[fc_selcol["key"]] else u"") pos (20 + len(fc_selcol["short"]) * 21 + 12, 298) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 14 color "#cfcfcf"
            text (u"%d / %d 끝까지 읽음" % (fc_sel_rd, fc_sel_total)) xanchor 1.0 pos (1005, 300) font "gui/fonts/NotoSansCJKjp-Light.otf" size 11 color (F12_FC_GOLD if (fc_sel_total and fc_sel_rd == fc_sel_total) else "#9a9a9a")
            for fc_wn, fc_wopen, fc_wrd, fc_wnow, fc_wtarget in fc_weeks:
                $ fc_won = fc_selcol["wn"] == fc_wn
                button:
                    pos (340 + (fc_wn - 1) * 36, 287)
                    xysize (32, 32)
                    background None
                    hover_background "gui/num_hover.png"
                    selected_background F12_FC_NUM_SEL
                    selected fc_won
                    sensitive fc_wopen
                    action [SetScreenVariable("sel", fc_wtarget), Function(f12_fc_scroll, fc_adj, fc_wtarget)]
                    text (F12_FC_ROMAN[fc_wn - 1] if fc_wopen else u"·") align (0.5, 0.5) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 14 color ("#fff" if (fc_wrd or fc_won) else ("#9a9a9a" if fc_wopen else "#5a5a5a"))
            add im.Scale("gui/right_click_fg.png", 985, 2) pos (20, 322)

            for fc_ci in range(4):
                for fc_ri, fc_row in enumerate(fc_grid[fc_ci]):
                    $ fc_rx = 24 + fc_ci * 246
                    $ fc_ry = 332 + fc_ri * 23
                    if fc_row[0] == u"c":
                        $ fc_ch = fc_row[1]
                        $ fc_act = F12FCChain(fc_ch["file"], fc_ch["sid"], fc_selcol["colk"]) if fc_mode == u"replay" else F12FCReplay(fc_ch["file"], fc_ch["sid"], fc_selcol["colk"])
                        button:
                            pos (fc_rx - 8, fc_ry - 1)
                            xysize (238, 22)
                            background (Solid("#d9b65c40") if fc_row[3] else None)
                            hover_background "#74040499"
                            action fc_act
                            add (F12_FC_GEAR_READ if fc_row[2] else F12_FC_GEAR_UNREAD) pos (8, 5)
                            text (fc_ch["name"][:14] if (fc_row[2] or fc_reveal or fc_row[3]) else u"？？？") xpos 28 ypos 11 yanchor 0.5 font "gui/fonts/NotoSerifCJKjp-Light.otf" size 13 color ("#fff" if (fc_row[2] or fc_row[3]) else "#8a8a8a")
                            if fc_row[3]:
                                text fc_now_tag xanchor 1.0 yanchor 0.5 pos (232, 11) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 10 color F12_FC_GOLD
                            else:
                                text fc_ch["sid"] xanchor 1.0 yanchor 0.5 pos (232, 11) font "gui/fonts/NotoSansCJKjp-Light.otf" size 9 color "#6a6a6a"
                    elif fc_row[0] == u"m":
                        $ fc_mv = fc_row[1]
                        $ fc_mok = f12_fc_end_open([u"", u"", fc_mv["unlock"]])
                        button:
                            pos (fc_rx - 8, fc_ry - 1)
                            xysize (238, 22)
                            background None
                            hover_background "#74040499"
                            action Function(f12_fc_play_movie, fc_mv["path"])
                            sensitive fc_mok
                            frame:
                                pos (8, 4)
                                xysize (14, 14)
                                background Solid(F12_FC_GOLD if fc_mok else u"#5a5a5a")
                                padding (0, 0)
                                text u"▶" align (0.5, 0.5) font "gui/fonts/NotoSansCJKjp-Regular.otf" size 8 color "#000"
                            text (fc_mv["label_open"] if fc_mok else fc_mv["label"]) xpos 28 ypos 11 yanchor 0.5 font "gui/fonts/NotoSerifCJKjp-Light.otf" size 13 color (F12_FC_GOLD if fc_mok else "#8a8a8a")
                            text u"영상" xanchor 1.0 yanchor 0.5 pos (232, 11) font "gui/fonts/NotoSansCJKjp-Light.otf" size 9 color "#6a6a6a"
                    elif fc_row[0] == u"n":
                        text fc_row[1] xpos fc_rx ypos (fc_ry + 10) yanchor 0.5 font "gui/fonts/NotoSansCJKjp-Light.otf" size 12 color "#9a9a9a"
                    else:
                        $ fc_mark = u"▶ " if fc_row[7] else u""
                        $ fc_ocol = ((u"#9c8448" if fc_row[8] else F12_FC_GOLD) if fc_row[7] else ("#d0d0d0" if fc_row[6] else "#8a8a8a"))
                        text (u"└ " + ((fc_mark + fc_row[1][:13]) if fc_row[5] else u"？？？")) xpos (fc_rx + 20) ypos (fc_ry + 10) yanchor 0.5 font "gui/fonts/NotoSansCJKjp-Light.otf" size 12 color fc_ocol
                        if fc_row[5] and fc_row[3]:
                            text fc_row[3] xanchor 1.0 yanchor 0.5 pos (fc_rx + 224, fc_ry + 10) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 11 color fc_row[4]
                        elif fc_row[5] and fc_row[2]:
                            text (u"호감도 " + fc_row[2]) xanchor 1.0 yanchor 0.5 pos (fc_rx + 224, fc_ry + 10) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"

            if fc_mode == u"replay":
                text u"끝까지 읽은 장면을 누르면 지금 다시보기를 끝내고 그 장면으로 넘어갑니다. ▶ 표시는 오프닝·엔딩 영상입니다." pos (20, 540) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            else:
                text u"끝까지 읽은 장면을 누르면 그 장면만 다시 봅니다. ▶ 표시는 오프닝·엔딩 영상. 진행·플래그·세이브에는 영향이 없습니다." pos (20, 540) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"

    if fc_mode == u"replay":
        textbutton u"다시보기 종료" style "menu_navigation_button" text_style "menu_navigation_button_text" pos (972, 670) action EndReplay(False)

    use menu_navigation(config.menu_navigation_align)

    on "show" action Function(f12_fc_scroll, fc_adj, sel)

    # 마우스 휠: 화면 어디서든 리본을 좌우로 한 칸씩 (올리면 왼쪽, 내리면 오른쪽)
    key "mousedown_4" action Function(f12_fc_scroll_by, fc_adj, -F12_FC_CW)
    key "mousedown_5" action Function(f12_fc_scroll_by, fc_adj, F12_FC_CW)


screen f12_flowchart_ingame():
    tag menu

    default sel = f12_fc_default_sel(u"ingame")
    default fc_adj = ui.adjustment()

    python:
        fc_mode = u"ingame"
        fc_reveal = f12_fc_revealed()
        fc_cols = F12_FC_COLS
        fc_cur = f12_fc_current(fc_mode)
        fc_cur_col = fc_cur[0] if fc_cur else None
        fc_states = [f12_fc_col_state(c) for c in fc_cols]
        fc_colored = {}
        fc_opened = {}
        for fc_i, fc_c in enumerate(fc_cols):
            fc_colored[fc_c["key"]] = f12_fc_col_colored(fc_c, fc_states[fc_i])
            fc_opened[fc_c["key"]] = fc_reveal or fc_colored[fc_c["key"]] or fc_i == fc_cur_col
        if not fc_opened[fc_cols[sel]["key"]]:
            fc_fallback = f12_fc_default_sel(fc_mode)
            if fc_fallback != sel:
                sel = fc_fallback
                f12_fc_scroll(fc_adj, sel)
        fc_selcol = fc_cols[sel]
        fc_ops = f12_fc_ribbon_ops(fc_opened, fc_reveal)
        fc_grid = f12_fc_grid(fc_selcol, fc_reveal, fc_mode, (fc_cur[1] if (fc_cur and fc_cur[0] == sel) else None), fc_opened)
        fc_legend = f12_fc_legend(fc_opened, fc_reveal)
        fc_sel_rd, fc_sel_total = fc_states[sel]
        fc_now_tag = u"다시보기 중" if fc_mode == u"replay" else u"진행 중"
        fc_weeks = []
        for fc_wn in range(1, 14):
            fc_wcols = [fc_j for fc_j, fc_cc in enumerate(fc_cols) if fc_cc["wn"] == fc_wn]
            fc_wopencols = [fc_j for fc_j in fc_wcols if fc_opened[fc_cols[fc_j]["key"]]]
            fc_wnow = fc_cur_col is not None and fc_cur_col in fc_wcols
            fc_wtarget = fc_cur_col if fc_wnow else (fc_wopencols or fc_wcols)[0]
            fc_wrd = bool([fc_j for fc_j in fc_wcols if fc_colored[fc_cols[fc_j]["key"]]])
            fc_weeks.append((fc_wn, bool(fc_wopencols), fc_wrd, fc_wnow, fc_wtarget))

    if main_menu:
        add "title_art"
    add "gui/right_click_bg.png"

    if fc_mode == u"extra":
        use menu_page_title(_("エクストラ"), (1.0, 0.00))
        frame:
            style_prefix "extra_manager_mode"
            has hbox
            textbutton _("ギャラリー") action ShowMenu("extra", "gallery")
            textbutton _("リプレイ") action ShowMenu("extra", "replay")
            textbutton u"플로우 차트" action F12FCSelected()
    else:
        add "gui/headline_bg.png" pos (968, 0)
        text u"플로우 차트" xanchor 1.0 yanchor 0.5 pos (1166, 61) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 32 color "#fff"

    # ---- 왼쪽: 주차 목록 (줄거리 화면의 장 목록과 같은 틀)
    frame:
        pos (40, 98)
        xysize (160, 560)
        background Frame("gui/frame.png", 4, 4)
        padding (0, 0)

        fixed:
            xysize (160, 560)
            for fc_wn, fc_wopen, fc_wrd, fc_wnow, fc_wtarget in fc_weeks:
                $ fc_won = fc_selcol["wn"] == fc_wn
                button:
                    pos (1, 20 + (fc_wn - 1) * 40)
                    xysize (158, 40)
                    background None
                    hover_background "#74040488"
                    selected_background "#4b4b4b88"
                    selected fc_won
                    sensitive fc_wopen
                    action [SetScreenVariable("sel", fc_wtarget), Function(f12_fc_scroll, fc_adj, fc_wtarget)]
                    text ((u"%d주차" % fc_wn) if fc_wopen else u"？？？") align (0.5, 0.5) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 16 color ("#fff" if fc_wopen else "#6e6e6e")
                    if fc_wnow:
                        text (u"다시보기" if fc_mode == u"replay" else u"지금") xanchor 1.0 yanchor 0.5 pos (150, 20) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 9 color F12_FC_GOLD

    # ---- 오른쪽: 리본 + 장면 목록
    frame:
        pos (215, 98)
        xysize (1025, 560)
        background Frame("gui/frame.png", 4, 4)
        padding (0, 0)

        fixed:
            xysize (1025, 560)

            text u"여신의 선정 — 선택이 어느 줄기로 이어지는지" pos (20, 12) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 15 color "#fff"
            if fc_reveal:
                text u"스포일러 주의: 모든 주차·장면·줄기 표시" xanchor 1.0 pos (818, 16) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#c0392b"
            button:
                pos (830, 8)
                xysize (175, 30)
                background Frame("gui/tab_idle.png", 4, 4)
                selected_background Frame("gui/tab_selected.png", 4, 4)
                hover_background Frame("gui/tab_hover.png", 4, 4)
                id "f12_fc_reveal_toggle"
                selected fc_reveal
                action Function(f12_fc_set_revealed, not fc_reveal)
                text (u"전체 개방 취소" if fc_reveal else u"플로우 차트 전체 개방") align (0.5, 0.5) font "gui/fonts/NotoSansCJKjp-Regular.otf" size 13 color (F12_FC_GOLD if fc_reveal else "#fff")

            if fc_mode == u"ingame":
                text u"금색 톱니: 끝까지 읽은 장면 · 금빛 줄: 지금 읽는 장면 · ▶ 이번 회차에 고른 선택지 (흐린 ▶: 깃발로 추정)" pos (20, 44) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            elif fc_mode == u"replay":
                text u"금색 톱니: 끝까지 읽은 장면 · 금빛 줄: 지금 다시 보는 장면" pos (20, 44) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            else:
                text u"금색 톱니: 끝까지 읽은 장면 · 회색: 아직 · 그림: 채색=읽음, 흑백=아직, 시계=미도달" pos (20, 44) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            hbox:
                xanchor 1.0
                pos (1005, 44)
                spacing 8
                for fc_lc, fc_lab in fc_legend:
                    add Solid(fc_lc, xsize=12, ysize=4) yoffset 7
                    text fc_lab font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"

            viewport:
                pos (12, 58)
                xysize (F12_FC_VIEW_W, 228)
                xadjustment fc_adj
                draggable True
                fixed:
                    xsize (len(fc_cols) * F12_FC_CW + 24)
                    ysize 228
                    for op in fc_ops:
                        if op[0] == u"r":
                            add Solid(op[5], xsize=op[3], ysize=op[4]) pos (op[1], op[2])
                        else:
                            frame:
                                xanchor 0.5
                                yanchor 0.5
                                pos (op[1], op[2])
                                background "#080808eb"
                                xpadding 4
                                ypadding 0
                                text op[3] font "gui/fonts/NotoSansCJKjp-Regular.otf" size op[5] color op[4]
                    for fc_i, fc_c in enumerate(fc_cols):
                        $ fc_x = 12 + fc_i * F12_FC_CW
                        $ fc_open = fc_opened[fc_c["key"]]
                        $ fc_rd = fc_colored[fc_c["key"]]
                        $ fc_lane_col = f12_fc_color(fc_c["colk"], fc_opened, fc_reveal)
                        if fc_i == sel:
                            add Solid(F12_FC_GOLD, xsize=F12_FC_TW + 6, ysize=F12_FC_TH + 6) pos (fc_x - 3, F12_FC_TY - 3)
                            add Solid("#000", xsize=F12_FC_TW + 2, ysize=F12_FC_TH + 2) pos (fc_x - 1, F12_FC_TY - 1)
                        elif fc_open and fc_c["colk"] != u"S":
                            add Solid(fc_lane_col, xsize=F12_FC_TW + 2, ysize=F12_FC_TH + 2) pos (fc_x - 1, F12_FC_TY - 1)
                        button:
                            pos (fc_x, F12_FC_TY)
                            xysize (F12_FC_TW, F12_FC_TH)
                            background f12_fc_thumb(fc_c, fc_open, fc_rd, fc_reveal)
                            action [SetScreenVariable("sel", fc_i), Function(f12_fc_scroll, fc_adj, fc_i)]
                            sensitive fc_open
                            add Solid("#000000af", xsize=F12_FC_TW, ysize=20) pos (0, F12_FC_TH - 20)
                            text (fc_c["short"] if fc_open else u"？？？") xanchor 0.5 yanchor 0.5 pos (F12_FC_TW // 2, F12_FC_TH - 10) font "gui/fonts/NotoSerifCJKjp-Medium.otf" size 12 color ("#fff" if fc_rd else ("#bdbdbd" if fc_open else "#6e6e6e"))
                            if fc_i == fc_cur_col:
                                frame:
                                    pos (0, 0)
                                    background Solid(F12_FC_GOLD)
                                    xpadding 5
                                    ypadding 1
                                    text (u"다시보기" if fc_mode == u"replay" else u"지금") font "gui/fonts/NotoSansCJKjp-Medium.otf" size 10 color "#000"
                        if fc_open and fc_c["sub"]:
                            text fc_c["sub"][:12] xanchor 0.5 yanchor 0.5 pos (fc_x + F12_FC_TW // 2, F12_FC_TY + F12_FC_TH + 9) font "gui/fonts/NotoSansCJKjp-Light.otf" size 9 color ("#bdbdbd" if fc_rd else "#8a8a8a")
                        for fc_ei, fc_end in enumerate([fc_e for fc_e in fc_c["ends"] if fc_reveal or (fc_open and f12_fc_end_open(fc_e))]):
                            $ fc_ey = F12_FC_TY + F12_FC_TH + 20 + fc_ei * 18
                            $ fc_eok = f12_fc_end_open(fc_end)
                            $ fc_eopen = fc_reveal or fc_eok
                            $ fc_eplay = bool(fc_end[3]) and fc_eok
                            $ fc_ecol = F12_FC_LANE_COLOR[fc_end[0]] if fc_eopen else u"#5a5a5a"
                            button:
                                pos (fc_x + 10, fc_ey)
                                xysize (F12_FC_TW - 20, 15)
                                background Solid(fc_ecol)
                                hover_background Solid(u"#f0d890")
                                padding (0, 0)
                                action Function(f12_fc_play_movie, fc_end[3])
                                sensitive fc_eplay
                                add Solid("#000000c8", xsize=F12_FC_TW - 22, ysize=13) pos (1, 1)
                                text ((u"▶ " if fc_eplay else u"") + (fc_end[4] if fc_eok else fc_end[1])) align (0.5, 0.5) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 9 color (F12_FC_LANE_COLOR[fc_end[0]] if fc_eopen else "#6e6e6e")

            textbutton u"◀" pos (0, 165) xysize (14, 30) background None text_size 13 text_color "#bbb" action Function(f12_fc_scroll_by, fc_adj, -F12_FC_CW)
            textbutton u"▶" pos (1011, 165) xysize (14, 30) background None text_size 13 text_color "#bbb" action Function(f12_fc_scroll_by, fc_adj, F12_FC_CW)

            text (fc_selcol["short"] if fc_opened[fc_selcol["key"]] else u"？？？") pos (20, 290) font "gui/fonts/NotoSerifCJKjp-Medium.otf" size 20 color "#fff"
            text (fc_selcol["sub"] if fc_opened[fc_selcol["key"]] else u"") pos (20 + len(fc_selcol["short"]) * 21 + 12, 298) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 14 color "#cfcfcf"
            text (u"%d / %d 끝까지 읽음" % (fc_sel_rd, fc_sel_total)) xanchor 1.0 pos (1005, 300) font "gui/fonts/NotoSansCJKjp-Light.otf" size 11 color (F12_FC_GOLD if (fc_sel_total and fc_sel_rd == fc_sel_total) else "#9a9a9a")
            for fc_wn, fc_wopen, fc_wrd, fc_wnow, fc_wtarget in fc_weeks:
                $ fc_won = fc_selcol["wn"] == fc_wn
                button:
                    pos (340 + (fc_wn - 1) * 36, 287)
                    xysize (32, 32)
                    background None
                    hover_background "gui/num_hover.png"
                    selected_background F12_FC_NUM_SEL
                    selected fc_won
                    sensitive fc_wopen
                    action [SetScreenVariable("sel", fc_wtarget), Function(f12_fc_scroll, fc_adj, fc_wtarget)]
                    text (F12_FC_ROMAN[fc_wn - 1] if fc_wopen else u"·") align (0.5, 0.5) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 14 color ("#fff" if (fc_wrd or fc_won) else ("#9a9a9a" if fc_wopen else "#5a5a5a"))
            add im.Scale("gui/right_click_fg.png", 985, 2) pos (20, 322)

            for fc_ci in range(4):
                for fc_ri, fc_row in enumerate(fc_grid[fc_ci]):
                    $ fc_rx = 24 + fc_ci * 246
                    $ fc_ry = 332 + fc_ri * 23
                    if fc_row[0] == u"c":
                        $ fc_ch = fc_row[1]
                        $ fc_act = F12FCChain(fc_ch["file"], fc_ch["sid"], fc_selcol["colk"]) if fc_mode == u"replay" else F12FCReplay(fc_ch["file"], fc_ch["sid"], fc_selcol["colk"])
                        button:
                            pos (fc_rx - 8, fc_ry - 1)
                            xysize (238, 22)
                            background (Solid("#d9b65c40") if fc_row[3] else None)
                            hover_background "#74040499"
                            action fc_act
                            add (F12_FC_GEAR_READ if fc_row[2] else F12_FC_GEAR_UNREAD) pos (8, 5)
                            text (fc_ch["name"][:14] if (fc_row[2] or fc_reveal or fc_row[3]) else u"？？？") xpos 28 ypos 11 yanchor 0.5 font "gui/fonts/NotoSerifCJKjp-Light.otf" size 13 color ("#fff" if (fc_row[2] or fc_row[3]) else "#8a8a8a")
                            if fc_row[3]:
                                text fc_now_tag xanchor 1.0 yanchor 0.5 pos (232, 11) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 10 color F12_FC_GOLD
                            else:
                                text fc_ch["sid"] xanchor 1.0 yanchor 0.5 pos (232, 11) font "gui/fonts/NotoSansCJKjp-Light.otf" size 9 color "#6a6a6a"
                    elif fc_row[0] == u"m":
                        $ fc_mv = fc_row[1]
                        $ fc_mok = f12_fc_end_open([u"", u"", fc_mv["unlock"]])
                        button:
                            pos (fc_rx - 8, fc_ry - 1)
                            xysize (238, 22)
                            background None
                            hover_background "#74040499"
                            action Function(f12_fc_play_movie, fc_mv["path"])
                            sensitive fc_mok
                            frame:
                                pos (8, 4)
                                xysize (14, 14)
                                background Solid(F12_FC_GOLD if fc_mok else u"#5a5a5a")
                                padding (0, 0)
                                text u"▶" align (0.5, 0.5) font "gui/fonts/NotoSansCJKjp-Regular.otf" size 8 color "#000"
                            text (fc_mv["label_open"] if fc_mok else fc_mv["label"]) xpos 28 ypos 11 yanchor 0.5 font "gui/fonts/NotoSerifCJKjp-Light.otf" size 13 color (F12_FC_GOLD if fc_mok else "#8a8a8a")
                            text u"영상" xanchor 1.0 yanchor 0.5 pos (232, 11) font "gui/fonts/NotoSansCJKjp-Light.otf" size 9 color "#6a6a6a"
                    elif fc_row[0] == u"n":
                        text fc_row[1] xpos fc_rx ypos (fc_ry + 10) yanchor 0.5 font "gui/fonts/NotoSansCJKjp-Light.otf" size 12 color "#9a9a9a"
                    else:
                        $ fc_mark = u"▶ " if fc_row[7] else u""
                        $ fc_ocol = ((u"#9c8448" if fc_row[8] else F12_FC_GOLD) if fc_row[7] else ("#d0d0d0" if fc_row[6] else "#8a8a8a"))
                        text (u"└ " + ((fc_mark + fc_row[1][:13]) if fc_row[5] else u"？？？")) xpos (fc_rx + 20) ypos (fc_ry + 10) yanchor 0.5 font "gui/fonts/NotoSansCJKjp-Light.otf" size 12 color fc_ocol
                        if fc_row[5] and fc_row[3]:
                            text fc_row[3] xanchor 1.0 yanchor 0.5 pos (fc_rx + 224, fc_ry + 10) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 11 color fc_row[4]
                        elif fc_row[5] and fc_row[2]:
                            text (u"호감도 " + fc_row[2]) xanchor 1.0 yanchor 0.5 pos (fc_rx + 224, fc_ry + 10) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"

            if fc_mode == u"replay":
                text u"끝까지 읽은 장면을 누르면 지금 다시보기를 끝내고 그 장면으로 넘어갑니다. ▶ 표시는 오프닝·엔딩 영상입니다." pos (20, 540) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            else:
                text u"끝까지 읽은 장면을 누르면 그 장면만 다시 봅니다. ▶ 표시는 오프닝·엔딩 영상. 진행·플래그·세이브에는 영향이 없습니다." pos (20, 540) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"

    if fc_mode == u"replay":
        textbutton u"다시보기 종료" style "menu_navigation_button" text_style "menu_navigation_button_text" pos (972, 670) action EndReplay(False)

    use menu_navigation(config.menu_navigation_align)

    on "show" action Function(f12_fc_scroll, fc_adj, sel)

    # 마우스 휠: 화면 어디서든 리본을 좌우로 한 칸씩 (올리면 왼쪽, 내리면 오른쪽)
    key "mousedown_4" action Function(f12_fc_scroll_by, fc_adj, -F12_FC_CW)
    key "mousedown_5" action Function(f12_fc_scroll_by, fc_adj, F12_FC_CW)


screen f12_flowchart_replay():
    tag menu

    default sel = f12_fc_default_sel(u"replay")
    default fc_adj = ui.adjustment()

    python:
        fc_mode = u"replay"
        fc_reveal = f12_fc_revealed()
        fc_cols = F12_FC_COLS
        fc_cur = f12_fc_current(fc_mode)
        fc_cur_col = fc_cur[0] if fc_cur else None
        fc_states = [f12_fc_col_state(c) for c in fc_cols]
        fc_colored = {}
        fc_opened = {}
        for fc_i, fc_c in enumerate(fc_cols):
            fc_colored[fc_c["key"]] = f12_fc_col_colored(fc_c, fc_states[fc_i])
            fc_opened[fc_c["key"]] = fc_reveal or fc_colored[fc_c["key"]] or fc_i == fc_cur_col
        if not fc_opened[fc_cols[sel]["key"]]:
            fc_fallback = f12_fc_default_sel(fc_mode)
            if fc_fallback != sel:
                sel = fc_fallback
                f12_fc_scroll(fc_adj, sel)
        fc_selcol = fc_cols[sel]
        fc_ops = f12_fc_ribbon_ops(fc_opened, fc_reveal)
        fc_grid = f12_fc_grid(fc_selcol, fc_reveal, fc_mode, (fc_cur[1] if (fc_cur and fc_cur[0] == sel) else None), fc_opened)
        fc_legend = f12_fc_legend(fc_opened, fc_reveal)
        fc_sel_rd, fc_sel_total = fc_states[sel]
        fc_now_tag = u"다시보기 중" if fc_mode == u"replay" else u"진행 중"
        fc_weeks = []
        for fc_wn in range(1, 14):
            fc_wcols = [fc_j for fc_j, fc_cc in enumerate(fc_cols) if fc_cc["wn"] == fc_wn]
            fc_wopencols = [fc_j for fc_j in fc_wcols if fc_opened[fc_cols[fc_j]["key"]]]
            fc_wnow = fc_cur_col is not None and fc_cur_col in fc_wcols
            fc_wtarget = fc_cur_col if fc_wnow else (fc_wopencols or fc_wcols)[0]
            fc_wrd = bool([fc_j for fc_j in fc_wcols if fc_colored[fc_cols[fc_j]["key"]]])
            fc_weeks.append((fc_wn, bool(fc_wopencols), fc_wrd, fc_wnow, fc_wtarget))

    if main_menu:
        add "title_art"
    add "gui/right_click_bg.png"

    if fc_mode == u"extra":
        use menu_page_title(_("エクストラ"), (1.0, 0.00))
        frame:
            style_prefix "extra_manager_mode"
            has hbox
            textbutton _("ギャラリー") action ShowMenu("extra", "gallery")
            textbutton _("リプレイ") action ShowMenu("extra", "replay")
            textbutton u"플로우 차트" action F12FCSelected()
    else:
        add "gui/headline_bg.png" pos (968, 0)
        text u"플로우 차트" xanchor 1.0 yanchor 0.5 pos (1166, 61) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 32 color "#fff"

    # ---- 왼쪽: 주차 목록 (줄거리 화면의 장 목록과 같은 틀)
    frame:
        pos (40, 98)
        xysize (160, 560)
        background Frame("gui/frame.png", 4, 4)
        padding (0, 0)

        fixed:
            xysize (160, 560)
            for fc_wn, fc_wopen, fc_wrd, fc_wnow, fc_wtarget in fc_weeks:
                $ fc_won = fc_selcol["wn"] == fc_wn
                button:
                    pos (1, 20 + (fc_wn - 1) * 40)
                    xysize (158, 40)
                    background None
                    hover_background "#74040488"
                    selected_background "#4b4b4b88"
                    selected fc_won
                    sensitive fc_wopen
                    action [SetScreenVariable("sel", fc_wtarget), Function(f12_fc_scroll, fc_adj, fc_wtarget)]
                    text ((u"%d주차" % fc_wn) if fc_wopen else u"？？？") align (0.5, 0.5) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 16 color ("#fff" if fc_wopen else "#6e6e6e")
                    if fc_wnow:
                        text (u"다시보기" if fc_mode == u"replay" else u"지금") xanchor 1.0 yanchor 0.5 pos (150, 20) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 9 color F12_FC_GOLD

    # ---- 오른쪽: 리본 + 장면 목록
    frame:
        pos (215, 98)
        xysize (1025, 560)
        background Frame("gui/frame.png", 4, 4)
        padding (0, 0)

        fixed:
            xysize (1025, 560)

            text u"여신의 선정 — 선택이 어느 줄기로 이어지는지" pos (20, 12) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 15 color "#fff"
            if fc_reveal:
                text u"스포일러 주의: 모든 주차·장면·줄기 표시" xanchor 1.0 pos (818, 16) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#c0392b"
            button:
                pos (830, 8)
                xysize (175, 30)
                background Frame("gui/tab_idle.png", 4, 4)
                selected_background Frame("gui/tab_selected.png", 4, 4)
                hover_background Frame("gui/tab_hover.png", 4, 4)
                id "f12_fc_reveal_toggle"
                selected fc_reveal
                action Function(f12_fc_set_revealed, not fc_reveal)
                text (u"전체 개방 취소" if fc_reveal else u"플로우 차트 전체 개방") align (0.5, 0.5) font "gui/fonts/NotoSansCJKjp-Regular.otf" size 13 color (F12_FC_GOLD if fc_reveal else "#fff")

            if fc_mode == u"ingame":
                text u"금색 톱니: 끝까지 읽은 장면 · 금빛 줄: 지금 읽는 장면 · ▶ 이번 회차에 고른 선택지 (흐린 ▶: 깃발로 추정)" pos (20, 44) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            elif fc_mode == u"replay":
                text u"금색 톱니: 끝까지 읽은 장면 · 금빛 줄: 지금 다시 보는 장면" pos (20, 44) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            else:
                text u"금색 톱니: 끝까지 읽은 장면 · 회색: 아직 · 그림: 채색=읽음, 흑백=아직, 시계=미도달" pos (20, 44) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            hbox:
                xanchor 1.0
                pos (1005, 44)
                spacing 8
                for fc_lc, fc_lab in fc_legend:
                    add Solid(fc_lc, xsize=12, ysize=4) yoffset 7
                    text fc_lab font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"

            viewport:
                pos (12, 58)
                xysize (F12_FC_VIEW_W, 228)
                xadjustment fc_adj
                draggable True
                fixed:
                    xsize (len(fc_cols) * F12_FC_CW + 24)
                    ysize 228
                    for op in fc_ops:
                        if op[0] == u"r":
                            add Solid(op[5], xsize=op[3], ysize=op[4]) pos (op[1], op[2])
                        else:
                            frame:
                                xanchor 0.5
                                yanchor 0.5
                                pos (op[1], op[2])
                                background "#080808eb"
                                xpadding 4
                                ypadding 0
                                text op[3] font "gui/fonts/NotoSansCJKjp-Regular.otf" size op[5] color op[4]
                    for fc_i, fc_c in enumerate(fc_cols):
                        $ fc_x = 12 + fc_i * F12_FC_CW
                        $ fc_open = fc_opened[fc_c["key"]]
                        $ fc_rd = fc_colored[fc_c["key"]]
                        $ fc_lane_col = f12_fc_color(fc_c["colk"], fc_opened, fc_reveal)
                        if fc_i == sel:
                            add Solid(F12_FC_GOLD, xsize=F12_FC_TW + 6, ysize=F12_FC_TH + 6) pos (fc_x - 3, F12_FC_TY - 3)
                            add Solid("#000", xsize=F12_FC_TW + 2, ysize=F12_FC_TH + 2) pos (fc_x - 1, F12_FC_TY - 1)
                        elif fc_open and fc_c["colk"] != u"S":
                            add Solid(fc_lane_col, xsize=F12_FC_TW + 2, ysize=F12_FC_TH + 2) pos (fc_x - 1, F12_FC_TY - 1)
                        button:
                            pos (fc_x, F12_FC_TY)
                            xysize (F12_FC_TW, F12_FC_TH)
                            background f12_fc_thumb(fc_c, fc_open, fc_rd, fc_reveal)
                            action [SetScreenVariable("sel", fc_i), Function(f12_fc_scroll, fc_adj, fc_i)]
                            sensitive fc_open
                            add Solid("#000000af", xsize=F12_FC_TW, ysize=20) pos (0, F12_FC_TH - 20)
                            text (fc_c["short"] if fc_open else u"？？？") xanchor 0.5 yanchor 0.5 pos (F12_FC_TW // 2, F12_FC_TH - 10) font "gui/fonts/NotoSerifCJKjp-Medium.otf" size 12 color ("#fff" if fc_rd else ("#bdbdbd" if fc_open else "#6e6e6e"))
                            if fc_i == fc_cur_col:
                                frame:
                                    pos (0, 0)
                                    background Solid(F12_FC_GOLD)
                                    xpadding 5
                                    ypadding 1
                                    text (u"다시보기" if fc_mode == u"replay" else u"지금") font "gui/fonts/NotoSansCJKjp-Medium.otf" size 10 color "#000"
                        if fc_open and fc_c["sub"]:
                            text fc_c["sub"][:12] xanchor 0.5 yanchor 0.5 pos (fc_x + F12_FC_TW // 2, F12_FC_TY + F12_FC_TH + 9) font "gui/fonts/NotoSansCJKjp-Light.otf" size 9 color ("#bdbdbd" if fc_rd else "#8a8a8a")
                        for fc_ei, fc_end in enumerate([fc_e for fc_e in fc_c["ends"] if fc_reveal or (fc_open and f12_fc_end_open(fc_e))]):
                            $ fc_ey = F12_FC_TY + F12_FC_TH + 20 + fc_ei * 18
                            $ fc_eok = f12_fc_end_open(fc_end)
                            $ fc_eopen = fc_reveal or fc_eok
                            $ fc_eplay = bool(fc_end[3]) and fc_eok
                            $ fc_ecol = F12_FC_LANE_COLOR[fc_end[0]] if fc_eopen else u"#5a5a5a"
                            button:
                                pos (fc_x + 10, fc_ey)
                                xysize (F12_FC_TW - 20, 15)
                                background Solid(fc_ecol)
                                hover_background Solid(u"#f0d890")
                                padding (0, 0)
                                action Function(f12_fc_play_movie, fc_end[3])
                                sensitive fc_eplay
                                add Solid("#000000c8", xsize=F12_FC_TW - 22, ysize=13) pos (1, 1)
                                text ((u"▶ " if fc_eplay else u"") + (fc_end[4] if fc_eok else fc_end[1])) align (0.5, 0.5) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 9 color (F12_FC_LANE_COLOR[fc_end[0]] if fc_eopen else "#6e6e6e")

            textbutton u"◀" pos (0, 165) xysize (14, 30) background None text_size 13 text_color "#bbb" action Function(f12_fc_scroll_by, fc_adj, -F12_FC_CW)
            textbutton u"▶" pos (1011, 165) xysize (14, 30) background None text_size 13 text_color "#bbb" action Function(f12_fc_scroll_by, fc_adj, F12_FC_CW)

            text (fc_selcol["short"] if fc_opened[fc_selcol["key"]] else u"？？？") pos (20, 290) font "gui/fonts/NotoSerifCJKjp-Medium.otf" size 20 color "#fff"
            text (fc_selcol["sub"] if fc_opened[fc_selcol["key"]] else u"") pos (20 + len(fc_selcol["short"]) * 21 + 12, 298) font "gui/fonts/NotoSerifCJKjp-Light.otf" size 14 color "#cfcfcf"
            text (u"%d / %d 끝까지 읽음" % (fc_sel_rd, fc_sel_total)) xanchor 1.0 pos (1005, 300) font "gui/fonts/NotoSansCJKjp-Light.otf" size 11 color (F12_FC_GOLD if (fc_sel_total and fc_sel_rd == fc_sel_total) else "#9a9a9a")
            for fc_wn, fc_wopen, fc_wrd, fc_wnow, fc_wtarget in fc_weeks:
                $ fc_won = fc_selcol["wn"] == fc_wn
                button:
                    pos (340 + (fc_wn - 1) * 36, 287)
                    xysize (32, 32)
                    background None
                    hover_background "gui/num_hover.png"
                    selected_background F12_FC_NUM_SEL
                    selected fc_won
                    sensitive fc_wopen
                    action [SetScreenVariable("sel", fc_wtarget), Function(f12_fc_scroll, fc_adj, fc_wtarget)]
                    text (F12_FC_ROMAN[fc_wn - 1] if fc_wopen else u"·") align (0.5, 0.5) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 14 color ("#fff" if (fc_wrd or fc_won) else ("#9a9a9a" if fc_wopen else "#5a5a5a"))
            add im.Scale("gui/right_click_fg.png", 985, 2) pos (20, 322)

            for fc_ci in range(4):
                for fc_ri, fc_row in enumerate(fc_grid[fc_ci]):
                    $ fc_rx = 24 + fc_ci * 246
                    $ fc_ry = 332 + fc_ri * 23
                    if fc_row[0] == u"c":
                        $ fc_ch = fc_row[1]
                        $ fc_act = F12FCChain(fc_ch["file"], fc_ch["sid"], fc_selcol["colk"]) if fc_mode == u"replay" else F12FCReplay(fc_ch["file"], fc_ch["sid"], fc_selcol["colk"])
                        button:
                            pos (fc_rx - 8, fc_ry - 1)
                            xysize (238, 22)
                            background (Solid("#d9b65c40") if fc_row[3] else None)
                            hover_background "#74040499"
                            action fc_act
                            add (F12_FC_GEAR_READ if fc_row[2] else F12_FC_GEAR_UNREAD) pos (8, 5)
                            text (fc_ch["name"][:14] if (fc_row[2] or fc_reveal or fc_row[3]) else u"？？？") xpos 28 ypos 11 yanchor 0.5 font "gui/fonts/NotoSerifCJKjp-Light.otf" size 13 color ("#fff" if (fc_row[2] or fc_row[3]) else "#8a8a8a")
                            if fc_row[3]:
                                text fc_now_tag xanchor 1.0 yanchor 0.5 pos (232, 11) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 10 color F12_FC_GOLD
                            else:
                                text fc_ch["sid"] xanchor 1.0 yanchor 0.5 pos (232, 11) font "gui/fonts/NotoSansCJKjp-Light.otf" size 9 color "#6a6a6a"
                    elif fc_row[0] == u"m":
                        $ fc_mv = fc_row[1]
                        $ fc_mok = f12_fc_end_open([u"", u"", fc_mv["unlock"]])
                        button:
                            pos (fc_rx - 8, fc_ry - 1)
                            xysize (238, 22)
                            background None
                            hover_background "#74040499"
                            action Function(f12_fc_play_movie, fc_mv["path"])
                            sensitive fc_mok
                            frame:
                                pos (8, 4)
                                xysize (14, 14)
                                background Solid(F12_FC_GOLD if fc_mok else u"#5a5a5a")
                                padding (0, 0)
                                text u"▶" align (0.5, 0.5) font "gui/fonts/NotoSansCJKjp-Regular.otf" size 8 color "#000"
                            text (fc_mv["label_open"] if fc_mok else fc_mv["label"]) xpos 28 ypos 11 yanchor 0.5 font "gui/fonts/NotoSerifCJKjp-Light.otf" size 13 color (F12_FC_GOLD if fc_mok else "#8a8a8a")
                            text u"영상" xanchor 1.0 yanchor 0.5 pos (232, 11) font "gui/fonts/NotoSansCJKjp-Light.otf" size 9 color "#6a6a6a"
                    elif fc_row[0] == u"n":
                        text fc_row[1] xpos fc_rx ypos (fc_ry + 10) yanchor 0.5 font "gui/fonts/NotoSansCJKjp-Light.otf" size 12 color "#9a9a9a"
                    else:
                        $ fc_mark = u"▶ " if fc_row[7] else u""
                        $ fc_ocol = ((u"#9c8448" if fc_row[8] else F12_FC_GOLD) if fc_row[7] else ("#d0d0d0" if fc_row[6] else "#8a8a8a"))
                        text (u"└ " + ((fc_mark + fc_row[1][:13]) if fc_row[5] else u"？？？")) xpos (fc_rx + 20) ypos (fc_ry + 10) yanchor 0.5 font "gui/fonts/NotoSansCJKjp-Light.otf" size 12 color fc_ocol
                        if fc_row[5] and fc_row[3]:
                            text fc_row[3] xanchor 1.0 yanchor 0.5 pos (fc_rx + 224, fc_ry + 10) font "gui/fonts/NotoSansCJKjp-Medium.otf" size 11 color fc_row[4]
                        elif fc_row[5] and fc_row[2]:
                            text (u"호감도 " + fc_row[2]) xanchor 1.0 yanchor 0.5 pos (fc_rx + 224, fc_ry + 10) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"

            if fc_mode == u"replay":
                text u"끝까지 읽은 장면을 누르면 지금 다시보기를 끝내고 그 장면으로 넘어갑니다. ▶ 표시는 오프닝·엔딩 영상입니다." pos (20, 540) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"
            else:
                text u"끝까지 읽은 장면을 누르면 그 장면만 다시 봅니다. ▶ 표시는 오프닝·엔딩 영상. 진행·플래그·세이브에는 영향이 없습니다." pos (20, 540) font "gui/fonts/NotoSansCJKjp-Light.otf" size 10 color "#9a9a9a"

    if fc_mode == u"replay":
        textbutton u"다시보기 종료" style "menu_navigation_button" text_style "menu_navigation_button_text" pos (972, 670) action EndReplay(False)

    use menu_navigation(config.menu_navigation_align)

    on "show" action Function(f12_fc_scroll, fc_adj, sel)

    # 마우스 휠: 화면 어디서든 리본을 좌우로 한 칸씩 (올리면 왼쪽, 내리면 오른쪽)
    key "mousedown_4" action Function(f12_fc_scroll_by, fc_adj, -F12_FC_CW)
    key "mousedown_5" action Function(f12_fc_scroll_by, fc_adj, F12_FC_CW)
