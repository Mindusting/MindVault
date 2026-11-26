---
aliases: ["Funciones en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:47:51
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# FUNCIONES EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Functions.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Argumentos de un script en bash](arguments.md)
> - [Estado de salida en bash](exit_status.md)
> - [Estructura de un script en bash](../advanced/script_structure.md)

## DEFINICIÓN

Una función agrupa comandos reutilizables bajo un nombre. Bash ejecuta las funciones normalmente en el shell actual; una función no es un programa externo independiente.

> [!abstract] SINTAXIS
> 
> ```bash
> function_name() {
>     commands
> }
> function_name argument1 argument2
> ```

También existe `function name {...; }`, pero la primera forma es compatible con más shells. La definición debe haberse ejecutado antes de llamar a la función.

## PARÁMETROS Y VARIABLES LOCALES

```bash
greet() {
    local name=$1
    printf 'Hola %s\n' "$name"
}
greet 'Ana García'
```

Los parámetros posicionales se sustituyen durante la llamada y se restauran al terminar. `local` evita modificar una variable homónima fuera de la función. Bash emplea ámbito dinámico: una función llamada desde otra puede ver sus variables locales si no las oculta.

## DEVOLVER ESTADO O DATOS

```bash
is_file() {
    [[ -f $1 ]]
}
if is_file 'report.txt'; then
    printf 'Existe\n'
fi
```

`return` devuelve un estado, no un entero arbitrario ni una cadena. Para producir datos, escribe en stdout y captura mediante sustitución de comandos:

```bash
join_words() {
    printf '%s-%s\n' "$1" "$2"
}
result=$(join_words 'hello' 'world')
printf '%s\n' "$result"
```

`$(...)` ejecuta la función en un entorno de subshell: las modificaciones a variables no se conservan en el padre. Los mensajes de diagnóstico deben ir a stderr para no contaminar los datos.

## COMPROBAR ERRORES

```bash
get_date() {
    local result
    if ! result=$(date +%F); then
        printf 'No se pudo obtener la fecha\n' >&2
        return 1
    fi
    printf '%s\n' "$result"
}
get_date
```

Declara `local result` y realiza la asignación separadamente cuando necesites conocer el estado de la orden: `local result=$(command)` puede ocultar ese estado.
