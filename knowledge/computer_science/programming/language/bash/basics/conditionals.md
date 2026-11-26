---
aliases: ["Condicionales en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:45:32
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# CONDICIONALES EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Operadores aritméticos en bash](arithmetic.md)
> - [Patrones y expresiones regulares en bash](patterns.md)
> - [Estado de salida en bash](exit_status.md)

## DEFINICIÓN

Un condicional permite decidir qué instrucciones ejecutar. `if` evalúa el estado de salida de una lista de comandos; no necesita una expresión booleana de un tipo específico.

> [!abstract] SINTAXIS
> 
> ```bash
> if condition; then
>     commands
> elif another_condition; then
>     commands
> else
>     commands
> fi
> ```

```bash
age=20
if (( age >= 18 )); then
    printf 'Mayor de edad\n'
else
    printf 'Menor de edad\n'
fi
```

## TEST, `[]` Y `[[ ]]`

`test` y `[` son comandos; `[` necesita un argumento final `]` separado por espacios. `[[ ]]` es una construcción de Bash, evita división en palabras y globbing sobre sus operandos y admite patrones y regex.

```bash
name='Ana García'
if [ "$name" = 'Ana García' ]; then
    printf 'Coincide\n'
fi
if [[ $name == Ana* && -n $name ]]; then
    printf 'Empieza por Ana\n'
fi
```

| OPERADOR                   | SIGNIFICADO                                               |
|:-------------------------- |:--------------------------------------------------------- |
| `-eq`, `-ne`               | Igual, distinto (enteros).                                |
| `-lt`, `-le`, `-gt`, `-ge` | Menor, menor o igual, mayor, mayor o igual.               |
| `=`, `!=`                  | Igualdad, desigualdad de cadenas.                         |
| `-z`, `-n`                 | Cadena vacía, no vacía.                                   |
| `-e`, `-f`, `-d`           | Ruta existente, archivo regular, directorio.              |
| `-L`                       | Enlace simbólico.                                         |
| `-r`, `-w`, `-x`           | Permiso de lectura, escritura, ejecución según la prueba. |
| `-s`                       | Archivo con tamaño mayor que cero.                        |

En `[[ ]]`, `<` y `>` comparan cadenas según la configuración regional; para números usa operadores numéricos o `(())`. En `[]` utiliza `=` para portabilidad y combina pruebas como `[...] && [...]`.

## OPERADORES LÓGICOS

```bash
file='report.txt'
if [[ -f $file && -r $file ]]; then
    printf 'Archivo legible\n'
fi
if ! command -v git >/dev/null 2>&1; then
    printf 'Git no está disponible\n'
fi
```

Los tests de archivos no garantizan que una operación posterior tenga éxito: el estado del sistema puede cambiar. Comprueba también el resultado de la operación real.

## CASE

```bash
option='start'
case $option in
    start|run) printf 'Iniciar\n' ;;
    stop) printf 'Detener\n' ;;
    *) printf 'Opción desconocida\n' >&2 ;;
esac
```

`case` compara con patrones de shell, no regex. `;;` finaliza la rama. Es práctico para opciones y menús.
