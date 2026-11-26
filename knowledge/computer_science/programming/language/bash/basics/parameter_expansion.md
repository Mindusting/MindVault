---
aliases: ["Expansión de parámetros en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:49:02
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# EXPANSIÓN DE PARÁMETROS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Variables en bash](variables.md)
> - [Cadenas de texto en bash](strings.md)
> - [Patrones y expresiones regulares en bash](patterns.md)

## DEFINICIÓN

La forma `${parameter}` permite acceder a valores y aplicar operaciones de sustitución, extracción o comprobación sin ejecutar programas externos.

## VALORES POR DEFECTO

| SINTAXIS           | SIGNIFICADO                                                |
|:------------------ |:---------------------------------------------------------- |
| `${name:-default}` | Usa el valor alternativo si no está definida o está vacía. |
| `${name:=default}` | Asigna el alternativo en ese caso.                         |
| `${name:?message}` | Produce un error en ese caso.                              |
| `${name:+value}`   | Usa `value` si está definida y no está vacía.              |

Si se elimina `:` de estas cuatro formas, solo se comprueba si el parámetro no está definido, no si está vacío. `:=` no se puede usar para asignar parámetros posicionales o especiales; `:?` hace salir a un shell no interactivo.

```bash
unset name
printf '%s\n' "${name:-Invitado}"
name=''
printf '<%s>\n' "${name-Invitado}" # <>
printf '%s\n' "${name:=Invitado}" # Invitado
```

## SUBCADENAS Y LONGITUD

```bash
text='abcdef'
printf '%s\n' "${#text}"    # 6
printf '%s\n' "${text:1:3}" # bcd
printf '%s\n' "${text: -2}" # ef
```

El índice comienza en 0. El espacio antes del desplazamiento negativo evita confundirlo con `:-`. En una configuración regional multibyte la longitud se expresa en caracteres, no necesariamente bytes.

## PATRONES Y SUSTITUCIONES

```bash
file='archive.tar.gz'
printf '%s\n' "${file%.*}"  # archive.tar
printf '%s\n' "${file%%.*}" # archive
printf '%s\n' "${file#*.}"  # tar.gz
printf '%s\n' "${file##*.}" # gz
text='a-b-c'
printf '%s\n' "${text/-/_}"  # a_b-c
printf '%s\n' "${text//-/_}" # a_b_c
```

`#` y `##` eliminan el prefijo coincidente más corto o más largo; `%` y `%%` hacen lo propio con el sufijo. Los patrones son de shell, no expresiones regulares. Las transformaciones no modifican la variable original si no se reasigna el resultado.
