# -*- coding: utf-8 -*-
from core import *
from archetypes import *


@animal('gorilla', 'Gorila', 'Gorilla', 'land', 'jungle', egg=('#2e2e33', '#6a6a72'), hp=30, speed=0.22,
        temper='neutral', attack=8, food='minecraft:melon_slice', drop='minecraft:leather', sound='polar_bear',
        weight=3, group=(1, 3))
def gorilla(m):
    c = dict(torso='#2e2e33', leg='#27272b', arm='#2e2e33', head='#26262a')
    biped(m, c, (10, 10, 6), (4, 7, 4), (4, 13, 4), (6, 6, 6), lean=0.3, gait=0.9, arm_swing=0.7,
          torso_pats=[('frontpatch', '#4a4a52', 1), ('speckle', 0.1)], head_pats=[('mask', '#15151a')],
          arm_pats=[('speckle', 0.1)], eyes=dict(style='front', white=False))
    m.add('brow', 'head', (0, -hh_g(), -2.2), (-3, -1, -1.5, 6, 1, 2), '#1c1c20')
    m.add('muzzle', 'head', (0, -2, -3.4), (-2, -1.5, -1.5, 4, 3, 2), '#3d3d44', nose=True)
    m.add('crest', 'head', (0, -6, 0), (-1.5, -2, -2, 3, 2, 4), '#26262a')
    ground(m)


def hh_g():
    return 4.5


@animal('brown_bear', 'Oso pardo', 'Brown Bear', 'land', 'taiga', egg=('#5b3a22', '#c9a074'), hp=30, speed=0.24,
        temper='neutral', attack=8, food='minecraft:salmon', drop='minecraft:beef', sound='polar_bear',
        weight=5, group=(1, 2))
def brown_bear(m):
    c = dict(body='#5b3a22', leg='#4f3119', head='#5b3a22')
    k = quad(m, c, (11, 10, 16), (4, 7), (7, 7, 6), gait=1.0, head_dy=0.5,
             body_pats=[('speckle', 0.1)], head_pats=[('speckle', 0.08)], leg_pats=[('socks', '#2f1c0e', 2)])
    m.add('hump', 'body', (0, 0, -3), (-3, -3, -3, 6, 3, 6), '#5b3a22')
    snout(m, k, (4, 3, 3), '#c9a074', dy=1.5)
    ears(m, k, (2, 2), '#4f3119', inset=0, dz=-1)
    tail(m, k, (2, 2, 1), 'down', '#4f3119')


@animal('red_panda', 'Panda rojo', 'Red Panda', 'land', 'mountain', egg=('#b9501e', '#f4e9dc'), hp=10,
        speed=0.24, food='minecraft:bamboo', drop='minecraft:bamboo', sound='fox', weight=6, group=(1, 2))
def red_panda(m):
    c = dict(body='#b9501e', leg='#2a1c16', head='#b9501e')
    k = quad(m, c, (5, 5, 10), (2, 5), (6, 5, 5), gait=1.3, head_dy=0.5,
             body_pats=[('belly', '#2a1c16', 0.35)], head_pats=[('frontpatch', '#f4e9dc', 1)])
    snout(m, k, (3, 2, 2), '#f4e9dc', dy=1.2)
    ears(m, k, (2, 2), '#b9501e', inset=0, dz=-1, pats=[('tip', '#f4e9dc', 1)])
    tail(m, k, (4, 4, 10), 'back', '#b9501e', rot=(0.25, 0, 0), pats=[('rings', '#7a2f10', 2, 4)], pivot=(0, 0, 5))


@animal('meerkat', 'Suricata', 'Meerkat', 'land', 'desert', egg=('#c9a674', '#8d6a3b'), hp=8, speed=0.26,
        food='minecraft:spider_eye', drop='minecraft:string', sound='fox', weight=8, group=(3, 6))
def meerkat(m):
    c = dict(torso='#c9a674', leg='#a98557', arm='#a98557', head='#dcc59b')
    biped(m, c, (4, 7, 3), (2, 4, 2), (1, 4, 1), (4, 4, 4), lean=0.0, gait=1.4, arm_swing=0.4,
          torso_pats=[('stripes', '#8d6a3b', 3, 1), ('belly', '#e8d8b8', 0.3)],
          head_pats=[('mask', '#3a2a20')], eyes=dict(style='front', white=False))
    m.add('snout', 'head', (0, -1.2, -2.5), (-1, -1, -1.5, 2, 2, 2), '#dcc59b', nose=True)
    pair(m, 'ear', 'head', (2, -3.5, 0), (-0.5, -1, -0.5, 1, 1, 1), '#3a2a20')
    m.add('tail', 'torso', (0, -1.5, 1.5), (-0.5, 0, -0.5, 1, 7, 1), '#a98557', rot=(0.5, 0, 0),
          anims=[A('wave', 'z', 0.2, 0.2)])
    ground(m)


@animal('otter', 'Nutria', 'Otter', 'land', 'river', egg=('#6b4a2e', '#cdb594'), hp=10, speed=0.28,
        food='minecraft:cod', drop='minecraft:leather', sound='fox', weight=8, group=(2, 4))
def otter(m):
    c = dict(body='#6b4a2e', leg='#5a3d24', head='#6b4a2e')
    k = quad(m, c, (5, 5, 14), (2, 3), (4, 4, 5), gait=1.5, head_dy=0.5,
             body_pats=[('belly', '#cdb594', 0.4)], head_pats=[('belly', '#cdb594', 0.3)])
    snout(m, k, (3, 2, 2), '#d9c3a3', dy=1)
    ears(m, k, (1, 1), '#5a3d24', inset=0, dz=-1)
    tail(m, k, (3, 3, 9), 'back', '#6b4a2e', pivot=(0, 0.5, 6.5), seg2=(2, 2, 5, '#5a3d24', (0, 0, 0)))


@animal('beaver', 'Castor', 'Beaver', 'land', 'river', egg=('#6a4a2a', '#3a2a1e'), hp=10, speed=0.2,
        food='minecraft:apple', drop='minecraft:stick', sound='pig', weight=7, group=(1, 3))
def beaver(m):
    c = dict(body='#6a4a2a', leg='#5a3d22', head='#6a4a2a')
    k = quad(m, c, (7, 6, 10), (2, 3), (5, 5, 5), gait=1.3, head_dy=0.5,
             body_pats=[('belly', '#8c6a42', 0.3), ('speckle', 0.1)])
    snout(m, k, (3, 2, 1), '#8c6a42', dy=1.5)
    m.add('teeth', 'head', (0, 2.5, -k['hd']), (-1, 0, -1, 2, 2, 1), '#f4f0d8')
    ears(m, k, (1, 1), '#5a3d22', inset=0, dz=-1)
    tail(m, k, (5, 1, 7), 'back', '#3a2a1e', pivot=(0, 1.5, 5), pats=[('scales', 0.75)], wag=0.1)


@animal('badger', 'Tejón', 'Badger', 'land', 'forest', egg=('#7b7b80', '#2f2f33'), hp=12, speed=0.22,
        temper='neutral', attack=3, food='minecraft:cod', drop='minecraft:leather', sound='fox', weight=7,
        group=(1, 2))
def badger(m):
    c = dict(body='#7b7b80', leg='#2f2f33', head='#2f2f33')
    k = quad(m, c, (8, 6, 12), (3, 3), (5, 5, 6), gait=1.3, head_dy=0.5,
             body_pats=[('belly', '#2f2f33', 0.35), ('speckle', 0.08)],
             head_pats=[('stripes', '#eeeeee', 5, 2)])
    snout(m, k, (3, 2, 2), '#e4e4e4', dy=1.3)
    ears(m, k, (2, 1), '#2f2f33', inset=0, dz=-1, pats=[('tip', '#eeeeee', 1)])
    tail(m, k, (2, 2, 3), 'back', '#7b7b80', pivot=(0, 0.5, 5.5))


@animal('skunk', 'Mofeta', 'Skunk', 'land', 'plains', egg=('#1e1e22', '#f2f2f2'), hp=8, speed=0.22,
        food='minecraft:sweet_berries', drop='minecraft:string', sound='fox', weight=7, group=(1, 2))
def skunk(m):
    c = dict(body='#1e1e22', leg='#1e1e22', head='#1e1e22')
    k = quad(m, c, (5, 5, 9), (2, 3), (4, 4, 4), gait=1.4, head_dy=0.5, body_pats=[('speckle', 0.06)])
    m.add('stripe', 'body', (0, 0, 0), (-1.5, -0.5, -4.5, 3, 1, 9), '#f2f2f2')
    m.add('headstripe', 'head', (0, -2, -2), (-0.5, -0.5, -2, 1, 1, 4), '#f2f2f2')
    snout(m, k, (2, 2, 1), '#2d2d33', dy=1)
    ears(m, k, (1, 1), '#1e1e22', inset=0, dz=-1)
    tail(m, k, (3, 6, 3), 'up', '#1e1e22', rot=(0.5, 0, 0), pivot=(0, 2, 4), wag=0.08,
         pats=[('cap', '#f2f2f2', 0.55)])


@animal('bison', 'Bisonte', 'Bison', 'land', 'plains', egg=('#4a3020', '#2f1f14'), hp=28, speed=0.22,
        temper='neutral', attack=6, food='minecraft:wheat', drop='minecraft:beef', sound='cow', weight=6,
        group=(3, 6))
def bison(m):
    c = dict(body='#6a4a30', leg='#5a3c26', head='#4a3020')
    k = quad(m, c, (12, 12, 16), (4, 9), (7, 8, 7), gait=0.9, head_dy=1.5,
             body_pats=[('speckle', 0.1)], head_pats=[('speckle', 0.12)])
    m.add('hump', 'body', (0, 0, -3), (-5, -4, -6, 10, 5, 9), '#2f1f14', pats=[('speckle', 0.15)], noise=0.12)
    m.add('beard', 'head', (0, k['hh'] / 2 - 1, -3), (-2, 0, -1.5, 4, 5, 3), '#2f1f14', pats=[('speckle', 0.15)])
    pair(m, 'horn', 'head', (3.5, -k['hh'] / 2 + 1, -2), (0, -1, -0.5, 3, 1, 1), '#d8d0c0', rot=(0, 0, -0.3))
    pair(m, 'horntip', 'head', (6.2, -k['hh'] / 2 - 0.5, -2), (-0.5, -3, -0.5, 1, 3, 1), '#d8d0c0')
    snout(m, k, (5, 4, 2), '#3a2616', dy=2)
    tail(m, k, (1, 8, 1), 'down', '#4a3020', seg2=(2, 3, 2, '#2f1f14', (0, 0, 0)))


@animal('warthog', 'Facóquero', 'Warthog', 'land', 'savanna', egg=('#7d6552', '#d9cfae'), hp=16, speed=0.26,
        temper='neutral', attack=4, food='minecraft:carrot', drop='minecraft:porkchop', sound='pig',
        weight=7, group=(2, 4))
def warthog(m):
    c = dict(body='#7d6552', leg='#6c5545', head='#7d6552')
    k = quad(m, c, (7, 8, 12), (3, 6), (6, 6, 7), gait=1.4, head_dy=0.5, head_dz=1,
             body_pats=[('speckle', 0.1)], head_pats=[('speckle', 0.08)])
    m.add('mane', 'body', (0, 0, -1), (-1, -3, -6, 2, 3, 11), '#4f3d30')
    snout(m, k, (4, 3, 3), '#9b8470', dy=1.8)
    pair(m, 'tusk', 'head', (2.5, 2.5, -k['hd'] + 1), (-0.5, -3, -0.5, 1, 3, 1), '#efe6cf')
    pair(m, 'wart', 'head', (3.3, 0, -3), (-0.5, -1, -1, 1, 2, 2), '#9b8470')
    ears(m, k, (2, 2), '#6c5545', inset=0, dz=-1.5)
    tail(m, k, (1, 6, 1), 'down', '#6c5545', seg2=(2, 2, 2, '#2f251d', (0, 0, 0)))


@animal('anteater', 'Oso hormiguero', 'Anteater', 'land', 'savanna', egg=('#6d5d4b', '#2b2420'), hp=14, speed=0.2,
        food='minecraft:honeycomb', drop='minecraft:string', sound='fox', weight=5, group=(1, 2))
def anteater(m):
    c = dict(body='#6d5d4b', leg='#5a4b3a', head='#7d6c58')
    k = quad(m, c, (6, 7, 12), (2, 6), (4, 4, 11), gait=1.1, head_dy=2.5, head_dz=1,
             body_pats=[('speckle', 0.1), ('stripes', '#2b2420', 7, 1)], leg_pats=[('socks', '#2b2420', 2)])
    m.add('tip', 'head', (0, 0, -k['hd']), (-1, -1, -1, 2, 2, 1), '#2b2420')
    tail(m, k, (5, 5, 10), 'back', '#5a4b3a', pivot=(0, 2, 5.5), rot=(-0.05, 0, 0), pats=[('speckle', 0.2)],
         seg2=(4, 4, 4, '#2b2420', (0, 0, 0)), wag=0.15)


@animal('hyena', 'Hiena', 'Hyena', 'land', 'savanna', egg=('#b79a63', '#4e3d22'), hp=18, speed=0.28,
        temper='hostile', attack=5, food='minecraft:rotten_flesh', drop='minecraft:rotten_flesh',
        sound='wolf', weight=4, group=(2, 4))
def hyena(m):
    c = dict(body='#b79a63', leg='#a08550', head='#b79a63')
    k = quad(m, c, (7, 8, 12), (3, 9), (6, 6, 7), gait=1.2, head_dy=0.5,
             body_pats=[('spots', '#4e3d22', 0.07, 2)], leg_pats=[('socks', '#4e3d22', 3)],
             head_pats=[('speckle', 0.1)])
    m.add('mane', 'body', (0, 0, -3), (-2, -3, -4, 4, 3, 8), '#4e3d22')
    snout(m, k, (4, 3, 3), '#2b2118', dy=1.5)
    ears(m, k, (3, 3), '#b79a63', inset=-0.5, dz=-1.5)
    tail(m, k, (2, 6, 2), 'down', '#4e3d22', rot=(0.3, 0, 0))


# --- reptiles y anfibios ---------------------------------------------------------------------------

@animal('iguana', 'Iguana', 'Iguana', 'land', 'jungle', egg=('#4f9a3a', '#b6d38a'), hp=8, speed=0.2,
        food='minecraft:melon_slice', drop='minecraft:string', sound='frog', weight=8, group=(1, 3))
def iguana(m):
    c = dict(body='#4f9a3a', leg='#437f30', head='#5aa844')
    k = quad(m, c, (5, 4, 10), (2, 3), (4, 4, 5), gait=1.5, splay=0.6, head_dy=0.5,
             body_pats=[('belly', '#b6d38a', 0.3), ('speckle', 0.12)], head_pats=[('speckle', 0.1)],
             eyes=dict(style='side', white=False))
    m.add('crest', 'body', (0, 0, 0), (-0.5, -2, -5, 1, 2, 10), '#3a7a2a')
    m.add('dewlap', 'head', (0, 2, -3), (-0.5, 0, -1, 1, 3, 3), '#b6d38a')
    tail(m, k, (3, 3, 10), 'back', '#4f9a3a', pivot=(0, 1.5, 5), pats=[('rings', '#3a7a2a', 2, 4)],
         seg2=(2, 2, 8, '#437f30', (0, 0, 0)), wag=0.3)


@animal('crocodile', 'Cocodrilo', 'Crocodile', 'land', 'swamp', egg=('#3f6b3a', '#d6d4a0'), hp=28, speed=0.22,
        temper='hostile', attack=7, food='minecraft:rotten_flesh', drop='minecraft:leather', sound='turtle',
        weight=4, group=(1, 2))
def crocodile(m):
    c = dict(body='#3f6b3a', leg='#35592f', head='#44733f')
    k = quad(m, c, (8, 6, 16), (3, 3), (6, 5, 5), gait=1.3, splay=0.5, head_dy=0.5,
             body_pats=[('belly', '#d6d4a0', 0.3), ('scales', 0.8)], head_pats=[('scales', 0.85)],
             eyes=dict(style='front', color='#e0c020', white=False))
    snout(m, k, (4, 3, 8), '#44733f', dy=1.5, nose=True, pats=[('belly', '#d6d4a0', 0.35)])
    pair(m, 'eyebump', 'head', (2, -3, -2), (-1, -1, -1, 2, 1, 2), '#44733f', eyes=dict(style='front', color='#e0c020', white=False))
    tail(m, k, (6, 5, 12), 'back', '#3f6b3a', pivot=(0, 0.5, 6), pats=[('scales', 0.8)],
         seg2=(4, 3, 10, '#35592f', (0, 0, 0)), wag=0.25)


@animal('chameleon', 'Camaleón', 'Chameleon', 'land', 'jungle', egg=('#6dbb4a', '#c7a93a'), hp=6, speed=0.14,
        food='minecraft:spider_eye', drop='minecraft:string', sound='frog', weight=6, group=(1, 2))
def chameleon(m):
    c = dict(body='#6dbb4a', leg='#5aa23a', head='#74c452')
    k = quad(m, c, (4, 5, 7), (2, 3), (4, 4, 5), gait=1.0, splay=0.4, head_dy=0.5,
             body_pats=[('spots', '#c7a93a', 0.08, 1), ('belly', '#d7e8a0', 0.3)], head_pats=[('speckle', 0.1)],
             eyes=dict(style='front', white=False))
    m.add('casque', 'head', (0, -2, -1), (-1, -2, -2, 2, 2, 4), '#5aa23a')
    pair(m, 'eye', 'head', (2.5, -0.5, -3), (-1, -1, -1, 2, 2, 2), '#e0c040', eyes=dict(style='front', color='#111111', white=False))
    m.add('tail', 'body', (0, 1, 3.5), (-1, -1, 0, 2, 2, 6), '#6dbb4a', rot=(-0.3, 0, 0), anims=[A('wave', 'y', 0.3, 0.12)])
    m.add('tail2', 'tail', (0, 0, 6), (-1, -1, 0, 2, 2, 3), '#5aa23a', rot=(-0.9, 0, 0))


@animal('snake', 'Serpiente', 'Snake', 'land', 'desert', egg=('#8a9a3a', '#2e2a1a'), hp=8, speed=0.2,
        temper='neutral', attack=3, food='minecraft:rabbit', drop='minecraft:spider_eye', sound='frog',
        weight=7, group=(1, 1))
def snake(m):
    sizes = [(3, 3, 5), (3, 3, 5), (3, 3, 5), (3, 3, 5), (2, 2, 5), (2, 2, 5), (2, 2, 4), (1, 1, 4)]
    cols = ['#8a9a3a', '#7d8c33']
    pz, prev = -8.0, None
    for i, (w, h, d) in enumerate(sizes):
        pv = (0, 24 - h / 2, pz) if prev is None else (0, (sizes[i - 1][1] - h) / 2, sizes[i - 1][2])
        m.add('s%d' % i, prev, pv, (-w / 2, -h / 2, 0, w, h, d), cols[i % 2],
              pats=[('bands', '#2e2a1a', 1, 'j'), ('belly', '#d9d19a', 0.3)],
              anims=[A('wave', 'y', 0.38, 0.28, phase=-i * 0.75)])
        prev = 's%d' % i
    m.add('head', 's0', (0, 0, 0.5), (-2, -1.5, -4, 4, 3, 4), '#8a9a3a', pats=[('belly', '#d9d19a', 0.3)],
          eyes=dict(style='side', white=False), anims=[A('look')])
    m.add('tongue', 'head', (0, 0.5, -4), (-0.5, -0.5, -2, 1, 1, 2), '#c62828',
          anims=[A('wave', 'pz', 0.8, 0.4)])


@animal('salamander', 'Salamandra', 'Salamander', 'land', 'swamp', egg=('#e6732a', '#1c1c1c'), hp=6, speed=0.18,
        food='minecraft:spider_eye', drop='minecraft:slime_ball', sound='frog', weight=7, group=(1, 3))
def salamander(m):
    c = dict(body='#e6732a', leg='#d4651f', head='#ea7c34')
    k = quad(m, c, (4, 3, 9), (2, 2), (4, 3, 4), gait=1.6, splay=0.5, head_dy=0.5,
             body_pats=[('spots', '#1c1c1c', 0.09, 1), ('belly', '#f3b266', 0.3)],
             head_pats=[('spots', '#1c1c1c', 0.07, 1)], eyes=dict(style='side', white=False))
    tail(m, k, (3, 3, 8), 'back', '#e6732a', pivot=(0, 0, 4.5), pats=[('spots', '#1c1c1c', 0.08, 1)],
         seg2=(2, 2, 5, '#d4651f', (0, 0, 0)), wag=0.3)
