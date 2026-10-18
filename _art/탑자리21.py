# 21 다니엘의 환상 길 시안 v0.1 (2026-10-18): 탑자리.py의 고르기와 참조 그림에 큰 바다·바닷가·성도들의 진을 더한다
# 사용: python 탑자리21.py 지도2.json 출력폴더   (지도2.json의 "21"만 본다)
# sea(바닷가 선, 왼쪽에서 오른쪽): 그 위는 밤의 큰 바다(단 7:2). 길 셋이 바다에서 올라와(7:3) 아래 가운데 언덕의 진(camp)으로 모인다
# 결과: 출력폴더\ref21.png(바다까지 그린 참조 그림), preview21.png, 표준 출력에 spots
import sys, json, os, importlib.util
from PIL import ImageDraw

spec = importlib.util.spec_from_file_location('tj', os.path.join(os.path.dirname(os.path.abspath(__file__)), '탑자리.py'))
tj = importlib.util.module_from_spec(spec); spec.loader.exec_module(tj)

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    st = json.load(open(sys.argv[1], encoding='utf-8'))['21']; out = sys.argv[2]
    shore = st['sea']
    st = dict(st, avoid=st.get('avoid', []) + [[x - 50, 0, x + 50, y + 70] for x, y in shore])   # 바다와 물가에는 탑 자리를 두지 않는다
    pl, spots = tj.pick(st)
    im = tj.draw_ref(st, pl, os.path.join(out, 'ref21.png')); d = ImageDraw.Draw(im)
    poly = [(0, 0), (1280, 0)] + [tuple(q) for q in shore[::-1]]
    d.polygon(poly, fill='#1d3a5c')
    for k in range(5):   # 물결 줄
        pts = [(x, y - 18 - k * 26) for x, y in shore]
        d.line(pts, fill='#3d6a92', width=4, joint='curve')
    d.line([tuple(q) for q in shore], fill='#d8c79a', width=10, joint='curve')   # 모래 물가
    for x, y, rx, ry, col in st.get('blobs', []):
        d.ellipse([x - rx, y - ry, x + rx, y + ry], fill=col)
    for p in pl:   # 길은 물가부터 다시 그린다(바다 위에는 길이 없다)
        q = [tuple(map(round, a)) for a in p if a[1] > min(y for _, y in shore) + 10]
        for w, col in zip((60, 56, 46, 24), ['#3b2614'] + st['road']):
            if len(q) > 1: d.line(q, fill=col, width=w, joint='curve')
    cx, cy = st['camp']
    for dx, dy in [(-60, -6), (55, -10), (-25, 30), (35, 34)]:
        d.polygon([(cx + dx - 22, cy + dy + 14), (cx + dx, cy + dy - 18), (cx + dx + 22, cy + dy + 14)], fill='#c9b48a')
    im.save(os.path.join(out, 'ref21.png'))
    pv = im.copy(); dp = ImageDraw.Draw(pv)
    for i, (x, y) in enumerate(spots):
        dp.ellipse([x - 31, y - 10, x + 31, y + 20], outline='#ffffff', width=3); dp.text((x - 4, y - 2), str(i), fill='#ffffff')
    for a in st.get('avoid', []): dp.rectangle(a, outline='#ff4040', width=1)
    pv.save(os.path.join(out, 'preview21.png'))
    print(len(spots)); print(json.dumps(spots))

if __name__ == '__main__':
    main()
