# 14 엘라 골짜기 그림 작업 파일(새그림14.json) 만들기 v0.1 (2026-10-15)
# 사용: python 새그림14작성.py → 새그림14.json. 그린 뒤 고르기_14.json으로 모은다.
# 배경(bg14)은 ref2/ref14.png(길 시안)를 참조로 그린다. 블레셋 군사는 13에서 그린 b_를 그대로 쓴다.
# 시내나 장막이 길을 덮으면 9·10처럼 그림에 맞춰 길과 탑 자리를 고친다.
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
NOIDOL = " No statues, no idols, no carved figures, no religious symbols anywhere."
NOBLOOD = " Nobody is wounded, no blood."
SAMUEL = "the old prophet Samuel, a thin elderly Israelite man with very long uncut white hair and a long white beard, wearing a plain cream linen robe and a brown wool cloak"
SAUL = "King Saul, a very tall handsome Israelite man of about forty, a head taller than everyone else, with a dark beard, wearing a simple bronze crown band and a rich deep-blue and purple royal robe"
DAVID = "David, a ruddy Israelite shepherd boy of about sixteen with tousled reddish-brown hair, bright eyes and a handsome friendly face, no beard, wearing a plain light-brown wool shepherd's tunic with a rope belt and sandals, a small leather shepherd's bag at his hip"
JONATHAN = "Jonathan, the king's son, a brave young prince of about twenty-five with a short dark beard, wearing a fine royal-blue robe with a gold-trimmed sash, a leather belt and a leather quiver"
GOLIATH = "Goliath of Gath, a giant Philistine champion about twice the height of a normal man, broad and strong, with a dark curly beard, a polished bronze helmet, a coat of bronze scale armor, bronze greaves on his legs, a bronze javelin slung across his back, holding a huge spear with a shaft as thick as a weaver's beam, stern scornful face, a dignified human, not a monster"
BEARER = "his shield bearer, a Philistine soldier in a feathered headdress carrying a very large tall shield in front of Goliath"
ISRAEL = "Israelite soldiers in plain brown and tan tunics with headcloths, spears and small shields"
PHIL = "Philistine soldiers in tall headdresses of upright reed feathers with round shields"
LIGHT = "a soft beam of white-gold light from heaven shines down on him, with no figure and no face in the light"


def scene(i, pr, seeds=(1, 2)):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + END}


items = [
    {"id": "bg14", "종류": "장면", "크기": [1536, 864], "시드": [1, 2], "참조": ["ref2/ref14.png"],
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield in the Valley of Elah in bright clear daylight, seen from above at a slight angle. "
                 "Keep exactly the same sandy road shapes and positions: one road enters from the top edge right of the middle and winds down the right hillside, another road enters from the right edge and makes a big S-curve below the right hill; "
                 "the two roads meet in the middle of the map, cross the brook at a shallow ford, and then climb in an S-curve to the lower left where the road ends. "
                 "A shallow clear blue brook with smooth round pebbles runs diagonally from the top left corner down to the bottom middle, exactly where the blue line is, lined with reeds and a few terebinth oak trees; "
                 "in the brook just below the ford, a small bar of smooth pale gravel stones. "
                 "On the upper right hillside: the camp of the Philistines with many low tents. "
                 "On the lower left hillside: the camp of Israel with tents and a few wooden supply wagons. "
                 "On the left above the ford, beside the brook, a small rocky cliff spur of gray stone. "
                 "Elsewhere: dry grassy hillsides, small bushes and boulders. Nothing covers the roads. No characters, no text." + NOIDOL},
    # 이야기(13→14): 우리에게 왕을 세워(삼상 8:5) → 사울에게 기름을(10:1) → 순종이 제사보다 낫고(15:22, 27) → 중심을 보느니라(16:7) → 막내 다윗(16:13) → 수금(16:23) → 사십 일을 조석으로(17:16, 26)
    scene("s14a", f"in the town of Ramah, a group of gray-bearded Israelite elders in robes stand before {SAMUEL}, who sits on a stone bench; the elders speak earnestly with outstretched hands, asking him for a king, while Samuel listens with a sad troubled face; flat-roofed mud-brick houses behind; serious mood."),
    scene("s14b", f"on a quiet hilltop path at early morning, {SAMUEL}, pours oil from a small clay flask onto the head of a very tall handsome young Israelite man with a short dark beard in a plain brown traveling cloak, who bows his head; two donkeys graze nearby; peaceful, solemn and hopeful." ),
    scene("s14c", f"outside a camp, {SAMUEL}, turns away to leave with a stern sorrowful face, and {SAUL}, grabs the hem of Samuel's brown cloak to hold him back, and the edge of the cloak tears off in Saul's hand; Saul looks shocked and afraid; cloudy sky; no other people."),
    scene("s14d", f"in the courtyard of a simple farmhouse in Bethlehem, seven grown Israelite brothers stand in a row before {SAMUEL}, who holds a ram's horn filled with oil; in front stands the oldest brother Eliab, very tall and handsome; Samuel looks at him but hesitates; their old father Jesse with a white beard stands aside; warm afternoon light; flat-roofed house."),
    scene("s14e", f"in the same courtyard, the youngest son {DAVID}, just called in from the sheep field, kneels on one knee while {SAMUEL}, pours oil from a ram's horn onto his head; {LIGHT}; his seven older brothers and old father Jesse stand around watching in surprise; a few sheep behind; holy joyful moment."),
    scene("s14f", f"inside a dim royal tent, {SAUL}, sits troubled on a wooden throne with his head in one hand, and a cloud of dark purple smoke is around him; in front of him {DAVID}, sits on a small stool and plays a wooden lyre with strings with both hands; where the music sounds, the dark smoke thins out, breaks apart and drifts away, and warm light returns; gentle and hopeful."),
    scene("s14g", f"on a ridge above the Valley of Elah, {DAVID}, carrying a big sack of roasted grain and a basket of bread loaves, has just arrived and looks down into the valley; below by a shallow brook stands {GOLIATH}, with {BEARER}, shouting up the hill; on the near slope the {ISRAEL}, step back afraid; on the far hill across the valley stand ranks of {PHIL}; tense but child-friendly." + NOIDOL),
    # 승리 만화(넷): 만군의 여호와의 이름으로(17:45) → 물매와 돌 하나(17:48–49) → 전쟁은 여호와께 속한 것(17:50) → 자기 생명 같이 사랑하니라(18:4). 해치는 장면은 그리지 않는다
    scene("v14a", f"in the Valley of Elah beside a shallow brook with smooth stones, {DAVID}, stands without any armor, holding a wooden shepherd's staff in his left hand and a leather sling in his right hand, facing {GOLIATH}, who walks toward him behind {BEARER}, and looks down on him with scorn; on the two hills on both sides of the valley the two armies watch; David's face is calm and brave; bright daylight." + NOIDOL),
    scene("v14b", f"in the Valley of Elah, {DAVID}, runs forward toward {GOLIATH}, and swings his leather sling; one small smooth stone flies from the sling as a bright golden streak straight toward the giant's forehead; the giant raises his huge spear and steps forward behind his big shield bearer; dynamic action, child-friendly." + NOBLOOD + NOIDOL),
    scene("v14c", f"by the brook in the Valley of Elah, the giant Goliath lies fallen face down on the ground with his bronze helmet on, completely still, his huge spear lying beside him; {DAVID}, stands near him holding only an empty leather sling, with no sword in his hands, looking up thankfully to the sky; the shield bearer drops his big shield and backs away; on the near hill the {ISRAEL}, jump up and shout with joy; on the far hill the {PHIL}, turn and run away." + NOBLOOD + NOIDOL),
    scene("v14d", f"in front of a royal tent at sunset, {JONATHAN}, takes off his fine royal-blue robe and puts it on {DAVID}, and hands him his bow and his belt with a warm smile; David receives them humbly; the two young men are becoming close friends; warm golden light." ),
    # 다윗(영웅): 지팡이·물매·목자의 주머니, 수염 없음(삼상 16:12, 17:40, 42)
    {"id": "david", "종류": "인물", "시드": [1, 2, 3, 4], "프롬프트": DAVID + ", holding a wooden shepherd's staff in his left hand and a leather sling hanging from his right hand, standing bravely ready, joyful confident face, exactly two arms and exactly two hands."},
    # 골리앗(보스)과 방패 든 자(17:5–7, 41)
    {"id": "goliath", "종류": "인물", "시드": [1, 2, 3], "프롬프트": GOLIATH + ", walking forward heavily, holding the huge spear in his right hand, exactly two arms." + NOIDOL},
    {"id": "b_bearer", "종류": "인물", "시드": [1, 2], "프롬프트": "A Philistine shield bearer of the Sea Peoples, clean-shaven, wearing a tall headdress of upright reed feathers and a short paneled kilt, carrying a very large tall rectangular wooden shield covered with bronze in front of him with both hands, walking forward, exactly two arms." + NOIDOL},
    # 밤의 공포(시 91:5): 하늘의 어둠. 해진 천 같은 그림자와 빛나는 두 눈. 초승달 같은 모양은 쓰지 않는다
    {"id": "fear", "종류": "정령", "시드": [1, 2, 3], "프롬프트": "A floating dark shadow spirit shaped like a tattered dark blue-gray hooded cloth drifting in the air, with ragged wispy smoky edges trailing behind, empty inside the hood except two glowing pale blue eyes, slightly spooky but not scary, cute game style, no hands, no crescent shapes, no moon."},
    # 요나단(NPC, 절벽 위 궁수)과 사울(NPC, 15의 보스와 같은 사람)
    {"id": "jonathan", "종류": "인물", "시드": [1, 2, 3], "프롬프트": JONATHAN + ", drawing a curved wooden bow with an arrow aimed forward, brave kind face, exactly two arms and exactly two hands."},
    {"id": "saul", "종류": "인물", "시드": [1, 2, 3], "프롬프트": SAUL + ", standing tall and holding a long spear upright in his right hand, worried proud face, exactly two arms."},
    # 숨은 이야기: 시냇가의 매끄러운 돌 다섯(17:40)
    {"id": "e_stones", "종류": "물건", "시드": [1, 2], "프롬프트": "Five smooth round river pebbles of gray and cream color, glistening wet, lying close together in a little group on a patch of sand."},
]
items = [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면' and i['id'] != 'bg14'] + items[:1]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림14.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 14b(10-15): 다윗 넷 모두 물매가 손에 없어서, 물매(가죽 끈 둘과 돌을 담은 주머니)를 또렷이 다시 그린다
items_b = [
    {"id": "david", "종류": "인물", "시드": [5, 6, 7, 8], "프롬프트": DAVID + ", holding a wooden shepherd's staff in his left hand, and in his right hand a leather sling: two long thin leather cords hang down from his right hand with a small leather pouch at the bottom holding one smooth round stone, standing bravely ready, joyful confident face, exactly two arms and exactly two hands."},
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_b}, open('새그림14b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('14b', len(items_b), '항목')

# 14c(10-15): s14a·s14d는 박공지붕·기와가 나와서 평평한 지붕의 흙벽돌집으로(12에서 사용자가 고친 것과 같음), s14d는 일곱 형을 어른으로,
#   s14f는 수금이 류트처럼 나와서 U자 틀의 수금으로, v14c는 골리앗이 갑옷 없이 나와서 놋 비늘 갑옷과 투구를 그대로 입고 칼 없이
FLAT = " All houses are one-story mud-brick houses with flat earthen rooftops and low parapets; no sloped roofs, no roof tiles, no red tiles."
KINNOR = "a small wooden kinnor lyre: a U-shaped wooden frame with two curved arms joined by a crossbar at the top and about eight straight vertical strings, held upright against his chest and plucked with his fingers; not a lute, not a guitar, not a mandolin"
items_c = [
    scene("s14a", f"in the town of Ramah, a group of gray-bearded Israelite elders in robes stand before {SAMUEL}, who sits on a stone bench; the elders speak earnestly with outstretched hands, asking him for a king, while Samuel listens with a sad troubled face; serious mood." + FLAT, seeds=(3, 4)),
    scene("s14d", f"in the courtyard of a simple farmhouse in Bethlehem, seven grown Israelite brothers, all adult men with short beards, stand in a row before {SAMUEL}, who holds a ram's horn filled with oil; in front stands the oldest brother Eliab, very tall and handsome; Samuel looks at him but hesitates; their old father Jesse with a white beard stands aside; warm afternoon light." + FLAT, seeds=(3, 4)),
    scene("s14f", f"inside a dim royal tent, {SAUL}, sits troubled on a wooden throne with his head in one hand, and a cloud of dark purple smoke is around him; in front of him {DAVID}, sits on a small stool and plays {KINNOR}; where the music sounds, the dark smoke thins out, breaks apart and drifts away, and warm light returns; gentle and hopeful.", seeds=(3, 4)),
    scene("v14c", f"by the brook in the Valley of Elah, the giant Goliath lies fallen face down on the ground, still wearing his whole bronze scale armor coat, bronze greaves and his bronze helmet, completely still, his huge spear lying beside him; {DAVID}, stands near him holding only an empty leather sling, looking up thankfully to the sky; there is no sword anywhere in the picture; the shield bearer drops his big shield and backs away; on the near hill the {ISRAEL}, jump up and shout with joy; on the far hill the {PHIL}, turn and run away." + NOBLOOD + NOIDOL, seeds=(3, 4)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_c}, open('새그림14c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('14c', len(items_c), '항목')

# 14d(10-15): e_stones 둘 다 돌이 여섯이라, 한 줄로 놓인 다섯으로 다시
items_d = [
    {"id": "e_stones", "종류": "물건", "시드": [3, 4, 5], "프롬프트": "Exactly five smooth round river pebbles, no more and no fewer, of gray and cream color, glistening wet, lying side by side in one single straight row on a small patch of sand, clearly separated from each other."},
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_d}, open('새그림14d.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('14d', len(items_d), '항목')

# 14e(10-15): 새로 그려도 셋이라, 14의 e_stones 시드 1(여섯)을 참조로 왼쪽 아래 회색 돌 하나만 지워 다섯으로
items_e = [
    {"id": "e_stones", "종류": "물건", "시드": [1, 2, 3], "참조": ["raw/e_stones_s1_f01129.png"],
     "프롬프트": "Repaint this exact picture in the same style, but remove the gray stone at the bottom left and fill its place with sand, so that exactly five smooth stones remain on the patch of sand. Keep everything else the same."},
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_e}, open('새그림14e.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('14e', len(items_e), '항목')
