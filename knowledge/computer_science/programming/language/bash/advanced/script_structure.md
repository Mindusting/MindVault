---
aliases: ["Estructura de un script en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:38:25
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# ESTRUCTURA DE UN SCRIPT EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Funciones en bash](../basics/functions.md)
> - [Opciones de línea de comandos en bash](command_line_options.md)
> - [Depuración y pruebas de scripts bash](debugging.md)

## DEFINICIÓN

En scripts pequeños se pueden escribir órdenes consecutivas. Cuando crecen, separar configuración, funciones, validación y punto de entrada hace que el código sea más fácil de probar y mantener.

## PUNTO DE ENTRADA

```bash
#!/usr/bin/env bash
usage() {
    printf 'Uso: %s ARCHIVO\n' "$0" >&2
}
main() {
    if (( $# != 1 )); then
        usage
        return 2
    fi
    if [[ ! -f $1 ]]; then
        printf 'No es un archivo regular: %s\n' "$1" >&2
        return 1
    fi
    wc -l -- "$1"
}
main "$@"
```

El estado de la última orden (`main`) es el estado del script. `wc -l` cuenta saltos de línea, no necesariamente líneas lógicas si falta el último salto.

## MÓDULOS MEDIANTE SOURCE

Una organización posible:

```text
project/
|- main.sh
|- lib/
|  |- strings.sh
|- tests/
   |- test_strings.sh
```

`lib/strings.sh` puede contener funciones sin ejecutar operaciones al cargarse. Para cargarlo desde `main.sh` sin depender del directorio de trabajo actual:

```bash
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P) || exit 1
source "$script_dir/lib/strings.sh" || exit 1
```

Esto presupone un script iniciado con una ruta que identifica su ubicación; si lo invocas mediante un enlace simbólico, puede localizar el directorio del enlace y no el del archivo original. No cargues rutas que pueda modificar un usuario no confiable.

## ESTILO

- Usa nombres significativos (`source_dir`, `destination_file`).
- Reserva mayúsculas para constantes convencionales y variables de entorno, evitando colisiones con variables especiales de Bash.
- Indenta con cuatro espacios y separa funciones por una línea vacía.
- Usa `local` en funciones y `printf` para resultados.
- Mantén separadas la lógica y la interacción con el usuario.
