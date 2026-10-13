# 고른 곡을 게임 폴더(music\)로 모은다 v0.1 (2026-10-13). ffmpeg만 있으면 어느 파이썬에서도 돈다.
# 사용: python 모으기.py [고르기.json]
# 고르기.json: {"title": "title_s2_ab12cd.flac", ...} — 값은 raw\ 안의 파일 이름
# 앞뒤 무음을 걷어 내고, 소리 크기를 곡끼리 맞춘 뒤(EBU R128 두 번 재기, 선형이라 웅장·잔잔의 차이는 그대로) AAC 96k .m4a로 music\<id>.m4a.
#   잔잔한 곡은 조금 작게(LUFS 표). 게임은 BGM_VOL로 효과음 밑에 깐다.
import sys, os, json, re, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
RAW, OUT = os.path.join(HERE, 'raw'), os.path.join(HERE, '..', 'music')
LUFS = {'map': -19, 'story': -20, 'defeat': -20, 's5': -18.5, 's9': -18.5}   # 그 밖은 -17
FF = 'ffmpeg'


def measure(src, pre):
    r = subprocess.run([FF, '-hide_banner', '-nostats', '-i', src, '-af', pre + ',loudnorm=print_format=json', '-f', 'null', '-'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    m = re.findall(r'\{[^{}]*"input_i"[^{}]*\}', r.stderr)
    if not m:
        raise RuntimeError(r.stderr[-400:])
    return json.loads(m[-1])


def main():
    picks = json.load(open(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '고르기.json'), encoding='utf-8'))
    os.makedirs(OUT, exist_ok=True)
    for tid, name in picks.items():
        src = os.path.join(RAW, name)
        dst = os.path.join(OUT, tid + '.m4a')
        pre = ('silenceremove=start_periods=1:start_threshold=-55dB,'   # 앞의 무음, 끝의 무음(0.8초만 남김. 반복할 때 틈이 안 생기게)
               'areverse,silenceremove=start_periods=1:start_threshold=-48dB:start_silence=0.8,areverse')
        target = LUFS.get(tid, -17)
        m = measure(src, pre)
        ln = (f"loudnorm=I={target}:TP=-1.5:LRA=20:linear=true:measured_I={m['input_i']}:measured_TP={m['input_tp']}"
              f":measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}")
        r = subprocess.run([FF, '-y', '-hide_banner', '-loglevel', 'error', '-i', src, '-af', pre + ',' + ln,
                            '-ar', '44100', '-ac', '2', '-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart', dst],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        if r.returncode:
            print(tid, '실패', r.stderr[-300:])
            continue
        print(f"{tid:8s} {name}  {float(m['input_i']):.1f} → {target} LUFS  {os.path.getsize(dst) / 1e6:.1f} MB")


if __name__ == '__main__':
    main()
