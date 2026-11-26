---
aliases: ["Estado de salida en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:46:28
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# ESTADO DE SALIDA EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Exit-Status.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Condicionales en bash](conditionals.md)
> - [Funciones en bash](functions.md)
> - [Gestión de errores en bash](../advanced/error_handling.md)

## DEFINICIÓN

Cada comando devuelve un estado de salida (*exit status*). Bash utiliza ese estado para decidir cómo ejecutar los condicionales, bucles y listas de comandos.

- `0`: éxito según la convención del comando.
- `1` a `255`: otros resultados, frecuentemente errores.
- `126`: Bash encontró el comando, pero no pudo ejecutarlo.
- `127`: Bash no encontró el comando.
- `128 + N`: Bash representa así la terminación por la señal número `N`.

El significado concreto depende del comando; `grep`, por ejemplo, distingue entre encontrar coincidencias (0), no encontrar ninguna (1) y un error (habitualmente 2).

## CONSULTA Y CONTROL

```bash
false
status=$?
printf 'Estado: %d\n' "$status" # 1
```

Guarda `$?` inmediatamente: cualquier orden posterior lo reemplaza.

```bash
if printf 'Hola\n'; then
    printf 'La orden tuvo éxito\n'
fi
false || printf 'La orden falló\n'
```

## EXIT Y RETURN

`exit n` finaliza el shell que ejecuta el script con estado `n`. `return n` termina una función (o un archivo cargado con `source`) y establece su estado de salida. Sin argumento, se utiliza el estado de la última orden ejecutada. Normalmente limita `n` a 0–255.

```bash
is_even() {
    (( $1 % 2 == 0 ))
}
if is_even 4; then
    printf 'Es par\n'
fi
```

Este ejemplo presupone un argumento entero de confianza.

> [!important] NO CONFUNDIR
> Una expresión aritmética cuyo valor es 0 es falsa, pero un comando cuyo estado es 0 se considera exitoso. `((expression))` convierte entre ambas convenciones.
