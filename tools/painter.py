# -*- coding: utf-8 -*-
"""Pinta texturas pixel-art estilo vanilla para cada caja y las empaqueta en una hoja."""
import random
from PIL import Image
from core import hx, shade, mix

FACE_TONE = {'top': 1.10, 'bottom': 0.78, 'left': 0.96, 'right': 0.96, 'front': 1.0, 'back': 0.90}
DARK = (22, 18, 16)


def rect_size(w, h, d):
    return 2 * d + 2 * w, d + h


def next_pow2(n):
    p = 16
    while p < n:
        p *= 2
    return p


def pack(rects):
    """rects: {key: (w, h)} -> (W, H, {key: (x, y)}) con la hoja más pequeña posible."""
    best = None
    widest = max(w for w, h in rects.values())
    for W in (32, 64, 128, 256):
        if widest > W:
            continue
        x = y = shelf = 0
        pos = {}
        for key, (w, h) in sorted(rects.items(), key=lambda kv: (-kv[1][1], kv[0])):
            if x + w > W:
                x, y, shelf = 0, y + shelf, 0
            pos[key] = (x, y)
            x += w
            shelf = max(shelf, h)
        H = next_pow2(y + shelf)
        if best is None or W * H < best[0]:
            best = (W * H, W, H, pos)
    return best[1], best[2], best[3]


def put(img, x, y, c):
    if 0 <= x < img.width and 0 <= y < img.height:
        img.putpixel((x, y), tuple(c) + (255,))


def paint_part(img, ox, oy, w, h, d, paint, seed):
    rnd = random.Random(seed)
    base = hx(paint['color'])
    noise = paint.get('noise', 0.06)
    pats = paint.get('pats', [])
    faces = {
        'top': (ox + d, oy, w, d), 'bottom': (ox + d + w, oy, w, d),
        'left': (ox, oy + d, d, h), 'front': (ox + d, oy + d, w, h),
        'right': (ox + d + w, oy + d, d, h), 'back': (ox + 2 * d + w, oy + d, w, h)}
    long_axis = 'z' if (d >= h and d >= w) else ('y' if h >= w else 'x')

    spots = {}
    for k, pt in enumerate(pats):
        if pt[0] != 'spots':
            continue
        dens = pt[2] if len(pt) > 2 else 0.05
        size = pt[3] if len(pt) > 3 else 1
        for fname, (fx, fy, fw, fh) in faces.items():
            s = set()
            for _ in range(max(1 if fw * fh > 8 else 0, int(round(fw * fh * dens)))):
                i, j = rnd.randrange(fw), rnd.randrange(fh)
                s.add((i, j))
                if size >= 2:
                    if rnd.random() < .7 and i + 1 < fw:
                        s.add((i + 1, j))
                    if rnd.random() < .5 and j + 1 < fh:
                        s.add((i, j + 1))
            spots[(k, fname)] = s

    def axis_t(fname, i, j, fw, fh):
        if long_axis == 'z':
            if fname == 'left':
                return i
            if fname == 'right':
                return fw - 1 - i
            if fname in ('top', 'bottom'):
                return j
        elif long_axis == 'y':
            if fname in ('left', 'right', 'front', 'back'):
                return fh - 1 - j
        return None

    eye_row = max(1, h // 3) if h >= 3 else 0

    for fname, (fx, fy, fw, fh) in faces.items():
        for j in range(fh):
            for i in range(fw):
                f = FACE_TONE[fname] * (1 - 0.10 * j / max(1, fh)) if fname not in ('top', 'bottom') else FACE_TONE[fname]
                c = shade(base, f * (1 + rnd.uniform(-noise, noise)))
                t = axis_t(fname, i, j, fw, fh)
                for k, pt in enumerate(pats):
                    kind = pt[0]
                    col = hx(pt[1]) if len(pt) > 1 and isinstance(pt[1], str) else None
                    if kind == 'belly':
                        frac = pt[2] if len(pt) > 2 else 0.34
                        if fname == 'bottom' or (fname != 'top' and j >= fh * (1 - frac)):
                            c = mix(c, col, 0.9)
                    elif kind == 'socks':
                        n = pt[2] if len(pt) > 2 else 2
                        if fname == 'bottom' or (fname != 'top' and j >= fh - n):
                            c = mix(c, col, 0.95)
                    elif kind == 'cap':
                        frac = pt[2] if len(pt) > 2 else 0.4
                        if fname == 'top' or (fname in ('left', 'right', 'back', 'front') and j < fh * frac):
                            c = mix(c, col, 0.9)
                    elif kind == 'frontpatch':
                        inset = pt[2] if len(pt) > 2 else 1
                        if fname == 'bottom' or (fname == 'front' and inset <= i < fw - inset and j >= inset):
                            c = mix(c, col, 0.95)
                    elif kind == 'stripes' and fname != 'bottom':
                        period = pt[2] if len(pt) > 2 else 4
                        width = pt[3] if len(pt) > 3 else 2
                        lim = fh * 0.85 if fname in ('left', 'right', 'back') else 999
                        if (i % period) < width and j < lim and (j + (i // period) * 3) % 7 != 0:
                            c = mix(c, col, 0.9)
                    elif kind == 'bands' and fname != 'bottom':
                        width = pt[2] if len(pt) > 2 else 2
                        a = j if (len(pt) > 3 and pt[3] == 'j') else i
                        if (a // width) % 2 == 1:
                            c = mix(c, col, 0.92)
                    elif kind == 'spots' and fname != 'bottom':
                        if (i, j) in spots.get((k, fname), ()):
                            c = mix(c, col, 0.9)
                    elif kind == 'rings' and t is not None:
                        width = pt[2] if len(pt) > 2 else 2
                        period = pt[3] if len(pt) > 3 else 4
                        off = pt[4] if len(pt) > 4 else 0
                        if (t + off) % period < width:
                            c = mix(c, col, 0.92)
                    elif kind == 'tip':
                        n = pt[2] if len(pt) > 2 else 2
                        cap = (long_axis == 'z' and fname == 'back') or (long_axis == 'y' and fname == 'bottom')
                        if cap or (t is not None and t < n):
                            c = mix(c, col, 0.95)
                    elif kind == 'mask':
                        if fname == 'front' and eye_row - 1 <= j <= eye_row + 1:
                            c = mix(c, col, 0.9)
                        elif fname == 'left' and i == fw - 1 and eye_row - 1 <= j <= eye_row + 1:
                            c = mix(c, col, 0.9)
                        elif fname == 'right' and i == 0 and eye_row - 1 <= j <= eye_row + 1:
                            c = mix(c, col, 0.9)
                    elif kind == 'speckle':
                        amt = pt[1]
                        c = shade(c, 1 + rnd.uniform(-amt, amt))
                    elif kind == 'scales':
                        if i % 3 == 0 or j % 3 == 0:
                            c = shade(c, pt[1] if len(pt) > 1 else 0.82)
                    elif kind == 'border' and fname in ('top', 'bottom'):
                        n = pt[2] if len(pt) > 2 else 1
                        if i < n or j < n or i >= fw - n or j >= fh - n:
                            c = mix(c, col, 0.95)
                put(img, fx + i, fy + j, c)

    eyes = paint.get('eyes')
    if eyes:
        style = eyes.get('style', 'front')
        ecol = hx(eyes.get('color', '#111111'))
        wv = eyes.get('white', True)
        white = None if wv is False else hx('#f4f4f4' if wv is True else wv)
        if style in ('front', 'big'):
            fx, fy, fw, fh = faces['front']
            row = min(eye_row, fh - 1)
            if style == 'big' and fw >= 6:
                xl = 1 if fw >= 8 else 0
                for (x0, px) in ((xl, xl + 1), (fw - 2 - xl, fw - 2 - xl)):
                    for dx in (0, 1):
                        for dy in (0, 1):
                            put(img, fx + x0 + dx, fy + row + dy, ecol)
                    put(img, fx + px, fy + row + 1, DARK)
            elif fw >= 6:
                xl = (fw - 6) // 2
                put(img, fx + xl, fy + row, white or ecol)
                put(img, fx + xl + 1, fy + row, ecol)
                put(img, fx + fw - 2 - xl, fy + row, ecol)
                put(img, fx + fw - 1 - xl, fy + row, white or ecol)
            elif fw >= 3:
                xl = 0 if fw <= 4 else 1
                put(img, fx + xl, fy + row, ecol)
                put(img, fx + fw - 1 - xl, fy + row, ecol)
            else:
                put(img, fx, fy + row, ecol)
        elif style == 'side':
            for fname, col_i in (('left', 'L'), ('right', 'R')):
                fx, fy, fw, fh = faces[fname]
                row = min(max(0, fh // 3), fh - 1)
                if fw >= 2:
                    ex = fw - 2 if col_i == 'L' else 1
                    put(img, fx + ex, fy + row, ecol)
                    if white and fw >= 4:
                        put(img, fx + (ex - 1 if col_i == 'L' else ex + 1), fy + row, white)
                else:
                    put(img, fx, fy + row, ecol)

    if paint.get('nose'):
        fx, fy, fw, fh = faces['front']
        row = min(fh // 2, fh - 1)
        nose = (28, 20, 18)
        if fw >= 5:
            put(img, fx + 1, fy + row, nose)
            put(img, fx + fw - 2, fy + row, nose)
        elif fw == 4:
            put(img, fx + 1, fy + row, nose)
            put(img, fx + 2, fy + row, nose)
        elif fw == 3:
            put(img, fx, fy + row, nose)
            put(img, fx + 2, fy + row, nose)
        else:
            put(img, fx, fy + row, nose)


def build_texture(model, seed):
    """Devuelve (imagen, W, H) y rellena el campo 'uv' de cada pieza."""
    rects = {}
    for p in model.parts:
        if p['uvkey'] == p['name']:
            rects[p['uvkey']] = rect_size(p['box'][3], p['box'][4], p['box'][5])
    W, H, pos = pack(rects)
    img = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    for p in model.parts:
        p['uv'] = list(pos[p['uvkey']])
        if p['uvkey'] == p['name']:
            _, _, _, w, h, d = p['box']
            paint_part(img, p['uv'][0], p['uv'][1], w, h, d, p['paint'], seed + model.idx[p['name']])
    return img, W, H
