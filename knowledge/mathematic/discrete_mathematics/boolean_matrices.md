---
aliases: [Matrices cero-uno]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-10 04:47:20
rating: 
tags: [Math]
---

# MATRICES BOOLEANAS

> [!seealso]- MIRA TAMBIÉN
> - [Matrices](../linear_algebra/matrix.md)
> - [Operaciones con matrices](../linear_algebra/matrix_operations.md)
> - [Conectores lógicos](logic/logical_connectives.md)
> - [Relaciones binarias](binary_relations.md)
> - [Teoría de conjuntos](set_theory.md)

Una **matriz booleana** (o **matriz cero-uno**) contiene solamente los valores $0$ y $1$.

- $0$: falso.
- $1$: verdadero.
- Se utiliza para representar relaciones y estructuras discretas.

## UNIÓN (JOIN)

Se aplica **OR** ($\lor$) a los elementos de la misma posición de dos matrices de igual orden.

> [!syntax] SINTAXIS
> 
> $$(A \lor B)_{ij} = a_{ij} \lor b_{ij}$$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 1& 0& 1\\
> 0& 1& 0
> \end{pmatrix},
> \quad B = \begin{pmatrix}
> 0& 1& 0\\
> 1& 1& 0
> \end{pmatrix}
> $$
> 
> $$
> A \lor B = \begin{pmatrix}
> 1& 1& 1\\
> 1& 1& 0
> \end{pmatrix}
> $$

## INTERSECCIÓN (MEET)

Se aplica **AND** ($\land$) a los elementos correspondientes de dos matrices de igual orden.

> [!syntax] SINTAXIS
> 
> $$(A \land B)_{ij} = a_{ij} \land b_{ij}$$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 1& 0& 1\\
> 0& 1& 0
> \end{pmatrix},
> \quad B = \begin{pmatrix}
> 0& 1& 0\\
> 1& 1& 0
> \end{pmatrix}
> $$
> 
> $$
> A \land B = \begin{pmatrix}
> 0& 0& 0\\
> 0& 1& 0
> \end{pmatrix}
> $$

## PRODUCTO BOOLEANO

Se parece al producto de matrices habitual, pero sustituye:

- Multiplicación numérica ($\cdot$) por **AND** ($\land$).
- Suma numérica ($+$) por **OR** ($\lor$).

> [!syntax] SINTAXIS
> 
> Si $A$ tiene orden $m \times p$ y $B$ tiene orden $p \times n$:
> 
> $$C = A \odot B,\qquad c_{ij} = \bigvee_{k = 1}^{p}(a_{ik} \land b_{kj})$$
> 
> - $\odot$: producto booleano.
> - $\bigvee$: OR de todos los términos.

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 1& 0\\
> 0& 1\\
> 1& 0
> \end{pmatrix},
> \quad B = \begin{pmatrix}
> 1& 1& 0\\
> 0& 1&1
> \end{pmatrix}
> $$
> 
> $$
> A \odot B = \begin{pmatrix}
> 1& 1& 0\\
> 0& 1& 1\\
> 1& 1& 0
> \end{pmatrix}
> $$
> 
> Por ejemplo, $c_{12} = (1 \land 1) \lor (0 \land 1) = 1$.

## POTENCIA BOOLEANA

Para una matriz booleana **cuadrada** $A$:

- $A^{\odot0} = I_n$.
- $A^{\odot1} = A$.
- $A^{\odot2} = A \odot A$.
- $A^{\odot k}$ aplica el producto booleano $k$ veces.

> [!important] IMPORTANTE
> **No confundir** la potencia booleana con la potencia usual: $A^{\odot2}$ siempre contiene ceros y unos, mientras que $A^2$ (producto numérico) puede contener valores mayores que $1$.

## RELACIONES Y CAMINOS

- Una matriz booleana puede indicar si existe una relación entre dos elementos.
- En una matriz de adyacencia, $(A^{\odot k})_{ij} = 1$ indica que existe un **camino de longitud $k$** del elemento $i$ al $j$.
- Consulta [Relaciones binarias](binary_relations.md) para cierres de relaciones.

## RESUMEN

|   OPERACIÓN   | NOMBRE              | REGLA                       |
|:-------------:|:------------------- |:--------------------------- |
|  $A \lor B$   | Join / unión        | OR elemento a elemento.     |
|  $A \land B$  | Meet / intersección | AND elemento a elemento.    |
|  $A \odot B$  | Producto booleano   | Fila-columna con AND y OR.  |
| $A^{\odot k}$ | Potencia booleana   | Producto booleano repetido. |

> [!warning] ERRORES FRECUENTES
> - Sumar bits numéricamente en lugar de aplicar $\lor$.
> - Confundir **join** con **meet**.
> - Confundir el producto booleano con el producto habitual.
