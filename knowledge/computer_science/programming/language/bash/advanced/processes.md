---
aliases: ["Procesos, subshells y trabajos en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:38:12
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# PROCESOS, SUBSHELLS Y TRABAJOS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Job-Control-Basics.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Señales y trap en bash](traps.md)
> - [Tuberías en bash](../io/pipes.md)
> - [Variables de entorno en bash](../environment/environment_variables.md)

## DEFINICIÓN

Un proceso es una instancia de un programa en ejecución. Un shell puede lanzar procesos hijos y esperar a que terminen. Un subshell es un entorno de ejecución separado de Bash; las modificaciones de su estado normalmente no regresan al shell padre.

## AGRUPAR COMANDOS

```bash
value='original'
( value='subshell'; printf '%s\n' "$value" )
printf '%s\n' "$value" # original
{ value='actual'; printf '%s\n' "$value"; }
printf '%s\n' "$value" # actual
```

Los paréntesis crean un subshell; las llaves agrupan órdenes en el shell actual (si no están, por ejemplo, dentro de un pipeline). Las llaves requieren separación y una nueva línea o `;` antes de cerrar.

## SEGUNDO PLANO

```bash
sleep 1 &
worker_pid=$!
printf 'PID: %s\n' "$worker_pid"
if wait "$worker_pid"; then
    printf 'Proceso completado\n'
fi
```

`&` inicia una tarea asíncrona y `$!` permite identificarla. El estado inicial de la lista asíncrona no es el resultado final del proceso; `wait` espera y recupera su estado.

En una sesión interactiva, `jobs` muestra trabajos; `fg %1` trae un trabajo al primer plano; `bg %1` continúa un trabajo detenido en segundo plano. El número de trabajo no es un PID. Ctrl+C suele enviar SIGINT al grupo de primer plano y Ctrl+Z suele enviar SIGTSTP; no son simples órdenes de Bash.

## SEÑALES

`kill -TERM PID` solicita la terminación de un proceso identificado. Usa el PID que hayas guardado y evita señales sobre procesos ajenos. SIGKILL (`kill -KILL`) no puede ser capturada y no permite limpieza normal. `trap` permite reaccionar a señales capturables.

## PID Y EXEC

`$$` representa el PID del shell original incluso dentro de muchos subshells; `$BASHPID` identifica el proceso Bash actual. `exec command` reemplaza el proceso shell por el programa sin volver a la siguiente instrucción si tiene éxito.
