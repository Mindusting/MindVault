---
aliases: ["Archivos de inicio de bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:52:24
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# ARCHIVOS DE INICIO DE BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Variables de entorno en bash](environment_variables.md)
> - [Primer programa en bash](../basics/first_program.md)
> - [Compatibilidad entre bash y sh](../advanced/portability.md)

## DEFINICIÓN

Bash puede leer archivos de configuración al iniciarse. Los archivos que lee dependen de si es un shell interactivo, de login, o no interactivo.

| TIPO                     | ARCHIVOS HABITUALES                                                                      |
|:------------------------ |:---------------------------------------------------------------------------------------- |
| Login interactivo        | `/etc/profile` y el primero legible de `~/.bash_profile`, `~/.bash_login`, `~/.profile`. |
| Interactivo no login     | `~/.bashrc` (la distribución puede añadir configuración global).                         |
| No interactivo ordinario | Archivo señalado por `BASH_ENV`, si está definido y es aplicable.                        |

Existen excepciones (invocación como `sh`, modo POSIX, ciertas conexiones remotas, etc.). Un script normal no debería depender de que se haya leído `.bashrc`.

## BASHRC

Para hacer persistente una variable destinada a sesiones interactivas, puedes añadir a `~/.bashrc`:

```bash
export MY_EDITOR='nvim'
alias ll='ls -alF'
```

Puedes cargar los cambios en el shell actual mediante `source ~/.bashrc`. Hazlo únicamente con tu configuración de confianza; abrir otro terminal normalmente crea otra sesión y vuelve a leer la configuración correspondiente.

Los aliases son sustituciones de palabras, no funciones con argumentos. En scripts no interactivos normalmente están desactivados. Para lógica reutilizable, utiliza funciones o scripts independientes.

## COMPROBAR EL TIPO DE SHELL

```bash
if [[ $- == *i* ]]; then
    printf 'Shell interactivo\n'
fi
if shopt -q login_shell; then
    printf 'Shell de login\n'
fi
```

## NOTAS

En Debian, Ubuntu y Linux Mint es habitual que la shell interactiva y `/bin/sh` no sean el mismo intérprete. No modifiques los archivos de inicio solo para ejecutar un script: declara sus propias dependencias y configuración.
