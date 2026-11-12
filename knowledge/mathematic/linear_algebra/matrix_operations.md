---
aliases: [Operaciones matriciales]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-12 01:07:10
rating: 
tags: [Math]
---

# OPERACIONES CON MATRICES

> [!external-link]- REFERENCIAS WEB
> - [NumPy: multiplicación de matrices (`matmul`)](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)
> - [NumPy: guía de operaciones básicas](https://numpy.org/doc/stable/user/quickstart)

> [!seealso]- MIRA TAMBIÉN
> - [Matrices](matrix.md)
> - [Escalares](scalar.md)
> - [Vectores](vector.md)
> - [Determinantes](matrix_determinants.md)
> - [Matrices inversas](matrix_inverse.md)
> - [Matrices booleanas](../discrete_mathematics/boolean_matrices.md)
> - [Chuleta de matrices](matrix_cheatsheet.md)

Las **operaciones con matrices** permiten combinar o transformar sus elementos. Aunque algunas recuerdan a las operaciones con números, no se realizan siempre de la misma manera: unas actúan **elemento a elemento** y otras combinan **filas y columnas**.

Antes de operar, debemos comprobar las **dimensiones**. Una operación con matrices incompatibles no está definida.

## SUMA Y RESTA

La suma y la resta se calculan combinando los elementos que ocupan la **misma posición**. Por eso, las dos matrices deben tener el **mismo número de filas y columnas**.

> [!syntax] SINTAXIS
> 
> Si $A, B \in M_{m \times n}$:
> 
> $$
> (A \pm B)_{ij} = a_{ij} \pm b_{ij}
> $$

> [!example] EJEMPLO
> 
> $$
> \begin{aligned}
> A &= \begin{pmatrix}1 & 2 \\  3 & 4\end{pmatrix}\\
> B &= \begin{pmatrix}5 & 0 \\ -1 & 2\end{pmatrix}
> \end{aligned}
> $$
> 
> $$
> A + B = \begin{pmatrix}
> 1 +   5  & 2 + 0\\
> 3 + (-1) & 4 + 2
> \end{pmatrix}
> = \begin{pmatrix}
> 6 & 2\\
> 2 & 6
> \end{pmatrix}
> $$
> 
> La resta se calcula del mismo modo, pero restando los elementos correspondientes.

Propiedades de la suma (para matrices del mismo orden):

- **Conmutativa:** $A + B = B + A$.
- **Asociativa:** $(A + B) + C = A + (B + C)$.
- **Elemento neutro:** $A + 0 = A$.
- **Opuesto:** $A + (-A) = 0$.

> [!note] NOTA (para programadores)
> Con NumPy, `+` y `-` realizan estas operaciones directamente sobre arrays de la misma forma:
> 
> ```python
> import numpy as np
>
> A = np.array(
>     [[1, 2],
>      [3, 4]]
> )
> B = np.array(
>     [[ 5, 0],
>      [-1, 2]]
> )
>
> print(A + B)
> # SALIDA:
> # [[6 2]
> #  [2 6]]
> 
> print(A - B)
> # SALIDA:
> # [[-4  2]
> #  [ 4  2]]
> ```
> 
> NumPy también tiene **broadcasting**, que permite operar arrays de ciertas formas distintas. Eso es una funcionalidad de la biblioteca y **no modifica la regla matemática** de suma de matrices del mismo orden.

## PRODUCTO POR UN ESCALAR

Multiplicar una matriz por un [escalar](scalar.md) $k$ significa multiplicar **cada uno de sus elementos** por $k$. El resultado mantiene el mismo orden que la matriz original.

> [!syntax] SINTAXIS
> 
> $$(kA)_{ij} = k \cdot a_{ij}$$

> [!example] EJEMPLO
> 
> $$
> 2 \begin{pmatrix}
> 1 & -2\\
> 0 &  3
> \end{pmatrix}
> = \begin{pmatrix}
> 2 & -4\\
> 0 &  6
> \end{pmatrix}
> $$

> [!note] NOTA (para programadores)
> 
> ```python
> import numpy as np
> 
> A = np.array(
>     [[1, -2],
>      [0,  3]]
> )
> 
> print(2 * A)
> # SALIDA:
> # [[2 -4]
> #  [0  6]]
> ```
> 
> En este caso `2 * A` tiene el mismo significado en NumPy que en matemáticas.

## PRODUCTO DE DOS MATRICES

La multiplicación matricial **no se hace posición a posición**. Cada elemento del resultado se calcula mediante el **producto escalar de una fila** de la primera matriz con una **columna** de la segunda.

Solo puede realizarse si el número de **columnas de la primera matriz** coincide con el número de **filas de la segunda**.

> [!syntax] SINTAXIS
> 
> $$
> \underbrace{A_{m \times p}}_{\text{filas }m}
> \cdot
> \underbrace{B_{p \times n}}_{\text{columnas }n}
> = C_{m \times n}
> $$
> 
> El elemento de la fila $i$, columna $j$ del producto es:
> 
> $$
> c_{ij} = \sum_{k = 1}^{p} a_{ik} b_{kj}
> $$
> 
> El índice $k$ recorre las $p$ posiciones de la fila de $A$ y de la columna de $B$.

> [!example] EJEMPLO PASO A PASO
> 
> $$
> A = \begin{pmatrix}
> 1 & 2\\
> 0 & 1
> \end{pmatrix}
> \qquad
> B = \begin{pmatrix}
> 0 & 1\\
> 2 & 3
> \end{pmatrix}
> $$
> 
> Ambas matrices son $2 \times 2$, por lo que el producto tendrá orden $2 \times 2$.
> 
> $$
> \begin{aligned}
> c_{11} &= 1 \cdot 0 + 2 \cdot 2 = 4\\
> c_{12} &= 1 \cdot 1 + 2 \cdot 3 = 7\\
> c_{21} &= 0 \cdot 0 + 1 \cdot 2 = 2\\
> c_{22} &= 0 \cdot 1 + 1 \cdot 3 = 3
> \end{aligned}
> $$
> 
> $$
> AB = \begin{pmatrix}
> 4 & 7\\
> 2 & 3
> \end{pmatrix}
> $$

> [!important] IMPORTANTE
> **El orden importa.** En general, $AB \ne BA$; incluso puede estar definido $AB$ y no estarlo $BA$. La multiplicación de matrices **no es conmutativa**.

Propiedades (siempre que las dimensiones sean compatibles):

- **Asociativa:** $A(BC) = (AB)C$.
- **Distributiva:** $A(B + C) = AB + AC$ y $(A + B)C = AC + BC$.
- **Identidad:** si $A$ es $m \times n$, entonces $I_mA = A = AI_n$.
- **Compatibilidad con escalares:** $k(AB) = (kA)B = A(kB)$.

> [!note] NOTA (para programadores)
> En NumPy, el operador **`@`** representa el producto matricial. En cambio, **`*`** entre arrays multiplica elemento a elemento.
> 
> ```python
> import numpy as np
> 
> A = np.array(
>     [[1, 2],
>      [0, 1]]
> )
> B = np.array(
>     [[0, 1],
>      [2, 3]]
> )
>
> print(A @ B) # producto matricial
> # SALIDA:
> # [[4 7]
> #  [2 3]]
> 
> print(A * B) # elemento a elemento
> # SALIDA:
> # [[0 2]
> #  [0 3]]
> ```
>
> `A @ B` también puede escribirse `np.matmul(A, B)`. Si las dimensiones no son compatibles, NumPy lanza un `ValueError`.

## MATRIZ TRANSPUESTA

La **transpuesta** $A^T$ se obtiene convirtiendo las **filas de $A$ en columnas**, respetando el orden de sus elementos. Una matriz $m \times n$ pasa a ser $n \times m$.

> [!syntax] SINTAXIS
> 
> $$(A^T)_{ij} = a_{ji}$$

> [!example] EJEMPLO
> 
> $$
> \begin{pmatrix}
> 1 & 2 & 3\\
> 4 & 5 & 6
> \end{pmatrix}^{T}
> = \begin{pmatrix}
> 1 & 4\\
> 2 & 5\\
> 3 & 6
> \end{pmatrix}
> $$

Propiedades:

- $(A^T)^T = A$.
- $(A + B)^T = A^T + B^T$.
- $(kA)^T = kA^T$.
- $(AB)^T = B^T A^T$: **cambia el orden**.

> [!note] NOTA (para programadores)
> 
> ```python
> import numpy as np
> 
> A = np.array(
>     [[1, 2, 3],
>      [4, 5, 6]]
> )
> 
> print(A.T) # Forma (3, 2)
> # SALIDA:
> # [[1 4]
> #  [2 5]
> #  [3 6]]
> 
> print(A.T.shape)
> # SALIDA:
> # (3, 2)
> ```

## POTENCIA DE UNA MATRIZ

La potencia usual $A^k$ consiste en multiplicar una matriz **cuadrada** por sí misma $k$ veces. Para $k=0$, el resultado es la matriz identidad.

> [!syntax] SINTAXIS
> 
> $$
> \begin{aligned}
> A^0 &= I_n\\
> A^1 &= A\\
> A^2 &= AA\\
> A^3 &= AAA
> \end{aligned}
> $$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 1 & 1\\
> 0 & 1
> \end{pmatrix}
> \quad\Longrightarrow\quad
> A^2 = \begin{pmatrix}
> 1 & 2\\
> 0 & 1
> \end{pmatrix}
> $$

> [!note] NOTA (para programadores)
> __`A ** 2` no calcula $A^2$__: eleva cada componente al cuadrado. Utiliza `np.linalg.matrix_power(A, 2)` para la potencia matricial.
> 
> ```python
> import numpy as np
> 
> A = np.array(
>     [[1, 1],
>      [0, 1]]
> )
> 
> print(np.linalg.matrix_power(A, 2))
> # SALIDA:
> # [[1 2]
> #  [0 1]]
> 
> print(A ** 2)
> # SALIDA:
> # [[1 1]
> #  [0 1]]
> ```

## OPERACIONES ELEMENTALES POR FILAS

Son transformaciones que permiten simplificar una matriz para resolver sistemas de ecuaciones o hallar una [inversa](matrix_inverse.md). Las tres operaciones admitidas son:

- **Intercambiar filas:** $F_i \leftrightarrow F_j$.
- **Multiplicar una fila por un escalar no nulo:** $F_i \leftarrow kF_i$, con $k \ne 0$.
- **Sumar a una fila un múltiplo de otra:** $F_i \leftarrow F_i + kF_j$, con $i \ne j$.

> [!example] EJEMPLO
> 
> $$
> \begin{pmatrix}
> 1 & 2\\
> 3 & 7
> \end{pmatrix}
> \xrightarrow{F_2 \leftarrow F_2 - 3F_1}
> \begin{pmatrix}
> 1 & 2\\
> 0 & 1
> \end{pmatrix}
> $$
> 
> Hemos restado tres veces la primera fila a la segunda para crear un cero.

> [!note] NOTA (para programadores)
> 
> ```python
> import numpy as np
> 
> A = np.array(
>     [[1, 2],
>      [3, 7]],
>     dtype = float
> )
> 
> A[1] = A[1] - 3 * A[0] # Fila 2 <- Fila 2 - 3*Fila 1
> 
> print(A)
> # [[1. 2.]
> #  [0. 1.]]
> ```

## PRODUCTO POR BLOQUES

Cuando las matrices son grandes, podemos dividirlas en **submatrices (bloques)** y multiplicar esos bloques utilizando las mismas reglas del producto matricial. Las particiones deben ser compatibles para poder sumar y multiplicar los bloques correspondientes.

> [!syntax] SINTAXIS
> 
> Para una partición en cuatro bloques:
> 
> $$
> A = \begin{pmatrix}
> A_{11} & A_{12}\\
> A_{21} & A_{22}
> \end{pmatrix}
> \quad
> B = \begin{pmatrix}
> B_{11} & B_{12}\\
> B_{21} & B_{22}
> \end{pmatrix}
> $$
> 
> El bloque superior izquierdo de $AB$ se obtiene con:
> 
> $$
> (AB)_{11} = A_{11}B_{11} + A_{12}B_{21}
> $$
> 
> No es una multiplicación de bloques de la misma posición: cada bloque del resultado combina **filas de bloques** con **columnas de bloques**.

## RESUMEN

| OPERACIÓN | CONDICIÓN                          | RESULTADO                            |
|:--------- |:---------------------------------- |:------------------------------------ |
| $A \pm B$ | Mismas dimensiones.                | Se opera elemento a elemento.        |
| $kA$      | Escalar $k$.                       | Cada elemento se multiplica por $k$. |
| $AB$      | Columnas de $A$ = filas de $B$.    | Producto fila-columna.               |
| $A^T$     | Cualquier matriz.                  | Intercambia filas y columnas.        |
| $A^k$     | Matriz cuadrada; $k \ge 0$ entero. | Multiplicación matricial repetida.   |

> [!warning] ERRORES FRECUENTES
> - Utilizar $A_{ij}B_{ij}$ como si fuera el producto matricial general.
> - Suponer que $AB = BA$.
> - Confundir el producto `@` con el producto `*` de NumPy.
> - Confundir la potencia matemática $A^2$ con `A ** 2` de NumPy.
> - Olvidar comprobar las dimensiones antes de multiplicar.
