# 길 옆 탑 자리 고르기 + 길 그림(배경 참조용) v0.1 (2026-10-11)
# 사용: python 탑자리.py 지도.json 출력폴더
# 지도.json: {"2": {"paths": [[[x,y],...],...], "avoid": [[x0,y0,x1,y1],...], "n": 14, "base": "#c9b07a", "road": ["#9b7442","#d9b878","#e8cc95"], "marks": [[x,y,r,"#hex"],...], "river": [[x,y],...], "riverW": 46}}
# river(선택, 11 기손 강): 길 아래에 강을 그리고, 강에서 riverW/2+34 안에는 탑 자리를 두지 않는다
# lanes(선택, 18 도단 v0.2 2026-10-17): 적이 다니지 않는 길(사마리아 길). 좁게 그리고 탑 자리는 피하지만 덮을 길로 세지 않는다
# 결과: 스테이지마다 spots(JSON 출력) + 출력폴더\ref<N>.png(1280×720 참조 그림: 바탕색, 길, 표시) + preview<N>.png(탑 자리 표시)
# 게임과 같은 Catmull-Rom으로 길을 그린다. 탑 자리는 길에서 타원(31×15)이 떨어지게, 길을 고르게 덮도록(한계 이득) 고른다.
import sys, json, math
from PIL import Image, ImageDraw

W, H = 1280, 720

def catmull(ctrl, step=9):
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

def resample(pts, gap):
    out = [pts[0]]; acc = 0
    for a, b in zip(pts, pts[1:]):
        d = math.hypot(b[0] - a[0], b[1] - a[1]); acc += d
        if acc >= gap:
            out.append(b); acc = 0
    return out

def pick(st):
    pl = [catmull(c) for c in st['paths']]
    dense = [q for p in pl + [catmull(c) for c in st.get('lanes', [])] for q in p]
    samples = []
    for p in pl:
        for q in resample(p, 18):
            if -10 < q[0] < W + 10 and -10 < q[1] < H + 10 and not any(abs(q[0] - s[0]) < 9 and abs(q[1] - s[1]) < 9 for s in samples):
                samples.append(q)
    river = catmull(st['river']) if st.get('river') else []
    avoid = st.get('avoid', []) + [[0, 0, 430, 78], [1110, 0, 1280, 80], [900, 600, 1280, 720]]
    def ok(x, y):
        if not (46 < x < W - 46 and 84 < y < H - 30): return False
        if any(a[0] <= x <= a[2] and a[1] <= y <= a[3] for a in avoid): return False
        for q in dense:
            if ((x - q[0]) / 61) ** 2 + ((y - q[1]) / 45) ** 2 < 1: return False
        for q in river:
            if math.hypot(x - q[0], (y - q[1]) * 1.2) < st.get('riverW', 46) / 2 + 34: return False
        return True
    cands = []
    for q in resample([q for p in pl for q in p], 10):
        for ang in range(0, 360, 30):
            for r in (64, 74, 86):
                x = q[0] + math.cos(math.radians(ang)) * r; y = q[1] + math.sin(math.radians(ang)) * r * .8
                if ok(x, y): cands.append((round(x), round(y)))
    cands = list(set(cands))
    cover = {c: [i for i, s in enumerate(samples) if math.hypot(c[0] - s[0], (c[1] - s[1]) * 1.25) < 150] for c in cands}
    cnt = [0] * len(samples); chosen = []
    for _ in range(st.get('n', 14)):
        best, bv = None, -1
        for c in cands:
            if any(math.hypot(c[0] - o[0], (c[1] - o[1]) * 1.35) < 86 for o in chosen): continue
            v = sum(1 / (1 + cnt[i]) ** 1.6 for i in cover[c])
            if v > bv: bv, best = v, c
        if not best: break
        chosen.append(best)
        for i in cover[best]: cnt[i] += 1
    return pl, chosen

def draw_ref(st, pl, path):
    im = Image.new('RGB', (W, H), st.get('base', '#c9b07a')); d = ImageDraw.Draw(im)
    for x, y, r, col in st.get('marks', []):
        d.ellipse([x - r, y - r * .62, x + r, y + r * .62], fill=col)
    if st.get('river'):
        rv = [tuple(map(round, q)) for q in catmull(st['river'])]; rw = st.get('riverW', 46)
        for w, col in ((rw + 8, '#7a8a6a'), (rw, '#3f86b0'), (rw - 18, '#5aa3c8')):
            d.line(rv, fill=col, width=w, joint='curve')
    for c in st.get('lanes', []):
        lp = [tuple(map(round, q)) for q in catmull(c)]
        for w, col in zip((40, 36, 22), ['#3b2614'] + st.get('road', ['#9b7442', '#d9b878', '#e8cc95'])[1:]):
            d.line(lp, fill=col, width=w, joint='curve')
    for w, col in zip((60, 56, 46, 24), ['#3b2614'] + st.get('road', ['#9b7442', '#d9b878', '#e8cc95'])):
        for p in pl:
            d.line([tuple(map(round, q)) for q in p], fill=col, width=w, joint='curve')
            for q in (p[0], p[-1]):
                d.ellipse([q[0] - w / 2, q[1] - w / 2, q[0] + w / 2, q[1] + w / 2], fill=col)
    im.save(path)
    return im

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    data = json.load(open(sys.argv[1], encoding='utf-8')); out = sys.argv[2]
    res = {}
    for sid, st in data.items():
        pl, spots = pick(st)
        res[sid] = spots
        im = draw_ref(st, pl, f'{out}/ref{sid}.png').copy(); d = ImageDraw.Draw(im)
        for i, (x, y) in enumerate(spots):
            d.ellipse([x - 31, y - 10, x + 31, y + 20], outline='#ffffff', width=3); d.text((x - 4, y - 2), str(i), fill='#ffffff')
        for a in st.get('avoid', []): d.rectangle(a, outline='#ff4040', width=2)
        im.save(f'{out}/preview{sid}.png')
        print(sid, len(spots))
    print(json.dumps(res))

if __name__ == '__main__':
    main()
