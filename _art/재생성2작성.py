# 재생성2.json 만들기: 방주 승리 그림을 상자 모양 방주로 다시, 복제된 아브람·액자 그림 다시. 사용: python 재생성2작성.py raw/arkbox_sN_xxxx.png
import json, sys
ARK = sys.argv[1]
NOAH = "raw/noah_s1_65e1aa.png"
P = "Wide illustrated story panel for a children's Bible game: "
I = [
 {"id": "v1a", "참조": [ARK], "프롬프트": P + "animals of every kind, two by two, elephants, lions, giraffes, sheep and birds, walk up a wooden ramp into this same huge long box-shaped wooden ark, a kind old man with a long white beard, cream headcloth and brown robe (Noah) and his family welcoming them, cloudy sky."},
 {"id": "v1b", "참조": [ARK], "프롬프트": P + "the great side door of this same huge long box-shaped wooden ark closing by itself as warm heavenly golden light shines on it from parting clouds above, the first rain beginning to fall, no people visible."},
 {"id": "v1c", "참조": [ARK], "프롬프트": P + "this same huge long box-shaped wooden ark, with no mast and no sails, floating safely on a vast stormy flood under heavy rain clouds, big waves and distant lightning, warm light glowing from its small windows, only the ark on the water."},
 {"id": "v1d", "참조": [ARK], "프롬프트": P + "this same long box-shaped wooden ark resting on green mountains after the flood, a brilliant rainbow across the clearing sky, a kind old man with a long white beard, cream headcloth and brown robe (Noah) and his family giving thanks at a stone altar, a white dove flying with an olive leaf, animals coming out."},
 {"id": "v3a", "프롬프트": P + "at dawn an old man with a long grey-streaked beard in a blue and cream striped robe (Abram) leads a band of men bringing freed captives home: a younger man with a short black beard in a red-brown cloak (Lot) with his wife and daughters, women and children, flocks and goods, a joyful reunion."},
 {"id": "s3c", "프롬프트": P + "an old man with a long grey-streaked beard in a blue and cream striped robe (Abram) gathers his trained household servants, young men of many ages, at his camp under great oak trees at night, torches burning, the men holding staffs, slings and bows, brave determined faces."},
 {"id": "s4c", "프롬프트": P + "Hebrew slaves making mud bricks under a hot sun in ancient Egypt, carrying heavy loads past half-built monuments, taskmasters with sticks standing over them, faint shadowy purple wisps hovering above the taskmasters. The picture fills the whole frame edge to edge, no picture frame, no border."},
 {"id": "v4b", "프롬프트": P + "a brave young Hebrew girl speaks to a kind Egyptian princess by the river among papyrus reeds, offering to fetch a nurse, the princess cradling the baby with both arms, every person with exactly two arms and two hands, the baby's mother hurrying near behind the reeds. The picture fills the whole frame edge to edge, no picture frame, no border, no speech bubbles, no text."},
 {"id": "v5c", "프롬프트": P + "a bush burning with golden flames glows on a desert mountain at dusk, beams of golden light rising into the sky, and far below in the distance the land of Egypt where tiny slaves labor among pyramids. The picture fills the whole frame edge to edge, no picture frame, no border."},
 {"id": "v6b", "프롬프트": P + "the people of Israel, families with children, sheep and carts, walk on dry sandy ground through the middle of the sea between two towering walls of deep blue-green sea water with foaming crests, fish visible inside the water walls, lit at night by a glowing pillar of fire behind them. The picture fills the whole frame edge to edge, no border."},
 {"id": "v6c", "프롬프트": P + "dawn breaks over the sea as the towering walls of water crash back together and the sea returns to its place with big rolling waves, the people of Israel standing safe on the far shore watching in awe, the sea empty. The picture fills the whole frame edge to edge, no picture frame, no border."}
]
for it in I:
    it["종류"] = "장면"; it["시드"] = [2]
json.dump({"출력": "raw", "크기": [1536, 864], "단계": 4, "항목": I}, open('재생성2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', ARK)
