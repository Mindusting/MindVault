---
aliases: ["Gestión de errores en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:35:31
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# GESTIÓN DE ERRORES EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Estado de salida en bash](../basics/exit_status.md)
> - [Señales y trap en bash](traps.md)
> - [Depuración y pruebas de scripts bash](debugging.md)
> - [Tuberías en bash](../io/pipes.md)

## DEFINICIÓN

Bash no tiene excepciones como Java o Python. Los comandos comunican éxito o fallo mediante estados de salida; el script decide cómo interpretarlos. Un código no nulo no siempre significa que deba abortarse el programa.

## COMPROBACIONES EXPLÍCITAS

```bash
if output=$(date +%F); then
    printf '%s\n' "$output"
else
    status=$?
    printf 'Error de date: %d\n' "$status" >&2
fi
```

La asignación sin nombre de comando recibe el estado de su última sustitución de comandos. Guarda `$?` inmediatamente. Con `if! command; then`, dentro de la rama `$?` corresponde a la negación, no al estado original.

## OPCIONES DE SHELL

| OPCIÓN            | COMPORTAMIENTO                                                 |
|:----------------- |:-------------------------------------------------------------- |
| `set -e`          | Sale ante ciertos estados no nulos no controlados.             |
| `set -u`          | Trata muchas expansiones de variables no definidas como error. |
| `set -o pipefail` | Propaga estados no nulos desde un pipeline.                    |
| `set -x`          | Imprime trazas de órdenes expandidas.                          |
| `set -E`          | Hereda la trampa ERR en más contextos.                         |

`set -euo pipefail` es una combinación habitual, pero no reemplaza el manejo explícito de fallos. `-e` tiene excepciones: condiciones de `if`, `while` y `until`, partes de listas `&&`/`||`, comandos negados y elementos no finales de pipelines, entre otros. Si una función se llama en un contexto donde se ignora `-e`, esto puede afectar a todo su cuerpo. Las sustituciones de comandos normalmente desactivan `-e` en su entorno, salvo modos/opciones como `inherit_errexit`.

```bash
(
    set -e
    if false; then
        printf 'No se ejecuta\n'
    fi
    printf 'El script continúa\n'
)
```

Con `set -u`, utiliza `${1-}` para comprobar un argumento opcional antes de acceder a él. No actives trazas sobre secretos. `((counter++))` puede devolver 1 sin que haya fallado el incremento.

## CÓDIGOS DE SALIDA PROPIOS

Define una convención para tu script, por ejemplo 0 para éxito, 1 para fallo de operación y 2 para argumentos inválidos. Documenta las excepciones. No ocultes errores mediante `|| true` salvo que realmente sean aceptables.
