# -*- coding: utf-8 -*-
"""Núcleo del generador: utilidades de color, modelo por cajas y helpers de animación."""
import math


def r2(v):
    return round(float(v), 2)


def hx(c):
    c = c.lstrip('#')
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def clamp8(v):
    return max(0, min(255, int(round(v))))


def shade(c, f):
    return tuple(clamp8(v * f) for v in c)


def mix(a, b, t):
    return tuple(clamp8(a[i] * (1 - t) + b[i] * t) for i in range(3))


def color_int(c):
    r, g, b = hx(c)
    return (r << 16) | (g << 8) | b


def A(kind, axis='x', amp=1.0, speed=0.0, phase=0.0, gate=None):
    """Animación de una pieza. Tipos: look, swing, wave, hop, pose.
    axis: x/y/z = rotación (pitch/yaw/roll); px/py/pz = desplazamiento del pivote.
    gate: always, moving, idle, air, ground, water, swim."""
    d = {'type': kind, 'axis': axis, 'amp': r2(amp), 'speed': r2(speed), 'phase': r2(phase)}
    if gate:
        d['gate'] = gate
    return d


class Model:
    """Lista de piezas (cajas). Los pivotes son relativos al padre (o absolutos si no hay padre).
    Convención vanilla: Y hacia abajo, suelo en y=24, el frente del animal es -Z."""

    def __init__(self):
        self.parts = []
        self.idx = {}

    def add(self, name, parent, pivot, box, color, rot=(0, 0, 0), pats=(), anims=(),
            eyes=None, nose=False, noise=0.06, mirror=False, uvkey=None):
        assert name not in self.idx, 'pieza duplicada: ' + name
        ox, oy, oz, w, h, d = box
        for v in (w, h, d):
            assert float(v).is_integer() and v > 0, (name, box)
        part = dict(
            name=name, parent=parent,
            pivot=[r2(v) for v in pivot], rot=[r2(v) for v in rot],
            box=[r2(ox), r2(oy), r2(oz), int(w), int(h), int(d)],
            mirror=mirror, uvkey=uvkey or name, anims=list(anims),
            paint=dict(color=color, pats=list(pats), eyes=eyes, nose=nose, noise=noise))
        self.idx[name] = len(self.parts)
        self.parts.append(part)
        return part

    def get(self, name):
        return self.parts[self.idx[name]]

    def bounds(self):
        """Caja envolvente aproximada (sin rotaciones) en píxeles."""
        absp = {}
        xs, ys, zs = [], [], []
        for p in self.parts:
            par = absp[p['parent']] if p['parent'] else (0, 0, 0)
            a = (par[0] + p['pivot'][0], par[1] + p['pivot'][1], par[2] + p['pivot'][2])
            absp[p['name']] = a
            ox, oy, oz, w, h, d = p['box']
            xs += [a[0] + ox, a[0] + ox + w]
            ys += [a[1] + oy, a[1] + oy + h]
            zs += [a[2] + oz, a[2] + oz + d]
        return min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)


def pair(m, name, parent, pivot, box, color, rot=(0, 0, 0), pats=(), anims=None,
         eyes=None, nose=False, noise=0.06):
    """Crea una pieza derecha (+x, sufijo _r) y su espejo izquierdo (-x, sufijo _l).
    `anims` puede ser una lista o una función f(lado) con lado=+1/-1.
    `parent` puede ser una tupla (padre_r, padre_l)."""
    pr, pl = parent if isinstance(parent, tuple) else (parent, parent)

    def an(s):
        return list(anims(s)) if callable(anims) else list(anims or [])

    ox, oy, oz, w, h, d = box
    m.add(name + '_r', pr, pivot, box, color, rot, pats, an(1), eyes, nose, noise)
    m.add(name + '_l', pl, (-pivot[0], pivot[1], pivot[2]), (-(ox + w), oy, oz, w, h, d), color,
          (rot[0], -rot[1], -rot[2]), pats, an(-1), eyes, nose, noise,
          mirror=True, uvkey=name + '_r')


ANIMALS = []


def animal(id, es, en, kind, habitat, egg, hp=10, speed=0.22, temper='passive', attack=2,
           food='minecraft:wheat', drop=None, sound='cow', weight=8, group=(2, 4), scale=1.0,
           fly=0.4, water='water_ambient', seed=None):
    """Decorador que registra un animal. kind: land | flying | water."""
    def deco(fn):
        ANIMALS.append(dict(id=id, es=es, en=en, kind=kind, habitat=habitat, egg=egg, hp=hp,
                            speed=speed, temper=temper, attack=attack, food=food, drop=drop,
                            sound=sound, weight=weight, group=group, scale=scale, fly=fly,
                            water=water, seed=seed or sum(ord(c) for c in id), fn=fn))
        return fn
    return deco


def ground(m, y=24.0):
    """Baja/sube las piezas raíz para que el punto más bajo del modelo quede en y=24 (suelo)."""
    lo = m.bounds()[3]
    for p in m.parts:
        if p['parent'] is None:
            p['pivot'][1] = r2(p['pivot'][1] + y - lo)
