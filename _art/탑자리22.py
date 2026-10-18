# 22 예루살렘 함락 · 23 곡과 마곡 길 시안 v0.1 (2026-10-19): 탑자리.py의 고르기와 참조 그림에 성(22)·고을과 북쪽 구름(23)을 더한다
# 사용: python 탑자리22.py 지도2.json 출력폴더 22|23
# 22 city(성벽, 시계 방향 점): 길 셋(0~2)이 성벽 바깥에서 끝나고(토성, 왕하 25:1), 길 3은 동남쪽 곁문(25:4)에서 들로 나가는 길(적은 들에서 곁문으로, 남은 자는 거꾸로).
#    temple·palace(성 안 표시), garden(왕의 동산), field(아나돗 밭, 남은 자가 가는 곳)
# 23 north(위쪽 구름 띠 아래 선), villages(성벽 없는 고을, 겔 38:11), 길 넷이 북쪽 끝에서 내려와 아래 가운데 고을로
# 결과: 출력폴더\ref<N>.png, preview<N>.png, 표준 출력에 spots
import sys, json, os, importlib.util
from PIL import ImageDraw

spec = importlib.util.spec_from_file_location('tj', os.path.join(os.path.dirname(os.path.abspath(__file__)), '탑자리.py'))
tj = importlib.util.module_from_spec(spec); spec.loader.exec_module(tj)


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    sid = sys.argv[3]; st = json.load(open(sys.argv[1], encoding='utf-8'))[sid]; out = sys.argv[2]
    pl, spots = tj.pick(st)
    im = tj.draw_ref(st, pl, os.path.join(out, f'ref{sid}.png')); d = ImageDraw.Draw(im)
    if sid == '22':
        city = [tuple(q) for q in st['city']]
        d.polygon(city, fill='#d6cbb0')   # 돌바닥과 집들
        for y in range(-10, 300, 26):
            for x in range(380, 940, 30):
                if tj_inside(city, x + 6, y + 6) and tj_inside(city, x + 22, y + 20):
                    d.rectangle([x + 4, y + 4, x + 22, y + 18], fill='#bfae8a', outline='#8f7e5e')
        tx, ty = st['temple']; d.rectangle([tx - 70, ty - 40, tx + 70, ty + 40], fill='#efe6cf', outline='#8f7e5e', width=3)
        px, py = st['palace']; d.rectangle([px - 50, py - 30, px + 50, py + 30], fill='#e3d3a8', outline='#8f7e5e', width=3)
        w = city + city[:1]
        d.line(w, fill='#5e5242', width=30, joint='curve'); d.line(w, fill='#a89c84', width=22, joint='curve'); d.line(w, fill='#c9bfa6', width=12, joint='curve')
        for x, y, r, col in st.get('marks2', []):
            d.ellipse([x - r, y - r * .62, x + r, y + r * .62], fill=col)
        for w2, col in zip((60, 56, 46, 24), ['#3b2614'] + st['road']):   # 길을 성벽 위에 다시(끝이 성벽에 닿게)
            for p in pl:
                d.line([tuple(map(round, q)) for q in p], fill=col, width=w2, joint='curve')
        gx, gy = st['sidegate']; d.rectangle([gx - 14, gy - 12, gx + 14, gy + 12], fill='#3b2a1a')
    if sid == '23':
        nl = [tuple(q) for q in st['north']]
        d.polygon([(0, 0), (1280, 0)] + nl[::-1], fill='#4a4a5a')   # 북쪽 끝의 구름 띠
        for x, y, r, col in st.get('marks2', []):
            d.ellipse([x - r, y - r * .62, x + r, y + r * .62], fill=col)
        for w2, col in zip((60, 56, 46, 24), ['#3b2614'] + st['road']):
            for p in pl:
                d.line([tuple(map(round, q)) for q in p], fill=col, width=w2, joint='curve')
        for vx, vy in st['villages']:
            for dx, dy in [(-40, -10), (0, -24), (38, -8), (-18, 18), (24, 20)]:
                d.rectangle([vx + dx - 14, vy + dy - 10, vx + dx + 14, vy + dy + 10], fill='#e8dcc0', outline='#7a6a4a', width=2)
    im.save(os.path.join(out, f'ref{sid}.png'))
    pv = im.copy(); dp = ImageDraw.Draw(pv)
    for q in tj.catmull(st.get('sky') or [[0, 0]])[::6]:   # 하늘길은 시안에만(참조 그림에 그리면 길로 그려진다)
        dp.ellipse([q[0] - 3, q[1] - 3, q[0] + 3, q[1] + 3], fill='#ffffff')
    for i, (x, y) in enumerate(spots):
        dp.ellipse([x - 31, y - 10, x + 31, y + 20], outline='#ffffff', width=3); dp.text((x - 4, y - 2), str(i), fill='#ffffff')
    for a in st.get('avoid', []): dp.rectangle(a, outline='#ff4040', width=1)
    pv.save(os.path.join(out, f'preview{sid}.png'))
    print(len(spots)); print(json.dumps(spots))


def tj_inside(poly, x, y):
    n, c = len(poly), False
    for i in range(n):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % n]
        if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1: c = not c
    return c


if __name__ == '__main__':
    main()
