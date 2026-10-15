# 음악 후보 '도파민' 점수 v0.1 (2026-10-16). librosa가 있는 venv(%LOCALAPPDATA%\banjeon_sound\venv)에서 돈다.
# 사용: python 점수.py s15 boss5 ...   (raw\<id>_s*.flac 후보끼리 비교)
# 10-16 사용자: 음악은 도파민을 극대화하는가로 우수함을 판단해 고른다. 신나는 곡의 특징을 재어 후보끼리 견준다(같은 곡의 후보 사이 z점수 합).
#   빠르기(bpm) · 박의 또렷함(onset 자기상관 봉우리) · 박의 촘촘함(초당 onset) · 타악 비중(HPSS) · 밝기(스펙트럼 중심)
#   쌓였다 터짐(6초 사이 크기가 가장 많이 오른 폭) · 첫 박(곡 크기의 중간값에 처음 닿는 시각, 짧을수록 좋음) · 되풀이(후렴·리프가 다시 나오는 정도)
# 결과: 표와 함께 점수.json(곡마다 후보별 점수와 1등)을 남긴다. 고를 때는 점수 1등을 들어 보고 확정한다.
import sys, os, glob, json
import numpy as np
import librosa

HERE = os.path.dirname(os.path.abspath(__file__))
W = {'bpm': .10, 'pulse': .18, 'dense': .14, 'perc': .14, 'bright': .08, 'build': .14, 'early': .10, 'repeat': .12}


def feats(path):
    y, sr = librosa.load(path, sr=22050, mono=True)
    hop = 512
    onset = librosa.onset.onset_strength(y=y, sr=sr, hop_length=hop)
    tempo = float(np.atleast_1d(librosa.feature.tempo(onset_envelope=onset, sr=sr, hop_length=hop))[0])
    ac = librosa.autocorrelate(onset - onset.mean(), max_size=int(sr / hop * 2))
    ac = ac / (ac[0] + 1e-9)
    lo = int(sr / hop * .25)
    pulse = float(ac[lo:].max())
    ons = librosa.onset.onset_detect(onset_envelope=onset, sr=sr, hop_length=hop)
    dense = len(ons) / (len(y) / sr)
    H, Pc = librosa.effects.hpss(y)
    perc = float(np.sum(Pc ** 2) / (np.sum(y ** 2) + 1e-9))
    bright = float(librosa.feature.spectral_centroid(y=y, sr=sr, hop_length=hop).mean())
    rms = librosa.feature.rms(y=y, frame_length=2048, hop_length=hop)[0]
    db = librosa.amplitude_to_db(rms + 1e-9)
    fps = sr / hop
    n2 = int(fps * 2); sm = np.convolve(np.pad(db, (n2 // 2, n2 - n2 // 2 - 1), mode='edge'), np.ones(n2) / n2, mode='valid')   # 2초로 고르게(가장자리는 끝값으로 메움)
    k, st = int(fps * 6), int(fps * 8)   # 쌓였다 터짐은 첫 8초(들머리)를 빼고 곡 가운데서 잰다
    build = float(max(sm[i + k] - sm[i] for i in range(st, len(sm) - k, int(fps / 2)))) if len(sm) > st + k else 0.
    build = min(build, 18.)   # 곡 가운데의 긴 무음 뒤 터짐은 18dB까지만 친다(무음을 상으로 주지 않게)
    med = np.median(sm)
    early = float(np.argmax(sm >= med) / fps)
    ch = librosa.feature.chroma_cqt(y=H, sr=sr, hop_length=hop)
    _, beats = librosa.beat.beat_track(onset_envelope=onset, sr=sr, hop_length=hop)
    cs = librosa.util.sync(ch, beats, aggregate=np.median) if len(beats) > 8 else ch
    R = librosa.segment.recurrence_matrix(cs, mode='affinity', sym=True)
    repeat = float(R.mean())
    return {'bpm': tempo, 'pulse': pulse, 'dense': dense, 'perc': perc, 'bright': bright, 'build': build, 'early': -early, 'repeat': repeat, '_early_s': early, '_len': len(y) / sr}


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    out = {}
    for tid in sys.argv[1:]:
        fs = sorted(glob.glob(os.path.join(HERE, 'raw', f'{tid}_s*.flac')))
        if not fs:
            print(tid, '후보 없음'); continue
        rows = [(os.path.basename(f), feats(f)) for f in fs]
        z = {n: 0. for n, _ in rows}
        for key, w in W.items():
            v = np.array([r[key] for _, r in rows]); sd = v.std() or 1
            for (n, _), x in zip(rows, v):
                z[n] += w * (x - v.mean()) / sd
        print(f'\n[{tid}] 후보 {len(rows)}')
        print('후보'.ljust(26), 'bpm  또렷  촘촘  타악  밝기  터짐  첫박  되풀이  점수')
        for n, r in sorted(rows, key=lambda t: -z[t[0]]):
            print(n.ljust(26), f"{r['bpm']:4.0f} {r['pulse']:5.2f} {r['dense']:5.2f} {r['perc']:5.2f} {r['bright']:5.0f} {r['build']:5.1f} {r['_early_s']:5.1f} {r['repeat']:6.3f} {z[n]:+6.2f}")
        best = max(z, key=z.get)
        out[tid] = {'1등': best, '점수': {n: round(z[n], 3) for n in z}, '값': {n: {k: round(v, 3) for k, v in r.items()} for n, r in rows}}
    p = os.path.join(HERE, '점수.json')
    old = json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}
    old.update(out)
    json.dump(old, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
