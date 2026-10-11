# 처음엔 막혀 있다가 중간에 뚫리는 뒷길(스테이지의 rear 길)을 덮는 그림을 만든다 v0.1 (2026-10-12). 썸네일 venv에서 돈다.
# 사용: python 뒷길덮개.py 열린배경.png 막힌배경.png 출력.png [미리보기.jpg]
#   7 르비딤: python 뒷길덮개.py raw/bg7w_s2_4a5b31.png raw/bg7closed_s8_3809ea.png ../art/bg7_rear.png (막힌배경은 재생성11.json)
#   열린배경: 뒷길이 그려진 배경(raw), 막힌배경: 같은 배경을 참조로 뒷길만 지워 다시 그린 것(raw)
#   길 좌표는 게임의 다듬어진 길(G.paths)과 같게 아래 REAR·MAIN에 적는다(1280×720). 뒷길이 큰길에 닿기 전까지만 덮는다.
# 결과: 1536×864 RGBA. 뒷길 둘레만 막힌배경이고 나머지는 투명. 게임은 bgN.jpg 위에 bgN_rear.png를 얹었다가 길을 뚫을 때 걷어 낸다.
import sys, math
from PIL import Image, ImageDraw, ImageFilter

# 7 르비딤: 진영 뒤쪽 짧은 길(G.paths[2])과 큰길(G.paths[0]) — 큰길과 합쳐지는 (1000, 540) 앞까지
REAR = [[780, 790], [780.4, 762.6], [781.9, 724.1], [787, 697.3], [794.1, 683], [804.8, 670.3], [817.8, 659.2], [832, 649], [846.5, 639.5],
        [860, 630], [874, 620], [888, 610.9], [902, 602.3], [916, 593.8], [930, 585], [943.7, 574.6], [957, 562.9], [970.6, 551.9], [984.7, 543.6], [1000, 540]]
MAIN = [[720, 560], [737, 528.5], [745.2, 491.5], [760, 460], [786.3, 438], [818.8, 420.4], [852.1, 410.8], [886.4, 412.5], [922.6, 425.2],
        [953.8, 444.6], [973.9, 472.3], [984.3, 508.9], [1000, 540], [1029.5, 560.8], [1064.8, 574.8], [1098.8, 580.3], [1135.6, 572.5], [1170, 560]]
RAD, WIDE, FEATHER, KEEP = 44, 88, 6, 64   # 길 반폭(늘 덮음), 바뀐 곳을 찾는 반폭, 가장자리 흐림, 큰길에서 이만큼은 덮지 않는다

def seg_d(p, a, b):
    vx, vy = b[0] - a[0], b[1] - a[1]; l2 = vx * vx + vy * vy or 1
    t = max(0, min(1, ((p[0] - a[0]) * vx + (p[1] - a[1]) * vy) / l2))
    return math.hypot(p[0] - a[0] - vx * t, p[1] - a[1] - vy * t)

def main_d(p):
    return min(seg_d(p, MAIN[i], MAIN[i + 1]) for i in range(len(MAIN) - 1))

def main():
    op, cl = Image.open(sys.argv[1]).convert('RGB'), Image.open(sys.argv[2]).convert('RGB')
    W, H = 1536, 864; k = W / 1280
    op, cl = op.resize((W, H), Image.LANCZOS), cl.resize((W, H), Image.LANCZOS)
    m = Image.new('L', (W, H), 0); d = ImageDraw.Draw(m)
    pts = []
    for i in range(len(REAR) - 1):   # 촘촘히 나눠 큰길에 너무 가까운 곳은 뺀다
        a, b = REAR[i], REAR[i + 1]; n = max(1, int(math.hypot(b[0] - a[0], b[1] - a[1]) / 4))
        for j in range(n):
            p = (a[0] + (b[0] - a[0]) * j / n, a[1] + (b[1] - a[1]) * j / n)
            if main_d(p) < KEEP: break
            pts.append(p)
        else: continue
        break
    wide = Image.new('L', (W, H), 0); dw = ImageDraw.Draw(wide)
    for x, y in pts:
        r = RAD * k; d.ellipse([x * k - r, y * k - r, x * k + r, y * k + r], fill=255)
        r = WIDE * k; dw.ellipse([x * k - r, y * k - r, x * k + r, y * k + r], fill=255)
    # 길 둘레(WIDE) 안에서 두 그림이 실제로 다른 곳(쌓인 바위 전체)도 덮는다. 같은 모래에서 흐려지게 해서 바위가 반쯤 잘리지 않는다
    from PIL import ImageChops
    diff = ImageChops.difference(op, cl).convert('L').filter(ImageFilter.GaussianBlur(3)).point(lambda v: 255 if v > 38 else int(v * 255 / 38))
    diff = ImageChops.multiply(diff, wide.filter(ImageFilter.GaussianBlur(12 * k)))
    m = ImageChops.lighter(m, diff).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(FEATHER * k / 2))
    out = cl.convert('RGBA'); out.putalpha(m)
    out = Image.composite(out, Image.new('RGBA', (W, H), (0, 0, 0, 0)), m.point(lambda v: 255 if v > 0 else 0))   # 투명한 곳은 비워 파일을 작게
    out.save(sys.argv[3], optimize=True)
    print('덮개', sys.argv[3], '끝', [round(v) for v in pts[-1]])
    if len(sys.argv) > 4:
        pv = op.copy(); pv.paste(cl, (0, 0), m); pv.save(sys.argv[4], quality=88)

if __name__ == '__main__':
    main()
