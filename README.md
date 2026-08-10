# cli-tools-learning · rama `grep-samples`

Material de práctica para los comandos que **leen y filtran texto**: `grep`,
`head`, `tail`, `sort`, `wc`, `cut`, `du`.

> Este README es el de ESTA rama y no coincide con el de `main` a propósito.
> Ver "Esta rama no se mergea" más abajo.

## Qué es una rama de práctica

Un **punto de partida**, no trabajo en curso. Existe para que la tarjeta de Anki
que la nombra vuelva a encontrar el mismo árbol en cada repaso — el enunciado da
por cierto un estado, y si el estado cambió el ejercicio ya no mide lo mismo.

De ahí las dos reglas que la gobiernan:

**No se mergea. Nunca.** Su destino no es `main`. Nada de merges, PRs ni rebases
contra `main`; no la borres "porque ya está mergeada" —no lo va a estar— ni le
aplastes la historia para dejarla prolija. Diverge de `main` y de las otras ramas
a propósito, y no vuelve a converger.

**Todo va commiteado.** Un ejercicio que dependa de un archivo sin commitear
queda inservible al segundo repaso, y no te enterás hasta que te toca: el reset
borra también lo ignorado.

Antes de sentarte a practicar:

```bash
bun <ankify>/bin/lib/practica/cli.ts reset cli-tools-learning
```

Devuelve el árbol al estado preparado y se lleva lo que hayas dejado del intento
anterior.

## El material

| Ruta | Para qué |
|---|---|
| `assets/eventos.csv` | ~24 mil filas de eventos por servicio y nivel. El archivo grande: `grep` con volumen, y el que domina el ranking de `du` |
| `logs/` | tres logs de formatos distintos — aplicación, errores y accesos HTTP |
| `docs/notas.md` | por qué los directorios pesan lo que pesan. **Leelo antes de tocar tamaños** |
| `docs/tamanos.txt` | salida real de `du -h` —tabulador de separador, coma decimal— para practicar `sort -h` sobre lo que `du` escupe de verdad |
| `tamanos.txt` (raíz) | el hermano sintético del anterior: espacio de separador y punto decimal (`2.1G backups`). Es el operando de la tarjeta de `sort -h` sobre un archivo, con su salida pegada — **no lo borres ni le cambies el orden**, el enunciado la da por cierta |
| `vendor/LICENSES.txt` | texto repetitivo con estructura: bueno para `grep -c` y `uniq` |
| `tmp/build-output.txt` | salida de compilación simulada |
| `src/utils.py`, `app.py` | código, para separar coincidencias en fuente de coincidencias en texto plano |
| `data.txt`, `log.txt` | los archivos chicos originales, para ejercicios de una sola pantalla |

Los seis directorios tienen **tamaños deliberadamente distintos**, y el salto de
escala de `assets/` no es casual: es lo que hace que olvidarse un flag dé un
resultado visiblemente equivocado. `docs/notas.md` lo explica y da los números.

Si agregás o borrás material, revisá que ese orden siga en pie — es la mitad de
lo que los ejercicios de ranking miden.

## Qué tarjetas dependen de esta rama

```
du -sh */ 2>/dev/null
sort -h
tail -5
du -sh */ 2>/dev/null | sort -h | tail -5
```

Mazo `00. General::Progamming::Terminal`. Las tres primeras son los átomos; la
cuarta es el cableado, que es un ejercicio propio: saber encadenar la tubería no
reemplaza saber cada comando por separado.
