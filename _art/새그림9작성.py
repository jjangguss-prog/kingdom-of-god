# 9 여리고 그림 작업 파일(새그림9.json) 만들기 v0.1 (2026-10-12)
# 사용: python 새그림9작성.py → 새그림9.json. 그린 뒤 고르기_9.json으로 모은다.
# 무너진 성벽 배경(bg9fall)은 bg9를 고른 뒤 그 그림을 참조로 따로 그린다.
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
MOSES = "Moses, an elderly prophet with a long white beard, a deep red-brown robe over a cream tunic and a cream headcloth"
JOSHUA = "Joshua, a strong Israelite leader of about thirty with a short dark beard and a determined kind face, wearing a simple tan wool tunic with a brown leather belt, leather bracers and a cream headcloth with a cord"
RAHAB = "Rahab, a kind Canaanite woman of about thirty with long dark hair, wearing a modest long dress with colorful patterned Canaanite weaving and a red headscarf"
SPIES = "two young Israelite spies in plain brown travel cloaks"
PRIESTS = "priests in white linen robes with white headcloths"
# 궤는 행진할 때처럼 청색 보자기로 덮는다(민 4:5–6)
ARK = "the ark of the covenant, a chest completely covered with a plain deep-blue cloth so that nothing of it can be seen, carried on the shoulders of priests by two long wooden poles"
SHOFAR = "long curved ram's horn trumpets"
SHADOW = "small dark wispy shadow creatures holding thin dark strings tied to the guards hover above them like puppeteers"


def scene(i, pr, seeds=(1, 2)):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + END}


items = [
    {"id": "bg9w", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3, 4], "참조": ["ref2/ref9.png"],
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield on the plain of Jericho near the Jordan river, seen from above at a slight angle. "
                 "Keep exactly the same sandy road shapes and positions: the oval road that goes all the way around the city and the winding road from it to the camp on the right. "
                 "Inside the oval ring road, on a low earthen mound, stands the walled city of Jericho: a thick high city wall of sun-dried mud brick on a sloping stone base with a few square towers, "
                 "completely surrounding many small flat-roofed mud-brick houses packed together and a few palm trees inside. The strong wooden city gate is in the left (west) side of the wall, right where the road begins. "
                 "In the front (south) part of the wall facing the viewer, one small house is built into the wall with a window, and a bright scarlet red cord hangs from that window down the outside of the wall. "
                 "At the right end of the road is the Israelite camp of Gilgal with several brown goat-hair tents and a small circle of twelve big river stones; beyond it at the right edge flows the blue Jordan river lined with green reeds and tamarisk trees. "
                 "Everywhere else: the warm green-and-golden plain of Jericho with groves of tall date palm trees, especially in the lower left, small fields of barley, scattered rocks and shrubs; no other water. "
                 "Warm morning light. No characters, no text."},
    scene("s9a", f"on the top of Mount Nebo at sunset, {MOSES}, stands alone leaning on his wooden staff and looks out over the wide promised land below: the green Jordan valley with the river winding through it, the plain with the palm city of Jericho far away, hills beyond and the Dead Sea shining; his face is peaceful and full of hope; warm golden light from the sky."),
    scene("s9b", f"in the camp of Israel on the plains of Moab beside the Jordan river, {JOSHUA}, stands on a low rock before the gathered people of Israel and raises one hand with courage, the tribal elders and families listening; behind him {PRIESTS} stand beside {ARK}; the full river Jordan flows beyond; bright morning light, brave and hopeful."),
    scene("s9c", f"at night under a bright moon, {RAHAB}, leans out of the window of her house, which is built into the high mud-brick city wall of Jericho, and lets {SPIES} down the outside of the wall with a long rope; a bright scarlet cord is tied at the window; palm trees and dark hills around; quiet suspense, child-friendly."),
    scene("s9d", f"the people of Israel cross the Jordan river on dry ground: {PRIESTS} stand firm in the middle of the dry riverbed carrying {ARK}; far upstream the river water stops and rises up in a great heap; families with children, donkeys and flocks walk across the dry riverbed; in front of them march armed warriors of the tribes of Reuben, Gad and half of Manasseh with long bows and round shields; {JOSHUA}, leads them; bright morning light, wonder and joy."),
    scene("s9e", "evening at the Israelite camp of Gilgal on the plain of Jericho among date palm trees: twelve big smooth river stones are set up in a circle as a memorial, children point at them and ask their parents; families sit together around low fires sharing the Passover meal with flat unleavened bread and roasted grain from the land; brown tents behind; warm sunset and lamp light, peaceful."),
    # 여호와의 군대 대장(수 5:13–15)은 사람 모습 없이 빛으로만
    scene("s9f", f"on the plain near the walls of Jericho in the evening, {JOSHUA}, kneels with his face bowed to the ground and his sandals taken off and set beside him, before a tall upright blade-shaped column of dazzling white and golden light standing on the ground like a drawn sword; there is no person, no face and no figure inside the light, only pure light; the ground around glows softly; holy awe and quiet.", (1, 2, 3)),
    scene("s9g", f"the walled city of Jericho on its mound among date palm trees, its great wooden gates shut tight and barred; nervous Canaanite guards with spears and bows stand on top of the high mud-brick walls and look out; {SHADOW}; far away on the plain stand the tents of the Israelite camp; tense but nobody is hurt; late afternoon light."),
    scene("v9a", f"the high mud-brick walls of Jericho crumble and fall down flat in huge billowing clouds of dust, while in front of the city {PRIESTS} blow {SHOFAR} beside {ARK}, and the people of Israel, men, women and children, shout joyfully with raised hands; dark wispy shadow creatures flee up into the sky and break apart; nobody is near the falling walls, nobody is hurt, no blood; warm golden morning light breaking through the dust."),
    scene("v9b", f"after the walls of Jericho have fallen, {SPIES} lead {RAHAB}, and her whole family, her old father and mother, her brothers and sisters and their little children, safely out of her house, which still stands with the bright scarlet cord hanging from its window, while dust settles on the ruins around; relieved, grateful faces; warm light."),
    scene("v9c", f"at the Israelite camp of Gilgal among date palm trees, {RAHAB}, and her family now live peacefully among the people of Israel, sharing bread with Israelite families while their children play together; {JOSHUA}, smiles nearby; the twelve memorial river stones stand in the background; warm golden morning light, joy and welcome."),
    # 가나안 적(c_): 2 아브람의 길의 c_soldier·c_raider와 같은 옷
    {"id": "c_shield", "종류": "인물", "시드": [1, 2], "프롬프트": "A big Canaanite shield bearer of the city of Jericho, a man with curly black hair and a short beard, a rounded bronze helmet, a colorful patterned wool tunic wrapped over one shoulder and a leather belt, holding a tall rectangular wooden shield covered with bronze plates and a short spear, proud chin up, exactly two arms."},
    {"id": "c_centurion", "종류": "인물", "시드": [1, 2], "프롬프트": "A Canaanite captain of the city of Jericho, a stern bearded man with curly black hair, a tall crested bronze helmet and a bronze scale armor shirt over a colorful patterned wool tunic, holding a bronze-headed commander's mace and pointing forward, exactly two arms."},
    {"id": "c_archer", "종류": "인물", "시드": [1, 2], "프롬프트": "A Canaanite archer of the city of Jericho, a lean young man with curly black hair and a short beard, a colorful patterned wool tunic wrapped over one shoulder and a leather belt, a leather quiver of arrows on his back, drawing a curved wooden bow with an arrow aimed forward, narrowed eyes, exactly two arms."},
    # 요단 동편 용사(파수꾼 4단계 B): 망대 파수꾼(watch3)을 바산 현무암 저격 망대로
    {"id": "watch_jordan", "종류": "건물", "크기": [1024, 1024], "시드": [1, 2], "참조": ["raw/watch3_s2_9e6c20.png"],
     "프롬프트": "Draw the special sniper version of this exact watchtower in the same style, colors and camera angle, but rebuilt from dark grey-black basalt stone blocks of Bashan as one tall strong square tower with a flat crenellated top; on top stands a single tall warrior of the tribes east of the Jordan with a short dark beard, a green-and-brown tunic and leather armor, drawing a very long powerful bow and aiming far away, a quiver of long arrows at his side; green and brown banners hang from the tower."},
    # 행렬(수 6:9, 13): 무장한 선봉·후군(같은 그림), 나팔 부는 제사장, 궤를 멘 제사장들
    {"id": "p_soldier", "종류": "인물", "시드": [1, 2], "프롬프트": "An armed Israelite warrior marching silently in the procession around Jericho, a young man with a short dark beard, a rounded bronze helmet, a tan wool tunic with a leather armor vest, holding a spear upright and a round wooden shield, solemn quiet face, mouth closed, walking, exactly two arms."},
    {"id": "p_trumpet", "종류": "인물", "시드": [1, 2], "프롬프트": "An Israelite priest in a white linen robe with a white headcloth and a blue sash, walking while blowing a long curved ram's horn trumpet held up with both hands, cheeks puffed, exactly two arms."},
    {"id": "p_ark", "종류": "무리", "시드": [1, 2, 3], "프롬프트": "Four Israelite priests in white linen robes with white headcloths walk to the right carrying on their shoulders the ark of the covenant, a chest completely covered with a plain deep-blue cloth so that nothing of it can be seen, by two long wooden poles; two priests in front and two behind; solemn quiet faces; each priest has exactly two arms and two legs."},
    # 이스터 에그 물건: 6 요셉의 유골(출 13:19), 8 옥의 철 침상(신 3:11), 9 라합의 붉은 줄(수 2:18, 배경에 안 보일 때)
    {"id": "e_bones", "종류": "물건", "시드": [1, 2], "프롬프트": "A small Egyptian wooden coffin chest painted with simple blue and gold patterns, carefully tied with ropes and resting on a small two-wheeled wooden handcart, a folded linen cloth on top."},
    {"id": "e_bed", "종류": "물건", "시드": [1, 2], "프롬프트": "An enormous heavy iron bed of a giant king, very long and wide, with thick dark iron legs, a plain iron frame and a few iron bars, slightly rusty, empty, simple and huge."},
    {"id": "e_cord", "종류": "물건", "시드": [1, 2], "프롬프트": "A small section of a mud-brick city wall with the window of a house built into it, a bright scarlet red cord tied to the window frame and hanging down the outside of the wall."},
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림9.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 둘째 작업(새그림9b.json): bg9w는 성이 둘레 길의 북쪽을 덮어 버려서, 빈 언덕만 있는 배경과 성을 따로 그린 뒤 여리고합성.py로 합친다.
# 무너진 성(jericho_fall)은 고른 성 그림을 참조로 그려 같은 자리에 합성하므로, 성 밖 배경은 무너지기 전과 똑같다.
items2 = [
    {"id": "bg9base", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3, 4], "참조": ["ref2/ref9b.png"],
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield on the plain of Jericho near the Jordan river, seen from above at a slight angle. "
                 "Keep exactly the same sandy road shapes and positions: the closed oval loop road on the left that goes all the way around, and the winding road from the right side of the loop to the camp on the right. "
                 "Inside the oval loop road there is only a low, wide, bare mound of packed brown earth with a few small stones and dry grass tufts; it is completely empty: no buildings, no walls, no trees on it. "
                 "At the right end of the road is the Israelite camp of Gilgal with several brown goat-hair tents and a small circle of twelve big river stones; beyond it at the right edge flows the blue Jordan river lined with green reeds and tamarisk trees. "
                 "Everywhere else outside the loop: the warm green-and-golden plain of Jericho with groves of tall date palm trees, especially in the lower left, small fields of barley, scattered rocks and shrubs; no other water. "
                 "Warm morning light. No characters, no text."},
    {"id": "jericho", "종류": "건물", "크기": [1536, 1024], "시드": [1, 2, 3, 4],
     "프롬프트": "The ancient walled city of Jericho as one big strategy-map building, wide and low: an oval ring of thick high sun-dried mud-brick city walls on a sloping stone base with six square towers, "
                 "a strong closed wooden city gate in the left end of the wall, and many small flat-roofed mud-brick houses packed close together inside with a few date palm trees. "
                 "In the front wall facing the viewer, one small house is built into the wall with a little window, and a bright scarlet red cord hangs from that window down the outside of the wall. "
                 "The city sits on a low oval earthen mound. Seen from high above at a steep angle like a strategy game map."},
    # 다시: s9d는 강바닥에 물이 남고, s9e는 열두 돌이 불 둘레 돌처럼, s9f는 신을 신은 채로 나와서
    scene("s9d", f"the people of Israel cross the Jordan river on completely dry ground: the riverbed in the middle of the picture is totally dry, cracked mud and smooth stones with no water at all; far upstream in the distance the river water has stopped and stands up in a great heap like a wall; {PRIESTS} stand firm in the middle of the dry riverbed carrying {ARK}; families with children, donkeys and flocks walk across the dry riverbed past them; in front march armed warriors of the tribes of Reuben, Gad and half of Manasseh with long bows and round shields; {JOSHUA}, leads them; bright morning light, wonder and joy.", (3, 4, 5)),
    scene("s9e", "evening at the Israelite camp of Gilgal among date palm trees: in the center stand twelve big smooth grey river stones piled up and standing upright together as one tall memorial monument, not a fire ring; children point at the memorial stones and ask their parents; to the side, families sit around a small separate cooking fire sharing the Passover meal with flat unleavened bread and roasted grain; brown tents behind; warm sunset light, peaceful.", (3, 4)),
    {"id": "p_trumpet", "종류": "인물", "시드": [3, 4, 5], "프롬프트": "An Israelite priest in a white linen robe with a white headcloth and a blue sash, walking while blowing a shofar: a long curved natural ram's horn, cream and light brown colored animal horn with a twisted shape, not metal, not a brass trumpet, held up with both hands, cheeks puffed, exactly two arms."},
    scene("s9f", f"on the plain near Jericho in the evening, {JOSHUA}, barefoot, bows down low with his forehead touching the ground; his two leather sandals have been taken off and lie on the ground beside him; in front of him stands a tall upright blade-shaped column of dazzling white and golden light like a drawn sword; there is no person, no face and no figure inside the light, only pure light; the walls of Jericho far away in the background; holy awe and quiet.", (4, 5, 6)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items2}, open('새그림9b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 셋째 작업(새그림9c.json): 고른 성(jericho 시드 3)을 참조로, 같은 구도에서 성벽만 무너진 그림. 붉은 줄이 걸린 라합의 집 한 칸은 남긴다(수 6:22–23, '더 깊이 보기'에 적음)
items3 = [
    # 1536×1024에 참조까지 넣으면 GPU 메모리가 넘쳐 한 장도 못 끝내서(10-12), 참조를 768×512로 줄이고 1152×768로 그린다. 합성할 때 성 그림 크기로 맞춘다
    {"id": "jericho_fall", "종류": "건물", "크기": [1152, 768], "시드": [1, 2, 3], "참조": ["raw/jericho_s3_768.png"],
     "프롬프트": "Draw this exact same walled city in the same style, colors, size, position and camera angle, keeping the earthen mound, the houses inside and the palm trees the same, except one change: "
                 "the high city walls and towers have collapsed and fallen down flat outward into low heaps of broken mud bricks and stones with a little dust, and the wooden gate has fallen too; "
                 "only one short piece of the front wall still stands: the part with the little window and the bright scarlet cord hanging from it, with the small house behind it unharmed."},
    # 위 참조 편집은 성벽이 금만 가고 서 있어서(10-12), 참조 없이 무너진 성을 따로 그리는 안(fall2)과 더 세게 지시하는 참조 편집(fall3)을 함께 그린다
    {"id": "jericho_fall2", "종류": "건물", "크기": [1536, 1024], "시드": [1, 2, 3, 4],
     "프롬프트": "The ancient city of Jericho right after its walls fell down flat, as one big strategy-map building, wide and low: where an oval ring of high mud-brick city walls stood, there are now only long low heaps of broken mud bricks and stones lying flat on the ground all the way around, with a little drifting dust; "
                 "many small flat-roofed mud-brick houses packed close together inside with a few date palm trees are still standing and are now fully visible; "
                 "in the front, one short piece of wall still stands with a little window and a bright scarlet red cord hanging from it. "
                 "The city sits on a low oval earthen mound. Seen from high above at a steep angle like a strategy game map."},
    {"id": "jericho_fall3", "종류": "건물", "크기": [1152, 768], "시드": [1, 2, 3], "참조": ["raw/jericho_s3_768.png"],
     "프롬프트": "Redraw this city after its walls fell down flat: remove all the tall city walls, towers and the gate completely; in their place draw only low flat heaps of broken mud bricks lying on the ground around the city, so every house inside is fully visible from outside; "
                 "keep the same houses, palm trees, earthen mound, camera angle and style; keep one short piece of the front wall with the little window and the scarlet cord."},
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items3}, open('새그림9c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
