---
aliases: ["Tipos de datos en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:46:08
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# TIPOS DE DATOS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Operadores aritméticos en bash](arithmetic.md)
> - [Arrays en bash](arrays.md)
> - [Estado de salida en bash](exit_status.md)
> - [Cadenas de texto en bash](strings.md)

## DEFINICIÓN

Bash no dispone de un sistema de tipos como Python o Java. Sus variables escalares almacenan texto; las operaciones y atributos determinan cómo se interpreta. También existen arrays indexados y asociativos.

| DATO             | EJEMPLO          | OBSERVACIÓN                                    |
|:---------------- |:---------------- |:---------------------------------------------- |
| Cadena           | `name='Ana'`     | Puede estar vacía.                             |
| Entero           | `number=42`      | Se interpreta como entero en aritmética.       |
| Decimal          | `pi=3.14`        | Es texto; no existe aritmética decimal nativa. |
| Array indexado   | `values=(10 20)` | Índices enteros.                               |
| Array asociativo | `declare -A map` | Claves de texto no vacías.                     |

## NÚMEROS ENTEROS

```bash
number=7
printf '%s\n' "$((number / 2))" # 3
printf '%s\n' "$((number % 2))" # 1
printf '%s\n' "$((2#1010))"     # 10
printf '%s\n' "$((0xFF))"       # 255
```

Bash realiza aritmética con enteros de ancho fijo, sin comprobar desbordamientos. Una constante con cero inicial se interpreta normalmente como octal: `010` es 8. Valida los datos externos antes de convertirlos.

## NÚMEROS DECIMALES

Para calcular con decimales puedes utilizar un programa externo como `awk`:

```bash
LC_ALL=C awk 'BEGIN {printf "%.2f\n", 7 / 2}'
# 3.50
```

`LC_ALL=C` fija una configuración regional reproducible para este comando. No confundas el formateo de decimales mediante `printf` con la aritmética nativa de Bash.

## VALORES BOOLEANOS

No existe un tipo `bool` nativo. En una expresión aritmética, `0` significa falso y un valor distinto de cero significa verdadero. En cambio, para el estado de salida de un comando, `0` significa éxito y cualquier valor no nulo indica un resultado diferente (por ejemplo, fallo o ausencia de coincidencia).

```bash
if true; then
    printf 'Estado de salida correcto\n'
fi
printf '%s\n' "$((5 > 2))" # 1
```

## LIMITACIÓN DE LAS CADENAS

Una variable no puede contener un byte NUL (`\0`). Para datos binarios utiliza archivos, tuberías o un lenguaje que permita manejar bytes directamente.
