---
aliases: ["Entrada y salida en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:48:04
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# ENTRADA Y SALIDA EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html) #WWW/GNU
> - [ShellCheck SC2162](https://www.shellcheck.net/wiki/SC2162)

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Flujos y descriptores de archivo](../io/streams.md)
> - [Lectura y escritura de archivos en bash](../io/reading_files.md)
> - [Comillas y caracteres de escape en bash](quoting.md)

## DEFINICIÓN

Un script suele comunicarse mediante entrada estándar (stdin), salida estándar (stdout) y salida de errores (stderr). `read` obtiene datos; `printf` permite escribirlos con formato.

## PRINTF

> [!abstract] SINTAXIS
> 
> ```bash
> printf 'format' argument1 argument2
> ```

```bash
name='Ana'
printf 'Hola %s\n' "$name"
printf 'ID: %04d\n' 7
printf 'Progreso: %d%%\n' 50
```

| FORMATO | SIGNIFICADO                                                  |
|:------- |:------------------------------------------------------------ |
| `%s`    | Cadena.                                                      |
| `%d`    | Entero decimal.                                              |
| `%04d`  | Entero con al menos cuatro posiciones, rellenadas con ceros. |
| `%f`    | Número en formato decimal.                                   |
| `%%`    | Signo de porcentaje literal.                                 |

`printf` no añade salto de línea automáticamente. Es preferible a `echo` cuando se necesita control del formato o texto arbitrario. Usa `printf '%s\n' "$text"`, no `printf "$text"`: el contenido no debe controlar el formato.

## READ

```bash
printf 'Escribe tu nombre: '
if IFS= read -r name; then
    printf 'Hola %s\n' "$name"
else
    printf 'No se pudo leer la entrada\n' >&2
fi
```

`IFS=` conserva espacios iniciales y finales; `-r` conserva las barras invertidas. `read` devuelve un estado distinto de cero al encontrar EOF antes de completar la lectura.

| OPCIÓN       | DESCRIPCIÓN                                         |
|:------------ |:--------------------------------------------------- |
| `-r`         | No interpreta barras invertidas.                    |
| `-p`         | Muestra un prompt si la entrada es un terminal.     |
| `-s`         | Oculta los caracteres si la entrada es un terminal. |
| `-t seconds` | Limita el tiempo de espera.                         |
| `-a array`   | Guarda las palabras en un array indexado.           |

```bash
read -r -s -p 'Contraseña (demostración): ' password
printf '\n'
unset password
```

No imprimas ni registres contraseñas. Ocultar la entrada no cifra ni protege el valor en memoria.
