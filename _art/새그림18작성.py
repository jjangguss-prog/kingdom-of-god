# 18 도단 그림 작업 파일(새그림18.json) 만들기 v0.1 (2026-10-18)
# 사용: python 새그림18작성.py → 새그림18.json. 그린 뒤 고르기_18.json으로 모은다.
# 배경(bg18)은 ref2/ref18.png(길 시안)를 참조로 그린다. 아람(r_)은 남청색 겉옷에 붉은 술띠, 끈으로 묶은 붉은 머리띠와 둥근 가죽 방패. 림몬 같은 신의 상징은 그리지 않는다.
# 고르는 기준(10-16 사용자): 인물마다 확대해 이목구비가 뚜렷한가와 팔이 정상인가. 하나라도 어긋나면 다시 그린다.
# 사람마다 손이 어디 있는지 정해 준다(s18a 뻗은 두 손, s18b 겉옷을 쥔 두 손, s18c 아이를 안은 두 팔, s18d 가리키는 손과 바구니, s18e 모은 손과 감싼 팔, s18f 자루와 가리키는 손, s18g 가리키는 손, v18a 가리키는 손과 어깨의 손, v18b 칼자루와 편 손바닥, v18c 떡과 물동이).
# 하나님은 빛·구름·불로만. 불말과 불병거는 탄 이 없이 불로 된 말과 수레로만. 죽은 아이와 나병은 그리지 않는다.
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
FACE = " Every face is clear and well drawn with distinct eyes, nose and mouth."
HANDS = " Hands are drawn simply and clearly, each hand with four fingers and a thumb, and no hand overlaps another person."
NOIDOL = " No statues, no idols, no carved figures, no calves, no crescent shapes, no moon ornaments, no religious symbols anywhere."
NOBLOOD = " Nobody is wounded, no blood, nobody lying dead."
FLAT = " All houses are one-story mud-brick or stone houses with flat earthen rooftops and low parapets; no sloped roofs, no roof tiles, no red tiles."
ELISHA = "Elisha the prophet, an Israelite man of about forty with a short black beard, a plain white cloth covering his head, wearing a rough brown hairy cloak over a cream tunic with a leather belt"
ELIJAH = "Elijah the prophet, an old Israelite man with a long white beard and long white hair, wearing a rough hairy brown cloak tied with a leather belt"
SERVANT = "Elisha's servant, a young Israelite man of about eighteen, clean-shaven, with short curly black hair, wearing a plain light-blue tunic with a rope belt"
KING = "the king of Israel, a man of about thirty-five with a short black beard, a simple gold crown, a dark red royal robe with gold trim and a sword in a sheath at his belt"
DISCIPLES = "young men who are disciples of the prophets, in plain brown and grey wool tunics with short beards"
ARAM = ("an Aramean warrior from Damascus, a man with a black beard, wearing a dark navy-blue knee-length tunic with a red tasseled sash, "
        "a red cloth headband tied with cords around his black hair, leather sandals")
FIRE = "horses and chariots made entirely of bright living fire and golden light, with no riders, no drivers and no people in them"
LIGHT = "a soft beam of white-gold light from heaven shines down, with no figure and no face in the light"


def scene(i, pr, seeds=(1, 2, 3)):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + HANDS + FACE + END}


def man(i, pr, seeds=(1, 2, 3), kind="인물"):
    return {"id": i, "종류": kind, "시드": list(seeds), "프롬프트": pr}


items = [
    {"id": "bg18", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3], "참조": ["ref2/ref18.png"],
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield in the green Dothan valley of ancient Israel in bright daylight, seen from above at a slight angle. "
                 "Keep exactly the same sandy road shapes and positions. In the very middle, the small round mound is a low round hill (a tell) with a walled little town on top: a ring of mud-brick town walls with three small dark gateways, one gateway at the end of each of the three wide roads (north gate at the top, west gate at the left, east gate at the right), "
                 "and inside the walls a cluster of small flat-roofed mud-brick houses with one house in the very center that has an outside staircase. "
                 "The three wide roads each end at their own town gate and do not join each other: one road comes down from the top edge and loops around to the north gate; one road comes from the right edge, crosses a shallow ford of the river and winds through the valley floor up to the east gate; one road comes from the left edge, curves around hills and reaches the west gate. "
                 "The narrow pale path goes from the south side of the town down to the lower left corner, where the edge of a bigger walled city with a stone wall and a gate stands on a hill. "
                 "The light green patch beside the narrow path is a low soft grassy meadow. The dark brown blobs are low rounded hills with olive trees and rocks. The blue strip on the right edge is the Jordan river with reeds along its banks, and the small green spot is a reedy bank by the water. "
                 "Elsewhere: green and golden fields, olive trees, small bushes and stones. Nothing covers the roads. No characters, no people, no text." + FLAT + NOIDOL},
    # 이야기(17→18): 불수레와 불말(왕하 2:11) → 엘리야의 하나님 여호와는 어디(2:14) → 네 아들을 데리고 가라(4:36) → 먹고 남으리라(4:43) → 사마리아에 계신 선지자 앞에(5:3) → 쇠도끼가 떠오르고(6:6) → 그가 도단에 있도다(6:13)
    scene("s18a", f"at sunset in the open plain east of the Jordan, a great whirlwind of golden light lifts {ELIJAH}, up into the glowing sky; between the two men a chariot and horses made entirely of bright fire race across, with no rider and no driver; below on the ground {ELISHA}, stands and reaches up toward the sky with both arms stretched upward, amazed; Elijah's brown cloak flutters down through the air toward Elisha; dramatic orange and gold clouds." + NOIDOL),
    scene("s18b", f"on the bank of the Jordan river among reeds, {ELISHA}, holds a rolled-up brown hairy cloak in both hands and strikes the water with it; the river water parts to the left and to the right, opening a dry path across the riverbed; far away on the other bank a small group of {DISCIPLES}, watch amazed; bright afternoon light." + NOIDOL),
    scene("s18c", f"inside a small upper room on a flat roof with a simple wooden bed, a small table, a stool and an oil lamp on a stand; a joyful Israelite mother in a dark green dress and a white headscarf hugs her little son of about six in both arms; the boy is awake with open eyes, smiling and looking at his mother; on the right {ELISHA}, stands beside them and smiles warmly with his hands folded in front of him; warm daylight from a small window. Only these three people." + NOBLOOD),
    scene("s18d", f"during a famine at Gilgal under a dry tree, {ELISHA}, stands and points with his right hand toward a group of {DISCIPLES}, sitting on the ground in a row; beside Elisha {SERVANT}, holds a big woven basket of twenty small round barley loaves in both arms and looks unsure; a farmer in a plain tunic who brought the bread stands behind them; dry brown hills, warm light." + NOIDOL),
    scene("s18e", f"in the courtyard of a rich house in Damascus with blue tiles and a fountain, a little Israelite girl of about ten in a plain beige dress and a small headscarf folds her hands together and speaks earnestly to a kind noblewoman in a rich purple dress and gold earrings, who bends down and listens; in the doorway behind them stands Naaman, a tall Aramean army commander with a black beard, bronze scale armor and a red cloak, his left forearm wrapped in white cloth, looking thoughtful. Only these three people." + NOIDOL),
    scene("s18f", f"on the bank of the Jordan river where {DISCIPLES}, have been cutting trees; in the front one young man holds an empty wooden axe handle in his left hand and points at the water with his right hand, surprised; {ELISHA}, stands beside him and has just thrown a small stick into the water; an iron axe head floats up on the surface of the water next to the stick; logs and tree stumps on the bank, bright morning light." + NOIDOL),
    scene("s18g", f"at night inside the tent of the king of Aram, lit by an oil lamp: the king of Aram, an angry man with a black curled beard, a tall red cap and a navy-blue royal robe, rises from his seat in front of a wooden table with a rough painted map; an Aramean officer in a navy-blue tunic and red headband points toward the tent door with his right hand; through the open tent door, under the moonlight, Aramean horses, chariots and soldiers set out on a road; only two people inside the tent." + NOIDOL),
    # 승리 그림 만화(셋): 불말과 불병거가 산에 가득하여(6:17) → 치지 마소서(6:22) → 음식을 많이 베풀고(6:23). 해치는 장면은 그리지 않는다
    scene("v18a", f"at dawn on top of the mud-brick wall of the little town of Dothan, {SERVANT}, stares with wide astonished eyes and points with his right hand at the hills; beside him {ELISHA}, rests his left hand on the servant's shoulder and raises his right hand calmly; below in the valley the tents and chariots of the Aramean army surround the town; and all over the surrounding hills, many {FIRE}, fill the mountains in a great ring, glowing in the pink morning sky." + NOIDOL + NOBLOOD),
    scene("v18b", f"in the stone square inside the city of Samaria, a group of Aramean soldiers in navy-blue tunics with red headbands, without weapons, look around in surprise as if just waking up; on the left {KING}, grips the hilt of his sheathed sword with his right hand and looks at them; in the middle {ELISHA}, stands between the king and the soldiers and holds up his open right palm toward the king to stop him, with a kind firm face; city walls and flat-roofed houses behind." + NOIDOL + NOBLOOD),
    scene("v18c", f"a great feast outside the city gate of Samaria in the late afternoon: long low wooden tables on the grass covered with round loaves of bread and clay cups; Aramean soldiers in navy-blue tunics and red headbands, without any weapons, sit and eat bread and drink with calm happy faces; in the front an Israelite woman in a green dress pours water from a clay jar held in both hands into a soldier's cup, and an Israelite man hands round loaves from a basket; {ELISHA}, stands and smiles; far away a line of men walks home along a hill road under the golden sunset." + NOIDOL + NOBLOOD),
    # 아람 일곱(r_): 이스라엘의 친척 겨레라 존엄하게
    man("r_soldier", ARAM + ", holding a long spear in his right hand and a round leather shield on his left arm, angry frown, walking forward, exactly two arms and exactly two hands." + NOIDOL),
    man("r_raider", ARAM + ", a lightly dressed fast raider without armor, holding a short curved sword in his right hand, running forward eagerly with a greedy grin, exactly two arms and exactly two hands." + NOIDOL),
    man("r_shield", ARAM + ", a big heavy shield bearer with a bronze scale vest over the tunic, holding a tall round-topped wooden shield covered with leather and bronze studs in his left hand and a short spear in his right hand, proud chin up, exactly two arms and exactly two hands." + NOIDOL),
    man("r_centurion", ARAM + ", a stern captain with a grey-streaked beard, a pointed bronze helmet and a bronze scale armor shirt and a long red cloak, holding a sword in his right hand and pointing forward commandingly with his left hand, hard proud face, exactly two arms and exactly two hands." + NOIDOL),
    man("r_archer", ARAM + ", a lean young archer with a leather quiver of arrows on his back, drawing a curved wooden bow with an arrow aimed forward, narrowed eyes, exactly two arms and exactly two hands." + NOIDOL),
    man("r_drummer", ARAM + ", without weapons, beating a round wooden frame drum hanging at his waist with both hands, wide fearful eyes, exactly two arms and exactly two hands." + NOIDOL),
    man("r_chariot", "An Aramean war chariot of Damascus: a two-wheeled chariot of dark wood with navy-blue and red painted trim and six-spoked wheels, pulled by two brown horses with red plumes, galloping, side view facing right, one charioteer with a black beard, a red headband and a navy-blue tunic holding the reins and a spear, proud stern face. The whole chariot and both horses fully visible." + NOIDOL),
    # 앉은 아람 사람(6:22): 무기를 내려놓고 평온한 얼굴로 들에 앉아 기다림
    man("r_sit", "An Aramean man from Damascus with a black beard, a dark navy-blue tunic with a red sash and a red cloth headband, sitting cross-legged on the ground with no weapons, his hands resting on his knees, calm peaceful face, side view facing right, exactly two arms and exactly two hands."),
    man("r_sit2", "A young Aramean man from Damascus with a short black beard, a dark navy-blue tunic with a red sash and a red cloth headband, sitting on the ground with his knees up and his arms resting around his knees, no weapons, gentle relieved face, side view facing right, exactly two arms and exactly two hands."),
    # 공성 망치(창 6:11): 겨레 없는 그림. 바퀴 달린 나무 틀에 가죽 지붕과 쇠머리 들보, 지붕 아래로 미는 사람 넷의 다리만
    man("ram", "A wooden battering ram siege engine: a long low wooden frame on four solid wooden wheels, covered by a sloped roof of brown animal hides, with a heavy wooden beam ending in a dark iron ram head hanging on ropes under the roof and pulled back; under the roof only the legs and sandals of four men pushing are visible; a thin smoky lavender mist curls above the roof, side view facing right. The whole machine fully visible. No faces, no text.", seeds=(1, 2, 3, 4), kind="물건"),
    man("ram_swing", "A wooden battering ram siege engine: a long low wooden frame on four solid wooden wheels, covered by a sloped roof of brown animal hides, with a heavy wooden beam ending in a dark iron ram head hanging on ropes under the roof and swung far forward, sticking out in front of the frame; under the roof only the legs and sandals of four men pushing are visible; a thin smoky lavender mist curls above the roof, side view facing right. The whole machine fully visible. No faces, no text.", seeds=(1, 2, 3, 4), kind="물건"),
    # 엘리사 셋, 사환 둘, 이스라엘 왕
    man("elisha", ELISHA + ", standing calmly with a wooden staff in his right hand and his left hand open at his side, kind brave face, exactly two arms and exactly two hands."),
    man("elisha_pray", ELISHA + ", praying with both hands raised high toward the sky with open palms, face lifted up, eyes closed, exactly two arms and exactly two hands."),
    man("elisha_lead", ELISHA + ", walking forward and beckoning with his right hand raised and waving people to follow, his left hand holding a wooden staff, kind smile, exactly two arms and exactly two hands."),
    man("servant", SERVANT + ", frightened, holding his head with both hands on the sides of his head, mouth open, wide scared eyes, exactly two arms and exactly two hands."),
    man("servant_see", SERVANT + ", amazed and full of wonder, pointing forward and up with his right arm outstretched, his left hand on his chest, wide shining eyes and an open smile, exactly two arms and exactly two hands."),
    man("king_israel", KING + ", standing tall with his right hand resting on the hilt of his sheathed sword, his left hand at his side, stern uncertain face, exactly two arms and exactly two hands." + NOIDOL),
    # 상을 차리는 이스라엘 사람(6:22): 떡 바구니, 물동이
    man("p_server", "An Israelite man with a short brown beard in a plain tan tunic and a white headcloth, walking forward and carrying a big woven basket full of round loaves of bread in both arms, friendly smile, exactly two arms and exactly two hands."),
    man("p_server2", "An Israelite woman in a dark green dress and a white headscarf, walking forward and carrying a big clay water jar on her left shoulder, holding it with her left hand, her right hand holding a small clay cup, friendly smile, exactly two arms and exactly two hands."),
    # 불말과 불병거(6:17): 탄 이 없이 불로 된 말과 수레
    man("firehorse", "A galloping horse made entirely of bright living flames and golden light, with a flowing mane of fire and glowing hooves, no rider, no saddle, no person, side view facing right. Isolated on a plain pure white background.", seeds=(1, 2, 3, 4), kind="정령"),
    man("firechariot", "A two-wheeled chariot made entirely of bright living fire and golden light with fiery spoked wheels, pulled by two galloping horses made of flames, completely empty with no rider, no driver, no person in it, side view facing right. Isolated on a plain pure white background.", seeds=(1, 2, 3, 4), kind="정령"),
    # 숨은 이야기: 나아만이 일곱 번 씻었다(왕하 5:14). 나병은 감싼 천으로만
    man("e_naaman", "Naaman, a tall Aramean army commander with a black beard, wearing only a plain knee-length white linen tunic with a red sash and a red headband, his left forearm wrapped in white cloth bandages, standing in shallow river water up to his knees and looking around unsure, exactly two arms and exactly two hands." + NOIDOL),
    man("e_naaman_clean", "Naaman, a tall Aramean army commander with a black beard, wearing a plain knee-length white linen tunic with a red sash and a red headband, standing in shallow river water up to his knees and raising both bare clean arms high in joy, laughing with a happy face, a loose white cloth floating away on the water, exactly two arms and exactly two hands." + NOIDOL),
]
items = items[:1] + [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면' and i['id'] != 'bg18']   # 배경을 먼저(길과 탑 자리를 그림에 맞춰야 해서)
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림18.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 18b(10-18): 사람과 손이 어긋난 것을 다시 그린다 — 새그림18b.json
#   s18f: 시드 1은 젊은이 다리 하나가 투명하게 지워지고, 시드 2는 젊은이 왼쪽에 손이 하나 더, 시드 3은 얼굴이 뒤로 돌아감 → 수염 난 젊은 어른 하나만 앞에, 빈 자루를 쥐고 물을 가리킴
#   v18a: 시드 1은 사환과 엘리사가 한 사람으로 합쳐지고, 시드 2·3은 엘리사 어깨에 주인 없는 손 → 둘이 닿지 않게, 엘리사는 두 손을 들고 기도
#   v18b: 아람 군사가 모두 아이처럼 나오고 시드 3은 관 쓴 사람이 둘 → 수염 난 어른 군사, 관은 왕 하나만
#   r_walk: 풀려나 무기 없이 들로 걷는 아람 사람(새로)
YOUNG = "a young Israelite man of about twenty with a short black beard and a plain grey tunic with a brown belt"
items_b = [
    scene("s18f", f"on the bank of the Jordan river beside logs and tree stumps, only two people in front: {YOUNG}, stands on the bank holding an empty wooden axe handle with no blade in his left hand and pointing down at the water with his right hand, surprised; beside him {ELISHA}, has just thrown a small stick into the water and watches calmly with both hands open at his sides; on the water surface next to the floating stick, a dark iron axe head without a handle floats up; far behind them two other disciples carry logs on their shoulders, small; bright morning light." + NOIDOL, seeds=(11, 12, 13, 14)),
    scene("v18a", f"at dawn on top of the mud-brick wall of the little town of Dothan, only two people standing apart and not touching each other: on the left {SERVANT}, a grown young man with a thin beginning beard, stares with wide astonished eyes and points with his right arm at the hills, his left hand on his chest; on the right {ELISHA}, raises both hands up in prayer with a calm face; below in the valley the tents and chariots of the Aramean army surround the town; all over the surrounding hills many {FIRE}, glow in a great ring under the pink morning sky. No sloped roofs, no red tiles." + NOIDOL + NOBLOOD, seeds=(11, 12, 13, 14)),
    scene("v18b", f"in the stone square inside the city of Samaria: on the right a group of grown-up bearded Aramean soldiers, adult men with black beards in navy-blue tunics and red headbands, without weapons, look around in surprise; on the left {KING}, the only person wearing a crown, grips the hilt of his sheathed sword at his belt with his right hand; in the middle {ELISHA}, stands between them and holds up his open right palm toward the king to stop him, his left hand at his side, kind firm face; flat-roofed stone houses behind. Only one crown in the picture. No writing anywhere." + NOIDOL + NOBLOOD, seeds=(11, 12, 13, 14)),
    man("r_walk", "An Aramean man from Damascus with a black beard, a dark navy-blue knee-length tunic with a red tasseled sash and a red cloth headband, walking forward calmly with no weapons and empty open hands relaxed at his sides, gentle relieved face, exactly two arms and exactly two hands."),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_b}, open('새그림18b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_b), '항목(18b)', sum(len(i['시드']) for i in items_b), '장')

# 18c(10-18 삽화 검토): s18d는 사환 뒤로 주인 없는 다리와 신발이 하나 더, s18f(14)는 도끼날이 자루에 붙은 채라 이야기(날 빠진 자루)와 어긋남 — 새그림18c.json
items_c = [
    scene("s18d", f"during a famine at Gilgal under a dry tree: on the left {ELISHA}, stands and points with his right hand toward a row of five {DISCIPLES}, sitting cross-legged on the ground in front of him; on the right, standing apart with empty space around him, {SERVANT}, holds a big woven basket of twenty small round barley loaves in both arms and looks unsure; only these people, nobody standing behind the servant; dry brown hills, warm light." + NOIDOL, seeds=(21, 22, 23, 24)),
    scene("s18f", f"on the bank of the Jordan river beside logs and tree stumps, only two people in front: {YOUNG}, stands on the bank holding in his left hand a plain wooden stick-like axe handle whose end is empty and broken with NO blade on it, and pointing down at the water with his right hand, surprised; beside him {ELISHA}, has just thrown a small twig into the water and watches calmly; on the water surface beside the floating twig, a separate dark iron axe head with no handle floats up; two other disciples carry logs far behind, small; bright morning light." + NOIDOL, seeds=(21, 22, 23, 24)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_c}, open('새그림18c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_c), '항목(18c)', sum(len(i['시드']) for i in items_c), '장')
