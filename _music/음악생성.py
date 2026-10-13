# Kingdom of God 배경 음악 생성 v0.1 (2026-10-13)
# 로컬 무료 생성: ACE-Step 1.5 turbo + 5Hz LM 1.7B(MIT, 상업 사용 가능). 음악 venv(%LOCALAPPDATA%\kog_music\ACE-Step-1.5\.venv)에서 돈다.
# 사용: python 음악생성.py 곡.json [id ...]      (id를 주면 그 곡만). 곡 하나 2분쯤(LM 1.5분 + DiT 0.5분, RTX 3060)
# 곡.json: {"공통": "...", "출력": "raw", "항목": [{"id": "title", "캡션": "...", "가사": "[Intro]...", "bpm": 76, "key": "D minor", "길이": 150, "시드": [1,2,3,4]}]}
#   캡션 끝에 "공통"을 붙인다. 가사가 "[Instrumental]"이면 노래 없이.
# 결과: 출력\<id>_s<시드>_<지문6>.flac + 같은 이름 .json. 이미 있으면 건너뛴다. 캡션·가사·박자를 고치면 지문이 바뀌어 새로 만든다.
# 그림생성.py(FLUX)·누끼와 동시에 돌리지 않는다(GPU 12GB).
import sys, os, json, time, hashlib, shutil, tempfile

ACE = os.path.join(os.environ['LOCALAPPDATA'], 'kog_music', 'ACE-Step-1.5')
sys.path.insert(0, ACE)
for k in ('http_proxy', 'https_proxy', 'HTTP_PROXY', 'HTTPS_PROXY', 'ALL_PROXY'):
    os.environ.pop(k, None)

SEEDS = [1, 2, 3]


def tag(it, common):
    key = '|'.join([it['캡션'], common, it.get('가사', ''), str(it.get('bpm')), it.get('key', ''), str(it.get('길이')), it.get('박자', '')])
    return hashlib.sha1(key.encode('utf-8')).hexdigest()[:6]


def main():
    job_path = os.path.abspath(sys.argv[1])
    only = set(sys.argv[2:])
    job = json.load(open(job_path, encoding='utf-8'))
    out = os.path.join(os.path.dirname(job_path), job.get('출력', 'raw'))
    os.makedirs(out, exist_ok=True)
    common = job.get('공통', '')

    todo = []   # (곡, 시드, 이름). 시드 차례로 돈다: 모든 곡의 첫 후보 → 둘째 후보 …(먼저 한 벌을 들어 볼 수 있게)
    items = [it for it in job['항목'] if not only or it['id'] in only]
    for k in range(max(len(it.get('시드', SEEDS)) for it in items)):
        for it in items:
            seeds = it.get('시드', SEEDS)
            if k < len(seeds):
                name = f"{it['id']}_s{seeds[k]}_{tag(it, common)}"
                if not os.path.exists(os.path.join(out, name + '.flac')):
                    todo.append((it, seeds[k], name))
    print(f'만들 곡 {len(todo)}개')
    if not todo:
        return

    from acestep.handler import AceStepHandler
    from acestep.llm_inference import LLMHandler
    from acestep.inference import GenerationParams, GenerationConfig, generate_music

    t0 = time.time()
    dit = AceStepHandler()
    msg, ok = dit.initialize_service(project_root=ACE, config_path='acestep-v15-turbo', device='cuda', offload_to_cpu=False)
    if not ok:
        sys.exit('DiT 실패: ' + msg)
    llm = LLMHandler()   # 윈도에는 Triton이 없어 vLLM 대신 PyTorch로
    msg, ok = llm.initialize(checkpoint_dir=os.path.join(ACE, 'checkpoints'), lm_model_path='acestep-5Hz-lm-1.7B', backend='pt', device='cuda', offload_to_cpu=False)
    if not ok:
        sys.exit('LM 실패: ' + msg)
    print(f'모델 준비 {time.time() - t0:.0f}초')

    def run(it, seeds):
        lyrics = it.get('가사', '[Instrumental]')
        cap = (it['캡션'] + ' ' + common).strip()
        if len(cap) > 512:
            print(f"  ! {it['id']} 캡션이 {len(cap)}자라 512자에서 잘려요")
        p = GenerationParams(
            task_type='text2music', caption=cap[:512], lyrics=lyrics,
            instrumental=lyrics.strip() == '[Instrumental]', vocal_language='en',
            bpm=it.get('bpm'), keyscale=it.get('key', ''), timesignature=it.get('박자', '4'), duration=float(it.get('길이', 150)),
            inference_steps=8, shift=3.0, seed=seeds[0], thinking=True,
            use_cot_metas=False, use_cot_caption=False, use_cot_language=False,
            fade_out_duration=float(it.get('페이드', 3.0)),
        )
        c = GenerationConfig(batch_size=1, use_random_seed=False, seeds=list(seeds), audio_format='flac')   # 한꺼번에 하면 LM은 어차피 하나씩 돌고, VRAM이 모자라 하나만 남는다
        return generate_music(dit, llm, params=p, config=c, save_dir=tmp)

    tmp = tempfile.mkdtemp(prefix='kogmus_')
    for i, (it, s, name) in enumerate(todo, 1):
        t1 = time.time()
        r = run(it, [s])
        if not r.success or not r.audios:
            print(f'[{i}/{len(todo)}] {name} 실패: {r.error or r.status_message}', flush=True)
            continue
        shutil.move(r.audios[0]['path'], os.path.join(out, name + '.flac'))
        meta = {k: it.get(k) for k in ('id', '이름', '결', '캡션', '가사', 'bpm', 'key', '길이')}
        meta.update(시드=s, 공통=common, 초=round(time.time() - t1, 1))
        json.dump(meta, open(os.path.join(out, name + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'[{i}/{len(todo)}] {name} {time.time() - t1:.0f}초', flush=True)
    shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    main()
