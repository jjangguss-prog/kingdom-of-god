# 매끄러운 돌 다섯(e_stones, 삼상 17:40) 합성 v0.1 (2026-10-15)
# FLUX가 돌 수를 맞추지 못해서(여섯·셋), 새그림14d.json 시드 4(돌 셋이 한 줄)의 돌을 잘라 모래 위에 다섯을 한 줄로 놓는다.
# 사용: python 돌다섯합성.py → raw\e_stones_s9_five00.png (고르기_14.json의 e_stones). 그 뒤 모으기.py로 누끼.
from PIL import Image, ImageDraw, ImageFilter, ImageOps
import glob, random, math, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
S = Image.open(glob.glob('raw/e_stones_s4_e107ce.png')[0]).convert('RGBA')


def stone(cx, cy, r=121):   # 돌 하나를 둥글게 잘라 냄(바깥 흰 바탕이 묻지 않게 테두리 안쪽까지만)
    st = S.crop((cx - r, cy - r, cx + r, cy + r))
    m = Image.new('L', st.size, 0); ImageDraw.Draw(m).ellipse((0, 0, 2 * r - 1, 2 * r - 1), fill=255)
    st.putalpha(m.filter(ImageFilter.GaussianBlur(.8))); return st


def blob(cx, cy, rx, ry, n=90, j=.07):   # 울퉁불퉁한 모래 자리
    ph = [random.uniform(0, 6.28) for _ in range(4)]
    return [(cx + rx * math.cos(t) * (1 + j * math.sin(3 * t + ph[0]) + j * .6 * math.sin(5 * t + ph[1])),
             cy + ry * math.sin(t) * (1 + j * math.sin(2 * t + ph[2]) + j * .6 * math.sin(7 * t + ph[3]))) for t in [i / n * 6.2832 for i in range(n)]]


gray, c1, c2 = stone(248, 500), stone(513, 487), stone(776, 467)
W = 1024; im = Image.new('RGBA', (W, W), (255, 255, 255, 255))
random.seed(11)
cx, cy = 512, 566
d = ImageDraw.Draw(im)
pts = blob(cx, cy, 470, 150)
d.polygon([(x, y + 16) for x, y in pts], fill=(176, 120, 64))
d.polygon(pts, fill=(214, 164, 100), outline=(120, 74, 36), width=8)
d.polygon(blob(cx, cy - 12, 440, 118, j=.05), fill=(232, 188, 124))
for _ in range(50):
    x = random.randint(cx - 420, cx + 420); y = random.randint(cy - 90, cy + 110)
    if ((x - cx) / 430) ** 2 + ((y - cy) / 125) ** 2 < 1: d.ellipse((x - 4, y - 3, x + 4, y + 3), fill=(198, 148, 88))
k = 0.70; stones = [gray, c1, ImageOps.mirror(gray), c2, ImageOps.mirror(c1)]
xs = [158, 336, 512, 688, 866]; ys = [560, 534, 552, 530, 556]
sh = Image.new('RGBA', (W, W), (0, 0, 0, 0)); ds = ImageDraw.Draw(sh)
for x, y in zip(xs, ys): ds.ellipse((x - 66, y + 50, x + 90, y + 90), fill=(110, 70, 30, 120))
im = Image.alpha_composite(im, sh.filter(ImageFilter.GaussianBlur(6)))
for st, x, y in zip(stones, xs, ys):
    s2 = st.resize((round(st.width * k), round(st.height * k)), Image.LANCZOS)
    im.alpha_composite(s2, (x - s2.width // 2, y - s2.height // 2))
im.convert('RGB').save('raw/e_stones_s9_five00.png'); print('raw/e_stones_s9_five00.png')
