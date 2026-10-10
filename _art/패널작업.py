# 배경·이야기·승리 그림 작업 파일(배경2.json, 이야기2.json) 만들기 v0.1 (2026-10-11)
import json, hashlib
def tag(it): return hashlib.sha1((it['프롬프트'] + it.get('종류', '인물') + '|'.join(it.get('참조', []))).encode('utf-8')).hexdigest()[:6]
c3 = {i['id']: i for i in json.load(open('인물3.json', encoding='utf-8'))['항목']}
ABRAM = f"raw/abram_s1_{tag(c3['abram'])}.png"
MOSY = f"raw/moses_young_s1_{tag(c3['moses_young'])}.png"
NOAH = "raw/noah_s1_65e1aa.png"
MOSES = "raw/moses_s2_8da0a7.png"
P = "Wide illustrated story panel for a children's Bible game: "

bg = {
 'bg2': ("ref/ref2.png", "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield in the green hill country of ancient Canaan, seen from above at a slight angle. Keep exactly the same winding dirt road shapes and positions and the bare earth clearing on the right side. Rolling green and golden hills, olive trees and terebinth oaks, scattered rocks, wildflowers and low stone field walls; in the right clearing a small camp of a few goat-hair tents with resting camels and sheep. Warm morning light. No characters, no text."),
 'bg3': ("ref/ref3.png", "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield in rocky hill country at dusk, seen from above at a slight angle. Keep exactly the same winding road shapes and positions and the clearing on the left side. Dark green shrubs, boulders, a dry stream bed and twisted oak trees; in the left clearing a small camp of tents with a glowing campfire. Warm dusk light fading to blue. No characters, no text."),
 'bg4': ("ref/ref4.png", "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield on the bank of the Nile river in ancient Egypt, seen from above at a slight angle. Keep exactly the same two sandy road shapes meeting at the river bank, the blue river along the bottom and the thick green papyrus reeds at the water's edge; on the upper part of the map palm groves, irrigated green fields and a few mud-brick houses; a tiny woven basket hidden among the reeds at the bottom center. Warm daylight. No characters, no text."),
 'bg5': ("ref/ref5.png", "Repaint this top-down tower defense game map as a richly hand-painted Kingdom Rush style battlefield at a desert oasis in the land of Midian, seen from above at a slight angle. Keep exactly the same sandy road shapes meeting on the right, where a round stone well with a wooden pulley stands in a small green oasis with palm trees and stone water troughs. Red rock outcrops, desert shrubs and scattered stones. Warm late afternoon light. No characters, no text."),
}
story = {
 's0a': (None, "the beautiful newly created world at sunrise: light breaking over the waters, green hills, rivers and flowers, birds in the sky, fish in the sea and animals of every kind, rays of warm golden light from above, wonder and goodness. No people."),
 's0b': (None, "a man and a woman in simple garments of animal skin walk sadly out of a lush garden into a wild land, looking back; behind them at the garden gate a bright turning sword of fire; a serpent slithers away into the grass; soft golden light from the sky still shines gently on the couple. Tender, sad but hopeful."),
 's2a': (None, "crowds of ancient people building a gigantic brick tower toward the sky in a plain city, carrying bricks and tar on ladders, proud faces, dark storm clouds gathering around the top of the tower."),
 's2b': (ABRAM, "this same man Abram stands outside his house in the town of Haran at dawn, looking up in awe at warm golden light breaking through the clouds, his wife Sarai watching from the doorway."),
 's2c': (ABRAM, "this same Abram leads a long caravan of his family, servants, camels, donkeys and flocks of sheep and goats across rolling hills toward the land of Canaan, a younger man, his nephew Lot, walking beside him, bright day."),
 's2d': (None, "on a hilltop road at dusk, a band of desert raiders sneaks toward a caravan camp of tents and sheep in the valley; small shadowy purple imps hover above the raiders holding thin glowing threads tied to their shoulders like puppet strings. Child-friendly suspense."),
 's3a': (ABRAM, "this same Abram and his younger nephew Lot stand on a hilltop with their flocks behind them; Lot points eagerly down at the lush green Jordan plain with a walled city far away, while Abram calmly opens his hand to let him choose."),
 's3b': (None, "in the evening an army of the four kings of the East marches away from a walled city with smoke rising, leading a line of worried captives, a man with his wife and daughters among them, carrying loot on donkeys; faint purple shadow wisps hover above the soldiers. Not violent."),
 's3c': (ABRAM, "this same Abram gathers his trained household servants at his camp under great oak trees at night, torches burning, the men holding staffs, slings and bows, brave determined faces."),
 's3d': (None, "under a bright moon, groups of brave men with torches quietly approach a sleeping enemy camp in a valley from several sides, tents and campfires below, adventurous mood, no fighting shown."),
 's4a': (ABRAM, "this same man, now very old Abraham, and his young son Isaac stand by a stone altar on a mountaintop at dawn, looking with joy and relief at a ram caught by its horns in a thicket nearby, warm golden light."),
 's4b': (None, "in a grand Egyptian hall full of grain sacks, a young ruler in fine Egyptian robes, Joseph, tearfully embraces his eleven Hebrew brothers who kneel in astonishment, warm light."),
 's4c': (None, "Hebrew slaves making mud bricks under a hot sun in ancient Egypt, carrying heavy loads past half-built monuments, taskmasters with sticks standing over them, faint shadowy purple wisps hovering above the taskmasters."),
 's4d': (None, "at dawn a Hebrew mother gently lays her baby boy in a small woven papyrus basket coated with pitch among the tall reeds at the edge of the Nile, while a young girl, his sister, watches from behind the reeds. Tender and quiet."),
 's5a': (None, "a young boy prince Moses grows up in the Egyptian palace, wearing fine linen, studying papyrus scrolls with scribes among painted columns, the kind Egyptian princess watching him with love."),
 's5b': (MOSY, "this same man Moses, wearing Egyptian clothes, flees alone across the desert at sunset, looking back with fear and regret, the cities of Egypt far behind him."),
 's5c': (MOSY, "at a round stone well in a desert oasis of Midian, seven young shepherd sisters draw water into stone troughs for their father's flock of sheep, while this same tired traveler Moses sits resting by the well."),
 's5d': (MOSY, "rough herdsmen push seven shepherd sisters away from a desert well and scatter their sheep, small shadowy purple imps hovering above the herdsmen holding glowing puppet threads; this same Moses stands up with his staff to protect the sisters."),
}
victory = {
 'v1a': (NOAH, "animals of every kind, two by two, elephants, lions, giraffes, sheep and birds, walk up a wooden ramp into the huge finished ark, this same Noah and his family welcoming them, cloudy sky."),
 'v1b': (None, "the great side door of Noah's huge wooden ark closing by itself as warm heavenly golden light shines on it from parting clouds above, the first rain beginning to fall, no people visible."),
 'v1c': (None, "Noah's huge wooden ark floating safely on a vast stormy flood under heavy rain clouds, big waves and distant lightning, warm light glowing from its small windows, only the ark on the water."),
 'v1d': (NOAH, "Noah's ark resting on green mountains after the flood, a brilliant rainbow across the clearing sky, this same Noah and his family giving thanks at a stone altar, a white dove flying with an olive leaf, animals coming out."),
 'v2a': (ABRAM, "this same Abram's caravan arrives at a great oak tree in a lush green valley near Shechem, families resting in the shade with their flocks, golden afternoon light."),
 'v2b': (ABRAM, "this same Abram kneels and builds an altar of stones under the great oak tree, a beam of warm golden light shines down from the sky onto him and onto the green land all around."),
 'v2c': (None, "a vast night sky full of countless bright stars over the hills of Canaan, a small figure of an old man with a staff standing on a hilltop looking up at the stars, tents glowing below."),
 'v3a': (ABRAM, "at dawn this same Abram and his men lead freed captives home, a younger man Lot with his family, women and children, with their flocks and goods, joyful reunion."),
 'v3b': (ABRAM, "a dignified old king and priest, Melchizedek, in white and purple robes with a simple gold circlet, brings bread and wine to this same Abram in a green valley and lifts his hand to bless him, soft golden light."),
 'v3c': (ABRAM, "this same Abram stands guard on a hill beside a covenant offering laid on stones under the open sky, waving his staff to chase away dark birds of prey swooping down from the sky."),
 'v4a': (None, "a kind Egyptian princess with her maidens at the edge of the Nile among papyrus reeds opens a small woven basket and finds a crying Hebrew baby boy inside, her face full of compassion, morning light."),
 'v4b': (None, "a brave young Hebrew girl speaks to the Egyptian princess by the river, offering to fetch a nurse, the baby now in the princess's arms, the baby's mother hurrying near behind the reeds."),
 'v4c': (None, "a Hebrew mother joyfully hugs and nurses her baby son at home in warm lamplight, her young daughter smiling beside her, a small royal Egyptian purse of payment on the table."),
 'v5a': (MOSY, "this same Moses has watered the flock of seven grateful shepherd sisters at a desert oasis well, the sisters smiling, sheep drinking from stone troughs, warm evening light."),
 'v5b': (MOSY, "on the slope of a desert mountain this same Moses, a shepherd with his flock nearby, kneels barefoot with his sandals set aside before a bush burning with bright golden flames that do not burn it up, awe and wonder."),
 'v5c': (None, "a bush burning with golden flames glows on a mountain at dusk, beams of golden light rising into the sky, and far below in the distance the land of Egypt where tiny slaves labor among pyramids."),
 'v6a': (MOSES, "this same old Moses stands on the shore at night stretching his staff out over the sea while a mighty wind blows and the sea begins to split apart, a glowing pillar of fire behind the camp of tents."),
 'v6b': (None, "the people of Israel, families with children, sheep and carts, walk on dry ground through the middle of the sea between two towering walls of blue water, lit by a glowing pillar of fire behind them at night."),
 'v6c': (None, "dawn breaks over the sea as the towering walls of water crash back together and the sea returns to its place with big rolling waves, the people of Israel standing safe on the far shore watching, the sea empty."),
 'v6d': (None, "on the shore in bright morning light, Miriam, a joyful elderly woman, dances with a tambourine leading the women of Israel in a song of praise, families raising their hands, the calm sea behind."),
}
def job(d, kind, prefix):
    items = []
    for k, (ref, pr) in d.items():
        it = {"id": k, "종류": kind, "시드": [1], "프롬프트": prefix + pr}
        if ref: it["참조"] = [ref]
        items.append(it)
    return items
json.dump({"출력": "raw", "크기": [1536, 864], "단계": 4, "항목": job(bg, '장면', '') + [{"id": "levi_priest", "종류": "건물", "시드": [1, 2], "크기": [1024, 1024], "참조": ["raw/levi3_s1_008019.png"],
  "프롬프트": "Draw the special priest version of this exact sacred tent in the same style, colors and camera angle: a bronze altar of burnt offering with a thin column of smoke in front, a golden incense altar glowing inside, and a high priest in a blue robe with golden bells and pomegranates on the hem, a golden ephod with a breastplate of twelve colored stones and a white turban with a golden plate, raising his hands in blessing."}]},
          open('배경2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for it in json.load(open('배경2.json', encoding='utf-8'))['항목']:
    if it['id'].startswith('bg'): it['시드'] = [1, 2]
j = json.load(open('배경2.json', encoding='utf-8'))
for it in j['항목']:
    if it['id'].startswith('bg'): it['시드'] = [1, 2]
json.dump(j, open('배경2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump({"출력": "raw", "크기": [1536, 864], "단계": 4, "항목": job(story, '장면', P) + job(victory, '장면', P)}, open('이야기2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(ABRAM, MOSY)
