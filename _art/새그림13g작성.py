# 13 미스바 그림 더하기 v0.1 (2026-10-18) → 새그림13g.json
# 10-18 사용자: "병사들과 룻의 디자인이 초기 상태대로야. 그림체에 맞게 바꿔줘." 코드로 그리던 물을 붓는 백성(삼상 7:6)과 이삭 줍는 룻(룻 2:16, 숨은 이야기)을 그림으로.
# 물 붓는 백성은 물동이를 든 모습(기다릴 때)과 붓는 모습 둘씩(남자·여자). 룻은 걷는 모습과 이삭을 줍는 모습.
# 고르는 기준(10-16 사용자): 이목구비가 뚜렷하고 팔·손이 정상인가.
import json
HANDS = " Exactly two arms and exactly two hands, each hand with four fingers and a thumb."
MAN = "An Israelite villager man of about thirty with a short brown beard, a cream headcloth and a plain brown wool tunic with a rope belt and leather sandals"
WOMAN = "An Israelite village woman of about thirty in a long olive-green dress, a cream headscarf and leather sandals"
RUTH = ("Ruth, a young Moabite woman of about twenty-five with long dark hair under a simple light-brown headscarf, "
        "wearing a plain long blue dress with a cream sash and leather sandals, gentle hopeful face")

def man(i, pr, seeds=(1, 2, 3)):
    return {"id": i, "종류": "인물", "시드": list(seeds), "프롬프트": pr + HANDS}

items = [
    man("p_jar", MAN + ", standing and holding a round brown clay water jar with both hands in front of his chest, calm earnest face, three-quarter view facing right, whole body visible."),
    man("p_jar2", WOMAN + ", standing and holding a round brown clay water jar with both hands in front of her waist, gentle face, three-quarter view facing right, whole body visible."),
    man("p_pour", MAN + ", leaning slightly forward and tipping a round brown clay water jar with both hands so a stream of clear water pours out onto the ground in front of him, humble prayerful face, three-quarter view facing right, whole body visible."),
    man("p_pour2", WOMAN + ", leaning slightly forward and tipping a round brown clay water jar with both hands so a stream of clear water pours out onto the ground in front of her, humble prayerful face, three-quarter view facing right, whole body visible."),
    man("ruth", RUTH + ", walking and carrying a small bundle of golden barley stalks in her arms against her chest, three-quarter view facing right, whole body visible."),
    man("ruth_glean", RUTH + ", kneeling on one knee on the ground and picking up a fallen golden barley stalk with her right hand while holding a small bundle of barley in her left arm, three-quarter view facing right, whole body visible."),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림13g.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), 'items')
