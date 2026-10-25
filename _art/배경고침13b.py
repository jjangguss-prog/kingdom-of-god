# 13 미스바 배경(bg13) 길 위 뾰족 바위 지우기 v0.1 (2026-10-25)
# 10-25 사용자: "미스바 맵에서는 길 한가운데 바위가 가로막고 있는데 장애물인지 헷갈릴 것 같아. 아무 의미 없어 보이는 바위인데 치워줘."
# 설계의 센(삼상 7:12, '이빨')은 두 길 사이 쐐기 땅의 바위다. 그림에는 쐐기 땅에 바위 무리가 따로 있고, 뾰족 바위 하나가 길 0의 오른쪽 가장자리 위에 서 있었다.
# 그 바위와 오른쪽 풀밭의 그림자 자리만 FLUX.2 klein 참조 편집으로 길과 풀로 다시 그리고 나머지는 그대로 둔다(배경고침13.py와 같은 방식).
# 사용(생성 venv %LOCALAPPDATA%\buiknam_gen): python 배경고침13b.py [시드 ...] → raw\bg13_fix2_s<시드>.png(1536×864) + 고침\bg13_fix2_s<시드>_보기.jpg
import sys, os, json, time
os.environ.setdefault('HF_HOME', os.path.join(os.path.expanduser('~'), '.cache', 'huggingface'))
import torch
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = 'black-forest-labs/FLUX.2-klein-4B'
BOX = (400, 240, 784, 624)   # 고칠 상자(배경 그림 좌표, 384×384)
ROCK = [(568, 330), (604, 356), (628, 430), (694, 438), (700, 500), (640, 510), (612, 532), (560, 542), (520, 536), (502, 500), (508, 456), (532, 414), (546, 364)]   # 바위·밑동 풀·오른쪽 그림자
PROMPT = ("Edit the picture. Remove the tall grey pointed rock and the small grey rocks at its foot, and remove its dark shadow on the grass. "
          "Where the rock was, continue the sandy dirt road with its thin dark brown outline, following the existing curve and edges of the road exactly, "
          "so the road runs smoothly down into the junction below; fill the rest of that place with the same sunny green grass and a few grass tufts. "
          "Keep everything else exactly the same: the same hand-drawn cartoon picture-book style, colors, lighting and outlines. No rocks there, no people, no animals, no text.")


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    seeds = [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4]
    pick = json.load(open(os.path.join(HERE, '고르기_13.json'), encoding='utf-8'))['bg13']
    src = Image.open(os.path.join(HERE, 'raw', pick)).convert('RGB').resize((1536, 864), Image.LANCZOS)
    crop = src.crop(BOX); cw, ch = crop.size
    mask = Image.new('L', (cw, ch), 0); ImageDraw.Draw(mask).polygon([(x - BOX[0], y - BOX[1]) for x, y in ROCK], fill=255)
    mask = mask.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(6))   # 가장자리를 조금 넓혀 부드럽게
    from diffusers import Flux2KleinPipeline
    t0 = time.time(); pipe = Flux2KleinPipeline.from_pretrained(MODEL, torch_dtype=torch.bfloat16)
    pipe.enable_model_cpu_offload(); pipe.set_progress_bar_config(disable=True); print(f'모델 적재 {time.time()-t0:.0f}초', flush=True)
    od = os.path.join(HERE, '고침'); os.makedirs(od, exist_ok=True)
    w = h = 768
    for sd in seeds:
        t = time.time()
        out = pipe(prompt=PROMPT, image=crop.resize((w, h), Image.LANCZOS), height=h, width=w, guidance_scale=1.0, num_inference_steps=4,
                   generator=torch.Generator('cpu').manual_seed(sd)).images[0].resize((cw, ch), Image.LANCZOS)
        fixed = src.copy(); fixed.paste(Image.composite(out, crop, mask), BOX[:2])
        fixed.save(os.path.join(HERE, 'raw', f'bg13_fix2_s{sd}.png'))
        pv = Image.new('RGB', (cw * 2 + 8, ch), (40, 30, 20)); pv.paste(crop, (0, 0)); pv.paste(fixed.crop(BOX), (cw + 8, 0))
        pv.save(os.path.join(od, f'bg13_fix2_s{sd}_보기.jpg'), quality=88)
        print(f'bg13_fix2_s{sd}', f'{time.time()-t:.1f}초', flush=True)


if __name__ == '__main__':
    main()
