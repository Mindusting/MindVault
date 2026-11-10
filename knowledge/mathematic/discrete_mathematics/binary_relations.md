---
aliases: [Relaciones binarias]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-10 04:36:13
rating: 
tags: [Math]
---

# RELACIONES BINARIAS

> [!seealso]- MIRA TAMBIÉN
> - [Teoría de conjuntos](set_theory.md)
> - [Matrices booleanas](boolean_matrices.md)
> - [Matrices](../linear_algebra/matrix.md)

Una **relación binaria** entre conjuntos $A$ y $B$ es un subconjunto del **producto cartesiano** $A \times B$.

> [!syntax] SINTAXIS
> 
> $$R \subseteq A \times B$$
> 
> Si $(a, b) \in R$, escribimos también $aRb$.

## MATRIZ DE UNA RELACIÓN

Para un conjunto finito $A=\{a_1, \dots, a_n\}$, una relación $R \subseteq A \times A$ se representa mediante una matriz cero-uno:

- $m_{ij} = 1$ si $(a_i, a_j) \in R$.
- $m_{ij} = 0$ en caso contrario.

> [!example] EJEMPLO
> 
> Si $A = \{1, 2, 3\}$ y $R = \{(1, 2), (2, 3)\}$:
> 
> $$
> M_R = \begin{pmatrix}
> 0& 1& 0\\
> 0& 0& 1\\
> 0& 0& 0
> \end{pmatrix}
> $$

## PROPIEDADES BÁSICAS

Para una relación sobre un mismo conjunto:

- **Reflexiva:** $aRa$ para todo $a$; la diagonal de $M_R$ contiene unos.
- **Simétrica:** $aRb \Rightarrow bRa$; $M_R = M_R^T$.
- **Transitiva:** $aRb \land bRc \Rightarrow aRc$.

## CIERRE TRANSITIVO

El **cierre transitivo** de $R$ es la relación transitiva **más pequeña que contiene a $R$**.

> [!example] EJEMPLO
> 
> Si $R = \{(1, 2), (2, 3)\}$, debe añadirse $(1, 3)$ para que sea transitiva:
> 
> $$R^+ = \{(1, 2), (2, 3), (1, 3)\}$$
> 
> $$
> M_{R^+} = \begin{pmatrix}
> 0& 1& 1\\
> 0& 0& 1\\
> 0& 0& 0
> \end{pmatrix}
> $$

- La **potencia booleana** $M_R^{\odot k}$ detecta conexiones de longitud $k$.
- Para $n = |A|$, el cierre transitivo puede calcularse con la unión booleana:

> [!syntax] SINTAXIS
> 
> $$M_{R^+} = M_R \lor M_R^{\odot2} \lor \cdots \lor M_R^{\odot n}$$

> [!note] NOTA
> El **cierre reflexivo-transitivo** incluye además los pares $(a, a)$, por lo que incorpora $I_n$ a la expresión anterior.

## RESUMEN

| CONCEPTO              | IDEA ESENCIAL                                         |
|:--------------------- |:----------------------------------------------------- |
| Relación binaria      | Conjunto de pares ordenados.                          |
| Matriz de la relación | $1$ si hay relación, $0$ si no.                       |
| Transitividad         | Si $aRb$ y $bRc$, entonces $aRc$.                     |
| Cierre transitivo     | Añade los pares necesarios para lograr transitividad. |

> [!warning] ERRORES FRECUENTES
> - Confundir el producto cartesiano $A \times B$ con un producto de matrices.
> - Confundir cierre **transitivo** con cierre **reflexivo-transitivo**.
