# 여러 그림을 한 장으로 모아 본다(검토용). 사용: python 모아보기.py 출력.png 칸크기 그림... (투명 그림은 체크무늬 위에)
import sys
from PIL import Image, ImageDraw
out, cell = sys.argv[1], int(sys.argv[2]); files = sys.argv[3:]
cols = min(4, len(files)); rows = (len(files) + cols - 1) // cols
sheet = Image.new('RGB', (cols * cell, rows * (cell + 18)), (60, 60, 60))
d = ImageDraw.Draw(sheet)
for i, f in enumerate(files):
    im = Image.open(f).convert('RGBA'); im.thumbnail((cell, cell))
    x, y = (i % cols) * cell, (i // cols) * (cell + 18)
    bg = Image.new('RGBA', (cell, cell), (200, 190, 170, 255))
    cd = ImageDraw.Draw(bg)
    for yy in range(0, cell, 16):
        for xx in range(0, cell, 16):
            if (xx // 16 + yy // 16) % 2: cd.rectangle([xx, yy, xx + 15, yy + 15], fill=(185, 175, 155, 255))
    bg.alpha_composite(im, ((cell - im.width) // 2, (cell - im.height) // 2))
    sheet.paste(bg.convert('RGB'), (x, y))
    d.text((x + 4, y + cell + 2), f.replace('\\', '/').split('/')[-1][:40], fill=(240, 240, 240))
sheet.save(out)
