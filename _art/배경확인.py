# 새로 그린 배경 위에 실제 길(빨강)과 탑 자리(흰 타원)를 겹쳐 본다. 사용: python 배경확인.py 지도2.json ref2/spots.json 접두(bg?w) 출력폴더
import sys, json, glob
sys.path.insert(0, '.')
from 탑자리 import catmull
from PIL import Image, ImageDraw
M = json.load(open(sys.argv[1], encoding='utf-8')); SP = json.load(open(sys.argv[2], encoding='utf-8')); pat, out = sys.argv[3], sys.argv[4]
for part, ids in (('a', '123'), ('b', '456')):
    tiles = []
    for sid in ids:
        for f in sorted(glob.glob(f'raw/{pat.replace("?", sid)}_s*.png'))[:2]:
            im = Image.open(f).convert('RGB').resize((1280, 720)); d = ImageDraw.Draw(im)
            for c in M[sid]['paths']:
                d.line([tuple(map(round, q)) for q in catmull(c)], fill=(255, 0, 0), width=4)
            for x, y in SP[sid]:
                d.ellipse([x - 31, y - 10, x + 31, y + 20], outline=(255, 255, 255), width=3)
            d.text((8, 8), f.split('/')[-1].split('\\')[-1][:14], fill=(255, 255, 0))
            tiles.append(im.resize((640, 360)))
    o = Image.new('RGB', (1280, 360 * ((len(tiles) + 1) // 2)))
    for i, t in enumerate(tiles):
        o.paste(t, ((i % 2) * 640, (i // 2) * 360))
    o.save(f'{out}/bgw_{part}.jpg', quality=85)
print('ok')
