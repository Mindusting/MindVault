---
aliases: ["Lectura y escritura de archivos en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:55:00
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# LECTURA Y ESCRITURA DE ARCHIVOS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Entrada y salida en bash](../basics/input_output.md)
> - [Redirecciones en bash](redirections.md)
> - [Tuberías en bash](pipes.md)
> - [Gestión de archivos y directorios en bash](../tools/file_management.md)

## DEFINICIÓN

Bash puede leer archivos línea a línea y escribir resultados con redirecciones. No es necesario ejecutar `cat` para alimentar un bucle si se puede redirigir el archivo directamente.

## LEER LÍNEA A LÍNEA

```bash
printf '  primera línea  \nsegunda sin salto' > demo.txt
while IFS= read -r line || [[ -n $line ]]; do
    printf '<%s>\n' "$line"
done < demo.txt
```

`IFS=` preserva los espacios, `-r` evita que las barras invertidas se interpreten y `|| [[ -n $line ]]` permite procesar la última línea aunque no termine con un salto. Esta condición está pensada para archivos de texto.

## LEER EN UN ARRAY

```bash
mapfile -t lines < demo.txt
for line in "${lines[@]}"; do
    printf '%s\n' "$line"
done
```

`mapfile` (Bash 4+) lee líneas en un array; `-t` elimina el delimitador final de cada línea. Para archivos grandes es preferible el bucle, que no necesita almacenar todo el contenido a la vez.

## LEER NOMBRES DE ARCHIVOS

En Linux, los nombres pueden contener saltos de línea, pero no NUL. Utiliza ese byte como separador cuando pases rutas a través de un flujo:

```bash
while IFS= read -r -d '' file; do
    printf 'Ruta: %q\n' "$file"
done < <(find . -type f -name '*.txt' -print0)
```

`find -print0` separa rutas por NUL; `read -d ''` lee hasta NUL. La sustitución de procesos no propaga por sí sola un fallo de `find`; para una tarea donde sea importante distinguir búsqueda completa de parcial, guarda primero la lista en un archivo temporal y verifica el estado de `find`.

## ESCRIBIR

```bash
printf '%s\n' 'entrada 1' > demo_output.txt
printf '%s\n' 'entrada 2' >> demo_output.txt
```

Usa rutas de prueba. Las redirecciones no crean directorios padres y pueden fallar por permisos o almacenamiento insuficiente.
