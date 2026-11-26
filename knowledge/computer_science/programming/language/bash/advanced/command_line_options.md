---
aliases: ["Opciones de línea de comandos en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:28:52
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# OPCIONES DE LÍNEA DE COMANDOS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Argumentos de un script en bash](../basics/arguments.md)
> - [Condicionales en bash](../basics/conditionals.md)
> - [Estructura de un script en bash](script_structure.md)

## DEFINICIÓN

Una interfaz de línea de comandos suele separar opciones (`-v`, `-o FILE`) y operandos. Bash proporciona `getopts` para procesar opciones cortas de forma estructurada.

## GETOPTS

Guarda como `greet.sh`:

```bash
#!/usr/bin/env bash
usage() {
    printf 'Uso: %s [-v] [-n NOMBRE]\n' "$0"
}
name='Invitado'
verbose=0
while getopts ':vn:h' option; do
    case $option in
        v) verbose=1 ;;
        n) name=$OPTARG ;;
        h) usage; exit 0 ;;
        :) printf 'Falta argumento para -%s\n' "$OPTARG" >&2; exit 2 ;;
        \?) printf 'Opción desconocida: -%s\n' "$OPTARG" >&2; exit 2 ;;
    esac
done
shift "$((OPTIND - 1))"
if (( $# != 0 )); then
    usage >&2
    exit 2
fi
if (( verbose )); then
    printf 'Modo detallado\n' >&2
fi
printf 'Hola %s\n' "$name"
```

`n:` significa que `-n` necesita un argumento; `v` no lo necesita. El `:` inicial activa el manejo silencioso de errores; `OPTARG` contiene el argumento o la opción problemática, y `OPTIND` el índice siguiente. Si quieres analizar otro conjunto de opciones en el mismo shell, reinicia `OPTIND=1` antes.

```bash
bash greet.sh -v -n 'Ana García'
bash greet.sh -h
```

## OPCIONES LARGAS

`getopts` no analiza `--name` de forma nativa. Puedes usar un bucle `while` con `case` que valide el número de argumentos antes de `shift`, o un analizador externo. Define `--` para señalar el fin de las opciones cuando sea pertinente.

> [!tip] DISEÑO
> Incluye una ayuda `-h` o `--help`, valida los parámetros y envía diagnósticos a stderr. No construyas una cadena para ejecutarla mediante `eval`.
