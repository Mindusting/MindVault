---
aliases: [Complemento a dos, Two’s complement]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# ENTEROS CON SIGNO: COMPLEMENTO A DOS

> [!seealso]- MIRA TAMBIÉN
> - [Enteros sin signo](unsigned_integers.md)
> - [Cómo cambiar el signo](twos_complement_negation.md)
> - [Sumador/restador](../arithmetic/adder_subtractor.md)

> [!important] CONCEPTOS IMPORTANTES
> - El **complemento a dos** es la representación habitual de enteros con signo en hardware moderno.
> - Con $n$ bits representa desde $-2^{n-1}$ hasta $2^{n-1}-1$.
> - El bit más significativo tiene peso **negativo**, pero no basta con interpretarlo como un signo separado.
## DEFINICIÓN

El **complemento a dos** permite representar enteros positivos y negativos utilizando $n$ bits y compartir circuitos de suma para ambos. La mitad de los patrones representan valores negativos.

> [!abstract] RANGO EN $n$ BITS
> $$-2^{n-1}\le x\le2^{n-1}-1$$

| Bits | Mínimo | Máximo |
| ---: | ---: | ---: |
| 4 | -8 | 7 |
| 8 | -128 | 127 |
| 16 | -32 768 | 32 767 |
| 32 | -2 147 483 648 | 2 147 483 647 |

## CÓMO INTERPRETAR LOS BITS

El MSB aporta $-2^{n-1}$ en lugar de $+2^{n-1}$, y el resto conserva sus pesos positivos:

> [!abstract] FÓRMULA
> $$x=-b_{n-1}2^{n-1}+\sum_{i=0}^{n-2}b_i2^i$$

> [!example] EJEMPLO — INTERPRETAR `1111 1011` COMO ENTERO CON SIGNO DE 8 BITS
> $$-128+64+32+16+8+0+2+1=-5$$
>
> El mismo patrón, **sin signo**, representaría 251.

## CÓMO CODIFICAR UN NEGATIVO

Partimos de la magnitud positiva, invertimos todos los bits **dentro del ancho elegido** y sumamos 1:

> [!example] EJEMPLO — CODIFICAR $-5$ EN 8 BITS
> ```text
>  +5:            0000 0101
>  Invertir:      1111 1010
>  Sumar 1:       1111 1011
>  Resultado -5:  1111 1011
> ```

Esto funciona cuando el número positivo que usamos como punto de partida es representable en el ancho elegido. Para el mínimo negativo, es preferible usar directamente su patrón (`1000 0000` para -128 en 8 bits) o calcular $x\bmod2^n$.

## POR QUÉ EL SUMADOR FUNCIONA PARA LOS NEGATIVOS

En $n$ bits, el patrón que codifica $-B$ coincide con $2^n-B$ (módulo $2^n$). Por eso:

$$A+(-B)\equiv A+(2^n-B)\pmod{2^n}$$

> [!example] EJEMPLO — $5+(-3)$ EN 8 BITS
> ```text
>    0000 0101  (+5)
>  + 1111 1101  (-3)
>  ------------
>  1 0000 0010
>    0000 0010  (+2, descartando el acarreo exterior)
> ```

## EXTENSIÓN DE SIGNO

Al ampliar un entero con signo hay que **repetir el MSB**, no añadir ceros indiscriminadamente:

```text
-5, 8 bits:   1111 1011
-5, 16 bits:  1111 1111 1111 1011

+5, 8 bits:   0000 0101
+5, 16 bits:  0000 0000 0000 0101
```

## PROPIEDADES Y CASOS LÍMITE

- Existe un **único cero** (`0000 ... 0000`); no hay dos ceros como en signo y magnitud.
- El mínimo negativo no tiene un positivo equivalente en el **mismo ancho**: $-128$ cabe en 8 bits; $+128$ no.
- **El acarreo de salida NO indica por sí solo desbordamiento con signo**. Para detectarlo se comparan los signos de los operandos y del resultado, o los acarreos alrededor del bit de signo.
- El ancho es esencial: `1000` significa -8 en cuatro bits, pero `0000 1000` significa +8 en ocho bits.

## OTRAS REPRESENTACIONES

En **signo y magnitud**, el primer bit identifica el signo y los demás guardan el valor absoluto; en **complemento a uno**, el negativo se obtiene invirtiendo bits. Ambas pueden tener dos representaciones de cero. Se estudian como antecedentes, pero el complemento a dos simplifica el hardware aritmético y predomina en los procesadores actuales.
