# Notas del proyecto

Los directorios tienen tamaños deliberadamente separados, para que `du -sh */`
produzca un ranking donde el orden importe:

| Directorio | Peso | Qué guarda |
|---|---|---|
| `src/` | el más liviano | el código de ejemplo |
| `docs/` | | esta nota y `tamanos.txt` |
| `logs/` | | la salida de la app (varios archivos) |
| `tmp/` | | salidas descartables de compilación |
| `vendor/` | | licencias de dependencias |
| `assets/` | el más pesado | `eventos.csv`, un dataset de ~24 mil filas |

Ninguno empata con otro, y hay **seis**: con cinco o menos, `tail -5` los
devuelve todos y no recorta nada.

El salto de escala de `assets/` es a propósito. Es lo que hace que `sort -h` se
note: sin el flag, `1,9M` se ordena como texto y queda **segundo**, detrás de
`16K`, mientras que `8,0K` termina último. Con tres directorios del mismo orden
de magnitud, olvidarse el flag daba casi el mismo resultado y el ejercicio no
enseñaba nada.

`tamanos.txt` es la misma idea servida ya hecha: un listado con sufijos para
practicar `sort -h` sola, sin depender de la salida de `du`.
