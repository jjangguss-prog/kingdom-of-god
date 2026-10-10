# Kingdom of God 게임 그림 누끼 v0.1 (2026-10-11)
# raw\*.png(흰 배경)에서 배경을 걷어 내고 그림만 남긴다. rembg BiRefNet-general(~/.rembg/models). 썸네일 venv(%LOCALAPPDATA%\buiknam_thumb)에서 돈다.
# 사용: python 누끼.py raw cut [이름 일부 ...]
# 결과: cut\<같은 이름>.png(투명 배경, 그림 둘레만 남기고 잘라 냄, 긴 변 최대 512px). 이미 있으면 건너뛴다.
# 그림생성.py(FLUX)와 동시에 돌리지 않는다(GPU 12GB).
import sys, os
import onnxruntime as ort
try:
    ort.preload_dlls()
except Exception:
    pass
from rembg import new_session, remove
from PIL import Image

MAX = 512

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    src, dst = sys.argv[1], sys.argv[2]; keys = sys.argv[3:]
    os.makedirs(dst, exist_ok=True)
    files = [f for f in sorted(os.listdir(src)) if f.endswith('.png') and (not keys or any(k in f for k in keys))
             and not os.path.exists(os.path.join(dst, f))]
    if not files:
        print('할 것 없음'); return
    try:
        sess = new_session('birefnet-general', providers=[('CUDAExecutionProvider', {'cudnn_conv_algo_search': 'HEURISTIC'}), 'CPUExecutionProvider'])
    except Exception as e:
        print('GPU 실패 → CPU', str(e)[-80:]); sess = new_session('birefnet-general', providers=['CPUExecutionProvider'])
    for f in files:
        im = Image.open(os.path.join(src, f)).convert('RGB')
        out = remove(im, session=sess, post_process_mask=True)
        a = out.getchannel('A').point(lambda v: 0 if v < 10 else v)
        out.putalpha(a)
        box = a.getbbox()
        if box:
            pad = 6; box = (max(0, box[0]-pad), max(0, box[1]-pad), min(im.width, box[2]+pad), min(im.height, box[3]+pad))
            out = out.crop(box)
        k = MAX / max(out.size)
        if k < 1:
            out = out.resize((round(out.width*k), round(out.height*k)), Image.LANCZOS)
        out.save(os.path.join(dst, f), optimize=True)
        print(f, out.size, flush=True)

if __name__ == '__main__':
    main()
