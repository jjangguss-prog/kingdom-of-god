# 16 시글락 마침 그림 더하기 v0.2 (2026-10-19, 자루 e_sack 더함) → 새그림16d.json
# 10-19 사용자: "시글락 스테이지에서도 끝나고 옛날버전 이미지들이 떠. (사람들, 재물 등) 고쳐줘"
# 코드로 그리던 브솔 시내의 이백 명(삼상 30:10, 21)과 되찾은 물건 더미(30:19–20, 24)를 그림으로.
# 이백 명은 지쳐 앉은 모습과 일어나 두 팔을 들어 맞는 모습(걸을 때는 행렬의 p_soldier). 행렬의 p_soldier와 같은 차림으로 맞춘다.
import json
HANDS = " Exactly two arms and exactly two hands, each hand with four fingers and a thumb."
MAN = ("one of David's Israelite warriors, a young man with a short dark beard, a rounded bronze helmet, "
       "a tan wool tunic with a leather armor vest and leather sandals")

def it(i, kind, pr, seeds=(1, 2, 3)):
    return {"id": i, "종류": kind, "시드": list(seeds), "프롬프트": pr}

items = [
    it("p_rest", "인물", "An exhausted man, " + MAN + ", sitting on the ground with his knees up resting after a long march, his spear lying on the ground beside him, "
       "one hand on his knee and the other hand wiping his brow, tired but kind face, three-quarter view facing left, whole body visible." + HANDS),
    it("p_cheer", "인물", "A joyful man, " + MAN + ", standing and raising both arms high in welcome with open hands, his spear left aside, "
       "big happy smile, three-quarter view facing left, whole body visible." + HANDS),
    it("e_spoils", "물건", "A big heap of recovered household goods and spoils piled on the sand: cloth sacks of grain tied with cord, round clay jars and water pots, "
       "a small open wooden chest with gold and silver cups and coins, rolled colorful woven rugs, folded cloaks, a bundle of white sheep wool and a leather bag. "
       "No people, no animals, no statues, no idols, no religious symbols."),
    it("e_sack", "물건", "One small plump cloth sack of plundered goods made of rough tan burlap, tied at the top with a brown cord, bulging with round shapes, "
       "a gold coin and the rim of a silver cup peeking out of the opening. No people, no text."),   # 빼앗아 달아나는 자루(30:2) · 17의 노략물
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림16d.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), 'items')
