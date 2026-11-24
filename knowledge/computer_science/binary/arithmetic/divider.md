---
aliases: [Divisor binario, Restoring division]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# DIVISIÓN BINARIA

> [!seealso]- MIRA TAMBIÉN
> - [Sumador y restador](adder_subtractor.md)
> - [Comparadores](../components/comparators.md)
> - [Desplazadores](../components/shifters.md)
> - [Complemento a dos](../representation/twos_complement.md)

> [!important] CONCEPTOS IMPORTANTES
> - La división binaria obtiene **cociente** y **resto** utilizando comparaciones, desplazamientos y restas.
> - Puede implementarse con el algoritmo de división larga, sin dividir mediante instrucciones especiales.
> - La división entera por cero es inválida; al operar con signo hay que definir cómo se redondea el cociente.
> - En ancho fijo, dividir el mínimo negativo entre -1 puede **desbordar**.
## DEFINICIÓN

La **división entera** de un dividendo $A$ entre un divisor $B\ne0$ produce un cociente $Q$ y un resto $R$. Para operandos sin signo, se cumple:

> [!abstract] IDENTIDAD
> $$A=BQ+R,\qquad0\le R<B$$

La división larga binaria es muy parecida a la decimal: vamos incorporando bits del dividendo, comprobamos si el divisor cabe y, si cabe, lo restamos.

## ALGORITMO DE DIVISIÓN LARGA SIN SIGNO

Una implementación didáctica, procesando del **MSB al LSB**, mantiene un resto parcial:

```text
si divisor == 0:
    error "división por cero"

cociente = 0
resto = 0

para i desde n-1 hasta 0:
    resto = (resto << 1) | bit_i(dividendo)

    si resto >= divisor:
        resto = resto - divisor
        poner bit_i(cociente) = 1
```

Este algoritmo también se conoce, en su forma hardware habitual, como una variante de división **restauradora** (*restoring division*) cuando se prueba una resta y se restaura el resto si no es válida. La presentación anterior compara **antes** de restar para facilitar el aprendizaje.

> [!warning] ANCHO FIJO
> En hardware, el resto parcial debe poder representar el valor temporal al desplazar y añadir el bit siguiente. Una implementación directa puede usar **$n+1$ bits para el resto temporal**, o diseñar las comparaciones y desplazamientos para evitar perder un bit. No se debe truncar ese resto antes de comparar con el divisor.

## EJEMPLO PASO A PASO: $13\div3$

Dividendo: `1101₂` (13). Divisor: `0011₂` (3). Procesamos los bits `1`, `1`, `0`, `1` de izquierda a derecha:

| Paso | Bit incorporado | Resto antes de comparar | ¿Resto ≥ 3? | Bit de Q | Nuevo resto |
| ---: | :-: | ---: | :-: | :-: | ---: |
| 1 | 1 | 1 | No | 0 | 1 |
| 2 | 1 | 3 | Sí | 1 | 0 |
| 3 | 0 | 0 | No | 0 | 0 |
| 4 | 1 | 1 | No | 0 | 1 |

Cociente obtenido: `0100₂` (4). Resto: `0001₂` (1).

> [!example] COMPROBACIÓN
> $$13=3\cdot4+1$$

## COMPONENTES DE UN DIVISOR

Un divisor secuencial básico reutiliza durante varios ciclos:

- Un **registro de resto parcial**.
- Un **registro de cociente** y otro de divisor.
- Un **comparador** o restador para decidir si el divisor cabe.
- Un **restador** para actualizar el resto.
- **Desplazadores** y lógica de control.

Existen algoritmos más avanzados: división no restauradora, división de SRT y otros. Primero conviene dominar la versión por desplazamiento y resta.

## DIVISIÓN CON SIGNO

Para operadores con signo en complemento a dos, una implementación fácil de razonar es trabajar con magnitudes de ancho suficiente, dividir **sin signo** y después aplicar signos.

En muchas ISA y lenguajes habituales, la división entera con signo **trunca hacia cero**. Con esa convención:

- El cociente es negativo si los operandos tienen signos distintos.
- Si el resto es distinto de cero, conserva el signo del **dividendo**.
- Siempre se cumple $A=BQ+R$ y $|R|<|B|$.

> [!example] EJEMPLO — $-13\div3$
> $$Q=-4,\qquad R=-1$$
>
> Comprobación: $-13=3\cdot(-4)+(-1)$.

> [!warning] CONVENCIÓN IMPORTANTE
> Algunos contextos matemáticos y lenguajes usan **división hacia $-\infty$** en vez de truncamiento hacia cero; cambian cociente y resto en casos negativos. Por ejemplo, Python usa `-13 // 3 == -5` y `-13 % 3 == 2`. Antes de implementar un divisor hay que elegir la semántica.

## CASOS LÍMITE

- **Divisor cero:** no hay un cociente entero definido.
- **Dividendo menor que divisor (sin signo):** cociente 0, resto igual al dividendo.
- **Resto 0:** la división es exacta.
- **Mínimo con signo entre -1:** en 8 bits, $-128/-1=128$, valor que no cabe en 8 bits con signo; exige detectar desbordamiento o ampliar el resultado.

## EJERCICIOS

1. Calcula `10111₂ / 11₂` (23 entre 3), obteniendo cociente y resto.
2. Explica cómo dividir sin usar un tipo de dato del doble de tamaño.
3. Calcula `-17 / 5` con truncamiento hacia cero.
4. ¿Qué problema aparece al dividir -128 entre -1 usando enteros con signo de 8 bits?
