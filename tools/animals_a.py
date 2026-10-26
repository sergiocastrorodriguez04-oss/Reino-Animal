# -*- coding: utf-8 -*-
from core import *
from archetypes import *


@animal('deer', 'Ciervo', 'Deer', 'land', 'forest', egg=('#a5743f', '#ead9b8'), hp=16, speed=0.27,
        food='minecraft:wheat', drop='minecraft:leather', sound='horse', weight=10, group=(2, 5))
def deer(m):
    c = dict(body='#a5743f', leg='#8c5f32', head='#a5743f', neck='#a5743f')
    k = quad(m, c, (7, 8, 14), (3, 11), (5, 5, 6), neck=(4, 8, 4), gait=1.2,
             leg_pats=[('socks', '#4a3320', 3)], body_pats=[('belly', '#ead9b8', 0.3), ('spots', '#ead9b8', 0.04)],
             head_pats=[('belly', '#ead9b8', 0.3)], eyes=dict(style='side'))
    snout(m, k, (3, 3, 3), '#d8bf94', dy=1.5)
    ears(m, k, (2, 3), '#8c5f32', inset=-1, tilt=0.6, dz=-1.5)
    pair(m, 'antler', 'head', (1.2, -k['hh'] / 2, -2.5), (-0.5, -6, -0.5, 1, 6, 1), '#d8c9a0', rot=(0, 0, 0.25))
    pair(m, 'antlerb', 'head', (1.6, -k['hh'] / 2 - 3, -2.5), (0, -0.5, -0.5, 3, 1, 1), '#d8c9a0', rot=(0, 0, -0.3))
    tail(m, k, (2, 3, 2), 'down', '#ead9b8', rot=(0.3, 0, 0))


@animal('moose', 'Alce', 'Moose', 'land', 'taiga', egg=('#4b3624', '#b08a5a'), hp=26, speed=0.22,
        temper='neutral', attack=5, food='minecraft:sweet_berries', drop='minecraft:leather', sound='horse',
        weight=6, group=(1, 2))
def moose(m):
    c = dict(body='#4b3624', leg='#7a6045', head='#5a412b', neck='#4b3624')
    k = quad(m, c, (10, 12, 18), (4, 14), (6, 7, 8), neck=(5, 8, 5), gait=1.0,
             leg_pats=[('socks', '#2f2118', 2)], body_pats=[('speckle', 0.12)], head_pats=[('speckle', 0.1)],
             eyes=dict(style='side'))
    snout(m, k, (5, 5, 4), '#6a4d33', dy=1.5)
    ears(m, k, (2, 3), '#4b3624', inset=-1, tilt=0.7, dz=-2)
    pair(m, 'antler', 'head', (2.5, -k['hh'] / 2, -2), (0, -1, -3, 7, 1, 6), '#8a6b43', rot=(0, 0, -0.35))
    m.add('beard', 'head', (0, k['hh'] / 2 - 1, -3), (-1, 0, -0.5, 2, 4, 1), '#3a2a1c')
    m.add('hump', 'body', (0, 0, -4), (-3, -2, -3, 6, 2, 6), '#4b3624')
    tail(m, k, (2, 2, 2), 'down', '#4b3624')


@animal('elephant', 'Elefante', 'Elephant', 'land', 'savanna', egg=('#8b8d93', '#efe6cf'), hp=44, speed=0.2,
        temper='neutral', attack=8, food='minecraft:sugar_cane', drop='minecraft:leather', sound='cow',
        weight=3, group=(1, 3))
def elephant(m):
    c = dict(body='#8b8d93', leg='#85878d', head='#8b8d93')
    k = quad(m, c, (14, 15, 22), (5, 14), (12, 13, 10), gait=0.8,
             leg_pats=[('socks', '#c9c9cf', 2)], body_pats=[('speckle', 0.1)], head_pats=[('speckle', 0.08)])
    ring = [('rings', '#7a7c82', 1, 3)]
    m.add('trunk', 'head', (0, 2, -9), (-2, 0, -2, 4, 8, 4), '#85878d', pats=ring, anims=[A('wave', 'x', 0.15, 0.09)])
    m.add('trunk2', 'trunk', (0, 8, 0), (-1.5, 0, -1.5, 3, 7, 3), '#85878d', rot=(-0.45, 0, 0), pats=ring,
          anims=[A('wave', 'x', 0.25, 0.09, phase=0.8)])
    pair(m, 'tusk', 'head', (4, 4, -9), (-0.5, 0, -4, 1, 1, 4), '#efe6cf', rot=(0.45, 0, 0))
    pair(m, 'ear', 'head', (5.5, -5, -6), (0, 0, 0, 1, 10, 7), '#7e8087', rot=(0, 0.5, 0),
         anims=lambda s: [A('wave', 'y', 0.12 * s, 0.14)])
    tail(m, k, (2, 10, 2), 'down', '#85878d', rot=(0.1, 0, 0), seg2=(3, 3, 3, '#5d5f66', (0, 0, 0)))


@animal('giraffe', 'Jirafa', 'Giraffe', 'land', 'savanna', egg=('#d9a441', '#7b4a1e'), hp=26, speed=0.24,
        food='minecraft:wheat', drop='minecraft:leather', sound='horse', weight=5, group=(2, 4))
def giraffe(m):
    sp = ('spots', '#7b4a1e', 0.1, 2)
    c = dict(body='#d9a441', leg='#d9a441', head='#d9a441', neck='#d9a441')
    k = quad(m, c, (7, 9, 13), (3, 15), (5, 5, 7), neck=(4, 16, 4), gait=1.0,
             leg_pats=[('spots', '#7b4a1e', 0.07, 1), ('socks', '#e8d9a6', 3)],
             body_pats=[sp], head_pats=[('speckle', 0.1)], eyes=dict(style='side'))
    m.get('neck')['paint']['pats'] = [sp]
    snout(m, k, (3, 3, 2), '#e8cf8e', dy=1.2)
    pair(m, 'horn', 'head', (1.2, -k['hh'] / 2, -3), (-0.5, -3, -0.5, 1, 3, 1), '#7b4a1e')
    pair(m, 'knob', 'head', (1.2, -k['hh'] / 2 - 3, -3), (-1, -1, -1, 2, 1, 2), '#3a2414')
    ears(m, k, (2, 2), '#d9a441', inset=-1.5, tilt=1.0, dz=-1.5)
    tail(m, k, (1, 9, 1), 'down', '#d9a441', seg2=(2, 3, 2, '#3a2414', (0, 0, 0)))


@animal('lion', 'León', 'Lion', 'land', 'savanna', egg=('#d4a050', '#6b3d14'), hp=22, speed=0.28,
        temper='hostile', attack=6, food='minecraft:beef', drop='minecraft:beef', sound='cat', weight=4,
        group=(1, 3))
def lion(m):
    c = dict(body='#d4a050', leg='#d4a050', head='#d4a050')
    k = quad(m, c, (8, 8, 14), (3, 8), (6, 6, 6), gait=1.1, leg_pats=[('socks', '#c08a3a', 2)],
             body_pats=[('belly', '#ecd5a0', 0.3)], head_pats=[('belly', '#ecd5a0', 0.25)])
    m.add('mane', 'head', (0, 0, -1), (-5, -5, -4, 10, 10, 5), '#6b3d14', pats=[('speckle', 0.18)])
    snout(m, k, (4, 3, 2), '#ecd5a0', dy=1.5)
    ears(m, k, (2, 2), '#c08a3a', inset=-1, dz=-0.5)
    tail(m, k, (1, 9, 1), 'down', '#d4a050', rot=(0.35, 0, 0), seg2=(2, 3, 2, '#6b3d14', (0, 0, 0)))


@animal('tiger', 'Tigre', 'Tiger', 'land', 'jungle', egg=('#e08a2c', '#1f1a17'), hp=22, speed=0.29,
        temper='hostile', attack=7, food='minecraft:beef', drop='minecraft:beef', sound='cat', weight=4,
        group=(1, 2))
def tiger(m):
    st = ('stripes', '#1f1a17', 4, 2)
    c = dict(body='#e08a2c', leg='#e08a2c', head='#e08a2c')
    k = quad(m, c, (8, 8, 14), (3, 8), (7, 6, 6), gait=1.1, leg_pats=[st, ('socks', '#f4efe6', 2)],
             body_pats=[st, ('belly', '#f4efe6', 0.3)], head_pats=[('stripes', '#1f1a17', 3, 1), ('belly', '#f4efe6', 0.25)])
    snout(m, k, (4, 3, 2), '#f4efe6', dy=1.5)
    ears(m, k, (2, 2), '#e08a2c', inset=-1, dz=-0.5, pats=[('tip', '#1f1a17', 1)])
    tail(m, k, (1, 10, 1), 'down', '#e08a2c', rot=(0.3, 0, 0), pats=[('bands', '#1f1a17', 2, 'j')],
         seg2=(2, 2, 2, '#1f1a17', (0, 0, 0)))


@animal('zebra', 'Cebra', 'Zebra', 'land', 'savanna', egg=('#f1f1f1', '#1c1c1c'), hp=18, speed=0.3,
        food='minecraft:wheat', drop='minecraft:leather', sound='horse', weight=8, group=(3, 6))
def zebra(m):
    st = ('stripes', '#1c1c1c', 3, 2)
    c = dict(body='#f1f1f1', leg='#f1f1f1', head='#f1f1f1', neck='#f1f1f1')
    k = quad(m, c, (7, 9, 15), (3, 11), (5, 5, 9), neck=(4, 9, 5), gait=1.2, leg_pats=[st],
             body_pats=[st], head_pats=[('stripes', '#1c1c1c', 3, 1)], eyes=dict(style='side'))
    m.get('neck')['paint']['pats'] = [st]
    snout(m, k, (4, 4, 2), '#2a2a2e', dy=1.0)
    ears(m, k, (2, 3), '#1c1c1c', inset=-0.5, dz=-1.5)
    m.add('mane', 'neck', (0, 0, 2), (-0.5, -9, -0.5, 1, 9, 2), '#1c1c1c')
    tail(m, k, (1, 8, 2), 'down', '#1c1c1c', rot=(0.15, 0, 0))


@animal('hippo', 'Hipopótamo', 'Hippo', 'land', 'swamp', egg=('#8a7f8e', '#c9a09a'), hp=34, speed=0.18,
        temper='neutral', attack=8, food='minecraft:melon_slice', drop='minecraft:beef', sound='cow',
        weight=3, group=(1, 3))
def hippo(m):
    c = dict(body='#8a7f8e', leg='#8a7f8e', head='#8a7f8e')
    k = quad(m, c, (14, 10, 20), (5, 5), (11, 8, 8), gait=0.9, head_dy=1.0, head_dz=1,
             body_pats=[('belly', '#c9a09a', 0.3), ('speckle', 0.08)], head_pats=[('speckle', 0.08)])
    snout(m, k, (11, 5, 3), '#b28f8f', dy=2.5, nose=True)
    pair(m, 'eye', 'head', (3, -4.5, -3), (-1, -1, -1, 2, 1, 2), '#8a7f8e', eyes=dict(style='front', white=False))
    pair(m, 'nostril', 'head', (2.5, -1, -hippo_hd(k)), (-0.5, -1, -1, 1, 1, 1), '#6f6573')
    ears(m, k, (2, 2), '#8a7f8e', inset=1, dz=-1.5)
    tail(m, k, (2, 3, 2), 'down', '#8a7f8e')


def hippo_hd(k):
    return k['hd'] - 1


@animal('rhino', 'Rinoceronte', 'Rhino', 'land', 'savanna', egg=('#8f9296', '#b9b2a3'), hp=34, speed=0.2,
        temper='neutral', attack=9, food='minecraft:wheat', drop='minecraft:leather', sound='cow',
        weight=3, group=(1, 2))
def rhino(m):
    c = dict(body='#8f9296', leg='#85888c', head='#8f9296')
    k = quad(m, c, (11, 11, 18), (4, 8), (7, 8, 9), gait=0.9, head_dy=2,
             body_pats=[('bands', '#838689', 3), ('speckle', 0.06)], head_pats=[('speckle', 0.06)],
             leg_pats=[('socks', '#7a7d81', 2)])
    m.add('horn', 'head', (0, -hh_of(k) / 2 + 2, -k['hd'] + 1), (-1, -5, -1.5, 2, 5, 3), '#c9c2b0', rot=(-0.3, 0, 0))
    m.add('horn2', 'head', (0, -hh_of(k) / 2 + 1.5, -k['hd'] + 6), (-1, -3, -1, 2, 3, 2), '#c9c2b0')
    ears(m, k, (2, 3), '#85888c', inset=0, dz=-1.5)
    tail(m, k, (1, 7, 1), 'down', '#85888c', seg2=(2, 2, 2, '#4d4f52', (0, 0, 0)))


def hh_of(k):
    return k['hh']


@animal('kangaroo', 'Canguro', 'Kangaroo', 'land', 'savanna', egg=('#c98a5a', '#ecd2a8'), hp=16, speed=0.3,
        food='minecraft:carrot', drop='minecraft:rabbit', sound='rabbit', weight=7, group=(2, 4))
def kangaroo(m):
    c = dict(torso='#c98a5a', leg='#b6784a', arm='#c98a5a', head='#c98a5a')
    k = biped(m, c, (6, 10, 6), (3, 11, 5), (2, 5, 2), (5, 6, 5), lean=0.35, hop_=True,
              torso_pats=[('belly', '#ecd2a8', 0.5)], head_pats=[('belly', '#ecd2a8', 0.25)],
              leg_pats=[('socks', '#7e5232', 3)], arm_swing=0.3)
    m.add('muzzle', 'head', (0, -1.5, -3.5), (-1.5, -1.5, -3, 3, 3, 3), '#ecd2a8', nose=True)
    pair(m, 'ear', 'head', (1.5, -6, 0), (-1, -5, -0.5, 2, 5, 1), '#c98a5a', rot=(0, 0, 0.15),
         anims=lambda s: [A('wave', 'z', 0.08 * s, 0.15)])
    m.add('tail', 'torso', (0, -1.5, 3), (-1.5, -1.5, 0, 3, 3, 12), '#b6784a', rot=(-0.7, 0, 0),
          anims=[A('wave', 'y', 0.12, 0.17)])
    ground(m)


@animal('koala', 'Koala', 'Koala', 'land', 'forest', egg=('#8e8e96', '#d9d4cf'), hp=10, speed=0.14,
        food='minecraft:sweet_berries', drop='minecraft:string', sound='fox', weight=7, group=(1, 3))
def koala(m):
    c = dict(body='#8e8e96', leg='#85858d', head='#8e8e96')
    k = quad(m, c, (6, 6, 7), (2, 4), (6, 5, 5), gait=0.9, head_dy=0.5,
             body_pats=[('belly', '#d9d4cf', 0.35)], head_pats=[('belly', '#d9d4cf', 0.2)])
    snout(m, k, (2, 3, 1), '#1d1d22', dy=1, nose=False)
    pair(m, 'ear', 'head', (2.5, -2.5, -1.5), (-1.5, -2, -0.5, 3, 3, 1), '#a9a9b1',
         anims=lambda s: [A('wave', 'z', 0.06 * s, 0.17)])


@animal('raccoon', 'Mapache', 'Raccoon', 'land', 'forest', egg=('#8d8d8d', '#1a1a1a'), hp=10, speed=0.25,
        food='minecraft:sweet_berries', drop='minecraft:string', sound='fox', weight=8, group=(1, 3))
def raccoon(m):
    c = dict(body='#8d8d8d', leg='#4a4a4c', head='#a6a6a6')
    k = quad(m, c, (6, 5, 10), (2, 4), (5, 4, 4), gait=1.4, head_dy=0.5,
             body_pats=[('belly', '#bdbdbd', 0.3), ('speckle', 0.1)],
             head_pats=[('mask', '#1a1a1a'), ('speckle', 0.05)], eyes=dict(style='front', white=False))
    snout(m, k, (3, 2, 2), '#d2d2d2', dy=1)
    ears(m, k, (2, 2), '#8d8d8d', inset=0, dz=-1)
    tail(m, k, (3, 3, 9), 'back', '#8d8d8d', rot=(0.2, 0, 0), pats=[('rings', '#242424', 2, 4)], pivot=(0, 0, 5))


@animal('squirrel', 'Ardilla', 'Squirrel', 'land', 'forest', egg=('#b0662c', '#f0e0c0'), hp=6, speed=0.3,
        food='minecraft:wheat_seeds', drop='minecraft:string', sound='rabbit', weight=10, group=(1, 3))
def squirrel(m):
    c = dict(body='#b0662c', leg='#9a5622', head='#b0662c')
    k = quad(m, c, (4, 4, 7), (2, 3), (4, 4, 3), gait=1.5, head_dy=0.5, body_pats=[('belly', '#f0e0c0', 0.35)],
             head_pats=[('belly', '#f0e0c0', 0.25)])
    hop(m, 'body', 1.5)
    snout(m, k, (2, 2, 1), '#f0e0c0', dy=1)
    ears(m, k, (1, 2), '#9a5622', inset=0, dz=-0.5)
    tail(m, k, (3, 6, 3), 'up', '#b0662c', rot=(0.2, 0, 0), pivot=(0, 2, 3), wag=0.08,
         pats=[('speckle', 0.15)], seg2=(3, 3, 3, '#c97a3a', (0.7, 0, 0)))


@animal('hedgehog', 'Erizo', 'Hedgehog', 'land', 'forest', egg=('#4f3b2a', '#c8a888'), hp=8, speed=0.18,
        food='minecraft:sweet_berries', drop='minecraft:string', sound='fox', weight=8, group=(1, 2))
def hedgehog(m):
    c = dict(body='#c8a888', leg='#a98a6a', head='#c8a888')
    k = quad(m, c, (6, 4, 8), (2, 2), (4, 3, 4), gait=1.6, head_dy=1.0, head_dz=2, body_pats=[('speckle', 0.05)])
    m.add('spines', 'body', (0, 0.5, 1), (-3.5, -3, -4, 7, 4, 9), '#4f3b2a',
          pats=[('speckle', 0.3), ('spots', '#c8b79c', 0.12, 1)], noise=0.12)
    snout(m, k, (2, 2, 2), '#e1c9ac', dy=1)


@animal('capybara', 'Capibara', 'Capybara', 'land', 'swamp', egg=('#8a6a45', '#5b4429'), hp=14, speed=0.2,
        food='minecraft:melon_slice', drop='minecraft:leather', sound='pig', weight=7, group=(2, 5))
def capybara(m):
    c = dict(body='#8a6a45', leg='#775a39', head='#8a6a45')
    k = quad(m, c, (8, 8, 14), (3, 5), (6, 6, 6), gait=1.1, head_dy=1.0, body_pats=[('speckle', 0.1)],
             head_pats=[('speckle', 0.08)])
    snout(m, k, (4, 4, 2), '#775a39', dy=1.8)
    ears(m, k, (2, 2), '#775a39', inset=0, dz=-1)


@animal('sloth', 'Perezoso', 'Sloth', 'land', 'jungle', egg=('#9a8a72', '#3a2c20'), hp=12, speed=0.08,
        food='minecraft:glow_berries', drop='minecraft:string', sound='fox', weight=6, group=(1, 2))
def sloth(m):
    c = dict(body='#9a8a72', leg='#85755d', head='#b4a58d')
    k = quad(m, c, (6, 6, 10), (2, 7), (5, 5, 4), gait=0.6, head_dy=1.5,
             body_pats=[('speckle', 0.14)], leg_pats=[('socks', '#3a2c20', 2)],
             head_pats=[('mask', '#3a2c20')], eyes=dict(style='front', white=False))
    snout(m, k, (2, 2, 1), '#2a2018', dy=1.5, nose=False)
    m.get('body')['anims'].append(A('wave', 'z', 0.03, 0.06))


@animal('monkey', 'Mono', 'Monkey', 'land', 'jungle', egg=('#7a5230', '#e8c9a0'), hp=12, speed=0.3,
        food='minecraft:glow_berries', drop='minecraft:string', sound='parrot', weight=8, group=(2, 5))
def monkey(m):
    c = dict(body='#7a5230', leg='#6a4526', head='#7a5230')
    k = quad(m, c, (5, 6, 8), (2, 6), (5, 5, 5), gait=1.4, head_dy=0,
             body_pats=[('belly', '#c9a074', 0.3)], head_pats=[('frontpatch', '#e8c9a0', 1)])
    snout(m, k, (3, 2, 2), '#c9a074', dy=1.5)
    pair(m, 'ear', 'head', (3, 0, -2), (0, -1.5, -1, 1, 3, 2), '#e8c9a0')
    tail(m, k, (1, 10, 1), 'down', '#6a4526', rot=(0.7, 0, 0), wag=0.3, seg2=(1, 4, 1, '#6a4526', (-0.9, 0, 0)))
