# 13 미스바 그림 작업 파일(새그림13.json) 만들기 v0.1 (2026-10-15)
# 사용: python 새그림13작성.py → 새그림13.json. 그린 뒤 고르기_13.json으로 모은다.
# 배경(bg13)은 ref2/ref13.png(길 시안)를 참조로 그린다. 블레셋 겉모습(b_) 일곱은 14 엘라 골짜기에서도 쓴다.
# 제단이나 장막이 길을 덮으면 9·10처럼 그림에 맞춰 길과 탑 자리를 고친다.
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
NOIDOL = " No statues, no idols, no carved figures, no poles, no religious symbols anywhere."
SAMUEL = "the old prophet Samuel, a thin elderly Israelite man with very long uncut white hair falling to his shoulders and a long white beard, wearing a plain cream linen robe and a brown wool cloak"
ISRAEL = "Israelite men, women and children in plain brown, tan and cream wool tunics and headcloths"
# 블레셋(바다 사람들): 메디넷 하부 부조의 깃털 관(머리띠 위에 곧게 선 갈대 깃털), 둥근 방패, 술 달린 짧은 치마 갑옷. 웃음거리로 그리지 않는다. 다곤 같은 신의 모습은 넣지 않는다
PHIL = "a Philistine warrior of the Sea Peoples, clean-shaven, wearing a tall headdress made of a headband with a neat row of upright reed feathers, a ribbed leather-and-bronze strapped corselet, a short paneled kilt with tassels, and sandals"
LIGHT = "the angel of the LORD is shown only as a tall column of bright white-gold flame and light rising to the sky, with no figure, no face, no body and no wings inside the light"


def scene(i, pr, seeds=(1, 2)):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + END}


items = [
    {"id": "bg13", "종류": "장면", "크기": [1536, 864], "시드": [1, 2], "참조": ["ref2/ref13.png"],
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield in the green hill country of Benjamin at Mizpah in bright clear daylight, seen from above at a slight angle. "
                 "Keep exactly the same sandy road shapes and positions: the road that enters from the top edge left of the middle and runs diagonally down to the middle of the map, the road that enters from the left edge near the bottom and runs up to the right, "
                 "the place in the middle where the two roads meet, and the short road that then climbs in an S-curve up to the right and ends on the broad round hilltop. "
                 "On the broad rounded hilltop on the right side of the map: a simple square altar of rough uncut field stones, and around it many small Israelite tents of brown and tan wool. "
                 "On the left of the middle, between the two roads, one tall jagged gray rock standing up like a big tooth, the rock of Shen. "
                 "Just below the place where the roads meet, a small flat empty patch of short green grass. "
                 "At the bottom middle, the corner of a small terraced field of golden ripe barley with low stone walls. "
                 "On the far left the slope falls away toward a hazy pale western plain. "
                 "Elsewhere: grassy hillsides with olive trees, terebinth trees, small bushes and stones. Nothing covers the roads. No characters, no text." + NOIDOL},
    # 이야기(12→13): 태에서부터 나실인(삿 13:5, 20) → 이번만 나를 강하게 하사(16:28) → 어머니의 하나님이 나의 하나님(룻 1:16) → 한나의 기도(삼상 1:11) → 말씀하옵소서(3:10) → 젖 나는 소 두 마리(6:12–13) → 미스바로 모이라(7:6)
    scene("s13a", f"on a hillside field at dusk, a married Israelite couple, Manoah and his wife, in plain brown and blue wool clothes, have offered a young goat on a big flat rock; a bright flame shoots up from the rock high into the evening sky, and {LIGHT}; the man and the woman bow down with their faces to the ground in awe; holy, quiet and wonderful."),
    scene("s13b", "inside a large ancient stone hall with two tall thick round stone pillars in the middle, Samson, a very strong Israelite man in a torn plain tunic, with long dark hair that has grown back down to his shoulders and a short beard, stands between the two pillars with one hand on each pillar, his eyes closed peacefully, his face lifted up in prayer; a soft beam of light falls on him from above; the hall is dim; no other people close by, nothing is falling, nobody is hurt." + NOIDOL),
    scene("s13c", f"on a dusty road through golden barley fields toward the small hill town of Bethlehem, a young Moabite woman named Ruth with a dark blue headscarf hugs an older Israelite widow named Naomi in a gray-brown shawl, holding her hands warmly and promising to stay with her; far behind on the road another young woman walks away back home; warm morning light, tender and loyal."),
    scene("s13d", f"at the doorway of the tent sanctuary of Shiloh, a large tent of woven goat hair with a wooden doorpost; a young Israelite woman named Hannah in a soft blue robe and white veil kneels and prays with tears, her lips moving silently and her hands clasped; beside the doorpost sits the old heavy priest Eli in a white linen robe on a wooden seat, watching her; gentle evening light."),
    scene("s13e", "at night inside the tent sanctuary at Shiloh, a small boy Samuel of about eight years, with long hair and a simple white linen tunic, sits up on a sleeping mat and listens with wide eyes; beside him a tall golden seven-branched lamp still burns with small warm flames; a soft glow of white-gold light shines gently into the dark tent like a voice calling, with no figure and no face in the light; quiet, holy and hopeful."),
    scene("s13f", "in a broad valley of ripe golden wheat at harvest, Israelite reapers of Beth-shemesh with sickles stand up and look with great joy at the road; on the road two brown milk cows pull a new wooden cart by themselves; on the cart rides a box completely covered with a plain blue cloth; the reapers raise their hands and smile; bright happy summer light; no other animals."),
    scene("s13g", f"on the top of the hill of Mizpah beside a simple altar of rough uncut stones, a large crowd of {ISRAEL}, pour water from clay jars onto the ground in sorrow and prayer, some kneeling and some weeping; {SAMUEL}, stands before them with both hands lifted up to heaven; far away in the hazy western plain below rises a cloud of dust from a coming army; serious but hopeful mood." + NOIDOL),
    # 승리 만화: 큰 우레를 발하여(7:10) → 에벤에셀(7:12) → 여호와의 손이 막으시매(7:13–14). 해치는 장면은 그리지 않는다
    scene("v13a", f"dark storm clouds over a western hillside; bright lightning and great thunder flash from the clouds; on the slope a whole army of Philistine soldiers in tall feathered headdresses is thrown into confusion and runs away down the hill, dropping their round shields; nobody is struck and nobody is hurt; on the hilltop above, smoke rises from a stone altar and {SAMUEL}, stands with both hands raised to heaven; dramatic but child-friendly." + NOIDOL),
    scene("v13b", f"on a green hill between the hill of Mizpah and a jagged tooth-shaped rock, {SAMUEL}, stands beside one big upright standing stone that has just been set up on a small mound, his hand resting on it; a crowd of {ISRAEL}, stand around it in a circle and look at it with thankful faces; warm golden afternoon light, peaceful and joyful." + NOIDOL),
    scene("v13c", f"a wide peaceful landscape of terraced fields at harvest time; Israelite families and children reap golden grain and carry sheaves, a girl laughs with a basket; far in the background on a green hill stands one big upright memorial stone; along a dirt road an old prophet with long white hair walks with a staff toward the next village; bright, safe and happy summer day." + NOIDOL),
    # 블레셋 일곱(b_): 14 엘라 골짜기에서도 쓴다
    {"id": "b_soldier", "종류": "인물", "시드": [1, 2], "프롬프트": PHIL + ", holding a long spear in his right hand and a small round bronze-rimmed shield on his left arm, angry frown, walking forward, exactly two arms." + NOIDOL},
    {"id": "b_raider", "종류": "인물", "시드": [1, 2], "프롬프트": "A lightly dressed fast Philistine raider of the Sea Peoples, clean-shaven, with a headband of a few upright reed feathers, a short plain kilt, no armor, holding a wooden club, running forward eagerly with a greedy grin, exactly two arms." + NOIDOL},
    {"id": "b_shield", "종류": "인물", "시드": [1, 2], "프롬프트": PHIL + ", carrying a big round bronze-rimmed shield in front of his body with his left arm and a short spear in his right hand, chin raised proudly, exactly two arms." + NOIDOL},
    {"id": "b_centurion", "종류": "인물", "시드": [1, 2], "프롬프트": "A Philistine captain of the Sea Peoples, a stern clean-shaven man with a taller headdress of upright reed feathers on a bronze band, a polished bronze scale breastplate, a red cloak, a paneled kilt with tassels, holding a commander's staff, hard stubborn face, exactly two arms." + NOIDOL},
    {"id": "b_archer", "종류": "인물", "시드": [1, 2], "프롬프트": PHIL + ", a leather quiver of arrows on his back, drawing a curved wooden bow with an arrow aimed forward, narrowed eyes, exactly two arms." + NOIDOL},
    {"id": "b_drummer", "종류": "인물", "시드": [1, 2], "프롬프트": PHIL + ", without weapons, beating a round wooden frame drum hanging at his waist with both hands, wide fearful eyes, exactly two arms and exactly two hands." + NOIDOL},
    {"id": "b_giant", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "A huge Philistine giant of Gath, one of the last of the Anakim, twice as tall and very broad and muscular, with a dark curly beard, a bronze helmet with a crest of upright reed feathers, a leather armor vest with bronze studs, a paneled kilt, holding a big heavy wooden club, scornful frowning face, a dignified human, not a monster, exactly two arms." + NOIDOL},
    # 나실인 탑(양치기 4단계 B): 에담 바위 틈(삿 15:8) 같은 바위 굴 막사. 나실인: 일곱 가닥으로 땋은 긴 머리(16:13), 맨손(14:6)
    {"id": "shep_nazirite", "종류": "건물", "시드": [1, 2], "프롬프트": "A small sturdy shelter built into a cleft of a big rounded boulder of tan rock, like the cleft of the rock of Etam: a dark cave mouth with a woven reed mat hanging as a curtain, a low wall of piled stones around a little yard, a wooden post with a coiled rope, a clay water jar and a bundle of grain beside the entrance."},
    {"id": "nazirite", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "A Nazirite strongman of ancient Israel, a muscular young man with very long dark hair braided into seven long thick braids hanging over his back and shoulders, a full dark beard, wearing a simple short brown wool tunic with a wide leather belt and sandals, barehanded with both hands empty and clenched into fists, ready to wrestle, brave determined face, exactly two arms and exactly two hands, no weapon."},
    # 사무엘(NPC): 두 손을 든 기도
    {"id": "samuel", "종류": "인물", "시드": [1, 2, 3], "프롬프트": SAMUEL + ", standing and praying with both hands lifted up to heaven, eyes looking up, calm faithful face, exactly two arms and exactly two hands."},
    # 에벤에셀 돌(7:12), 숨은 이야기의 곡식 다발(룻 2:16)
    {"id": "ebenezer", "종류": "물건", "시드": [1, 2], "프롬프트": "One big upright standing stone memorial, a tall rough gray boulder set upright on a small mound of earth, with a few small stones packed around its base and a little grass, no carvings, no letters."},
    {"id": "e_sheaf", "종류": "물건", "시드": [1, 2], "프롬프트": "One bundle of harvested golden barley sheaf tied around the middle with a twisted straw band, standing upright, with a few loose ears of grain lying on the ground beside it."},
]
items = [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면' and i['id'] != 'bg13'] + items[:1]   # 게임에 바로 쓰는 인물·물건 먼저, 참조가 있는 배경은 마지막에
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림13.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 13b(10-15): s13e는 등잔대가 촛대(초 다섯)로 나와서 일곱 등잔을 또렷이, s13f는 암소가 하나로 나와서 멍에를 멘 두 마리를 또렷이 다시 그린다
LAMP = "a solid gold lampstand of the tabernacle with one straight central shaft and exactly three curved branches on each side, seven branches in all, each branch ending in a small oil lamp bowl with a tiny flame, no candles, no wax"
items_b = [
    scene("s13e", f"at night inside the tent sanctuary at Shiloh, a small boy Samuel of about eight years, with long hair and a simple white linen tunic, sits up on a sleeping mat and listens with wide eyes; beside him stands {LAMP}, still burning low; a soft glow of white-gold light shines gently into the dark tent like a voice calling, with no figure and no face in the light; quiet, holy and hopeful.", seeds=(3, 4, 5)),
    scene("s13f", "in a broad valley of ripe golden wheat at harvest, Israelite reapers of Beth-shemesh with sickles stand up and look with great joy at the road; on the road a pair of two brown milk cows walking side by side under one wooden yoke pull a new wooden cart by themselves, two cows clearly visible; on the cart rides a box completely covered with a plain blue cloth; the reapers raise their hands and smile; bright happy summer light; no other animals.", seeds=(3, 4, 5)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_b}, open('새그림13b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('13b', len(items_b), '항목')

# 13c(10-15): s13c·v13c는 마을 집이 기와 박공지붕으로 나와서 평평한 지붕의 흙벽돌집으로(12에서 사용자가 고친 것과 같음)
FLAT = " All houses are one-story mud-brick houses with flat earthen rooftops and low parapets; no sloped roofs, no roof tiles, no red tiles."
items_c = [
    scene("s13c", "on a dusty road through golden barley fields toward the small hill town of Bethlehem, a young Moabite woman named Ruth with a dark blue headscarf hugs an older Israelite widow named Naomi in a gray-brown shawl, holding her hands warmly and promising to stay with her; far behind on the road another young woman walks away back home; warm morning light, tender and loyal." + FLAT, seeds=(3, 4)),
    scene("v13c", "a wide peaceful landscape of terraced fields at harvest time; Israelite families and children reap golden grain and carry sheaves, a girl laughs with a basket; far in the background on a green hill stands one big upright memorial stone; along a dirt road an old prophet with long white hair walks with a staff toward the next village; bright, safe and happy summer day." + FLAT + NOIDOL, seeds=(3, 4)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_c}, open('새그림13c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('13c', len(items_c), '항목')

# 13d(10-15): 13b의 s13e도 가지가 셋뿐이라, 일곱 불꽃이 한 줄로 나란히 타는 모양으로 한 번 더
items_d = [
    scene("s13e", "at night inside the tent sanctuary at Shiloh, a small boy Samuel of about eight years, with long hair and a simple white linen tunic, sits up on a sleeping mat and listens with wide eyes; behind him stands a wide golden menorah lampstand whose seven small oil flames burn in one straight horizontal row at the same height, its six curved branches rising like a fan from the central shaft, seven lamps in all; a soft glow of white-gold light shines gently into the dark tent like a voice calling, with no figure and no face in the light; quiet, holy and hopeful.", seeds=(6, 7, 8)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_d}, open('새그림13d.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('13d', len(items_d), '항목')

# 13e(10-15): 13d의 s13e 시드 7은 등잔대 모양은 좋지만 등잔이 아홉이라, 그 그림을 참조로 바깥 가지 한 쌍만 지워 일곱 등잔으로 고친다
items_e = [
    {"id": "s13e", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3], "참조": ["raw/s13e_s7_aca6aa.png"],
     "프롬프트": "Repaint this exact picture with the same boy, the same tent and the same style, changing only the golden lampstand: remove its two outermost curved branches and their two lamps, so the lampstand has exactly seven lamps, the center one on the main shaft and exactly three on each side. Keep everything else the same."},
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_e}, open('새그림13e.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('13e', len(items_e), '항목')
