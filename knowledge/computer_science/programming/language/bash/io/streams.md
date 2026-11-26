---
aliases: ["Flujos y descriptores de archivo"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:56:59
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# FLUJOS Y DESCRIPTORES DE ARCHIVO

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Redirections.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Redirecciones en bash](redirections.md)
> - [Tuberías en bash](pipes.md)
> - [Entrada y salida en bash](../basics/input_output.md)

## DEFINICIÓN

Los procesos de Linux se comunican mediante flujos de bytes. Un descriptor de archivo es un número que identifica un recurso abierto dentro del proceso (archivo, terminal, tubería, etc.). Por convención, los programas reciben tres descriptores iniciales:

| FD  | NOMBRE | FUNCIÓN                 |
|:---:|:------ |:----------------------- |
|  0  | stdin  | Entrada estándar.       |
|  1  | stdout | Salida estándar.        |
|  2  | stderr | Salida de diagnósticos. |

```text
stdin (0) --> program --> stdout (1)
                 |
                 +------> stderr (2)
```

En una sesión interactiva los tres suelen estar conectados al terminal. La shell puede cambiar esa conexión sin que el programa tenga que saber si escribe en un archivo o una tubería.

## EJEMPLO

```bash
printf 'Resultado: %d\n' 42
printf 'Aviso: dato de ejemplo\n' >&2
```

El primer mensaje va a stdout; el segundo a stderr. Esta separación permite encadenar resultados entre programas sin mezclar mensajes informativos.

## DESCRIPTORES ADICIONALES

```bash
exec 3< /etc/hostname
IFS= read -r -u 3 hostname_value
printf '%s\n' "$hostname_value"
exec 3<&-
```

`exec` sin comando modifica los descriptores del shell actual; `3<` abre un archivo para leer y `3<&-` cierra ese descriptor. El ejemplo presupone que `/etc/hostname` existe.

> [!note] DATOS BINARIOS
> Los flujos pueden contener cualquier byte. Las variables Bash, a diferencia de los flujos, no pueden conservar bytes NUL.
