# 13 미스바 배경(bg13) 왼쪽 위 고치기 v0.2 (2026-10-18)
# v0.2: 길 가림을 색으로(길의 황토색 바탕 + 짙은 테두리만) 잡아 길가에 남던 옛 안개 띠를 없애고, 상자 전체를 다시 그려 오른쪽·아래 끝만 부드럽게 이어 붙인다(v0.1은 언덕 가운데 이음매가 보였다)
# 10-18 사용자: "좌상단 길 때문에 적들이 하늘에서 내려오는 것 같은 인상을 줘." 그림에서 왼쪽 위 길이 파란 하늘과 먼 안개 골짜기 위로 그려져 있었다.
# 길 둘레의 하늘·안개 자리만 FLUX.2 klein 참조 편집으로 초록 언덕으로 다시 그리고, 길(게임 길 0의 선을 두껍게 그린 가림)은 원본 그대로 둔다.
# 사용(생성 venv %LOCALAPPDATA%\buiknam_gen): python 배경고침13.py [시드 ...] → raw\bg13_fix_s<시드>.png(1536×864) + 고침\bg13_fix_s<시드>_보기.jpg
import sys, os, json, time
os.environ.setdefault('HF_HOME', os.path.join(os.path.expanduser('~'), '.cache', 'huggingface'))
import torch
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = 'black-forest-labs/FLUX.2-klein-4B'
G2B = 1536 / 1280   # 게임 좌표 → 배경 그림 좌표
ROAD = [(240, -60), (240, 30), (270, 110), (325, 190), (390, 265), (440, 335)]   # index.html STAGES[13].paths[0] 앞부분
BOX = (0, 0, 800, 560)   # 고칠 상자(배경 그림 좌표). 왼쪽 아래 안개 골짜기 끝(y 450쯤)보다 넉넉히 아래까지
SKY = [(0, 0), (768, 0), (768, 12), (560, 80), (420, 190), (330, 270), (230, 370), (170, 448), (0, 448)]   # 언덕 가장자리 위·왼쪽(하늘과 안개 골짜기)
PROMPT = ("Edit the picture. Replace the pale blue sky and the hazy distant valley with a continuation of the sunny green grassy hillside: "
          "rolling green grassy hills with many round leafy trees, small bushes and grass tufts fill the whole picture up to the top edge, and the green slope continues beyond the top edge, "
          "so the sandy road runs over green grass all the way out of the top of the picture. No sky anywhere, no clouds, no distant haze. "
          "Keep the sandy road exactly the same shape, width and color. Keep everything else exactly the same: the same hand-drawn cartoon "
          "picture-book style, colors, lighting and outlines. No people, no animals, no text.")

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    seeds = [int(a) for a in sys.argv[1:]] or [1, 2, 3, 4]
    pick = json.load(open(os.path.join(HERE, '고르기_13.json'), encoding='utf-8'))['bg13']
    src = Image.open(os.path.join(HERE, 'raw', pick)).convert('RGB').resize((1536, 864), Image.LANCZOS)
    crop = src.crop(BOX); cw, ch = crop.size
    region = Image.new('L', (cw, ch), 0); ImageDraw.Draw(region).polygon(SKY, fill=255)
    band = Image.new('L', (cw, ch), 0); ImageDraw.Draw(band).line([(x * G2B, y * G2B) for x, y in ROAD], fill=255, width=110, joint='curve')
    road = Image.new('L', (cw, ch), 0); px = crop.load(); bp = band.load(); rp = road.load()
    for yy in range(ch):
        for xx in range(cw):
            if not bp[xx, yy]: continue
            r, g, b = px[xx, yy]
            if (g - b > 30 and r > 200) or (r - b > 45 and r < 200) or r + g + b < 330: rp[xx, yy] = 255   # 길 바탕(황토) · 테두리(밤색·짙은 색)
    road = road.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.MaxFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
    edge = Image.new('L', (cw, ch), 255); ImageDraw.Draw(edge).rectangle((cw - 60, 0, cw, ch), fill=0); ImageDraw.Draw(edge).rectangle((0, ch - 60, cw, ch), fill=0)
    region = edge.filter(ImageFilter.GaussianBlur(22))   # 상자 전체, 오른쪽·아래 끝만 부드럽게
    mask = Image.composite(Image.new('L', (cw, ch), 0), region, road)   # 다시 그린 자리 − 길
    from diffusers import Flux2KleinPipeline
    t0 = time.time(); pipe = Flux2KleinPipeline.from_pretrained(MODEL, torch_dtype=torch.bfloat16)
    pipe.enable_model_cpu_offload(); pipe.set_progress_bar_config(disable=True); print(f'모델 적재 {time.time()-t0:.0f}초', flush=True)
    od = os.path.join(HERE, '고침'); os.makedirs(od, exist_ok=True)
    w, h = 1024, round(1024 * ch / cw / 16) * 16
    for sd in seeds:
        t = time.time()
        out = pipe(prompt=PROMPT, image=crop.resize((w, h), Image.LANCZOS), height=h, width=w, guidance_scale=1.0, num_inference_steps=4,
                   generator=torch.Generator('cpu').manual_seed(sd)).images[0].resize((cw, ch), Image.LANCZOS)
        fixed = src.copy(); fixed.paste(Image.composite(out, crop, mask), BOX[:2])
        fixed.save(os.path.join(HERE, 'raw', f'bg13_fix_s{sd}.png'))
        pv = Image.new('RGB', (cw * 2 + 8, ch), (40, 30, 20)); pv.paste(crop, (0, 0)); pv.paste(fixed.crop(BOX), (cw + 8, 0))
        pv.save(os.path.join(od, f'bg13_fix_s{sd}_보기.jpg'), quality=88)
        print(f'bg13_fix_s{sd}', f'{time.time()-t:.1f}초', flush=True)

if __name__ == '__main__':
    main()
