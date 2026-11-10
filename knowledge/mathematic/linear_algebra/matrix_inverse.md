---
aliases: [Inversa de matrices]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-10 05:13:46
rating: 
tags: [Math]
---

# MATRIZ INVERSA

> [!seealso]- MIRA TAMBIÉN
> - [Matrices](matrix.md)
> - [Operaciones con matrices](matrix_operations.md)
> - [Determinantes](matrix_determinants.md)

La **matriz inversa** de una matriz cuadrada $A$ es la matriz $A^{-1}$ que cumple:

> [!syntax] SINTAXIS
> 
> $$AA^{-1} = A^{-1}A = I_n$$

- Existe **solo si** $\det(A) \ne 0$.
- Cuando existe, es **única**.

## INVERSA DE UNA MATRIZ DE ORDEN 2

> [!syntax] SINTAXIS
> 
> $$
> A = \begin{pmatrix}
> a& b\\
> c& d
> \end{pmatrix},
> \quad ad - bc \ne 0
> $$
> 
> $$
> A^{-1} = \frac{1}{ad - bc} \begin{pmatrix}
>  d& -b\\
> -c&  a
> \end{pmatrix}
> $$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 1& 1\\
> 1& 2
> \end{pmatrix},
> \quad \det(A) = 1
> $$
> 
> $$
> A^{-1} = \begin{pmatrix}
>  2& -1\\
> -1&  1
> \end{pmatrix}
> $$
> 
> Comprobación: $AA^{-1} = \begin{pmatrix} 1& 0\\ 0& 1\end{pmatrix} = I_2$.

## MÉTODO DE GAUSS-JORDAN

Permite encontrar la inversa utilizando [operaciones elementales por filas](matrix_operations.md#OPERACIONES%20ELEMENTALES%20POR%20FILAS).

1. Escribir la matriz ampliada $[A \mid I_n]$.
2. Hacer operaciones elementales hasta transformar $A$ en $I_n$.
3. El lado derecho se convierte en $A^{-1}$:

> [!syntax] SINTAXIS
> 
> $$[A \mid I_n] \longrightarrow [I_n \mid A^{-1}]$$

- Si no se puede convertir el bloque izquierdo en $I_n$, la matriz **no es invertible**.

## MÉTODO DE LA MATRIZ ADJUNTA

- Construir la matriz $C = (C_{ij})$ de **cofactores**.
- Transponerla: $\operatorname{adj}(A)=C^T$ (matriz adjunta o *adjugate*).
- Dividir por el determinante:

> [!syntax] SINTAXIS
> 
> $$
> A^{-1} = \frac{
> \operatorname{adj}(A)
> }{
> \det(A)
> }, \quad \det(A) \ne 0
> $$

> [!note] NOTA
> Aquí, **matriz adjunta** se refiere a la *transpuesta de la matriz de cofactores*. No es la misma cosa que un cofactor individual.

## PROPIEDADES

- $(AB)^{-1} = B^{-1} A^{-1}$ (**se invierte el orden**).
- $(A^T)^{-1} = (A^{-1})^T$.
- $(A^{-1})^{-1} = A$.

## RESUMEN

| MÉTODO               | CUÁNDO UTILIZARLO                           |
|:-------------------- |:------------------------------------------- |
| Fórmula $2 \times 2$ | Inversa de matrices de orden 2.             |
| Gauss-Jordan         | Inversa mediante operaciones por filas.     |
| Adjunta / cofactores | Inversa mediante determinante y cofactores. |

> [!warning] ERRORES FRECUENTES
> - Intentar invertir una matriz con determinante cero.
> - Confundir $A^{-1}$ con elevar cada elemento a $-1$.
> - Olvidar el orden inverso en $(AB)^{-1}$.
