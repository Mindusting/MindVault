---
aliases: ["Variables en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:51:20
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# VARIABLES EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameters.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Tipos de datos en bash](data_types.md)
> - [Comillas y caracteres de escape en bash](quoting.md)
> - [Funciones en bash](functions.md)
> - [Variables de entorno en bash](../environment/environment_variables.md)

## DEFINICIÓN

Una variable permite asociar un nombre a un valor. En Bash, las variables escalares contienen cadenas de caracteres; determinados atributos y contextos permiten tratarlas como enteros. No se declara un tipo estático como en C o Java.

> [!abstract] SINTAXIS
> 
> ```bash
> variable=value
> printf '%s\n' "$variable"
> printf '%s\n' "${variable}"
> ```

No pueden existir espacios alrededor del `=` en una asignación simple. El nombre comienza por una letra ASCII o `_` y puede contener letras ASCII, números y `_`.

```bash
name='Ana García'
age=20
printf 'Nombre: %s; edad: %s\n' "$name" "$age"
file='report'
printf '%s\n' "${file}_2026.txt"
```

Las llaves delimitan el nombre: `$file_2026` buscaría otra variable.

## DECLARAR, MODIFICAR Y ELIMINAR

```bash
counter=1
counter=2
readonly application_name='MyApp'
declare -i total=0
total=5+3
printf '%s\n' "$total" # 8
unset counter
```

`readonly` impide reasignar o eliminar la variable; `declare -i` activa la evaluación aritmética en las asignaciones. No convierte Bash en un lenguaje con tipos estáticos. Una variable vacía (`name=''`) sigue estando definida; una variable eliminada con `unset` no.

## ÁMBITO

Una variable ordinaria pertenece al intérprete actual. `export` la incorpora al entorno de los procesos que lance posteriormente; `local` crea una variable local dentro de una función. Un proceso hijo no puede cambiar directamente las variables de su padre.

> [!important] COMILLAS
> Como regla general, utiliza `"$variable"` al pasar valores como argumentos para evitar la división en palabras y la expansión de comodines.

## EJERCICIO

Crea una variable que contenga tu nombre completo y úsala para construir un nombre de archivo con un sufijo mediante `${variable}`.
