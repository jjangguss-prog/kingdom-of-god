# 17 브라가 골짜기 그림 작업 파일(새그림17.json) 만들기 v0.1 (2026-10-17)
# 사용: python 새그림17작성.py → 새그림17.json. 그린 뒤 고르기_17.json으로 모은다.
# 배경(bg17)은 ref2/ref17.png(길 시안)를 참조로 그린다. 세 겨레는 겉모습 둘: 암몬·모압(j_, 쪽빛과 샛노랑, 둥근 천 모자)과 세일 산(d_, 붉은 황토색 겉옷과 가죽 두건).
# 고르는 기준(10-16 사용자): 인물마다 확대해 이목구비가 뚜렷한가와 팔이 정상인가. 하나라도 어긋나면 다시 그린다.
# 사람마다 손이 어디 있는지 정해 준다(s17b 가리키는 손과 얼굴을 묻은 손, s17c 악기, s17d 찢은 옷 조각, s17e 든 두 손, s17f 철 뿔, s17g 든 두 손과 아이를 안은 팔, v17a 악기, v17b 꾸러미, v17c 든 손).
# 하나님은 빛·구름·불로만(s17a 장막 위의 빛, s17c 구름, s17e 불, v17c 빛). 금송아지·바알 상징·그모스·밀곰 상징은 그리지 않는다.
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
FACE = " Every face is clear and well drawn with distinct eyes, nose and mouth."
HANDS = " Hands are drawn simply and clearly, each hand with four fingers and a thumb, and no hand overlaps another person."
NOIDOL = " No statues, no idols, no carved figures, no calves, no crescent shapes, no moon ornaments, no religious symbols anywhere."
NOBLOOD = " Nobody is wounded, no blood, nobody lying dead."
FLAT = " All houses are one-story mud-brick or stone houses with flat earthen rooftops and low parapets; no sloped roofs, no roof tiles, no red tiles."
DAVID = "King David, a ruddy Israelite man of about forty with reddish-brown hair and a neat reddish-brown beard, wearing a simple gold crown band and a deep red royal robe with gold trim"
NATHAN = "Nathan the prophet, an old Israelite man with a long white beard, wearing a plain grey-brown wool robe and a cream headcloth"
AHIJAH = "Ahijah the prophet, an old Israelite man with a long grey beard and a cream headcloth"
JEROBOAM = "Jeroboam, a strong young Israelite man with short black hair and a short black beard, wearing a plain brown work tunic with a leather belt"
ELIJAH = "Elijah the prophet, a lean weathered Israelite man with long wild dark hair and a dark beard, wearing a rough hairy brown cloak tied with a leather belt"
AHAB = "King Ahab of Israel, a proud man with a black beard, a tall gold crown and a rich purple robe"
JEHOSHAPHAT = "King Jehoshaphat of Judah, a dignified Israelite man of about forty-five with a neat dark-brown beard, a simple gold crown band and a deep blue royal robe with gold trim over a white tunic"
MICAIAH = "Micaiah the prophet, a calm middle-aged Israelite man with a short brown beard, wearing a plain undyed wool robe"
SINGERS = "Levite singers in long white linen robes with golden sashes and white headcloths"
LIGHT = "a soft beam of white-gold light from heaven shines down, with no figure and no face in the light"
MOAB = ("a warrior of Moab and Ammon from the land east of the Jordan, a man with a thick curly black beard, wearing a rounded indigo-blue felt cap wrapped with a saffron-yellow cloth band, "
        "a knee-length indigo-blue tunic with a saffron-yellow border and a wide leather belt, and sandals")
SEIR = ("a warrior of Mount Seir (Edom), a rugged mountain man with a reddish-brown beard, wearing a brown leather hood wrapped around his head, "
        "a rough red-ochre wool cloak over a short tan tunic, leather leg wraps and sandals")


def scene(i, pr, seeds=(1, 2, 3)):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + HANDS + FACE + END}


items = [
    {"id": "bg17", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3], "참조": ["ref2/ref17.png"],
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield in the pale chalky Judean wilderness near Tekoa in bright early morning light, seen from above at a slight angle. "
                 "Keep exactly the same sandy road shapes and positions: one road comes up from the bottom edge on the lower right, climbs a steep rocky cliff in two tight zigzag hairpin turns, then crosses the plateau to the middle; "
                 "another road enters from the right edge near the top and winds left through dry rolling hills to the middle; the two roads meet in the middle and continue left as one road to a camp on the left. "
                 "Bottom right corner: the blue area is the still blue water of the Dead Sea with a pale salty shore, and the small green spot is a little oasis of date palm trees at a spring. "
                 "The big darker brown area around the zigzag road is a steep layered limestone cliff face with ledges. "
                 "Middle: in the narrow wedge of land between the two roads just before they meet, the dark spot is a small rocky knoll with a round watchtower of rough stacked stones on it, and the pale spot to its left is an empty flat rock ledge with nothing on it. "
                 "Left: the camp of Judah, rows of small tan cloth tents around a cleared pale area at the end of the road. "
                 "Upper left: a small hilltop town of flat-roofed stone houses. Lower left: the greenish area is a shallow green valley with grass and a few olive trees. "
                 "Upper middle: the small spot is a tiny stone hut with a clay jar by its door. "
                 "Elsewhere: pale dry hills, rocks, small thorn bushes and dry gullies. Nothing covers the roads. No characters, no people, no text." + FLAT + NOIDOL},
    # 이야기(16→17): 네 왕위가 영원히 견고하리라(삼하 7:16) → 내가 여호와께 죄를 범하였노라(12:13, 시 51) → 그의 자비하심이 영원히 있도다(대하 5:13) → 열두 조각(왕상 11:31) → 여호와 그는 하나님이시로다(18:39) → 내 하나님께서 말씀하시는 것(대하 18:13) → 오직 주만 바라보나이다(20:12)
    scene("s17a", f"at night in the courtyard of a cedar-wood palace in Jerusalem under a starry sky, {DAVID}, kneels on one knee with his hands folded at his chest, looking up with wonder toward a simple tent of plain woven curtains on the right; {NATHAN}, stands beside David and speaks kindly with his right hand raised and his left hand holding a wooden staff; {LIGHT} onto the curtained tent; peaceful holy night." + FLAT + NOIDOL),
    scene("s17b", f"inside a royal room of a palace with a window, {NATHAN}, stands on the left and points at the king with his right arm outstretched and his index finger extended, his left hand holding a wooden staff, with a sad serious face; on the right {DAVID}, kneels on the floor with his gold crown band taken off and lying on the floor beside him, his face buried in both hands, weeping in sorrow; a small harp leans against the wall; grey cloudy light from the window. Only these two people in the room." + NOBLOOD),
    scene("s17c", f"the dedication of the great stone temple in Jerusalem on a bright day: in front of the temple, {SINGERS}, stand on the east side of a big bronze altar; in the front, four people large: a singer singing with his face raised and his hands open, a second singer playing bronze cymbals held one in each hand, a priest in white blowing a long silver trumpet held with both hands, and a musician playing a wooden harp; "
                  "a shining white-gold cloud pours out of the open temple doors and fills the courtyard with glory; a large crowd of worshippers small and far away." + NOIDOL),
    scene("s17d", f"on a lonely road in the open countryside with only two people: {AHIJAH}, holds up in both hands a new pale blue cloak that he has torn into twelve pieces, and holds out a bundle of ten of the torn pieces toward {JEROBOAM}, who stands in front of him and reaches out with both hands to receive them in amazement; wheat fields and hills behind them, bright midday light." + NOIDOL),
    scene("s17e", f"on the top of Mount Carmel, {ELIJAH}, stands beside a stone altar built of twelve rough stones with a water-filled trench around it and a pile of wood and an offering on top, raising both arms high toward the sky; a great column of fire falls from the sky onto the altar and the water in the trench is boiling away in steam, with no figure in the fire; "
                  "behind Elijah a crowd of Israelite people bow down with their faces to the ground; far away on the left a small group of men in plain robes stand amazed; dramatic evening sky." + NOIDOL + NOBLOOD),
    scene("s17f", f"in the wide open square at the gate of the stone city of Samaria, two kings sit on two thrones side by side: on the left {AHAB}, and on the right {JEHOSHAPHAT}, looking uneasy; in front of them a crowd of court prophets in colorful robes raise their hands and shout; one prophet in front holds a pair of iron horns against his head with both hands; "
                  f"on the right, alone and apart, {MICAIAH}, stands calmly with his hands at his sides and looks straight at the two kings with a brave honest face." + NOIDOL),
    scene("s17g", f"in the new courtyard of the stone temple in Jerusalem, {JEHOSHAPHAT}, stands on a low stone step in front of the crowd and prays with both hands raised high toward heaven, his face lifted up; behind him the people of Judah stand quietly in prayer with their wives, children and little ones: in the front a young mother in a green dress and white headscarf holds a baby in her arms, and a small boy holds his father's hand; many more families small and far away; soft hopeful light." + NOIDOL),
    # 승리 그림 만화(셋): 군대 앞에서 행진하며(20:21) → 사흘 동안에 거두어들이고(20:25) → 브라가 골짜기(20:26). 해치는 장면은 그리지 않는다
    scene("v17a", f"early morning in the pale hills of the wilderness of Tekoa, {SINGERS}, walk at the very front of an army, singing joyfully with their faces raised: the singer in front plays a wooden lyre held against his chest, the next one plays bronze cymbals held one in each hand; behind them {JEHOSHAPHAT}, walks with a calm face, followed by long ranks of Judah's soldiers with round shields and upright spears; the golden morning sun rises over the far eastern hills." + NOIDOL + NOBLOOD),
    scene("v17b", f"beside a round stone watchtower on a hill in the wilderness, people of Judah look down into a wide dry valley that is strewn with abandoned spears, round shields, sacks, bundles of colorful cloth, clay jars and small chests of treasure; there are no people lying anywhere in the valley; in the front, two Judean men carry big bundles on their backs, and one smiling young man holds a huge heap of cloth bundles in both arms, laughing; bright midday light." + NOBLOOD + NOIDOL),
    scene("v17c", f"on the fourth day in a shallow green valley with grass and olive trees, a great joyful crowd of the people of Judah gather and lift their hands to praise God; in the front {JEHOSHAPHAT}, raises both hands with a joyful face, a Levite in a white linen robe plays a wooden harp, and a little girl lifts her hands and smiles; behind them priests blow long silver trumpets; {LIGHT} onto the valley." + NOIDOL + NOBLOOD),
    # 세 겨레: 암몬·모압(j_)과 세일 산(d_). 친척 민족이라 존엄하게, 신의 상징 없이
    {"id": "j_soldier", "종류": "인물", "시드": [1, 2, 3], "프롬프트": MOAB + ", holding a long spear in his right hand and a small round wooden shield on his left arm, angry frown, walking forward, exactly two arms and exactly two hands." + NOIDOL},
    {"id": "j_shield", "종류": "인물", "시드": [1, 2, 3], "프롬프트": MOAB + ", a big heavy shield bearer with a bronze scale vest over the tunic, holding a tall rectangular wooden shield covered with bronze plates in his left hand and a short spear in his right hand, proud chin up, exactly two arms and exactly two hands." + NOIDOL},
    {"id": "j_centurion", "종류": "인물", "시드": [1, 2, 3], "프롬프트": MOAB + ", a stern captain with a grey-streaked beard and a bronze scale armor shirt and a long saffron-yellow cloak, holding a bronze-headed mace in his right hand and pointing forward commandingly with his left hand, hard proud face, exactly two arms and exactly two hands." + NOIDOL},
    {"id": "j_archer", "종류": "인물", "시드": [1, 2, 3], "프롬프트": MOAB + ", a lean young archer with a leather quiver of arrows on his back, drawing a curved wooden bow with an arrow aimed forward, narrowed eyes, exactly two arms and exactly two hands." + NOIDOL},
    {"id": "j_drummer", "종류": "인물", "시드": [1, 2, 3], "프롬프트": MOAB + ", without weapons, beating a round wooden frame drum hanging at his waist with both hands, wide fearful eyes, exactly two arms and exactly two hands." + NOIDOL},
    {"id": "d_soldier", "종류": "인물", "시드": [1, 2, 3], "프롬프트": SEIR + ", holding a long spear in his right hand and a small round hide shield on his left arm, angry frown, walking forward, exactly two arms and exactly two hands." + NOIDOL},
    {"id": "d_shield", "종류": "인물", "시드": [1, 2, 3], "프롬프트": SEIR + ", a big heavy shield bearer holding a tall oval shield of thick hide on a wooden frame in his left hand and a short spear in his right hand, proud chin up, exactly two arms and exactly two hands." + NOIDOL},
    {"id": "d_archer", "종류": "인물", "시드": [1, 2, 3], "프롬프트": SEIR + ", a lean young archer with a leather quiver of arrows on his back, drawing a curved wooden bow with an arrow aimed forward, narrowed eyes, exactly two arms and exactly two hands." + NOIDOL},
    # 미혹하는 영(딤전 4:1): 크고 느린 하늘의 어둠. 손 없이 소매 끝에서 줄이 늘어진다
    {"id": "deceiver", "종류": "정령", "시드": [1, 2, 3, 4], "프롬프트": "A large slow floating shadow spirit: a tall drifting veil of smoky lavender and deep violet mist shaped like a big hooded cloak, with two softly glowing pale lilac eyes and a thin sly smile inside the dark hood, two long wide smoky sleeves with no hands, and from the end of each sleeve several thin glowing lilac threads hang straight down like a puppeteer's strings, ragged wispy smoky edges, eerie but not scary, cute game style, no horns, no hands, no crescent shapes, no moon, no religious symbols."},
    # 여호사밧(NPC, 20:20): 한 손을 들어 외침
    {"id": "jehoshaphat", "종류": "인물", "시드": [1, 2, 3], "프롬프트": JEHOSHAPHAT + ", standing tall and raising his right hand high with an open palm as he calls out to his people, his left hand resting at his side, earnest brave face, exactly two arms and exactly two hands." + NOIDOL},
    # 노래하는 자(20:21): 마침의 행렬
    {"id": "p_singer", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "An Israelite Levite singer in a long white linen robe with a golden sash and a white headcloth, walking forward and singing joyfully with an open mouth and a raised face, holding a small wooden lyre against his chest with his left arm and plucking its strings with his right hand, exactly two arms and exactly two hands."},
    # 숨은 이야기: 사르밧 과부의 기름병(왕상 17:16)
    {"id": "e_oil", "종류": "물건", "시드": [1, 2, 3], "프롬프트": "A small round clay oil jar with a narrow neck tipped slightly so a thin stream of golden olive oil pours from its lip into a small clay bowl, beside a round wooden barrel full of white flour heaped at the top. No people."},
]
items = items[:1] + [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면' and i['id'] != 'bg17']   # 배경을 먼저(길과 탑 자리를 그림에 맞춰야 해서)
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림17.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 17b(10-17): 사람과 관이 어긋난 것을 다시 그린다 — 새그림17b.json
#   s17b: 셋 다 다윗이 관을 쓴 채 바닥에도 관이 하나 더 있음 → 머리에는 관이 없고, 벗은 관 하나만 바닥에
#   s17f: 궁정 선지자들이 아이처럼 나오고(셋 다) 성문에 글자가 생김(시드 1) → 수염 난 어른 선지자들, 글자 없음
#   s17g: 군중 속에 관 쓴 사람이 또 있고 엄마가 아이처럼 나옴 → 관은 여호사밧 하나만, 앞쪽 엄마는 어른
DAVID_NC = "King David, a ruddy Israelite man of about forty with reddish-brown hair and a neat reddish-brown beard, bareheaded with no crown on his head, wearing a deep red royal robe with gold trim"
items_b = [
    scene("s17b", f"inside a royal room of a palace with a window, only two people. On the left {NATHAN}, stands and points at the king with his right arm outstretched and his index finger extended, his left hand holding a wooden staff, with a sad serious face. On the right {DAVID_NC}, kneels on the stone floor and buries his face in both hands, weeping in sorrow; his single gold crown lies on the floor in front of his knees. A small harp leans against the wall. Grey cloudy light from the window." + NOBLOOD, seeds=(11, 12, 13, 14)),
    scene("s17f", f"in the wide open stone square in front of a city gate, two kings sit on two thrones side by side: on the left {AHAB}, and on the right {JEHOSHAPHAT}, looking uneasy. In front of them a crowd of grown-up court prophets, all bearded adult men in colorful robes and turbans, raise their hands and shout; one bearded prophet in front holds a pair of iron horns against his head with both hands. "
                  f"On the right, alone and apart, {MICAIAH}, stands calmly with his hands at his sides and looks straight at the two kings with a brave honest face. Only the two kings wear crowns. No writing, no letters, no signs anywhere." + NOIDOL, seeds=(11, 12, 13, 14)),
    scene("s17g", f"in the new courtyard of the stone temple in Jerusalem, {JEHOSHAPHAT}, stands on a low stone step in front of the crowd and prays with both hands raised high toward heaven, his face lifted up; he is the only person wearing a crown. Behind him the people of Judah stand quietly in prayer with their wives, children and little ones: in the front a grown-up young mother in a green dress and white headscarf holds a baby in her arms, and a small boy holds his bearded father's hand; many more families small and far away, none of them wearing crowns; soft hopeful light." + NOIDOL, seeds=(11, 12, 13, 14)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_b}, open('새그림17b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_b), '항목(17b)', sum(len(i['시드']) for i in items_b), '장')
# 고른 것은 고르기_17.json. 고르는 기준(10-16 사용자): 인물마다 확대해 이목구비가 뚜렷한가와 팔이 정상인가.
#   bg17 시드 3(세 후보 모두 지그재그 벼랑길 대신 벼랑 끝 S자 길. 들 망대가 두 길이 만나는 곳에 서고 쐐기에 평평한 바위, 돌집과 항아리, 푸른 골짜기, 엔게디 종려나무가 다 있는 것),
#   s17a 시드 2, s17b 17b 시드 12, s17c 시드 1, s17d 시드 2, s17e 시드 2, s17f 17b 시드 13, s17g 17b 시드 12(17b의 11·13·14도 군중 속에 관 쓴 사람이 또 있음), v17a 시드 1, v17b 시드 2, v17c 시드 1,
#   j_shield 시드 3(시드 1·2는 몽둥이·창·방패를 한꺼번에 쥠), d_shield 시드 2(시드 1은 창이 둘), deceiver 시드 4, e_oil 시드 3
