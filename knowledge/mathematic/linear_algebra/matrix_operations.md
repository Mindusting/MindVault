---
aliases: [Operaciones matriciales]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-10 05:28:48
rating: 
tags: [Math]
---

# OPERACIONES CON MATRICES

> [!seealso]- MIRA TAMBIÉN
> - [Matrices](matrix.md)
> - [Escalares](scalar.md)
> - [Vectores](vector.md)
> - [Determinantes](matrix_determinants.md)
> - [Matrices inversas](matrix_inverse.md)
> - [Matrices booleanas](../discrete_mathematics/boolean_matrices.md)

Las operaciones con matrices requieren respetar las **dimensiones** de sus operandos.

## SUMA Y RESTA

- Solo se pueden sumar o restar matrices del **mismo orden**.
- Se opera **elemento a elemento**: $(A \pm B)_{ij} = a_{ij} \pm b_{ij}$.

> [!example] EJEMPLO
> 
> $$
> \begin{pmatrix}
> 1& 2\\
> 3& 4
> \end{pmatrix} +
> \begin{pmatrix}
>  5& 0\\
> -1 &2
> \end{pmatrix} =
> \begin{pmatrix}
> 6& 2\\
> 2& 6
> \end{pmatrix}
> $$

- **Conmutativa:** $A + B = B + A$.
- **Asociativa:** $(A + B) + C = A + (B + C)$.
- **Neutro:** $A + 0 = A$.
- **Opuesto:** $A + (-A) = 0$.

## PRODUCTO POR UN ESCALAR

Se multiplica **cada elemento** por el escalar $k$:

> [!syntax] SINTAXIS
> 
> $$(kA)_{ij} = k\,a_{ij}$$

> [!example] EJEMPLO
> 
> $$
> 2 \begin{pmatrix}
> 1& -2\\
> 0&  3
> \end{pmatrix}
> = \begin{pmatrix}
> 2& -4\\
> 0&  6
> \end{pmatrix}
> $$

## PRODUCTO DE DOS MATRICES

Para $A_{m \times p}$ y $B_{p \times n}$:

- **Condición:** columnas de $A$ = filas de $B$ (el número $p$).
- **Resultado:** $AB$ tiene orden $m \times n$.
- Cada elemento se obtiene multiplicando una **fila** de $A$ por una **columna** de $B$ y sumando los productos.

> [!syntax] SINTAXIS
> 
> $$A_{m \times p}\, B_{p \times n} = C_{m \times n}$$
> 
> $$c_{ij} = \sum_{k = 1}^{p}a_{ik}b_{kj}$$

> [!example] EJEMPLO
> 
> $$
> \underbrace{\begin{pmatrix}
> 1& 2\\
> 0& 1
> \end{pmatrix}}_{A}
> \underbrace{\begin{pmatrix}
> 0& 1\\ 2& 3
> \end{pmatrix}}_{B}
> = \begin{pmatrix}
> 4& 7\\
> 2& 3
> \end{pmatrix}
> $$
> 
> Primera entrada: $c_{11} = 1 \cdot 0 + 2 \cdot2 = 4$.

> [!important] IMPORTANTE
> La multiplicación de matrices **no es conmutativa en general**: $AB \ne BA$. Incluso puede existir $AB$ y no existir $BA$ por sus dimensiones.

Propiedades (cuando las operaciones están definidas):

- **Asociativa:** $A(BC) = (AB)C$.
- **Distributiva:** $A(B + C) = AB + AC$.
- **Identidad:** $I_mA = A = AI_n$ para $A$ de orden $m \times n$.

## MATRIZ TRANSPUESTA

La **transpuesta** de $A$, escrita $A^T$, intercambia sus filas y columnas.

> [!syntax] SINTAXIS
> 
> $$(A^T)_{ij} = a_{ji}$$
> 
> Si $A$ es de orden $m \times n$, $A^T$ es de orden $n \times m$.

> [!example] EJEMPLO
> 
> $$
> \begin{pmatrix}
> 1& 2& 3\\
> 4& 5& 6
> \end{pmatrix}^{T}
> = \begin{pmatrix}
> 1& 4\\
> 2& 5\\
> 3& 6
> \end{pmatrix}
> $$

- $(A^T)^T = A$.
- $(A + B)^T = A^T + B^T$.
- $(AB)^T = B^TA^T$ (**cambia el orden**).

## POTENCIA DE UNA MATRIZ

Solo se define la potencia usual $A^k$ para **matrices cuadradas** y $k$ entero no negativo.

- $A^0 = I_n$.
- $A^1 = A$.
- $A^2 = AA$, $A^3 = AAA$ (producto **matricial**, no elemento a elemento).

## OPERACIONES ELEMENTALES POR FILAS

- **Intercambiar:** $F_i \leftrightarrow F_j$.
- **Multiplicar por un escalar no nulo:** $F_i \leftarrow kF_i$, $k \ne 0$.
- **Sumar un múltiplo de otra fila:** $F_i \leftarrow F_i + kF_j$, $i \ne j$.

Se utilizan en la eliminación de Gauss y para obtener la [matriz inversa](matrix_inverse.md).

## PRODUCTO POR BLOQUES

- Se pueden agrupar matrices grandes en **submatrices (bloques)**.
- El producto se calcula como un producto matricial entre bloques, **si sus dimensiones son compatibles**.
- Es un método de organización del cálculo; no cambia el resultado.

## RESUMEN

| OPERACIÓN | CONDICIÓN                      | RESULTADO                       |
|:--------- |:------------------------------ |:------------------------------- |
| $A \pm B$ | Mismo orden                    | Mismo orden.                    |
| $kA$      | $k$ escalar                    | Mismo orden.                    |
| $AB$      | Columnas de $A$ = filas de $B$ | Filas de $A$ × columnas de $B$. |
| $A^T$     | Cualquier matriz               | Intercambia filas y columnas.   |
| $A^k$     | $A$ cuadrada                   | Matriz del mismo orden.         |

> [!warning] ERRORES FRECUENTES
> - Multiplicar matrices **posición a posición**: eso no es el producto matricial habitual.
> - Suponer que $AB=BA$.
> - Intercambiar las dimensiones de la matriz resultante.
> - Pensar que la transpuesta equivale a la matriz inversa.
