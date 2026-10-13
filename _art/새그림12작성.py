# 12 하롯 샘 그림 작업 파일(새그림12.json) 만들기 v0.1 (2026-10-13)
# 사용: python 새그림12작성.py → 새그림12.json. 그린 뒤 고르기_12.json으로 모은다.
# 배경(bg12w)은 ref2/ref12.png(길 시안)를 참조로 그린다. 밤은 코드가 어둡게 하므로 해 질 녘 그림으로 그린다.
# 장막이 길을 덮으면 9·10처럼 빈 골짜기(bg12base)에 장막을 얹거나 그림에 맞춰 길과 탑 자리를 고친다.
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
GIDEON = "Gideon, a humble young Israelite farmer of the tribe of Manasseh, a slim man of about thirty with a short dark-brown beard and kind worried eyes, wearing a plain brown wool tunic with a rope belt and a tan cloak"
PURAH = "his young servant Purah, a teenage boy with short curly black hair in a simple gray tunic"
ISRAEL = "Israelite men in plain brown and tan tunics and headcloths"
# 미디안(삿 6:3): 5 미디안 우물의 m_ 군사와 같은 옷(줄무늬 사막 겉옷, 끈을 두른 머릿수건). 웃음거리로 그리지 않는다. 낙타 목의 초승달 장식(8:21)은 그리지 않는다
MIDIAN = "Midianite desert herdsmen with dark beards, striped desert cloaks and headcloths tied with a cord"
CAMELS = "tall one-humped camels with plain woven saddle blankets and tassels"
NOMOON = " No crescent shapes, no moon ornaments, no religious symbols anywhere."
LIGHT = "the messenger of the LORD is shown only as a tall soft column of bright white-gold light, with no figure, no face, no body and no wings inside the light"


def scene(i, pr, seeds=(1, 2)):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + END}


items = [
    {"id": "bg12w", "종류": "장면", "크기": [1536, 864], "시드": [1, 2], "참조": ["ref2/ref12.png"],
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield in the eastern valley of Jezreel at dusk, seen from above at a slight angle, warm orange evening light with long soft shadows. "
                 "Keep exactly the same sandy road shapes and positions: the two roads that enter from the top edge on the left and on the right of the top middle, the left road that swings wide around the left side and the right road that swings wide around the right side, "
                 "the place in the lower middle where the two roads meet, and the road that then runs to the lower left and ends at the small dark-green area in the lower left corner. "
                 "At the top middle between the two roads, the lower slope of the hill of Moreh, a broad rounded brown-green hill. "
                 "In the big oval valley in the middle of the map, inside the loop of the roads, the huge camp of Midian: very many low black and brown goat-hair tents and many resting camels lying on the ground, filling the valley like a swarm; a few small cooking fires with thin smoke; "
                 "keep the western edge of the camp, a small empty grassy slope left of the middle, free of tents. "
                 "Three small low rocky hills with a few boulders and dry grass: one at the far left edge beside the left road, one at the far right edge beside the right road, and one small hill just below the camp in the lower middle, above the place where the roads meet. "
                 "In the lower left corner, the green foot of Mount Gilboa with the spring of Harod: water bubbling from a cleft in gray rocks into a small clear blue pool with reeds, and a few small Israelite tents of brown wool beside it where the road ends. "
                 "Elsewhere: dry grassy fields, small bushes and stones. Nothing covers the roads. No characters, no text." + NOMOON},
    # 이야기(11→12): 메뚜기 떼(6:5) → 큰 용사여(6:12) → 여호와 살롬(6:21, 24) → 밤에 헌 제단(6:27) → 양털의 이슬(6:40) → 삼백 명(7:6) → 보리떡 꿈(7:13–15)
    scene("s12a", f"Israelite farmland in a green valley at sowing time; from the eastern hills a huge crowd of {MIDIAN} and eastern desert people with countless {CAMELS} and big black goat-hair tents pours into the green fields like a swarm of locusts, and the camels eat the young green crops; in the foreground on the rocky mountainside, a worried Israelite family hides at the mouth of a cave among the rocks and peeks out; dusty and gloomy but child-friendly, nobody is hurt." + NOMOON),
    scene("s12b", f"inside a deep square winepress cut into the rock and hidden among bushes, {GIDEON}, kneels and beats a small pile of wheat with a short wooden stick, then looks up startled; under a great old oak tree beside the winepress, {LIGHT}, shining warmly on him; quiet amazed mood, child-friendly."),
    scene("s12c", f"under a great oak tree, {GIDEON}, kneels on one knee in awe with his hands open; before him, on a flat rock, bright fire bursts up out of the rock and burns up a little meat and round flat unleavened breads; beside it stands a small newly built altar of rough uncut stones; there is no other person; warm golden light, peaceful and holy."),
    scene("s12d", f"at night by the light of two torches on a dark hilltop, {GIDEON}, and a few young Israelite servant men quietly build a new altar of rough uncut stones; beside them lies only a scattered heap of old rubble stones, a broken-down pile; below the hill the flat-roofed village houses are dark and asleep under the stars; secret quiet mood. No statues, no idols, no carved figures, no poles, no symbols anywhere."),
    scene("s12e", f"early dawn on a round stone threshing floor on a hill; {GIDEON}, kneels and touches a white woolly sheep fleece lying in the middle with a surprised face: the fleece is completely dry, while all the ground and grass around it sparkles with fresh dew drops; far below in the valley lie many dark tents of a great desert camp; soft pink morning light, wonder." + NOMOON),
    scene("s12f", f"at the spring of Harod at the green foot of Mount Gilboa, water flows from gray rocks into a stream; many {ISRAEL}, kneel down at the water and drink with their faces near the water, while a few men stand bent and scoop up water in one hand to their mouth to lap it; {GIDEON}, stands on a rock and watches closely; in the background, a long line of other men walks away home over the hills; bright morning light, calm."),
    scene("s12g", f"at night at the edge of a huge desert camp of black goat-hair tents, {GIDEON}, and {PURAH}, crouch hidden in the shadow behind a tent and listen; in front of the tent, two {MIDIAN}, sit by a small campfire; one tells his dream with wide eyes and an open hand, the other listens thoughtfully with his hand on his beard; in the campfire smoke above them floats a faint dreamy picture of a round barley loaf tumbling into a tent; the Midianites are dignified, not funny; starry sky, quiet suspense." + NOMOON),
    # 승리 만화: 여호와와 기드온의 칼이다(7:20) → 오렙과 스엡을 사로잡아(7:25) → 여호와께서 너희를 다스리시리라(8:23). 해치는 장면은 그리지 않는다. 하나님은 빛으로만
    scene("v12a", f"night; on three low hills around a dark valley, three groups of {ISRAEL}, stand still in their places, each man holding a blazing torch high in his left hand and blowing a ram's horn trumpet held in his right hand; broken pieces of clay jars lie at their feet; below in the valley the great Midianite camp of black tents is in confusion: tents shake and fall, and camels and people run away into the darkness; nobody is hit and nobody is hurt; nobody holds a sword." + NOMOON),
    scene("v12b", f"dawn at a shallow river crossing of the Jordan with reeds and willows; Israelite men of Ephraim in tan tunics lead away two captured Midianite princes whose hands are tied in front of them with rope: one prince wears a long black cloak trimmed with black feathers, the other wears a gray wolf skin over his shoulders; they walk with their heads down, nobody is hurt; calm soft morning light." + NOMOON),
    scene("v12c", f"in a village square, a crowd of Israelite men, women and children gather around {GIDEON}, and an elder holds out a golden crown on a small cushion, asking him to be king; Gideon gently refuses with his left hand raised palm out, and points up to the sky with his right hand, where bright golden light shines down through the parting clouds; the people look up to the light; hopeful peaceful light."),
    # 새 적과 보스
    {"id": "m_camel", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "A Midianite camel rider: a tall one-humped camel with a woven red-and-brown saddle blanket and tassels, running forward, side view facing right; riding on its back a Midianite desert raider with a dark beard, a striped desert cloak and a headcloth tied with a cord, holding a long spear, frowning. The whole camel with all four legs and the rider fully visible." + NOMOON},
    {"id": "m_archer", "종류": "인물", "시드": [1, 2], "프롬프트": "A Midianite archer of the desert, a lean young man with a dark beard, a striped brown desert cloak, a headcloth tied with a cord, a leather quiver of arrows on his back, drawing a curved wooden bow with an arrow aimed forward, narrowed eyes, exactly two arms." + NOMOON},
    {"id": "oreb", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "Oreb, a prince of Midian, a tall dignified man of about forty-five with a black beard and sharp dark eyes, wearing a long black cloak trimmed with glossy black feathers on the shoulders and collar over a deep purple robe, gold earrings and a black headcloth tied with a gold cord, holding a tall dark wooden staff in his right hand, walking proudly, stern but noble face, exactly two arms." + NOMOON},
    {"id": "zeeb", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "Zeeb, a prince of Midian, a big strong man of about forty with a thick dark beard, wearing a gray wolf fur cloak over his shoulders over a red striped robe, riding a tall one-humped camel with a rich woven saddle blanket and tassels, holding a curved wooden staff, fierce proud face, side view facing right. The whole camel with all four legs and the rider fully visible." + NOMOON},
    # 인물: 기드온(NPC, 나팔과 항아리), 삼백 용사(왼손 횃불·오른손 나팔, 삿 7:20)
    {"id": "gideon", "종류": "인물", "시드": [1, 2, 3], "프롬프트": GIDEON + ", standing, holding a long curved ram's horn trumpet in his right hand and a round clay jar in his left hand, brave face, exactly two arms and exactly two hands."},
    {"id": "p_torch", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "One of Gideon's three hundred men, a young Israelite man with a short dark beard in a plain brown tunic and a tan headcloth, standing still in his place, holding a blazing torch high in his left hand and blowing a ram's horn trumpet held in his right hand, broken clay jar pieces at his feet, exactly two arms and exactly two hands."},
    # 숨은 이야기: 보리떡 한 덩어리(삿 7:13)
    {"id": "e_loaf", "종류": "물건", "시드": [1, 2], "프롬프트": "One round flat loaf of rustic barley bread, golden brown with a rough cracked floury crust, lying on its side."},
]
items = [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면' and i['id'] != 'bg12w'] + items[:1]   # 게임에 바로 쓰는 인물·물건 먼저, 참조가 있는 배경은 마지막에
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림12.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 둘째 작업(새그림12b.json): 기드온·삼백 용사·v12a의 나팔이 놋쇠 나팔로 나와서(10-13, 9의 p_trumpet과 같은 일) 양각 나팔로, s12g는 기드온과 부라가 함께 숨어 듣게(7:11) 다시 그린다
SHOFAR = "a shofar: a long curved natural ram's horn, cream and light brown colored animal horn with a twisted shape, not metal, not a brass trumpet"
items2 = [
    {"id": "gideon", "종류": "인물", "시드": [4, 5, 6], "프롬프트": GIDEON + ", standing, holding " + SHOFAR + ", in his right hand, and a round clay jar in his left hand, brave face, exactly two arms and exactly two hands."},
    {"id": "p_torch", "종류": "인물", "시드": [4, 5, 6], "프롬프트": "One of Gideon's three hundred men, a young Israelite man with a short dark beard in a plain brown tunic and a tan headcloth, standing still in his place, holding a blazing torch high in his left hand and blowing " + SHOFAR + ", held in his right hand, broken clay jar pieces at his feet, exactly two arms and exactly two hands."},
    scene("v12a", f"night; on three low hills around a dark valley, three groups of {ISRAEL}, stand still in their places, each man holding a blazing torch high in his left hand and blowing {SHOFAR}, held in his right hand; broken pieces of clay jars lie at their feet; below in the valley the great Midianite camp of black tents is in confusion: tents shake and fall, and camels and people run away into the darkness; nobody is hit and nobody is hurt; nobody holds a sword." + NOMOON, (3, 4, 5)),
    scene("s12g", f"at night at the edge of a huge desert camp of black goat-hair tents, two Israelites crouch side by side hidden in the shadow behind a tent and listen: {GIDEON}, and beside him {PURAH}; in front of the tent, two {MIDIAN}, sit by a small campfire; one tells his dream with wide eyes and an open hand, the other listens thoughtfully with his hand on his beard; in the campfire smoke above them floats a faint dreamy picture of a round barley loaf tumbling into a tent; the Midianites are dignified, not funny; starry sky, quiet suspense." + NOMOON, (3, 4, 5)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items2}, open('새그림12b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 셋째 작업(새그림12c.json): v12b 시드 1·2는 사로잡힌 방백이 셋처럼 보이고 스엡이 수염 없는 젊은이로 나와서(10-13), 두 방백을 게임 그림(oreb·zeeb)과 같은 모습으로 또렷이 다시 그린다.
# 삼백 용사(12b 시드 4–6)는 양각 나팔이 손에 들리지 않고 입에만 붙어 있어서, 오른손으로 나팔을 입에 대고 부는 모습으로 한 번 더
items3 = [
    {"id": "p_torch", "종류": "인물", "시드": [7, 8, 9], "프롬프트": "One of Gideon's three hundred men, a young Israelite man with a short dark beard in a plain brown tunic and a tan headcloth, standing still in his place; his left hand holds a blazing torch high above his head; his right hand grips " + SHOFAR + ", and holds it to his lips to blow it; broken clay jar pieces at his feet, exactly two arms and exactly two hands, both hands holding something."},
    scene("v12b", "dawn at a shallow river crossing of the Jordan with reeds and willows; two Israelite men of Ephraim in plain tan tunics walk in front and lead away exactly two captured Midianite princes by a rope: the first prince, Oreb, a tall man with a black beard in a long black cloak trimmed with black feathers over a deep purple robe; the second prince, Zeeb, a big strong man with a thick dark beard wearing a gray wolf fur cloak over a red striped robe; both princes have their hands tied in front of them and walk with their heads down; nobody is hurt; calm soft morning light." + NOMOON, (3, 4, 5)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items3}, open('새그림12c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 넷째 작업(새그림12d.json, 10-14 사용자: 남은 아쉬운 점을 모두 고친다)
#   v12a: 가운데 사람이 횃불을 둘 들어서 사람마다 왼손 횃불 하나, 오른손 양각 나팔 하나로(7:20)
#   v12b: 두 방백만 나와서 앞에서 줄을 잡고 이끄는 에브라임 사람 둘까지(7:24–25)
#   s12d·v12c: 집이 유럽풍 박공지붕이라 평평한 지붕의 흙벽돌·돌집으로
#   purah: 부라를 코드 그림 대신 게임 그림으로(남쪽 언덕에서 기드온 곁에, 7:10–11)
TOWN = "small ancient Near Eastern houses of mud brick and rough stone with flat roofs, no pitched roofs, no roof tiles, no timber framing, no chimneys"
items4 = [
    scene("v12a", f"night; on three low hills around a dark valley, three groups of {ISRAEL}, stand still in their places; every man holds exactly one blazing torch high in his left hand and exactly one {SHOFAR}, in his right hand, pressed to his lips; no man holds two torches; broken pieces of clay jars lie at their feet; below in the valley the great Midianite camp of black tents is in confusion: tents shake and fall, and camels and people run away into the darkness; nobody is hit and nobody is hurt; nobody holds a sword." + NOMOON, (6, 7, 8, 9)),
    scene("v12b", "dawn at a shallow river crossing of the Jordan with reeds and willows; four people walk together on a sandy path: in front, two Israelite men of Ephraim in plain tan tunics and headcloths, one of them holding the end of a rope; behind them follow exactly two captured Midianite princes whose wrists are tied with that rope: Oreb, a tall man with a black beard in a long black cloak trimmed with black feathers over a deep purple robe, and Zeeb, a big strong man with a thick dark beard wearing a gray wolf fur cloak over a red striped robe; the princes walk with their heads down; nobody is hurt; calm soft morning light." + NOMOON, (6, 7, 8, 9)),
    scene("s12d", f"at night by the light of two torches on a dark hilltop, {GIDEON}, and a few young Israelite servant men quietly build a new altar of rough uncut stones; beside them lies only a scattered heap of old rubble stones, a broken-down pile; below the hill lies a dark sleeping village of {TOWN}, under the stars; secret quiet mood. No statues, no idols, no carved figures, no poles, no symbols anywhere.", (3, 4, 5)),
    scene("v12c", f"in the square of an ancient Israelite town of {TOWN}, a crowd of Israelite men, women and children gather around {GIDEON}, and an elder holds out a golden crown on a small cushion, asking him to be king; Gideon wears no crown; he gently refuses with his left hand raised palm out toward the crown, and points up to the sky with his right hand, where bright golden light shines down through the parting clouds; the people look up to the light; hopeful peaceful light.", (3, 4, 5)),
    {"id": "purah", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "Purah, the young servant of Gideon, an Israelite teenage boy of about fifteen with short curly black hair and no beard, wearing a simple gray-and-tan wool tunic with a rope belt and sandals, standing quietly and attentively with both hands empty at his sides, a little worried but faithful face, exactly two arms and exactly two hands."},
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items4}, open('새그림12d.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 다섯째 작업(새그림12e.json, 10-14): 12d에서도 v12a는 가운데 사람이 횃불을 둘 들거나 나팔이 횃불처럼 나와서, 앞쪽 한 언덕의 세 사람을 크게 그리는 구도로 바꾸고 삼백 용사 그림(p_torch 시드 9)을 참조로 준다.
#   v12b는 에브라임 사람이 아이처럼 나와서 수염 난 어른으로, s12d는 아래 마을이 아직 박공지붕이고 종들이 아이처럼 나와서 상자 모양의 평평한 흙벽돌집과 어른 종으로
TORCHMAN = "raw/p_torch_s9_0e7584.png"
V12A = f"night; in the foreground on a low rocky hill, three Israelite men of Gideon's three hundred stand side by side in their places, each one looking like the man in the reference picture: his left hand holds one blazing torch high, his right hand holds {SHOFAR}, to his lips; each man holds only one torch and only one horn; broken clay jars lie at their feet; far away on two other dark hills glow the small torch lights of the other two companies; below in the valley the great Midianite camp of black tents is in confusion: tents shake and fall, camels and people run away into the darkness; nobody is hit and nobody is hurt; nobody holds a sword." + NOMOON
items5 = [
    dict(scene("v12a", V12A, (10, 11, 12, 13)), 참조=[TORCHMAN]),
    scene("v12a", V12A.replace("each one looking like the man in the reference picture: ", ""), (10, 11, 12)),
    scene("v12b", "dawn at a shallow river crossing of the Jordan with reeds and willows; four grown men walk together on a sandy path: in front, two strong adult Israelite soldiers of Ephraim with short dark beards, in plain tan tunics and headcloths, one of them holding the end of a rope; behind them follow exactly two captured Midianite princes whose wrists are tied with that rope: Oreb, a tall man with a black beard in a long black cloak trimmed with black feathers over a deep purple robe, and Zeeb, a big strong man with a thick dark beard wearing a gray wolf fur cloak over a red striped robe; the princes walk with their heads down; nobody is hurt; calm soft morning light; no children." + NOMOON, (10, 11, 12, 13)),
    scene("s12d", f"at night by the light of two torches on a dark hilltop, {GIDEON}, holds a torch while four grown Israelite servant men with beards quietly build a new altar of rough uncut stones; beside them lies only a scattered heap of old rubble stones, a broken-down pile; far below the hill lies a small dark sleeping village of box-shaped mud-brick houses with completely flat roofs like an ancient Middle Eastern village, no pitched roofs, no gables, no roof tiles, no chimneys; stars above; secret quiet mood; no children. No statues, no idols, no carved figures, no poles, no symbols anywhere.", (6, 7, 8, 9)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items5}, open('새그림12e.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
