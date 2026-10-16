# 16 시글락 그림 작업 파일(새그림16.json) 만들기 v0.1 (2026-10-16)
# 사용: python 새그림16작성.py → 새그림16.json. 그린 뒤 고르기_16.json으로 모은다.
# 배경(bg16)은 ref2/ref16.png(길 시안)를 참조로 그린다. 아말렉 창병·약탈병·방패병은 7에서 그린 k_ 그대로 쓰고, 낙타 기병·궁수·백부장을 더한다.
# 고르는 기준(10-16 사용자): 인물마다 확대해 이목구비가 뚜렷한가와 팔이 정상인가. 하나라도 어긋나면 다시 그린다.
# 마을은 평평한 지붕의 흙벽돌집(s16b·s16c·s16e). 사람마다 손이 어디 있는지 정해 준다(s16a 아비새의 창과 다윗의 손, s16c 활과 물매, s16f 에봇, v16a 가리키는 손, v16b 안는 팔, v16c 몫을 건네는 손).
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
FACE = " Every face is clear and well drawn with distinct eyes, nose and mouth."
HANDS = " Hands are drawn simply and clearly, each hand with four fingers and a thumb, and no hand overlaps another person."
NOIDOL = " No statues, no idols, no carved figures, no crescent shapes, no moon ornaments, no religious symbols anywhere."
NOBLOOD = " Nobody is wounded, no blood, nobody lying dead."
FLAT = " All houses are one-story mud-brick houses with flat earthen rooftops and low parapets; no sloped roofs, no roof tiles, no red tiles."
SAUL = "King Saul, a very tall handsome Israelite man of about fifty with a dark beard streaked with grey, wearing a simple bronze crown band and a rich deep-blue and purple royal robe"
DAVID = "David, a ruddy Israelite man of about twenty-eight with tousled reddish-brown hair, bright eyes, a handsome kind face and a short reddish-brown beard, wearing a plain light-brown wool tunic with a leather belt, a short sword at his side and sandals"
ABISHAI = "Abishai, a fierce young Israelite warrior with a black beard and a dark red tunic"
ACHISH = "Achish, the Philistine king of Gath, a dignified clean-shaven man of about fifty with a fair face, wearing a tall headdress made of a headband with a neat row of upright reed feathers and a long embroidered blue-and-white robe with a bronze collar"
PHILISTINE = "Philistine lords, clean-shaven men wearing tall headdresses of a headband with a row of upright reed feathers and ribbed bronze corselets"
ABIATHAR = "Abiathar the young priest, a beardless young Israelite man in a white linen robe"
EPHOD = "the ephod, a short sleeveless priestly vest woven of gold, blue, purple and scarlet threads with a round onyx stone on each shoulder"
BOY = "a thin young Egyptian servant of about seventeen with short black hair, brown skin, large dark eyes and a tired gaunt but gentle face, wearing a plain worn white linen kilt and a short white tunic, barefoot"
MEN = "David's men, bearded Israelite men in simple brown and tan wool tunics with leather belts"
LIGHT = "a soft beam of white-gold light from heaven shines down, with no figure and no face in the light"
AMALEK_TENT = "low black goat-hair tents of the desert"


def scene(i, pr, seeds=(1, 2, 3)):
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + HANDS + FACE + END}


items = [
    {"id": "bg16", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3], "참조": ["ref2/ref16.png"],
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield in the dry Negev desert at the brook Besor in bright clear daylight, seen from above at a slight angle. "
                 "Keep exactly the same sandy road shapes and positions: one road enters from the right edge near the top and winds left between low hills, another road enters from the right edge lower down and winds left; "
                 "the two roads meet in the middle and go left across the stream at a shallow ford to a small camp on the left. "
                 "A third road, narrower, rougher and stonier, curves from the camp down the left side, crosses the stream again at a second ford in the lower middle and leaves the picture at the bottom edge. "
                 "The blue line is a thin stream at the bottom of a deep narrow dry ravine with steep crumbling earthen banks running from the top edge to the bottom edge, with a few feathery tamarisk trees growing beside it. "
                 "Left: the camp, several piles of baggage, sacks and clay jars, three tethered donkeys and two small brown tents on pale trampled ground. "
                 "Upper left, far away: a small burned town of flat-roofed mud-brick houses blackened by fire with grey smoke rising into the sky. "
                 "Right side: low rolling sandy hills, dry gullies, rocks and thorny desert bushes; the small green spot on the right is a thorny bush. "
                 "Bottom middle: the brown spot is a stretch of darker rocky ground going down to the south. "
                 "Elsewhere: dry desert ground, small bushes and boulders. Nothing covers the roads. No characters, no people, no text." + FLAT + NOIDOL},
    # 이야기(15→16): 창과 물병(26:9–11) → 시글락을 그에게 주었으므로(27:6) → 좌우 손을 놀려(대상 12:2) → 그는 우리와 함께 싸움에 내려가지 못하리니(29:4) → 울 기력이 없도록(30:4) → 여호와를 힘입고(30:6) → 브솔 시내(30:10)
    scene("s16a", f"at night in King Saul's army camp on a hilltop under a starry sky and a bright moon, {SAUL}, lies fast asleep on his back on a blanket in the middle of the camp, eyes closed; his long spear is stuck upright in the ground beside his head and a round clay water jug stands beside the spear; around him the army commander Abner and several Israelite soldiers lie asleep wrapped in cloaks; "
                  f"{ABISHAI}, crouches beside the sleeping king and grips the king's long spear with both hands to pull it up; {DAVID}, crouches next to Abishai and firmly holds Abishai's forearm with his left hand to stop him, his right hand raised flat in a calm 'no' gesture, shaking his head; quiet, tense, child-friendly moonlit scene." + NOBLOOD),
    scene("s16b", f"in front of the big stone city gate of Gath in Philistia, {ACHISH}, stands kindly and points with his right arm toward the south, his left hand resting on his belt; in front of him {DAVID}, stands respectfully with his right hand on his chest; behind David a long line of his men with their wives, children and loaded donkeys; far away in the sunny southern fields lies a small town of flat-roofed mud-brick houses; bright morning light." + FLAT + NOIDOL),
    scene("s16c", f"at the gate of the small mud-brick town of Ziklag, two Benjamite warriors arrive: the first warrior holds a curved wooden bow in his left hand and draws the bowstring with his right hand, aiming up at the sky; the second warrior swings a leather sling above his head with his right hand and holds a small leather pouch of stones in his left hand; "
                  f"in the open wooden gate {DAVID}, welcomes them with both arms open and a big smile; behind them more warriors walk up the road; bright sunny day." + FLAT),
    scene("s16d", f"in a big Philistine army camp at Aphek with many colorful tents, {PHILISTINE}, stand angrily, one of them pointing with his right arm at a group of Israelite men in brown tunics standing at the back; {ACHISH}, turns his head back toward {DAVID}, with an awkward troubled face, his hands open in apology; in the background columns of Philistine soldiers with spears march past by hundreds; afternoon light." + NOIDOL),
    scene("s16e", f"the burned small town of Ziklag after a raid: several flat-roofed mud-brick houses with blackened walls and empty doorways, thin grey smoke rising from the rooftops into a hazy sky; in front of the houses {DAVID}, and five of {MEN}, sit on the dusty ground and weep loudly with tears on their faces, some covering their faces with both hands, David with his head lifted up and his hands open; no bodies anywhere, no fire monsters." + FLAT + NOBLOOD),
    scene("s16f", f"beside the burned mud-brick town of Ziklag with smoke behind, {DAVID}, kneels on both knees with his head bowed and his hands folded in prayer; in front of him {ABIATHAR}, stands and holds up {EPHOD}, with both hands; {LIGHT} onto David; at the left side three angry men of David's band stand and glare at David, each holding one rock in his right hand down at his side, not throwing." + FLAT + NOBLOOD + NOIDOL),
    scene("s16g", f"at the brook Besor, a deep dry ravine with steep crumbling earthen banks and a thin stream at the bottom with a few tamarisk trees: on the near bank on the left, about ten tired Israelite men sit and rest beside piles of baggage, sacks and tethered donkeys, waving goodbye; down in the ravine {DAVID}, wades across the shallow water, holding a spear in his right hand, leading a long column of his men who climb the far bank on the right; bright hot afternoon in the desert."),
    # 승리 그림 만화(셋): 그가 다윗을 인도하여 내려가니(30:15–16) → 아무것도 잃은 것이 없이(30:18–20) → 같이 분배할 것이니라(30:21–25). 해치는 장면은 그리지 않는다
    scene("v16a", f"at dawn on a rocky desert ridge, {BOY}, stands and points down into the valley with his right arm stretched out, his left arm hanging down at his side; next to him {DAVID}, looks down with a determined face, holding a spear in his left hand; behind them several of {MEN}, come up the ridge; far below on a wide plain lies a big desert camp of {AMALEK_TENT}, with thin smoke of dying campfires, resting camels and heaps of sacks, jars and bundles of plunder; soft pink-gold dawn light." + NOIDOL + NOBLOOD),
    scene("v16b", f"a joyful reunion in a sunny desert field: in the front, a young Israelite mother in a blue dress and headscarf runs into the arms of her bearded husband who hugs her with both arms, and a small boy hugs his father's leg; in the middle {DAVID}, warmly greets his two wives, two women in colorful dresses and headscarves, holding their hands; behind them men drive flocks of white sheep and brown cattle; in the distance a happy crowd of families, small and far away; bright golden light." + NOBLOOD),
    scene("v16c", f"at sunset on the bank of the brook Besor, {DAVID}, stands between two equal heaps of goods, sacks, folded cloth, clay jars and sheep, and with both hands gives a full bag to a tired Israelite man who stands in front of him and receives it with both hands, smiling with thankful eyes; behind him more tired men who stayed with the baggage come forward happily; in the background, small and far away, three grumbling men stand with their arms crossed; warm orange sunset light." + NOBLOOD),
    # 아말렉 겉모습(k_): 낙타 기병(30:17의 소년처럼 젊은이), 궁수, 백부장
    {"id": "k_camel", "종류": "인물", "시드": [1, 2, 3, 4], "프롬프트": "An Amalekite camel raider of the desert: a tall one-humped camel with a woven brown-and-black striped saddle blanket and a bulging cloth sack of plunder hanging on its side, running forward, side view facing right; riding on its back a young Amalekite desert youth with a light beard, a black headcloth with a cord and a dusty brown and black striped cloak, holding a long spear in his right hand and the reins in his left hand, frowning. The whole camel with all four legs and the rider fully visible, the rider has exactly two arms." + NOIDOL},
    {"id": "k_archer", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "An Amalekite archer of the desert, a lean young man with a dark beard, a dusty brown and black striped cloak, a black headcloth with a cord, a leather quiver of arrows on his back, drawing a curved wooden bow with an arrow aimed forward, narrowed eyes, exactly two arms and exactly two hands." + NOIDOL},
    {"id": "k_centurion", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "A stern Amalekite desert chief with a grey beard, a black headcloth with a cord, a richly patterned brown and black striped robe with a wide red sash, holding a long carved wooden staff in his right hand and pointing forward commandingly with his left hand, hard proud face, exactly two arms and exactly two hands." + NOIDOL},
    # 베냐민 궁수(파수꾼 4단계 A): 시글락의 흙벽돌 망대 위 궁수 둘(대상 12:2). 탑 3단계 그림을 참조로
    {"id": "watch_benjamin", "종류": "건물", "시드": [1, 2, 3, 4], "참조": ["raw/watch3_s2_9e6c20.png"],
     "프롬프트": "Draw the rapid-fire version of this exact watchtower in the same style, colors and camera angle, but rebuilt as a square mud-brick watchtower of the desert town Ziklag with a flat earthen roof and a low parapet; on the flat top stand two Benjamite archers side by side: the left archer holds a curved bow in his left hand and draws the string with his right hand, the right archer holds a curved bow in his right hand and draws the string with his left hand, both aiming forward; each archer has exactly two arms; a quiver full of arrows and a leather sling hang on the parapet; a small blue-and-white striped banner on a pole."},
    # 애굽 소년(30:11–15): 쓰러진 모습과 일어나 가리키는 모습(같은 사람)
    {"id": "boy_sick", "종류": "인물", "시드": [1, 2, 3], "프롬프트": BOY + ", lying on his side on the ground, too weak to stand, his head resting on his bent right arm and his left hand on his chest, eyes half closed, thin and tired, side view, whole body visible, exactly two arms and exactly two hands."},
    {"id": "boy_up", "종류": "인물", "시드": [1, 2, 3], "프롬프트": BOY + ", standing up again with new strength, pointing forward and down with his right arm stretched out and his index finger extended, his left arm hanging down at his side, a hopeful determined face, exactly two arms and exactly two hands."},
    # 되찾은 행렬(30:19–20): 소, 엄마와 아이
    {"id": "a_ox", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "A strong friendly brown ox with short curved horns and a pale muzzle, natural healthy anatomy with exactly four legs, calm walking pose, side view facing right, the whole animal visible."},
    {"id": "p_family", "종류": "무리", "시드": [1, 2, 3], "프롬프트": "A young Israelite mother in a long blue dress and a cream headscarf walking happily and holding the hand of her small son of about six in a tan tunic, both smiling with joy; the mother's free hand holds a small bundle; each has exactly two arms and exactly two hands."},
    # 숨은 이야기: 아비가일의 나귀(삼상 25:18)
    {"id": "e_abigail", "종류": "인물", "시드": [1, 2, 3], "프롬프트": "A gentle grey donkey with long ears and kind dark eyes, standing calmly, side view facing right, natural anatomy with exactly four legs; on its back a colorful woven saddle rug loaded with two round wicker baskets full of round loaves of bread, a small wineskin and pressed cakes of dried figs and clusters of raisins tied with cord. No people."},
]
items = items[:1] + [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면' and i['id'] != 'bg16']   # 배경을 먼저(길과 탑 자리를 그림에 맞춰야 해서)
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림16.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 16b(10-16): 손과 사람이 어긋난 것을 다시 그린다 — 새그림16b.json
#   s16a: 아비새가 창을 두 손으로 들지 않고(셋 다) 달이 둘이거나 깬 군사가 창을 쥠 → 아비새가 뽑은 왕의 창을 두 손으로 들고 다윗이 한 손으로 그 팔뚝을 잡음
#   s16c: 베냐민 사람 둘이 다윗과 똑같은 붉은 머리로 나와 다윗이 없음 → 베냐민 사람은 검은 머리와 짙은 초록 옷, 다윗은 성문 안에
#   s16g: 다윗의 창에 날이 둘, 사백 명이 구경하는 아이들처럼 → 창을 든 군사들이 물을 건너 저쪽 비탈을 오름
#   v16b: 아내·아이·다윗의 손이 한데 엉킴 → 앞에는 넷만: 무릎 꿇고 딸을 안은 아버지, 두 아내의 손을 하나씩 잡은 다윗
items_b = [
    scene("s16a", f"at night in King Saul's army camp on a hilltop under a starry sky with one bright full moon. In the middle, {SAUL}, sleeps peacefully on his back on a woven blanket on the ground with his eyes closed, and a round clay water jug stands on the ground beside his head; around him several Israelite soldiers sleep curled up in their cloaks with their eyes closed. "
                  f"On the right, {ABISHAI}, has pulled the king's long spear out of the ground and holds it up with both hands; beside him {DAVID}, firmly holds Abishai's forearm with his right hand to stop him and raises his left hand with the palm open, shaking his head. Quiet, tense, child-friendly moonlit scene." + NOBLOOD, seeds=(11, 12, 13, 14)),
    scene("s16c", f"at the open wooden gate of the small mud-brick town of Ziklag, {DAVID}, stands in the gateway and welcomes newcomers with both arms open and a big smile. In front of him two Benjamite warriors arrive, both with black hair and short black beards, wearing dark green tunics with leather belts: "
                  f"the first warrior holds a curved wooden bow in his left hand and draws the bowstring back with his right hand, aiming up at the sky; the second warrior swings a leather sling above his head with his right hand and holds a small leather pouch of stones in his left hand. Behind them more warriors walk up the dusty road. Bright sunny day." + FLAT, seeds=(11, 12, 13, 14)),
    scene("s16g", f"at the brook Besor, a deep dry ravine with steep crumbling earthen banks and a thin shallow stream at the bottom: on the near bank on the left, six tired bearded Israelite men sit and rest beside piles of baggage, sacks and two tethered donkeys, waving goodbye. "
                  f"In the middle, {DAVID}, wades across the shallow water holding one plain spear upright in his right hand and looks back with a determined face; behind him a long line of bearded Israelite warriors with spears and round shields follow him, some wading through the water and others climbing the far bank on the right. Bright hot afternoon in the desert.", seeds=(11, 12, 13)),
    scene("v16b", f"a joyful reunion in a sunny desert field. On the left, a bearded Israelite man kneels on one knee and hugs his small daughter with both arms, and the little girl hugs his neck. In the middle, {DAVID}, stands smiling with tears of joy and holds one hand of each of his two wives who stand on either side of him: "
                  f"on his right a young woman in a blue dress and white headscarf, on his left a young woman in a green dress and red headscarf. Behind them men drive a flock of white sheep and brown cattle. In the distance a happy crowd of families, small and far away. Bright golden light." + NOBLOOD, seeds=(11, 12, 13, 14)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_b}, open('새그림16b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_b), '항목(16b)', sum(len(i['시드']) for i in items_b), '장')

# 16c(10-16): s16c 16b도 넷 가운데 셋은 두 베냐민 사람이 한 몸처럼 겹치거나 다윗 팔이 넷(시드 13) → 둘을 왼쪽과 오른쪽으로 멀리 떼어 놓고 다윗은 가운데 성문에 — 새그림16c.json
items_c = [
    scene("s16c", f"at the open wooden gate of the small mud-brick town of Ziklag. In the center, {DAVID}, stands in the gateway and welcomes newcomers with both arms open and a big smile. "
                  f"On the far left, well apart from everyone, a Benjamite archer with black hair and a short black beard in a dark green tunic holds a curved wooden bow in his left hand and draws the bowstring back to his cheek with his right hand, aiming up at the sky. "
                  f"On the far right, well apart from everyone, a second Benjamite warrior with black hair and a short black beard in a dark green tunic swings a leather sling above his head with his right hand and holds a small leather pouch of stones at his hip with his left hand. "
                  f"Far behind them more warriors walk up the dusty road, small. Bright sunny day." + FLAT, seeds=(21, 22, 23, 24)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items_c}, open('새그림16c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items_c), '항목(16c)', sum(len(i['시드']) for i in items_c), '장')
# 고른 것은 고르기_16.json. 고르는 기준(10-16 사용자): 인물마다 확대해 이목구비가 뚜렷한가와 팔이 정상인가.
#   bg16 시드 3(세 후보 모두 아래 가운데에 큰 협곡. 북쪽·남쪽 여울이 둘 다 있고 오른쪽에 덤불이 있는 것), s16a 16b 시드 14, s16b 시드 2, s16c 16c 시드 23,
#   s16d 시드 1, s16e 시드 3, s16f 시드 1, s16g 16b 시드 11, v16a 시드 3, v16b 16b 시드 12, v16c 시드 1, watch_benjamin 시드 2(시드 3은 한 궁수가 활을 둘 쥠)
