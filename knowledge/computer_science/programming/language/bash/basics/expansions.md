---
aliases: ["Expansiones en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:46:52
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# EXPANSIONES EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Comillas y caracteres de escape en bash](quoting.md)
> - [Expansión de parámetros en bash](parameter_expansion.md)
> - [Patrones y expresiones regulares en bash](patterns.md)
> - [Tuberías en bash](../io/pipes.md)

## DEFINICIÓN

Las expansiones transforman partes de una orden antes de ejecutar el comando. Por ejemplo, `$HOME` se sustituye por el valor de la variable y `*.txt` por los nombres que coinciden con el patrón.

| EXPANSIÓN               | EJEMPLO         |
|:----------------------- |:--------------- |
| Llaves                  | `file{1,2}.txt` |
| Tilde                   | `~/Documents`   |
| Parámetros              | `${name}`       |
| Sustitución de comandos | `$(date +%F)`   |
| Aritmética              | `$((2 + 3))`    |
| Nombres de archivos     | `*.txt`         |

## ORDEN DE EVALUACIÓN

1. Expansión de llaves.
2. Tilde, parámetros y variables, sustitución de comandos, aritmética y, cuando está disponible, sustitución de procesos (las expansiones pertinentes se realizan de izquierda a derecha).
3. División en palabras.
4. Expansión de nombres de archivos.
5. Eliminación de las comillas sintácticas.

Las comillas y el contexto pueden impedir algunas fases. Las asignaciones simples, por ejemplo, no realizan la división en palabras ni la expansión de nombres sobre el valor asignado.

## LLAVES Y TILDE

```bash
printf '%s\n' file{1..3}.txt
# file1.txt
# file2.txt
# file3.txt
printf '%s\n' ~/Documents
```

La expansión de llaves se realiza antes de expandir variables: `{1..$limit}` no es un rango dinámico. Usa un bucle aritmético para ello.

## SUSTITUCIÓN DE COMANDOS

```bash
current_date=$(date +%F)
printf 'Fecha: %s\n' "$current_date"
```

`$(...)` ejecuta una orden en un entorno de subshell y sustituye la expresión por su salida estándar, eliminando los saltos de línea finales. No captura automáticamente stderr y tampoco devuelve el código de salida como texto.

## NOTAS

Bash no vuelve a interpretar arbitrariamente el resultado de una variable como código. Evita `eval` para intentar construir órdenes dinámicas: usa arrays de argumentos.
