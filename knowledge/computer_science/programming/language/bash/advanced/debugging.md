---
aliases: ["Depuración y pruebas de scripts bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:32:18
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# DEPURACIÓN Y PRUEBAS DE SCRIPTS BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Invoking-Bash.html) #WWW/GNU
> - [ShellCheck](https://www.shellcheck.net/)
> - [Bats](https://bats-core.readthedocs.io/)

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Gestión de errores en bash](error_handling.md)
> - [Estructura de un script en bash](script_structure.md)

## DEFINICIÓN

Depurar es localizar el motivo por el que un script no se comporta como se esperaba. Conviene separar errores de sintaxis, errores de ejecución y resultados lógicos incorrectos.

## COMPROBAR Y TRAZAR

```bash
bash -n script.sh
bash -x script.sh
```

`-n` verifica sintaxis sin ejecutar las órdenes habituales; no demuestra que el código funcione ni comprueba automáticamente archivos que se cargarían con `source`. `-x` ejecuta realmente el script y muestra órdenes expandidas; no lo uses con scripts peligrosos o secretos.

```bash
PS4='+ ${BASH_SOURCE[0]}:${LINENO}: '
set -x
value='demo'
printf '%s\n' "$value"
set +x
```

`PS4` configura el prefijo de las trazas. `set +x` las desactiva.

## SHELLCHECK

En Linux Mint, Ubuntu o Debian puedes instalar ShellCheck desde sus repositorios si está disponible:

```bash
sudo apt install shellcheck
shellcheck script.sh
```

ShellCheck analiza código estáticamente y señala problemas como expansiones sin comillas o `read` sin `-r`. Una advertencia requiere comprender el contexto; no la suprimas automáticamente.

## PRUEBAS SIMPLES

```bash
is_even() {
    (( $1 % 2 == 0 ))
}
if is_even 4 && ! is_even 5; then
    printf 'Prueba correcta\n'
else
    printf 'Prueba fallida\n' >&2
    exit 1
fi
```

Prueba argumentos vacíos, rutas con espacios, archivos inexistentes y permisos insuficientes. Para scripts mayores puedes usar Bats, que permite escribir casos de prueba automatizados.
