# 15 엔게디 그림 작업 파일(새그림15.json) 만들기 v0.1 (2026-10-16)
# 사용: python 새그림15작성.py → 새그림15.json. 그린 뒤 고르기_15.json으로 모은다.
# 배경(bg15)은 ref2/ref15.png(길 시안)를 참조로 그린다. 사울(saul)은 14에서 그린 그림을 그대로 쓰고, 창 드는 사울·악령이 내릴 때의 사울을 더한다.
# 고르는 기준(10-16 사용자): 인물마다 확대해 이목구비가 뚜렷한가와 팔이 정상인가. 하나라도 어긋나면 다시 그린다.
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
FACE = " Every face is clear and well drawn with distinct eyes, nose and mouth."
HANDS = " Hands are drawn simply and clearly, each hand with four fingers and a thumb, and no hand overlaps another person."
NOIDOL = " No statues, no idols, no carved figures, no religious symbols anywhere."
NOBLOOD = " Nobody is wounded, no blood."
FLAT = " All houses are one-story mud-brick houses with flat earthen rooftops and low parapets; no sloped roofs, no roof tiles, no red tiles."
SAUL = "King Saul, a very tall handsome Israelite man of about forty, a head taller than everyone else, with a dark beard, wearing a simple bronze crown band and a rich deep-blue and purple royal robe"
DAVID = "David, a ruddy young Israelite man of about twenty with tousled reddish-brown hair, bright eyes, a handsome friendly face and a short light reddish beard, wearing a plain light-brown wool tunic with a leather belt and sandals"
JONATHAN = "Jonathan, the king's son, a brave young prince of about twenty-five with a short dark beard, wearing a fine royal-blue robe with a gold-trimmed sash and a leather belt"
KINNOR = "a small wooden kinnor lyre: a U-shaped wooden frame with two curved arms joined by a crossbar at the top and about eight straight vertical strings; not a lute, not a guitar"
SPIRIT = "a cloud of dark purple smoke hangs around his head and shoulders"
LIGHT = "a soft beam of white-gold light from heaven shines down, with no figure and no face in the light"
ISRAEL_SOLDIER = "an Israelite soldier of King Saul's army, a bearded man wearing a simple rounded bronze helmet, a plain cream-white wool tunic with a brown leather belt, a deep purple sash across his chest, and sandals"


def scene(i, pr, seeds=(1, 2, 3)):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + HANDS + FACE + END}


items = [
    {"id": "bg15", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3], "참조": ["ref2/ref15.png"],
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield at the oasis of En-gedi beside the Dead Sea in bright clear daylight, seen from above at a slight angle. "
                 "Keep exactly the same sandy road shapes and positions: one road enters from the top edge left of the middle and zigzags down a rocky cliff in three switchbacks, another road enters from the top edge on the right and runs down beside the sea, "
                 "crosses a small stream at a shallow ford, and the two roads meet in the lower middle and run to the lower left where the road ends at the dark mouth of a cave in a cliff of tan limestone. "
                 "On the right side: the calm blue-green Dead Sea with white salt crusts along its pebbly shore. "
                 "In the upper right: a thin waterfall falls down a cliff into a small clear pool surrounded by date palm trees and green reeds, and a small stream flows from the pool down to the sea, exactly where the blue line is. "
                 "Upper left: a high dry plateau with several low brown goat-hair tents of an army camp, and a big flat rock outcrop beside them. "
                 "In the middle: steep rocky ledges of tan and ochre limestone with a few wild ibex goats standing on the rocks. "
                 "Below the road near the cave: two small round sheepfolds made of piled stones. "
                 "Elsewhere: dry desert ground, small bushes and boulders. Nothing covers the roads. No characters, no text." + NOIDOL},
    # 이야기(14→15): 천천이요 만만이로다(18:7) → 창은 벽에 박힌지라(19:10) → 화살이 네 앞쪽에(20:37) → 아둘람 굴(22:2) → 그일라를 구원하라(23:2) → 셀라하마느곳(23:26–28) → 들염소 바위로(24:2)
    scene("s15a", f"on a dusty road outside an Israelite town, joyful Israelite women in colorful dresses and headscarves dance and sing, beating round hand drums and shaking small cymbals; behind them the young war hero {DAVID}, walks humbly; in front {SAUL}, rides ahead with a stiff jealous frown, glancing back at David; townspeople cheer from flat rooftops; bright sunny day." + FLAT),
    scene("s15b", f"inside a stone room of the king's house, {DAVID}, sits on a stool by the wall playing {KINNOR} with both hands; across the room {SAUL}, sits on a wooden chair, {SPIRIT}, and he has just thrown a long spear with his right hand; the spear is stuck in the plaster wall beside David's head, and David leans aside to dodge it; dramatic but child-friendly." + NOBLOOD),
    scene("s15c", f"in an open field at morning, {JONATHAN}, draws a curved wooden bow and shoots an arrow far over the head of a small servant boy who runs across the field to fetch it; behind a big gray boulder at the left, {DAVID}, hides quietly and listens; green grass and a few trees; tender, a little sad mood."),
    scene("s15d", f"at the mouth of a big rocky cave in a tan hillside, the cave of Adullam, a crowd of tired poor Israelite men in worn patched clothes arrive with bundles and walking sticks; {DAVID}, stands at the cave entrance and welcomes them warmly with open arms; some men sit to rest, one man clasps David's hand; late afternoon light; hopeful."),
    scene("s15e", f"on a hilltop at dawn, {DAVID}, kneels on one knee with his head bowed and his hands folded in prayer; {LIGHT} onto him; far below in the valley lies a small walled town with flat-roofed houses and a round threshing floor with sheaves of grain; a few of David's men in tunics with spears stand behind him looking worried." + FLAT),
    scene("s15f", f"a rocky desert mountain seen from the side: on the left slope of the mountain {SAUL}, leads a column of Israelite soldiers with spears and round shields, searching; on the right slope, hidden from them by the ridge, {DAVID}, and his men hurry away running; on the top of the ridge a messenger on foot runs toward Saul waving one hand, bringing urgent news; tense but child-friendly." + NOBLOOD),
    scene("s15g", f"the oasis of En-gedi beside the blue Dead Sea: tall tan cliffs with ledges where wild ibex goats leap, a thin waterfall falling into a pool with date palms; in the shadow at the back of a big cave in the cliff, {DAVID}, and several of his men crouch quietly and watch; far away on the high plateau, {SAUL}, leads a long column of many Israelite soldiers with spears toward the cliffs; dramatic wide view."),
    # 승리 그림 만화(셋): 겉옷 자락(24:4–5) → 내 주 왕이여(24:8–11) → 너는 나보다 의롭도다(24:16–17). 해치는 장면은 그리지 않는다
    scene("v15a", f"inside a dark cave, near the bright cave entrance {SAUL}, sits resting on a low rock with his back turned, and his long purple royal robe spreads on the ground behind him; in the shadows {DAVID}, crouches low and quietly cuts off a small corner of the purple robe's hem with a small knife held in his right hand, his left hand holding the cut corner; behind him in the darkness three of his men watch with wide eyes; tense hushed moment." + NOBLOOD),
    scene("v15b", f"outside a cave on a rocky slope at En-gedi: on the path below, {SAUL}, has turned around to look up in surprise, and a few Israelite soldiers with spears stand still behind him; above at the cave mouth {DAVID}, kneels respectfully on one knee and holds up a small corner of purple cloth high in his right hand, his left hand on his chest; bright daylight, the blue Dead Sea in the distance." + NOBLOOD),
    scene("v15c", f"on a rocky path by the Dead Sea at late afternoon, {SAUL}, weeps with tears on his face, his hands open and lowered, and only a thin wisp of purple smoke fades away from his shoulders; in front of him {DAVID}, stands holding the small purple cloth corner in one hand, with a kind sorrowful face; behind Saul his soldiers lower their spears; warm golden light." + NOBLOOD),
    # 보스: 창 드는 사울, 악령이 내릴 때의 사울(saul과 같은 사람, 사람답게)
    {"id": "saul_throw", "종류": "인물", "시드": [1, 2, 3], "프롬프트": SAUL + ", raising a long spear high above his right shoulder with his right hand, about to throw it, his left arm stretched forward for balance, a dark purple smoky aura around his shoulders, angry troubled face, exactly two arms and exactly two hands."},
    {"id": "saul_fit", "종류": "인물", "시드": [1, 2, 3], "프롬프트": SAUL + ", standing and bending forward, holding his head with both hands, eyes squeezed shut, troubled tormented face, a swirling cloud of dark purple smoke around his head and shoulders, a dignified human, not a monster, exactly two arms and exactly two hands, no weapon."},
    # 다윗의 용사들(양치기 4단계 A): 아둘람 굴 막사와 용사(삼하 23)
    {"id": "shep_mighty", "종류": "건물", "시드": [1, 2, 3], "프롬프트": "A small rocky stronghold at the mouth of a cave in a big rounded hill of tan limestone, like the cave of Adullam: a dark cave entrance framed by large stones, a short wall of piled stones with a wooden gate in front, two round bronze-rimmed shields and three long spears leaning by the entrance, a small banner of red cloth on a pole."},
    {"id": "mighty", "종류": "인물", "시드": [1, 2, 3, 4], "프롬프트": "A mighty warrior of King David's band, a strong bearded Israelite man wearing a rounded bronze helmet, a leather scale vest over a dark red tunic and sandals, a round bronze-rimmed shield on his left arm and a long spear held in his right hand, standing firm and ready, brave loyal face, exactly two arms and exactly two hands."},
    # 사울의 군대(이스라엘 겉모습 i_)
    {"id": "i_soldier", "종류": "인물", "시드": [1, 2, 3], "프롬프트": ISRAEL_SOLDIER + ", holding a long spear in his right hand and a small round leather shield on his left arm, angry frown, walking forward, exactly two arms."},
    {"id": "i_shield", "종류": "인물", "시드": [1, 2, 3], "프롬프트": ISRAEL_SOLDIER + ", carrying a big tall rectangular wooden shield covered with leather in front of his body with his left arm and a short spear in his right hand, chin raised proudly, exactly two arms."},
    {"id": "i_centurion", "종류": "인물", "시드": [1, 2, 3], "prompt_note": "천부장·백부장(22:7)", "프롬프트": "An Israelite captain of King Saul's army, a stern bearded man with a polished bronze helmet, a bronze scale breastplate over a cream tunic, a long deep purple cloak, holding a commander's wooden staff in his right hand, hard stubborn face, exactly two arms."},
    {"id": "i_archer", "종류": "인물", "시드": [1, 2, 3], "프롬프트": ISRAEL_SOLDIER + ", a leather quiver of arrows on his back, drawing a curved wooden bow with an arrow aimed forward, narrowed eyes, exactly two arms."},
    {"id": "i_drummer", "종류": "인물", "시드": [1, 2, 3], "프롬프트": ISRAEL_SOLDIER + ", without weapons, beating a round wooden frame drum hanging at his waist with both hands, wide fearful eyes, exactly two arms and exactly two hands."},
    # 숨은 이야기: 엔게디에서부터 그물 치는 곳(겔 47:10)
    {"id": "e_net", "종류": "물건", "시드": [1, 2, 3], "프롬프트": "A small fishing net spread out on a white salty pebble shore at the edge of clear blue-green water, with two shiny silver fish jumping out of the water beside it."},
]
for it in items:
    it.pop('prompt_note', None)
items = items[:1] + [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면' and i['id'] != 'bg15']   # 배경을 먼저(길과 탑 자리를 그림에 맞춰야 해서)
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림15.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 15b(10-16): bg15 세 후보 모두 샘 길 윗부분이 폭포에 덮여서, 시드 2에 빠진 길과 굴 어귀를 칠한 ref2/bg15_edit_ref.png를 참조로 다시 다듬었다.
#   다듬은 시드 11은 길 모양이 조금 바뀌어서 index.html의 15 길·탑 자리(4·5번)·숨은 이야기 자리를 그림에 맞췄다(지도2.json의 15는 처음 시안 그대로 둔다).
# 15c(10-16): 무릎 꿇은 사울(saul_kneel), s15b(14의 s14f를 참조로 창이 벽에 박힘 → 셋 다 창이 다윗 손에 들리거나 사람이 겹쳐 버림),
#   v15c(다윗이 아이처럼 작게 나와서 어른으로) — 새그림15c.json
# 15d(10-16): v15a(셋 다 사울이 다윗 쪽을 보고 있어서, 사울이 등을 돌리고 밝은 어귀를 보게), s15b(창이 날아가는 순간으로) — 새그림15d.json
# 15e(10-16): s15b 시드 22(창이 아직 사울 손에)를 참조로 창이 손을 떠나 벽에 박히게 — 새그림15e.json
# 15f(10-16): s15b 시드 34를 참조로 둥근 몸통의 류트를 U자 틀의 수금으로(14의 s14f와 같은 일) — 새그림15f.json. 고른 것은 s15b 시드 42, v15a 시드 5(잘라 낸 자락과 작은 칼)
# 고른 것은 고르기_15.json. 고르는 기준(10-16 사용자): 인물마다 확대해 이목구비가 뚜렷한가와 팔이 정상인가.
#   s15a 시드 2(가운데 다윗이 또렷, 시드 1은 사울이 탈것 없이 말 탄 자세), s15d 시드 2(시드 1은 굴에 글자, 시드 3은 손이 남의 뺨에),
#   s15e 시드 2(시드 3은 먼 집이 기와 박공지붕), s15f 시드 1(시드 2는 전령이 다윗과 닮음, 시드 3은 전령이 관을 씀),
#   s15g 시드 2(시드 1은 사울 군대가 너무 가깝고, 시드 3은 다윗의 사람 가운데 관을 쓴 사람), v15b 시드 3, v15c 시드 4(어른 다윗).
