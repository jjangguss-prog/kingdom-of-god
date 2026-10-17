# 19 예루살렘 포위 길 시안 v0.1 (2026-10-17): 탑자리.py의 고르기와 참조 그림에 성벽과 성 위 자리를 더한다
# 사용: python 탑자리19.py 지도2.json 출력폴더   (지도2.json의 "19"만 본다)
# wall(성벽): 길 아래에 돌 성벽을 그린다. 길이 성벽을 지나는 곳이 성문이다
# fixed(성 위 자리): 성벽 위에 미리 정한 탑 자리. 먼저 고른 것으로 치고 나머지를 탑자리.py와 같은 방법(한계 이득)으로 고른다
# 결과: 출력폴더\ref19.png(성벽까지 그린 참조 그림), preview19.png(성 위 자리는 노란 테), 표준 출력에 spots
import sys, json, math, os, importlib.util
from PIL import ImageDraw

spec = importlib.util.spec_from_file_location('tj', os.path.join(os.path.dirname(os.path.abspath(__file__)), '탑자리.py'))
tj = importlib.util.module_from_spec(spec); spec.loader.exec_module(tj)

def pick(st):
    pl = [tj.catmull(c) for c in st['paths']]
    dense = [q for p in pl for q in p]
    samples = []
    for p in pl:
        for q in tj.resample(p, 18):
            if -10 < q[0] < tj.W + 10 and -10 < q[1] < tj.H + 10 and not any(abs(q[0] - s[0]) < 9 and abs(q[1] - s[1]) < 9 for s in samples):
                samples.append(q)
    avoid = st.get('avoid', []) + [[0, 0, 430, 78], [1110, 0, 1280, 80], [900, 600, 1280, 720]]
    def ok(x, y):
        if not (46 < x < tj.W - 46 and 84 < y < tj.H - 30): return False
        if any(a[0] <= x <= a[2] and a[1] <= y <= a[3] for a in avoid): return False
        return all(((x - q[0]) / 61) ** 2 + ((y - q[1]) / 45) ** 2 >= 1 for q in dense)
    fixed = [tuple(f) for f in st.get('fixed', [])]
    cands = set()
    for q in tj.resample(dense, 10):
        for ang in range(0, 360, 30):
            for r in (64, 74, 86):
                x = q[0] + math.cos(math.radians(ang)) * r; y = q[1] + math.sin(math.radians(ang)) * r * .8
                if ok(x, y): cands.add((round(x), round(y)))
    cands = list(cands) + fixed
    cover = {c: [i for i, s in enumerate(samples) if math.hypot(c[0] - s[0], (c[1] - s[1]) * 1.25) < 150] for c in cands}
    cnt = [0] * len(samples); chosen = []
    def take(c):
        chosen.append(c)
        for i in cover[c]: cnt[i] += 1
    for f in fixed: take(f)
    while len(chosen) < st.get('n', 14):
        best, bv = None, -1
        for c in cands:
            if c in chosen or any(math.hypot(c[0] - o[0], (c[1] - o[1]) * 1.35) < 86 for o in chosen): continue
            v = sum(1 / (1 + cnt[i]) ** 1.6 for i in cover[c])
            if v > bv: bv, best = v, c
        if not best: break
        take(best)
    return pl, chosen

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    st = json.load(open(sys.argv[1], encoding='utf-8'))['19']; out = sys.argv[2]
    pl, spots = pick(st)
    im = tj.draw_ref(st, pl, f'{out}/ref19.png'); d = ImageDraw.Draw(im)
    wl = [tuple(map(round, q)) for q in tj.catmull(st['wall'])]
    for w, col in ((34, '#5e5242'), (28, '#a89c84'), (18, '#c9bfa6'), (4, '#8f846c')):
        d.line(wl, fill=col, width=w, joint='curve')
    for w, col in zip((60, 56, 46, 24), ['#3b2614'] + st.get('road', ['#9b7442', '#d9b878', '#e8cc95'])):   # 성문: 길을 성벽 위에 다시 그림
        for p in pl:
            seg = [q for q in p if abs(q[0] - st['gate'][0]) < 70 and abs(q[1] - st['gate'][1]) < 40]
            if len(seg) > 1: d.line([tuple(map(round, q)) for q in seg], fill=col, width=w, joint='curve')
    im.save(f'{out}/ref19.png')
    d = ImageDraw.Draw(im); fixed = [tuple(f) for f in st.get('fixed', [])]
    for i, (x, y) in enumerate(spots):
        d.ellipse([x - 31, y - 10, x + 31, y + 20], outline='#ffd23f' if (x, y) in fixed else '#ffffff', width=3); d.text((x - 4, y - 2), str(i), fill='#ffffff')
    for a in st.get('avoid', []): d.rectangle(a, outline='#ff4040', width=2)
    im.save(f'{out}/preview19.png')
    L = lambda p: round(sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(p, p[1:])))
    print('길', [L(p) for p in pl], '하늘길', L(tj.catmull(st['sky'])), '탑 자리', len(spots))
    print(json.dumps([list(c) for c in spots]))

if __name__ == '__main__':
    main()
