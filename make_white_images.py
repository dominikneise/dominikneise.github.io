# coding: utf-8
from glob import glob
from PIL import Image
from PIL import Image, ImageDraw

jpgs = sorted(glob("*.jpg"))
for p in jpgs:
    im = Image.open(p)
    img = Image.new("RGB", im.size, color=(255, 255, 255))
    d = ImageDraw.Draw(img)

    N = len(p)
    pos = 0
    q = p
    for i in range(N // 16):
        d.text((0, pos), q[:16], fill=(0, 0, 0))
        pos += 20
        q = q[16:]
    d.text((0, pos), q[:16], fill=(0, 0, 0))
    img.save(f'white_images/{p}')
