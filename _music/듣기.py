# 만든 곡 후보를 한 쪽에서 들어 보고 고르는 검토 페이지(듣기.html)를 만든다 v0.1 (2026-10-13). 음악 venv에서 돈다(numpy·soundfile).
# 사용: python 듣기.py [곡.json]
# 곡마다 후보(시드)를 나란히 놓고, 소리 크기 흐름(웅장/잔잔이 언제 오는지)을 작은 그래프로 그린다.
# 페이지에서 고르면 "고르기.json 저장"으로 내려받거나, 보이는 JSON을 복사해 _music\고르기.json에 붙인다.
import sys, os, json, glob, html
import numpy as np
import soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
job = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '곡.json'), encoding='utf-8'))
RAW = os.path.join(HERE, job.get('출력', 'raw'))
picked = {}
if os.path.exists(os.path.join(HERE, '고르기.json')):
    picked = json.load(open(os.path.join(HERE, '고르기.json'), encoding='utf-8'))


def envelope(path, n=120):
    """소리 크기 흐름(구간별 RMS, dB)과 길이·최고값."""
    x, sr = sf.read(path, always_2d=True)
    m = x.mean(axis=1)
    seg = max(1, len(m) // n)
    rms = [float(np.sqrt(np.mean(m[i * seg:(i + 1) * seg] ** 2)) + 1e-9) for i in range(n)]
    db = [max(-60.0, 20 * np.log10(r)) for r in rms]
    return db, len(m) / sr, float(np.abs(x).max())


def spark(db):
    w, h = 240, 40
    pts = ' '.join(f'{i * w / (len(db) - 1):.1f},{h - (d + 60) / 60 * h:.1f}' for i, d in enumerate(db))
    return f'<svg viewBox="0 0 {w} {h}" class="sp"><polyline points="{pts}" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>'


cards = []
for it in job['항목']:
    files = sorted(glob.glob(os.path.join(RAW, it['id'] + '_s*.flac')))
    if not files:
        continue
    rows = []
    for f in files:
        name = os.path.basename(f)
        db, dur, peak = envelope(f)
        loud = np.mean(sorted(db)[len(db) // 2:])
        warn = []
        tail = 0
        while tail < len(db) and db[-1 - tail] < -45:
            tail += 1
        quiet = sum(1 for d in db[:len(db) - tail] if d < -45)
        if quiet > len(db) * .1:
            warn.append('중간에 조용한 데가 길어요')
        note = ''
        if tail * dur / len(db) > 2:
            note = f' · 끝 무음 {tail * dur / len(db):.0f}초(모을 때 잘라 냄)'
        if peak >= .999:
            warn.append('찌그러질 수 있어요')
        meta = os.path.splitext(f)[0] + '.json'
        seed = json.load(open(meta, encoding='utf-8')).get('시드') if os.path.exists(meta) else '?'
        chk = 'checked' if picked.get(it['id']) == name else ''
        rows.append(f'''<label class="cand"><input type="radio" name="{it['id']}" value="{name}" {chk}>
<span class="sd">시드 {seed}</span><audio controls preload="none" src="raw/{html.escape(name)}"></audio>
{spark(db)}<span class="mt">{int(dur // 60)}:{int(dur % 60):02d} · 큰 대목 {loud:.0f} dB{note}{' · ⚠ ' + ', '.join(warn) if warn else ''}</span></label>''')
    cards.append(f'''<section><h2>{html.escape(it.get('이름', it['id']))} <small>{html.escape(it.get('결', ''))} · {it['id']}</small></h2>
<p class="cap">{html.escape(it['캡션'])}</p>{''.join(rows)}</section>''')

page = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>배경 음악 고르기</title><style>
:root{{--bg:#f6efe2;--ink:#3b2614;--mute:#7a6650;--card:#fffaf0;--line:#e3d5bd;--acc:#b5652b}}
@media (prefers-color-scheme:dark){{:root{{--bg:#1d1813;--ink:#f1e6d4;--mute:#b3a28c;--card:#2a231c;--line:#43372b;--acc:#e09a5c}}}}
body{{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 "Gowun Dodum",system-ui,sans-serif}}
main{{max-width:900px;margin:0 auto;padding:16px}}h1{{font-size:22px;margin:8px 0}}
section{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:14px 0}}
h2{{font-size:17px;margin:0 0 4px}}h2 small{{color:var(--mute);font-weight:400;font-size:13px}}
.cap{{color:var(--mute);font-size:12.5px;margin:0 0 8px}}
.cand{{display:grid;grid-template-columns:auto auto 1fr;gap:4px 10px;align-items:center;padding:8px 6px;border-top:1px solid var(--line);cursor:pointer}}
.cand:has(input:checked){{background:color-mix(in srgb,var(--acc) 14%,transparent);border-radius:8px}}
.sd{{font-size:13px;white-space:nowrap}}audio{{width:100%;min-width:0;height:36px}}
.sp{{grid-column:2/4;width:100%;height:34px;color:var(--acc)}}.mt{{grid-column:2/4;font-size:12px;color:var(--mute)}}
.bar{{position:sticky;bottom:0;background:var(--bg);border-top:1px solid var(--line);padding:10px 16px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}}
button{{font:inherit;background:var(--acc);color:#fff;border:0;border-radius:8px;padding:8px 14px;cursor:pointer}}
textarea{{flex:1;min-width:200px;height:38px;font:12px monospace;background:var(--card);color:var(--ink);border:1px solid var(--line);border-radius:6px}}
</style></head><body><main><h1>배경 음악 고르기</h1>
<p>곡마다 마음에 드는 후보 하나를 고르세요. 그래프는 소리 크기 흐름이에요(위로 갈수록 웅장). 한 곡을 틀면 다른 곡은 멈춰요.</p>
{''.join(cards)}</main>
<div class="bar"><button id="save">고르기.json 저장</button><textarea id="out" readonly></textarea></div>
<script>
const out=document.getElementById('out');
function pick(){{const o={{}};for(const r of document.querySelectorAll('input[type=radio]:checked'))o[r.name]=r.value;out.value=JSON.stringify(o);return o;}}
document.addEventListener('change',pick);pick();
document.addEventListener('play',e=>{{for(const a of document.querySelectorAll('audio'))if(a!==e.target)a.pause();}},true);
document.getElementById('save').onclick=()=>{{const b=new Blob([JSON.stringify(pick(),null,1)],{{type:'application/json'}}),a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='고르기.json';a.click();}};
</script></body></html>'''
open(os.path.join(HERE, '듣기.html'), 'w', encoding='utf-8').write(page)
print('듣기.html', len(cards), '곡')
