---
aliases: [Determinantes de matrices]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-10 04:59:00
rating: 
tags: [Math]
---

# DETERMINANTES

> [!seealso]- MIRA TAMBIÉN
> - [Matrices](matrix.md)
> - [Operaciones con matrices](matrix_operations.md)
> - [Matrices inversas](matrix_inverse.md)

El **determinante** es un número asociado a una **matriz cuadrada**. Se escribe $\det(A)$ o $|A|$.

- Si $\det(A) = 0$, la matriz **no es invertible**.
- Si $\det(A) \ne 0$, la matriz **sí es invertible**.

## DETERMINANTE DE ORDEN 1

> [!syntax] SINTAXIS
> 
> $$A = (a) \quad \Rightarrow \quad \det(A) = a$$

## DETERMINANTE DE ORDEN 2

> [!syntax] SINTAXIS
> 
> $$
> A = \begin{pmatrix}
> a& b\\
> c& d
> \end{pmatrix}
> \quad \Rightarrow \quad \det(A) = ad - bc
> $$

> [!example] EJEMPLO
> 
> $$
> \det \begin{pmatrix}
> 1& -1\\
> 2& 3
> \end{pmatrix}
> = 1 \cdot 3 - (-1) \cdot 2
> = 5
> $$

## DETERMINANTE DE ORDEN 3 (SARRUS)

Para $A = \begin{pmatrix} a& b& c\\ d& e& f\\ g& h& i\end{pmatrix}$:

> [!syntax] SINTAXIS
> 
> $$\det(A) = aei + bfg + cdh - ceg - bdi - afh$$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
>  1&  0&  4\\
> -1&  2& -1\\
>  0&  3&  1
> \end{pmatrix}
> $$
> 
> $$\det(A) = 2 - 12 + 3 = -7$$

> [!important] IMPORTANTE
> La **regla de Sarrus** se aplica a matrices $3 \times 3$, **no** a matrices de orden superior.

## MENORES, COFACTORES Y LAPLACE

- **Menor $M_{ij}$:** matriz obtenida al eliminar la fila $i$ y la columna $j$.
- **Cofactor $C_{ij}$:** determinante del menor con signo alternante.
- **Desarrollo de Laplace:** permite calcular el determinante por cualquier fila o columna.

> [!syntax] SINTAXIS
> 
> $$C_{ij} = (-1)^{i + j} \det(M_{ij})$$
> 
> $$\det(A) = \sum_{j = 1}^{n}a_{ij}C_{ij} \quad \text{(desarrollo por la fila }i\text{)}$$

- Es práctico elegir una fila o columna que contenga **muchos ceros**.

## PROPIEDADES IMPORTANTES

- **Dos filas iguales:** $\det(A) = 0$.
- **Intercambiar dos filas:** cambia el signo del determinante.
- **Multiplicar una fila por $k$:** multiplica el determinante por $k$.
- **Sumar a una fila un múltiplo de otra:** el determinante no cambia.
- **Producto:** $\det(AB) = \det(A) \det(B)$.
- **Transpuesta:** $\det(A^T) = \det(A)$.
- **Identidad:** $\det(I_n) = 1$.

## RESUMEN

| MATRIZ      | CÁLCULO                          |
|:----------- |:-------------------------------- |
| $1\times1$  | Único elemento.                  |
| $2\times2$  | $ad - bc$.                       |
| $3\times3$  | Sarrus o Laplace.                |
| Orden mayor | Laplace o eliminación por filas. |

> [!warning] ERRORES FRECUENTES
> - Calcular determinantes de matrices no cuadradas.
> - Olvidar el signo $(-1)^{i + j}$ de los cofactores.
> - Confundir $\det(A) = 0$ con que $A$ sea invertible: significa **lo contrario**.
