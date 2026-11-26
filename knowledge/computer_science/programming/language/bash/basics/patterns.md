---
aliases: ["Patrones y expresiones regulares en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:49:31
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# PATRONES Y EXPRESIONES REGULARES EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Pattern-Matching.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Condicionales en bash](conditionals.md)
> - [Expansiones en bash](expansions.md)
> - [Procesamiento de texto desde bash](../tools/text_processing.md)

## DEFINICIÓN

Bash emplea patrones de shell (*glob*) para nombres de archivo, `case` y algunas expansiones. Las expresiones regulares (regex) son otro lenguaje de patrones, disponible en `[[ ... =~ ... ]]`.

|   GLOB   | SIGNIFICADO                               |
|:--------:|:----------------------------------------- |
|   `*`    | Cero o más caracteres.                    |
|   `?`    | Exactamente un carácter.                  |
| `[abc]`  | Un carácter del conjunto.                 |
| `[0-9]`  | Un carácter del rango.                    |
| `[!abc]` | Un carácter que no pertenece al conjunto. |

```bash
file='report.txt'
if [[ $file == *.txt ]]; then
    printf 'Archivo de texto\n'
fi
```

En `[[ ]]`, entrecomillar el patrón completo de `==` provoca una comparación literal. En la expansión de rutas, los patrones ordinarios no atraviesan `/` y normalmente no incluyen nombres que empiezan por `.` si el punto no se indica explícitamente.

## OPCIONES DE GLOBBING

```bash
(
    shopt -s nullglob dotglob
    files=(./*.txt)
    printf 'Cantidad: %d\n' "${#files[@]}"
)
```

`nullglob` elimina patrones sin coincidencias; `failglob` genera un error; `dotglob` incluye archivos ocultos; `globstar` habilita el uso recursivo de `**` (Bash 4+). El subshell evita cambiar las opciones del shell exterior.

## REGEX

```bash
value='ID-123'
pattern='^ID-([0-9]+)$'
if [[ $value =~ $pattern ]]; then
    printf 'Número: %s\n' "${BASH_REMATCH[1]}"
fi
```

`=~` utiliza expresiones regulares extendidas (ERE). `^` y `$` anclan inicio y final. `BASH_REMATCH[0]` guarda la coincidencia completa; los siguientes elementos contienen grupos capturados. No entrecomilles toda la expansión del patrón si quieres que funcione como regex.

> [!note] DIFERENCIA
> En glob, `*` significa cualquier secuencia. En regex, `*` repite el elemento anterior; el equivalente aproximado de glob `*` es regex `.*`.
