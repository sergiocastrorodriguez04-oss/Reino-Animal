# -*- coding: utf-8 -*-
"""Plantillas de cuerpo reutilizables. Todas las medidas son píxeles (16 px = 1 bloque)."""
import math
from core import A, pair

PI = math.pi


def quad(m, col, body, leg, head, neck=None, gait=1.1, splay=0, head_dy=0.0, head_dz=None,
         leg_pats=(), body_pats=(), head_pats=(), eyes=None, leg_in=0.0, breathe=True):
    """Cuadrúpedo. body=(ancho,alto,largo) leg=(grosor,largo) head=(ancho,alto,fondo).
    La cabeza pivota en el centro de su cara trasera y mira con A('look')."""
    bw, bh, bl = body
    lt, ll = leg
    hw, hh, hd = head
    cb = col['body']
    cl = col.get('leg', cb)
    ch = col.get('head', cb)
    by = 24 - ll - bh
    m.add('body', None, (0, by, 0), (-bw / 2, 0, -bl / 2, bw, bh, bl), cb, pats=body_pats,
          anims=[A('wave', 'py', 0.25, 0.09)] if breathe else [])
    fx = bw / 2 - lt / 2 - leg_in
    lbox = (-lt / 2, 0, -lt / 2, lt, ll, lt)
    pair(m, 'leg_f', 'body', (fx, bh, -bl / 2 + lt / 2), lbox, cl, rot=(0, 0, -splay), pats=leg_pats,
         anims=lambda s: [A('swing', 'x', gait, phase=0 if s > 0 else PI)])
    pair(m, 'leg_b', 'body', (fx, bh, bl / 2 - lt / 2), lbox, cl, rot=(0, 0, -splay), pats=leg_pats,
         anims=lambda s: [A('swing', 'x', gait, phase=PI if s > 0 else 0)])
    if neck:
        nw, nh, nd = neck
        m.add('neck', 'body', (0, 2, -bl / 2 + nd / 2), (-nw / 2, -nh, -nd / 2, nw, nh, nd),
              col.get('neck', cb), pats=body_pats)
        hy = 2 - nh + hh / 2 - 1 + head_dy
        hz = -bl / 2 + nd + (0.0 if head_dz is None else head_dz)
    else:
        hy = hh / 2 + head_dy
        hz = -bl / 2 + (1.0 if head_dz is None else head_dz)
    m.add('head', 'body', (0, hy, hz), (-hw / 2, -hh / 2, -hd, hw, hh, hd), ch, pats=head_pats,
          eyes=eyes if eyes is not None else dict(style='front'), anims=[A('look')])
    return dict(bw=bw, bh=bh, bl=bl, by=by, hw=hw, hh=hh, hd=hd, ll=ll, lt=lt, neck=neck)


def snout(m, ctx, size, color, dy=0.5, nose=True, pats=(), name='snout', parent='head', anims=()):
    w, h, d = size
    m.add(name, parent, (0, dy, -ctx['hd'] + 1), (-w / 2, -h / 2, -d, w, h, d), color,
          pats=pats, nose=nose, anims=anims)


def ears(m, ctx, size, color, inset=0.0, tilt=0, dy=0.0, dz=None, d=1, pats=(), wiggle=0.07,
         name='ear', parent='head'):
    w, h = size
    z = -ctx['hd'] / 2 if dz is None else dz
    pair(m, name, parent, (ctx['hw'] / 2 - w / 2 - inset, -ctx['hh'] / 2 + dy, z),
         (-w / 2, -h, -d / 2, w, h, d), color, rot=(0, 0, tilt), pats=pats,
         anims=lambda s: [A('wave', 'z', wiggle * s, 0.19, phase=0 if s > 0 else 1.7)])


def tail(m, ctx, size, mode='back', color='#888888', rot=(0, 0, 0), pats=(), pivot=None,
         wag=0.25, seg2=None, parent='body', name='tail'):
    """mode back: largo en +Z; down: cuelga; up: sube. seg2=(w,h,d,color,rot) segunda pieza."""
    w, h, d = size
    bl = ctx['bl']
    if mode == 'back':
        pv, box, axis = pivot or (0, 1.5, bl / 2 - 0.5), (-w / 2, -h / 2, 0, w, h, d), 'y'
        end = (0, 0, d - 1)
    elif mode == 'down':
        pv, box, axis = pivot or (0, 1.5, bl / 2 - 0.5), (-w / 2, 0, -d / 2, w, h, d), 'z'
        end = (0, h - 1, 0)
    else:
        pv, box, axis = pivot or (0, 2, bl / 2 - 0.5), (-w / 2, -h, -d / 2, w, h, d), 'z'
        end = (0, -h + 1, 0)
    m.add(name, parent, pv, box, color, rot, pats, anims=[A('wave', axis, wag, 0.17)])
    if seg2:
        w2, h2, d2, c2, r2_ = seg2
        if mode == 'back':
            b2 = (-w2 / 2, -h2 / 2, 0, w2, h2, d2)
        elif mode == 'down':
            b2 = (-w2 / 2, 0, -d2 / 2, w2, h2, d2)
        else:
            b2 = (-w2 / 2, -h2, -d2 / 2, w2, h2, d2)
        m.add(name + '2', name, end, b2, c2, r2_, anims=[A('wave', axis, wag * 1.4, 0.17, phase=0.9)])


def hop(m, name='body', amp=2.5):
    m.get(name)['anims'].append(A('hop', 'py', amp))


def biped(m, col, torso, leg, arm, head, lean=0.0, hop_=False, gait=1.0, arm_swing=0.9,
          torso_pats=(), head_pats=(), leg_pats=(), arm_pats=(), eyes=None, arm_rot=0.0):
    """Bípedo erguido. La torso pivota en la cadera (la caja crece hacia arriba)."""
    tw, th, td = torso
    lw, lh, ld = leg
    aw, ah, ad = arm
    hw, hh, hd = head
    ct = col['torso']
    cl = col.get('leg', ct)
    ca = col.get('arm', ct)
    chd = col.get('head', ct)
    hip = 24 - lh
    ta = [A('wave', 'py', 0.2, 0.09)]
    if hop_:
        ta.append(A('hop', 'py', 3.0))
    m.add('torso', None, (0, hip, 0), (-tw / 2, -th, -td / 2, tw, th, td), ct, rot=(lean, 0, 0),
          pats=torso_pats, anims=ta)
    lx = max(lw / 2, tw / 2 - lw / 2)
    pair(m, 'leg', None, (lx, hip, 0), (-lw / 2, 0, -ld / 2, lw, lh, ld), cl, pats=leg_pats,
         anims=(lambda s: [A('hop', 'py', 3.0)]) if hop_ else
         (lambda s: [A('swing', 'x', gait, phase=0 if s > 0 else PI)]))
    pair(m, 'arm', 'torso', (tw / 2 + aw / 2, -th + 2, 0), (-aw / 2, -1, -ad / 2, aw, ah, ad), ca,
         rot=(arm_rot - lean, 0, 0), pats=arm_pats,
         anims=lambda s: [A('swing', 'x', arm_swing, phase=PI if s > 0 else 0)])
    m.add('head', 'torso', (0, -th, 0), (-hw / 2, -hh, -hd / 2, hw, hh, hd), chd, rot=(-lean * 0.7, 0, 0),
          pats=head_pats, eyes=eyes if eyes is not None else dict(style='front'), anims=[A('look')])
    return dict(tw=tw, th=th, td=td, hw=hw, hh=hh, hd=hd, hip=hip)


def bird(m, col, body, leg, head, wing, neck=None, head_off=None, fly=False, tail_=None,
         beak=None, beak_rot=0.0, eyes=None, body_pats=(), head_pats=(), wing_pats=(), gait=1.3,
         leg_t=1):
    """Ave. body=(w,h,l) leg=(grosor,largo) head=(w,h,d) wing=(alto,largo) beak=(w,h,d,color)."""
    bw, bh, bl = body
    ll = leg[1]
    hw, hh, hd = head
    by = 24 - ll - bh
    m.add('body', None, (0, by, 0), (-bw / 2, 0, -bl / 2, bw, bh, bl), col['body'], pats=body_pats,
          anims=[A('wave', 'py', 0.3, 0.1)] + ([A('wave', 'py', 0.8, 0.35, gate='air')] if fly else []))
    pair(m, 'leg', 'body', (bw / 4 + 0.5, bh, 0), (-leg_t / 2, 0, -leg_t / 2, leg_t, ll, leg_t),
         col.get('leg', col['body']),
         anims=lambda s: [A('swing', 'x', gait, phase=0 if s > 0 else PI)] +
         ([A('pose', 'x', 0.9, gate='air')] if fly else []))
    if neck:
        nw, nh, nd = neck
        nz = -bl / 2 + nd / 2 + 0.5
        m.add('neck', 'body', (0, 1, nz), (-nw / 2, -nh, -nd / 2, nw, nh, nd), col.get('neck', col['body']))
        hoff = (1 - nh - hh / 2 + 1, nz)
    else:
        hoff = head_off
    m.add('head', 'body', (0, hoff[0], hoff[1]), (-hw / 2, -hh / 2, -hd / 2, hw, hh, hd), col['head'],
          pats=head_pats, eyes=eyes if eyes is not None else dict(style='side'), anims=[A('look')])
    if beak:
        bw_, bh_, bd_, bc = beak[:4]
        extra = beak[4] if len(beak) > 4 else ()
        m.add('beak', 'head', (0, 0.5, -hd / 2 + 0.5), (-bw_ / 2, -bh_ / 2, -bd_, bw_, bh_, bd_), bc,
              rot=(beak_rot, 0, 0), pats=extra, nose=False)
    wh, wl = wing
    if fly:
        wa = lambda s: [A('pose', 'z', -1.4 * s, gate='air'), A('wave', 'z', -0.55 * s, 1.1, gate='air'),
                        A('wave', 'z', -0.04 * s, 0.3, gate='ground')]
    else:
        wa = lambda s: [A('wave', 'z', -0.04 * s, 0.3)]
    pair(m, 'wing', 'body', (bw / 2, 1, 0), (0, 0, -wl / 2, 1, wh, wl), col.get('wing', col['body']),
         pats=wing_pats, anims=wa)
    if tail_:
        tw, th, td, tc, trot = tail_
        tail(m, dict(bl=bl), (tw, th, td), 'back', tc, rot=(trot, 0, 0), wag=0.12)
    return dict(bl=bl, by=by, hw=hw, hh=hh, hd=hd)
