# -*- coding: utf-8 -*-
import math
from core import *
from archetypes import *


# --- aves voladoras ---------------------------------------------------------------------------------

@animal('eagle', 'Águila', 'Eagle', 'flying', 'mountain', egg=('#4a2f1a', '#f2f2f2'), hp=12, speed=0.2, fly=0.55,
        food='minecraft:rabbit', drop='minecraft:feather', sound='parrot', weight=5, group=(1, 2))
def eagle(m):
    c = dict(body='#4a2f1a', head='#f2f2f2', leg='#e0a020', wing='#3d2814')
    bird(m, c, (6, 6, 10), (2, 5), (4, 4, 5), (9, 8), head_off=(-1.5, -4), fly=True,
         tail_=(4, 1, 6, '#f2f2f2', 0.2), beak=(2, 2, 3, '#e0a020'), beak_rot=0.15,
         body_pats=[('speckle', 0.12), ('belly', '#6a4426', 0.3)], wing_pats=[('tip', '#2a1a0c', 3)])


@animal('owl', 'Búho', 'Owl', 'flying', 'forest', egg=('#8a6a42', '#e6d8b8'), hp=8, speed=0.2, fly=0.45,
        food='minecraft:rabbit', drop='minecraft:feather', sound='parrot', weight=6, group=(1, 2))
def owl(m):
    c = dict(body='#8a6a42', head='#8a6a42', leg='#d9a233', wing='#7a5c38')
    bird(m, c, (6, 7, 6), (2, 3), (6, 5, 5), (7, 5), head_off=(-2, -0.5), fly=True,
         tail_=(4, 1, 4, '#7a5c38', 0.1), beak=(2, 2, 1, '#d9a233'), eyes=dict(style='big', color='#f0c020'),
         body_pats=[('belly', '#d9c7a4', 0.5), ('speckle', 0.14)], head_pats=[('frontpatch', '#e6d8b8', 1)])
    pair(m, 'tuft', 'head', (2, -2.5, -1), (-0.5, -2, -0.5, 1, 2, 1), '#7a5c38')


@animal('toucan', 'Tucán', 'Toucan', 'flying', 'jungle', egg=('#1c1c20', '#f08a1a'), hp=8, speed=0.2, fly=0.45,
        food='minecraft:glow_berries', drop='minecraft:feather', sound='parrot', weight=7, group=(1, 3))
def toucan(m):
    c = dict(body='#1c1c20', head='#1c1c20', leg='#7a8a9a', wing='#1c1c20')
    bird(m, c, (5, 6, 7), (2, 3), (4, 4, 4), (7, 5), head_off=(-2, -2.5), fly=True,
         tail_=(3, 1, 6, '#1c1c20', 0.15), beak=(2, 3, 6, '#f08a1a', [('tip', '#1c1c20', 1)]),
         body_pats=[('belly', '#f7f2e6', 0.0)], head_pats=[('frontpatch', '#f7f2e6', 1)])
    m.get('body')['paint']['pats'] = [('frontpatch', '#f7f2e6', 1), ('speckle', 0.08)]


@animal('duck', 'Pato', 'Duck', 'flying', 'river', egg=('#2a6b3a', '#8a7a5e'), hp=8, speed=0.2, fly=0.4,
        food='minecraft:wheat_seeds', drop='minecraft:feather', sound='chicken', weight=9, group=(2, 5))
def duck(m):
    c = dict(body='#8a7a5e', head='#2a6b3a', leg='#e07a1a', wing='#76694f', neck='#2a6b3a')
    bird(m, c, (6, 5, 9), (1, 3), (4, 4, 4), (6, 7), neck=(2, 4, 2), fly=True, leg_t=2,
         tail_=(4, 1, 3, '#2a2a2e', 0.2), beak=(3, 1, 3, '#f0b020'),
         body_pats=[('belly', '#d6cdb4', 0.3), ('speckle', 0.1)], wing_pats=[('tip', '#2a4fa8', 2)])
    m.add('ring', 'neck', (0, 0, 0), (-1.5, -1, -1.5, 3, 1, 3), '#f4f4f4')


@animal('crow', 'Cuervo', 'Crow', 'flying', 'plains', egg=('#1b1b22', '#6a6a78'), hp=6, speed=0.22, fly=0.5,
        food='minecraft:wheat_seeds', drop='minecraft:feather', sound='parrot', weight=8, group=(2, 4))
def crow(m):
    c = dict(body='#1b1b22', head='#1b1b22', leg='#2a2a30', wing='#17171d')
    bird(m, c, (5, 5, 8), (1, 4), (4, 4, 4), (8, 6), head_off=(-1.5, -3.5), fly=True,
         tail_=(4, 1, 6, '#17171d', 0.2), beak=(1, 2, 3, '#2a2a30'), beak_rot=0.1,
         body_pats=[('speckle', 0.1), ('belly', '#26262e', 0.3)], wing_pats=[('speckle', 0.1)])


@animal('hummingbird', 'Colibrí', 'Hummingbird', 'flying', 'jungle', egg=('#2fae6b', '#d62f4a'), hp=4,
        speed=0.2, fly=0.6, food='minecraft:sugar', drop='minecraft:feather', sound='parrot', weight=8,
        group=(1, 3))
def hummingbird(m):
    c = dict(body='#2fae6b', head='#2fae6b', leg='#2a2a2e', wing='#7fd6a6')
    bird(m, c, (3, 3, 5), (1, 1), (3, 3, 3), (5, 3), head_off=(-1, -2.5), fly=True,
         tail_=(2, 1, 3, '#1f8a55', 0.3), beak=(1, 1, 5, '#1a1a1a'),
         body_pats=[('belly', '#f1efe0', 0.3)], head_pats=[('belly', '#d62f4a', 0.4)])
    for n in ('wing_r', 'wing_l'):
        for a in m.get(n)['anims']:
            if a['type'] == 'wave' and a['speed'] > 1:
                a['speed'] = 2.8


# --- aves terrestres --------------------------------------------------------------------------------

@animal('flamingo', 'Flamenco', 'Flamingo', 'land', 'beach', egg=('#f27ba0', '#1c1c1c'), hp=8, speed=0.2,
        food='minecraft:kelp', drop='minecraft:feather', sound='parrot', weight=6, group=(3, 6))
def flamingo(m):
    c = dict(body='#f27ba0', head='#f27ba0', leg='#e8678f', wing='#f58fb0', neck='#f27ba0')
    bird(m, c, (5, 6, 8), (1, 12), (3, 3, 4), (6, 7), neck=(2, 10, 2), leg_t=1, gait=1.1,
         tail_=(3, 1, 3, '#f27ba0', 0.3), beak=(2, 2, 3, '#f4d0d8', [('tip', '#1c1c1c', 1)]), beak_rot=0.35,
         wing_pats=[('tip', '#1c1c1c', 2)], body_pats=[('speckle', 0.08)])


@animal('penguin', 'Pingüino', 'Penguin', 'land', 'snowy', egg=('#1b2230', '#f4f4f4'), hp=10, speed=0.18,
        food='minecraft:cod', drop='minecraft:feather', sound='chicken', weight=8, group=(3, 7))
def penguin(m):
    c = dict(torso='#1b2230', leg='#e07a1a', arm='#1b2230', head='#1b2230')
    biped(m, c, (6, 9, 5), (2, 2, 3), (1, 6, 3), (5, 5, 5), gait=0.9, arm_swing=0.25,
          torso_pats=[('frontpatch', '#f4f4f4', 1)], head_pats=[('speckle', 0.05)])
    m.add('beak', 'head', (0, -1.8, -2.5), (-1, -0.5, -2, 2, 1, 2), '#e07a1a')
    m.get('torso')['anims'].append(A('wave', 'z', 0.06, 0.45, gate='moving'))
    ground(m)


@animal('ostrich', 'Avestruz', 'Ostrich', 'land', 'savanna', egg=('#2a2a2e', '#f2f2f2'), hp=14, speed=0.32,
        food='minecraft:wheat_seeds', drop='minecraft:feather', sound='chicken', weight=6, group=(1, 3))
def ostrich(m):
    c = dict(body='#2a2a2e', head='#d9a08a', leg='#d9a08a', wing='#f2f2f2', neck='#d9a08a')
    bird(m, c, (7, 7, 10), (2, 13), (4, 3, 5), (6, 6), neck=(3, 14, 3), leg_t=2, gait=1.3,
         tail_=(5, 2, 5, '#f2f2f2', 0.3), beak=(2, 1, 2, '#e0b8a8'), body_pats=[('speckle', 0.1)],
         wing_pats=[('speckle', 0.06)])


@animal('peacock', 'Pavo real', 'Peacock', 'land', 'jungle', egg=('#1a54a8', '#1f8a70'), hp=8, speed=0.22,
        food='minecraft:wheat_seeds', drop='minecraft:feather', sound='chicken', weight=7, group=(1, 3))
def peacock(m):
    c = dict(body='#1a54a8', head='#2a6bd0', leg='#c9b070', wing='#2f7a5a', neck='#1f62c0')
    bird(m, c, (5, 5, 9), (1, 6), (3, 3, 4), (5, 6), neck=(2, 6, 2), leg_t=1, gait=1.2,
         beak=(1, 1, 2, '#c9b070'), body_pats=[('speckle', 0.1)], wing_pats=[('speckle', 0.1)])
    m.add('crest', 'head', (0, -1.5, 0), (-0.5, -3, -0.5, 1, 3, 1), '#2a6bd0')
    m.add('crest2', 'crest', (0, -3, 0), (-1.5, -1, -0.5, 3, 1, 1), '#1f8a70')
    m.add('train', 'body', (0, 3, 4.5), (-4, -0.5, 0, 8, 1, 14), '#1f8a70', rot=(-0.4, 0, 0),
          pats=[('spots', '#2347a8', 0.14, 2), ('spots', '#e0b020', 0.05, 1)], anims=[A('wave', 'y', 0.05, 0.12)])


# --- criaturas acuáticas ----------------------------------------------------------------------------

@animal('seahorse', 'Caballito de mar', 'Seahorse', 'water', 'warm_ocean', egg=('#e6a53a', '#c97d1d'), hp=4,
        speed=0.6, water='water_ambient', food='minecraft:kelp', drop='minecraft:kelp', sound='cod', weight=10,
        group=(2, 5))
def seahorse(m):
    m.add('body', None, (0, 10, 0), (-1.5, 0, -1.5, 3, 5, 3), '#e6a53a', pats=[('bands', '#c97d1d', 2, 'j')],
          anims=[A('wave', 'z', 0.1, 0.15), A('wave', 'py', 0.8, 0.12)])
    m.add('head', 'body', (0, 0, 0), (-2, -4, -2.5, 4, 4, 4), '#e6a53a', eyes=dict(style='side', white=False),
          anims=[A('look')])
    m.add('snout', 'head', (0, -1.5, -2.5), (-1, -1, -3, 2, 2, 3), '#d98e2a')
    m.add('crest', 'head', (0, -4, 0.5), (-0.5, -2, -1, 1, 2, 2), '#c97d1d')
    m.add('fin', 'body', (0, 1, 1.5), (-0.5, 0, 0, 1, 3, 2), '#f2d27a', anims=[A('wave', 'x', 0.3, 0.8)])
    m.add('tail1', 'body', (0, 5, 0), (-1, 0, -1, 2, 4, 2), '#e6a53a', pats=[('bands', '#c97d1d', 2, 'j')])
    m.add('tail2', 'tail1', (0, 4, 0), (-0.5, 0, -0.5, 1, 3, 1), '#d98e2a', rot=(-0.7, 0, 0))
    ground(m)


@animal('jellyfish', 'Medusa', 'Jellyfish', 'water', 'ocean', egg=('#f2a5d8', '#ffd4f0'), hp=6, speed=0.3,
        water='water_ambient', food='minecraft:kelp', drop='minecraft:slime_ball', sound='squid', weight=8,
        group=(2, 4))
def jellyfish(m):
    m.add('bell', None, (0, 10, 0), (-5, -6, -5, 10, 6, 10), '#f2a5d8',
          pats=[('spots', '#ffd4f0', 0.1, 2), ('speckle', 0.08)], anims=[A('wave', 'py', 1.2, 0.2)])
    m.add('rim', 'bell', (0, 0, 0), (-6, 0, -6, 12, 1, 12), '#e48ac4')
    for i, (x, z, ln) in enumerate([(-3, -3, 8), (3, -3, 6), (-3, 3, 7), (3, 3, 9), (0, 0, 10)]):
        m.add('t%d' % i, 'bell', (x, 1, z), (-0.5, 0, -0.5, 1, ln, 1), '#f7c3e6',
              anims=[A('wave', 'x', 0.3, 0.15, phase=i * 1.3), A('wave', 'z', 0.25, 0.13, phase=i * 0.9)])
    ground(m)


@animal('shark', 'Tiburón', 'Shark', 'water', 'deep_ocean', egg=('#6c7a8c', '#eeeeee'), hp=30, speed=1.0,
        temper='hostile', attack=7, water='water_creature', food='minecraft:cod', drop='minecraft:cod',
        sound='dolphin', weight=3, group=(1, 1))
def shark(m):
    g = '#6c7a8c'
    bel = ('belly', '#eeeeee', 0.4)
    m.add('body', None, (0, 12, 0), (-4, -4, -8, 8, 8, 16), g, pats=[bel], anims=[A('wave', 'y', 0.06, 0.2)])
    m.add('head', 'body', (0, 0, -8), (-3.5, -3.5, -6, 7, 7, 6), g, pats=[bel],
          eyes=dict(style='side', white=False), anims=[A('wave', 'y', 0.05, 0.2, phase=-0.5)])
    m.add('snout', 'head', (0, 1, -5.5), (-2.5, -2, -3, 5, 4, 3), g, pats=[('belly', '#eeeeee', 0.5)])
    m.add('tail', 'body', (0, 0, 8), (-3, -3, 0, 6, 6, 8), g, pats=[bel], anims=[A('wave', 'y', 0.35, 0.3, phase=0.8)])
    m.add('tailfin', 'tail', (0, 0, 8), (-0.5, -6, 0, 1, 10, 5), g, anims=[A('wave', 'y', 0.3, 0.3, phase=1.6)])
    m.add('dorsal', 'body', (0, -4, -1), (-0.5, -6, 0, 1, 6, 5), g)
    pair(m, 'pec', 'body', (4, 2, -3), (0, 0, -2, 5, 1, 4), g, rot=(0, 0, 0.5),
         anims=lambda s: [A('wave', 'z', 0.1 * s, 0.2)])
    ground(m)


@animal('orca', 'Orca', 'Orca', 'water', 'cold_ocean', egg=('#16181d', '#f4f4f4'), hp=40, speed=1.1,
        temper='neutral', attack=8, water='water_creature', food='minecraft:salmon', drop='minecraft:cod',
        sound='dolphin', weight=2, group=(1, 3))
def orca(m):
    d = '#16181d'
    bel = ('belly', '#f4f4f4', 0.35)
    m.add('body', None, (0, 14, 0), (-5, -5, -10, 10, 10, 20), d, pats=[bel], anims=[A('wave', 'y', 0.05, 0.18)])
    m.add('head', 'body', (0, 0, -10), (-4.5, -4.5, -6, 9, 9, 6), d, pats=[('belly', '#f4f4f4', 0.3)],
          eyes=dict(style='side', white=False), anims=[A('wave', 'y', 0.04, 0.18, phase=-0.5)])
    pair(m, 'patch', 'head', (4.55, -1.5, -3.5), (-0.5, -1, -1.5, 1, 2, 3), '#f4f4f4')
    m.add('tail', 'body', (0, 0, 10), (-3.5, -3.5, 0, 7, 7, 8), d, pats=[bel], anims=[A('wave', 'x', 0.18, 0.3, phase=0.6)])
    m.add('flukes', 'tail', (0, 0, 8), (-6, -0.5, 0, 12, 1, 5), d, anims=[A('wave', 'x', 0.22, 0.3, phase=1.2)])
    m.add('dorsal', 'body', (0, -5, -1), (-0.5, -8, 0, 1, 8, 6), d)
    pair(m, 'flipper', 'body', (5, 3, -5), (0, 0, -2.5, 7, 1, 5), d, rot=(0, 0, 0.55),
         anims=lambda s: [A('wave', 'z', 0.12 * s, 0.2)])
    ground(m)


@animal('octopus', 'Pulpo', 'Octopus', 'water', 'warm_ocean', egg=('#c7512b', '#e08a5a'), hp=10, speed=0.7,
        water='water_ambient', food='minecraft:cod', drop='minecraft:ink_sac', sound='squid', weight=6, group=(1, 2))
def octopus(m):
    m.add('head', None, (0, 8, 0), (-4, -8, -4, 8, 8, 8), '#c7512b',
          pats=[('spots', '#e08a5a', 0.1, 2), ('speckle', 0.08)], eyes=dict(style='front', white=True),
          anims=[A('wave', 'py', 0.8, 0.2)])
    for i in range(8):
        a = i * math.pi / 4
        m.add('t%d' % i, 'head', (round(math.cos(a) * 3, 2), 0, round(math.sin(a) * 3, 2)), (-1, 0, -1, 2, 9, 2),
              '#b8461f', rot=(round(0.35 * math.sin(a), 2), 0, round(-0.35 * math.cos(a), 2)),
              pats=[('rings', '#e08a5a', 1, 3)], anims=[A('wave', 'x', 0.25, 0.14, phase=i * 0.8), A('wave', 'z', 0.18, 0.11, phase=i * 0.6)])
    ground(m)


@animal('manta', 'Manta raya', 'Manta Ray', 'water', 'warm_ocean', egg=('#2a3347', '#f2f2f2'), hp=16, speed=0.8,
        water='water_ambient', food='minecraft:kelp', drop='minecraft:leather', sound='dolphin', weight=4,
        group=(1, 2))
def manta(m):
    dk = '#2a3347'
    bel = ('belly', '#f2f2f2', 0.5)
    m.add('body', None, (0, 12, 0), (-5, -1.5, -6, 10, 3, 12), dk, pats=[bel], eyes=dict(style='side', white=False),
          anims=[A('wave', 'py', 0.8, 0.12)])
    pair(m, 'wing', 'body', (5, 0, -1), (0, -0.5, -4, 9, 1, 8), dk, pats=[bel],
         anims=lambda s: [A('wave', 'z', 0.35 * s, 0.22)])
    pair(m, 'horn', 'body', (3, 0, -6), (-1, -0.5, -3, 2, 1, 3), dk, rot=(0, 0.2, 0))
    m.add('tail', 'body', (0, 0, 6), (-0.5, -0.5, 0, 1, 1, 12), dk, anims=[A('wave', 'y', 0.3, 0.2)])
    ground(m)
