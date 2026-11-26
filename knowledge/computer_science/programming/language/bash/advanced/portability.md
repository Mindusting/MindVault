---
aliases: ["Compatibilidad entre bash y sh"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:36:57
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# COMPATIBILIDAD ENTRE BASH Y SH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Bash-POSIX-Mode.html) #WWW/GNU
> - [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Primer programa en bash](../basics/first_program.md)
> - [Arrays en bash](../basics/arrays.md)
> - [Archivos de inicio de bash](../environment/startup_files.md)

## DEFINICIÓN

Bash es una implementación de shell con extensiones propias. POSIX especifica un conjunto de comportamientos comunes; `/bin/sh` puede apuntar a otra implementación. Por ejemplo, en muchas distribuciones basadas en Debian apunta a Dash.

| CONSTRUCCIÓN           | BASH | SH POSIX TRADICIONAL |
|:---------------------- |:----:|:--------------------:|
| `[...]`, `case`, `for` |  Sí  |          Sí          |
| `$(...)`, `$((...))`   |  Sí  |          Sí          |
| `[[ ... ]]`, `((...))` |  Sí  |          No          |
| Arrays, `mapfile`      |  Sí  |          No          |
| `<(command)`, `<<<`    |  Sí  |          No          |
| `source file`          |  Sí  |  No (usar `. file`)  |
| `local`                |  Sí  |    No garantizado    |

Algunas extensiones pueden existir en otros shells sin ser portables a todos ellos. Si necesitas `sh`, consulta el estándar objetivo y prueba con las implementaciones previstas.

## VERSIONES

```bash
printf '%s\n' "$BASH_VERSION"
if (( BASH_VERSINFO[0] < 4 )); then
    printf 'Se necesita Bash 4 o posterior\n' >&2
    exit 1
fi
```

Los arrays asociativos, `mapfile` y ciertas transformaciones de cadenas requieren Bash 4+. Algunas características más avanzadas requieren versiones posteriores.

## EJECUCIÓN

Usa `bash script.sh` o el shebang de Bash para un script de Bash. `sh script.sh` obliga a usar `sh` independientemente de lo que indique el shebang. El modo POSIX de Bash cambia determinados comportamientos, pero no demuestra por sí solo que el script sea portable.

> [!note] ALCANCE
> Estos apuntes se orientan a Bash 5.x sobre GNU/Linux. Se señalan extensiones y dependencias externas relevantes sin intentar cubrir todas las plataformas.
