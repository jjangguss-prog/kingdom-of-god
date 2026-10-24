# 숨은 이야기(이스터 에그) 새 그림 작업 파일(새그림에그.json) 만들기 v0.1 (2026-10-24)
# 사용: python 새그림에그작성.py → 새그림에그.json. 그린 뒤 고르기_에그.json으로 모은다.
# 10-24 사용자: "스테이지마다 Easter Egg 요소가 있으면 좋겠어. 나아만 같은 요소가 아주 좋았다고 생각해" → 에그가 없던 1·2·3·4·5·7과 특별 21·22·23에 나아만처럼 여러 번 눌러 이야기가 이루어지는 에그.
# 3(소돔 왕의 물품)은 e_spoils와 spoil_* 낱개, 23의 무기는 spoil_*, 21의 사자는 a_lion을 다시 쓴다.
# 고르는 기준(10-16 사용자): 인물마다 확대해 이목구비가 뚜렷한가와 팔이 정상인가. 하나라도 어긋나면 다시 그린다.
import json
NOIDOL = " No statues, no idols, no carved figures, no calves, no crescent shapes, no moon ornaments, no religious symbols anywhere."
ARMS = " Exactly two arms and exactly two hands, each hand with four fingers and a thumb."
FACE = " The face is clear and well drawn with distinct eyes, nose and mouth."
REBEKAH = ("Rebekah, a kind young woman of about sixteen from Haran in Mesopotamia, long dark braided hair under a light sand-colored headscarf, "
           "wearing a simple long rose-red dress with a woven brown belt and leather sandals")
SLAVE = ("a Hebrew brick-maker in ancient Egypt, a thin man of about thirty with a short black beard and a plain white cloth headband, "
         "wearing a rough knee-length off-white linen tunic with a rope belt, bare feet")
GIRL = "an Israelite girl of about eight in the wilderness, wearing a plain light-blue tunic with a rope belt and a cream headscarf over dark hair"


def man(i, pr, kind="인물", seeds=(1, 2, 3)):
    return {"id": i, "종류": kind, "시드": list(seeds), "프롬프트": pr}


items = [
    # 1 방주: 느린 거북 한 쌍(창 7:4, 9–10)
    man("e_tortoise", "Two small friendly tortoises, a pair walking slowly side by side, one a little behind the other, rounded brown domed shells with a simple hexagon pattern, "
        "olive-green heads and legs, sleepy happy eyes. Natural healthy anatomy, each tortoise has exactly four short legs and one head, side view walking to the right, both animals fully visible."),
    # 2 아브람의 길: 리브가와 낙타 열 필(창 24:10–22)
    man("e_camel", "A friendly adult dromedary camel with one hump, sandy tan fur, no rider and no saddle, a plain rope halter, standing and bending its long neck down low to drink. "
        "Natural healthy anatomy with exactly four legs, side view facing right, the whole animal visible."),
    man("e_rebekah", REBEKAH + ", tilting a big round clay water jar down from her shoulder with both hands and pouring a stream of clear water downward in front of her, kind cheerful smile." + ARMS + FACE),
    man("e_rebekah_glad", REBEKAH + ", now wearing a small gold nose ring and a pair of shiny gold bracelets on her wrists, holding an empty clay water jar against her hip with one hand "
        "and lifting the other hand to look at her gold bracelet, surprised happy smile." + ARMS + FACE),
    # 4 갈대 상자: 벽돌 굽는 사람의 탄식(출 1:14, 2:23–25)
    man("e_brick", SLAVE + ", kneeling on wet brown mud and pressing mud into a small open wooden rectangular brick mold with both hands, a short row of drying mud bricks beside him, "
        "tired sad face with his head bowed." + ARMS + FACE + " No whips, no wounds, nobody else."),
    man("e_brick_up", SLAVE + ", kneeling upright beside a short row of mud bricks and a small wooden brick mold, lifting his face up toward the sky with a hopeful peaceful expression, "
        "both open hands raised a little at chest height." + ARMS + FACE + " No whips, no wounds, nobody else."),
    # 5 미디안 우물: 네 손에 있는 것이 무엇이냐(출 4:2–4)
    man("e_staff", "A long plain wooden shepherd's staff with a curved crook at the top, lying diagonally across a small flat sandy desert rock, with a little tuft of dry grass beside it. No people.", "물건"),
    man("e_serpent", "A cartoon snake for a children's game, friendly and surprised with big round eyes, olive-brown back with a sandy-yellow belly, coiled in an S-shape and raising its head, "
        "mouth closed, no fangs, exactly one head, no legs.", "물건"),
    # 7 르비딤: 일곱째 날에는 만나가 없었다(출 16:22–30)
    man("e_gatherer", GIRL + ", kneeling on sandy ground and happily picking up small round white grains from the ground into a woven reed basket with both hands, the basket has some small white grains in it." + ARMS + FACE),
    man("e_gatherer_rest", GIRL + ", sitting peacefully on a small woven mat with her legs folded, beside a woven reed basket full of small round white grains, her hands folded in her lap, "
        "eyes gently closed with a content smile, resting." + ARMS + FACE),
    # 21 다니엘의 환상: 사자 굴(단 6:16–23)
    man("e_daniel", "Daniel the prophet as an old man of about eighty with a neat white beard, wearing a long deep-blue Babylonian court robe with gold trim and a soft cream turban, "
        "standing unhurt and joyful, raising both hands toward heaven in thanks." + ARMS + FACE + NOIDOL),
    man("e_den", "The dark open mouth of a small cave at the foot of a big grey rock mound, the opening is round and very dark inside, a few tufts of grass around it, seen from the front at a slight angle. No people, no animals.", "물건"),
    man("e_denstone", "A big round flat grey millstone-like stone standing upright on its edge, with a thick cord across it fastened by a lump of red clay seal pressed with a plain round mark. No people.", "물건"),
    # 22 예루살렘 함락: 토기장이의 집(렘 18:1–6). 처음엔 에벳멜렉과 구덩이(렘 38)였으나 22에는 예레미야가 늘 시위대 뜰에 서 있어(렘 32:2) 겹치므로 바꿨다.
    # 녹로와 그릇은 코드로 그린다(그릇이 터지고 다시 빚어지는 것을 보여야 해서). 사람은 두 손을 앞으로 내민 채 앉아 있게.
    man("e_potter", "A Judean potter, a cheerful middle-aged man with a short grey-black beard and a brown cloth headband, wearing a plain earth-brown knee-length tunic and a clay-stained apron, "
        "sitting on a low wooden stool and leaning forward with both clay-covered hands held out together in front of him at waist height as if shaping clay, side view facing right. "
        "Nothing in his hands, no wheel, no pots." + ARMS + FACE),
    # 23 곡과 마곡: 무기로 일곱 해 동안 불을 피움(겔 39:9–10) → 칼을 쳐서 보습을(사 2:4)
    man("e_plow", "An iron plowshare blade fixed to a simple wooden plow handle and a curved iron sickle with a wooden handle, lying together on a small patch of green grass with a few fresh green sprouts. No people.", "물건"),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림에그.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), '항목')
