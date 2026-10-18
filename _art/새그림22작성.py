# 22 예루살렘 함락(왕하 25, 렘 32·39) · 23 곡과 마곡(겔 38–39) 그림 목록 v0.1 (2026-10-19) → 새그림22.json
# 특별 '끝없는 판' 둘. 22는 반드시 무너지는 성에서 남은 자를 곁문으로 빼내고 바룩이 토기에 담은 밭 증서를 지키는 판,
# 23은 북쪽 끝에서 나라들이 하나씩 더해지며 몰려오고 정해진 무리마다 하나님이 우박·불·지진으로 치시는 판.
# 배경(bg22·bg23)은 길 시안(ref2/ref22.png·ref23.png)을 만든 뒤 새그림22b.json으로 따로 그린다.
# 갈대아(n_)는 둥근 놋 투구와 술 달린 짧은 치마, 곡의 연합군은 나라마다 옷이 다르다(g_ 마곡 · q_ 바사 · u_ 구스 · t_ 붓 · w_ 고멜 · y_ 도갈마).
# 성이 불타고 사람이 다치는 모습, 사슬·밧줄, 쓰러진 사람은 그리지 않는다. 하나님은 빛과 불과 구름으로만.
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
FACE = " Every face is clear and well drawn with distinct eyes, nose and mouth."
HANDS = " Hands are drawn simply and clearly, each hand with four fingers and a thumb, and no hand overlaps another person."
NOIDOL = " No statues, no idols, no carved figures, no winged discs, no crescent shapes, no moon ornaments, no religious symbols anywhere."
NOBLOOD = " Nobody is wounded, no blood, nobody lying on the ground, no chains, no ropes."
NOGOD = " There is no human figure, no face and no body of God anywhere: only light, fire and clouds."
FLAT = " All houses are one-story or two-story stone and mud-brick houses with flat earthen rooftops and low parapets; no sloped roofs, no roof tiles."
ARMS = ", exactly two arms and exactly two hands."
JEREMIAH = "Jeremiah the prophet, a thin earnest Judean man of about fifty with a short greying dark beard, wearing a plain undyed cream wool robe and a brown cloak"
BARUCH = "Baruch the scribe, a young Judean man of about thirty with a short neat black beard, wearing a pale blue linen robe with a small wooden scribe's ink case tied at his belt"
CHALDEAN = ("a Babylonian Chaldean soldier, a man with a short curled black beard, a rounded bronze helmet with a short neck guard, "
            "a knee-length dark blue tunic with a wide leather belt and a short fringed red kilt over it, sandals")
EZEKIEL = "Ezekiel the prophet, a strong Judean man of about thirty-five with a full black beard, wearing a white linen priest's tunic under a dark blue cloak"
LIGHT = "a soft beam of white-gold light from heaven shines down, with no figure and no face in the light"


def scene(i, pr, seeds=(1, 2, 3), people=True):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + (HANDS + FACE + END if people else "")}


def man(i, pr, seeds=(1, 2, 3), kind="인물"):
    return {"id": i, "종류": kind, "시드": list(seeds), "프롬프트": pr}


items = [
    # ---------- 22 예루살렘 함락 ----------
    # 이야기: 사방으로 토성을 쌓으매(왕하 25:1) → 시위대 뜰의 예레미야(렘 32:2, 33:3) → 아나돗의 밭을 삼(32:9–10) → 곁문으로 나가는 남은 자와 바룩(25:4, 32:14)
    scene("s22a", "seen from the top of the stone wall of Jerusalem at dusk, two Judean watchmen with bronze helmets and round shields rest their hands on the battlements and look out in worry; outside the walls all around the city spreads a vast Babylonian army camp with hundreds of tents, banners and small campfires, and long sloping earthen siege ramps are being piled up against the walls by tiny workers with baskets; the hills beyond; orange evening sky." + FLAT + NOIDOL + NOBLOOD),
    scene("s22b", f"in a small stone-paved courtyard surrounded by high stone walls (the court of the guard in Jerusalem), {JEREMIAH}, sits on a stone bench with his hands folded on his knees and lifts his face up as {LIGHT} on him; a Judean guard with a bronze helmet and a spear stands quietly by the arched doorway; beside Jeremiah a small clay water jar and one round loaf of bread." + NOIDOL),
    scene("s22c", f"in the stone courtyard of the guard in Jerusalem, {JEREMIAH}, holds a small bronze hand balance scale in his right hand and weighs out a few pieces of silver for his cousin Hanamel, a Judean man in a striped brown robe who holds out both open hands; beside them {BARUCH}, sits on a low stool and writes on a scroll with a reed pen; behind them three older Judean men stand as witnesses and watch; on a low wooden table two rolled scrolls and a lump of clay for a seal; bright day." + NOIDOL),
    scene("s22d", f"at night under the moon, a narrow stone gate between two high city walls beside a garden of olive and fig trees, Judean families quietly walk out through the gate onto a path down the hill carrying cloth bundles: a mother holding a little child on her hip, an old man with a wooden staff, a boy holding his father's hand; at the front {BARUCH}, carries a tall sealed clay jar in both arms; far away on the dark hills the small campfires of an enemy camp." + NOIDOL + NOBLOOD),
    # 마침(만화): 토기에 담아(32:14) → 아침마다 새로우니(애 3:22–23, 렘 39:10) → 집과 밭과 포도원을 다시(32:15, 44)
    scene("v22a", f"in the courtyard of the guard by warm lamplight, {BARUCH}, carefully lowers two rolled scrolls tied with string and sealed with clay into a tall clay jar with both hands, while {JEREMIAH}, kneels beside the jar and holds its clay lid ready in both hands with a hopeful face; only these two people." + NOIDOL),
    scene("v22b", f"at sunrise on a green hill outside Jerusalem, whose distant stone walls are broken down in places (no fire, no smoke), {JEREMIAH}, sits on a rock and lifts his face toward the golden rising sun with quiet tears of hope; below the hill a few poor Judean farmers in simple clothes tend green vineyards and small fields; birds fly in the bright morning sky." + NOIDOL + NOBLOOD),
    scene("v22c", "many years later on a bright sunny morning, on a green terraced hill full of grapevines, a happy Judean family: the father holds up an old sealed clay jar with both hands that he has just dug up from the field, the mother beside him smiles and holds a basket of grapes, a little girl and a little boy laugh and point at the jar; far away on the horizon the city of Jerusalem is being rebuilt with wooden scaffolds and cranes." + FLAT + NOIDOL),
    # 갈대아 군사 여섯(n_): 사람은 존엄하게
    man("n_soldier", CHALDEAN + ", holding a long spear in his right hand and a small round bronze shield on his left arm, determined frown, walking forward" + ARMS + NOIDOL),
    man("n_shield", CHALDEAN + ", a big heavy shield bearer holding ONE tall rectangular shield of woven wicker covered with leather in front of him with his left hand and a short spear in his right hand, proud chin up" + ARMS + NOIDOL),
    man("n_archer", CHALDEAN + ", a lean archer with a leather quiver of arrows on his back, drawing a big curved composite bow with an arrow aimed forward, narrowed eyes" + ARMS + NOIDOL),
    man("n_centurion", "A Babylonian Chaldean commander, a stern man with a long curled black beard streaked with grey, a tall rounded bronze helmet with a red horsehair crest, a long fringed red-and-gold robe over bronze scale armor, holding a curved sword in his right hand and pointing forward commandingly with his left hand, hard proud face" + ARMS + NOIDOL),
    man("n_raider", "A fast young Babylonian Chaldean scout, a lean man with a short black beard and a red cloth headband, a short sleeveless tan tunic with a belt, running forward quickly holding a short spear in his right hand, his left arm swinging, eager face" + ARMS + NOIDOL),
    man("n_chariot", "A Babylonian war chariot: a light two-wheeled chariot of dark wood with bronze fittings and big eight-spoked wheels, pulled by two galloping horses with blue and gold tasseled harness, side view facing right, with two Chaldean men in rounded bronze helmets riding in it: a driver holding the reins and an archer with a bow. The whole chariot and both horses fully visible." + NOIDOL),
    # 남은 자(곁문으로 나가는 사람들)와 바룩·예레미야, 증서를 담은 토기
    man("p_flee", "A Judean mother in a brown dress and a cream headscarf walking forward, holding a small child on her left hip with her left arm and carrying a cloth bundle in her right hand, worried but brave face; the child has short dark hair and holds onto her dress" + ARMS + NOIDOL),
    man("p_flee2", "An old Judean man with a long white beard, a grey wool robe and a brown headcloth, walking forward leaning on a wooden walking staff held in his right hand, a cloth bundle on his back with the strap held in his left hand at his chest, tired but steady face" + ARMS + NOIDOL),
    man("p_flee3", "A Judean boy of about ten with short curly dark hair in a short tan tunic, walking forward carrying a small clay water jar in both arms against his chest, brave face" + ARMS + NOIDOL),
    man("baruch", BARUCH + ", walking forward carrying a tall sealed clay jar with a clay lid in both arms against his chest, careful and hopeful face" + ARMS + NOIDOL),
    man("jeremiah", JEREMIAH + ", standing and raising his right hand with an open palm as he speaks God's word, holding a small rolled scroll in his left hand, earnest kind face" + ARMS + NOIDOL),
    man("e_deedjar", "A tall sealed clay storage jar with a round clay lid tied on with string, standing on a small patch of earth, with two small rolled scrolls tied with string and a round clay seal lying in front of it. No people.", kind="물건"),
    # ---------- 23 곡과 마곡 ----------
    # 이야기: 그발 강가의 에스겔(겔 1:1, 38:2) → 성벽도 없이 평안히(38:8, 11) → 구름이 땅을 덮음 같이(38:9, 16) → 하늘이 열림(38:18)
    scene("s23a", f"beside the wide river Chebar in Babylon among willow trees, {EZEKIEL}, stands at the water's edge holding a small scroll in his left hand and stretching his right hand toward the north, where far away over the horizon a huge dark storm cloud is gathering; a few Judean exiles in simple robes sit on the riverbank and listen; calm afternoon." + NOIDOL),
    scene("s23b", "the green mountains of Israel in peaceful warm sunlight: small villages of flat-roofed stone houses with no city walls, no gates and no bars around them; children play with a ball between the houses, a shepherd boy leads sheep, two women carry water jars on their shoulders, men work in vineyards and olive groves on the terraced hills; everything open, safe and happy." + FLAT + NOIDOL),
    scene("s23c", "seen from a hilltop, a vast army of many nations pours over the far northern hills like a dark storm cloud covering the land: countless tiny horsemen with banners, foot soldiers with shields and helmets of many different colors, and war chariots, all rolling forward under a dark boiling cloudy sky with flashes of lightning; menacing but not gory; no single person large; no people hurt." + NOIDOL + NOBLOOD, people=False),
    scene("s23d", f"on a green hill beside an unwalled village of flat-roofed houses, a Judean family (a father, a mother holding a baby, an old grandmother and two children) stand close together and look up at the sky, where dark storm clouds are breaking open and {LIGHT} on them; hopeful faces." + FLAT + NOIDOL + NOGOD),
    # 마침(만화): 우박과 불(38:22, 39:3) → 무기로 불을 피움(39:9–10) → 내 영을 쏟았음이라(39:29)
    scene("v23a", "over empty rocky mountains under a stormy sky, huge round white hailstones and glowing balls of fire fall from heaven and the ground cracks open in an earthquake; far away the countless invading army runs away scattering in panic, dropping their bows, arrows, shields, spears and banners all over the ground; nobody is hurt, no blood, nobody lying on the ground, the people are only small and far away." + NOGOD + NOIDOL, people=False),
    scene("v23b", "in a peaceful village square on the green mountains of Israel at evening, happy villagers throw piles of dropped wooden shields, bows, arrows, spears and a broken chariot wheel onto a big warm bonfire; a mother bakes round flat bread on a hot stone by the fire, two children warm their hands and smile, an old man with a white beard adds a broken spear to the flames; no weapons are being used by anyone." + FLAT + NOIDOL),
    scene("v23c", "at sunrise on the green mountains of Israel, crowds of joyful people from all the unwalled villages, men, women, children and old people, stand together on the hills with their arms raised, and brilliant warm golden light pours down from an opening in the clouds over all of them like gentle rain." + NOGOD + NOIDOL),
    # 곡의 연합군(겔 38:2–6): 나라마다 옷이 다르다. 사람은 존엄하게, 오늘의 어느 나라와도 닮지 않게
    man("g_soldier", "A warrior from the far north of the ancient world, a man with a bushy reddish-brown beard, a tall pointed felt cap trimmed with fur, a thick quilted brown coat, baggy trousers and soft boots, holding a spear in his right hand and a round wicker shield on his left arm, fierce face, walking forward" + ARMS + NOIDOL),
    man("g_horse", "A horseman from the far north of the ancient world riding a sturdy brown horse with a thick mane, the rider has a bushy reddish-brown beard, a tall pointed felt cap trimmed with fur, a quilted brown coat, a bow case at his side and holds a long spear in his right hand and the reins in his left hand, galloping, side view facing right. The whole horse and rider fully visible" + ARMS + NOIDOL),
    man("q_shield", "An ancient Persian soldier, a man with a neat curled black beard, a bronze helmet, a long-sleeved patterned purple-and-yellow tunic over trousers, holding a big rectangular wicker shield in front of him with his left hand and a short spear in his right hand, proud face, walking forward" + ARMS + NOIDOL),
    man("u_archer", "A tall ancient Cushite archer from the upper Nile, a dignified dark-skinned man with short black hair and a white ostrich feather in a red headband, a white linen kilt with a red sash and a leather quiver on his back, drawing a very long bow with an arrow aimed forward, focused face" + ARMS + NOIDOL),
    man("t_centurion", "An ancient Libyan commander from the land of Put, a stern man with a short pointed beard, a long braided side-lock and two white feathers in his hair, a long patterned red-and-green cloak over a tunic, holding a curved sword in his right hand and pointing forward commandingly with his left hand" + ARMS + NOIDOL),
    man("w_raider", "A fast young raider from the far north of the ancient world, a lean man with long braided blond hair and a short beard, a short sleeveless green tunic, leather leggings and a small round shield on his back, running forward quickly holding a short spear in his right hand, eager face" + ARMS + NOIDOL),
    man("y_chariot", "A light war chariot from the far north of the ancient world: a small two-wheeled chariot of pale wood with big spoked wheels, pulled by two galloping grey horses with red tasseled harness, side view facing right, with two men riding in it wearing pointed felt caps and quilted coats: a driver holding the reins and an archer with a bow. The whole chariot and both horses fully visible." + NOIDOL),
]
items = [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면']   # 작은 그림을 먼저
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림22.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 22b·23b 배경(2026-10-19): 길 시안 ref2/ref22.png·ref23.png(탑자리22.py)를 참조로 그린다 — 새그림22b.json
BG22 = ("Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield around the besieged walled city of ancient Jerusalem in warm late-afternoon light, seen from above at a slight angle. "
        "Keep exactly the same sandy road shapes and positions. The big pale area at the top center enclosed by the thick grey line is INSIDE the city: a tall thick stone CITY WALL with battlements and square towers runs all around it, "
        "and inside the wall a crowded city of many small flat-roofed stone houses; the big pale rectangle on the upper right inside the city is the stone temple courtyard on its hill, the smaller rectangle is the king's palace. "
        "The small dark square at the lower right corner of the wall is a narrow side gate between two walls, and the small green patch beside it is the king's garden with olive and fig trees. "
        "The three roads that come from the left, bottom and upper right edges end at the foot of the city wall, where each ends at a sloping ramp of piled brown earth leaning against the wall (siege ramps). "
        "The fourth road leads from the side gate down to the right edge through green fields and vineyards. "
        "Outside the walls: dry rocky hills; the darker brown patches on the left and at the bottom left are a Babylonian army camp with rows of plain tents, banners and small campfires; "
        "the green patches on the right are terraced fields, vineyards and olive groves. Nothing covers the roads. No characters, no people, no text.")
BG23 = ("Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield on the green mountains of Israel in bright daylight, seen from above at a slight angle. "
        "Keep exactly the same sandy road shapes and positions. The dark band across the very top is a huge dark storm cloud rolling over the far northern hills and covering the horizon, with faint flashes of lightning. "
        "Four sandy roads come down out of the dark northern clouds and wind across green terraced mountain slopes with olive groves, vineyards, rocks and small bushes, "
        "and meet at the bottom center at a small peaceful village of flat-roofed stone houses with no city wall, no gate and no bars, with a stone well and a sheep pen. "
        "The lighter green patches are grassy meadows. Nothing covers the roads. No characters, no people, no text.")
items_b = [{"id": "bg22", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3, 4], "참조": ["ref2/ref22.png"], "프롬프트": BG22 + FLAT + NOIDOL},
           {"id": "bg23", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3, 4], "참조": ["ref2/ref23.png"], "프롬프트": BG23 + FLAT + NOIDOL}]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_b}, open('새그림22b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_b), '항목(22b)', sum(len(i['시드']) for i in items_b), '장')

# 22c(10-19 고르기): v22c 셋 다 쇠 타워 크레인과 오늘날 옷(티셔츠·치마), s23b 셋 다 티셔츠·반바지·카우보이 모자·쇠 양동이, v23b 셋 다 오늘날 옷·전봇대·창 든 아이·피자 같은 빵 → 옛 옷차림과 나무 비계만 — 새그림22c.json
ANCIENT = (" Everyone wears ancient Israelite clothing: long simple wool tunics and robes with cloth sashes, women in long dresses with headscarves, children in short simple tunics, leather sandals;"
           " no modern clothes, no t-shirts, no shorts, no trousers, no hats, no metal buckets, no glass windows, no roof tiles; only clay jars and woven baskets.")
items_c = [
    scene("v22c", "many years later on a bright sunny morning, on a green terraced hillside vineyard full of grapevines, a happy Judean family: the father, a bearded man in a long brown wool robe, kneels by a small hole in the earth and lifts up an old sealed clay jar with both hands, the mother in a long blue dress and a white headscarf smiles and holds a basket of grapes, a little girl and a little boy laugh and point at the jar; far away on the horizon the stone walls of Jerusalem are being rebuilt with simple wooden scaffolding and workers carrying stones; no cranes, no machines." + FLAT + ANCIENT + NOIDOL, seeds=(11, 12, 13)),
    scene("s23b", "the green mountains of Israel in peaceful warm sunlight: a small village of flat-roofed stone and mud-brick houses with no city wall, no gate and no bars; two children play with a leather ball, a shepherd boy with a wooden staff leads a few sheep, two women carry clay water jars on their shoulders, two men prune grapevines on the terraced hills; everything open, safe and happy." + FLAT + ANCIENT + NOIDOL, seeds=(11, 12, 13)),
    scene("v23b", "in a peaceful village square on the green mountains of Israel at evening, happy villagers pile dropped wooden shields, bows, arrows and spears and a broken wooden chariot wheel onto a big warm bonfire as firewood: a father throws an armful of broken arrows onto the fire, a mother bakes plain round flat bread on a hot flat stone beside the fire, two small children sit and warm their open hands at the fire and smile, an old man with a white beard drops a broken bow onto the flames; the children hold no weapons and nobody holds a weapon ready to use; no poles, no wires." + FLAT + ANCIENT + NOIDOL, seeds=(11, 12, 13)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_c}, open('새그림22c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_c), '항목(22c)', sum(len(i['시드']) for i in items_c), '장')
