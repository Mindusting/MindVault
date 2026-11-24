---
aliases: [Negación binaria, Negar complemento a dos]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# CAMBIO DE SIGNO EN COMPLEMENTO A DOS

> [!seealso]- MIRA TAMBIÉN
> - [Complemento a dos](twos_complement.md)
> - [Sumador/restador](../arithmetic/adder_subtractor.md)

> [!important] CONCEPTOS IMPORTANTES
> - Para negar un entero, se invierten todos sus bits y se suma 1: $-x=\overline{x}+1$ (módulo $2^n$).
> - No es suficiente invertir el bit más significativo.
> - La negación del mínimo negativo **desborda** si el ancho no aumenta.
## DEFINICIÓN

**Negar** un entero con signo significa obtener su opuesto: de $x$ pasamos a $-x$. En complemento a dos, podemos hacerlo con las mismas puertas que utiliza un sumador.

> [!abstract] FÓRMULA EN $n$ BITS
> $$\operatorname{NEG}(x)=(\overline{x}+1)\bmod2^n$$

## PROCEDIMIENTO PASO A PASO

> [!example] EJEMPLO — DE `+18` A `-18` (8 BITS)
> ```text
> +18:            0001 0010
> NOT:            1110 1101
> +1:             0000 0001
> -------------------------
> -18:            1110 1110
> ```
>
> Verificación: $-128+64+32+8+4+2=-18$.

Si negamos otra vez `1110 1110`, recuperamos `0001 0010`.

## POR QUÉ FUNCIONA

Dentro de un ancho de $n$ bits, invertir un patrón equivale aritméticamente a restarlo de $2^n-1$. Al sumar 1:

$$\overline{x}+1\equiv(2^n-1-x)+1\equiv -x\pmod{2^n}$$

## IMPLEMENTACIÓN CON PUERTAS

Un negador combinacional puede construirse con:

1. Una puerta NOT para cada bit de entrada.
2. Un sumador que añada el valor constante `...0001`.

Si ya tenemos un circuito de [suma/resta](../arithmetic/adder_subtractor.md), podemos obtener $0-x$ **sin fabricar otro sumador**: fijamos el primer operando a cero y activamos la resta.

> [!tip] OPTIMIZACIÓN
> Hay una forma equivalente de negar sin un sumador genérico: desde el LSB hacia la izquierda, **conservamos los ceros iniciales y el primer `1`**; después invertimos todos los bits restantes. Por ejemplo, `0010 1000` → `1101 1000`. Esta regla sale de aplicar NOT + 1.

## CASO LÍMITE: MÍNIMO NEGATIVO

> [!warning] DESBORDAMIENTO
> ```text
> 8 bits con signo:
> -128 = 1000 0000
> NOT  = 0111 1111
> +1   = 1000 0000   (sigue representando -128)
> ```
>
> El resultado matemático sería +128, que no cabe en 8 bits con signo. La operación **desborda**; la secuencia modular de bits termina siendo la misma.

## EJERCICIOS

1. Obtén `-37` en complemento a dos de 8 bits.
2. Niega `1111 0011` interpretado como entero de 8 bits con signo.
3. ¿Por qué `1000 0000` no puede negarse correctamente sin ampliar el ancho?
