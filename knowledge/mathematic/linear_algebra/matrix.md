---
aliases: [Matrices en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-10 05:30:11
rating: 
tags: [Math]
---

# MATRICES

> [!seealso]- MIRA TAMBIÉN
> - [Álgebra lineal](linear_algebra.md)
> - [Vectores](vector.md)
> - [Escalares](scalar.md)
> - [Operaciones con matrices](matrix_operations.md)
> - [Determinantes](matrix_determinants.md)
> - [Matrices inversas](matrix_inverse.md)
> - [Matrices booleanas](../discrete_mathematics/boolean_matrices.md)

Una **matriz** es una tabla rectangular de elementos, generalmente números, organizada en **filas** y **columnas**.

- **Orden o dimensión:** $m \times n$, donde $m$ es el número de filas y $n$ el de columnas.
- **Elemento $a_{ij}$:** número situado en la fila $i$ y la columna $j$ (en ese orden).
- **Notación:** $A=(a_{ij}) \in M_{m \times n}(\mathbb{R})$ para matrices reales.

> [!syntax] SINTAXIS
> 
> $$
> A = \begin{pmatrix}
> a_{11}& a_{12}& \cdots& a_{1n}\\
> a_{21}& a_{22}& \cdots& a_{2n}\\
> \vdots& \vdots& \ddots& \vdots\\
> a_{m1}& a_{m2}& \cdots& a_{mn}
> \end{pmatrix}
> $$

> [!example] EJEMPLO
> 
> $$A = \begin{pmatrix}
> 3&  4&  1\\
> 0&  2& -1
> \end{pmatrix}
> $$
> 
> - Orden: $2 \times 3$.
> - $a_{12} = 4$; $a_{23} = -1$.

## IGUALDAD Y SUBMATRICES

- **Igualdad:** $A = B$ si tienen el mismo orden y $a_{ij} = b_{ij}$ en todas las posiciones.
- **Submatriz:** se obtiene eliminando filas o columnas de otra matriz.

## TIPOS DE MATRICES

- **Fila:** una sola fila ($1 \times n$).
- **Columna:** una sola columna ($m \times 1$).
- **Cuadrada:** mismo número de filas y columnas ($n \times n$).
- **Nula:** todos sus elementos son cero; se representa por $0$ o $0_{m \times n}$.
- **Diagonal:** cuadrada con ceros fuera de la diagonal principal.
- **Identidad ($I_n$):** diagonal con unos en la diagonal principal.
- **Triangular superior:** ceros por debajo de la diagonal.
- **Triangular inferior:** ceros por encima de la diagonal.
- **Simétrica:** cuadrada y $A^T=A$.

> [!example] EJEMPLOS
> 
> $$
> I_3 = \begin{pmatrix}
> 1& 0& 0\\
> 0& 1& 0\\
> 0& 0& 1
> \end{pmatrix}
> \qquad
> D = \begin{pmatrix}
> 2&  0\\
> 0& -3
> \end{pmatrix}
> $$
> 
> - $I_3$: identidad de orden $3$.
> - $D$: diagonal de orden $2$.

## VECTORES Y MATRICES

- Un [vector](vector.md) puede escribirse como **matriz fila** o como **matriz columna**.
- La **transpuesta** intercambia filas y columnas. Consulta [Operaciones con matrices](matrix_operations.md).

## RESUMEN

| CONCEPTO           | QUÉ RECORDAR                                              |
|:------------------ |:--------------------------------------------------------- |
| Orden $m \times n$ | $m$ filas, $n$ columnas.                                  |
| $a_{ij}$           | Fila $i$, columna $j$.                                    |
| Matriz cuadrada    | Mismo número de filas y columnas.                         |
| Matriz identidad   | Neutro de la multiplicación, con dimensiones compatibles. |

> [!warning] ERRORES FRECUENTES
> - Confundir el orden de los índices: **primero fila, después columna**.
> - Confundir la matriz identidad (ceros y unos) con una matriz de todos unos.
> - Pensar que todas las matrices son cuadradas.
