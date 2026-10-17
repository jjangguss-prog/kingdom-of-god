# 19 예루살렘 포위 그림 작업 파일(새그림19.json) 만들기 v0.1 (2026-10-18)
# 사용: python 새그림19작성.py → 새그림19.json. 그린 뒤 고르기_19.json으로 모은다.
# 배경(bg19)은 ref2/ref19.png(길 시안)를 참조로 그린다. 앗수르(s_)는 뾰족 투구, 비늘 갑옷과 술 달린 허리띠, 방패병은 키만 한 갈대 방패. 앗수르 신의 상징(날개 달린 원반 따위)은 그리지 않는다.
# 고르는 기준(10-16 사용자): 인물마다 확대해 이목구비가 뚜렷한가와 팔이 정상인가. 하나라도 어긋나면 다시 그린다.
# 사람마다 손이 어디 있는지 정해 준다(s19a 모래를 짚은 손, s19b 턱을 괸 손, s19c 가리키는 손, s19d 무릎 위의 손, s19e 잡은 손, s19f 문을 여는 손, s19g 든 손과 아이를 안은 팔, v19a 편지를 편 손, v19b 성가퀴를 짚은 손, v19c 예물을 든 손).
# 하나님은 빛과 연기로만(s19b 아침 빛, s19d 성전의 연기와 빛과 날개 모양의 빛, s19f·v19a 성전 문의 빛, v19b 진영 위 흰빛). 보좌·스랍의 얼굴과 몸·웃시야의 나병·사슬과 갈고리·쓰러진 사람은 그리지 않는다.
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
FACE = " Every face is clear and well drawn with distinct eyes, nose and mouth."
HANDS = " Hands are drawn simply and clearly, each hand with four fingers and a thumb, and no hand overlaps another person."
NOIDOL = " No statues, no idols, no carved figures, no winged discs, no crescent shapes, no moon ornaments, no religious symbols anywhere."
NOBLOOD = " Nobody is wounded, no blood, nobody lying dead."
FLAT = " All houses are one-story or two-story stone and mud-brick houses with flat earthen rooftops and low parapets; no sloped roofs, no roof tiles, no red tiles."
JONAH = "Jonah the prophet, a thin Israelite man of about forty with a short dark beard and messy dark hair, wearing a plain grey-brown wool robe"
UZZIAH = "young King Uzziah of Judah, a confident man of about twenty-five with a short brown beard, a simple gold crown band and a blue royal robe with gold trim"
ISAIAH = "young Isaiah the prophet, an Israelite man of about twenty-five with a short black beard and a plain cream wool robe"
HEZEKIAH = "King Hezekiah of Judah, a humble earnest man of about thirty-eight with a neat dark-brown beard, a simple gold crown band and a deep blue royal robe with gold trim over a white tunic"
ASSUR = ("an Assyrian soldier, a man with a long curled black beard, a pointed conical iron helmet, a knee-length tunic of bronze scale armor with a fringed tasseled belt, "
         "laced leather boots")
LIGHT = "a soft beam of white-gold light from heaven shines down, with no figure and no face in the light"


def scene(i, pr, seeds=(1, 2, 3)):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + HANDS + FACE + END}


def man(i, pr, seeds=(1, 2, 3), kind="인물"):
    return {"id": i, "종류": kind, "시드": list(seeds), "프롬프트": pr}


items = [
    {"id": "bg19", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3], "참조": ["ref2/ref19.png"],
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield outside the walls of ancient Jerusalem in warm afternoon light, seen from above at a slight angle. "
                 "Keep exactly the same sandy road shapes and positions. The grey stripe running from top to bottom on the left is a tall thick stone city wall with crenellations and four square stone towers on it, and a gate in the middle where the road passes through the wall. "
                 "Left of the wall is inside the city: on the upper left a big stone temple with a courtyard on a hill, in the middle flat-roofed stone houses, on the lower left a small blue pool. "
                 "Right of the wall is outside: the blue oval at the top is a stone-lined upper pool with a narrow stone water channel, and the white patch beside it is a washermen's field with long white cloths spread out on the grass to dry. "
                 "The green area in the upper middle is an olive tree hill. The big brown area on the upper right is an Assyrian army camp with rows of tents and banners and a tall wooden scaffold; "
                 "the brown area on the lower right is terraced fields with olive trees. The small blue spot below the wall is a spring in a rock cleft. "
                 "One road comes from the right edge at the top through the camp and winds to the middle; another road comes from the right edge near the bottom and winds between terraces to the middle; they join and go left through the city gate to the end inside the city. "
                 "Elsewhere: rocky ground, olive trees, small bushes. Nothing covers the roads. No characters, no people, no text." + FLAT + NOIDOL},
    # 이야기(18→19): 구원은 여호와께 속하였나이다(욘 2:9) → 내가 어찌 아끼지 아니하겠느냐(4:11) → 기이한 도우심을 얻어(대하 26:15) → 내가 여기 있나이다(사 6:8) → 그들이 듣지 아니하고(왕하 17:14) → 여호와를 의지하였는데(18:5) → 우리와 함께 하시는 이는(대하 32:8)
    scene("s19a", f"on a quiet sandy beach in the early morning, a big round friendly blue-grey sea fish swims away into the waves after setting Jonah on the shore; {JONAH}, in wet clothes kneels on the sand on both hands and knees and lifts his face up toward the soft sunrise with a thankful relieved expression; calm turquoise sea, gentle waves, a few seagulls." + NOIDOL),
    scene("s19b", f"on a dry hill east of a great city, {JONAH}, sits in the shade of a small booth made of branches beside a withered dry gourd vine with drooping yellow leaves, resting his chin on his right hand with his left hand on his knee, looking down sulkily at the big walled city of Nineveh far below; tiny people in rough brown sackcloth in the city; {LIGHT} over the city in the morning." + NOIDOL),
    scene("s19c", f"on top of a square stone corner tower of the walls of Jerusalem, a big wooden war machine stands: a huge crossbow-like bow frame and a long wooden throwing arm with a sling for big stones; {UZZIAH}, stands beside it and points out over the wall with his right hand, proud and hopeful; two workmen in plain tunics adjust the ropes of the machine with their hands; the city and hills spread below in bright daylight." + NOIDOL),
    scene("s19d", f"inside the great stone temple filled with swirling white smoke, brilliant golden light pours down from above; in the light there are only glowing shapes of six wide wings made of light, with no faces, no bodies and no figures; young {ISAIAH}, kneels on the stone floor with both hands resting on his knees and lifts his face up in awe; a single small glowing coal of fire floats down in the light toward his lips; no throne, no person in the light." + NOIDOL),
    scene("s19e", f"on a long dusty road leaving the walled city of Samaria behind on a hill, Israelite people walk away in a sad quiet line carrying bundles; in the front large: a mother in a brown dress holds the hand of her little daughter, an old man with a white beard carries a cloth bundle on his back with both hands holding the strap, and three young men walk with bowed heads; tiny Assyrian soldiers with pointed helmets far away in the distance; no chains, no ropes, no hooks; dignified, grey cloudy sky." + NOIDOL + NOBLOOD),
    scene("s19f", f"at early morning in the courtyard of the stone temple in Jerusalem, {HEZEKIAH}, pushes open the two tall wooden temple doors wide with both hands; bright golden light streams out from the opening doors; behind him two Levites in white linen robes follow, one holding a broom and the other carrying a clay water jar; dusty steps being cleaned." + NOIDOL),
    scene("s19g", f"in the stone gate square inside the Valley Gate of Jerusalem, {HEZEKIAH}, stands on a low stone step and speaks to the people with his right hand raised high and his left hand at his side, brave and calm; in front of him two Judean army commanders with bronze helmets and round shields listen, and a young mother in a green dress holds a baby in her arms; behind them the tall repaired stone wall with a square tower on which a big wooden war machine stands; bright day." + NOIDOL),
    # 승리 그림 만화(셋): 여호와 앞에 펴 놓고(19:19) → 이 밤에(19:34–35) → 예물을 가지고 예루살렘에 와서(대하 32:23). 해치는 장면과 사람 몸은 그리지 않는다
    scene("v19a", f"in the courtyard in front of the open temple doors of Jerusalem, {HEZEKIAH}, kneels on the stone pavement and spreads open a long scroll letter on the ground with both hands, his face lifted up in prayer; warm golden light flows out of the open temple doors onto him; behind him two royal officials wearing rough brown sackcloth bow down with their faces to the ground; only these three people." + NOIDOL),
    scene("v19b", f"at night, seen from behind, one Judean watchman with a bronze helmet stands on top of a stone tower of the Jerusalem wall, resting both hands on the stone battlement and looking out; beyond the wall in the dark valley spreads the great Assyrian army camp with hundreds of tents and small glowing campfires; from the starry sky a single long beam of pure white light sweeps slowly over the camp and the campfires go out one by one where it passes; no figure in the light, no swords, no people lying anywhere." + NOIDOL + NOBLOOD),
    scene("v19c", f"on a bright morning, the wide-open wooden Valley Gate of Jerusalem: travelers from many nations in clothes of different colors (one in a red striped robe, one in a yellow robe with a green turban, one in a white robe with a blue sash) walk in through the gate carrying gifts: clay jars, cloth bundles and a donkey loaded with packs; on top of the gate {HEZEKIAH}, raises both hands to welcome them with a joyful face; in the front a little Judean boy beside the gate waves; far away beyond the eastern hills an empty camp and a single chariot driving away, tiny." + NOIDOL + NOBLOOD),
    # 웃시야의 기계(장인 4단계 A, 대하 26:15): 돌 망대 위 나무 기계
    man("art_uzziah", "A square tower of cut tan stone blocks with crenellations, and on its flat top a big wooden war machine: a huge crossbow-like bow frame loaded with a big arrow and a long wooden throwing arm with a rope sling holding a round stone, wooden gears and ropes, a pile of round stones beside it. No people.", seeds=(1, 2, 3, 4), kind="건물"),
    # 앗수르 여섯(s_): 사람은 존엄하게
    man("s_soldier", ASSUR + ", holding a long spear in his right hand and a small round bronze shield on his left arm, angry frown, walking forward, exactly two arms and exactly two hands." + NOIDOL),
    man("s_shield", ASSUR + ", a big heavy shield bearer holding a very tall curved shield of woven reeds as tall as himself in his left hand and a short spear in his right hand, proud chin up, exactly two arms and exactly two hands." + NOIDOL),
    man("s_archer", ASSUR + ", a lean archer with a leather quiver of arrows on his back, drawing a big curved composite bow with an arrow aimed forward, narrowed eyes, exactly two arms and exactly two hands." + NOIDOL),
    man("s_centurion", ASSUR + ", a stern officer with a grey-streaked long curled beard, a fringed red shawl over his scale armor, holding a sword in his right hand and pointing forward commandingly with his left hand, hard proud face, exactly two arms and exactly two hands." + NOIDOL),
    man("s_drummer", ASSUR + ", without weapons, beating a round wooden frame drum hanging at his waist with both hands, wide fearful eyes, exactly two arms and exactly two hands." + NOIDOL),
    man("s_chariot", "An Assyrian war chariot: a heavy two-wheeled chariot of dark wood with bronze fittings and big six-spoked wheels, pulled by two strong horses with tasseled red harness, galloping, side view facing right, with three Assyrian men in pointed iron helmets riding in it: a driver holding the reins, an archer with a bow and a shield bearer. The whole chariot and both horses fully visible." + NOIDOL),
    # 산헤립의 공성탑(보스, 왕하 19:32–33): 바퀴 여섯의 높은 나무 탑, 가죽 덮개와 앞 방패, 꼭대기 궁수 셋, 연보라 연기와 빛나는 눈
    man("siegetower", "A huge Assyrian wooden siege tower on six big solid wooden wheels: a tall tower of heavy timber covered with brown leather hides, big wooden shields fixed to its front, and on its top platform three Assyrian archers in pointed iron helmets behind small shields holding bows; a heavy cloud of dark lavender and violet smoke wraps the top of the tower with two glowing pale lilac eyes in the smoke; thin glowing lilac threads hang down from the smoke to the wheels; side view facing right. The whole tower fully visible." + NOIDOL, seeds=(1, 2, 3, 4), kind="물건"),
    man("siegetower_bare", "A huge Assyrian wooden siege tower on six big solid wooden wheels: a tall tower of heavy timber with torn brown leather hides hanging loose, its front shields fallen off, the top platform empty with no people, no smoke, no glow, quiet and broken, side view facing right. The whole tower fully visible." + NOIDOL, seeds=(1, 2, 3, 4), kind="물건"),
    # 랍사게(NPC, 18:28): 술 달린 긴 옷의 앗수르 신하가 한 손을 들어 외침
    man("rabshakeh", "The Rabshakeh, a proud Assyrian royal official with a long curled black beard, a tall rounded cap with a gold band, a long ankle-length fringed robe of red and gold with a tasseled sash, standing and shouting loudly with his mouth wide open, his right hand raised high with an open palm, his left hand on his hip, exactly two arms and exactly two hands." + NOIDOL),
    # 히스기야 둘, 이사야
    man("hezekiah", HEZEKIAH + ", standing tall and raising his right hand with an open palm as he speaks to his people, his left hand at his side, calm brave face, exactly two arms and exactly two hands." + NOIDOL),
    man("hezekiah_pray", HEZEKIAH + ", kneeling on the ground and holding an open scroll letter spread out in front of him with both hands, face lifted up in prayer, exactly two arms and exactly two hands." + NOIDOL),
    man("isaiah", "Isaiah the prophet, an Israelite man of about sixty with a grey beard, a plain cream wool robe and a brown cloak, standing and raising his right hand as he speaks God's word, his left hand holding a small scroll, earnest kind face, exactly two arms and exactly two hands." + NOIDOL),
    # 예물을 가진 여러 나라 나그네(대하 32:23): 옷 빛이 서로 다른 셋
    man("p_guest", "A traveler from a far nation, a man with a short black beard wearing a long red-and-white striped robe and a white turban, walking forward carrying a big clay jar of gifts in both arms, friendly smile, exactly two arms and exactly two hands." + NOIDOL),
    man("p_guest2", "A traveler from a far nation, a dark-skinned man with a short beard wearing a long yellow robe and a green turban, walking forward carrying a wooden chest of gifts in both arms, friendly smile, exactly two arms and exactly two hands." + NOIDOL),
    man("p_guest3", "A traveler from a far nation, an older man with a grey beard wearing a long white robe with a blue sash and a blue headcloth, walking forward carrying a rolled bundle of fine purple cloth in both arms, friendly smile, exactly two arms and exactly two hands." + NOIDOL),
    # 숨은 이야기: 히스기야의 수로(대하 32:30). 기혼 샘의 바위 틈
    man("e_spring", "A small spring of clear blue water bubbling out of a cleft in a big rounded tan rock, with a little pool of water at its foot, green moss and a few small ferns around it. No people.", kind="물건"),
]
items = items[:1] + [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면' and i['id'] != 'bg19']   # 배경을 먼저
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림19.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 19b(10-18): bg19 세 후보 모두 세로 성벽을 회색 길처럼 그리고 성벽을 가로로 그려 성 안팎이 뒤섞임 → 성벽을 성가퀴·망대로, 성 안을 돌바닥과 집들로 그린 ref2/ref19b.png를 참조로 다시 — 새그림19b.json
BG19B = ("Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield of ancient Jerusalem in warm afternoon light, seen from above at a slight angle. "
         "Keep exactly the same sandy road shapes and positions. On the left a tall thick stone CITY WALL with battlements runs in a curve from the top edge down to the bottom edge; the four grey squares on it are square stone towers standing on the wall, "
         "and where the road crosses the wall there is a big stone city gate with an open arched gateway between two gate towers. "
         "Everything to the LEFT of the wall is INSIDE the city: a pale stone-paved city crowded with many small flat-roofed stone houses, the big pale square in the upper left is a great stone temple with a courtyard, the blue oval at the lower left is a stone pool; the road ends inside the city in a small square. "
         "Everything to the RIGHT of the wall is OUTSIDE the city: the blue oval at the top is a stone-lined upper pool with a narrow water channel, the white patch beside it is a washermen's field with white cloths drying on the grass, "
         "the green patch at the top middle is an olive tree hill, the triangles in the upper right are the tents of an Assyrian army camp with banners and a tall wooden scaffold, the lines on the lower right are terraced fields with olive trees, the small blue circle below the wall outside is a spring in a rock cleft. "
         "Elsewhere: rocky dry ground, olive trees, bushes. Nothing covers the roads. No characters, no people, no text.")
items_b = [{"id": "bg19", "종류": "장면", "크기": [1536, 864], "시드": [11, 12, 13, 14], "참조": ["ref2/ref19b.png"], "프롬프트": BG19B + FLAT + NOIDOL}]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_b}, open('새그림19b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_b), '항목(19b)', sum(len(i['시드']) for i in items_b), '장')

# 19c(10-18): s19f 셋 다 히스기야 말고도 관 쓴 사람이 뒤에 또 있음, s_shield 셋 다 갈대 방패와 둥근 방패를 함께 듦 — 새그림19c.json
items_c = [
    scene("s19f", f"at early morning in the stone courtyard of the temple in Jerusalem, {HEZEKIAH}, the only person wearing a crown, stands facing the temple and pushes open the two tall wooden temple doors wide with both hands; bright golden light streams out from the opening doors; a few steps behind him two Levites with no crowns and no hats, bareheaded young men in plain white linen robes, follow: one holds a broom in both hands and the other carries a clay water jar on his shoulder; dusty steps. Only one crown in the picture." + NOIDOL, seeds=(11, 12, 13, 14)),
    man("s_shield", ASSUR + ", a big heavy shield bearer holding ONE very tall curved shield of woven reeds, as tall as himself, in front of him with his left hand, and a short spear in his right hand; no other shield, proud chin up, exactly two arms and exactly two hands." + NOIDOL, seeds=(11, 12, 13, 14)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_c}, open('새그림19c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_c), '항목(19c)', sum(len(i['시드']) for i in items_c), '장')

# 19d(10-18 삽화 검토): s19e(2)는 엄마 손이 셋(아이 손, 노인 손, 가슴 위) — 새그림19d.json
items_d = [
    scene("s19e", f"on a long dusty road leaving the walled city of Samaria behind on a hill, Israelite people walk away in a quiet line carrying bundles; in the front large and separated by small gaps: a mother in a brown dress holding her little daughter's hand with her right hand while her left arm hangs at her side, then an old man with a white beard a little apart carrying a cloth bundle on his back with both hands holding the strap at his chest, then three young men with bowed heads; nobody holds the old man's hand; tiny Assyrian soldiers with pointed helmets far away; no chains, no ropes, no hooks; dignified, grey cloudy sky." + NOIDOL + NOBLOOD, seeds=(21, 22, 23, 24)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_d}, open('새그림19d.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_d), '항목(19d)', sum(len(i['시드']) for i in items_d), '장')
