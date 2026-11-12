---
aliases: [Determinantes de matrices]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-10 06:55:22
rating: 
tags: [Math]
---

# DETERMINANTES

> [!external-link]- REFERENCIAS WEB
> - [NumPy: `numpy.linalg.det`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html)

> [!seealso]- MIRA TAMBIÉN
> - [Matrices](matrix.md)
> - [Operaciones con matrices](matrix_operations.md)
> - [Matrices inversas](matrix_inverse.md)
> - [Chuleta de matrices](matrix_cheatsheet.md)

El **determinante** es un **número** que se calcula a partir de una **matriz cuadrada**. Se representa mediante $\det(A)$ o $|A|$ y permite conocer propiedades importantes de la matriz sin tener que realizar todas sus operaciones.

En particular, permite decidir si una matriz es **invertible**:

- **$\det(A) \ne 0$:** la matriz tiene inversa.
- **$\det(A) = 0$:** la matriz no tiene inversa; sus filas o columnas son linealmente dependientes.

En matrices reales que representan transformaciones geométricas, el **valor absoluto** del determinante indica cuánto se escala el área (en dos dimensiones) o el volumen (en tres dimensiones); su **signo** indica si cambia la orientación.

## DETERMINANTE DE ORDEN 1

Cuando la matriz tiene un solo elemento, el determinante es ese elemento.

> [!syntax] SINTAXIS
> 
> $$
> A = \begin{pmatrix} a \end{pmatrix}
> \quad \Longrightarrow \quad
> \det(A) = a
> $$

## DETERMINANTE DE ORDEN 2

Para una matriz $2 \times 2$, multiplicamos los elementos de la diagonal principal y restamos el producto de la diagonal secundaria.

> [!syntax] SINTAXIS
> 
> $$
> A = \begin{pmatrix}
> a & b\\
> c & d
> \end{pmatrix}
> $$
> 
> $$
> \det(A) = ad - bc
> $$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 1 & -1\\
> 2 & 3
> \end{pmatrix}
> $$
> 
> $$
> \begin{aligned}
> \det(A) &= 1\cdot3 - (-1)\cdot2\\
> &= 3 + 2\\
> &= 5
> \end{aligned}
> $$
> 
> Como el resultado es distinto de cero, $A$ es invertible.

## DETERMINANTE DE ORDEN 3: REGLA DE SARRUS

Para matrices $3 \times 3$ podemos utilizar la **regla de Sarrus**: sumamos tres productos de diagonales en una dirección y restamos otros tres productos en la dirección contraria.

> [!syntax] SINTAXIS
> 
> $$
> A = \begin{pmatrix}
> a & b & c\\
> d & e & f\\
> g & h & i
> \end{pmatrix}
> $$
> 
> $$
> \begin{aligned}
> \det(A) ={}& aei + bfg + cdh\\
>            & - ceg - bdi - afh
> \end{aligned}
> $$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
>  1 &  0 &  4\\
> -1 &  2 & -1\\
>  0 &  3 &  1
> \end{pmatrix}
> $$
> 
> $$
> \begin{aligned}
> \det(A) = {}& 1 \cdot 2 \cdot 1 + 0 + 4 \cdot(-1) \cdot3\\
>            & - 4 \cdot 2 \cdot 0 - 0 - 1 \cdot(-1) \cdot3\\
>          = {}& 2 - 12 + 3\\
>          ={ }& -7
> \end{aligned}
> $$
> 
> El determinante es negativo, pero **no es cero**, por lo que $A$ sí tiene inversa.

> [!important] IMPORTANTE
> La **regla de Sarrus solo sirve para matrices $3 \times 3$**. Para matrices mayores podemos emplear cofactores, desarrollo de Laplace o eliminación por filas.

## MENORES Y COFACTORES

Para calcular determinantes de mayor tamaño, reducimos el problema a determinantes de matrices más pequeñas:

- **Submatriz $A_{ij}$:** se obtiene eliminando de $A$ la fila $i$ y la columna $j$.
- **Menor $m_{ij}$:** es el determinante de esa submatriz.
- **Cofactor $C_{ij}$:** es el menor con el signo que corresponde a su posición.

> [!syntax] SINTAXIS
> 
> $$
> \begin{aligned}
> m_{ij} &= \det(A_{ij})\\
> C_{ij} &= (-1)^{i+j}m_{ij}
> \end{aligned}
> $$
> 
> Los signos de los cofactores comienzan con $+$ arriba a la izquierda y alternan como un tablero:
> 
> $$
> \begin{pmatrix}
> + & - & +\\
> - & + & -\\
> + & - & +
> \end{pmatrix}
> $$

## DESARROLLO DE LAPLACE

El **desarrollo de Laplace** permite calcular el determinante utilizando **cualquier fila o columna**. Multiplicamos cada elemento de la fila elegida por su cofactor y sumamos los resultados.

> [!syntax] SINTAXIS
> 
> Desarrollo por la fila $i$:
> 
> $$
> \det(A) = \sum_{j=1}^{n} a_{ij} C_{ij}
> $$
> 
> Desarrollo por la columna $j$:
> 
> $$
> \det(A) = \sum_{i = 1}^{n} a_{ij} C_{ij}
> $$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 2 & 0 & 1\\
> 1 & 3 & 0\\
> 0 & 4 & 1
> \end{pmatrix}
> $$
> 
> Desarrollamos por la **primera fila**. Su segundo elemento es cero, por lo que no es necesario calcular su cofactor:
> 
> $$
> \begin{aligned}
> \det(A)
> &= 2\begin{vmatrix}
> 3 & 0\\
> 4 & 1
> \end{vmatrix}
>    + 0 + 1
> \begin{vmatrix}
> 1 & 3\\
> 0 & 4
> \end{vmatrix}\\
> &= 2(3 \cdot 1 - 0 \cdot 4)
>    + (1 \cdot 4 - 3 \cdot 0)\\
> &= 6 + 4 = 10
> \end{aligned}
> $$
> 
> Conviene elegir una fila o columna con **muchos ceros** para hacer menos cálculos.

## PROPIEDADES DE LOS DETERMINANTES

Estas propiedades son útiles para simplificar operaciones y comprobar resultados:

- **Matriz triangular o diagonal:** su determinante es el producto de los elementos de la diagonal principal.
- **Dos filas o columnas iguales:** determinante cero.
- **Una fila o columna nula:** determinante cero.
- **Intercambiar dos filas:** cambia el signo del determinante.
- **Multiplicar una fila por $k$:** multiplica el determinante por $k$.
- **Sumar a una fila un múltiplo de otra:** no cambia el determinante.
- **Producto:** $\det(AB) = \det(A) \det(B)$.
- **Transpuesta:** $\det(A^T) = \det(A)$.
- **Identidad:** $\det(I_n) = 1$.

> [!example] EJEMPLO
> Si $T$ es triangular:
> 
> $$
> T = \begin{pmatrix}
> 2 &  4 &  1\\
> 0 & -3 &  5\\
> 0 &  0 &  2
> \end{pmatrix}
> \quad \Longrightarrow \quad
> \det(T) = 2 \cdot(-3) \cdot 2 = -12
> $$

## NOTA PARA PROGRAMADORES: NUMPY

> [!note] NOTA (para programadores)
> NumPy proporciona `np.linalg.det` para calcular determinantes. El resultado puede contener pequeños errores de **coma flotante**, por lo que no siempre conviene comparar directamente con cero usando `==`.
> 
> ```python
> import numpy as np
>
> A = np.array(
>     [[1, -1],
>      [2,  3]],
>     dtype=float
> )
> 
> det_A = np.linalg.det(A)
>
> print(det_A)                # Aproximadamente 5.0
> print(np.isclose(det_A, 5)) # True
> ```
> 
> Para estudiar un sistema numérico real también importa la **precisión** de los datos: un determinante muy próximo a cero puede señalar una matriz difícil de invertir de manera fiable.

## RESUMEN

| ORDEN        | MÉTODO                           |
|:------------ |:-------------------------------- |
| $1\times1$   | Único elemento.                  |
| $2\times2$   | $ad - bc$.                       |
| $3\times3$   | Sarrus o Laplace.                |
| Mayor tamaño | Laplace o eliminación por filas. |

> [!warning] ERRORES FRECUENTES
> - Calcular determinantes de matrices no cuadradas.
> - Aplicar Sarrus a una matriz que no sea $3 \times 3$.
> - Olvidar el signo $(-1)^{i + j}$ de los cofactores.
> - Interpretar $\det(A) < 0$ como "no invertible": **solo $\det(A) = 0$ impide la inversa**.
