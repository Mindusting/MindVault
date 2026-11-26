---
aliases: ["Comandos en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:43:54
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# COMANDOS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Simple-Commands.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Estado de salida en bash](exit_status.md)
> - [Redirecciones en bash](../io/redirections.md)
> - [Variables de entorno en bash](../environment/environment_variables.md)

## DEFINICIÓN

Bash lee una orden, interpreta su sintaxis, realiza las expansiones correspondientes y ejecuta el comando con sus argumentos. Un comando puede ser una función, un comando integrado (*builtin*) o un programa externo, entre otros casos.

> [!abstract] SINTAXIS
> 
> ```bash
> command option argument
> ```

Las opciones pertenecen al programa que se ejecuta; no existe una sintaxis universal de opciones impuesta por Bash.

```bash
printf '%s\n' 'Hola mundo'
ls -l -- "$HOME"
type cd
type -a printf
command -v bash
```

`type` informa de cómo interpreta Bash un nombre; `command -v` permite comprobar si un comando está disponible. `cd`, por ejemplo, debe afectar al directorio del propio intérprete; un proceso externo no podría cambiar el directorio de su padre.

## PATH

`PATH` contiene directorios separados por `:`. Si una orden no incluye `/` y se resuelve como programa externo, Bash busca en esos directorios (puede utilizar una ruta previamente memorizada). Una ruta como `./script.sh` evita esa búsqueda.

## AGRUPACIÓN Y SECUENCIAS

```bash
printf 'Primero\n'; printf 'Segundo\n'
printf 'Correcto\n' && printf 'Se ejecutó bien\n'
false || printf 'Se produjo un fallo\n'
```

`;` separa órdenes, `&&` ejecuta la derecha si la izquierda tiene éxito, y `||` si falla. No son equivalentes a concatenar texto.

> [!tip] AYUDA
> `help read` muestra ayuda de un builtin; `man ls` documenta el programa externo. `type -a nombre` ayuda cuando existen varias implementaciones.
