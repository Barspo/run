#!/usr/bin/env python3
"""Draws a 10 second cartoon: three friends dancing sirtaki at a Greek island
wedding. Everything is generated procedurally - the scenery, the dancers and
the bouzouki soundtrack - then encoded to an MP4 with ffmpeg.

    python3 make_video.py [-o out.mp4]

Like a real sirtaki the tempo accelerates, and the dancers speed up with it.
"""

import argparse
import math
import os
import random
import struct
import subprocess
import sys
import tempfile
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------- settings --

W, H = 1280, 720          # output resolution
SS = 2                    # supersampling factor for the drawing canvas
FPS = 25
DUR = 10.0                # seconds
NFRAMES = int(round(DUR * FPS))

BPM0, BPM1 = 96.0, 186.0  # sirtaki accelerando
BEATS_PER_STEP = 4.0      # one full dance figure per 4 beats

HORIZON = 352.0           # y of the sea horizon
FLOOR_Y = 432.0           # y where the dance floor starts
GROUND = 650.0            # y the dancers' feet stand on
OPA_T = 7.55              # when the "opa!" hits

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# ------------------------------------------------------------------ colors --

SKY_TOP = (11, 17, 44)
SKY_HORIZON = (86, 58, 74)
SEA = (18, 26, 58)
WALL = (236, 229, 214)
WALL_SHADE = (198, 186, 172)
DOME = (46, 96, 164)
WARM = (255, 196, 108)
FLOOR_BACK = (52, 41, 38)
FLOOR_FRONT = (36, 28, 27)
FLOOR_LIT = (126, 97, 74)
LEAF = (26, 48, 38)
BOUGAIN = (198, 62, 106)

CONFETTI_COLORS = [(255, 247, 226), (243, 201, 112), (236, 172, 178),
                   (152, 202, 236), (214, 236, 200)]

# --------------------------------------------------------------- the cast ---
# Cartoon stand-ins, matched to what everyone is wearing in the photos.

CAST = [
    dict(  # cream camp-collar shirt, black trousers, whisky in hand
        key="glassguy", dx=-186.0, scale=1.00, flip=1,
        skin=(226, 178, 140), skin_dark=(196, 148, 112),
        hair=(38, 27, 23), beard=True, curly=False,
        top=(240, 232, 213), top_shade=(214, 203, 182),
        collar="camp", sleeves="long",
        legwear="trousers", pants=(30, 30, 36), shoe="dress",
        free="left", prop="glass",
    ),
    dict(  # black maxi dress with a slit, long wavy hair, silver sandals
        key="dress", dx=0.0, scale=0.94, flip=1,
        skin=(232, 190, 156), skin_dark=(204, 160, 128),
        hair=(46, 30, 26), beard=False, curly=False, longhair=True,
        top=(26, 26, 32), top_shade=(14, 14, 18),
        collar="square", sleeves="none",
        legwear="dress", pants=(26, 26, 32), shoe="heel",
        kick_l_scale=0.22, kick_r_scale=1.0,
        free=None, prop=None,
    ),
    dict(  # pale beige button-down, black pants, black sneakers
        key="beigeguy", dx=186.0, scale=0.98, flip=1,
        skin=(224, 176, 138), skin_dark=(194, 146, 110),
        hair=(42, 28, 22), beard=True, curly=True,
        top=(233, 222, 186), top_shade=(206, 193, 158),
        collar="button", sleeves="rolled",
        legwear="trousers", pants=(28, 28, 33), shoe="sneaker",
        free="right", prop="napkin",
    ),
]

# ------------------------------------------------------------------- time ---


def beats_at(t):
    """Beat position at time t, under a linear tempo ramp."""
    return (BPM0 * t + (BPM1 - BPM0) * t * t / (2.0 * DUR)) / 60.0


def time_at(beat):
    """Inverse of beats_at."""
    k = (BPM1 - BPM0) / DUR
    if abs(k) < 1e-9:
        return 60.0 * beat / BPM0
    return (-BPM0 + math.sqrt(BPM0 * BPM0 + 120.0 * k * beat)) / k


TOTAL_BEATS = beats_at(DUR)


def bump(x):
    """Smooth 0..1..0 hump for x in [0, 1], zero outside."""
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return math.sin(math.pi * x) ** 2


def ease_out_back(x):
    c1, c3 = 1.70158, 2.70158
    return 1.0 + c3 * (x - 1.0) ** 3 + c1 * (x - 1.0) ** 2


def lerp(a, b, x):
    return a + (b - a) * x


def mix(c1, c2, x):
    return tuple(int(round(lerp(a, b, x))) for a, b in zip(c1, c2))


def shade(c, f):
    return tuple(max(0, min(255, int(round(v * f)))) for v in c)


# ------------------------------------------------------------------- pen ----


class Pen:
    """ImageDraw wrapper that takes 1x coordinates and draws at SS scale."""

    def __init__(self, draw, s=SS):
        self.d = draw
        self.s = s

    def _b(self, box):
        s = self.s
        return [box[0] * s, box[1] * s, box[2] * s, box[3] * s]

    def _p(self, pts):
        s = self.s
        return [(x * s, y * s) for x, y in pts]

    def line(self, pts, fill, width=1.0):
        self.d.line(self._p(pts), fill=fill, width=max(1, int(round(width * self.s))),
                    joint="curve")

    def limb(self, p0, p1, width, fill):
        self.line([p0, p1], fill, width)
        r = width / 2.0
        for p in (p0, p1):
            self.circle(p, r, fill)

    def circle(self, c, r, fill=None, outline=None, width=1.0):
        self.d.ellipse(self._b((c[0] - r, c[1] - r, c[0] + r, c[1] + r)),
                       fill=fill, outline=outline,
                       width=max(1, int(round(width * self.s))))

    def ellipse(self, box, fill=None, outline=None, width=1.0):
        self.d.ellipse(self._b(box), fill=fill, outline=outline,
                       width=max(1, int(round(width * self.s))))

    def chord(self, box, a0, a1, fill):
        self.d.chord(self._b(box), a0, a1, fill=fill)

    def pie(self, box, a0, a1, fill):
        self.d.pieslice(self._b(box), a0, a1, fill=fill)

    def arc(self, box, a0, a1, fill, width=1.0):
        self.d.arc(self._b(box), a0, a1, fill=fill,
                   width=max(1, int(round(width * self.s))))

    def poly(self, pts, fill, outline=None):
        self.d.polygon(self._p(pts), fill=fill, outline=outline)

    def rect(self, box, fill=None, outline=None, width=1.0):
        self.d.rectangle(self._b(box), fill=fill, outline=outline,
                         width=max(1, int(round(width * self.s))))

    def rrect(self, box, r, fill=None, outline=None, width=1.0):
        self.d.rounded_rectangle(self._b(box), radius=r * self.s, fill=fill,
                                 outline=outline,
                                 width=max(1, int(round(width * self.s))))


def two_bone(a, b, l1, l2, bend):
    """Elbow/knee position for a two bone chain from a to b."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    d = math.hypot(dx, dy)
    d = min(max(d, 1e-3), l1 + l2 - 1e-2)
    ux, uy = dx / d, dy / d
    t = (l1 * l1 - l2 * l2 + d * d) / (2.0 * d)
    h = math.sqrt(max(0.0, l1 * l1 - t * t))
    px, py = a[0] + ux * t, a[1] + uy * t
    return (px - uy * h * bend, py + ux * h * bend)


# ------------------------------------------------------------ background ----


def build_background():
    """Everything that never moves, rendered once at SS scale."""
    rng = random.Random(7)

    # --- sky + sea gradient, straight into numpy
    ys = np.arange(H, dtype=np.float32)
    grad = np.zeros((H, 3), dtype=np.float32)
    for i, y in enumerate(ys):
        if y < HORIZON:
            f = (y / HORIZON) ** 1.7
            grad[i] = np.array(mix(SKY_TOP, SKY_HORIZON, f), dtype=np.float32)
        elif y < FLOOR_Y:
            f = (y - HORIZON) / (FLOOR_Y - HORIZON)
            grad[i] = np.array(mix(SEA, shade(SEA, 0.7), f), dtype=np.float32)
        else:
            f = (y - FLOOR_Y) / (H - FLOOR_Y)
            near = mix(FLOOR_BACK, FLOOR_LIT, min(1.0, f * 1.9))
            grad[i] = np.array(mix(near, FLOOR_FRONT, max(0.0, (f - 0.55) / 0.45)),
                               dtype=np.float32)
    arr = np.repeat(grad[:, None, :], W, axis=1)
    img = Image.fromarray(arr.astype(np.uint8), "RGB").resize((W * SS, H * SS),
                                                              Image.BILINEAR)
    p = Pen(ImageDraw.Draw(img))

    # --- stars
    for _ in range(190):
        x = rng.uniform(0, W)
        y = rng.uniform(0, HORIZON - 14)
        b = rng.uniform(0.25, 1.0) * (1.0 - y / HORIZON) ** 0.5
        c = int(150 + 105 * b)
        p.circle((x, y), rng.uniform(0.5, 1.5), (c, c, min(255, c + 12)))

    # --- moon
    p.circle((172, 96), 27, (250, 244, 224))
    p.circle((160, 88), 25, mix(SKY_TOP, SKY_HORIZON, 0.12))

    # --- distant village along the horizon
    def house(x, base, w, h, dome=False):
        lit = mix(shade(WALL, 0.80), (255, 214, 160), 0.22)
        p.rect((x, base - h, x + w, base), shade(lit, 0.80))
        p.rect((x, base - h, x + w * 0.55, base), lit)
        p.rect((x - 1.5, base - h - 3, x + w + 1.5, base - h), shade(lit, 0.66))
        if dome:
            p.pie((x + w * 0.18, base - h - w * 0.62, x + w * 0.82, base - h + w * 0.2),
                  180, 360, shade(DOME, 0.95))
            p.line([(x + w * 0.5, base - h - w * 0.62), (x + w * 0.5, base - h - w * 0.85)],
                   shade(WALL, 0.7), 1.6)
        for _ in range(max(1, int(w * h / 900))):
            wx = x + rng.uniform(0.12, 0.78) * w
            wy = base - rng.uniform(0.25, 0.8) * h
            p.rect((wx, wy, wx + 4.5, wy + 6), (232, 186, 108))

    for cx in (28, 96, 168, 250, 330, 404, 470, 560, 700, 790, 860, 940, 1020, 1110, 1195):
        w = rng.uniform(34, 62)
        h = rng.uniform(24, 52)
        house(cx, HORIZON - rng.uniform(0, 8), w, h, dome=rng.random() < 0.28)

    # --- sea sparkle under the moon
    for _ in range(120):
        x = rng.gauss(190, 105)
        y = rng.uniform(HORIZON + 4, FLOOR_Y - 4)
        ln = rng.uniform(6, 34) * (1.0 - abs(x - 190) / 340.0)
        if ln > 1:
            a = 0.35 + 0.5 * rng.random()
            p.line([(x - ln / 2, y), (x + ln / 2, y)], mix(SEA, (238, 226, 196), a * 0.55), 1.4)

    # --- terrace wall between the sea and the dance floor
    p.rect((0, FLOOR_Y - 26, W, FLOOR_Y + 6), shade(WALL, 0.46))
    p.rect((0, FLOOR_Y - 26, W, FLOOR_Y - 20), shade(WALL, 0.60))
    for x in range(0, W + 30, 30):
        p.rect((x, FLOOR_Y - 26, x + 1.6, FLOOR_Y + 6), shade(WALL, 0.38))

    # --- floor tiles in perspective
    vy = HORIZON
    rows = []
    y = FLOOR_Y + 6
    step = 7.0
    while y < H + 40:
        rows.append(y)
        y += step
        step *= 1.185
    for y in rows:
        p.line([(0, y), (W, y)], shade(FLOOR_BACK, 1.28), 1.2)
    for i in range(-14, 15):
        x_far = 640 + i * 26
        x_near = 640 + i * 150
        p.line([(x_far, FLOOR_Y + 6), (x_near, H + 20)], shade(FLOOR_BACK, 1.22), 1.2)

    # --- planters and greenery along the wall
    def bush(x, y, w, h, flowers):
        for _ in range(int(w * h / 45)):
            bx = x + rng.gauss(0, w * 0.3)
            by = y - abs(rng.gauss(0, h * 0.34))
            r = rng.uniform(3, 8)
            p.circle((bx, by), r, mix(LEAF, (54, 88, 62), rng.random() * 0.6))
        if flowers:
            for _ in range(int(w * h / 130)):
                bx = x + rng.gauss(0, w * 0.32)
                by = y - abs(rng.gauss(0, h * 0.36))
                p.circle((bx, by), rng.uniform(1.8, 3.6),
                         mix(BOUGAIN, (245, 148, 186), rng.random()))

    for x, w, h, fl in ((70, 74, 54, True), (250, 60, 44, False), (1020, 82, 58, True),
                        (1190, 66, 46, False), (900, 52, 38, False)):
        p.rrect((x - w * 0.32, FLOOR_Y - 12, x + w * 0.32, FLOOR_Y + 16), 4,
                shade((150, 120, 96), 0.55))
        bush(x, FLOOR_Y - 10, w, h, fl)

    # --- olive tree on the left
    p.line([(150, FLOOR_Y + 30), (146, FLOOR_Y - 78)], (44, 36, 30), 9)
    p.line([(148, FLOOR_Y - 40), (176, FLOOR_Y - 72)], (44, 36, 30), 5)
    p.line([(148, FLOOR_Y - 46), (118, FLOOR_Y - 74)], (44, 36, 30), 5)
    for _ in range(150):
        bx = 148 + rng.gauss(0, 34)
        by = FLOOR_Y - 96 + rng.gauss(0, 24)
        p.circle((bx, by), rng.uniform(3, 9), mix((30, 52, 42), (66, 96, 70), rng.random()))

    # --- little bar table with bottles on the right
    tx, ty = 1108, FLOOR_Y + 96
    p.rrect((tx - 78, ty - 8, tx + 78, ty + 6), 6, (72, 52, 42))
    p.rrect((tx - 74, ty - 12, tx + 74, ty - 4), 4, (206, 194, 176))
    p.line([(tx, ty + 4), (tx, ty + 62)], (58, 42, 34), 7)
    p.ellipse((tx - 40, ty + 56, tx + 40, ty + 70), (52, 38, 32))
    for i, (bx, bh, bc) in enumerate(((-46, 46, (58, 92, 60)), (-28, 52, (96, 58, 40)),
                                      (36, 40, (66, 74, 118)))):
        p.rrect((tx + bx - 6, ty - 12 - bh, tx + bx + 6, ty - 10), 4, bc)
        p.rect((tx + bx - 2.4, ty - 20 - bh, tx + bx + 2.4, ty - 8 - bh), shade(bc, 0.8))
    for gx in (-8, 4, 16):
        p.poly([(tx + gx - 6, ty - 30), (tx + gx + 6, ty - 30), (tx + gx + 3, ty - 13),
                (tx + gx - 3, ty - 13)], (208, 214, 216))

    return img


# ---------------------------------------------------------- string lights ---


def light_strands(t):
    """Bulb positions for the three sagging strands, gently swaying."""
    strands = []
    for i, (y0, y1, sag, n) in enumerate(((28, 62, 96, 15), (8, 44, 138, 13),
                                          (58, 26, 82, 14))):
        sway = math.sin(t * 0.7 + i * 1.9) * 5.0
        pts, bulbs = [], []
        for k in range(41):
            u = k / 40.0
            x = lerp(-40, W + 40, u)
            y = lerp(y0, y1, u) + math.sin(math.pi * u) * sag + sway * math.sin(math.pi * u)
            pts.append((x, y))
        for k in range(n):
            u = (k + 0.5) / n
            x = lerp(-40, W + 40, u)
            y = lerp(y0, y1, u) + math.sin(math.pi * u) * sag + sway * math.sin(math.pi * u)
            bulbs.append((x, y + 9, i * 31 + k))
        strands.append((pts, bulbs))
    return strands


# ----------------------------------------------------------- the dancers ----


def dancer_pose(ch, t, beats):
    """Every joint position for one dancer at time t."""
    idx = CAST.index(ch)
    off = -0.055 * idx                       # the line ripples down its length
    u = (beats / BEATS_PER_STEP + off) % 1.0
    q = u * BEATS_PER_STEP                   # position inside the 4 beat figure

    kick_r = bump(q - 2.0)
    kick_l = bump(q - 3.0)
    hop = 11.0 * (kick_r + kick_l)
    bounce = 5.0 * abs(math.sin(math.pi * (beats + off * BEATS_PER_STEP)))
    sway = 22.0 * math.sin(2 * math.pi * u)
    lean = -7.0 * math.sin(2 * math.pi * u)

    s = ch["scale"]
    cx = 640.0 + ch["dx"] + sway * s
    base = GROUND

    leg = 212.0 * s
    torso = 142.0 * s
    neck = 12.0 * s
    head_r = 34.0 * s
    sh_w = (46.0 if ch["legwear"] == "trousers" else 37.0) * s
    hip_w = (35.0 if ch["legwear"] == "trousers" else 31.0) * s
    bone = leg / (2.0 * 0.972)
    ua, fa = 80.0 * s, 76.0 * s

    hip_y = base - leg - hop - bounce
    hip = (cx, hip_y)
    sh_y = hip_y - torso
    shoulder = (cx + lean * s, sh_y)
    head_c = (shoulder[0] + lean * 0.35 * s, sh_y - neck - head_r)

    sh_l = (shoulder[0] - sh_w, sh_y + 4 * s)
    sh_r = (shoulder[0] + sh_w, sh_y + 4 * s)
    hip_l = (hip[0] - hip_w, hip_y)
    hip_r = (hip[0] + hip_w, hip_y)

    # feet: planted, or kicked out sideways and up
    stance = 17.0 * s
    foot_l = [cx - stance, base]
    foot_r = [cx + stance, base]
    # the maxi dress only opens on one side, so that leg does the big kicks
    kl = kick_l * ch.get("kick_l_scale", 1.0)
    kr = kick_r * ch.get("kick_r_scale", 1.0)
    if kl > 0.01:
        foot_l[0] = cx - stance - 90.0 * s * kl
        foot_l[1] = base - 74.0 * s * kl
    if kr > 0.01:
        foot_r[0] = cx + stance + 90.0 * s * kr
        foot_r[1] = base - 74.0 * s * kr
    knee_l = two_bone(hip_l, foot_l, bone, bone, 1.0)
    knee_r = two_bone(hip_r, foot_r, bone, bone, -1.0)

    return dict(ch=ch, s=s, cx=cx, u=u, q=q, kick_l=kick_l, kick_r=kick_r,
                hop=hop + bounce, lean=lean, head_r=head_r, head_c=head_c,
                shoulder=shoulder, sh_l=sh_l, sh_r=sh_r, hip=hip, hip_l=hip_l,
                hip_r=hip_r, knee_l=knee_l, knee_r=knee_r,
                foot_l=tuple(foot_l), foot_r=tuple(foot_r), sh_y=sh_y,
                hip_y=hip_y, ua=ua, fa=fa, sh_w=sh_w, base=base)


def draw_shoe(p, foot, kind, s, ch, kicking):
    x, y = foot
    if kind == "dress":
        p.rrect((x - 15 * s, y - 8 * s, x + 15 * s, y + 3 * s), 4 * s, (32, 28, 30))
    elif kind == "sneaker":
        p.rrect((x - 16 * s, y - 12 * s, x + 16 * s, y + 1 * s), 5 * s, (30, 30, 34))
        p.rrect((x - 16 * s, y - 3 * s, x + 16 * s, y + 3 * s), 3 * s, (236, 236, 232))
    else:  # strappy silver heel
        p.rrect((x - 13 * s, y - 4 * s, x + 13 * s, y + 2 * s), 2 * s, (214, 210, 202))
        p.line([(x + 8 * s, y - 2 * s), (x + 10 * s, y - 16 * s)], (214, 210, 202), 3 * s)
        p.line([(x - 10 * s, y - 14 * s), (x + 8 * s, y - 6 * s)], (222, 218, 210), 2.4 * s)


def draw_leg(p, pose, side, over_dress=False):
    ch, s = pose["ch"], pose["s"]
    hip = pose["hip_l"] if side == "l" else pose["hip_r"]
    knee = pose["knee_l"] if side == "l" else pose["knee_r"]
    foot = pose["foot_l"] if side == "l" else pose["foot_r"]
    kicking = (pose["kick_l"] if side == "l" else pose["kick_r"]) > 0.25

    if ch["legwear"] == "dress":
        if over_dress:
            # the skirt drapes over the raised thigh, the slit shows the shin
            p.limb(hip, knee, 32 * s, shade(ch["top"], 1.7))
            p.limb(knee, foot, 21 * s, ch["skin"])
            draw_shoe(p, foot, ch["shoe"], s, ch, kicking)
            return
        col = shade(ch["skin"], 0.9)
        w = 24 * s
    else:
        col = ch["pants"]
        w = 33 * s
    p.limb(hip, knee, w, col)
    p.limb(knee, foot, w * 0.84, col)
    draw_shoe(p, foot, ch["shoe"], s, ch, kicking)


def draw_arm(p, pose, shoulder, hand, bend, sleeve):
    ch, s = pose["ch"], pose["s"]
    elbow = two_bone(shoulder, hand, pose["ua"], pose["fa"], bend)
    skin, top = ch["skin"], ch["top"]
    if sleeve == "long":
        p.limb(shoulder, elbow, 23 * s, top)
        p.limb(elbow, hand, 19 * s, top)
    elif sleeve == "rolled":
        p.limb(shoulder, elbow, 23 * s, top)
        p.limb(elbow, hand, 16 * s, skin)
        p.circle(elbow, 8 * s, shade(top, 0.94))
    else:
        p.limb(shoulder, elbow, 17 * s, skin)
        p.limb(elbow, hand, 14 * s, skin)
    p.circle(hand, 9.5 * s, skin)
    return elbow


def draw_head(p, pose, t):
    ch, s = pose["ch"], pose["s"]
    cx, cy = pose["head_c"]
    r = pose["head_r"]
    skin, hair = ch["skin"], ch["hair"]
    tilt = pose["lean"] * 0.5 * s

    # long hair sits behind everything
    if ch.get("longhair"):
        swing = math.sin(2 * math.pi * pose["u"]) * 9 * s
        p.ellipse((cx - r * 1.32 + swing * 0.5, cy - r * 1.02,
                   cx + r * 1.32 + swing * 0.5, cy + r * 3.5), hair)
        p.ellipse((cx - r * 1.5 + swing, cy + r * 0.6,
                   cx - r * 0.35 + swing, cy + r * 3.3), shade(hair, 1.12))
        p.ellipse((cx + r * 0.35 + swing, cy + r * 0.6,
                   cx + r * 1.5 + swing, cy + r * 3.3), shade(hair, 1.12))

    # neck + head
    p.limb((cx - tilt * 0.4, cy + r * 0.74), (pose["shoulder"][0], pose["sh_y"] + 4 * s),
           15 * s, shade(skin, 0.88))
    p.circle((cx - r * 0.96, cy + r * 0.16), r * 0.18, skin)
    p.circle((cx + r * 0.96, cy + r * 0.16), r * 0.18, skin)
    p.ellipse((cx - r * 0.94, cy - r, cx + r * 0.94, cy + r * 1.06), skin)

    # beard: fill the lower head, then carve the face back out so a jawline rim is left
    if ch["beard"]:
        p.chord((cx - r * 0.94, cy - r, cx + r * 0.94, cy + r * 1.06), -22, 202, hair)
        p.ellipse((cx - r * 0.70, cy - r * 0.62, cx + r * 0.70, cy + r * 0.80), skin)

    # eyes, brows, nose, smile
    ey = cy - r * 0.14
    for sx in (-1, 1):
        p.ellipse((cx + sx * r * 0.35 - r * 0.10, ey - r * 0.13,
                   cx + sx * r * 0.35 + r * 0.10, ey + r * 0.12), (36, 26, 22))
        p.circle((cx + sx * r * 0.35 - r * 0.03, ey - r * 0.05), r * 0.042, (255, 255, 255))
        p.line([(cx + sx * r * 0.15, ey - r * 0.3), (cx + sx * r * 0.56, ey - r * 0.35)],
               hair, r * 0.14)
    p.arc((cx - r * 0.15, ey + r * 0.04, cx + r * 0.15, ey + r * 0.34), 20, 150,
          shade(skin, 0.8), r * 0.07)

    mw, mh = r * 0.33, r * 0.24
    my = cy + r * 0.52
    if ch["beard"]:                                   # trimmed moustache, above the smile
        p.ellipse((cx - mw * 1.1, my - mh * 1.5, cx + mw * 1.1, my - mh * 0.78),
                  shade(hair, 1.3))
    p.ellipse((cx - mw, my - mh * 0.6, cx + mw, my + mh * 1.15), (92, 42, 42))
    p.chord((cx - mw, my - mh * 0.6, cx + mw, my + mh * 1.15), 182, 358, (250, 248, 244))

    # hair on top
    if not ch.get("longhair"):
        p.chord((cx - r * 1.02, cy - r * 1.68, cx + r * 1.02, cy + r * 0.36), 180, 360, hair)
        for sx in (-1, 1):                            # sideburns down to the beard
            p.rect((cx + sx * r * 0.86 - r * 0.1, cy - r * 0.7,
                    cx + sx * r * 0.86 + r * 0.1, cy + r * 0.08), hair)
        if ch["curly"]:
            for k in range(7):
                a = math.pi * (0.08 + 0.84 * k / 6.0)
                p.circle((cx - math.cos(a) * r * 0.9, cy - r * 0.66 - math.sin(a) * r * 0.66),
                         r * 0.25, hair)
    else:
        p.chord((cx - r * 1.08, cy - r * 1.52, cx + r * 1.08, cy + r * 0.58), 180, 360, hair)
        for sx in (-1, 1):                            # locks framing the face
            p.ellipse((cx + sx * r * 1.16 - r * 0.24, cy - r * 0.8,
                       cx + sx * r * 1.16 + r * 0.24, cy + r * 0.42), hair)


def draw_torso(p, pose):
    ch, s = pose["ch"], pose["s"]
    top, dark = ch["top"], ch["top_shade"]
    sl, sr = pose["sh_l"], pose["sh_r"]
    hl, hr = pose["hip_l"], pose["hip_r"]

    if ch["legwear"] == "dress":
        waist_y = lerp(sl[1], hl[1], 0.64)
        wl = (lerp(sl[0], hl[0], 0.64) - 1 * s, waist_y)
        wr = (lerp(sr[0], hr[0], 0.64) + 1 * s, waist_y)
        hem_y = pose["base"] - 5 * s
        hip_y = pose["hip_y"]
        bx = pose["cx"]
        drift = pose["lean"] * 1.8 * s
        # fitted column, nipped at the waist, with a slit cut up the right side
        p.poly([wl, wr,
                (bx + 50 * s, hip_y + 14 * s),
                (bx + 45 * s + drift, hem_y), (bx + 40 * s + drift, hem_y + 5 * s),
                (bx + 31 * s + drift, hem_y + 5 * s),
                (bx + 20 * s, hip_y + 66 * s),                       # slit apex
                (bx + 3 * s + drift, hem_y + 5 * s),
                (bx - 40 * s + drift, hem_y + 5 * s), (bx - 45 * s + drift, hem_y),
                (bx - 50 * s, hip_y + 14 * s)], top)
        p.poly([sl, sr, (wr[0], waist_y + 3 * s), (wl[0], waist_y + 3 * s)], top)
        p.line([(wl[0], waist_y), (wr[0], waist_y)], dark, 3 * s)
        # square neckline
        p.poly([(sl[0] + 12 * s, sl[1] - 3 * s), (sr[0] - 12 * s, sr[1] - 3 * s),
                (sr[0] - 12 * s, sl[1] + 17 * s), (sl[0] + 12 * s, sl[1] + 17 * s)],
               shade(ch["skin"], 0.94))
        return

    # shirt body, cut loose so it hangs over the belt
    p.poly([(sl[0], sl[1] - 7 * s), (sr[0], sr[1] - 7 * s),
            (sr[0] + 2 * s, lerp(sr[1], hr[1], 0.55)),
            (hr[0] + 12 * s, hr[1] + 18 * s), (hl[0] - 12 * s, hl[1] + 18 * s),
            (sl[0] - 2 * s, lerp(sl[1], hl[1], 0.55))], top)
    p.rrect((hl[0] - 6 * s, hr[1] + 4 * s, hr[0] + 6 * s, hr[1] + 20 * s), 3 * s, ch["pants"])
    p.rrect((hl[0] - 6 * s, hr[1] + 4 * s, hr[0] + 6 * s, hr[1] + 11 * s), 2 * s, (24, 22, 26))
    p.rect((pose["cx"] - 6 * s, hr[1] + 4 * s, pose["cx"] + 6 * s, hr[1] + 11 * s),
           (198, 196, 190))

    cx = pose["shoulder"][0]
    neck_y = sl[1] - 4 * s
    if ch["collar"] == "camp":
        p.poly([(cx - 17 * s, neck_y), (cx + 17 * s, neck_y), (cx, neck_y + 42 * s)],
               shade(ch["skin"], 0.9))
        p.poly([(cx - 20 * s, neck_y - 4 * s), (cx - 2 * s, neck_y - 2 * s),
                (cx - 20 * s, neck_y + 26 * s)], dark)
        p.poly([(cx + 20 * s, neck_y - 4 * s), (cx + 2 * s, neck_y - 2 * s),
                (cx + 20 * s, neck_y + 26 * s)], dark)
    else:
        p.poly([(cx - 14 * s, neck_y - 2 * s), (cx + 14 * s, neck_y - 2 * s),
                (cx, neck_y + 20 * s)], shade(ch["skin"], 0.9))
        p.poly([(cx - 17 * s, neck_y - 5 * s), (cx - 1 * s, neck_y - 2 * s),
                (cx - 15 * s, neck_y + 20 * s)], dark)
        p.poly([(cx + 17 * s, neck_y - 5 * s), (cx + 1 * s, neck_y - 2 * s),
                (cx + 15 * s, neck_y + 20 * s)], dark)
        p.rrect((cx + 6 * s, neck_y + 26 * s, cx + 24 * s, neck_y + 48 * s), 2 * s, dark)
    p.line([(cx, neck_y + 34 * s), (cx + (hr[0] + hl[0]) / 2 - cx, hr[1] + 2 * s)], dark, 2.2 * s)
    for k in range(3):
        p.circle((cx + 1 * s, neck_y + (48 + k * 26) * s), 2.4 * s, shade(dark, 0.85))


def draw_prop(p, pose, hand, t):
    ch, s = pose["ch"], pose["s"]
    x, y = hand
    if ch["prop"] == "glass":
        p.poly([(x - 13 * s, y - 20 * s), (x + 13 * s, y - 20 * s),
                (x + 10 * s, y + 8 * s), (x - 10 * s, y + 8 * s)], (206, 218, 224))
        p.poly([(x - 11 * s, y - 6 * s), (x + 11 * s, y - 6 * s),
                (x + 10 * s, y + 7 * s), (x - 10 * s, y + 7 * s)], (156, 52, 44))
        p.rect((x - 12 * s, y - 20 * s, x + 12 * s, y - 17 * s), (232, 240, 244))
        p.circle(hand, 9.5 * s, ch["skin"])
        p.line([(x - 9 * s, y - 4 * s), (x + 9 * s, y - 6 * s)], (188, 66, 56), 3 * s)
    elif ch["prop"] == "napkin":
        flap = math.sin(t * 11.0) * 0.5
        p.poly([(x, y), (x + 26 * s, y - (34 + 12 * flap) * s),
                (x + 46 * s, y - (10 - 16 * flap) * s), (x + 24 * s, y + 10 * s)],
               (246, 244, 238))
        p.poly([(x + 2 * s, y + 2 * s), (x + 24 * s, y - (26 + 10 * flap) * s),
                (x + 30 * s, y - (14 - 6 * flap) * s), (x + 14 * s, y + 8 * s)],
               (226, 222, 214))


def draw_dancer(p, poses, i, t, opa):
    pose = poses[i]
    ch, s = pose["ch"], pose["s"]

    # ground shadow
    sw = 62 * s * (1.0 - pose["hop"] / 260.0)
    p.ellipse((pose["cx"] - sw, GROUND - 9 * s, pose["cx"] + sw, GROUND + 12 * s),
              shade(FLOOR_LIT, 0.42))

    # far arm and far leg first so they read as behind the body
    if i > 0:
        target = (poses[i - 1]["sh_r"][0] + 4 * s, poses[i - 1]["sh_r"][1] + 2 * s)
        draw_arm(p, pose, pose["sh_l"], target, -1.0, ch["sleeves"])
    draw_leg(p, pose, "l")
    draw_leg(p, pose, "r")
    draw_torso(p, pose)
    if ch["legwear"] == "dress":                       # leg through the slit
        if pose["kick_r"] > 0.30:
            draw_leg(p, pose, "r", over_dress=True)
    draw_head(p, pose, t)

    # near arm: onto the next shoulder, or free and up
    if i < len(poses) - 1:
        target = (poses[i + 1]["sh_l"][0] - 4 * s, poses[i + 1]["sh_l"][1] - 15 * s)
        draw_arm(p, pose, pose["sh_r"], target, 1.0, ch["sleeves"])

    if ch["free"]:
        raise_ = 1.0 if opa < 0 else lerp(1.0, 1.45, opa)
        wob = math.sin(2 * math.pi * pose["u"] + 0.6) * 12 * s
        if ch["free"] == "left":
            hand = (pose["sh_l"][0] - (58 + wob) * s, pose["sh_y"] - (96 * raise_) * s)
            elbow_bend = -1.0
            shoulder = pose["sh_l"]
        else:
            hand = (pose["sh_r"][0] + (58 - wob) * s, pose["sh_y"] - (96 * raise_) * s)
            elbow_bend = 1.0
            shoulder = pose["sh_r"]
        draw_arm(p, pose, shoulder, hand, elbow_bend, ch["sleeves"])
        draw_prop(p, pose, hand, t)


# ------------------------------------------------------------- confetti -----


class Confetti:
    def __init__(self, seed=3):
        rng = random.Random(seed)
        self.bits = []
        for i in range(70):
            self.bits.append(dict(
                x=rng.uniform(-40, W + 40), y=rng.uniform(-H, -10),
                vy=rng.uniform(46, 108), vx=rng.uniform(-14, 14),
                w=rng.uniform(6, 13), h=rng.uniform(9, 17),
                spin=rng.uniform(1.6, 5.2), ph=rng.uniform(0, 6.3),
                c=rng.choice(CONFETTI_COLORS), t0=rng.uniform(0.0, 6.0)))
        self.burst = []
        for i in range(120):
            a = rng.uniform(0, 2 * math.pi)
            sp = rng.uniform(120, 620)
            self.burst.append(dict(a=a, sp=sp, w=rng.uniform(6, 14),
                                   h=rng.uniform(8, 18), spin=rng.uniform(2, 7),
                                   ph=rng.uniform(0, 6.3), c=rng.choice(CONFETTI_COLORS),
                                   x0=640 + rng.gauss(0, 60), y0=430 + rng.gauss(0, 40)))

    def draw(self, p, t):
        for b in self.bits:
            if t < b["t0"]:
                continue
            dt = t - b["t0"]
            y = b["y"] + b["vy"] * dt + (dt * dt) * 6.0
            y = ((y + H + 60) % (H + 120)) - 60
            x = b["x"] + math.sin(dt * 1.5 + b["ph"]) * 26 + b["vx"] * dt
            self._flake(p, x, y, b, dt)
        if t > OPA_T:
            dt = t - OPA_T
            for b in self.burst:
                x = b["x0"] + math.cos(b["a"]) * b["sp"] * dt
                y = b["y0"] + math.sin(b["a"]) * b["sp"] * dt + 210 * dt * dt
                if -40 < x < W + 40 and -40 < y < H + 40:
                    self._flake(p, x, y, b, dt)

    @staticmethod
    def _flake(p, x, y, b, dt):
        sq = abs(math.cos(dt * b["spin"] + b["ph"]))
        w = b["w"] * (0.25 + 0.75 * sq)
        c = b["c"] if sq > 0.4 else shade(b["c"], 0.66)
        p.poly([(x - w / 2, y - b["h"] / 2), (x + w / 2, y - b["h"] / 2 + 2),
                (x + w / 2, y + b["h"] / 2), (x - w / 2, y + b["h"] / 2 - 2)], c)


# ------------------------------------------------------------------ glow ----

_SPRITES = {}


def _sprite(r):
    if r not in _SPRITES:
        yy, xx = np.ogrid[-r:r + 1, -r:r + 1]
        d2 = (xx * xx + yy * yy) / float(r * r)
        s = np.exp(-d2 * 2.4).astype(np.float32)
        s[d2 > 1.0] = 0.0
        _SPRITES[r] = s
    return _SPRITES[r]


def add_glow(acc, cx, cy, r, strength, color):
    r = int(r)
    if r < 1:
        return
    x0, y0 = int(cx) - r, int(cy) - r
    x1, y1 = x0 + 2 * r + 1, y0 + 2 * r + 1
    sx0, sy0 = max(0, -x0), max(0, -y0)
    cx0, cy0 = max(0, x0), max(0, y0)
    cx1, cy1 = min(acc.shape[1], x1), min(acc.shape[0], y1)
    if cx1 <= cx0 or cy1 <= cy0:
        return
    sp = _sprite(r)[sy0:sy0 + (cy1 - cy0), sx0:sx0 + (cx1 - cx0)]
    acc[cy0:cy1, cx0:cx1] += sp[:, :, None] * (np.asarray(color, np.float32) * strength)


# ------------------------------------------------------------------ audio ---


def pluck(freq, dur, sr, amp=1.0, bright=1.0):
    n = max(1, int(dur * sr))
    t = np.arange(n, dtype=np.float32) / sr
    env = np.exp(-t * (3.4 + 2.0 / max(0.15, dur))).astype(np.float32)
    att = np.clip(t / 0.004, 0.0, 1.0)
    sig = np.zeros(n, dtype=np.float32)
    for course in (0.0, 4.0):                      # doubled strings, slightly detuned
        f = freq * (2.0 ** (course / 1200.0))
        for k in range(1, 8):
            a = (1.0 / (k ** 1.55)) * (bright if k > 1 else 1.0)
            sig += a * np.sin(2 * np.pi * f * k * t + k * 0.7).astype(np.float32)
    return sig * env * att * (amp * 0.16)


def clap(dur, sr, amp=1.0):
    n = int(dur * sr)
    rng = np.random.default_rng(11)
    t = np.arange(n, dtype=np.float32) / sr
    noise = rng.standard_normal(n).astype(np.float32)
    noise = np.convolve(noise, np.array([1, -0.6, 0.3], np.float32), mode="same")
    env = np.exp(-t * 46.0).astype(np.float32)
    return noise * env * amp * 0.35


def build_audio(path):
    sr = 44100
    n = int((DUR + 0.4) * sr)
    buf = np.zeros(n, dtype=np.float32)

    def place(sig, t0, gain=1.0):
        i = int(t0 * sr)
        if i < 0 or i >= n:
            return
        m = min(len(sig), n - i)
        buf[i:i + m] += sig[:m] * gain

    def midi(m):
        return 440.0 * 2.0 ** ((m - 69) / 12.0)

    # D hijaz-ish riff, two bars, looped until the clip runs out
    riff = [(0.0, 0.5, 69), (0.5, 0.5, 70), (1.0, 0.5, 69), (1.5, 0.5, 67),
            (2.0, 0.5, 66), (2.5, 0.5, 67), (3.0, 0.5, 69), (3.5, 0.5, 74),
            (4.0, 0.5, 74), (4.5, 0.5, 72), (5.0, 0.5, 70), (5.5, 0.5, 69),
            (6.0, 0.5, 67), (6.5, 0.5, 66), (7.0, 0.5, 63), (7.5, 0.5, 62)]

    bar = 0.0
    while bar < TOTAL_BEATS:
        for (b, d, note) in riff:
            beat = bar + b
            if beat >= TOTAL_BEATS:
                break
            t0 = time_at(beat)
            dt = max(0.10, time_at(min(TOTAL_BEATS, beat + d * 2.2)) - t0)
            place(pluck(midi(note + 12), dt, sr, amp=0.85, bright=0.9), t0)
            place(pluck(midi(note), dt, sr, amp=0.45, bright=0.7), t0)
        bar += 8.0

    beat = 0.0
    while beat < TOTAL_BEATS:
        root = 62 if int(beat // 4) % 2 == 0 else 57
        t0 = time_at(beat)
        dt = max(0.16, time_at(min(TOTAL_BEATS, beat + 1.6)) - t0)
        place(pluck(midi(root - 24), dt, sr, amp=1.5, bright=0.35), t0)
        if beat + 2 < TOTAL_BEATS:
            t2 = time_at(beat + 2)
            place(pluck(midi(root - 17), dt, sr, amp=1.0, bright=0.35), t2)
        for off in (1.0, 3.0):
            if beat + off < TOTAL_BEATS:
                place(clap(0.22, sr, 0.9), time_at(beat + off))
        beat += 4.0

    # cheer on the opa
    rng = np.random.default_rng(5)
    cn = int(2.2 * sr)
    ct = np.arange(cn, dtype=np.float32) / sr
    cheer = rng.standard_normal(cn).astype(np.float32)
    cheer = np.convolve(cheer, np.ones(9, np.float32) / 9.0, mode="same")
    cheer *= (np.clip(ct / 0.08, 0, 1) * np.exp(-ct * 1.3)).astype(np.float32)
    for _ in range(150):
        i = int(rng.uniform(0, cn - 900))
        cheer[i:i + 900] += (rng.standard_normal(900).astype(np.float32)
                             * np.exp(-np.arange(900, dtype=np.float32) / 90.0) * 0.5)
    place(cheer * 0.09, OPA_T - 0.12)

    # fades and normalisation
    fi, fo = int(0.12 * sr), int(0.45 * sr)
    buf[:fi] *= np.linspace(0, 1, fi, dtype=np.float32)
    buf[-fo:] *= np.linspace(1, 0, fo, dtype=np.float32)
    peak = float(np.max(np.abs(buf))) or 1.0
    buf = np.tanh(buf / peak * 1.5) * 0.86

    data = (buf * 32767.0).astype(np.int16)
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(data.tobytes())
    return path


# ------------------------------------------------------------------ render --


def render_frame(bg, confetti, font_big, i):
    t = i / float(FPS)
    beats = beats_at(t)
    img = bg.copy()
    p = Pen(ImageDraw.Draw(img))

    # string lights: wires now, bulbs are added to the glow pass too
    bulbs = []
    for pts, bl in light_strands(t):
        p.line(pts, (58, 48, 44), 1.6)
        for (bx, by, seed) in bl:
            tw = 0.72 + 0.28 * math.sin(t * (2.0 + (seed % 7) * 0.31) + seed)
            p.line([(bx, by - 9), (bx, by - 4)], (70, 60, 54), 1.6)
            p.circle((bx, by), 5.4, mix((255, 214, 150), (255, 246, 214), tw))
            bulbs.append((bx, by, tw))

    poses = [dancer_pose(ch, t, beats) for ch in CAST]
    opa = -1.0
    if t > OPA_T:
        opa = min(1.0, (t - OPA_T) / 0.35)
    order = [1, 0, 2]                      # middle dancer sits behind the ends
    for i_d in order:
        draw_dancer(p, poses, i_d, t, opa)

    confetti.draw(p, t)

    # "opa!" title
    if t > OPA_T:
        k = min(1.0, (t - OPA_T) / 0.45)
        sc = ease_out_back(k)
        txt = "ΩΠΑ!"
        size = int(116 * SS * max(0.05, sc))
        f = ImageFont.truetype(FONT_PATH, size)
        tmp = Image.new("RGBA", (int(760 * SS), int(300 * SS)), (0, 0, 0, 0))
        td = ImageDraw.Draw(tmp)
        td.text((int(380 * SS), int(150 * SS)), txt, font=f, anchor="mm",
                fill=(255, 236, 196, 255), stroke_width=int(8 * SS),
                stroke_fill=(58, 26, 32, 255))
        ang = math.sin((t - OPA_T) * 6.0) * 3.0 * (1.0 - k * 0.5) - 5.0
        tmp = tmp.rotate(ang, resample=Image.BICUBIC, expand=False)
        img.paste(tmp, (int((W / 2 - 380) * SS), int((116 - 150) * SS)), tmp)

    # down-sample for anti-aliasing
    small = img.resize((W, H), Image.LANCZOS)
    arr = np.asarray(small, dtype=np.float32)

    # additive light: bulbs, the pool on the floor, the opa flash
    glow = np.zeros((H, W, 3), dtype=np.float32)
    for (bx, by, tw) in bulbs:
        add_glow(glow, bx, by, 34, 0.52 * tw, (1.0, 0.72, 0.36))
    add_glow(glow, 640, 606, 330, 0.20, (1.0, 0.66, 0.30))
    add_glow(glow, 190, 96, 90, 0.10, (0.72, 0.80, 1.0))
    if t > OPA_T:
        fl = max(0.0, 1.0 - (t - OPA_T) / 0.5)
        add_glow(glow, 640, 300, 520, 0.55 * fl * fl, (1.0, 0.82, 0.55))
    arr = arr + glow * 255.0

    # slow push-in, then a warm grade and a vignette
    arr = np.clip(arr, 0, 255)
    out = Image.fromarray(arr.astype(np.uint8), "RGB")
    z = lerp(1.0, 1.10, (t / DUR) ** 0.85)
    if z > 1.001:
        cw, chh = W / z, H / z
        cx0 = (W - cw) / 2.0
        cy0 = (H - chh) / 2.0 + (1.0 - 1.0 / z) * 26.0
        out = out.resize((W, H), Image.BICUBIC,
                         box=(cx0, cy0, cx0 + cw, cy0 + chh))

    if t < 0.4:                                     # fade in from black
        f = t / 0.4
        out = Image.fromarray((np.asarray(out, np.float32) * f).astype(np.uint8), "RGB")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--out", default=os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "greek_wedding_dance.mp4"))
    ap.add_argument("--frames", type=int, default=NFRAMES)
    ap.add_argument("--preview", type=int, nargs="*", default=None,
                    help="render just these frame numbers as PNGs and stop")
    args = ap.parse_args()

    import imageio_ffmpeg
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

    sys.stderr.write("building background...\n")
    bg = build_background()
    confetti = Confetti()
    font_big = None

    if args.preview is not None:
        for i in args.preview:
            render_frame(bg, confetti, font_big, i).save(
                os.path.join(os.path.dirname(os.path.abspath(args.out)),
                             "preview_%03d.png" % i))
            sys.stderr.write("preview frame %d\n" % i)
        return

    tmpdir = tempfile.mkdtemp()
    wav = build_audio(os.path.join(tmpdir, "track.wav"))
    sys.stderr.write("audio done, rendering %d frames...\n" % args.frames)

    cmd = [ffmpeg, "-y", "-loglevel", "error",
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "%dx%d" % (W, H),
           "-r", str(FPS), "-i", "-", "-i", wav,
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20",
           "-preset", "medium", "-movflags", "+faststart",
           "-c:a", "aac", "-b:a", "160k", "-shortest", args.out]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    for i in range(args.frames):
        frame = render_frame(bg, confetti, font_big, i)
        proc.stdin.write(frame.tobytes())
        if i % 25 == 0:
            sys.stderr.write("  frame %d/%d\n" % (i, args.frames))
    proc.stdin.close()
    rc = proc.wait()
    if rc != 0:
        raise SystemExit("ffmpeg failed with %d" % rc)
    sys.stderr.write("wrote %s\n" % args.out)


if __name__ == "__main__":
    main()
