---
aliases: [Multiplicador binario, Shift-and-add multiplier]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# MULTIPLICACIÓN BINARIA

> [!seealso]- MIRA TAMBIÉN
> - [Sumador completo](full_adder.md)
> - [Desplazadores](../components/shifters.md)
> - [Complemento a dos](../representation/twos_complement.md)

> [!important] CONCEPTOS IMPORTANTES
> - La multiplicación binaria se basa en **productos parciales** y sumas.
> - Multiplicar por un bit `0` produce 0; multiplicar por `1` conserva el multiplicando.
> - El producto exacto de dos operandos sin signo de $n$ bits puede requerir **hasta $2n$ bits**.
> - Los negativos pueden tratarse mediante signo y magnitud temporal o mediante algoritmos especializados.
## DEFINICIÓN

Un **multiplicador binario** calcula $A\times B$. Para entenderlo, basta recordar la multiplicación tradicional por columnas: cada bit del multiplicador decide si añadimos una copia del multiplicando, desplazada a la posición correspondiente.

> [!abstract] FÓRMULA
> $$A\cdot B=\sum_{i=0}^{n-1}b_i(A\ll i)$$
>
> Aquí $b_i$ es el bit $i$ del multiplicador B y $\ll i$ representa el desplazamiento a la izquierda $i$ posiciones de **un acumulador suficientemente ancho**.

## MULTIPLICACIÓN PASO A PASO

> [!example] EJEMPLO — $13\times11$
>
> `13 = 1101₂` y `11 = 1011₂`:
>
> ```text
>       0000 1101  (13)
>     × 0000 1011  (11)
>     ----------
>       0000 1101  (bit 0 de B = 1)
>       0001 1010  (bit 1 de B = 1)
>       0000 0000  (bit 2 de B = 0)
>     + 0110 1000  (bit 3 de B = 1)
>     ----------
>       1000 1111  (143)
> ```

No se realiza una multiplicación nueva en cada fila: se decide si **añadir el multiplicando desplazado**.

## CIRCUITO DE DESPLAZAMIENTO Y SUMA

Una implementación iterativa puede utilizar:

- Un registro para el multiplicando.
- Un registro para el multiplicador.
- Un acumulador para el resultado parcial.
- Un sumador y lógica de desplazamiento.
- Un contador para procesar los bits.

### ALGORITMO SIN SIGNO

```text
producto = 0
para i desde 0 hasta n-1:
    si el bit i de B es 1:
        producto = producto + (A << i)
```

> [!warning] ANCHO INTERNO
> El `producto`, las sumas y los valores desplazados deben conservar los bits necesarios (normalmente hasta $2n$ bits). Si se utiliza un registro de solo $n$ bits, se puede perder parte del resultado.

## MULTIPLICACIÓN COMBINACIONAL

Otra arquitectura genera todos los productos parciales simultáneamente mediante AND:

$$p_{ij}=A_i\land B_j$$

Después, una red de [sumadores](full_adder.md) combina los productos parciales alineados. Según la arquitectura (matriz, árbol de Wallace, etc.) cambian área y retardo, pero no la operación matemática.

## MULTIPLICACIÓN CON SIGNO

Para aprender un multiplicador con signo, una estrategia conceptual clara es:

1. Determinar el signo del resultado mediante XOR de los signos de los operandos.
2. Obtener las magnitudes **sin signo**, con suficiente ancho para representar también la magnitud del mínimo negativo.
3. Multiplicar las magnitudes y guardar el resultado en hasta $2n$ bits.
4. Si los signos son diferentes, negar el resultado en complemento a dos de $2n$ bits.

> [!example] EJEMPLO — $-3\times5$
> $3\times5=15$; signos diferentes → resultado -15.
>
> En 8 bits, $-15=1111\,0001_2$. Si los operandos eran de 8 bits y se almacena el producto **completo** en 16 bits: `1111 1111 1111 0001` (`0xFFF1`).

En hardware existen técnicas que trabajan directamente con operandos en complemento a dos (por ejemplo, **Booth**), pero no son necesarias para entender el funcionamiento básico.

## DESBORDAMIENTO Y TRUNCAMIENTO

Si solo se guardan los $n$ bits bajos, el resultado es el producto módulo $2^n$. Eso puede ser útil para determinados cálculos modulares, pero **no** equivale al producto completo de los operandos.

## EJERCICIOS

1. Multiplica `101₂ × 110₂` mediante productos parciales.
2. ¿Cuántos bits puede necesitar el producto sin signo de dos operandos de 8 bits?
3. Calcula `-7 × 3` y escríbelo en complemento a dos de 8 bits.
