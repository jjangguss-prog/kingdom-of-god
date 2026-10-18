# 21 다니엘의 환상(단 7) 그림 목록 v0.2 (2026-10-18) → 새그림21.json
# 끝없는 판(10-18 사용자: 반드시 지지만 예수님에 대한 소망을 갖게 되는 서사, 새 바닷가 싸움터).
# 배경(bg21)은 ref2/ref21.png(길 시안: 위는 밤의 큰 바다, 길 셋이 바다에서 올라와 아래 가운데 성도들의 진으로)를 참조로 그린다.
# 네 짐승(7:3–7)과 작은 뿔(7:8)은 무섭기보다 크고 강한 환상의 짐승으로, 피와 상처는 그리지 않는다.
# 옛적부터 항상 계신 이(7:9)와 인자 같은 이(7:13)는 사람 모습 없이 빛과 불과 구름으로만(구약 편 원칙).
import json
P = "Wide illustrated story panel for a children's Bible game, one single full-bleed scene with no border and no frame: "
END = " Every person has exactly two arms, two hands, two legs and two feet."
FACE = " Every face is clear and well drawn with distinct eyes, nose and mouth."
HANDS = " Hands are drawn simply and clearly, each hand with four fingers and a thumb, and no hand overlaps another person."
NOIDOL = " No statues, no idols, no carved figures, no winged discs, no crescent shapes, no moon ornaments, no religious symbols anywhere."
NOGORE = " Not gory: no blood, no wounds, nobody hurt."
NOGOD = " There is no human figure, no face and no body of God anywhere: only light, fire and clouds."
AURA = " A faint dark purple shadowy aura clings around it."

def scene(i, pr, seeds=(1, 2, 3), ref=None):
    it = {"id": i, "종류": "장면", "크기": [1536, 864], "시드": list(seeds), "프롬프트": P + pr}
    if ref: it["참조"] = [ref]
    return it

def beast(i, pr, seeds=(1, 2, 3), kind="정령"):
    return {"id": i, "종류": kind, "시드": list(seeds), "프롬프트": pr + AURA + NOGORE}

BG21 = ("Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield at night beside the great sea, seen from above at a slight angle. "
        "Keep exactly the same sandy road shapes and positions. The dark blue area across the top is a huge stormy sea: dark heaving waves with white foam crests, "
        "churned by four great swirling winds that whirl over the water (spiral streaks of wind and spray), a few faint flashes of lightning in low dark clouds over the water. "
        "Below the pale sandy beach line: dark green grassy coastal hills at night lit by cool moonlight, with scattered rocks, low bushes and a few windswept trees. "
        "Three sandy roads come up out of the sea onto the beach and wind down to the bottom center, where a small camp of a few plain cloth tents sits on a low hill with one small warm lamp glowing among them. "
        "At the lower left a flat grey rock near the bottom edge. Nothing covers the roads. No characters, no people, no animals, no text.")

items = [
    {"id": "bg21", "종류": "장면", "크기": [1536, 864], "시드": [1, 2, 3, 4], "참조": ["ref2/ref21.png"], "프롬프트": BG21 + NOIDOL},
    # 네 짐승(단 7:4–7)과 작은 뿔
    beast("beast_lion", "A great golden lion with two large eagle wings spread wide, flying, mane blowing in the wind, fierce proud face, whole body visible."),
    beast("beast_bear", "A huge brown bear raised up on one side so that one shoulder is higher than the other, holding three long white ribs crosswise in its teeth like sticks, walking heavily, whole body visible.", kind="인물"),
    beast("beast_leopard", "A spotted leopard flying fast with four bird wings on its back and four leopard heads on four necks, whole body visible."),
    beast("beast_fourth", "A terrible fourth beast unlike any animal: a huge dark iron-grey beast with a wide mouth full of big shining iron teeth, bronze claws, and a crown of exactly ten sharp horns standing in one row across the top of its head like a comb, stamping forward on heavy feet, whole body visible.", seeds=(4, 5, 6, 7), kind="인물"),   # v0.2: 처음 셋은 뿔이 둘~넷뿐
    # 이야기(앞)
    scene("s21a", "at night in a palace room in Babylon, the old prophet Daniel, a gentle white-bearded man of about seventy in a blue robe with a cream sash and a white turban, sits on the edge of his bed beside a small clay oil lamp and writes down his dream on a scroll with a reed pen held in his right hand, his left hand holding the scroll on his knee; through a window a dark stormy night sky." + NOIDOL + HANDS + FACE + END),
    scene("s21b", "a vision in the night: the great sea under a dark stormy sky, the four winds of heaven stirring the water into huge waves with four great swirling spirals of wind, and out of the sea rise four great beasts one after another: a golden lion with eagle wings, a brown bear raised up on one side, a spotted leopard with four wings and four heads, and behind them in the dark a terrible iron-grey fourth beast with iron teeth and ten horns. No people." + NOIDOL + NOGORE),
    scene("s21c", "close view in a stormy night vision: the head of the terrible iron-grey fourth beast with big iron teeth and a row of ten sharp horns on its head; among the horns one small horn is growing up, and on the small horn itself there are two human-like eyes and a little open mouth as if shouting proud words; three of the big horns are broken off and falling away; dark purple storm clouds behind. The small horn is only a horn with eyes and a mouth on it, not a creature, not an animal, no extra creature, no speech bubble, no text. No people." + NOIDOL + NOGORE, seeds=(4, 5, 6, 7)),   # v0.2: 작은 뿔이 작은 짐승처럼 나옴
    scene("s21d", "at night on a dark grassy hill by the shore of the stormy sea, a small group of faithful people, men, women and two children in simple robes, gather close around one small glowing clay oil lamp, holding hands and praying, looking out at the dark sea where huge shadowy shapes of beasts rise from the waves; the old white-bearded prophet Daniel in a blue robe and white turban stands among them and lifts his face to the sky; warm lamplight on their faces." + NOIDOL + HANDS + FACE + END),
    # 마침(지는 순간, 단 7:9–14, 22, 27)
    scene("v21a", "a heavenly vision at night: thrones are set up, and in the middle a great throne made of blazing flames with burning wheels of fire, a river of fire flowing out from before it, and around it countless thousands upon thousands of tiny points of white light like a great host; at the center of the flames only a blinding pure white light like snow; far below at the bottom edge the dark beasts shrink back into the shadows." + NOGOD + NOIDOL + NOGORE),
    scene("v21b", "in the night sky over the great sea, the clouds of heaven part and a brilliant golden-white light comes riding on the glowing clouds like a rising sun; the light is pure and empty with nobody inside it; rays of light stream down over the whole world, and the stormy sea below grows calm and shining." + NOGOD + " No silhouette, no figure, no angel, no person inside the light." + NOIDOL, seeds=(4, 5, 6, 7)),   # v0.2: 빛 속에 사람 꼴이 보임
    scene("v21c", "at dawn on the grassy hill by the now calm shining sea, the small group of faithful people, two men, two women and two children in simple robes, stand together in warm golden morning light, smiling and laughing with happy tears of joy, looking up at the bright sky; a smiling child holds a small clay oil lamp with a little flame in both hands; the beasts are gone; the whole sky glows gold." + NOIDOL + HANDS + FACE + END, seeds=(4, 5, 6)),   # v0.2: 처음 셋은 얼굴이 슬퍼 보임
]
json.dump({"출력": "raw", "크기": [1024, 1024], "단계": 4, "항목": items}, open('새그림21.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(items), 'items')
