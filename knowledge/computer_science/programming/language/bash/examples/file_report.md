---
aliases: ["Ejemplo: informe de archivos en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:54:19
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# EJEMPLO: INFORME DE ARCHIVOS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Gestión de archivos y directorios en bash](../tools/file_management.md)
> - [Estructura de un script en bash](../advanced/script_structure.md)
> - [Tuberías en bash](../io/pipes.md)

## OBJETIVO

Crear un script que reciba un directorio y cuente sus archivos Markdown regulares (incluidos los de subdirectorios). No modificará los archivos originales y debe admitir rutas con espacios y saltos de línea.

## CÓDIGO

Guarda como `file_report.sh`:

```bash
#!/usr/bin/env bash

main() {
    if (( $# != 1 )); then
        printf 'Uso: %s DIRECTORIO\n' "$0" >&2
        return 2
    fi

    local directory=$1
    local count
    if [[ ! -d $directory ]]; then
        printf 'Directorio no válido: %s\n' "$directory" >&2
        return 1
    fi

    # Evita que find interprete una ruta relativa como una opción.
    if [[ $directory != /* ]]; then
        directory=./$directory
    fi

    # GNU find imprime un punto por archivo, no el nombre.
    # pipefail permite detectar también un fallo de find.
    if ! count=$(set -o pipefail; find "$directory" -type f -name '*.md' -printf '.' | wc -c); then
        printf 'No se pudo completar la búsqueda\n' >&2
        return 1
    fi
    printf 'Archivos Markdown: %s\n' "$count"
}

main "$@"
```

## EXPLICACIÓN

`$#` valida la cantidad de argumentos. `[[ -d ... ]]` comprueba si la ruta es un directorio. `find` busca archivos regulares y emite un byte por coincidencia; `wc -c` cuenta esos bytes. Así no se confunden los saltos de línea de los nombres de archivo con separadores. No sigue enlaces simbólicos a directorios por defecto; la búsqueda necesita permisos suficientes.

La sustitución de comandos captura el resultado; `pipefail` se activa dentro de ella sin afectar al shell exterior. Ante un fallo de búsqueda no se presenta un recuento parcial como correcto.

## PRUEBAS

```bash
mkdir -p 'demo report/sub'
touch 'demo report/a.md' 'demo report/sub/b.md' 'demo report/c.txt'
bash file_report.sh 'demo report'
# Archivos Markdown: 2
bash file_report.sh
# Uso: file_report.sh DIRECTORIO (stderr; estado 2)
```

Realiza las pruebas en un directorio nuevo que no contenga datos importantes. Se puede extender el informe para aceptar una extensión como argumento o contar archivos de varios tipos.
