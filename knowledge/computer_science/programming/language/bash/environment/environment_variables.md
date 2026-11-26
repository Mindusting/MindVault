---
aliases: ["Variables de entorno en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:51:42
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# VARIABLES DE ENTORNO EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Environment.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Variables en bash](../basics/variables.md)
> - [Archivos de inicio de bash](startup_files.md)
> - [Procesos, subshells y trabajos en bash](../advanced/processes.md)

## DEFINICIÓN

El entorno de un proceso es un conjunto de pares nombre-valor que recibe al iniciarse. Bash importa las variables válidas del entorno y permite exportar variables a los procesos hijos. Una variable ordinaria de Bash no se exporta necesariamente.

```bash
my_variable='Hola'
export my_variable
bash -c 'printf "%s\n" "$my_variable"'
```

El shell hijo recibe una copia del entorno. Si modifica una variable, no cambia automáticamente la del padre.

## VARIABLES HABITUALES

| VARIABLE         | SIGNIFICADO                                                             |
|:---------------- |:----------------------------------------------------------------------- |
| `HOME`           | Directorio personal.                                                    |
| `PATH`           | Directorios de búsqueda de ejecutables.                                 |
| `PWD`            | Directorio de trabajo actual (ruta lógica normalmente).                 |
| `USER`           | Nombre de usuario habitual del entorno; no es prueba de identidad.      |
| `SHELL`          | Shell de inicio configurada habitualmente; no necesariamente la actual. |
| `LANG`, `LC_ALL` | Configuración regional.                                                 |
| `BASH_VERSION`   | Versión del Bash en ejecución (variable de Bash).                       |

```bash
printenv PATH
printf '%s\n' "$BASH_VERSION"
LC_ALL=C sort <<'EOF'
b
a
EOF
```

`NAME=value command` configura temporalmente el entorno de un comando externo. `env` y `printenv` muestran variables de entorno, pero no necesariamente todas las variables del shell.

## MODIFICAR PATH

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Añade el directorio al principio, dándole prioridad. Solo incorpora directorios de confianza y evita componentes vacíos o `.` en `PATH` si no quieres buscar en el directorio actual.

> [!important] SECRETOS
> No exportes secretos innecesariamente: pueden heredarlos otros procesos y aparecer en herramientas de diagnóstico. No incluyas contraseñas reales en `.bashrc` ni en repositorios.
