from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "work" / "catalog_design" / "scenario_001.catalog.jsonl"
STYLE_GUIDE = Path(r"P:\AI\Codex\projects\fatal-twelve-ko\style_guide.md")
OUTPUT_JSON = Path(__file__).with_name("translation_001_after_2922.json")
OUTPUT_RPY = Path(__file__).with_name("translation_001_after_2922.rpy")

SOURCE_FILE = "scenario/001.rpy"
LINE_THRESHOLD = 2922
EXPECTED_FIRST_COMMAND = 657
EXPECTED_LAST_COMMAND = 844
EXPECTED_COUNT = 188
STATUS = "first_draft_unreviewed"
QA = "deferred_until_full_first_draft"
STYLE_GUIDE_SHA256 = "b2b87352fdfd9b25af688152b0ce8a7460ffeb88fc06ae6e45f1c5df2ae83891"


# Japanese source only. The first field is the catalog command_index and the
# second field is the unreviewed Korean first draft. Do not use this table as a
# reviewed translation memory until the deferred whole-draft QA pass.
DRAFT_TSV = r'''657	「――――읏!」
658	눈앞에 펼쳐진 것은 한 번도 본 적 없는 광경이었다.
659	끝없이 펼쳐진 어둠 속에 수많은 톱니바퀴가 떠 있다. 위를 올려다보니 희미한 빛이 어둠의 틈새로 쏟아져 내리고 있었다.
660	그리고 나는 내가 서 있다는 사실을 깨달았다.
661	지름 ３미터쯤 되는 둥근 바닥에 법정의 증언대 같은 난간이 붙어 있다. 이런 건 뉴스나 드라마에서밖에 본 적이 없다.
662	게다가 이 둥근 바닥은 어둠 속에 떠 있는 듯했다.
663	틀 같은 것에 끼워져 있기는 했지만, 바닥 자체는 따로 떨어져 떠 있었다.
664	비좁고 둥근 바닥 12개가 원을 그리며 늘어서 있다. 마치 시계 문자판 같은 배치였다.
665	그것을 암시하듯 내가 선 바닥에는 “Ⅰ”이라는 숫자가 적혀 있었다.
666	게다가 12개 바닥의 중심에서는 거대한 시곗바늘이 공기를 떨게 하며 아주 천천히 시간을 새기고 있었다.
667	「뭐야…… 여긴…… 대체 뭐야?」
668	「어째서…… 네가!」
669	그 목소리를 듣는 순간, 나는 저도 모르게 숨을 삼켰다.
670	내 옆 바닥. 번호로 말하면 “Ⅱ”의 바닥 위에 아는 얼굴이――미하루가 서 있었다.
671	「미……」
672	「“Ⅰ”번 님?　그분의 이름은 말씀하지 않는 편이 좋답니다」
673	이름을 부르려던 나를 처음 듣는 목소리가 제지했다. 목소리가 난 쪽에는 복슬복슬한 흰 머리의 소녀가 있었다.
674	「어……?　바닥도 없는 곳을 걷고 있어……?」
675	소녀는 우리와 달리 둥근 바닥 위에 서 있지 않았다.
676	이 공간의 아무것도 없는 곳을 태연하게 걷고 있었다.
677	허공에서 한 걸음 내디뎌 바닥이 끼워진 틀의 가장자리에 올라섰다. 그리고 그곳에서 멈춰 섰다.
678	치맛자락이 살랑 떠오르며 가느다란 허벅지가 하늘에서 비치는 빛을 반사했다.
679	솜사탕 같은 머리카락을 닮아 폭신해 보이는 그녀의 옷은 외국 아가씨가 입을 법한 품위 있는 차림이었다.
680	작은 머리 위에 살포시 얹힌 모자가 귀여웠다.
681	내가 뒤돌아 소녀를 보자 그녀도 돌아보았고, 시선이 마주쳤다.
682	「저는 운명의 여신 파르카. 『여신의 선정』을 관장하는 관리자이자, 여러분 인간보다 상위에 있는 존재랍니다」
683	「――――뭐?　미안, 무슨 소리야?」
684	「하아……. 아무래도 당신은 죽음의 충격으로 기억 일부가 빠져 버린 모양이군요」
685	「당신에게도 설명해 드렸던 것 같은데, 어쩔 수 없으니 딱 한 번만 더 설명하도록 하지요」
686	「설명?　죽음의 충격?　미안한데, 애초에 무슨 말인지 하나도 모르겠거든……」
687	「조용히 듣고 계시겠어요?」
688	소녀는 한숨을 내쉬며 어이없다는 목소리로 말했다.
689	누가 봐도 나보다 어렸지만, 이렇게까지 내려다보는 태도로 말하니 반감이 들었다.
690	「넌 잊고 있었기 때문에 지난 며칠을 평범하게 지낼 수 있었던 거구나. 너 자신을 위해서라도 이대로 이야기를 듣는 게 좋아」
691	「그, 그래도」
692	「말을 바꾸지. 그렇게 해 줘」
693	「아…… 알겠어」
694	「됐을까요?　괜찮으시다면 다른 여러분도 다시 한번 되짚어 보시길」
695	파르카는 떠 있는 바닥 끝에서 시곗바늘을 다리 삼아 나아가더니, 이번에는 거대한 시계 중심을 향해 움직이기 시작했다.
696	걸음을 옮기면서 우아한 말투로 이야기를 이어 갔다.
697	「여신의 선정. 그것은 똑같이 ≪인과의 때≫를 지닌 여러분이 각자의 ≪죽음의 운명≫을 피하기 위한 의식이랍니다」
698	「앞서도 말씀드렸지만, 저는 운명의 여신 파르카. 이제부터 12번의 일요일――오늘을 빼면 앞으로 11번뿐인――짧은 기간이지만, 잘 부탁드리겠어요」
699	파르카는 여기까지 말했을 때 마침 중심에 도착했다.
700	허리를 곧게 펴고 치맛자락을 살짝 들어 올려 인사한 뒤, 다시 천천히 입을 열었다.
701	「선정이 끝나는 12주 뒤, 여러분 12명은 같은 순간, 같은 장소에 있었을 예정이었습니다」
702	「하지만 그 결과에 도달하지 못한 채 여러분의 생명은 끝나 버렸습니다. 장소는 제각각이었지만, 공교롭게도 완전히 같은 시각에 말이지요」
703	「――바로 그때가 ≪인과의 때≫」
704	인과의, 때.
705	파르카는 그렇게 말했다. 하지만 나는 전혀 이해하지 못하고 있었다.
706	그녀의 말이 사실이라면 미하루도, 나도, 여기 있는 모두가――죽었다는 뜻이 된다.
707	그건 이상하다. 나는 평범하게 살아가고 있었으니까.
708	사실은 유령이었다고?――그건 더더욱 말이 안 된다.
709	뒤엉킨 생각 속에서 나는 일단 다음 이야기를 듣기로 했다.
710	「≪인과의 때≫에는 장소가 중요하지 않답니다. 죽음의 순간 여러분의 의식은 현실에서 분리되니까요. 형이하의 존재에서 형이상의 존재로 승화한 것이랍니다」
711	「살아 있는 동안에도 가끔 의식이 형이상으로 옮겨 간 적이 있었겠지요――사람들은 때로 그것을 꿈이라 부른답니다」
712	「이곳은――꿈의 세계라고 해 둘까요」
713	「사람들의 집단 무의식 세계이자 수많은 평행 세계이며, 여러분 각자의 정신세계이기도 한――불안정하고 실존하지 않는 세계」
714	「존재하는지조차 불확실한 세계를 여러분이 인식할 수 있도록, 제가 이 ≪운명의 대전당≫을 만들어 드렸답니다」
715	나는 주위를 둘러보았다.
716	벽도 없다. 천장도 없다.
717	하지만 파르카가 대전당이라고 부르자 이 기묘한 공간이 정말 대전당인 것처럼 느껴졌다.
718	「이름을 붙이는 것이야말로 실존하지 않는 것에 존재와 의미를 부여하는 가장 단순하면서도 가장 강력한 방법이랍니다. 이해하셨을까요?」
719	「잔말은 됐다. 어서 지명하게 해」
720	파르카의 말을 가로막듯 남자의 목소리가 들렸다.
721	목소리는 내 오른쪽 옆, 바닥 번호로 치면 “Ⅻ”에서 들려왔다.
722	갈색 피부에 검은 머리인 남자다. 키가 크고 근육질이며 이목구비가 뚜렷했다. 생김새로 보아 중동 사람처럼 보인다.
723	아니, 잠깐만.
724	소녀도 남자도 어떻게 일본어를 이렇게 유창하게 하는 걸까.
725	이런 의문은 훨씬 일찍 가졌어야 했다. 「아, 일본어를 할 줄 아는구나」라고 바로 생각했어야 했다.
726	너무나 자연스러워서 신경 쓰지 못했던 것이다.
727	「서두른다고 좋은 일은 없답니다. 중요한 설명은 지금부터니까요」
728	소녀는 끝까지 차분한 말투로 남자를 타일렀다.
729	「이야기를 돌려놓도록 하지요」
730	「여러분 12명 가운데 운명의 너머로 나아갈 수 있는 사람은 단 １명뿐입니다」
731	「선정 기간에는 여러분의 사인이 된 사건이 없었던 일이 되어 있지만, 마지막에 남는 １명을 제외하면 결국 본래의 ≪죽음의 운명≫으로 돌아가게 됩니다」
732	「누군가 탈락하는 순간, 이 세계는 ≪그 사람이 본래의 때에 죽은 세계≫로 다시 쓰입니다. 운명이 되감기고 선정 기간에 이룬 일들이 사라진다는 뜻이지요」
733	「그리고 ≪인과의 때≫부터 ≪선정 종료≫까지의 기간 동안 여러분은 ≪이치를 벗어난 존재≫라고 여기셔도 무방하답니다」
734	「즉, 이 ≪여신의 선정≫ 이외의 이유로는 절대로 죽지 않습니다. 죽지 않을 정도의 부상이라면 입을지도 모르지만요」
735	「어리석은 “Ⅰ”번 님?　이제 당신도 이해하셨겠지요?」
736	파르카는 나를 바라보며 말을 이었다.
737	여기까지 들으면 소녀가 무슨 말을 하려는지 싫어도 짐작할 수밖에 없다.
738	「12명이 서로 죽이는 거야――?」
739	「90％ 정답이랍니다. 하지만 어디까지나 ９할일 뿐. 실제로 서로 죽이는 야만적인 방법은 쓰지 않습니다」
740	「여러분에게는 서로를 ≪죽이는≫ 대신 ≪탈락시키며≫ 겨뤄 주셔야겠어요. 왜냐하면――여러분은 이미 죽었으니까요」
741	「…………빈정거리네」
742	미하루와 나 이외의 10명도 저마다 다른 반응을 보이고 있었다.
743	파르카와 우리의 목소리는 이 공간에 울려 퍼져 모두에게 들리고 있는 모양이다.
744	하지만 지금의 내게는 이 자리에 있는 모두를 제대로 살펴볼 마음의 여유가 없었다.
745	단 한 사람, “Ⅵ”번만은 낙담한 듯 주저앉아 있었다. 기운이 없고 잠든 것처럼 보였다. 여자였다.
746	나는 관찰하기보다 이 영문 모를 상황과 말로 다 할 수 없는 불안을 떨쳐 내려고 파르카의 설명에 귀를 기울였다.
747	믿을지 말지는 그다음에 정하면 된다.
748	「선정 참가자를 탈락시키는 방법은 카드 ３장을 모으는 것」
749	「여러분 한 사람 한 사람에게는 ≪현재≫≪과거≫≪미래≫를 나타내는 ≪성명≫≪사인≫≪미련≫ 카드 ３장이 할당되어 있습니다」
750	「자신의 정보가 적힌 ≪자신의 카드≫를 가지고 계실 테니, 이미 알고 계시겠지요」
751	「아무런 단서도 없으면 선정이 진행되지 않겠지요. 여러분에게는 ≪자신의 카드≫ 외에도 다른 참가자의 카드를 무작위로 ３장씩 나눠 드렸답니다」
752	「그리고 이제부터는 카드를 직접 모으셔야 합니다. 선정 참가자 각자의 정보를 알게 되는 순간, 정보라는 개념은 카드라는 실존으로 바뀝니다」
753	「여러분의 세계――이 꿈의 세계가 아닌 현실 세계에서 정보를 모으세요. 그러면 자연스럽게 카드를 얻게 될 것입니다」
754	「꿈과 현실을 잇는 것――≪카드북≫은 이미 여러분의 손에 있습니다. 자, 여기에도」
755	그 말을 듣고 나는 시선을 아래로 내렸다.
756	난간이라고 생각했던 것은 독서대였다. 평평한 부분 위에 책 한 권이 놓여 있었다.
757	적갈색 표지에는 금빛 톱니바퀴 같은 장식이 되어 있었다.
758	「이 책…… 나오미와 함께 봤어. 왜 여기에 있지?」
759	펼쳐 보니 라이온관에서 봤던 것과 마찬가지로 한가운데에 직사각형 구멍이 뚫려 있었다.
760	「으앗!」
761	그 순간 책에서 눈부신 빛이 흘러넘쳤다.
762	나는 반사적으로 눈을 감았다. 눈꺼풀 너머로 빛이 조금씩 약해지는 것을 느끼고 서서히 눈을 떴다.
763	카드가 허공에 떠 있었다. ４장의 카드는 같은 간격으로 늘어서 책 바로 위에 멈춰 있었다.
764	――Ⅰ・성명・시시마이 린카.
765	――Ⅲ・성명・페데리코 카르미나티.
766	――Ⅳ・사인・소사.
767	――Ⅸ・미련・금메달.
768	카드들은 이 정보가 적힌 면을 내 쪽으로 향하고 있었다.
769	기억이 흐릿해서인지 내 정보가 적힌 카드는 １장밖에 없다. 거기에 다른 사람의 카드 ３장을 더해 모두 ４장이다.
770	무심코 미하루 쪽을 보았지만 책 주위가 빛에 둘러싸여 잘 보이지 않았다.
771	「자신 이외에는 카드의 정보도, 몇 장을 가지고 있는지도 보이지 않는다는 거네」
772	「그래서 네 책 주위가 빛나서 보이지 않는 거구나」
773	미하루는 내 시선을 눈치챘는지 알아낸 사실을 짤막하게 알려 주었다.
774	파르카는 우리에게 신경 쓰지 않고 설명을 더 이어 갔다.
775	「지명 순서는 여러분이 의사를 밝힌 뒤 정해집니다. 여러분에게 할당된 번호 때문에 지명할 수 없게 되는 일은 없습니다」
776	「지명한 상대가 자신을 지명했을 때는 ≪자신의 카드≫ １장을 참가자 모두에게 공개한 쪽이 지명할 권리를 얻게 됩니다」
777	양쪽 모두 ≪자신의 카드≫를 공개했다면 １장을 더…… 파르카는 계속 설명했다.
778	서로 ３장을 공개하면…… 우열을 가릴 수 없어 지명은 무효가 된다고 한다. 다른 참가자에게 지명당할 위험만 낳을 뿐이다.
779	애초에 자신의 정보는 세 가지뿐이다. 하나라도 참가자 모두에게 알려지는 것만으로도 큰 위험이 된다.
780	하지만 결국 거기서 ≪자신의 카드≫를 공개하지 않는다면 자신이 탈락하고 만다.
781	게다가 나는 ≪자신의 카드≫를 １장밖에 가지고 있지 않다. 이건 어떻게 된 일일까.
782	질문할 틈도 없이 파르카는 이야기를 계속했다.
783	「그 밖에 주의하실 점이 있습니다. 예를 들어 Ⅰ번 님이 Ⅻ번 님을 지명하고 Ⅲ번 님이 Ⅰ번 님을 지명했다면, Ⅰ번 님이 Ⅻ번 님을 탈락시킨 뒤 Ⅰ번 님은 Ⅲ번 님에게 탈락당합니다」
784	「지명 의사를 밝힌 뒤 지명은 할당된 번호 순서대로 진행됩니다. 이것이 기본 규칙이랍니다」
785	「다만 Ⅰ번 님이 Ⅻ번 님을, Ⅻ번 님이 Ⅲ번 님을 지명했다면, Ⅰ번 님이 Ⅻ번 님을 탈락시키는 순간 Ⅲ번 님을 향한 지명은 사라지고 맙니다」
786	「이렇게 순서가 뒤틀릴 때――탈락자가 가장 많아지도록 순서를 바꾼답니다」
787	나는 새삼 이 카드가 지닌 의미를 깨달았다.
788	나도 모르는 사이에 죽고, 여신의 선정이라는 것에 참가하게 되어 카드를 손에 넣었다.
789	카드를 모아 상대를 탈락시킨다. ≪여신의 선정≫이라고 부르지만, 이래서는 마치 게임이다. 단, 걸려 있는 것은 내 미래의 목숨이다.
790	처음 보는 상대의 정보를 모으는 건 쉬운 일이 아니다. 하지만 모으기만 한다면…….
791	「정보 ３개를 다 들키면 끝이라는 거잖아?　그건……」
792	「……방어책이라는 게 있는 모양이야」
793	그 말을 듣고 나는 미하루를 빤히 바라보며 다음 말을 기다렸다.
794	「자신을 탈락시키려고 지명해 온 상대의 카드를 ３장 가지고 있는 것」
795	「그 ３장의 카드를 바쳐――소멸시키면 자신을 지킬 수 있는 모양이야. 지명해 온 상대의 카드도 소멸한다……는 뜻이겠지」
796	「지명당한 쪽은 지명해 온 상대를 앞으로 지명할 수 없게 되는 대신, 그 상대에게도 지명당하지 않게 돼」
797	「다만 그 경우 지명자는 ≪자신의 카드≫ １장을 참가자 모두에게 공개해서 상대의 방어를 깨뜨릴 수 있어…… 맞지?」
798	「그래요. 당신은 제대로 기억하고 계신 모양이라 안심했답니다」
799	「만약 그 둘이 마지막 두 사람이 되면…… 어떻게 돼?」
800	「그건…… 때가 오면 설명해 드리지요」
801	파르카는 잘라 말하듯 그렇게 말했다.
802	내가 「하지만」이나 「그럼」 같은 말로 끈질기게 물어도 전혀 상대해 주지 않았다.
803	「한 가지 더, 지명당해도 탈락하지 않고…… 피할 수 있는 경우가 있지?」
804	질문한 미하루를 향해 파르카는 대담한 미소를 지었다.
805	「예를 들어 어떤 인물을 다른 두 사람이 동시에 지명하는 경우」
806	「이때 지명 우선권을 놓고 다투게 돼. 조건은 아까와 같은 『≪자신의 카드≫ １장을 참가자 모두에게 공개하는 것』이 맞지?」
807	「둘 다 ≪자신의 카드≫를 공개하지 않고 우선권을 가져가지 않으면 지명은 무효가 되는 거야……?」
808	「눈치가…… 아주 나쁘지는 않으시군요. 맞습니다」
809	미하루는 파르카가 설명을 계속하려는 것을 보고 책을 덮었다.
810	나도 책을 덮으려 했지만 저항감이 느껴졌고, 그사이 카드는 저절로 책 속으로 돌아가 있었다.
811	그러자 저항감이 사라져 원래대로 덮을 수 있었다.
812	스마트폰 앱에서 흔히 보던 익숙한 동작이 물리적으로 일어나고 있었다.
813	「하룻밤에 지명할 수 있는 사람은 한 사람당 한 번까지라는 것도 잊지 마시길」
814	「그리고 모두의 지명 의사를 확인한 뒤 실제 지명으로 넘어갑니다」
815	「지명자가 ≪자신의 카드≫를 공개한 탓에 다른 참가자가 그분의 카드 ３장을 모으게 되더라도, 실제로 지명할 수 있는 것은 다음 선정부터랍니다」
816	선정에도 정해진 흐름이 있는 모양이다.
817	「지명할지 말지」를 정한 뒤 「실제 지명」을 진행한다는 것.
818	파르카가 말하는 규칙이 중요하다는 건 안다. 혼란스러운 머리로도 필사적으로 따라가려 했다.
819	「지명해 상대를 탈락시키면 여러분에게도 이점이 있답니다」
820	「그것은 탈락시킨 상대에게서 카드 １장을 얻을 수 있다는 점이지요. 그 대신……」
821	「이제 그만하면 됐잖아?」
822	그렇게 말한 사람은 아까도 파르카의 말을 가로막으려 했던 남자였다.
823	「아니, 그만해!　시작되면 나!　내가!」
824	「싫어!　빌!　살려 줘어어어어!」
825	「닥쳐」
826	「여신. 당신도 이 상태로는 이야기를 계속할 수 없겠지?」
827	비통하게 외치는 여자를 향해 그는 아무런 감정도 보이지 않았다.
828	성가심조차도. 여신도 마찬가지였다.
829	「정말, 어쩔 수 없군요. 좋습니다, 그러면」
830	「――지금부터 오늘 밤의 선정을 시작하겠습니다」
831	그 뒤에 일어난 일은 잘 기억나지 않는다.
832	Ⅻ번 남자가 Ⅵ번 여자를 지명하자 두 사람의 바닥이 솟아올라 위쪽으로 사라졌다.
833	잠시 뒤 Ⅻ번 남자만 내려왔다. 아마 그것이 이른바 ≪지명≫이었고, Ⅻ번 남자가 Ⅵ번 여자의 카드 ３장을 가지고 있어 그것으로 탈락시킨 것이리라.
834	돌아왔을 때 남자는 「Ⅷ・성명이다」라며 파르카에게 카드를 보여 주었다.
835	분명 이것이 아까 여신이 「그 대신」이라고 말하다 만 이야기의 뒷부분일 것이다.
836	누구의 어떤 카드를 얻었는지 그 사실이 다른 참가자들에게 알려지고 만다.
837	「걱정하지 않으셔도 이 시간은 여러분이 잠든 시간. 현실의 시간과는 다른 틈새의 때랍니다」
838	「즉, 눈을 뜨면――언제나와 같은 아침」
839	「그러면 오늘 밤의 탈락자는 １명. 이것으로 선정을 마치도록 하지요」
840	몽롱한 의식 속에서 파르카의 그런 목소리가 들렸다.
841	의식은 흐려져 갔고 잠에 빠질 때와 같은 감각이 밀려왔다.
842	나는 이미 완전히 생각하기를 멈춘 상태였다.
843	「받아들이는 게 무리잖아」
844	――그 모든 걸.
'''


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_drafts() -> dict[int, str]:
    drafts: dict[int, str] = {}
    for raw_line in DRAFT_TSV.splitlines():
        if not raw_line:
            continue
        index_text, draft = raw_line.split("\t", 1)
        index = int(index_text)
        if index in drafts:
            raise ValueError(f"duplicate command_index in draft: {index}")
        drafts[index] = draft
    expected = set(range(EXPECTED_FIRST_COMMAND, EXPECTED_LAST_COMMAND + 1))
    if set(drafts) != expected:
        missing = sorted(expected - set(drafts))
        extra = sorted(set(drafts) - expected)
        raise ValueError(f"draft index mismatch: missing={missing}, extra={extra}")
    return drafts


def load_source_rows() -> list[dict]:
    rows = []
    with CATALOG.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            record = json.loads(raw_line)
            source = record["source"]
            if source["script"] == SOURCE_FILE and source["line"] > LINE_THRESHOLD:
                rows.append(record)
    rows.sort(key=lambda row: row["command_index"])
    indices = [row["command_index"] for row in rows]
    expected = list(range(EXPECTED_FIRST_COMMAND, EXPECTED_LAST_COMMAND + 1))
    if indices != expected:
        raise ValueError(f"catalog command range changed: {indices[:3]}...{indices[-3:]}")
    if len(rows) != EXPECTED_COUNT:
        raise ValueError(f"catalog row count changed: {len(rows)}")
    if any(row["localization"]["translation_id"] is None for row in rows):
        raise ValueError("unexpected menu/string record in this source-line range")
    return rows


def assert_protected_tokens(record: dict, draft: str) -> None:
    for packed, expected_count in record["protected_token_multiset"].items():
        _kind, value = packed.split("\0", 1)
        actual_count = draft.count(value)
        if actual_count != expected_count:
            raise ValueError(
                f"protected token mismatch at command {record['command_index']}: "
                f"{value!r} expected={expected_count} actual={actual_count}"
            )


def renpy_quote(text: str) -> str:
    return text.replace("\\", "\\\\").replace('"', '\\"')


def build_entry(record: dict, draft: str) -> dict:
    source = record["source"]
    speaker_code = record["speaker"]["code"] if record["speaker"] else "narrator"
    return {
        "sequence": record["command_index"],
        "command_index": record["command_index"],
        "stable_id": record["stable_id"],
        "translation_id": record["localization"]["translation_id"],
        "id_origin": record["localization"]["id_origin"],
        "source_file": source["script"],
        "source_line": source["line"],
        "source_label": source["label"],
        "lane": record["lane"],
        "speaker": speaker_code,
        "source_jp": source["text_ja"],
        "source_statement_code": source["statement_code"],
        "source_group_code": source["group_code"],
        "source_text_sha256": source["text_sha256"],
        "source_group_sha256": source["group_sha256"],
        "voice_call": record["voice_call"]["statement"] if record["voice_call"] else "",
        "protected_tokens": record["protected_tokens"],
        "draft_ko": draft,
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "status": STATUS,
        "qa": QA,
    }


def build_rpy(entries: list[dict]) -> str:
    output = [
        "# -*- coding: utf-8 -*-",
        "# Fatal Twelve scenario/001.rpy Korean first draft",
        "# Semantic/style source: Japanese only; English prose was not opened or used.",
        f"# Scope: source_line > {LINE_THRESHOLD}; records: {len(entries)}.",
        f"# status: {STATUS}",
        f"# qa: {QA}",
        "",
    ]
    for entry in entries:
        translation_id = entry["translation_id"]
        output.append(
            f"# {entry['stable_id']} | {entry['source_file']}:{entry['source_line']}"
        )
        output.append(f"translate korean {translation_id}:")
        group = entry["source_group_code"]
        for prelude in group[:-1]:
            output.append(f"    {prelude}")
        output.append(f"    # {entry['source_statement_code']}")
        statement = entry["source_statement_code"]
        quote_position = statement.find('"')
        if quote_position < 0:
            raise ValueError(f"unsupported Say statement: {statement!r}")
        prefix = statement[:quote_position]
        output.append(f'    {prefix}"{renpy_quote(entry["draft_ko"])}"')
        output.append("")
    return "\n".join(output) + "\n"


def main() -> None:
    if sha256(STYLE_GUIDE) != STYLE_GUIDE_SHA256:
        raise ValueError("style guide SHA-256 changed")
    drafts = load_drafts()
    rows = load_source_rows()
    entries = []
    for row in rows:
        draft = drafts[row["command_index"]]
        assert_protected_tokens(row, draft)
        entries.append(build_entry(row, draft))

    ids = [entry["translation_id"] for entry in entries]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate translation ID")

    packet = {
        "schema_version": "fatal-twelve-ko-first-draft-v1",
        "packet_id": "scenario_001_after_source_line_2922",
        "source_file": SOURCE_FILE,
        "source_line_filter": {"operator": ">", "value": LINE_THRESHOLD},
        "entry_count": len(entries),
        "first_source_line": entries[0]["source_line"],
        "last_source_line": entries[-1]["source_line"],
        "first_command_index": entries[0]["command_index"],
        "last_command_index": entries[-1]["command_index"],
        "source_language": "ja",
        "target_language": "ko",
        "translation_basis": "Japanese source only; Codex internal translation",
        "source_authority": "Japanese only",
        "english_reference_used": False,
        "external_translation_api_used": False,
        "translation_validation": "not_performed",
        "structure_validation": "performed_during_generation",
        "status": STATUS,
        "qa": QA,
        "style_guide": {
            "path": str(STYLE_GUIDE),
            "sha256": STYLE_GUIDE_SHA256,
        },
        "catalog": {
            "path": str(CATALOG.relative_to(ROOT)).replace("\\", "/"),
            "sha256": sha256(CATALOG),
            "stable_id_source": "exact catalog stable_id",
        },
        "entries": entries,
    }
    OUTPUT_JSON.write_text(
        json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    OUTPUT_RPY.write_text(build_rpy(entries), encoding="utf-8", newline="\n")
    print(
        json.dumps(
            {
                "json": str(OUTPUT_JSON),
                "rpy": str(OUTPUT_RPY),
                "entry_count": len(entries),
                "first_source_line": entries[0]["source_line"],
                "last_source_line": entries[-1]["source_line"],
                "status": STATUS,
                "qa": QA,
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
