---
aliases: [Bash, Bash Script, Bash Scripting]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: true
modificationDate: 2026-11-25 11:53:07
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# BASH SCRIPT

> [!external-link]- REFERENCIAS WEB
> - [Manual oficial de GNU Bash](https://www.gnu.org/software/bash/manual/bash.html) #WWW/GNU
> - [ShellCheck](https://www.shellcheck.net/)
> - [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/)
> - [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9799919799/utilities/V3_chap02.html)

> [!seealso]- MIRA TAMBIÉN
> - [Linux](../../../../../temp/os/linux/linux.md)
> - [Comandos de Linux](../../../../../temp/os/linux/linux_cmd.md)

> [!important] CONCEPTOS IMPORTANTES
> - Bash es un **intérprete de comandos** y un lenguaje de scripting.
> - La shell, el terminal y el sistema operativo no son lo mismo.
> - Las expansiones se realizan antes de ejecutar una orden; las comillas controlan cómo se separan los argumentos.
> - El estado de salida `0` significa éxito, no falso.
> - Los scripts pueden combinar comandos mediante flujos de entrada y salida.

## DEFINICIÓN

**Bash** (*Bourne Again SHell*) es un intérprete de comandos que forma parte del proyecto GNU. Se puede utilizar de forma interactiva, escribiendo órdenes en un terminal, o de forma no interactiva, ejecutando instrucciones almacenadas en archivos llamados *scripts*.

Un terminal presenta una interfaz para introducir y visualizar texto. Bash interpreta las instrucciones y solicita al sistema operativo la ejecución de programas o realiza operaciones mediante sus propios comandos integrados. Linux es el núcleo del sistema, no el lenguaje que interpreta las instrucciones.

La programación en Bash (*Bash scripting*) resulta especialmente útil para automatizar tareas de administración, combinar programas, manipular archivos y preparar procesos de compilación o ejecución. Para cálculos complejos, aplicaciones grandes o estructuras de datos elaboradas suele ser más adecuado un lenguaje de propósito general.

## ALCANCE Y CONVENCIONES

Estos apuntes utilizan **Bash 5.x sobre GNU/Linux**, especialmente distribuciones como Linux Mint y Ubuntu. Se distingue el lenguaje Bash de las herramientas externas y de las características portables de `sh`. Puedes consultar tu versión mediante `bash --version`.

Los ejemplos están escritos con nombres de variables en inglés, explicaciones en castellano e indentación de cuatro espacios. Los bloques de código se ejecutan en Bash, salvo que se indique otra cosa. Cuando un ejemplo crea archivos, utiliza un directorio de pruebas y evita rutas con datos importantes. Los fragmentos de sintaxis contienen nombres ilustrativos que se deben sustituir; los ejemplos completos se identifican por su contexto.

## RUTA DE APRENDIZAJE

Sigue los apartados en orden la primera vez. Las notas pueden consultarse también de forma independiente mediante los enlaces internos y la chuleta.

### FUNDAMENTOS

- [Primer programa y archivos `.sh`](basics/first_program.md): Shebang, permisos y ejecución.
- [Comentarios](basics/comments.md): Documentar código.
- [Comandos](basics/commands.md): Builtins, ejecutables, PATH y listas de órdenes.
- [Variables](basics/variables.md): Declaración, atributos y ámbito.
- [Tipos de datos](basics/data_types.md): Texto, enteros, decimales y valores lógicos.
- [Comillas y escapes](basics/quoting.md): Conservar datos y argumentos.
- [Expansiones](basics/expansions.md): Qué interpreta Bash antes de ejecutar una orden.
- [Expansión de parámetros](basics/parameter_expansion.md): Valores por defecto, subcadenas y sustituciones.
- [Cadenas de texto](basics/strings.md): Concatenación, transformaciones y formato.
- [Operadores aritméticos](basics/arithmetic.md): Operaciones enteras, comparaciones y bits.
- [Arrays](basics/arrays.md): Arrays indexados y asociativos.
- [Argumentos](basics/arguments.md): Parámetros posicionales y parámetros especiales.
- [Entrada y salida](basics/input_output.md): Uso de read y printf.
- [Estado de salida](basics/exit_status.md): Cómo se comunica el éxito o fallo.
- [Condicionales](basics/conditionals.md): if, test, `[[ ]]`, case.
- [Bucles](basics/loop.md): for, while, until, break y continue.
- [Funciones](basics/functions.md): Argumentos, variables locales y retorno.
- [Patrones y expresiones regulares](basics/patterns.md): Globbing, regex y BASH_REMATCH.

### FLUJOS Y ARCHIVOS

- [Flujos y descriptores de archivo](io/streams.md): stdin, stdout y stderr.
- [Redirecciones](io/redirections.md): Archivos, descriptores y here documents.
- [Tuberías](io/pipes.md): Composición de procesos, pipefail y sustitución de procesos.
- [Lectura y escritura de archivos](io/reading_files.md): Líneas, arrays y nombres de archivos.

### ENTORNO

- [Variables de entorno](environment/environment_variables.md): export, env y PATH.
- [Archivos de inicio](environment/startup_files.md): Bashrc y tipos de shell.

### CONCEPTOS AVANZADOS

- [Procesos, subshells y trabajos](advanced/processes.md): Agrupación, señales, segundo plano y wait.
- [Gestión de errores](advanced/error_handling.md): Estados, set -e, set -u y pipefail.
- [Señales y trap](advanced/traps.md): Limpieza de recursos temporales.
- [Opciones de línea de comandos](advanced/command_line_options.md): getopts y diseño de interfaces.
- [Estructura de un script](advanced/script_structure.md): Punto de entrada, módulos y convenciones.
- [Depuración y pruebas](advanced/debugging.md): bash -n, bash -x y ShellCheck.
- [Compatibilidad entre Bash y sh](advanced/portability.md): POSIX y versiones.

### HERRAMIENTAS Y AUTOMATIZACIÓN

- [Gestión de archivos y directorios](tools/file_management.md): Rutas, find y herramientas GNU.
- [Procesamiento de texto](tools/text_processing.md): grep, sed, awk y tuberías.
- [Automatización de scripts](tools/automation.md): Cron, systemd y bloqueos.

### EJEMPLOS PRÁCTICOS

- [Informe de archivos](examples/file_report.md): Cuenta notas Markdown sin modificar los datos.
- [Copia de seguridad](examples/backup.md): Archivo tar.gz, comprobación y limpieza.

### REPASO

- [Chuleta de Bash](bash_cheatsheet.md): Sintaxis y reglas importantes.
- [Ejercicios](exercises.md): Doce propuestas para practicar.
- [Soluciones](solutions.md): Resolución y explicación.
