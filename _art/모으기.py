# 고른 그림을 게임 폴더(art\)로 모은다 v0.1 (2026-10-11). 썸네일 venv(%LOCALAPPDATA%\buiknam_thumb)에서 돈다.
# 사용: python 모으기.py [고르기.json]
# 고르기.json: {"noah": "noah_s1_65e1aa.png", "bg1": "bg1_s1_f77c3e.png", ...} — 값은 raw\ 안의 파일 이름
#   이름이 bg로 시작하면 배경: 1536×864 JPEG(품질 86)로 art\bgN.jpg
#   그 밖은 누끼(birefnet-general) → 그림 둘레만 남겨 자르고(cut\, 긴 변 512) → LIMIT 크기로 줄여 art\<이름>.png
#   누끼 결과는 cut\에 남겨 두고 다시 쓰지 않는다(고친 그림을 다시 뽑으면 파일 이름이 바뀐다).
# 그림생성.py(FLUX)와 동시에 돌리지 않는다(GPU 12GB).
import sys, os, json, re
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
RAW, CUT, ART = (os.path.join(HERE, d) for d in ('raw', 'cut', os.path.join('..', 'art')))
MAX = 512
# 게임 화면에 그려지는 크기의 3배쯤(고해상도 폰). 영웅은 초상화에도 쓰여 크게, 탑·전차는 크게, 나머지 병사·적은 256
CROP = {'v3a': .035, 'v4c': .03, 's7b': (.09, .18, .91, 1), 's3c': (0, .25, .75, 1)}   # 비율. 넷이면 (왼, 위, 오른, 아래): s7b는 이야기 글 상자 위로 물줄기가 보이게, s3c는 오른쪽 끝의 아이 머리를 든 사람·머리가 둘인 사람을 잘라 냄(10-12 사용자)
LIMIT = {'noah': 512, 'moses': 512, 'joshua': 512, 'caleb': 512, 'chariot': 384, 'pharaoh': 512, 'og': 512, 'giant': 384, 'levi_priest': 384, 'levi_choir': 384, 'art_menorah': 384, 'watch_jordan': 384, 'c_chariot': 384, 'c_chariot_empty': 384, 'deborah': 384, 'barak': 384, 'm_camel': 384, 'oreb': 384, 'zeeb': 384, 'gideon': 384, 'b_giant': 384, 'shep_nazirite': 384, 'samuel': 384, 'david': 512, 'goliath': 512, 'b_bearer': 384, 'jonathan': 384, 'saul': 384, 'saul_throw': 384, 'saul_fit': 384, 'saul_kneel': 384, 'shep_mighty': 384, 'watch_benjamin': 384, 'k_camel': 384}   # 탑(이름 끝이 숫자)은 384

def cutter():
    import onnxruntime as ort
    try:
        ort.preload_dlls()
    except Exception:
        pass
    from rembg import new_session, remove
    try:
        if os.environ.get('NUKKI_DEVICE', '').lower() == 'cpu':   # FLUX가 GPU를 쓰는 중이면 CPU로(장당 약 17초)
            raise RuntimeError('NUKKI_DEVICE=cpu')
        s = new_session('birefnet-general', providers=[('CUDAExecutionProvider', {'cudnn_conv_algo_search': 'HEURISTIC'}), 'CPUExecutionProvider'])
    except Exception as e:
        print('GPU 실패 → CPU', str(e)[-80:]); s = new_session('birefnet-general', providers=['CPUExecutionProvider'])
    def cut(im):
        out = remove(im, session=s, post_process_mask=True)
        a = out.getchannel('A').point(lambda v: 0 if v < 10 else v); out.putalpha(a)
        box = a.getbbox()
        if box:
            p = 6; out = out.crop((max(0, box[0]-p), max(0, box[1]-p), min(im.width, box[2]+p), min(im.height, box[3]+p)))
        k = MAX / max(out.size)
        return out.resize((round(out.width*k), round(out.height*k)), Image.LANCZOS) if k < 1 else out
    return cut

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    pick = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '고르기.json'), encoding='utf-8'))
    os.makedirs(CUT, exist_ok=True); os.makedirs(ART, exist_ok=True)
    cut = None
    for key, f in pick.items():
        src = os.path.join(RAW, f)
        if key.startswith('bg') or (re.fullmatch(r'[sv]\d+[a-z]', key) or key == 'title'):   # 배경·이야기·승리·제목 그림
            im = Image.open(src).convert('RGB')
            c = CROP.get(key, 0)   # 그림 둘레에 액자 테두리가 그려진 것은 그만큼 잘라 낸다
            if isinstance(c, tuple): im = im.crop((round(im.width * c[0]), round(im.height * c[1]), round(im.width * c[2]), round(im.height * c[3])))
            elif c: im = im.crop((round(im.width * c), round(im.height * c), round(im.width * (1 - c)), round(im.height * (1 - c))))
            im.resize((1536, 864), Image.LANCZOS).save(os.path.join(ART, key + '.jpg'), quality=86, optimize=True)
            print(key, '배경'); continue
        c = os.path.join(CUT, f)
        if not os.path.exists(c):
            cut = cut or cutter()
            cut(Image.open(src).convert('RGB')).save(c, optimize=True)
        im = Image.open(c)
        lim = LIMIT.get(key) or (384 if key[-1].isdigit() and not key.startswith('a_') else 256)   # a_ 짐승 짝(a_sheep2)은 탑이 아니다
        k = lim / max(im.size)
        if k < 1:
            im = im.resize((round(im.width*k), round(im.height*k)), Image.LANCZOS)
        im.save(os.path.join(ART, key + '.png'), optimize=True)
        print(key, im.size)

if __name__ == '__main__':
    main()
