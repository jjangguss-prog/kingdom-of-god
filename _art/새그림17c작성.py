# 17 브라가 골짜기 마침의 노략물 그림 v0.1 (2026-10-19) → 새그림17c.json
# 10-19 사용자: "17스테이지 끝나고 전리품? 으로 남는 방패 창 등도 디자인이 초안수준인것 같아." 코드로 그리던 창·방패·옷·항아리를 그림으로.
# 대하 20:25 "재물과 의복과 보물이 많으므로 각기 탈취하는데 그 물건이 너무 많아 능히 가져갈 수 없을 만큼 많으므로 사흘 동안에 거두어들이고". 자루는 16의 e_sack을 같이 쓴다.
# 땅에 놓인 작은 물건이라 위에서 조금 비스듬히 내려다본 모습. 우상·종교 상징은 넣지 않는다.
import json
GROUND = " lying flat on the ground, seen from slightly above, no people, no text, no symbols."

def it(i, pr, seeds=(1, 2, 3)):
    return {"id": i, "종류": "물건", "시드": list(seeds), "프롬프트": pr + GROUND}

items = [
    it("spoil_spear", "One long ancient spear with a straight wooden shaft and a leaf-shaped bronze spearhead, shown horizontally from the side,"),
    it("spoil_shield", "One round ancient warrior's shield made of brown leather stretched over wood with a bronze rim and a round bronze boss in the middle,"),
    it("spoil_shield2", "One round ancient warrior's shield painted deep blue with a simple plain yellow rim and a round bronze boss in the middle,"),
    it("spoil_cloth", "One neatly folded fine garment of rich red wool with gold embroidered edges, a small stack of fine clothing,"),
    it("spoil_cloth2", "One neatly folded fine garment of deep blue linen with a striped white and yellow border, a small stack of fine clothing,"),
    it("spoil_treasure", "A small pile of precious things: a gold jug, two silver cups, a few gold coins and a string of colored jewels,"),
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림17c.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), 'items')
