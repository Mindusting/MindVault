---
aliases: [Matrices en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-12 01:12:40
rating: 
tags: [Math]
---

# MATRICES

> [!external-link]- REFERENCIAS WEB
> - [NumPy: guía de iniciación](https://numpy.org/doc/stable/user/quickstart)

> [!seealso]- MIRA TAMBIÉN
> - [Álgebra lineal](linear_algebra.md)
> - [Vectores](vector.md)
> - [Escalares](scalar.md)
> - [Operaciones con matrices](matrix_operations.md)
> - [Determinantes](matrix_determinants.md)
> - [Matrices inversas](matrix_inverse.md)
> - [Matrices booleanas](../discrete_mathematics/boolean_matrices.md)
> - [Chuleta de matrices](matrix_cheatsheet.md)

Una **matriz** es una disposición rectangular de elementos, normalmente números, organizada en **filas** y **columnas**. Permite representar varios valores de forma ordenada y operar con ellos siguiendo unas reglas determinadas. Por ejemplo, una matriz puede representar un sistema de ecuaciones, una transformación geométrica o una tabla de datos numéricos.

A diferencia de un número aislado, una matriz tiene una **forma** o **dimensión** que condiciona las operaciones que podemos realizar con ella.

## REPRESENTACIÓN Y NOTACIÓN

> [!syntax] SINTAXIS
> 
> $$
> A = \begin{pmatrix}
> a_{11} & a_{12} & \cdots & a_{1n}\\
> a_{21} & a_{22} & \cdots & a_{2n}\\
> \vdots & \vdots & \ddots & \vdots\\
> a_{m1} & a_{m2} & \cdots & a_{mn}
> \end{pmatrix}
> $$
> 
> - **$A$:** nombre de la matriz.
> - **$m$:** número de filas.
> - **$n$:** número de columnas.
> - **$m \times n$:** orden o dimensión de la matriz, siempre **filas $\times$ columnas**.
> - **$a_{ij}$:** elemento de la **fila $i$**, **columna $j$**.
> 
> Si todos sus elementos son reales, escribimos $A \in M_{m \times n}(\mathbb{R})$.

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 3 & 4 &  1\\
> 0 & 2 & -1
> \end{pmatrix}
> $$
> 
> - Su orden es $2 \times 3$: dos filas y tres columnas.
> - $a_{12} = 4$: primera fila, segunda columna.
> - $a_{23} = -1$: segunda fila, tercera columna.

### IGUALDAD DE MATRICES

Dos matrices son **iguales** cuando tienen las mismas dimensiones y cada elemento coincide con el que ocupa la misma posición en la otra matriz.

$$
A = B
\iff
\begin{cases}
\text{tienen el mismo orden}\\
a_{ij} = b_{ij}\text{ para todo }i, j
\end{cases}
$$

Por ejemplo, cambiar de posición dos filas generalmente produce otra matriz, aunque contenga los mismos números.

### SUBMATRICES

Una **submatriz** se obtiene seleccionando algunas filas y columnas de una matriz y conservando el orden de sus elementos. Una forma habitual de obtenerla consiste en eliminar filas o columnas.

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 3 & 4 &  1\\
> 0 & 2 & -1
> \end{pmatrix}
> \qquad
> B = \begin{pmatrix}
> 4 &  1\\
> 2 & -1
> \end{pmatrix}
> $$
> 
> Hemos obtenido $B$ eliminando la primera columna de $A$.

## TIPOS DE MATRICES

### SEGÚN SUS DIMENSIONES

- **Matriz fila:** tiene una sola fila ($1 \times n$).
- **Matriz columna:** tiene una sola columna ($m \times 1$).
- **Matriz cuadrada:** tiene tantas filas como columnas ($n \times n$).

> [!example] EJEMPLO
> 
> $$
> F = \begin{pmatrix}
> 2 & 5 & -1
> \end{pmatrix}
> \qquad
> C = \begin{pmatrix}
>  2\\
>  5\\
> -1
> \end{pmatrix}
> $$
> 
> $F$ es una matriz fila de orden $1 \times 3$ y $C$ una matriz columna de orden $3 \times 1$.

### SEGÚN SUS ELEMENTOS

- **Matriz nula ($0_{m \times n}$):** todos sus elementos son cero. Puede ser rectangular.
- **Matriz diagonal:** es cuadrada y todos sus elementos **fuera** de la diagonal principal son cero; los de la diagonal pueden ser cero o distintos de cero.
- **Matriz identidad ($I_n$):** es diagonal, con unos en la diagonal principal. Se comporta como el número $1$ en la multiplicación de matrices compatibles.
- **Triangular superior:** es cuadrada y tiene ceros **debajo** de la diagonal.
- **Triangular inferior:** es cuadrada y tiene ceros **encima** de la diagonal.
- **Simétrica:** es cuadrada y sus elementos se reflejan respecto a la diagonal principal: $a_{ij} = a_{ji}$, es decir, $A^T = A$.

> [!example] EJEMPLOS
> 
> $$
> I_3 = \begin{pmatrix}
> 1 & 0 & 0\\
> 0 & 1 & 0\\
> 0 & 0 & 1
> \end{pmatrix}
> \qquad
> D = \begin{pmatrix}
> 2 &  0\\
> 0 & -3
> \end{pmatrix}
> $$
> 
> $$
> S = \begin{pmatrix}
> 1 & 4\\
> 4 & 2
> \end{pmatrix}
> \qquad
> T = \begin{pmatrix}
> 1 & 5\\
> 0 & 2
> \end{pmatrix}
> $$
> 
> - $I_3$ es la identidad, $D$ es diagonal, $S$ es simétrica y $T$ es triangular superior.
> - Una matriz puede pertenecer a **varias categorías simultáneamente**; por ejemplo, toda matriz diagonal es triangular superior e inferior.

## RELACIÓN CON LOS VECTORES

Un [vector](vector.md) de $n$ componentes puede representarse como una matriz fila ($1 \times n$) o una matriz columna ($n \times 1$). Aunque tienen los mismos componentes, **su disposición importa** en una multiplicación matricial.

La operación de [transposición](matrix_operations.md#MATRIZ%20TRANSPUESTA) convierte una matriz fila en una matriz columna y viceversa.

## NOTA PARA PROGRAMADORES: NUMPY

> [!note] NOTA (para programadores)
> En Python podemos representar matrices mediante **arrays bidimensionales** de NumPy (`numpy.ndarray`). Su propiedad `shape` indica las dimensiones, pero **los índices empiezan en cero**, mientras que en la notación matemática habitual empiezan en uno.
> 
> ```python
> import numpy as np
>
> A = np.array(
>     [[3, 4,  1],
>      [0, 2, -1]]
> )
>
> print(A.shape)
> # SALIDA:
> # (2, 3)
> 
> print(A[0, 1]) # 4  -> a_12 en matemáticas
> print(A[1, 2]) # -1 -> a_23 en matemáticas
>
> B = A[:, 1:]   # Elimina la primera columna
> print(B.shape) # (2, 2)
>
> I = np.eye(3, dtype=int) # Matriz identidad 3x3
> 
> print(I)
> # SALIDA:
> # [[1 0 0]
> #  [0 1 0]
> #  [0 0 1]]
> 
> Z = np.zeros((2, 3), dtype=int) # Matriz nula 2x3
> 
> print(Z)
> # SALIDA:
> # [[0 0 0]
> #  [0 0 0]]
> ```
> 
> Un `np.array([2, 5, -1])` tiene forma `(3,)`: **no** es lo mismo que una matriz fila de forma `(1, 3)` ni una columna de forma `(3, 1)`. Podemos construirlas con `np.array([[2, 5, -1]])` y `np.array([[2], [5], [-1]])`.
> 
> Para comparar matrices completas, utiliza `np.array_equal(A, B)`. El operador `A == B` produce comparaciones **elemento a elemento**, no un único booleano.

## RESUMEN

| CONCEPTO           | IDEA FUNDAMENTAL                          |
|:------------------ |:----------------------------------------- |
| Orden $m \times n$ | $m$ filas y $n$ columnas.                 |
| Elemento $a_{ij}$  | Primero fila, después columna.            |
| Matriz cuadrada    | Mismo número de filas y columnas.         |
| Identidad $I_n$    | Neutro del producto matricial compatible. |
| Matriz simétrica   | $A^T=A$.                                  |

> [!warning] ERRORES FRECUENTES
> - Confundir una matriz de $2 \times 3$ con una de $3 \times 2$.
> - Pensar que tener los mismos elementos basta para que dos matrices sean iguales.
> - Confundir una matriz identidad con una matriz llena de unos.
> - Confundir los índices matemáticos (*desde $1$*) con los de Python (*desde $0$*).
