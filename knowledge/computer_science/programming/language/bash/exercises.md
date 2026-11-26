---
aliases: ["Ejercicios de bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:25:25
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# EJERCICIOS DE BASH

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](bash.md)
> - [Chuleta de bash](bash_cheatsheet.md)

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Scripts.html) #WWW/GNU

## FUNDAMENTOS

1. Crea un script que reciba un nombre y muestre `Hola NOMBRE`. Si no recibe exactamente un argumento, escribe un mensaje de uso en stderr y devuelve 2. Prueba con `Ana García`.
2. Predice el resultado de `printf '<%s>\n' $name` y `printf '<%s>\n' "$name"` cuando `name='uno dos'`. Explícalo antes de ejecutarlo.
3. Recibe un entero decimal no negativo de hasta seis dígitos. Valídalo, conviértelo sin problemas con ceros iniciales y muestra si es par o impar. Rechaza `abc`, `1+2` y una entrada vacía.
4. Crea un array con los elementos `uno dos`, `*` y una cadena vacía. Imprime un elemento por línea, entre `<` y `>`, conservando los tres elementos.
5. Escribe una función que devuelva éxito si recibe una cadena no vacía. Usa la función dentro de un `if`; después explica por qué `return 0` no devuelve el número 0 como dato.

## FLUJOS Y ARCHIVOS

6. Escribe en un archivo dos mensajes, uno en stdout y otro en stderr. Experimenta con `> demo.log 2>&1` y `2>&1 > demo.log` sobre el mismo grupo de comandos. Predice la diferencia.
7. Lee un archivo línea a línea. Conserva espacios iniciales, barras invertidas y la última línea aunque no termine con salto de línea.
8. Crea un directorio de pruebas con dos archivos `.txt`, uno con espacios en su nombre. Recorre las rutas usando `find -print0` y `read -d ''`, sin analizar `ls`.
9. Predice los estados de `false | true` con y sin `pipefail`. Después demuestra qué ocurre con una variable incrementada dentro de un `while` alimentado por una tubería.

## SCRIPTS COMPLETOS

10. Escribe una herramienta con `getopts` que acepte `-n NOMBRE`, `-v` y `-h`, y rechace opciones desconocidas y operandos sobrantes.
11. Crea un directorio con `mktemp -d`, escribe un archivo en su interior y configura `trap` para eliminarlo al finalizar. Comprueba también una salida con estado 1.
12. Implementa un informe de frecuencias de palabras de un archivo sencillo (una palabra por línea) con `sort` y `uniq -c`. Comprueba entradas vacías y archivos inexistentes. No presentes un resultado parcial como exitoso si un comando falla.

> [!tip] CÓMO PRACTICAR
> Haz primero los ejercicios sin mirar las soluciones. Para los que escriben archivos usa un directorio de pruebas. Comprueba argumentos inválidos, estados de salida y casos límite, no solo el resultado esperado.

Puedes consultar las [soluciones razonadas](solutions.md).
