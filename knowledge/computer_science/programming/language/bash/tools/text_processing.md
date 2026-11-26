---
aliases: ["Procesamiento de texto desde bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25
headerFile: false
modificationDate: 2026-11-25
rating:
tags: [Programming, BashScript, OS/Linux/BASH]
---

# PROCESAMIENTO DE TEXTO DESDE BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html) #WWW/GNU
> - [GNU Grep](https://www.gnu.org/software/grep/manual/)
> - [GNU Sed](https://www.gnu.org/software/sed/manual/)
> - [GNU Awk](https://www.gnu.org/software/gawk/manual/)
> - [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/)

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Tuberías en bash](../io/pipes.md)
> - [Patrones y expresiones regulares en bash](../basics/patterns.md)
> - [Lectura y escritura de archivos en bash](../io/reading_files.md)

## DEFINICIÓN

El procesamiento de texto en la shell suele combinar programas especializados mediante tuberías. No son instrucciones propias del lenguaje Bash: sus opciones y reglas dependen de cada herramienta.

| COMANDO | FUNCIÓN                                        |
|:------- |:---------------------------------------------- |
| `grep`  | Selecciona líneas que coinciden con un patrón. |
| `sed`   | Transforma un flujo de texto.                  |
| `awk`   | Procesa registros y campos.                    |
| `cut`   | Extrae campos o posiciones.                    |
| `sort`  | Ordena líneas.                                 |
| `uniq`  | Agrupa líneas repetidas consecutivas.          |
| `wc`    | Cuenta líneas, palabras o bytes.               |
| `tr`    | Traduce o elimina caracteres.                  |

## GREP Y SED

```bash
printf '%s\n' 'INFO inicio' 'ERROR disco' | grep '^ERROR'
printf '%s\n' 'a-b-a' | sed 's/a/x/g'
# x-b-x
```

`grep -F` busca texto literal y `grep -E` usa regex extendidas. `sed` modifica el flujo por defecto, no el archivo original; opciones como `-i` tienen diferencias entre implementaciones y pueden alterar archivos.

## AWK Y CUT

```bash
printf '%s\n' 'Ana:10' 'Luis:20' | awk -F: '{sum += $2} END {print sum}'
# 30
printf '%s\n' 'Ana:10' 'Luis:20' | cut -d: -f1
```

Las comillas simples protegen `$2` frente a Bash: pertenece al programa `awk`. `-F:` establece el separador de campos. Este formato simple no es un analizador de CSV con comillas y campos complejos.

## CONTAR FRECUENCIAS

```bash
printf '%s\n' rojo azul rojo verde azul rojo | LC_ALL=C sort | uniq -c | sort -nr
```

`uniq` agrupa líneas iguales consecutivas; por eso se ordena antes. `sort -nr` ordena numéricamente en orden descendente. `wc -l` cuenta caracteres de nueva línea; `wc -c` cuenta bytes.

> [!tip] OTROS FORMATOS
> Para JSON utiliza herramientas como `jq` o un lenguaje con un analizador JSON. Evita analizar formatos estructurados complejos mediante expresiones regulares improvisadas.
