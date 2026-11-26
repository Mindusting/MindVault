---
aliases: ["Tuberías en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:54:34
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# TUBERÍAS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Flujos y descriptores de archivo](streams.md)
> - [Redirecciones en bash](redirections.md)
> - [Procesos, subshells y trabajos en bash](../advanced/processes.md)
> - [Gestión de errores en bash](../advanced/error_handling.md)

## DEFINICIÓN

Una tubería (*pipe*) conecta stdout de un comando a stdin del siguiente. Permite procesar datos de manera incremental, sin tener que guardar todos los resultados intermedios en archivos.

> [!abstract] SINTAXIS
> 
> ```bash
> command1 | command2 | command3
> ```

```bash
printf '%s\n' pera manzana pera | sort | uniq -c
# 1 manzana
# 2 pera
```

Los comandos de un pipeline pueden ejecutarse concurrentemente. `|` no conecta stderr por defecto; `|&` también conecta stderr (equivale a añadir `2>&1` después de las redirecciones del primer comando).

## ESTADO DE SALIDA

```bash
false | true
printf '%d\n' "$?" # 0 por defecto
(
    set -o pipefail
    false | true
    printf '%d\n' "$?" # 1
)
false | true
printf '%s\n' "${PIPESTATUS[@]}" # 1 y 0
```

Sin `pipefail`, el estado es el del último comando. Con `pipefail`, es el del comando no exitoso situado más a la derecha, o cero si todos tienen éxito. `PIPESTATUS` contiene los estados individuales; léelo antes de ejecutar otra orden. Algunos pipelines terminan deliberadamente antes de consumir toda la entrada, lo que puede provocar SIGPIPE aguas arriba.

## SUBSHELL Y VARIABLES

```bash
count=0
printf '%s\n' A B | while IFS= read -r line; do
    count=$((count + 1))
done
printf '%d\n' "$count" # normalmente 0
```

Normalmente cada parte se ejecuta en un entorno de subshell; la opción `lastpipe`, con control de trabajos desactivado, puede cambiar el comportamiento del último elemento.

```bash
count=0
while IFS= read -r line; do
    count=$((count + 1))
done < <(printf '%s\n' A B)
printf '%d\n' "$count" # 2
```

`<(command)` presenta la salida de una orden como una ruta legible; `<` la conecta a stdin del bucle. Es sustitución de procesos, una extensión de Bash que necesita soporte del sistema. El estado de su productor no se incorpora automáticamente a `$?` del consumidor; si importa el error de ese productor, compruébalo por separado.
