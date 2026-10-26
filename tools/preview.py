# -*- coding: utf-8 -*-
"""Renderiza cada modelo (caras con el color medio de su textura) para revisar formas y proporciones."""
import json
import math
import os
import sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ASSETS = os.path.join(ROOT, 'src/main/resources/assets/animalmod')


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def rot_zyx(rx, ry, rz):
    cx, sx, cy, sy, cz, sz = math.cos(rx), math.sin(rx), math.cos(ry), math.sin(ry), math.cos(rz), math.sin(rz)
    X = [[1, 0, 0], [0, cx, -sx], [0, sx, cx]]
    Y = [[cy, 0, sy], [0, 1, 0], [-sy, 0, -cy * 0 + cy]]
    Y = [[cy, 0, sy], [0, 1, 0], [-sy, 0, cy]]
    Z = [[cz, -sz, 0], [sz, cz, 0], [0, 0, 1]]
    return matmul(Z, matmul(Y, X))


def apply(R, v):
    return [sum(R[i][k] * v[k] for k in range(3)) for i in range(3)]


def avg(img, x, y, w, h):
    px, n = [0, 0, 0], 0
    for j in range(int(h)):
        for i in range(int(w)):
            r, g, b, a = img.getpixel((int(x) + i, int(y) + j))
            if a > 0:
                px[0] += r; px[1] += g; px[2] += b; n += 1
    return tuple(int(c / n) for c in px) if n else (200, 0, 200)


def render(animal_id, size=300, yaw=-38, pitch=24, scale=None):
    model = json.load(open(os.path.join(ASSETS, 'animal_models/%s.json' % animal_id)))
    img = Image.open(os.path.join(ASSETS, 'textures/entity/%s.png' % animal_id)).convert('RGBA')
    world = {}
    faces = []
    th, ph = math.radians(yaw), math.radians(pitch)
    for p in model['parts']:
        R = rot_zyx(*p['rot'])
        if p['parent']:
            PR, PT = world[p['parent']]
            R = matmul(PR, R)
            T = [PT[i] + apply(PR, p['pivot'])[i] for i in range(3)]
        else:
            T = list(p['pivot'])
        world[p['name']] = (R, T)
        ox, oy, oz, w, h, d = p['box']
        u, v = p['uv']
        regions = {
            'top': (u + d, v, w, d), 'bottom': (u + d + w, v, w, d), 'left': (u, v + d, d, h),
            'front': (u + d, v + d, w, h), 'right': (u + d + w, v + d, d, h), 'back': (u + 2 * d + w, v + d, w, h)}
        # (nombre, normal local, esquinas)
        x0, x1, y0, y1, z0, z1 = ox, ox + w, oy, oy + h, oz, oz + d
        defs = {
            'top': ((0, -1, 0), [(x0, y0, z0), (x1, y0, z0), (x1, y0, z1), (x0, y0, z1)]),
            'bottom': ((0, 1, 0), [(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)]),
            'left': ((-1, 0, 0), [(x0, y0, z0), (x0, y0, z1), (x0, y1, z1), (x0, y1, z0)]),
            'right': ((1, 0, 0), [(x1, y0, z0), (x1, y0, z1), (x1, y1, z1), (x1, y1, z0)]),
            'front': ((0, 0, -1), [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0)]),
            'back': ((0, 0, 1), [(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)])}
        for name, (nl, corners) in defs.items():
            col = avg(img, *regions[name])
            wc = [[T[i] + apply(R, c)[i] for i in range(3)] for c in corners]
            nw = apply(R, nl)
            faces.append((name, nw, wc, col))

    def proj(pt):
        X, Y, Z = pt[0], -pt[1], -pt[2]
        x2 = X * math.cos(th) + Z * math.sin(th)
        z2 = -X * math.sin(th) + Z * math.cos(th)
        y3 = Y * math.cos(ph) - z2 * math.sin(ph)
        dep = z2 * math.cos(ph) + Y * math.sin(ph)
        return x2, y3, dep

    def pn(n):
        return proj((n[0], n[1], n[2]))

    allp = [proj(c) for f in faces for c in f[2]]
    minx, maxx = min(p[0] for p in allp), max(p[0] for p in allp)
    miny, maxy = min(p[1] for p in allp), max(p[1] for p in allp)
    sc = scale or (size * 0.84) / max(maxx - minx, maxy - miny, 1)
    out = Image.new('RGBA', (size, size), (214, 232, 247, 255))
    dr = ImageDraw.Draw(out)
    dr.rectangle([0, size * 0.80, size, size], fill=(120, 168, 92, 255))
    cx, cy = (minx + maxx) / 2, (miny + maxy) / 2
    draw = []
    for name, nw, wc, col in faces:
        n = pn(nw)
        o = pn((0, 0, 0))
        nd = n[2] - o[2]
        if nd <= 0:
            continue
        pts = [proj(c) for c in wc]
        depth = sum(p[2] for p in pts) / 4
        light = 0.62 + 0.38 * max(0.0, (n[1] - o[1]) * 0.6 + nd * 0.7)
        draw.append((depth, [(size / 2 + (p[0] - cx) * sc, size * 0.5 - (p[1] - cy) * sc) for p in pts],
                     tuple(min(255, int(c * light)) for c in col)))
    for depth, poly, col in sorted(draw, key=lambda t: t[0]):
        dr.polygon(poly, fill=col + (255,), outline=tuple(int(c * 0.6) for c in col) + (255,))
    return out


def sheet(ids, path, cols=5, size=300, yaw=-38):
    rows = (len(ids) + cols - 1) // cols
    S = Image.new('RGBA', (cols * size, rows * size), (255, 255, 255, 255))
    for i, aid in enumerate(ids):
        im = render(aid, size, yaw=yaw)
        d = ImageDraw.Draw(im)
        d.text((6, 6), aid, fill=(0, 0, 0, 255))
        S.paste(im, ((i % cols) * size, (i // cols) * size))
    S.convert('RGB').save(path)


if __name__ == '__main__':
    animals = json.load(open(os.path.join(ROOT, 'src/main/resources/animals.json')))
    ids = [a['id'] for a in animals]
    out = os.path.join(ROOT, 'previews')
    os.makedirs(out, exist_ok=True)
    for k in range(0, len(ids), 10):
        sheet(ids[k:k + 10], os.path.join(out, 'sheet_%d.png' % (k // 10 + 1)))
    print('ok', len(ids))
