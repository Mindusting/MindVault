---
aliases: ["Argumentos de un script en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:41:46
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# ARGUMENTOS DE UN SCRIPT EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Special-Parameters.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Funciones en bash](functions.md)
> - [Arrays en bash](arrays.md)
> - [Opciones de línea de comandos en bash](../advanced/command_line_options.md)

## DEFINICIÓN

Los argumentos son valores que se proporcionan al ejecutar un script o al llamar a una función. Bash los expone como parámetros posicionales.

| PARÁMETRO  | SIGNIFICADO                                     |
|:---------- |:----------------------------------------------- |
| `$0`       | Nombre con el que se inició el script o shell.  |
| `$1`, `$2` | Primer y segundo argumento.                     |
| `${10}`    | Décimo argumento (necesita llaves).             |
| `$#`       | Cantidad de argumentos.                         |
| `"$@"`     | Argumentos independientes, incluso vacíos.      |
| `"$*"`     | Una cadena que agrupa los argumentos.           |
| `$?`       | Estado de salida de la última orden o pipeline. |
| `$$`       | PID del shell original.                         |
| `$!`       | PID del último trabajo en segundo plano.        |

## EJEMPLO

Guarda como `greet.sh`:

```bash
#!/usr/bin/env bash
if (( $# != 1 )); then
    printf 'Uso: %s NOMBRE\n' "$0" >&2
    exit 2
fi
printf 'Hola %s\n' "$1"
```

```bash
bash greet.sh 'Ana García'
# Hola Ana García
```

## RECORRER Y DESPLAZAR

```bash
for argument in "$@"; do
    printf '<%s>\n' "$argument"
done
if (( $# > 0 )); then
    shift
fi
```

`shift` elimina el primer parámetro y desplaza los demás; `shift n` elimina los primeros `n`. No modifica `$0`. `set --` permite reemplazar los parámetros posicionales.

```bash
set -- 'uno dos' '' tres
printf '<%s>\n' "$@"
# <uno dos>
# <>
# <tres>
```

> [!tip] REENVIAR ARGUMENTOS
> Para llamar a otro programa conservando exactamente los argumentos, usa `program "$@"`, no `program $*`.
