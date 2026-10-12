# v1a(방주로 들어가는 짐승들) 문 안의 두 번째 노인 지우기 v0.1 (2026-10-12, 사용자 요청)
# 원래 "노아와 그의 아내"로 그리게 했는데 아내가 노아와 똑같은 흰 수염 노인으로 그려져서, 뒤쪽 노인을 문 안쪽 어둠으로 덮어 노아만 남긴다.
# GPU 없이 손으로 덮는다(그때 GPU를 다른 작업들이 쓰고 있었음). 좌표는 1280×720 그림 기준.
# 사용: python 방주문고침.py raw/v1a_comp3.png raw/v1a_comp4.png
import sys
from PIL import Image, ImageDraw

im = Image.open(sys.argv[1]).convert('RGB')
px = im.load()
dark = px[900, 240]                      # 문 안쪽 어둠
d = ImageDraw.Draw(im)
# 뒤쪽 노인: 앞의 노아 머리 위(머리·두건), 노아 머리 오른쪽(수염·어깨), 왼팔, 오른팔
for box in [(878, 248, 958, 289), (923, 286, 962, 326), (856, 284, 887, 331), (958, 292, 979, 334)]:
    d.rectangle(box, fill=dark)
# 노아 두건 오른쪽 위에 남은 뒤쪽 노인의 수염 조각: 노아 머리(타원) 밖이면 어둠으로
cx, cy, rx, ry = 905.5, 318, 17.5, 27.5
for x in range(900, 926):
    for y in range(282, 330):
        if ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 > 1:
            px[x, y] = dark
# 왼쪽 문틀에 얹힌 뒤쪽 노인의 손: 손 바로 위 문틀 줄을 아래로 이어 나뭇결을 메우고, 아래 끝은 원래 그림과 섞는다
for x in range(832, 857):
    c = px[x, 281]
    for y in range(282, 319):
        px[x, y] = c
    for i, y in enumerate(range(319, 325)):
        k = (i + 1) / 7; o = px[x, y]
        px[x, y] = tuple(round(c[j] * (1 - k) + o[j] * k) for j in range(3))
im.save(sys.argv[2])
