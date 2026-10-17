# 20 무너진 성벽 길 시안 v0.1 (2026-10-17): 탑자리.py의 고르기와 참조 그림에 무너진 성벽·성문·틈과 하늘길을 더한다
# 사용: python 탑자리20.py 지도2.json 출력폴더   (지도2.json의 "20"만 본다)
# wall(성벽, 시계 방향 점): 길 아래에 무너진 낮은 돌 성벽을 그린다. gates(성문 이름: 자리): 검은 문 자리. 둘레에는 탑 자리를 두지 않는다
# breaches(무너진 틈): 길이 성벽을 지나는 흙무더기. 느헤미야가 쌓으면 그 자리가 성 위 자리가 된다(고르기에서 빼고 따로 표시)
# paths 0~2는 틈길, 3~5는 틈을 메운 뒤의 성문길(같은 들머리에서 갈라짐). 모두 길로 쳐서 탑 자리를 피한다
# 결과: 출력폴더\ref20.png(성벽까지 그린 참조 그림), preview20.png(틈의 성 위 자리는 노란 W), 표준 출력에 spots
import sys, json, os, importlib.util
from PIL import ImageDraw

spec = importlib.util.spec_from_file_location('tj', os.path.join(os.path.dirname(os.path.abspath(__file__)), '탑자리.py'))
tj = importlib.util.module_from_spec(spec); spec.loader.exec_module(tj)

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    st = json.load(open(sys.argv[1], encoding='utf-8'))['20']; out = sys.argv[2]
    st = dict(st, avoid=st.get('avoid', []) + [[x - 30, y - 24, x + 30, y + 24] for x, y in st['gates'].values()])
    pl, spots = tj.pick(st)
    im = tj.draw_ref(st, pl, os.path.join(out, 'ref20.png')); d = ImageDraw.Draw(im)
    w = [tuple(q) for q in st['wall'] + st['wall'][:1]]
    d.line(w, fill='#6e6658', width=20, joint='curve'); d.line(w, fill='#a39a88', width=12, joint='curve')
    for x, y in st['breaches']: d.ellipse([x - 26, y - 16, x + 26, y + 16], fill='#9b8460')
    for x, y in st['gates'].values(): d.rectangle([x - 12, y - 9, x + 12, y + 9], fill='#3b2a1a')
    im.save(os.path.join(out, 'ref20.png'))
    for i, (x, y) in enumerate(spots):
        d.ellipse([x - 31, y - 10, x + 31, y + 20], outline='#ffffff', width=3); d.text((x - 4, y - 2), str(i), fill='#ffffff')
    for j, (x, y) in enumerate(st['breaches']):
        d.ellipse([x - 31, y - 10, x + 31, y + 20], outline='#ffd23a', width=3); d.text((x - 6, y - 2), 'W%d' % j, fill='#ffd23a')
    for a in st['avoid']: d.rectangle(a, outline='#ff4040', width=2)
    im.save(os.path.join(out, 'preview20.png'))
    print(json.dumps(spots))

if __name__ == '__main__':
    main()
