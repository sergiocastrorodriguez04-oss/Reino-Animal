# Reino Animal — mod de Minecraft Java (Fabric 1.21.1)

**50 animales nuevos** con estética Minecraft (modelos de cajas, texturas pixel-art de 1 px = 1 píxel de bloque),
**animaciones propias** y un **huevo generador (spawn egg) para cada criatura**, todos en la pestaña
creativa "Reino Animal".

## Animales
- **Mamíferos (29):** ciervo, alce, elefante, jirafa, león, tigre, cebra, hipopótamo, rinoceronte, canguro, koala,
  mapache, ardilla, erizo, capibara, perezoso, mono, gorila, oso pardo, panda rojo, suricata, nutria, castor,
  tejón, mofeta, bisonte, facóquero, oso hormiguero, hiena
- **Reptiles y anfibios (5):** iguana, cocodrilo, camaleón, serpiente, salamandra
- **Aves terrestres (4):** flamenco, pingüino, avestruz, pavo real
- **Aves voladoras (6):** águila, búho, tucán, pato, cuervo, colibrí (vuelan y se posan de vez en cuando)
- **Acuáticos (6):** caballito de mar, medusa, tiburón, orca, pulpo, manta raya

Temperamento: 34 pasivos (huyen), 11 neutrales (se defienden: elefante, alce, hipopótamo, rinoceronte, oso, gorila,
bisonte, tejón, facóquero, serpiente, orca) y 5 hostiles (león, tigre, hiena, cocodrilo, tiburón; desaparecen en Pacífico).

Todos se pueden criar con su comida (`food` en `animals.json`), aparecen en biomas acordes y sueltan un objeto.
Invocación por comando: `/summon animalmod:ciervo` → usa el id en inglés: `/summon animalmod:deer`.

## Animaciones (todas procedimentales, definidas por pieza en el JSON del modelo)
caminar (patas alternas), mirar al jugador (cabeza), respiración, cola/orejas que se mueven, trompa del elefante,
tentáculos del pulpo y la medusa, aleteo de las aves en vuelo (distinto en tierra), colibrí con aleteo rápido,
natación ondulante de tiburón/orca/manta, serpiente que ondula, saltos de canguro/ardilla, bamboleo del pingüino.

## Compilar
Requisitos: **JDK 21**, Minecraft 1.21.1 con **Fabric Loader ≥ 0.16** y **Fabric API**.

1. Abre la carpeta con IntelliJ IDEA (importa el proyecto Gradle) **o** en terminal, una sola vez: `gradle wrapper --gradle-version 8.8`
2. `./gradlew build`
3. El `.jar` queda en `build/libs/reino-animal-1.0.0.jar`; cópialo a tu carpeta `mods` junto con Fabric API.
4. Para probar en desarrollo: `./gradlew runClient`.

> Importante: el código Java se ha revisado a mano y su sintaxis se validó, pero **no se pudo compilar contra Minecraft**
> en el entorno donde se generó. Si Gradle marca algún error de nombre de método (las APIs de Yarn cambian entre versiones),
> suele ser un ajuste de una línea. Los recursos (texturas, modelos, idiomas, loot tables) sí están comprobados.

## Estructura
```
tools/                 generador en Python (Pillow): define los 50 animales y crea texturas/modelos/idiomas/loot
  animals_a/b/c.py     definición de cada animal (cajas, colores, patrones, animaciones)
  build.py             regenera src/main/resources  →  python3 tools/build.py
  preview.py           renderiza previews/ (hojas con los 50 modelos)
src/main/java/...      entidades (terrestre, voladora, acuática), registro, renderer y animación
src/main/resources/    animals.json, texturas, modelos, huevos, idiomas (es/en), loot tables
```

## Personalizar
- **Cambiar un animal:** edita su función en `tools/animals_*.py` y ejecuta `python3 tools/build.py`.
- **Retocar una textura a mano:** edita `assets/animalmod/textures/entity/<id>.png` (el mapa UV es el estándar de cajas de Minecraft).
- **Ajustar vida, velocidad, biomas, comida:** `src/main/resources/animals.json` (o los parámetros del decorador `@animal`).
- Los modelos y animaciones se pueden sobrescribir desde un resource pack (`assets/animalmod/animal_models/<id>.json`).
