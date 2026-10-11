# 방주로 들어가는 짐승들을 정확히 둘씩 짝지어 배경 위에 세운다(생성 모델이 마릿수를 자주 틀려서 손으로 배치).
# 사용: python 방주합성.py 배경.png 경사로발x 경사로발y 출력.png   (v1a: raw/arkscene_s2_bbc049.png 800 618 raw/v1a_comp3.png)
# 짐승 그림은 cut\ 의 누끼(a_*). 행렬은 왼쪽에서 경사로 쪽(오른쪽)으로 짝지어 걸어간다. 짝은 나란히(뒤쪽 하나는 조금 위·작게).
import sys, glob, os
from PIL import Image, ImageFilter, ImageDraw

bg = Image.open(sys.argv[1]).convert('RGBA').resize((1280, 720), Image.LANCZOS)
RX, RY = int(sys.argv[2]), int(sys.argv[3])
CUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cut')

def sprite(name, i=0):
    fs = sorted(glob.glob(os.path.join(CUT, f'{name}_s*.png')))
    return Image.open(fs[min(i, len(fs) - 1)]).convert('RGBA')

def put(im, cx, by, h, flip=False):
    k = h / im.height; w = round(im.width * k)
    s = im.resize((w, round(h)), Image.LANCZOS)
    if flip: s = s.transpose(Image.FLIP_LEFT_RIGHT)
    sh = Image.new('RGBA', bg.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)
    d.ellipse([cx - w * .42, by - h * .05, cx + w * .42, by + h * .05], fill=(30, 20, 10, 110))
    bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)))
    bg.alpha_composite(s, (round(cx - w / 2), round(by - h)))

# 경사로에 가까운 쪽부터: 양 → 얼룩말 → 사자 → 기린 → 코끼리 (작은 짐승이 앞에서 먼저 오른다)
PAIRS = [(('a_sheep', 0), ('a_sheep', 1), 86), (('a_zebra', 0), ('a_zebra', 1), 132), (('a_lion', 0), ('a_lioness2', 0), 118),
         (('a_giraffe', 0), ('a_giraffe', 1), 232), (('a_elephant', 0), ('a_elephant', 1), 172)]
x, y = RX - 30, RY
order = []
for (a, b, h) in PAIRS:
    A, B = sprite(*a), sprite(*b)
    wA = A.width * h / A.height
    order.append((B, x - wA * .34, y - 30, h * .9))   # 뒤쪽 짝(조금 왼쪽 위·작게) — 둘 다 잘 보이게
    order.append((A, x, y, h))
    x -= wA * 1.06 + 8; y += 5
for im, cx, by, h in sorted(order, key=lambda t: t[2]):
    put(im, cx, by, h)
# 비둘기 한 쌍
D0, D1 = sprite('a_dove', 0), sprite('a_dove', 1)
put(D0, RX - 160, 170, 70); put(D1, RX - 70, 140, 62)
bg.convert('RGB').save(sys.argv[4])
print('ok', sys.argv[4])
