---
aliases: [Inversa de matrices]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-10 07:06:21
rating: 
tags: [Math]
---

# MATRIZ INVERSA

> [!external-link]- REFERENCIAS WEB
> - [NumPy: `numpy.linalg.inv`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html)
> - [NumPy: `numpy.linalg.solve`](https://numpy.org/doc/stable/reference/generated/numpy.linalg.solve.html)

> [!seealso]- MIRA TAMBIÉN
> - [Matrices](matrix.md)
> - [Operaciones con matrices](matrix_operations.md)
> - [Determinantes](matrix_determinants.md)
> - [Chuleta de matrices](matrix_cheatsheet.md)

La **matriz inversa** de una matriz cuadrada $A$ es otra matriz, escrita $A^{-1}$, que al multiplicarse por $A$ produce la **matriz identidad**. Es la operación que permite deshacer el efecto de una transformación matricial invertible.

No todas las matrices tienen inversa: deben ser **cuadradas** y su [determinante](matrix_determinants.md) debe ser distinto de cero.

> [!syntax] SINTAXIS
> 
> $$
> AA^{-1} = A^{-1}A = I_n
> $$
> 
> - $A$: matriz cuadrada de orden $n$.
> - $A^{-1}$: su inversa, si existe.
> - $I_n$: matriz identidad del mismo orden.

Cuando la inversa existe, es **única**. Una matriz con inversa se llama **invertible** o **regular**; una que no tiene inversa es **singular**.

## ¿CUÁNDO EXISTE LA INVERSA?

> [!syntax] CONDICIÓN
> 
> $$
> A^{-1}\text{ existe}
> \iff
> \det(A) \ne 0
> $$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 1 & 2\\
> 2 & 4
> \end{pmatrix}
> \quad \Longrightarrow \quad
> \det(A) = 1 \cdot 4 - 2 \cdot 2 = 0
> $$
> 
> Por tanto, $A$ **no tiene inversa**. Su segunda fila es el doble de la primera: no aportan información independiente.

## INVERSA DE UNA MATRIZ DE ORDEN 2

Para una matriz $2 \times 2$ existe una fórmula directa: intercambiamos los elementos de la diagonal principal, cambiamos el signo de los de la otra diagonal y dividimos por el determinante.

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
> A^{-1} = \frac{1}{ad-bc}
> \begin{pmatrix}
>  d & -b\\
> -c &  a
> \end{pmatrix}
> \qquad (ad-bc\ne0)
> $$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 1 & 1\\
> 1 & 2
> \end{pmatrix}
> \qquad
> \det(A) = 1 \cdot 2 - 1 \cdot 1 = 1
> $$
> 
> $$
> A^{-1} = \frac{1}{1}
> \begin{pmatrix}
>  2 & -1\\
> -1 &  1
> \end{pmatrix}
> = \begin{pmatrix}
>  2 & -1\\
> -1 &  1
> \end{pmatrix}
> $$
> 
> Comprobamos el resultado multiplicando las dos matrices:
> 
> $$
> AA^{-1}
> = \begin{pmatrix}
> 1 & 1\\
> 1 & 2
> \end{pmatrix}
> \begin{pmatrix}
>  2 & -1\\
> -1 &  1
> \end{pmatrix}
> = \begin{pmatrix}
> 1 & 0 \\
> 0 & 1
> \end{pmatrix}
> = I_2
> $$

## MÉTODO DE GAUSS-JORDAN

Este método permite calcular la inversa mediante **operaciones elementales por filas**. Se escribe la matriz $A$ junto a la identidad $I_n$ y se transforma la parte izquierda en la identidad. Las operaciones deben aplicarse a **ambas partes**.

> [!syntax] SINTAXIS
> 
> $$
> \left[A \mid I_n \right]
> \longrightarrow
> \left[I_n \mid A^{-1} \right]
> $$

> [!example] EJEMPLO PASO A PASO
> 
> Partimos de la misma matriz de orden 2:
> 
> $$
> \left[\begin{array}{cc|cc}
> 1 & 1 & 1 & 0\\
> 1 & 2 & 0 & 1
> \end{array} \right]
> $$
> 
> **1.** Restamos la primera fila a la segunda: $F_2 \leftarrow F_2 - F_1$.
> 
> $$
> \left[\begin{array}{cc|cc}
> 1 &  1 &  1 &  0\\
> 0 &  1 & -1 &  1
> \end{array}\right]
> $$
> 
> **2.** Restamos la segunda fila a la primera: $F_1 \leftarrow F_1 - F_2$.
> 
> $$
> \left[\begin{array}{cc|cc}
> 1 &  0 &  2 & -1\\
> 0 &  1 & -1 &  1
> \end{array}\right]
> $$
> 
> La parte izquierda ya es $I_2$; la derecha es la **matriz inversa**:
> 
> $$
> A^{-1} = \begin{pmatrix}
>  2 & -1\\
> -1 &  1
> \end{pmatrix}
> $$

Si no podemos reducir la parte izquierda a $I_n$ mediante operaciones elementales, la matriz **no es invertible**.

## MÉTODO DE LA MATRIZ ADJUNTA

Este procedimiento utiliza los [cofactores](matrix_determinants.md#MENORES%20Y%20COFACTORES) y el determinante. Es útil para comprender la fórmula general de la inversa, aunque para matrices grandes suele ser más práctico trabajar por eliminación.

1. Calculamos la **matriz de cofactores** $C = (C_{ij})$.
2. La **transponemos** para obtener la matriz adjunta: $\operatorname{adj}(A) = C^T$.
3. Dividimos por el determinante, que debe ser distinto de cero.

> [!syntax] SINTAXIS
> 
> $$
> A^{-1} = \frac{\operatorname{adj}(A)}{\det(A)}
> \qquad (\det(A) \ne 0)
> $$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 2 & 1\\
> 3 & 2
> \end{pmatrix}
> \qquad
> \det(A) = 4 - 3 = 1
> $$
> 
> Su matriz de cofactores y su adjunta son:
> 
> $$
> C = \begin{pmatrix}
>  2 & -3\\
> -1 &  2
> \end{pmatrix}
> \qquad
> \operatorname{adj}(A) = C^T
> = \begin{pmatrix}
>  2 & -1\\
> -3 &  2
> \end{pmatrix}
> $$
> 
> Como $\det(A) = 1$, su inversa coincide con la adjunta en este ejemplo.

> [!important] IMPORTANTE
> La **matriz de cofactores** y la **matriz adjunta** no son lo mismo: la adjunta se obtiene **transponiendo** la matriz de cofactores.

## PROPIEDADES DE LA INVERSA

Si las matrices involucradas son invertibles y sus productos están definidos:

- **Inversa de un producto:** $(AB)^{-1} = B^{-1} A^{-1}$ (**se invierte el orden**).
- **Inversa de la transpuesta:** $(A^T)^{-1} = (A^{-1})^T$.
- **Inversa de la inversa:** $(A^{-1})^{-1} = A$.
- **Identidad:** $I_n^{-1} = I_n$.

## NOTA PARA PROGRAMADORES: NUMPY

> [!note] NOTA (para programadores)
> NumPy permite calcular una inversa con `np.linalg.inv`. Para comprobarla, multiplicamos con `@` y utilizamos `np.allclose`, ya que los resultados numéricos pueden incluir redondeos.
> 
> ```python
> import numpy as np
>
> A = np.array(
>     [[1, 1],
>      [1, 2]],
>     dtype=float
> )
> inversa = np.linalg.inv(A)
>
> print(inversa) # Aproximadamente [[2., -1.], [-1., 1.]]
> print(np.allclose(A @ inversa, np.eye(2))) # True
> ```
> 
> Si la matriz es singular, `np.linalg.inv` normalmente lanza `np.linalg.LinAlgError`. Una matriz **casi singular** puede producir resultados poco precisos incluso si la función no falla.
> 
> Para resolver un sistema $Ax = b$, suele ser preferible `np.linalg.solve(A, b)` a calcular explícitamente `np.linalg.inv(A) @ b`.

## RESUMEN

| MÉTODO               | EN QUÉ CONSISTE                                             |
|:-------------------- |:----------------------------------------------------------- |
| Fórmula $2 \times 2$ | Intercambiar, cambiar signos y dividir por el determinante. |
| Gauss-Jordan         | Transformar $[A \mid I_n]$ en $[I_n \mid A^{-1}]$.            |
| Adjunta              | Transponer cofactores y dividir por $\det(A)$.              |

> [!warning] ERRORES FRECUENTES
> - Intentar invertir matrices no cuadradas o con determinante cero.
> - Interpretar $A^{-1}$ como elevar cada elemento a $-1$.
> - Olvidar realizar las mismas operaciones en ambos lados de $[A \mid I_n]$.
> - Olvidar transponer la matriz de cofactores.
> - Escribir $(AB)^{-1} = A^{-1} B^{-1}$: **el orden correcto está invertido**.
