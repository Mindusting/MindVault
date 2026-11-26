---
aliases: ["Primer programa en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:47:37
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# PRIMER PROGRAMA EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Scripts.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Comentarios en bash](comments.md)
> - [Comandos en bash](commands.md)
> - [Entrada y salida en bash](input_output.md)

## DEFINICIÓN

Un **script de Bash** es un archivo de texto que contiene instrucciones que Bash interpreta. Puede ejecutar programas externos, manipular variables y controlar qué instrucciones se ejecutan. No necesita compilarse antes de ejecutarse.

La extensión `.sh` es una convención, no un requisito ni una garantía de que el intérprete sea Bash.

## SHEBANG

> [!abstract] SINTAXIS
> 
> ```bash
> #!/bin/bash
> ```

La primera línea, llamada *shebang*, indica al sistema qué intérprete usar al ejecutar el archivo directamente. Debe comenzar exactamente por `#!`, sin espacios entre ambos caracteres y sin líneas anteriores.

También se puede usar `#!/usr/bin/env bash`, que busca Bash en `PATH`. En Linux, `/bin/bash` es habitual; `env` facilita usar otras instalaciones, pero depende del entorno.

## HOLA MUNDO

Guarda el siguiente contenido en `hello.sh`:

```bash
#!/usr/bin/env bash
# Author: Mindusting

printf 'Hola mundo!!!\n'
```

Desde el directorio que contiene el archivo:

```bash
bash hello.sh
chmod u+x hello.sh
./hello.sh
```

La primera orden ejecuta Bash explícitamente y no necesita permiso de ejecución en el archivo (sí de lectura). Las otras dos habilitan la ejecución para el propietario y lo ejecutan mediante el shebang. `./` indica una ruta relativa al directorio actual; sin ella, Bash buscaría `hello.sh` en `PATH`.

## EJECUTAR O CARGAR

| INSTRUCCIÓN       | COMPORTAMIENTO                               |
|:----------------- |:-------------------------------------------- |
| `bash hello.sh`   | Inicia otro Bash.                            |
| `./hello.sh`      | Ejecuta el archivo usando su intérprete.     |
| `source hello.sh` | Ejecuta las instrucciones en el Bash actual. |
| `../hello.sh`    | Alternativa a `source` con ruta explícita.   |

Un script cargado con `source` puede cambiar las variables y el directorio del intérprete actual. No lo uses con código que no conozcas.

> [!note] ARCHIVOS EN LINUX
> Utiliza finales de línea LF. Un archivo con CRLF puede provocar un error como `bad interpreter` al ejecutar el shebang.

## EJERCICIO

Crea `hello.sh`, ejecútalo de las dos primeras formas y comprueba qué ocurre cuando cambias el texto que se imprime.
