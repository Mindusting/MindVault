---
aliases: ["Redirecciones en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:55:11
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# REDIRECCIONES EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Redirections.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Flujos y descriptores de archivo](streams.md)
> - [Tuberías en bash](pipes.md)
> - [Lectura y escritura de archivos en bash](reading_files.md)

## DEFINICIÓN

Las redirecciones modifican la entrada o salida de una orden antes de ejecutarla. Si una redirección falla (por ejemplo, por falta de permisos), la orden normalmente no se ejecuta.

| SINTAXIS      | SIGNIFICADO                                 |
|:------------- |:------------------------------------------- |
| `> file`      | stdout a un archivo, truncándolo si existe. |
| `>> file`     | stdout al final de un archivo.              |
| `< file`      | stdin desde un archivo.                     |
| `2> file`     | stderr a un archivo.                        |
| `2>> file`    | Añade stderr al archivo.                    |
| `2>&1`        | Duplica en FD 2 el destino actual del FD 1. |
| `&> file`     | stdout y stderr al mismo archivo (Bash).    |
| `> /dev/null` | Descarta stdout.                            |

## EJEMPLO

En un directorio de pruebas, utiliza nombres de archivo que no contengan datos importantes:

```bash
printf 'Primera línea\n' > demo.txt
printf 'Segunda línea\n' >> demo.txt
cat < demo.txt
```

`>` puede destruir el contenido anterior aunque el programa falle posteriormente. `set -o noclobber` protege frente a determinadas sobrescrituras accidentales con `>`; `>|` permite forzarlas. No sustituye a una política de copias de seguridad.

## ORDEN DE REDIRECCIONES

```bash
{ printf 'Datos\n'; printf 'Error\n' >&2; } > demo.log 2>&1
{ printf 'Datos\n'; printf 'Error\n' >&2; } 2>&1 > demo.log
```

Las redirecciones se aplican de izquierda a derecha. En la primera línea ambas salidas van al archivo; en la segunda stderr mantiene el destino que tenía stdout antes de redirigirlo al archivo.

## AQUÍ DOCUMENTO Y AQUÍ CADENA

```bash
name='Ana'
cat <<EOF
Hola $name
EOF
cat <<'EOF'
Hola $name
EOF
IFS= read -r value <<< 'una línea'
printf '%s\n' "$value"
```

Un *here document* proporciona varias líneas como stdin. Si el delimitador inicial está entrecomillado, no se expanden variables ni sustituciones de comandos en su contenido. El delimitador final debe aparecer solo, sin espacios adicionales (salvo el caso especial `<<-`, que admite tabuladores). Un *here string* (`<<<`) proporciona una cadena seguida de un salto de línea.

> [!warning] NO REDIRIJAS SOBRE EL ARCHIVO DE ENTRADA
> `sort data.txt > data.txt` trunca el archivo antes de que `sort` pueda leerlo. Escribe en otro archivo o usa una opción específicamente diseñada para ello, tras revisar sus garantías.
