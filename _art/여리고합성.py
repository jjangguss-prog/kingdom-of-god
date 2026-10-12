# 9 여리고 배경 합성 v0.1 (2026-10-12). 썸네일 venv(%LOCALAPPDATA%\buiknam_thumb, rembg)에서 돈다. 그림생성.py와 동시에 돌리지 않는다(GPU 12GB).
# 생성 모델이 성을 그리면 성이 둘레 길의 북쪽을 덮어 버려서, 빈 언덕만 있는 배경(bg9base)과 따로 그린 성(jericho)을 합친다.
# 무너진 성(jericho_fall)은 성 그림을 참조로 같은 구도로 그린 것이라, 두 그림을 같은 상자로 잘라 같은 자리에 얹는다.
# 그러면 성 밖은 무너지기 전과 똑같아서 게임에서 bg9 → bg9_fall로 겹쳐 바꿀 수 있다.
# 사용: python 여리고합성.py raw/bg9base_sN.png raw/jericho_sN.png [raw/jericho_fall_sN.png] [--cx 440 --cy 330 --w 360]
#   cx, cy: 성 그림 가운데(게임 좌표 1280×720, 둘레 길의 가운데), w: 성 그림 폭(게임 좌표)
# 결과: ..\art\bg9.jpg, ..\art\bg9_fall.jpg(셋째 그림이 있을 때), cut\jericho*_full.png(누끼 캐시), ref2\check9.png(길을 겹쳐 본 확인 그림)
import sys, os, json, argparse
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.path.join(HERE, '..', 'art')
GW, GH, BW, BH = 1280, 720, 1536, 864
K = BW / GW
_sess = None


def nukki(path):
    """BiRefNet 누끼를 원본 크기 그대로(자르지 않고) cut\\<이름>_full.png로 남긴다."""
    global _sess
    out = os.path.join(HERE, 'cut', os.path.basename(path)[:-4] + '_full.png')
    if os.path.exists(out):
        return Image.open(out).convert('RGBA')
    from rembg import new_session, remove
    if _sess is None:
        try:
            if os.environ.get('NUKKI_DEVICE', '').lower() == 'cpu':   # FLUX가 GPU를 쓰는 중이면 CPU로
                raise RuntimeError('cpu')
            _sess = new_session('birefnet-general', providers=[('CUDAExecutionProvider', {'cudnn_conv_algo_search': 'HEURISTIC'}), 'CPUExecutionProvider'])
        except Exception:
            _sess = new_session('birefnet-general', providers=['CPUExecutionProvider'])
    im = remove(Image.open(path).convert('RGB'), session=_sess, post_process_mask=True)
    im.putalpha(im.getchannel('A').point(lambda v: 0 if v < 10 else v))
    os.makedirs(os.path.dirname(out), exist_ok=True); im.save(out)
    return im


def place(base, city, cx, cy, w):
    tw = round(w * K); th = round(city.height * tw / city.width)
    c = city.resize((tw, th), Image.LANCZOS)
    x, y = round(cx * K - tw / 2), round(cy * K - th / 2)
    out = base.convert('RGBA')
    sh = Image.new('RGBA', out.size, (0, 0, 0, 0)); d = ImageDraw.Draw(sh)   # 성 밑 그림자: 언덕에 내려앉아 보이게
    d.ellipse([x + tw * .06, y + th * .55, x + tw * .94, y + th * 1.02], fill=(40, 26, 12, 90))
    out = Image.alpha_composite(out, sh.filter(ImageFilter.GaussianBlur(14)))
    out.alpha_composite(c, (x, y))
    return out.convert('RGB'), (x, y, tw, th)


def check(im, box, path):
    import importlib.util
    st = json.load(open(os.path.join(HERE, '지도2.json'), encoding='utf-8'))['9']
    spec = importlib.util.spec_from_file_location('tj', os.path.join(HERE, '탑자리.py')); tj = importlib.util.module_from_spec(spec); spec.loader.exec_module(tj)
    v = im.resize((GW, GH), Image.LANCZOS); d = ImageDraw.Draw(v)
    for p in st['paths']:
        d.line([tuple(map(round, q)) for q in tj.catmull(p)], fill=(255, 40, 40), width=3)
    x, y, tw, th = box; d.rectangle([x / K, y / K, (x + tw) / K, (y + th) / K], outline=(60, 160, 255), width=2)
    v.save(path)


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    a = argparse.ArgumentParser()
    a.add_argument('base'); a.add_argument('city'); a.add_argument('fall', nargs='?')
    a.add_argument('--cx', type=float, default=440); a.add_argument('--cy', type=float, default=330); a.add_argument('--w', type=float, default=360)
    o = a.parse_args()
    base = Image.open(os.path.join(HERE, o.base)).convert('RGB').resize((BW, BH), Image.LANCZOS)
    city = nukki(os.path.join(HERE, o.city))
    fall = nukki(os.path.join(HERE, o.fall)) if o.fall else None
    if fall is not None and fall.size != city.size:
        fall = fall.resize(city.size, Image.LANCZOS)
    box = city.getchannel('A').getbbox()                       # 두 그림을 같은 상자로 자른다
    if fall is not None:
        fb = fall.getchannel('A').getbbox()
        box = (min(box[0], fb[0]), min(box[1], fb[1]), max(box[2], fb[2]), max(box[3], fb[3]))
    im, pb = place(base, city.crop(box), o.cx, o.cy, o.w)
    im.save(os.path.join(ART, 'bg9.jpg'), quality=86, optimize=True)
    check(im, pb, os.path.join(HERE, 'ref2', 'check9.png'))
    print('bg9', pb)
    if fall is not None:
        fim, _ = place(base, fall.crop(box), o.cx, o.cy, o.w)
        fim.save(os.path.join(ART, 'bg9_fall.jpg'), quality=86, optimize=True)
        fim.resize((GW, GH), Image.LANCZOS).save(os.path.join(HERE, 'ref2', 'check9_fall.png'))
        print('bg9_fall')


if __name__ == '__main__':
    main()
