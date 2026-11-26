---
aliases: ["Gestión de archivos y directorios en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:57:54
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# GESTIÓN DE ARCHIVOS Y DIRECTORIOS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html) #WWW/GNU
> - [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/html_node/)
> - [GNU Findutils](https://www.gnu.org/software/findutils/manual/html_node/find_html/)

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Patrones y expresiones regulares en bash](../basics/patterns.md)
> - [Lectura y escritura de archivos en bash](../io/reading_files.md)
> - [Señales y trap en bash](../advanced/traps.md)

## DEFINICIÓN

Bash se encarga de interpretar las órdenes, mientras que programas externos como `cp`, `mv`, `mkdir` y `find` realizan operaciones sobre el sistema de archivos. Los ejemplos están orientados a las herramientas GNU de Linux.

| COMANDO            | FUNCIÓN                                        |
|:------------------ |:---------------------------------------------- |
| `pwd`              | Muestra el directorio actual.                  |
| `mkdir -p DIR`     | Crea directorios, incluidos padres necesarios. |
| `cp SOURCE DEST`   | Copia archivos.                                |
| `mv SOURCE DEST`   | Mueve o renombra.                              |
| `rm FILE`          | Elimina un archivo.                            |
| `find DIR -type f` | Busca archivos regulares.                      |
| `stat FILE`        | Consulta metadatos.                            |
| `mktemp -d`        | Crea un directorio temporal.                   |

## RUTAS Y OPCIONES

```bash
file='mi archivo.txt'
printf '%s\n' "$file"
printf 'Nombre: %s\n' "${file##*/}"
```

Utiliza comillas al pasar rutas. Muchos programas GNU aceptan `--` para marcar el fin de las opciones, de modo que un nombre como `-n` no se interprete como opción. También puedes usar rutas como `./-n`.

## EJEMPLO EN UN DIRECTORIO TEMPORAL

```bash
(
    demo_dir=$(mktemp -d) || exit 1
    trap 'rm -rf -- "$demo_dir"' EXIT
    mkdir -- "$demo_dir/source" "$demo_dir/destination" || exit 1
    printf 'Hola\n' > "$demo_dir/source/mi archivo.txt" || exit 1
    cp -- "$demo_dir/source/mi archivo.txt" "$demo_dir/destination/" || exit 1
    find "$demo_dir" -type f -name '*.txt'
)
```

El patrón de `find` va entre comillas para que no lo expanda Bash antes de ejecutarlo. El subshell y `trap` limitan la limpieza al directorio temporal recién creado.

## BUSCAR Y EJECUTAR

```bash
find . -type f -name '*.md' -exec wc -l -- {} +
```

`{}` representa las rutas encontradas; `+` permite agruparlas en una o varias ejecuciones del programa. Esta construcción evita dividir nombres que contienen espacios o saltos de línea.

> [!warning] OPERACIONES DESTRUCTIVAS
> Antes de usar `rm`, `mv` o redirecciones sobre datos importantes, comprueba las rutas, considera una simulación y evita privilegios innecesarios. No analices `ls` para obtener nombres. Las comprobaciones previas no eliminan condiciones de carrera.
