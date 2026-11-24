---
aliases: [Shift, Barrel shifter, Rotación binaria]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# DESPLAZADORES Y ROTADORES

> [!seealso]- MIRA TAMBIÉN
> - [Operaciones bit a bit](../fundamentals/bitwise_operations.md)
> - [Multiplicador](../arithmetic/multiplier.md)
> - [Divisor](../arithmetic/divider.md)

> [!important] CONCEPTOS IMPORTANTES
> - Desplazar mueve bits a posiciones adyacentes; los que salen del ancho se pierden.
> - El desplazamiento **lógico** a la derecha introduce ceros; el **aritmético** replica el bit de signo.
> - Una **rotación** reutiliza los bits que salen por un extremo y los introduce por el otro.
## DESPLAZAMIENTO LÓGICO

Un desplazamiento lógico mueve un patrón a izquierda o derecha y rellena las posiciones libres con ceros. Veamos una palabra de 8 bits:

```text
Origen:           1011 0010
Lógico << 1:      0110 0100
Lógico >> 1:      0101 1001
```

Los bits descartados ya **no están** en el resultado. Para enteros sin signo sin pérdida de bits, desplazar a la izquierda equivale a multiplicar por una potencia de 2 y desplazar a la derecha a efectuar una división entera por una potencia de 2.

## DESPLAZAMIENTO ARITMÉTICO A LA DERECHA

Cuando una palabra se interpreta en complemento a dos, un desplazamiento aritmético a la derecha **rellena con copias del bit de signo**:

```text
Entrada:                 1111 1000 (-8)
Aritmético >> 1:         1111 1100 (-4)
Lógico >> 1:             0111 1100 (124 si se interpreta sin signo)
```

Para negativos impares, la operación aritmética a la derecha suele corresponder a redondear la división por $2^k$ **hacia $-\infty$**, no necesariamente hacia cero: por ejemplo, `-3 >> 1` con desplazamiento aritmético da -2.

> [!warning] PRECAUCIÓN
> No hay un “desplazamiento aritmético a la izquierda” que resuelva automáticamente el desbordamiento: desplazar un valor con signo hacia la izquierda puede alterar el signo o perder información.

## ROTACIÓN

En una **rotación**, los bits desplazados por un extremo vuelven a entrar por el otro:

```text
Origen:           1001 0110
Rotar izquierda:  0010 1101
Rotar derecha:    0100 1011
```

Una rotación conserva el número de bits a 1; un desplazamiento lógico no tiene por qué hacerlo.

## DESPLAZADOR DE BARRIL (BARREL SHIFTER)

Un **barrel shifter** permite desplazar una palabra varios bits en una sola operación combinacional. Puede fabricarse organizando niveles de multiplexadores, por ejemplo para desplazamientos opcionales de 1, 2, 4, 8... posiciones.

Para una palabra de 8 bits, tres controles pueden elegir desplazamientos de 0 a 7, combinando etapas de desplazamiento de 1, 2 y 4 posiciones.

## APLICACIONES

- Multiplicación/división por potencias de dos (cuando su semántica lo permite).
- Normalización de significandos en coma flotante.
- Multiplicación y división binaria por desplazamiento y suma/resta.
- Rotaciones en funciones de mezcla y determinados algoritmos criptográficos.
