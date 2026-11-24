---
aliases: [Boolean algebra, Álgebra booleana]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# ÁLGEBRA DE BOOLE

> [!seealso]- MIRA TAMBIÉN
> - [Puertas lógicas](logic_gates.md)
> - [Construcciones con NAND](nand_composition.md)
> - [Conectores lógicos en matemáticas](../../../mathematic/discrete_mathematics/logic/logical_connectives.md)

> [!important] CONCEPTOS IMPORTANTES
> - El álgebra de Boole opera con dos valores: falso (`0`) y verdadero (`1`).
> - Las expresiones lógicas describen el comportamiento de las puertas y los circuitos.
> - Las leyes de De Morgan permiten transformar expresiones AND/OR en combinaciones con NOT.
## DEFINICIÓN

El **álgebra de Boole** estudia operaciones sobre valores lógicos. Es la base matemática del diseño digital: una expresión determina qué salida debe producir un circuito ante cada combinación de entradas.

> [!abstract] OPERACIONES
> - Negación: $\overline A$ (**NOT**).
> - Conjunción: $A\land B$ o $AB$ (**AND**).
> - Disyunción: $A\lor B$ o $A+B$ en notación booleana (**OR**).
> - Disyunción exclusiva: $A\oplus B$ (**XOR**).
>
> En fórmulas booleanas, `+` puede representar OR: **no** es una suma entera convencional.

## LEYES FUNDAMENTALES

| Ley | AND | OR |
| --- | --- | --- |
| Identidad | $A\land1=A$ | $A\lor0=A$ |
| Dominación | $A\land0=0$ | $A\lor1=1$ |
| Idempotencia | $A\land A=A$ | $A\lor A=A$ |
| Complemento | $A\land\overline A=0$ | $A\lor\overline A=1$ |
| Conmutativa | $A\land B=B\land A$ | $A\lor B=B\lor A$ |

Otras propiedades:

$$\overline{\overline A}=A$$

$$A\land(B\lor C)=(A\land B)\lor(A\land C)$$

$$A\lor(A\land B)=A \quad\text{(absorción)}$$

## LEYES DE DE MORGAN

> [!abstract] EQUIVALENCIAS
> $$\overline{A\land B}=\overline A\lor\overline B$$
> $$\overline{A\lor B}=\overline A\land\overline B$$

Por ejemplo, "no ocurre A y B a la vez" equivale a "no ocurre A o no ocurre B". Estas transformaciones ayudan a construir una función con puertas NAND o NOR.

## SIMPLIFICAR UNA EXPRESIÓN

> [!example] EJEMPLO
> $$Y=(A\land B)\lor(A\land\overline B)$$
>
> Sacando factor común:
>
> $$Y=A\land(B\lor\overline B)=A\land1=A$$
>
> El circuito inicial podría usar varias puertas, pero su comportamiento coincide con conectar directamente $A$ a la salida.

## TABLAS DE VERDAD

Para $n$ entradas, una función combinacional tiene $2^n$ filas posibles. La tabla de verdad enumera todas ellas, sin depender de cómo esté construida físicamente.

> [!note] ORDEN DE PRIORIDAD
> Cuando no se ponen paréntesis, suele interpretarse primero NOT, después AND y por último OR. Para evitar dudas, aquí se usan paréntesis en las expresiones complejas.

## EJERCICIOS

1. Simplifica $\overline{A\land B}$ utilizando De Morgan.
2. Simplifica $(A\lor B)\land(A\lor\overline B)$.
3. ¿Cuántas filas tiene una tabla de verdad de cinco entradas?
