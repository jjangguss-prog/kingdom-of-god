# 생성한 아이콘 그림(raw)을 안드로이드 mipmap 크기별로 만든다. 사용: python 앱아이콘.py raw/icon_s1_xxxx.png
import sys, os
from PIL import Image, ImageDraw

src = Image.open(sys.argv[1]).convert('RGBA')
w, h = src.size; c = min(w, h) * .86
src = src.crop(((w - c) / 2, (h - c) / 2, (w + c) / 2, (h + c) / 2))
RES = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'app', 'app', 'src', 'main', 'res')

def mask(sz, round_):
    m = Image.new('L', (sz * 4, sz * 4), 0); d = ImageDraw.Draw(m)
    if round_: d.ellipse([0, 0, sz * 4 - 1, sz * 4 - 1], fill=255)
    else: d.rounded_rectangle([0, 0, sz * 4 - 1, sz * 4 - 1], radius=sz * 4 * .2, fill=255)
    return m.resize((sz, sz), Image.LANCZOS)

for name, sz in [('mdpi', 48), ('hdpi', 72), ('xhdpi', 96), ('xxhdpi', 144), ('xxxhdpi', 192)]:
    d = os.path.join(RES, f'mipmap-{name}'); os.makedirs(d, exist_ok=True)
    im = src.resize((sz, sz), Image.LANCZOS)
    for fn, r in (('ic_launcher.png', False), ('ic_launcher_round.png', True)):
        o = Image.new('RGBA', (sz, sz), (0, 0, 0, 0)); o.paste(im, (0, 0), mask(sz, r)); o.save(os.path.join(d, fn))
src.resize((512, 512), Image.LANCZOS).save(os.path.join(RES, '..', '..', '..', '..', 'icon-512.png'))
print('ok')
