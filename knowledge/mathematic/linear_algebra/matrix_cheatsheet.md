---
aliases: [Matrices en matemáticas (Chuleta)]
author: Mindusting
corrected: false
creationDate: 2026-11-10 12:00:00
headerFile: false
modificationDate: 2026-11-10 06:28:24
rating:
tags: [CheatSheet, Math]
---

# CHULETA DE MATRICES

> [!seealso]- MIRA TAMBIÉN
> - [Matrices](matrix.md)
> - [Operaciones con matrices](matrix_operations.md)
> - [Determinantes](matrix_determinants.md)
> - [Matriz inversa](matrix_inverse.md)
> - [Matrices booleanas](../discrete_mathematics/boolean_matrices.md)
> - [Relaciones binarias](../discrete_mathematics/binary_relations.md)

> [!note] NOTA
> Este archivo es la **chuleta de todos los apuntes de matrices**. Las explicaciones, demostraciones y ejemplos desarrollados están en los documentos enlazados.

## [MATRICES](matrix.md)

Una **matriz** es una tabla rectangular de elementos organizada en filas y columnas.

- **Orden $m \times n$:** $m$ filas, $n$ columnas.
- **$a_{ij}$:** elemento de la fila $i$ y columna $j$.
- **Igualdad:** mismo orden y mismos elementos en cada posición.
- **Submatriz:** selección de filas y columnas conservando el orden.

$$
A = \begin{pmatrix}
3 & 4 &  1\\
0 & 2 & -1
\end{pmatrix}
\quad \Longrightarrow \quad
A \text{ es }2 \times3,\ a_{12}=4
$$

### [TIPOS DE MATRICES](matrix.md#TIPOS%20DE%20MATRICES)

- **Fila / columna:** $1 \times n$ / $m \times1$.
- **Cuadrada:** $n \times n$.
- **Nula:** todos los elementos son $0$.
- **Diagonal:** ceros fuera de la diagonal principal.
- **Identidad $I_n$:** diagonal con unos; neutro del producto.
- **Triangular superior / inferior:** ceros debajo / encima de la diagonal.
- **Simétrica:** $A^T=A$.

## [OPERACIONES CON MATRICES](matrix_operations.md)

| OPERACIÓN          | CONDICIÓN                   | REGLA                                 |
|:------------------ |:--------------------------- |:------------------------------------- |
| Suma / resta       | Mismo orden.                | $(A \pm B)_{ij} = a_{ij} \pm b_{ij}$. |
| Producto escalar   | Escalar $k$.                | $(kA)_{ij} = ka_{ij}$.                |
| Producto matricial | $(m \times p)(p \times n)$. | Resultado $m \times n$.               |
| Transpuesta        | Cualquier matriz.           | $(A^T)_{ij} = a_{ji}$.                |
| Potencia $A^k$     | $A$ cuadrada, $k \ge0$.     | Producto matricial repetido.          |

### [PRODUCTO MATRICIAL](matrix_operations.md#PRODUCTO%20DE%20DOS%20MATRICES)

$$
\underbrace{A_{m \times p}}_{\text{primera matriz}}
\underbrace{B_{p \times n}}_{\text{segunda matriz}}
= C_{m \times n}
$$

$$
c_{ij} = \sum_{k = 1}^{p}a_{ik}b_{kj}
$$

- **Fila de $A$ por columna de $B$**; se suman los productos.
- **No es conmutativo:** normalmente $AB \ne BA$.
- **Propiedades:** $A(BC) = (AB)C$ y $A(B + C) = AB + AC$.
- **Identidad:** $I_mA = A = AI_n$ para $A$ de orden $m \times n$.

### [TRANSPUESTA](matrix_operations.md#MATRIZ%20TRANSPUESTA)

- Cambia filas por columnas: $m \times n \to n \times m$.
- $(A^T)^T = A$.
- $(AB)^T = B^TA^T$.

### [POTENCIAS Y FILAS](matrix_operations.md#POTENCIA%20DE%20UNA%20MATRIZ)

- $A^0 = I_n$; $A^2 = AA$ (solo matrices cuadradas).
- **Operaciones elementales:** intercambiar filas, multiplicar una fila por escalar no nulo o sumar a una fila un múltiplo de otra.

## [DETERMINANTES](matrix_determinants.md)

El determinante es un número definido para **matrices cuadradas**.

- **Invertible:** $\det(A) \ne 0$.
- **No invertible:** $\det(A) = 0$.

### ORDEN 2

$$
\det \begin{pmatrix}
a & b\\
c & d
\end{pmatrix}
= ad - bc
$$

### ORDEN 3: SARRUS

$$
\det\begin{pmatrix}
a & b & c\\
d & e & f\\
g & h & i
\end{pmatrix}
= aei + bfg + cdh - ceg - bdi - afh
$$

### [COFACTORES Y LAPLACE](matrix_determinants.md#MENORES%20Y%20COFACTORES)

$$
\begin{aligned}
m_{ij} &= \det(A_{ij})\\
C_{ij} &= (-1)^{i + j}m_{ij}\\
\det(A) &= \sum_{j = 1}^{n}a_{ij}C_{ij}
\end{aligned}
$$

- Intercambiar dos filas cambia el signo.
- Sumar a una fila un múltiplo de otra **no** cambia el determinante.
- En matrices triangulares: producto de la diagonal.
- $\det(AB) = \det(A) \det(B)$; $\det(A^T) = \det(A)$.

## [MATRIZ INVERSA](matrix_inverse.md)

$$
AA^{-1} = A^{-1}A = I_n
$$

Existe solo si $A$ es cuadrada y $\det(A)\ne0$.

### INVERSA DE ORDEN 2

$$
\begin{pmatrix}
a & b\\
c & d
\end{pmatrix}^{-1}
= \frac{1}{ad-bc}
\begin{pmatrix}
 d & -b\\
-c & a
\end{pmatrix}
$$

### MÉTODOS GENERALES

- **Gauss-Jordan:** $[A \mid I_n] \to [I_n \mid A^{-1}]$.
- **Adjunta:** $A^{-1} = \operatorname{adj}(A) / \det(A)$.
- **Producto:** $(AB)^{-1} = B^{-1}A^{-1}$ (**orden inverso**).

## [MATRICES BOOLEANAS](../discrete_mathematics/boolean_matrices.md)

Contienen únicamente $0$ y $1$, que representan **falso** y **verdadero**.

| OPERACIÓN                  | REGLA                                |
|:-------------------------- |:------------------------------------ |
| **Join $A \lor B$**        | OR elemento a elemento.              |
| **Meet $A \land B$**       | AND elemento a elemento.             |
| **Producto $A \odot B$**   | AND entre parejas; OR de resultados. |
| **Potencia $A^{\odot k}$** | Producto booleano repetido.          |

$$
(A \odot B)_{ij}
= \bigvee_{k=1}^{p}(a_{ik} \land b_{kj})
$$

- El producto booleano exige **dimensiones compatibles**, igual que el matricial.
- $A^{\odot k}$ detecta recorridos de longitud **exactamente $k$**.
- No confundir el producto booleano con el numérico.

## [RELACIONES BINARIAS](../discrete_mathematics/binary_relations.md)

- **Relación:** $R \subseteq A \times B$.
- **Matriz de relación:** $m_{ij} = 1$ si $(a_i, a_j) \in R$.
- **Reflexiva:** diagonal con unos.
- **Simétrica:** $M_R = M_R^T$.
- **Transitiva:** $aRb \land bRc \Rightarrow aRc$.
- **Cierre transitivo:** añade pares necesarios para asegurar transitividad.

$$
M_{R^+} = M_R \lor M_R^{\odot2} \lor \cdots \lor M_R^{\odot n}
$$

$$
M_{R^*} = I_n\lor M_{R^+}
$$

## NOTA PARA PROGRAMADORES: NUMPY

> [!note] NOTA (para programadores)
> En NumPy, las equivalencias más útiles son:
> 
> - $A + B$, $kA$: `A + B`, `k * A`
> - $AB$: `A @ B`
> - $A^T$: `A.T`
> - $A^k$: `np.linalg.matrix_power(A, k)`
> - $\det(A)$: `np.linalg.det(A)`
> - $A^{-1}$: `np.linalg.inv(A)`
> - Join / meet: `A | B` / `A & B` con `dtype=bool`
> 
> **Atención:** `A * B` multiplica **elemento a elemento** y `A ** 2` eleva cada componente al cuadrado. No sustituyen a `@` ni a `matrix_power`.

> [!warning] ERRORES FRECUENTES
> - Confundir filas con columnas al leer $a_{ij}$.
> - Sumar matrices de distinto orden.
> - Suponer que el producto matricial conmuta.
> - Usar Sarrus fuera de matrices $3 \times 3$.
> - Confundir determinante cero con invertibilidad.
> - Confundir potencias numéricas y booleanas.
