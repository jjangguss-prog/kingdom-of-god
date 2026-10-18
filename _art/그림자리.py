# 사용: python 그림자리.py 그림자리/face1.json 그림자리/face2.json …
# 그림마다 얼굴이 잘리거나 글 상자에 가리지 않게 위아래 자리(s, 그림 높이 비율, +는 위로)와 크기(k, 1보다 작으면 줄여서 뒤에 흐린 그림)를 고른다
import json,os,sys
T=os.path.join(os.path.dirname(os.path.abspath(__file__)),'그림자리')   # frame_meas.json(글 상자·제목 띠 높이, 브라우저에서 잰 값), face*.json(그림마다 중요한 얼굴의 위아래 끝 %), 결과 frame_out.json → index.html의 ART_FRAME
M=json.load(open(os.path.join(T,'frame_meas.json'),encoding='utf-8'))
F={}
for fn in sys.argv[1:]:
    for it in json.load(open(fn,encoding='utf-8')):F[it['key']]=it
H=720.0;MG=0.02
def solve(a,b,vis,zs,off,s0,kmin=.84):
    """vis: 보이는 화면 아래 끝(px), zs: 확대 범위, off: 그림을 늘 위로 올리는 px(이야기 70, 만화 0)"""
    zmax=max(zs);k=min(1.0,vis/((b-a+2*MG)*H*zmax));k=max(kmin,k)
    def top(z,s): h=H*z*k;return .5-H/(2*h)+off/h+s
    def bot(z,s): h=H*z*k;return vis/h+.5-H/(2*h)+off/h+s
    s_hi=min(a-MG-top(z,0) for z in zs);s_lo=max(b+MG-bot(z,0) for z in zs)
    nogap=-min(.5-H/(2*H*z*k)+off/(H*z*k) for z in zs) if k>=1 else -9   # 이보다 아래로 내리면 위에 빈 띠
    A,B=max(s_lo,nogap),s_hi
    if A<=B+1e-9: s=min(max(s0,A),B);ok=True
    else: s=max(nogap,s_lo) if s_lo<=s_hi or nogap>s_hi else s_hi;ok=s_lo<=s_hi   # 맨 위 끝에 닿은 것은 그림 끝까지만 보인다
    return round(s,3),round(k,3),ok
out={};bad=[];rows=[]
for kk,c,s0 in M['story']:
    f=F.get(kk)
    if not f: continue
    s,k,ok=solve(f['top']/100,f['bottom']/100,c-8,(1.0,1.04),70,s0)
    out[kk]=[s,k] if k<1 else s
    rows.append((kk,f['top'],f['bottom'],c,s0,s,k,ok))
for kk,B,z0,z1,px,py in M['comic']:
    f=F.get(kk)
    if not f: continue
    zs=(1+(z0-1)*.5,1+(z1-1)*.5)
    s,k,ok=solve(f['top']/100,f['bottom']/100,B-6,zs,0,0)
    out[kk]=[s,k] if k<1 else s
    rows.append((kk,f['top'],f['bottom'],B,0,s,k,ok))
for r in rows:
    if r[6]<1 or not r[7] or abs(r[4]-r[5])>.03: print(r)
print('scaled',sum(1 for r in rows if r[6]<1),'not ok',[r[0] for r in rows if not r[7]],'nonzero',sum(1 for r in rows if abs(r[5])>1e-9 or r[6]<1))
json.dump(out,open(os.path.join(T,'frame_out.json'),'w'))
