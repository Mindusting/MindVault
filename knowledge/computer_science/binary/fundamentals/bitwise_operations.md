---
aliases: []
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# OPERACIONES BIT A BIT

> [!seealso]- MIRA TAMBIÉN
> - [Puertas lógicas](../logic/logic_gates.md)
> - [Desplazadores y rotadores](../components/shifters.md)
> - [Cambio de signo](../representation/twos_complement_negation.md)

> [!important] CONCEPTOS IMPORTANTES
> - Las operaciones bit a bit trabajan sobre cada posición de una palabra binaria.
> - XOR detecta diferencias y permite invertir bits seleccionados.
> - Para interpretar correctamente NOT y los desplazamientos hay que fijar el **ancho** y el tipo de dato.
## DEFINICIÓN

Una **operación bit a bit** toma uno o varios patrones y aplica una operación lógica a cada posición. Las operaciones usuales son AND (`&`), OR (`|`), XOR (`^`), NOT (`~`) y desplazamientos (`<<`, `>>`).

| A | B | AND | OR | XOR |
| :-: | :-: | :-: | :-: | :-: |
| 0 | 0 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 |
| 1 | 1 | 1 | 1 | 0 |

## OPERACIONES BÁSICAS

```text
A:       1010 1100
B:       1100 1010
------------------
A AND B: 1000 1000
A OR B:  1110 1110
A XOR B: 0110 0110
```

Para NOT, con **8 bits**:

```text
A:       0000 0101
NOT A:   1111 1010
```

> [!warning] ANCHO DE PALABRA
> En matemáticas podemos escribir $\overline{A}$ sin especificar un ancho. En una implementación real, NOT invierte todos los bits **del tipo o tamaño elegido**. No es correcto suponer que `~5` tiene siempre un resultado de 8 bits.

## MÁSCARAS DE BITS

Una **máscara** selecciona posiciones de interés.

> [!abstract] OPERACIONES COMUNES
> - Comprobar si el bit $i$ está activo: `value & (1 << i)`.
> - Activar el bit $i$: `value | (1 << i)`.
> - Desactivar el bit $i$: `value & ~(1 << i)` (sobre un ancho controlado).
> - Invertir el bit $i$: `value ^ (1 << i)`.

> [!example] EJEMPLO — ACTIVAR EL BIT 2
> ```text
> Valor:  1000 0001
> Máscara:0000 0100
> OR:     1000 0101
> ```

## DESPLAZAMIENTOS

Un desplazamiento lógico a la izquierda mueve los bits hacia posiciones más altas y añade ceros por la derecha. A la derecha hace lo contrario, añadiendo ceros por la izquierda. Los bits que salen del ancho se pierden.

```text
8 bits:  0001 0110  (22)
<< 1:   0010 1100  (44)
>> 2:   0000 0101  (5)
```

Sin desbordamiento, desplazar un entero sin signo $k$ posiciones a la izquierda multiplica por $2^k$. Desplazar a la derecha divide por $2^k$ **descartando el resto**.

> [!note] NOTA
> El **desplazamiento aritmético a la derecha** replica el bit de signo y se estudia en [Desplazadores](../components/shifters.md). No equivale a un desplazamiento lógico cuando el valor es negativo.

## USOS DE XOR

- `x XOR 0 = x`: deja un bit intacto.
- `x XOR 1 = NOT x`: invierte un bit.
- `x XOR x = 0`: detecta igualdad entre patrones.
- `x XOR m`: permite invertir **solo** los bits seleccionados en la máscara $m$.
