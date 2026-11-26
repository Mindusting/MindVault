---
aliases: ["Señales y trap en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:39:16
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# SEÑALES Y TRAP EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Procesos, subshells y trabajos en bash](processes.md)
> - [Gestión de errores en bash](error_handling.md)
> - [Gestión de archivos y directorios en bash](../tools/file_management.md)

## DEFINICIÓN

`trap` registra una acción para ciertas señales o eventos del shell. Resulta útil para eliminar archivos temporales y terminar de forma ordenada.

> [!abstract] SINTAXIS
> 
> ```bash
> trap 'commands' SIGNAL
> trap - SIGNAL
> ```

La segunda forma restaura la disposición original de la señal. `EXIT` es un evento de Bash, no una señal del sistema operativo.

## LIMPIEZA DE ARCHIVOS TEMPORALES

```bash
#!/usr/bin/env bash
tmp_dir=$(mktemp -d) || exit 1
cleanup() {
    rm -rf -- "$tmp_dir"
}
trap cleanup EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
printf 'Datos temporales\n' > "$tmp_dir/data.txt" || exit 1
cat -- "$tmp_dir/data.txt"
```

`mktemp -d` crea un directorio temporal con nombre impredecible. Aquí la limpieza se limita al directorio obtenido de una creación correcta y nunca se reutiliza la variable. Evita `rm -rf` con rutas de usuario o variables cuyo valor no puedas garantizar.

`EXIT` se ejecuta cuando el shell termina normalmente o mediante `exit`; las trampas INT y TERM convierten esas señales en una salida que permite realizar la limpieza. No hay garantía de limpieza ante SIGKILL, un apagado abrupto o determinados fallos del sistema.

## EXPANSIÓN AL REGISTRAR O EJECUTAR

```bash
value='inicial'
trap 'printf "%s\n" "$value"' EXIT
value='final'
```

La acción entre comillas simples expande `$value` cuando se ejecuta la trampa, no cuando se registra. Ejecuta este ejemplo en un script separado.

## ERR, DEBUG Y RETURN

Bash también permite registrar trampas para `ERR`, `DEBUG` y `RETURN`. `ERR` tiene excepciones similares a `set -e`; no es un mecanismo universal de excepciones. `DEBUG` y `RETURN` son útiles para instrumentación avanzada.
