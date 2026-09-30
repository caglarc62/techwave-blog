# -*- coding: utf-8 -*-
"""X icin profil resmi uretir: images/x-profile.png (800x800, 2x supersample)."""
import math
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

S = 2                      # supersample katsayisi
W = H = 800 * S
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images", "x-profile.png")


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def pick_font(names, size):
    for n in names:
        try:
            return ImageFont.truetype(n, size * S)
        except Exception:
            continue
    return ImageFont.load_default()


# --- Arka plan: capraz ocean gradienti ---
c1 = (13, 148, 136)
c2 = (8, 145, 178)
c3 = (37, 99, 235)
bg = Image.new("RGB", (W, H))
px = bg.load()
for y in range(H):
    for x in range(W):
        t = (x + y) / (W + H)
        col = lerp(c1, c2, t * 2) if t < 0.5 else lerp(c2, c3, (t - 0.5) * 2)
        px[x, y] = col

draw = ImageDraw.Draw(bg, "RGBA")

# --- Koyu dairesel overlay (okunurluk icin) ---
draw.ellipse([80 * S, 80 * S, W - 80 * S, H - 80 * S], fill=(7, 20, 28, 165))

# --- Dalga cizgileri (yumusak) ---
for i, (wd, alpha) in enumerate([(18, 150), (14, 115), (10, 85)]):
    pts = []
    yb = 555 * S + i * 34 * S
    for x in range(140 * S, W - 140 * S, 3):
        y = yb + 26 * S * math.sin((x - 140 * S) / (55.0 * S) + i * 1.2)
        pts.append((x, y))
    draw.line(pts, fill=(34, 211, 238, alpha), width=wd, joint="curve")

# --- TW monogrami ---
font = pick_font(
    ["arialbd.ttf", "segoeuib.ttf", "C:/Windows/Fonts/arialbd.ttf",
     "C:/Windows/Fonts/segoeuib.ttf", "C:/Windows/Fonts/arial.ttf"],
    300,
)
text = "TW"
box = draw.textbbox((0, 0), text, font=font)
tw, th = box[2] - box[0], box[3] - box[1]
x0 = (W - tw) / 2 - box[0]
y0 = (H - th) / 2 - box[1] - 40 * S

for off in range(12, 0, -1):
    draw.text((x0, y0 + off), text, font=font, fill=(0, 0, 0, 60))
draw.text((x0, y0), text, font=font, fill=(6, 182, 212, 255))
draw.text((x0, y0), text, font=font, fill=(240, 253, 250, 120))

# --- altinda TechWave yazisi ---
small = pick_font(["arialbd.ttf", "C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arial.ttf"], 64)
label = "TECHWAVE"
lb = draw.textbbox((0, 0), label, font=small)
lw = lb[2] - lb[0]
draw.text(((W - lw) / 2 - lb[0], 620 * S), label, font=small, fill=(226, 232, 240, 235))

# --- Yaricap kenar maskesi + indirgeme (yumusak kenar) ---
mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).ellipse([0, 0, W, H], fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(3))

final = bg.convert("RGBA")
final.putalpha(mask)
final = final.resize((800, 800), Image.LANCZOS)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
final.save(OUT, "PNG")
print("Yazildi:", OUT, final.size)
