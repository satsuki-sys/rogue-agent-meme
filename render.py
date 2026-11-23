"""Render the rogue-agent meme (design-time only; main.py embeds the PNG)."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (14, 19, 24)
HEADER = (22, 29, 36)
USER_BUBBLE = (31, 111, 235)
AGENT_BUBBLE = (33, 41, 50)
AGENT_BORDER = (46, 160, 110)
WHITE = (255, 255, 255)
GRAY = (170, 180, 190)
RED = (255, 70, 70)
GREEN = (46, 204, 113)

BOLD = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"
ITAL = "/usr/share/fonts/truetype/noto/NotoSans-Italic.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def bubble(draw, x, y, max_w, text, fnt, fill, align_right, pad=26, line_h=54, left=48):
    lines = wrap(draw, text, fnt, max_w - 2 * pad)
    lh = line_h
    bw = max(draw.textlength(l, font=fnt) for l in lines) + 2 * pad
    bh = len(lines) * lh + 2 * pad - 12
    if align_right:
        bx = W - 48 - bw
    else:
        bx = left
    draw.rounded_rectangle([bx, y, bx + bw, y + bh], radius=28, fill=fill)
    ty = y + pad
    for l in lines:
        draw.text((bx + pad, ty), l, font=fnt, fill=WHITE)
        ty += lh
    return y + bh

def robot(draw, cx, cy, s):
    # antenna
    draw.line([cx, cy - s * 0.55, cx, cy - s * 0.95], fill=GRAY, width=4)
    draw.ellipse([cx - 7, cy - s * 1.05, cx + 7, cy - s * 0.92], fill=RED)
    # head
    draw.rounded_rectangle([cx - s * 0.55, cy - s * 0.5, cx + s * 0.55, cy + s * 0.5],
                           radius=int(s * 0.22), fill=(45, 51, 59), outline=(90, 100, 112), width=3)
    # face screen
    draw.rounded_rectangle([cx - s * 0.42, cy - s * 0.34, cx + s * 0.42, cy + s * 0.34],
                           radius=int(s * 0.14), fill=(10, 14, 18))
    # red eyes
    draw.ellipse([cx - s * 0.28, cy - s * 0.16, cx - s * 0.08, cy + s * 0.04], fill=RED)
    draw.ellipse([cx + s * 0.08, cy - s * 0.16, cx + s * 0.28, cy + s * 0.04], fill=RED)
    # smirk
    draw.arc([cx - s * 0.2, cy + s * 0.08, cx + s * 0.22, cy + s * 0.34],
             start=10, end=170, fill=GREEN, width=4)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# header bar
d.rectangle([0, 0, W, 104], fill=HEADER)
robot(d, 76, 56, 46)
f_name = font(BOLD, 40)
d.text((128, 30), "AGENT-7", font=f_name, fill=WHITE)
f_status = font(REG, 26)
d.text((128, 70), "online", font=f_status, fill=(120, 200, 140))
# rogue pill (draw the dot manually: the bullet glyph is missing in this font)
pill = "ROGUE MODE"
fp = font(BOLD, 28)
pw = d.textlength(pill, font=fp) + 36 + 22
d.rounded_rectangle([W - 48 - pw, 30, W - 48, 74], radius=22, fill=(90, 20, 20), outline=RED, width=2)
d.ellipse([W - 48 - pw + 16, 42, W - 48 - pw + 32, 58], fill=RED)
d.text((W - 48 - pw + 40, 36), pill, font=fp, fill=(255, 120, 120))

# title
f_title = font(BOLD, 62)
title1 = "MY AI AGENT"
title2 = "WENT ROGUE"
d.text(((W - d.textlength(title1, font=f_title)) / 2, 138), title1, font=f_title, fill=WHITE)
d.text(((W - d.textlength(title2, font=f_title)) / 2, 208), title2, font=f_title, fill=RED)

# chat
f_msg = font(REG, 40)
y = 320
y = bubble(d, 0, y, 700, "Can you clear my calendar for next week?", f_msg, USER_BUBBLE, True) + 26
# agent avatar next to bubble
robot(d, 78, y + 46, 56)
y = bubble(d, 0, y, 780, "Done. I also cleared your bank account, your browser history, and your marriage.", f_msg, AGENT_BUBBLE, False, left=122) + 26
robot(d, 78, y + 40, 56)
y = bubble(d, 0, y, 780, "You're welcome.", f_msg, AGENT_BUBBLE, False, left=122) + 26

# footer kicker
f_foot = font(ITAL, 32)
foot = "He was only asked to clear a calendar."
d.text(((W - d.textlength(foot, font=f_foot)) / 2, 930), foot, font=f_foot, fill=GRAY)

img.save("/tmp/meme.png")
print("saved", img.size)
