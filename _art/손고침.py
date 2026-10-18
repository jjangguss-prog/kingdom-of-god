# 다시 그린 이야기 그림의 작은 잘못(손·팔이 하나 더, 머리 둘 달린 소)을 그 자리만 고쳐 그린다 v0.1 (2026-10-18)
# FLUX.2 [klein] 4B 참조 편집으로 상자 안을 다시 그리고, 가림(타원) 안만 원본 위에 부드럽게 덮는다. 나머지 픽셀은 그대로.
# 사용(생성 venv %LOCALAPPDATA%\buiknam_gen): python 손고침.py 손고침.json
# 손고침.json: {"항목": [{"key": "v1d", "상자": [x0, y0, x1, y1], "가림": [[cx, cy, rx, ry]], "프롬프트": "...", "시드": [1, 2, 3]}]}
#   "지움": true면 가림 안을 먼저 흐릿하게 문질러 넣는다([r,g,b]면 그 색으로 채운다). 좌표는 게임 그림(art\, 1536×864) 기준. 원본은 고르기_다시.json이 고른 raw\ 그림(1920×1080)이다.
# 결과: 고침\<key>_s<시드>.png(1920×1080 전체) + <key>_s<시드>_보기.jpg(고치기 전|후). 마음에 들면 raw\로 옮겨 고르기_다시.json에 적고 모으기.py를 돌린다.
import sys, os, json, time
os.environ.setdefault('HF_HOME', os.path.join(os.path.expanduser('~'), '.cache', 'huggingface'))
import torch
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = 'black-forest-labs/FLUX.2-klein-4B'
KEEP = (' Keep everything else exactly the same as the reference picture: the same people, faces, poses, clothes, colors, lighting, '
        'outlines and the same hand-drawn cartoon picture-book style. Every person has exactly two arms and two hands. No text.')
K = 1920 / 1536   # 게임 그림 좌표 → raw 좌표

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    job = json.load(open(sys.argv[1], encoding='utf-8'))
    pick = json.load(open(os.path.join(HERE, '고르기_다시.json'), encoding='utf-8'))
    od = os.path.join(HERE, '고침'); os.makedirs(od, exist_ok=True)
    from diffusers import Flux2KleinPipeline
    t0 = time.time(); pipe = Flux2KleinPipeline.from_pretrained(MODEL, torch_dtype=torch.bfloat16)
    pipe.enable_model_cpu_offload(); pipe.set_progress_bar_config(disable=True); print(f'모델 적재 {time.time()-t0:.0f}초', flush=True)
    for it in job['항목']:
        src = Image.open(os.path.join(HERE, it['원본']) if it.get('원본') else os.path.join(HERE, 'raw', pick[it['key']])).convert('RGB')   # 원본: 앞서 고친 그림에 이어서 고칠 때
        x0, y0, x1, y1 = [round(v * K) for v in it['상자']]
        crop = src.crop((x0, y0, x1, y1)); cw, ch = crop.size
        s = 1024 / max(cw, ch); w, h = max(256, round(cw * s / 16) * 16), max(256, round(ch * s / 16) * 16)
        mask = Image.new('L', (cw, ch), 0); d = ImageDraw.Draw(mask)
        for cx, cy, rx, ry in it['가림']:
            cx, cy, rx, ry = cx * K - x0, cy * K - y0, rx * K, ry * K
            d.ellipse((cx - rx, cy - ry, cx + rx, cy + ry), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(max(4, min(cw, ch) / 60)))
        if it.get('지움'):   # 지울 것을 먼저 흐릿하게 문질러 놓아야 모델이 그 자리를 옷·배경으로 새로 그린다(그대로 두면 다시 그려 넣는다)
            fill = Image.new('RGB', crop.size, tuple(it['지움']) if isinstance(it['지움'], list) else (0, 0, 0))
            blur = crop.filter(ImageFilter.GaussianBlur(it.get('번짐', 28)))
            crop_in = Image.composite(blur if not isinstance(it['지움'], list) else fill, crop, mask)
        else:
            crop_in = crop
        for sd in it.get('시드', [1]):
            name = f"{it.get('id', it['key'])}_s{sd}"; t = time.time()
            out = pipe(prompt=it['프롬프트'].strip() + KEEP, image=crop_in.resize((w, h), Image.LANCZOS), height=h, width=w,
                       guidance_scale=1.0, num_inference_steps=it.get('단계', 4), generator=torch.Generator('cpu').manual_seed(int(sd))).images[0]
            out = out.resize((cw, ch), Image.LANCZOS)
            fixed = src.copy(); fixed.paste(Image.composite(out, crop, mask), (x0, y0))
            fixed.save(os.path.join(od, name + '.png'))
            after = fixed.crop((x0, y0, x1, y1)); pv = Image.new('RGB', (cw * 2 + 8, ch), (40, 30, 20)); pv.paste(crop, (0, 0)); pv.paste(after, (cw + 8, 0))
            sc = min(1, 1400 / pv.width); pv.resize((round(pv.width * sc), round(pv.height * sc))).save(os.path.join(od, name + '_보기.jpg'), quality=88)
            print(name, f'{time.time()-t:.1f}초', flush=True)

if __name__ == '__main__':
    main()
