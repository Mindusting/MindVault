---
aliases: ["Operadores aritméticos en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:43:09
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# OPERADORES ARITMÉTICOS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Tipos de datos en bash](data_types.md)
> - [Condicionales en bash](conditionals.md)
> - [Estado de salida en bash](exit_status.md)
> - [Gestión de errores en bash](../advanced/error_handling.md)

## DEFINICIÓN

Bash admite expresiones aritméticas con una sintaxis parecida a C. `$((expression))` produce un valor; `((expression))` ejecuta una evaluación y devuelve un estado de salida.

| OPERADOR                         | DESCRIPCIÓN                                    |
|:-------------------------------- |:---------------------------------------------- |
| `+`, `-`, `*`, `/`, `%`          | Suma, resta, multiplicación, división y resto. |
| `**`                             | Potencia.                                      |
| `++`, `--`                       | Incremento y decremento.                       |
| `+=`, `-=`, `*=`, `/=`           | Asignación compuesta.                          |
| `==`, `!=`, `<`, `<=`, `>`, `>=` | Comparaciones.                                 |
| `!`, `&&`, \|\|                  | Operadores lógicos.                            |
| `~`, `&`, `^`, `<<`, `>>`        | Complemento, AND, XOR y desplazamientos.       |
| \|                               | OR bit a bit.                                  |
| `condition? a: b`              | Operador ternario.                             |

```bash
x=7
y=2
printf '%s\n' "$((x + y))"  # 9
printf '%s\n' "$((x / y))"  # 3
printf '%s\n' "$((x % y))"  # 1
((x += 2))
printf '%s\n' "$x"         # 9
```

## VALOR Y ESTADO DE SALIDA

```bash
if (( 4 > 2 )); then
    printf 'Verdadero\n'
fi
printf '%s\n' "$((4 > 2))" # 1
```

`((expression))` devuelve estado 0 si el resultado es distinto de cero, y 1 si es cero. `((counter++))` con `counter=0` incrementa correctamente, pero devuelve 1 porque el valor de la expresión era cero antes del incremento; tenlo en cuenta con `set -e`.

## ENTRADA NUMÉRICA

Bash puede evaluar el contenido de variables como expresiones, no solo como números literales. No pases valores arbitrarios del usuario a contextos aritméticos. Un ejemplo para aceptar hasta seis dígitos decimales no negativos:

```bash
raw='008'
if [[ $raw =~ ^[0-9]{1,6}$ ]]; then
    value=$((10#$raw))
    printf '%s\n' "$value" # 8
fi
```

El prefijo `10#` evita interpretar el cero inicial como octal. Para entradas negativas valida y trata el signo por separado. El límite de longitud reduce el riesgo de desbordamiento.

> [!note] LIMITACIONES
> La división entera trunca hacia cero, no redondea al entero más próximo. Dividir entre cero produce un error. Bash no comprueba el desbordamiento de enteros.
