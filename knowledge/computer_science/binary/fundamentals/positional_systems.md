---
aliases: [Sistema binario, Base dos]
author: Mindusting
corrected: false
creationDate: 2026-11-24 04:29:24
headerFile: false
modificationDate: 2026-11-24 06:12:45
rating: 
tags: [Binary, DigitalLogic]
---

# SISTEMAS DE NUMERACIÓN POSICIONALES

> [!seealso]- MIRA TAMBIÉN
> - [Conversión entre bases](conversions.md)
> - [Complemento a dos](../representation/twos_complement.md)

> [!important] CONCEPTOS IMPORTANTES
> - El valor de una cifra depende de su posición y de la **base**.
> - En binario, las posiciones valen $1, 2, 4, 8, 16, \ldots$.
> - Cuatro bits binarios corresponden exactamente a una cifra hexadecimal.

## DEFINICIÓN

Un **sistema de numeración posicional** representa números mediante una secuencia de cifras. Cada cifra multiplica una potencia de la base $b$; la posición más a la derecha de la parte entera tiene índice cero.

> [!abstract] VALOR DE UN NÚMERO EN BASE $b$
> 
> $$N = \sum_{i = 0}^{n - 1}d_i b^i$$
> 
> - $b$: base (2 para binario, 10 para decimal, 16 para hexadecimal).
> - $d_i$: cifra situada en la posición $i$, con $0 \le d_i < b$.

## BINARIO

Las cifras posibles son `0` y `1`:

| Posición $i$ |   7 |   6 |   5 |   4 |   3 |   2 |   1 |   0 |
| ------------ | ---:| ---:| ---:| ---:| ---:| ---:| ---:| ---:|
| Peso $2^i$   | 128 |  64 |  32 |  16 |   8 |   4 |   2 |   1 |

Por ejemplo:

$$
101101_2 =
1 \cdot 32 + 0 \cdot 16 + 1 \cdot 8 + 1 \cdot 4 + 0 \cdot 2 + 1 =
45_{10}
$$

Añadir ceros **a la izquierda** de un entero sin signo no cambia su valor: `00101` y `101` equivalen a 5.

## FRACCIONES BINARIAS

A la derecha de la coma binaria los pesos son $2^{-1},2^{-2},\ldots$:

$$10.101_2 = 2 + \frac 12 + \frac 18 = 2.625_{10}$$

| Posición | $2^2$ | $2^1$ | $2^0$ | $2^{-1}$ | $2^{-2}$ | $2^{-3}$ |
| -------- | -----:| -----:| -----:| --------:| --------:| --------:|
| Peso     |     4 |     2 |     1 |      0,5 |     0,25 |    0,125 |

## HEXADECIMAL Y OCTAL

El hexadecimal usa dieciséis cifras (`0`–`9` y `A`–`F`). Es especialmente útil porque **un dígito hexadecimal equivale a cuatro bits**:

```text
Binario:     1101 0110 1010
Hexadecimal:    D    6    A
Resultado: 0xD6A
```

El octal utiliza ocho cifras: cada dígito octal representa tres bits. Son formas de escribir **el mismo patrón de bits**, no formatos de almacenamiento diferentes.

## CUÁNDO IMPORTA EL ANCHO

`1111` como entero sin signo vale 15, pero, interpretado en **complemento a dos de 4 bits**, vale -1. Por tanto, para interpretar un patrón no basta con saber su base: también hace falta conocer el **formato y el ancho**.
