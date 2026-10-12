# 10 기브온 그림 작업 파일(새그림10.json) 만들기 v0.1 (2026-10-12)
# 사용: python 새그림10작성.py → 새그림10.json. 그린 뒤 고르기_10.json으로 모은다.
# 배경(bg10w)은 ref2/ref10.png(길 시안)를 참조로 그린다. 성이 길을 덮으면 여리고처럼 빈 언덕에 성을 따로 얹는다.
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
JOSHUA = "Joshua, a strong Israelite leader of about thirty with a short dark beard and a determined kind face, wearing a simple tan wool tunic with a brown leather belt, leather bracers and a cream headcloth with a cord"
PRIESTS = "priests in white linen robes with white headcloths"
ARK = "the ark of the covenant, a chest completely covered with a plain deep-blue cloth so that nothing of it can be seen, carried on the shoulders of priests by two long wooden poles"
# 기브온 사람(히위 족속, 수 9:7): 처음에는 해어진 옷으로 속이고, 나중에는 깨끗한 옷으로 제단을 섬긴다. 웃음거리로 그리지 않는다
GIBEON_OLD = "a small group of Gibeonite men, Hivite people of the hill country with dark curly hair and beards, wearing worn-out patched travel cloaks and cracked mended old sandals, with old torn and patched wineskins on their tired donkeys"
GIBEON = "Gibeonite men and women, Hivite people of the hill country with dark curly hair, wearing clean simple wool clothes in blue, ochre and cream"
CITY = "the walled city of Gibeon on a round rocky hilltop, with strong pale limestone walls, square towers and many flat-roofed stone houses inside"


def scene(i, pr, seeds=(1,)):   # GPU를 다른 프로그램과 나눠 써서 한 장에 몇 분씩 걸려(10-12), 한 장씩 그리고 고칠 것만 다시 그린다
    return {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr + END}


items = [
    {"id": "bg10w", "종류": "장면", "크기": [1536, 864], "시드": [1], "참조": ["ref2/ref10.png"],   # 시드 1이 길을 잘 따라서(성문으로 오르는 공유 길만 그림에 맞춰 지도2.json을 고침) 더 그리지 않는다
    
     "프롬프트": "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield in the rocky hill country of Benjamin around the city of Gibeon, seen from above at a slight angle. "
                 "Keep exactly the same sandy road shapes and positions: the long winding switchback road on the left that climbs up from the valley in the lower left, the road that comes up from the bottom and curves around on the right, and the shared road that leads up to the city gate at the upper right. "
                 "At the upper right, on a round rocky hilltop, stands the walled city of Gibeon with strong pale limestone walls, square towers and many flat-roofed stone houses packed inside; its wooden city gate faces the lower left, exactly where the road ends; nothing covers the roads. "
                 "Just to the right of and below the city, a large round open pool cut deep into the rock with stone steps spiraling down to dark blue water. "
                 "On the left, the slope is covered with stone-walled terraced fields and olive trees between the bends of the switchback road; in the lower left corner, the green fertile valley of Aijalon with small fields. "
                 "In the upper middle, a small bare rocky knoll. Elsewhere: pale limestone hill country with olive groves, small vineyards, scattered boulders and shrubs; no river, no lake. "
                 "Warm morning light. No characters, no text."},
    # 이야기(9→10): 아간과 아이(7–8) → 에발 산(8:30–35) → 기브온의 꾀와 맹세(9) → 다섯 왕과 밤의 행군(10:1–9)
    scene("s10a", "inside a brown goat-hair tent at night by the light of a small clay oil lamp, Achan, an Israelite man with a brown beard in a plain striped tunic, nervously digs a hole in the dirt floor of the tent and hides inside it a beautiful embroidered colorful robe, a small pile of silver pieces and one gold bar, glancing worriedly over his shoulder at the tent door; tense quiet mood, child-friendly."),
    scene("s10b", f"at dawn on a rocky hill facing the small walled city of Ai in the distance, {JOSHUA}, stands on a big rock and stretches out his arm holding a short javelin, pointing it toward the city; behind him the Israelite soldiers wait ready and hopeful; the sky glows pink and gold with sunrise; no fighting, no fire."),
    scene("s10c", f"two big green hills facing each other, Mount Ebal and Mount Gerizim; on the slope stands a plain altar of rough uncut natural field stones with thin white smoke; in the valley between the hills {PRIESTS} stand around {ARK}; {JOSHUA}, reads aloud from a large open scroll; the whole people of Israel, men, women, children and foreign travelers in different colorful clothes, stand on both hillsides listening; bright clear day."),
    scene("s10d", f"at the Israelite camp of Gilgal among brown goat-hair tents, {GIBEON_OLD}, bow politely and show {JOSHUA}, and the gray-bearded Israelite elders their dry crumbly bread covered with spots of green mold, as if they had traveled from a very far country; the elders lean in curiously; warm afternoon light, gentle and respectful, nobody is laughed at."),
    scene("s10e", f"at the camp of Gilgal, {JOSHUA}, and the gray-bearded Israelite elders, each raising one right hand to swear an oath, make a peace treaty with the dusty Gibeonite travelers in patched cloaks, who smile with relief; one elder holds a piece of their dry old bread; brown tents behind; warm golden light."),
    scene("s10f", f"on a hillside near {CITY}, {GIBEON}, carry bundles of chopped firewood on their backs and big clay water jars on their shoulders, climbing up from a large round stone pool with steps cut into the rock toward a simple stone altar where white smoke rises to the sky; {PRIESTS} gratefully receive the wood and water; working together in peace; warm morning light."),
    scene("s10g", f"night: by torchlight the army of Israel marches quickly up a steep winding mountain road through the dark hills, {JOSHUA}, at the front holding up a torch and pointing ahead; far away on a moonlit hilltop {CITY} is surrounded by the many small campfires of an enemy army camp; stars above; urgent but hopeful, child-friendly."),
    # 승리 만화: 큰 덩이 돌(10:11) → 태양아 머무르라(10:12–13) → 여호와의 제단을 위하여(9:27). 맞는 사람은 그리지 않는다. 하나님은 구름과 빛으로만
    scene("v10a", "a long steep winding mountain road going down a rocky slope with stone terraces; from dark storm clouds above, huge round white hailstones fall like rain onto the slope and bounce on the rocks; far below in the distance a small army of Amorite soldiers in red tunics runs away down the road, seen from behind, tiny, nobody is hit, nobody is hurt; dark wispy shadow creatures break apart and flee up into the sky; in the foreground on the hilltop Israelite soldiers watch in awe; golden sunlight breaks through the clouds on one side."),
    scene("v10b", f"{JOSHUA}, stands on a rocky hilltop with both of his arms raised high toward the sky, praying, his face looking up; on the right side of the sky, above {CITY}, blazes a bright golden sun; on the left side of the sky, above a green valley with small fields, hangs a pale white full moon in the blue daytime sky; the Israelite soldiers below look up in wonder; brilliant golden light. Joshua has exactly two arms and exactly two hands.", (1, 2)),
    scene("v10c", f"in front of the open wooden gate of {CITY}, {GIBEON}, joyfully welcome {JOSHUA}, and the Israelites; Gibeonite men carry bundles of firewood and big clay water jars together with Israelites toward a simple stone altar with rising white smoke; children wave and smile; warm golden evening light, peace and friendship."),
    # 아모리 적(o_): 8 에드레이의 o_soldier와 같은 옷(뾰족한 청동 투구, 붉은색·크림색 옷)
    {"id": "o_archer", "종류": "인물", "시드": [1], "프롬프트": "An Amorite archer of the five kings, a lean young man with a black beard, a pointed bronze helmet, a short red-and-cream tunic with a leather belt, a leather quiver of arrows on his back, drawing a curved wooden bow with an arrow aimed forward, narrowed eyes, exactly two arms."},
    {"id": "o_drummer", "종류": "인물", "시드": [1, 2], "프롬프트": "An Amorite war drummer of the five kings, a stocky man with a black beard, a pointed bronze helmet, a short red-and-cream tunic with a leather belt, a big round frame drum of stretched hide hanging in front of his belly from a strap over his shoulder, beating the drum with two short wooden drumsticks, mouth open shouting, wide fearful eyes, exactly two arms."},
    # 기도하는 여호수아(수 10:12): 고른 여호수아 그림을 참조로 자세만 바꾼다(손 든 모세와 같은 방법)
    {"id": "joshua_pray", "종류": "인물", "크기": [1024, 1024], "시드": [1, 2], "참조": ["raw/joshua_s3_45162d.png"],
     "프롬프트": "Redraw this same Joshua in the same style, colors and camera angle with a new pose: he lifts both of his arms straight up high above his head in prayer with both hands open and empty; his sword is put away in its sheath at his belt and there is no shield. He has exactly two arms and exactly two hands, no other hands. His face looks up to heaven."},
    # 숨은 이야기 물건: 기브온 큰 못 곁의 물동이(수 9:27)
    {"id": "e_jar", "종류": "물건", "시드": [1], "프롬프트": "A big round clay water jar of ancient Gibeon with two handles, full of water with a little water splashing over the rim, standing beside a small bundle of chopped firewood tied with rope."},
]
items = [i for i in items if i['종류'] != '장면'] + [i for i in items if i['종류'] == '장면' and i['id'] != 'bg10w'] + items[:1]   # 게임에 바로 쓰는 인물·물건 먼저, 참조가 있는 배경(한 장에 6분쯤)은 마지막에
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림10.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목', sum(len(i['시드']) for i in items), '장')

# 둘째 작업(새그림10b.json): s10a는 아간이 둘로, s10e는 맹세 장면에 기브온 사람이 빠져 나와서(10-12) 다시 그린다
items2 = [
    scene("s10a", "inside a brown goat-hair tent at night by the light of one small clay oil lamp on the ground: one single Israelite man named Achan, all alone, with a brown beard and a plain striped tunic, kneels and nervously hides a beautiful embroidered colorful robe, a small pile of silver pieces and one gold bar in a hole dug in the dirt floor, glancing worriedly over his shoulder at the closed tent flap; nobody else is in the tent; tense quiet mood, child-friendly.", (2, 3)),
    scene("s10e", f"at the Israelite camp of Gilgal among brown goat-hair tents: on the left side, three Gibeonite travelers with dark curly hair and beards in worn-out patched cloaks stand beside their tired donkeys with old cracked wineskins, smiling with relief; on the right side, {JOSHUA}, and three gray-bearded Israelite elders face them, each raising his right hand to swear an oath of peace; on the ground between the two groups lies a small basket of dry crumbly bread with green mold spots; warm golden light.", (1, 2)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items2}, open('새그림10b.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 셋째 작업(새그림10c.json): s10a 시드 2는 감춘 은과 금이 그림 맨 아래라 이야기 글 상자에 가려서(10-12), 물건을 그림 가운데에 두고 다시 그린다
items3 = [
    scene("s10a", "inside a brown goat-hair tent at night by the light of one small clay oil lamp: one single Israelite man named Achan, all alone, with a brown beard and a plain striped tunic, kneels behind a shallow hole dug in the dirt floor and nervously hides in it a beautiful embroidered colorful robe, a small pile of shining silver pieces and one gold bar, glancing worriedly over his shoulder at the closed tent flap; the hole with the robe, the silver and the gold is right in the center of the picture at the height of the man's waist, seen from the front at eye level; the bottom third of the picture is only plain dark dirt floor; nobody else is in the tent; tense quiet mood, child-friendly.", (4, 5, 6)),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items3}, open('새그림10c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
