# Kingdom of God 게임 그림 생성 v0.1 (2026-10-11)
# 로컬 무료 생성: FLUX.2 [klein] 4B(Apache 2.0, 상업 사용 가능). 생성 venv(%LOCALAPPDATA%\buiknam_gen)에서 돈다.
# 사용: python 그림생성.py 작업.json
# 작업.json: {"출력": "raw", "크기": [1024, 1024], "항목": [{"id": "noah", "종류": "인물", "프롬프트": "...", "시드": [1, 2]}]}
#   종류: 인물(캐릭터) · 건물(탑) · 정령(마귀 등 떠 있는 것) · 장면(배경·이야기 그림, 흰 배경을 붙이지 않는다)
#   "참조": ["ref/bg1.png"]를 주면 그 그림의 배치를 이어받아 다시 그린다(멀티 레퍼런스 편집). 경로는 작업.json 기준.
# 결과: 출력\<id>_s<시드>_<지문6>.png + 같은 이름 .json. 이미 있으면 건너뛴다. 프롬프트를 고치면 지문이 바뀌어 새로 그린다.
# 누끼(BiRefNet)와 동시에 돌리지 않는다(GPU 12GB). 생성이 끝난 뒤 누끼.py를 돌린다.
import sys, os, json, time, hashlib
os.environ.setdefault('HF_HOME', os.path.join(os.path.expanduser('~'), '.cache', 'huggingface'))
import torch
from PIL import Image

MODEL = 'black-forest-labs/FLUX.2-klein-4B'
LOOK = ('in the style of the Kingdom Rush tower defense games by Ironhide Game Studio: polished hand-painted 2D cartoon, '
        'bold clean dark-brown outlines, soft cel shading with gentle painted gradients and rim light, warm rich colors, '
        'ancient Near East Bronze Age setting. ')
STYLE = {
    '인물': ('A single 2D game character sprite ' + LOOK +
            'Chunky cute proportions with a large head about one third of the body height, friendly expressive face, '
            'full body visible from head to feet, three-quarter view facing right, camera slightly above. '
            'Isolated on a plain pure white background, no ground, no cast shadow, no text.'),
    '건물': ('A single 2D tower defense building sprite ' + LOOK +
            'Three-quarter top-down view, the whole structure visible, standing on a small round patch of earth. '
            'Isolated on a plain pure white background, no text.'),
    '정령': ('A single 2D game creature sprite ' + LOOK +
            'Full body visible, floating, three-quarter view facing right. '
            'Isolated on a plain pure white background, no text.'),
    '장면': LOOK + 'No text, no lettering.',
}

def tag(it):
    return hashlib.sha1((it['프롬프트'] + it.get('종류', '인물') + '|'.join(it.get('참조', []))).encode('utf-8')).hexdigest()[:6]

def load():
    from diffusers import Flux2KleinPipeline
    pipe = Flux2KleinPipeline.from_pretrained(MODEL, torch_dtype=torch.bfloat16)
    pipe.enable_model_cpu_offload()
    pipe.set_progress_bar_config(disable=True)
    return pipe

def main():
    sys.stdout.reconfigure(encoding='utf-8')
    jp = os.path.abspath(sys.argv[1]); job = json.load(open(jp, encoding='utf-8'))
    od = os.path.join(os.path.dirname(jp), job.get('출력', 'raw')); os.makedirs(od, exist_ok=True)
    W, H = job.get('크기', [1024, 1024])
    todo = []
    for it in job['항목']:
        for sd in it.get('시드', [1]):
            name = f"{it['id']}_s{sd}_{tag(it)}"
            if os.path.exists(os.path.join(od, name + '.png')):
                print('있음', name); continue
            todo.append((it, sd, name))
    if not todo:
        return
    t0 = time.time(); pipe = load(); print(f'모델 적재 {time.time()-t0:.0f}초', flush=True)
    for it, sd, name in todo:
        t = time.time()
        w, h = it.get('크기', [W, H])
        prompt = it['프롬프트'].strip() + ' ' + STYLE[it.get('종류', '인물')]
        kw = dict(prompt=prompt, height=h, width=w, guidance_scale=1.0, num_inference_steps=job.get('단계', 4),
                  generator=torch.Generator('cpu').manual_seed(int(sd)))
        refs = [Image.open(os.path.join(os.path.dirname(jp), r)).convert('RGB') for r in it.get('참조', [])]
        if refs:
            kw['image'] = refs if len(refs) > 1 else refs[0]
        im = pipe(**kw).images[0]
        im.save(os.path.join(od, name + '.png'))
        json.dump(dict(it, 시드=sd, 전체프롬프트=prompt, 모델=MODEL, 초=round(time.time() - t, 1)),
                  open(os.path.join(od, name + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(name, f'{time.time()-t:.1f}초', flush=True)

if __name__ == '__main__':
    main()
