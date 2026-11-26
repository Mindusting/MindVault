---
aliases: ["Comillas y caracteres de escape en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:49:50
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# COMILLAS Y CARACTERES DE ESCAPE EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Quoting.html) #WWW/GNU
> - [ShellCheck SC2086](https://www.shellcheck.net/wiki/SC2086)

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Expansiones en bash](expansions.md)
> - [Arrays en bash](arrays.md)
> - [Argumentos de un script en bash](arguments.md)

## DEFINICIÓN

Las comillas controlan cómo interpreta Bash los caracteres. No son parte del valor salvo que se incluyan explícitamente como datos.

| SINTAXIS     | COMPORTAMIENTO                                                                  |
|:------------ |:------------------------------------------------------------------------------- |
| `'texto'`    | Conserva todos los caracteres literalmente.                                     |
| `"texto"`    | Conserva espacios y comodines, permite expansiones como `$name` y `$(command)`. |
| `\x`         | Protege el carácter siguiente (una nueva línea escapada es una continuación).   |
| `$'texto\n'` | Interpreta secuencias de escape como `\n` y `\t`.                               |

```bash
name='Ana García'
printf '%s\n' '$name'  # $name
printf '%s\n' "$name"  # Ana García
printf '%s\n' "Dijo: \"hola\""
printf '%s' $'A\nB\n'
```

Dentro de comillas simples no puedes escapar otra comilla simple mediante `\`. Puedes concatenar fragmentos: `'It'\''s fine'` o usar comillas dobles.

## DIVISIÓN EN PALABRAS Y COMODINES

```bash
name='Ana García'
printf '<%s>\n' $name
# <Ana>
# <García>
printf '<%s>\n' "$name"
# <Ana García>
```

Sin comillas, el resultado de una expansión puede dividirse según `IFS` y, después, interpretarse como patrón de nombres de archivo. El problema no se limita a los espacios; también afecta a los valores vacíos, tabuladores, saltos de línea y comodines.

## ARGUMENTOS Y ARRAYS

```bash
args=('uno dos' '*' '')
printf '<%s>\n' "${args[@]}"
# <uno dos>
# <*>
# <>
```

`"$@"` conserva los argumentos de un script del mismo modo que `"${args[@]}"` conserva los elementos de un array. No uses una cadena con opciones y argumentos como sustituto de un array.

> [!important] REGLA GENERAL
> Protege con comillas dobles las expansiones que representen datos. Deja un patrón sin comillas solo cuando busques deliberadamente ese comportamiento, por ejemplo `*.txt`.
