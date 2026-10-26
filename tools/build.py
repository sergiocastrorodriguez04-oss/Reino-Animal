# -*- coding: utf-8 -*-
"""Genera todos los recursos del mod a partir de las definiciones de animales."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from PIL import Image
from core import ANIMALS, color_int, hx
import painter
import animals_a, animals_b, animals_c  # noqa: F401  (registran los animales al importarse)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RES = os.path.join(ROOT, 'src/main/resources')
ASSETS = os.path.join(RES, 'assets/animalmod')
DATA = os.path.join(RES, 'data/animalmod')

HABITATS = {
    'forest': ['forest', 'birch_forest', 'dark_forest', 'flower_forest', 'old_growth_birch_forest', 'windswept_forest'],
    'plains': ['plains', 'sunflower_plains', 'meadow'],
    'taiga': ['taiga', 'old_growth_pine_taiga', 'old_growth_spruce_taiga', 'snowy_taiga', 'grove'],
    'snowy': ['snowy_plains', 'ice_spikes', 'snowy_beach', 'snowy_slopes'],
    'desert': ['desert', 'badlands', 'eroded_badlands', 'wooded_badlands'],
    'savanna': ['savanna', 'savanna_plateau', 'windswept_savanna'],
    'jungle': ['jungle', 'sparse_jungle', 'bamboo_jungle'],
    'swamp': ['swamp', 'mangrove_swamp'],
    'mountain': ['windswept_hills', 'windswept_forest', 'stony_peaks', 'jagged_peaks', 'cherry_grove'],
    'river': ['river', 'swamp'],
    'beach': ['beach', 'stony_shore'],
    'ocean': ['ocean', 'deep_ocean', 'lukewarm_ocean', 'deep_lukewarm_ocean', 'cold_ocean', 'warm_ocean'],
    'warm_ocean': ['warm_ocean', 'lukewarm_ocean', 'deep_lukewarm_ocean'],
    'cold_ocean': ['cold_ocean', 'deep_cold_ocean', 'frozen_ocean', 'deep_frozen_ocean'],
    'deep_ocean': ['deep_ocean', 'deep_lukewarm_ocean', 'deep_cold_ocean'],
}


def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def export_model(model, W, H):
    parts = []
    for p in model.parts:
        parts.append(dict(
            name=p['name'], parent=p['parent'], pivot=p['pivot'], rot=p['rot'], box=p['box'],
            uv=p['uv'], mirror=p['mirror'], anims=p['anims']))
    return dict(tex=[W, H], parts=parts)


def hitbox(model):
    x0, x1, y0, y1, z0, z1 = model.bounds()
    width = max(x1 - x0, (z1 - z0) * 0.7) / 16.0
    height = (24.0 - y0) / 16.0
    return round(min(max(width, 0.3), 1.9), 2), round(min(max(height, 0.3), 3.2), 2)


def loot_table(drop, kind):
    if not drop:
        return {"type": "minecraft:entity", "pools": []}
    return {"type": "minecraft:entity", "pools": [{"rolls": 1, "entries": [{
        "type": "minecraft:item", "name": drop,
        "functions": [{"function": "minecraft:set_count",
                       "count": {"type": "minecraft:uniform", "min": 0, "max": 2}}]}]}]}


def main():
    from core import Model
    ids = [a['id'] for a in ANIMALS]
    assert len(ids) == len(set(ids)), 'ids duplicados'
    out, es, en = [], {}, {}
    for a in ANIMALS:
        m = Model()
        a['fn'](m)
        img, W, H = painter.build_texture(m, a['seed'])
        tex_path = os.path.join(ASSETS, 'textures/entity/%s.png' % a['id'])
        os.makedirs(os.path.dirname(tex_path), exist_ok=True)
        img.save(tex_path)
        w(os.path.join(ASSETS, 'animal_models/%s.json' % a['id']),
          json.dumps(export_model(m, W, H), separators=(',', ':')))
        w(os.path.join(ASSETS, 'models/item/%s_spawn_egg.json' % a['id']),
          json.dumps({"parent": "minecraft:item/template_spawn_egg"}))
        w(os.path.join(DATA, 'loot_table/entities/%s.json' % a['id']),
          json.dumps(loot_table(a['drop'], a['kind']), indent=2))
        wd, ht = hitbox(m)
        gmin, gmax = a['group']
        out.append(dict(
            id=a['id'], es=a['es'], en=a['en'], kind=a['kind'], temper=a['temper'], food=a['food'],
            drop=a['drop'] or '', sound=a['sound'], water=a['water'], hp=a['hp'], weight=a['weight'],
            minGroup=gmin, maxGroup=gmax, eggA=color_int(a['egg'][0]), eggB=color_int(a['egg'][1]),
            speed=a['speed'], attack=a['attack'], fly=a['fly'], width=wd, height=ht,
            biomes=HABITATS[a['habitat']]))
        es['entity.animalmod.%s' % a['id']] = a['es']
        en['entity.animalmod.%s' % a['id']] = a['en']
        es['item.animalmod.%s_spawn_egg' % a['id']] = 'Huevo generador de %s' % a['es'].lower() if a['es'][0].isupper() else a['es']
        en['item.animalmod.%s_spawn_egg' % a['id']] = '%s Spawn Egg' % a['en']
        print('%-12s %-6s tex %3dx%-3d piezas %2d  caja %.2fx%.2f' % (a['id'], a['kind'], W, H, len(m.parts), wd, ht))
    es['itemGroup.animalmod'] = 'Reino Animal'
    en['itemGroup.animalmod'] = 'Animal Kingdom'
    w(os.path.join(RES, 'animals.json'), json.dumps(out, ensure_ascii=False, indent=1))
    w(os.path.join(ASSETS, 'lang/es_es.json'), json.dumps(es, ensure_ascii=False, indent=2))
    w(os.path.join(ASSETS, 'lang/en_us.json'), json.dumps(en, ensure_ascii=False, indent=2))
    print('\nTotal animales:', len(out))


if __name__ == '__main__':
    main()
