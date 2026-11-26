---
aliases: ["Comentarios en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-25 11:53:46
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# COMENTARIOS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Comments.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Primer programa en bash](first_program.md)
> - [Comillas y caracteres de escape en bash](quoting.md)

## DEFINICIÓN

Un comentario permite explicar el código sin cambiar su ejecución. En un script, `#` inicia un comentario cuando comienza una palabra y no está protegido mediante comillas o una barra invertida.

> [!abstract] SINTAXIS
> \# ***\[comment\]***

> [!example] EJEMPLO
> 
> ```bash
> # Nombre que se mostrará al usuario.
> name='Adelio'
> printf 'Hola %s\n' "$name" # Saludo.
> printf '%s\n' 'Esto # no es un comentario'
> printf '%s\n' archivo#1
> ```

Bash no tiene una sintaxis específica de comentarios multilínea. Utiliza `#` en cada línea. Un *here document* enviado a `:` no es un comentario real: puede realizar expansiones si su delimitador no está entrecomillado.

> [!note] NOTA
> Comenta el motivo de una decisión, no solamente lo que ya expresa la instrucción. El shebang `#!` es un caso especial interpretado por el sistema al iniciar el script.
