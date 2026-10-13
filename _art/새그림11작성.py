# 11 기손 강 그림 작업 파일(새그림11.json) 만들기 v0.1 (2026-10-13)
# 사용: python 새그림11작성.py → 새그림11.json. 그린 뒤 고르기_11.json으로 모은다.
# 배경(bg11w)은 ref2/ref11.png(길 시안, 강 포함)를 참조로 그린다. 강이나 산이 길을 덮으면 9·10처럼 그림에 맞춰 길과 탑 자리를 고친다.
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
DEBORAH = "Deborah, the prophetess and judge of Israel, a wise and kind Israelite woman of about fifty with dark hair touched with gray under a long cream-and-blue headscarf, wearing a deep blue wool robe with an ochre sash"
BARAK = "Barak, the commander of Israel from Naphtali, a strong man of about thirty-five with a black beard, a rounded bronze helmet and a brown leather armor vest over a green tunic, holding a spear"
ISRAEL = "Israelite soldiers of Zebulun and Naphtali, ordinary men in tan and green tunics with rounded bronze helmets, spears and round wooden shields"
# 가나안(하솔 왕 야빈, 삿 4:2): 9 여리고의 c_ 군사와 같은 옷(둥근 청동 투구, 한쪽 어깨에 두른 무늬 모직 옷). 웃음거리로 그리지 않는다
CANAAN = "Canaanite charioteers with curly black hair and short beards, rounded bronze helmets and colorful patterned wool tunics"
CHARIOTS = "heavy Canaanite war chariots of dark wood plated with black iron, with iron-rimmed spoked wheels, each pulled by two dark brown horses"
TABOR = "Mount Tabor, a big lonely round dome-shaped green mountain rising from the plain"
WISPS = "small dark purple-and-indigo smoke wisps with glowing lilac eyes and curly smoke tails, swarming like a flock of tiny shadows"


def scene(i, pr, seeds=(1, 2)):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + END}


items = [
    {"id": "bg11w", "종류": "장면", "크기": [1536, 864], "시드": [1, 2], "참조": ["ref2/ref11.png"],
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield on the wide green plain of Jezreel, seen from above at a slight angle. "
                 "Keep exactly the same sandy road shapes and positions: the road that enters from the left edge in the upper part and bends down beside the river, the road that enters from the left edge in the lower part, the place in the middle where they meet just left of the river, "
                 "the shallow stony ford where the road crosses the river, and the winding road on the right side that ends at the upper right. "
                 "Keep the blue river exactly where it is: the old river Kishon, a calm winding river flowing from the top edge down to the bottom edge through the middle of the map, with grassy banks, reeds and a few flat stones at the shallow ford; the road crosses the water only at the ford. "
                 "At the upper right corner, the lower slope of Mount Tabor, a big round dome-shaped green mountain; at its foot, exactly where the road ends, a small Israelite camp of a few brown goat-hair tents. "
                 "On the right side, between the road and the right edge, one olive tree. "
                 "Elsewhere: a flat fertile plain with green and golden fields, low stone field walls, a few olive trees and bushes, small boulders; the plain is open and flat, good for chariots. "
                 "Nothing covers the roads or the river. Soft daylight under a few clouds. No characters, no text."},
    # 이야기(10→11): 여호수아의 마지막 말(수 24) → 다른 세대(삿 2:10) → 하늘의 어둠(2:11) → 사사들(2:16) → 철 병거(4:3) → 드보라(4:4–6) → 다볼 산(4:7–10)
    scene("s11a", "at Shechem under a great old oak tree beside a big standing stone, old Joshua, the leader of Israel, a very old man with a long white beard and white hair in a simple cream robe, stands on a low rock and speaks to the whole people of Israel gathered on the slope before him; right beside Joshua stand his own family, his gray-haired wife, his grown sons and two small grandchildren, holding hands; Joshua lays one hand on his chest; the people listen; warm late-afternoon light, solemn and hopeful."),
    scene("s11b", "beside a low pile of twelve big smooth river stones in an open field near Gilgal, a gray-bearded old Israelite man points at the stones and tells a story with a happy face, but the young Israelite men and women around him have turned their backs to him and walk away chatting and looking at the busy town in the distance; only the old man faces the stones; quiet sad mood, warm afternoon light, child-friendly."),
    scene("s11c", f"an Israelite village of flat-roofed houses on a hillside; on a small hilltop a simple plain stone altar stands alone, forgotten, with no smoke and weeds around it; the villagers walk away from the altar with their backs turned to it; above the village the sky turns gloomy and many {WISPS}, pour down across the sky toward the houses; no statues, no idols, no figures of gods anywhere; eerie but child-friendly."),
    scene("s11d", "Othniel, a young Israelite judge with a short brown beard, a simple tan tunic and a leather belt, holding a plain wooden staff, stands on a small hill with a bright golden light shining from the parted clouds behind him; below him tired Israelite men, women and children who had been crying out lift their faces and hands toward the light with hope; the dark wisps in the sky flee away; hopeful warm light."),
    scene("s11e", f"a wide flat plain under a heavy gray sky, with long rows of {CHARIOTS}, lined up in a menacing army; {CANAAN}, stand in them; in the foreground, on a narrow hidden footpath behind bushes and rocks, a worried Israelite family with a little donkey walks quietly, hiding from the big empty main road; tense but child-friendly."),
    scene("s11f", f"under a tall date palm tree in the hill country, {DEBORAH}, sits on a simple stone seat and speaks with wise authority, raising her right hand; before her stands {BARAK}, listening carefully with a serious face; a few Israelites wait nearby to bring their questions to her; warm morning light, calm and dignified."),
    scene("s11g", f"on the broad green summit of {TABOR}, {DEBORAH}, stands beside {BARAK}, and points down to the plain with her right hand; around and behind them stand many {ISRAEL}, ten thousand of them filling the mountain top; far below on the wide plain, many tiny dark iron chariots gather beside a winding river; clear morning light, brave and hopeful."),
    # 승리 만화: 하늘이 물을 내리고(5:4) → 기손 강이 휩쓸다(5:21) → 해가 힘 있게 돋음 같게(5:31). 다친 사람, 물에 빠진 사람은 그리지 않는다. 하나님은 비·구름·빛으로만
    scene("v11a", f"a fierce rainstorm pours down from dark clouds over a wide muddy plain; {CHARIOTS}, are stuck deep in thick brown mud with their wheels sunk up to the axles and the horses straining; the charioteers in colorful tunics and bronze helmets climb down from their stuck chariots and run away on foot through the rain; nobody is hurt; in the background {ISRAEL}, come down the slope of {TABOR}; small dark wisps flee up into the sky."),
    scene("v11b", "the old river Kishon has risen into a wide rushing flood of brown water under a stormy sky that is beginning to clear; the flood sweeps away many empty dark iron chariots and loose chariot wheels downstream; there are no people and no horses in the water at all; far away on the dry bank, tiny figures run away; bright rays of light break through the clouds onto the river."),
    scene("v11c", f"a fresh clear morning after the storm: a bright golden sun rises powerfully over {TABOR}; in a green meadow {DEBORAH}, and {BARAK}, sing joyfully together with the people of Israel, men, women and children; women play round hand drums and children dance; glistening wet grass and a calm river behind them; joyful peaceful light."),
    # 새 적과 인물
    {"id": "c_chariot", "종류": "인물", "시드": [1, 2], "프롬프트": "A Canaanite iron war chariot of King Jabin of Hazor: a heavy two-wheeled chariot of dark wood plated with black iron, with iron-rimmed spoked wheels, pulled by two dark brown horses with red plumes, galloping, side view facing right, one charioteer with curly black hair and a short beard, a rounded bronze helmet and a colorful patterned wool tunic holding the reins, proud stern face. The whole chariot and both horses fully visible."},
    {"id": "c_chariot_empty", "종류": "물건", "시드": [1, 2], "프롬프트": "An empty abandoned Canaanite war chariot of dark wood plated with black iron, tilted to one side with its two iron-rimmed spoked wheels sunk deep in a small patch of thick brown mud, no horses, no people, side view facing right."},
    {"id": "c_drummer", "종류": "인물", "시드": [1, 2], "프롬프트": "A Canaanite war drummer of Hazor, a stocky man with curly black hair and a short beard, a rounded bronze helmet, a colorful patterned wool tunic wrapped over one shoulder and a leather belt, a big round frame drum of stretched hide hanging in front of his belly from a strap over his shoulder, beating the drum with two short wooden drumsticks, mouth open shouting, wide fearful eyes, exactly two arms."},
    {"id": "whisper", "종류": "정령", "시드": [1, 2, 3], "프롬프트": "A tiny flying whisper spirit: a small round puff of dark purple and indigo smoke with two big glowing lilac eyes and a sly little whispering mouth, a thin curly smoke tail like a little serpent, two small wispy smoke fins instead of wings, no horns, no arms, no legs, cute but eerie."},
    {"id": "deborah", "종류": "인물", "시드": [1, 2, 3], "프롬프트": DEBORAH + ", standing and raising her right arm to point forward with her index finger, her left hand resting at her side, calm brave face, exactly two arms and exactly two hands."},
    {"id": "barak", "종류": "인물", "시드": [1, 2], "프롬프트": BARAK + " upright in his right hand and a round wooden shield on his left arm, determined brave face, exactly two arms."},
    # 숨은 이야기: 흰 나귀(삿 5:10)
    {"id": "e_donkey", "종류": "인물", "시드": [1, 2], "프롬프트": "A gentle white donkey with long ears, a soft gray muzzle and dark kind eyes, a colorful woven saddle rug on its back, standing calmly, side view facing right."},
]
items = [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면' and i['id'] != 'bg11w'] + items[:1]   # 게임에 바로 쓰는 인물·물건 먼저, 참조가 있는 배경은 마지막에
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림11.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 둘째 작업(새그림11b.json): 빈 병거가 바퀴 넷 달린 수레로 나와서(병거는 바퀴가 둘), 드보라가 너무 젊게 나와서(10-13, "이스라엘의 어머니" 삿 5:7) 다시 그린다
items2 = [
    {"id": "c_chariot_empty", "종류": "물건", "시드": [3, 4], "프롬프트": "An empty abandoned two-wheeled Canaanite war chariot: a small open-backed cab of dark wood plated with black iron standing on one single axle with exactly two large iron-rimmed spoked wheels, one wheel on each side, its long wooden shaft pole lying on the ground in front, tilted to one side with both wheels sunk in a small patch of thick brown mud, no horses, no people, side view facing right."},
    {"id": "deborah", "종류": "인물", "시드": [4, 5, 6], "프롬프트": "Deborah, the prophetess and judge of Israel, a wise motherly Israelite woman of about sixty with gray hair, a few gentle wrinkles and a calm brave face, under a long cream-and-blue headscarf, wearing a deep blue wool robe with an ochre sash, standing and raising her right arm to point forward with her index finger, her left hand resting at her side, exactly two arms and exactly two hands."},
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items2}, open('새그림11b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 셋째 작업(새그림11c.json): v11a 시드 1·2는 이스라엘 군사가 병거로 곧장 달려드는 싸움 장면이 되어서(10-13), 진흙에 빠진 병거와 내려서 달아나는 병사만 앞에 두고 이스라엘은 멀리 산비탈에 둔다
items3 = [
    scene("v11a", f"a fierce rainstorm pours down from dark clouds over a wide muddy plain; in the foreground, several heavy two-wheeled Canaanite war chariots of dark wood plated with black iron are stuck deep in thick brown mud, their two wheels sunk up to the axle, the dark brown horses standing still and tired; the charioteers in colorful tunics and bronze helmets have climbed down from their stuck chariots and run away on foot to the left through the rain, seen from behind, nobody is hurt; far away in the background, tiny Israelite soldiers come down the green slope of {TABOR}; nobody is fighting; small dark wisps flee up into the sky.", (3, 4, 5)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items3}, open('새그림11c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
