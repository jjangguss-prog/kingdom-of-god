# 20 무너진 성벽 그림 작업 파일(새그림20.json) 만들기 v0.1 (2026-10-18)
# 사용: python 새그림20작성.py → 새그림20.json. 그린 뒤 고르기_20.json으로 모은다.
# 배경(bg20)은 ref2/ref20.png(길 시안)를 참조로 그린다. 다 지은 성벽(bg20_full)은 고른 bg20을 참조로 따로 그린다(새그림20b.json, 아래).
# 사마리아(h_)는 바사 시대 지방 군대: 긴 겉옷에 비늘 갑옷, 둥근 펠트 모자. 바사의 날개 달린 원반 같은 신의 상징은 그리지 않는다.
# 고르는 기준(10-16 사용자): 인물마다 확대해 이목구비가 뚜렷한가와 팔이 정상인가. 하나라도 어긋나면 다시 그린다.
# 사람마다 손이 어디 있는지 정해 준다(s20a 수금, s20b 모은 손, s20c 나팔과 제금과 든 손, s20d 금 규, s20e 모은 손, s20f 잔, s20g 고삐와 횃불, v20a 흙손, v20b 율법책, v20c 악기, e20a 붓, e20b 창, e20c 고삐).
# 하나님은 빛으로만(s20b 굴 어귀의 빛, e20c 별빛). 무너지는 성·불타는 성전·하만의 끝·베들레헴의 아기는 그리지 않는다.
import json, sys
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
FACE = " Every face is clear and well drawn with distinct eyes, nose and mouth."
HANDS = " Hands are drawn simply and clearly, each hand with four fingers and a thumb, and no hand overlaps another person."
NOIDOL = " No statues, no idols, no carved figures, no winged discs, no crescent shapes, no moon ornaments, no religious symbols anywhere."
NOBLOOD = " Nobody is wounded, no blood, nobody lying dead."
FLAT = " All houses are one-story or two-story stone and mud-brick houses with flat earthen rooftops and low parapets; no sloped roofs, no roof tiles, no red tiles."
NEHEMIAH = "Nehemiah, a Jewish man of about forty with a neat short black beard, wearing a long Persian-court robe of deep teal with a golden sash and a soft cream turban"
DANIEL = "Daniel, an old Jewish man with a long white beard, wearing a long purple-and-cream robe"
SAMARIA = ("a soldier of Samaria in the Persian era, a man with a dark brown beard, wearing a round brown felt cap, a long ochre-yellow robe under a short bronze scale-armor vest and a brown leather belt, "
           "leather boots")
LIGHT = "a soft beam of white-gold light from heaven shines down, with no figure and no face in the light"


def scene(i, pr, seeds=(1, 2, 3)):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + HANDS + FACE + END}


def man(i, pr, seeds=(1, 2, 3), kind="인물"):
    return {"id": i, "종류": kind, "시드": list(seeds), "프롬프트": pr}


BG20 = ("Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield of ancient Jerusalem in the Persian era in bright daylight, seen from above at a slight angle. "
        "Keep exactly the same sandy road shapes and positions. In the middle is the city: the grey ring is the city wall, but it is broken down almost everywhere into knee-high lines of tumbled stones and rubble, "
        "and the small dark squares on the ring are burned blackened stone gateways with no doors. Where three roads cross the ring there are three wide gaps of rubble and heaps of dirt. "
        "Inside the ring: in the upper right a rebuilt plain stone temple with a courtyard on a pale patch, in the middle many small flat-roofed mud-brick houses and a small open square where the roads meet. "
        "At the bottom the small blue oval is a pool. On the right the blue stripe is the Kidron brook flowing from top to bottom. The green area on the right is the Mount of Olives with olive trees; "
        "the dark area on the lower left is a deep rocky valley. Near three edges of the picture (upper right, lower right, lower left) there are tiny enemy camps with a few small tents. "
        "Elsewhere: dry fields, olive trees, rocks and bushes. Nothing covers the roads. No characters, no people, no text.")

items = [
    {"id": "bg20", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3], "참조": ["ref2/ref20.png"], "프롬프트": BG20 + FLAT + NOIDOL},
    # 이야기(19→20): 바벨론의 여러 강변(시 137:1) → 사자들의 입을 봉하셨으므로(단 6:22) → 그의 인자하심이 이스라엘에게 영원하시도다(스 3:11) → 이 때를 위함이 아닌지(에 4:14) → 앉아서 울고(느 1:4) → 하늘의 하나님께 묵도하고(2:4) → 일어나 건축하자(2:18)
    scene("s20a", "beside a wide slow river in Babylon under weeping willow trees, Jewish captives sit sadly on the grassy bank; harps hang on the willow branches; in the front large: a young man in a brown tunic hangs a wooden harp on a branch with both hands, a young mother in a blue dress holds a baby in her arms, and an old man with a white beard sits with his head bowed; one woman looks toward the western sky; soft evening light." + NOIDOL + NOBLOOD),
    scene("s20b", f"inside a dim rocky den, {DANIEL}, kneels peacefully on the stone floor with his hands folded together in prayer and his eyes closed; around him three big lions lie down quietly with closed mouths, calm and sleepy like big cats; a soft beam of white-gold light shines down from the opening of the den above, with no figure and no face in the light." + NOIDOL + NOBLOOD),
    scene("s20c", "at the site of the temple in Jerusalem beside fresh new foundation stones on a bright day: priests in white linen robes blow long silver trumpets held in both hands, and Levites in white robes clash bronze cymbals held one in each hand, singing; in the front large: an old man with a long white beard stands beside the new foundation stone and weeps with joy, wiping his eyes with his right hand, and a young man raises both hands high and shouts for joy; a crowd of families behind." + NOIDOL),
    scene("s20d", "in the inner court of the Persian royal palace of Susa with tall columns and blue-and-gold glazed brick walls, Queen Esther, a beautiful young Jewish woman with long dark hair, a gold crown and a royal purple-and-gold gown, stands alone in the court with her hands folded humbly in front of her; on a raised throne King Ahasuerus, a Persian king with a long curled black beard, a tall gold crown and a rich robe, holds out a golden scepter toward her with his right hand, his face kind; only these two people." + NOIDOL),
    scene("s20e", f"in a room of the Persian palace of Susa with a window showing palace towers, {NEHEMIAH}, sits on a rug on the floor with his head bowed and his hands folded together, praying and weeping; beside him stands his brother Hanani, a tired traveler in a dusty brown cloak with a walking staff, who has come from far away; only these two people; quiet evening light." + NOIDOL),
    scene("s20f", f"at a royal banquet table in the Persian palace, {NEHEMIAH}, the king's cupbearer, holds out a golden cup of wine with both hands to King Artaxerxes, a Persian king with a long curled black beard and a tall gold crown, who sits and looks at Nehemiah's face with his right hand raised as he asks a question; beside the king sits the queen in a gold-and-blue gown; Nehemiah's eyes are closed for a moment in silent prayer; only these three people." + NOIDOL),
    scene("s20g", f"under a full moon at night outside the broken walls of Jerusalem, {NEHEMIAH}, rides a grey donkey holding the reins in his left hand and looks at the broken-down stone walls and the burned blackened gateway; beside him two men walk on foot holding burning torches high; heaps of rubble and fallen stones everywhere; deep blue night sky with stars." + NOIDOL),
    # 승리 그림 만화(셋): 오십이 일 만인 엘룰월 이십오일에(6:15) → 여호와로 인하여 기뻐하는 것이(8:10) → 즐거워하는 소리가 멀리 들렸느니라(12:43)
    scene("v20a", f"at sunset on top of the newly finished tall stone wall of Jerusalem, {NEHEMIAH}, with a sword at his belt holds a builder's trowel in his right hand and looks down over the city with a thankful face; beside him a priest in white holds a long curved ram's horn trumpet; below the wall, workers who carried stones put down their baskets and rest, looking up at the finished wall and smiling; golden sky." + NOIDOL),
    scene("v20b", "in the wide square before the Water Gate of Jerusalem, the scribe Ezra, an old man with a long grey beard and a white robe, stands on a tall wooden platform and holds a big open scroll of the law in both hands, reading aloud; a great crowd stands and listens; in the front large: an old man weeping, a Levite in a white robe gently resting his hand on the old man's shoulder, and a little girl looking up; morning light." + NOIDOL),
    scene("v20c", "two great joyful choirs of Levite singers in white linen robes walk in procession along the top of the finished stone wall of Jerusalem, playing bronze cymbals, harps and lyres and singing with raised faces; below inside the city, women and little children on the flat rooftops and in the streets clap and wave with happy faces; bright blue sky, banners of cloth." + NOIDOL),
    # 엔딩 만화(셋): 내 앞에서 길을 준비할 것이요(말 3:1) → 파수꾼이 아침을 기다림보다(시 130:6) → 그의 별을 보고(마 2:2)
    {"id": "e20a", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3], "프롬프트": P + "at dawn in the courtyard of the rebuilt temple in Jerusalem, the prophet Malachi, an Israelite man of about fifty with a grey-streaked beard and a plain cream robe, sits on a stone bench and writes on a long scroll with a reed pen held in his right hand, his left hand holding the scroll; the golden sun rises over the eastern hills behind the temple with warm healing rays of light." + NOIDOL + HANDS + FACE + END},
    {"id": "e20b", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3], "프롬프트": P + "at night on top of a square stone watchtower of the finished Jerusalem wall, one watchman in a brown cloak and a bronze helmet stands holding a long spear upright in his right hand and looks up at the starry night sky, waiting for the morning; the sleeping city with flat roofs below, the deep blue sky full of stars, a faint glow of dawn on the far horizon." + NOIDOL + HANDS + FACE + END},
    {"id": "e20c", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3], "프롬프트": P + "at night over the small hill village of Bethlehem with flat-roofed houses, one great bright star shines in the sky and sends a beam of soft light down onto one small humble house; in the fields shepherds sit with their flocks of sheep and look up at the star; far away on a hill road a few wise men from the east ride camels toward the village, one of them pointing at the star with his right hand; no baby, no people inside the house are shown." + NOIDOL + HANDS + FACE + END},
    # 느헤미야(플레이어블 NPC, 4:17–18): 허리에 칼, 한 손에 흙손
    man("nehemiah", NEHEMIAH + ", a sword in a sheath at his belt, holding a builder's iron trowel in his right hand and resting his left hand on the hilt of his sword, standing firm with a determined brave face, exactly two arms and exactly two hands." + NOIDOL),
    # 사마리아 다섯(h_): 바사 시대 지방 군대
    man("h_soldier", SAMARIA + ", holding a long spear in his right hand and a small round wicker shield on his left arm, angry frown, walking forward, exactly two arms and exactly two hands." + NOIDOL),
    man("h_shield", SAMARIA + ", a big heavy shield bearer holding a tall rectangular wicker shield covered with leather in his left hand and a short spear in his right hand, proud chin up, exactly two arms and exactly two hands." + NOIDOL),
    man("h_centurion", SAMARIA + ", a stern captain with a grey-streaked beard and a long dark red cloak over his armor, holding a short sword in his right hand and pointing forward commandingly with his left hand, hard proud face, exactly two arms and exactly two hands." + NOIDOL),
    man("h_archer", SAMARIA + ", a lean young archer with a leather quiver of arrows on his back, drawing a curved bow with an arrow aimed forward, narrowed eyes, exactly two arms and exactly two hands." + NOIDOL),
    man("h_chariot", "A Persian-era war chariot of Samaria: a two-wheeled chariot of light wood with ochre-yellow painted trim and spoked wheels, pulled by two bay horses with yellow plumes, galloping, side view facing right, one charioteer with a dark brown beard, a round brown felt cap and an ochre robe holding the reins and a spear, proud stern face. The whole chariot and both horses fully visible." + NOIDOL),
    # 산발랏의 사자(6:2–5): 두루마리 편지를 든 사람
    man("p_messenger", "A messenger of Sanballat, a lean man with a thin black beard wearing a long grey-green robe with a striped sash and a round felt cap, walking forward and holding out a rolled scroll letter with a red seal in his right hand, his left hand at his side, sly polite smile, exactly two arms and exactly two hands." + NOIDOL),
    # 숨은 이야기: 성벽 밑의 여우(4:3)
    man("e_fox", "A small cute red fox with a bushy white-tipped tail sitting on a grey stone, looking up curiously with bright eyes, side view facing right. No people.", kind="물건"),
]
items = items[:1] + [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면' and i['id'] != 'bg20']   # 배경을 먼저
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림20.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 20b: 다 지은 성벽(bg20_full). 고른 bg20(raw 파일 이름을 인자로)을 참조로 성벽과 성문만 다 지은 같은 그림을 그린다 — 새그림20b.json
#   사용: python 새그림20작성.py <고른 bg20 raw 파일 이름>
if len(sys.argv) > 1:
    FULL = ("Repaint exactly the same picture with exactly the same roads, houses, temple, river, hills, camps and colors, changing only the city wall: the whole ring of the city wall is now completely rebuilt, "
            "a tall thick wall of fresh cut tan stone blocks with crenellations all the way around, with square towers, and every gateway is rebuilt as a tall stone gatehouse with new wooden doors standing open; "
            "the three gaps where the roads cross the wall are closed by new stone wall; no rubble left. Nothing covers the roads outside the wall. No characters, no people, no text.")
    items_b = [{"id": "bg20_full", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3, 4], "참조": ["raw/" + sys.argv[1]], "프롬프트": FULL + FLAT + NOIDOL}]
    json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_b}, open('새그림20b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(len(items_b), '항목(20b)', sum(len(i['시드']) for i in items_b), '장')

# 20c(10-18): bg20 세 후보 모두 성전을 성벽 밖 기드론 쪽에 그림 → 성 안 북동쪽에 성전과 뜰, 성 안에 집들, 무너진 돌무더기 성벽과 검게 탄 성문을 그린 ref2/ref20b.png를 참조로 다시 — 새그림20c.json
BG20C = BG20.replace("Inside the ring: in the upper right a rebuilt plain stone temple with a courtyard on a pale patch,",
                     "Inside the ring, INSIDE the broken city wall: the pale square with a smaller square in it, in the upper right part inside the wall, is the rebuilt plain stone temple with its courtyard (the temple stands inside the city wall, not outside),")
items_c = [{"id": "bg20", "종류": "장면", "크기": [1536, 864], "시드": [11, 12, 13, 14], "참조": ["ref2/ref20b.png"], "프롬프트": BG20C + FLAT + NOIDOL}]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_c}, open('새그림20c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_c), '항목(20c)', sum(len(i['시드']) for i in items_c), '장')

# 20d(10-18): v20a 시드 1은 나팔 든 제사장의 머리가 없고 2는 둘이 한 몸처럼 붙고 3은 흙손 대신 낫·나팔 부는 자 없음, v20b는 주인 모를 손과 인형처럼 작은 아이, e20c는 셋 다 목자가 없음 — 새그림20d.json
items_d = [
    scene("v20a", f"at sunset on top of the newly finished tall stone wall of Jerusalem, only two people on the wall standing apart and not touching: {NEHEMIAH}, with a sword in a sheath at his belt, holds a flat iron builder's trowel in his right hand and rests his left hand on his sword hilt, looking down over the city with a thankful face; a few steps away a priest in a white robe and a white headcloth, with a clearly visible bearded face, blows a long curved ram's horn trumpet held in both hands; below the wall, grown-up workers put down their baskets of stones and rest, looking up and smiling; golden sky." + NOIDOL, seeds=(11, 12, 13, 14)),
    scene("v20b", "in the wide stone square before the Water Gate of Jerusalem, the scribe Ezra, an old man with a long grey beard and a white robe, stands on a tall wooden platform and holds a big open scroll in both hands, reading aloud; a great crowd stands and listens; in the front large and life-sized, standing on the ground: an old man with a white beard weeping and wiping his eyes with his right hand, a Levite in a white robe standing beside him and resting his left hand on the old man's shoulder, and a little girl standing on the ground holding her mother's hand and looking up; nobody else touches them; morning light." + NOIDOL, seeds=(11, 12, 13, 14)),
    {"id": "e20c", "종류": "장면", "크기": [1536, 864], "시드": [11, 12, 13, 14], "프롬프트": P + "at night over the small hill village of Bethlehem with flat-roofed stone houses, one great bright star shines in the sky and sends a soft beam of light down onto one small humble flat-roofed house; in the field in front, two shepherds in brown cloaks with wooden staffs sit by their sheep and look up at the star with wonder; far away on a hill road a few wise men from the east in rich robes ride camels toward the village, one of them pointing at the star with his right hand; no baby and no people inside the house are shown." + NOIDOL + HANDS + FACE + END},
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_d}, open('새그림20d.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_d), '항목(20d)', sum(len(i['시드']) for i in items_d), '장')
