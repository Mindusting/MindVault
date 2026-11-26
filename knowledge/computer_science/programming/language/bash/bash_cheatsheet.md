---
aliases: ["Chuleta de bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:25:57
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# CHULETA DE BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](bash.md)
> - [Comillas y caracteres de escape en bash](basics/quoting.md)
> - [Estado de salida en bash](basics/exit_status.md)
> - [Redirecciones en bash](io/redirections.md)
> - [Gestión de errores en bash](advanced/error_handling.md)

## EJECUCIÓN

| SINTAXIS              | DESCRIPCIÓN                              |
|:--------------------- |:---------------------------------------- |
| `#!/usr/bin/env bash` | Shebang.                                 |
| `bash script.sh`      | Ejecutar con Bash.                       |
| `chmod u+x script.sh` | Dar permiso de ejecución al propietario. |
| `./script.sh`         | Ejecutar directamente.                   |
| `bash -n script.sh`   | Comprobar sintaxis.                      |
| `source script.sh`    | Cargar en el shell actual.               |

## VARIABLES Y EXPANSIONES

| SINTAXIS               | DESCRIPCIÓN                                    |
|:---------------------- |:---------------------------------------------- |
| `name='Adelio'`        | Asignar sin espacios alrededor de `=`.         |
| `"$name"`, `"${name}"` | Expandir como un argumento.                    |
| `${name:-default}`     | Valor alternativo si no definida o vacía.      |
| `${#name}`             | Longitud.                                      |
| `${name:0:3}`          | Subcadena.                                     |
| `${file##*/}`          | Último componente de una ruta sin barra final. |
| `${file%.*}`           | Eliminar sufijo desde el último punto.         |
| `${text//a/b}`         | Sustituir todas las coincidencias.             |
| `$(command)`           | Capturar stdout sin saltos finales.            |
| `$((a + b))`           | Evaluar aritmética entera.                     |
| `"$@"`                 | Argumentos independientes.                     |
| `$#`, `$?`, `$!`       | Cantidad, último estado y PID asíncrono.       |

## CONTROL DE FLUJO

```bash
if [[ -f $file ]]; then
    printf '%s\n' "$file"
fi
for item in "${items[@]}"; do
    printf '%s\n' "$item"
done
while IFS= read -r line || [[ -n $line ]]; do
    printf '%s\n' "$line"
done < "$file"
```

`[[ ]]`: pruebas y cadenas; `(())`: aritmética; `[]`: comando de prueba portable. Estado 0 = éxito. En aritmética, valor 0 = falso. Para `case`, patrones glob; para `[[ ... =~ ... ]]`, regex ERE.

## ARRAYS Y FUNCIONES

```bash
items=('a b' c)
items+=('d')
printf '%s\n' "${items[@]}"
function_name() {
    local value=$1
    printf '%s\n' "$value"
}
```

`return` devuelve un estado; stdout transporta datos. `"${items[@]}"` mantiene cada elemento por separado.

## ENTRADA Y SALIDA

| SINTAXIS                 | DESCRIPCIÓN                                   |
| ------------------------ | --------------------------------------------- |
| `>`, `>>`, `<`           | Sobrescribir, añadir, leer.                   |
| `2> file`                | Redirigir stderr.                             |
| `> file 2>&1`            | stdout y stderr al archivo.                   |
| a \| b                   | stdout de a a stdin de b.                     |
| `IFS= read -r line`      | Leer una línea preservando espacios y barras. |
| `printf '%s\n' "$value"` | Imprimir datos literalmente.                  |

## REGLAS IMPORTANTES

- Protege expansiones de datos con comillas dobles; usa arrays para argumentos múltiples.
- Valida entradas antes de evaluarlas aritméticamente.
- Usa `--` cuando la herramienta lo admita y pueda recibir rutas que empiecen por `-`.
- No analices `ls`; usa glob o `find -print0` / `find -exec`.
- Comprueba errores de operaciones reales. `set -euo pipefail` no sustituye estas comprobaciones.
- Usa `mktemp` y `trap` para temporales; no ejecutes código desconocido mediante `source` o `eval`.
