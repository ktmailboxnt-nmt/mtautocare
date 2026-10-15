"""Draw assets/og.jpg — the preview image shown when the site link is shared (Zalo, Facebook)."""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
W, H = 1200, 630
INK, PAPER, AMBER, MUTE = (14, 14, 13), (247, 246, 243), (242, 165, 22), (150, 148, 140)
F = '/usr/share/fonts/opentype/inter/'
display = lambda s: ImageFont.truetype(F + 'InterDisplay-Medium.otf', s)
text = lambda s: ImageFont.truetype(F + 'Inter-Medium.otf', s)

img = Image.new('RGB', (W, H), INK)
# soft amber glow behind the logo
glow = Image.new('L', (W, H), 0)
ImageDraw.Draw(glow).ellipse((700, -120, 1380, 560), fill=110)
glow = glow.filter(ImageFilter.GaussianBlur(140))
img.paste(Image.new('RGB', (W, H), (70, 46, 8)), (0, 0), glow)

d = ImageDraw.Draw(img)
# fine grid, like the map block on the site
for x in range(0, W, 48):
    d.line([(x, 0), (x, H)], fill=(24, 24, 22))
for y in range(0, H, 48):
    d.line([(0, y), (W, y)], fill=(24, 24, 22))

logo = Image.open(os.path.join(ROOT, 'assets/logo.png')).convert('RGBA')
lh = 205
logo = logo.resize((int(logo.width * lh / logo.height), lh), Image.LANCZOS)
img.paste(logo, (W - logo.width - 80, 100), logo)

x = 72
d.ellipse((x, 92, x + 10, 102), fill=AMBER)
d.text((x + 22, 85), 'MT AUTO — NÂNG NIU XẾ YÊU', font=text(20), fill=MUTE)
f = display(92)
d.text((x - 4, 150), 'Chăm chút', font=f, fill=PAPER)
w1 = d.textlength('từng ', font=f)
d.text((x - 4, 255), 'từng ', font=f, fill=PAPER)
d.text((x - 4 + w1, 255), 'chi tiết.', font=f, fill=AMBER)
d.text((x, 395), 'Độ đèn · Màn hình · Phanh – mâm · Chăm sóc', font=text(30), fill=PAPER)

d.line([(x, 500), (W - 72, 500)], fill=(60, 60, 56), width=1)
small = text(24)
d.text((x, 528), '71A Tôn Thất Tùng, Pleiku, Gia Lai', font=small, fill=MUTE)
phone = 'Hotline 0823 418 418'
d.text((W - 72 - d.textlength(phone, font=small), 528), phone, font=small, fill=PAPER)
d.rectangle((0, H - 8, W, H), fill=AMBER)

img.save(os.path.join(ROOT, 'assets/og.jpg'), quality=88, optimize=True, progressive=True)
print('assets/og.jpg', img.size)
