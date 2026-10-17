# 그린 배경에 길 맞추기 v0.1 (2026-10-18). 생성 venv(numpy·scipy)에서 돈다.
# 사용: python 길맞추기.py 배경.png 길.json 출력.png
# 길.json: {"paths": [[[x,y],...],...], "r": 26}  — 게임 좌표(1280×720)로 대강 찍은 점. 그림의 밝은 길 띠(모래색)를 찾아
#   점마다 둘레 r 안에서 길 가운데(길 가장자리에서 가장 먼 곳)로 옮기고, 화면 밖 점은 그대로 둔다.
# "route": true면 점을 들러야 할 곳으로 보고, 점과 점 사이를 길 띠 가운데로 따라가는 가장 싼 길(가운데일수록 쌈)로 잇고 gap마다 점을 다시 찍는다.
# 결과: 고친 점을 JSON으로 찍고, 출력.png에 배경 위로 길(게임과 같은 Catmull-Rom)과 점 번호를 그린다.
import sys, json, math
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage

W, H = 1280, 720


def catmull(ctrl, step=6):
    out, n = [], len(ctrl)
    P = lambda i: ctrl[max(0, min(n - 1, i))]
    for i in range(n - 1):
        p0, p1, p2, p3 = P(i - 1), P(i), P(i + 1), P(i + 2)
        m = max(2, math.ceil(math.hypot(p2[0] - p1[0], p2[1] - p1[1]) / step))
        for k in range(m):
            t = k / m; t2 = t * t; t3 = t2 * t
            f = lambda a, b, c, d: .5 * (2 * b + (-a + c) * t + (2 * a - 5 * b + 4 * c - d) * t2 + (-a + 3 * b - 3 * c + d) * t3)
            out.append((f(p0[0], p1[0], p2[0], p3[0]), f(p0[1], p1[1], p2[1], p3[1])))
    out.append(tuple(ctrl[-1]))
    return out


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    im = Image.open(sys.argv[1]).convert('RGB').resize((W, H), Image.LANCZOS)
    job = json.load(open(sys.argv[2], encoding='utf-8'))
    a = np.asarray(im).astype(int); R, G, B = a[..., 0], a[..., 1], a[..., 2]
    lo = job.get('lo', [205, 185, 140])
    road = (R > lo[0]) & (G > lo[1]) & (B > lo[2]) & (R >= G - 4) & (G >= B) & (R - B < 95)
    road = ndimage.binary_opening(road, iterations=2)
    dist = ndimage.distance_transform_edt(road)
    r = job.get('r', 26)
    out = []
    if job.get('route'):
        from skimage.graph import route_through_array
        cost = np.where(road, 1.0 / (dist ** 2 + .5), 50.0)
        gap = job.get('gap', 42)
        for path in job['paths']:
            inside = [(x, y) for x, y in path if 0 <= x < W and 0 <= y < H]
            pre = [p for p in path[:2] if not (0 <= p[0] < W and 0 <= p[1] < H)]
            post = [p for p in path[-2:] if not (0 <= p[0] < W and 0 <= p[1] < H)]
            pix = []
            for (x0, y0), (x1, y1) in zip(inside, inside[1:]):
                idx, _ = route_through_array(cost, (int(y0), int(x0)), (int(y1), int(x1)), fully_connected=True, geometric=True)
                pix += [(c, rr) for rr, c in idx]
            pts, acc = [list(pix[0])], 0
            for a, b in zip(pix, pix[1:]):
                acc += math.hypot(b[0] - a[0], b[1] - a[1])
                if acc >= gap: pts.append(list(b)); acc = 0
            if pts[-1] != list(pix[-1]): pts.append(list(pix[-1]))
            out.append([list(p) for p in pre] + pts + [list(p) for p in post])
        job['paths'] = []
    for path in job['paths']:
        np_ = []
        for x, y in path:
            if not (4 <= x < W - 4 and 4 <= y < H - 4):
                np_.append([x, y]); continue
            x0, x1, y0, y1 = max(0, int(x - r)), min(W, int(x + r + 1)), max(0, int(y - r)), min(H, int(y + r + 1))
            win = dist[y0:y1, x0:x1].copy()
            yy, xx = np.mgrid[y0:y1, x0:x1]
            win[(xx - x) ** 2 + (yy - y) ** 2 > r * r] = 0
            if win.max() < 3:
                np_.append([x, y]); print('길을 못 찾음', x, y); continue
            # 길 가운데에 가까우면서 처음 점에서 멀지 않게
            score = win - .08 * np.hypot(xx - x, yy - y)
            k = np.unravel_index(np.argmax(score), score.shape)
            np_.append([int(xx[k]), int(yy[k])])
        out.append(np_)
    print(json.dumps(out))
    ov = im.copy(); d = ImageDraw.Draw(ov)
    mask = Image.fromarray((road * 90).astype('uint8'))
    ov.paste((255, 0, 255), (0, 0), mask)
    cols = [(255, 40, 40), (40, 120, 255), (40, 200, 40), (255, 200, 0), (200, 0, 200)]
    for i, p in enumerate(out + [job.get('lane', [])]):
        if len(p) < 2: continue
        c = catmull(p)
        d.line(c, fill=cols[i % len(cols)], width=3)
        for j, (x, y) in enumerate(p):
            d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=cols[i % len(cols)])
    for s in job.get('spots', []):
        d.ellipse([s[0] - 31, s[1] - 15, s[0] + 31, s[1] + 15], outline=(255, 255, 0), width=2)
    for m in job.get('marks', []):
        d.ellipse([m[0] - 8, m[1] - 8, m[0] + 8, m[1] + 8], outline=(0, 255, 255), width=3)
    ov.save(sys.argv[3])


if __name__ == '__main__':
    main()
