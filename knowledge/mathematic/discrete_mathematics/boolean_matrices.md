---
aliases: [Matrices cero-uno]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-10 06:46:02
rating: 
tags: [Math]
---

# MATRICES BOOLEANAS

> [!external-link]- REFERENCIAS WEB
> - [NumPy: operadores lógicos (`logical_and`)](https://numpy.org/doc/stable/reference/generated/numpy.logical_and.html)
> - [NumPy: multiplicación matricial (`matmul`)](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html)

> [!seealso]- MIRA TAMBIÉN
> - [Matrices](../linear_algebra/matrix.md)
> - [Operaciones con matrices](../linear_algebra/matrix_operations.md)
> - [Chuleta de matrices](../linear_algebra/matrix_cheatsheet.md)
> - [Conectores lógicos](logic/logical_connectives.md)
> - [Relaciones binarias](binary_relations.md)
> - [Teoría de conjuntos](set_theory.md)

Una **matriz booleana**, también llamada **matriz cero-uno**, es una matriz cuyos elementos solo pueden valer **$0$** o **$1$**. Se utiliza para representar condiciones y relaciones entre elementos, como la existencia de una conexión entre dos vértices de un grafo.

Sus elementos se interpretan como valores lógicos:

- **$0$:** falso; la relación o condición no se cumple.
- **$1$:** verdadero; la relación o condición se cumple.

En estas matrices podemos aplicar operaciones de la [lógica proposicional](logic/logical_connectives.md), no solamente operaciones aritméticas. Es importante **distinguir el producto booleano del producto matricial numérico**.

## UNIÓN (JOIN)

La **unión**, también llamada **join**, se calcula aplicando el operador lógico **OR ($\lor$)** a los elementos de la misma posición de dos matrices booleanas del **mismo orden**.

El resultado vale $1$ cuando **al menos una** de las entradas correspondientes vale $1$.

> [!syntax] SINTAXIS
> 
> $$
> (A \lor B)_{ij} = a_{ij} \lor b_{ij}
> $$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 1 & 0 & 1\\
> 0 & 1 & 0
> \end{pmatrix}
> \qquad
> B = \begin{pmatrix}
> 0 & 1 & 0\\
> 1 & 1 & 0
> \end{pmatrix}
> $$
> 
> $$
> A\lor B = \begin{pmatrix}
> 1\lor0 & 0\lor1 & 1\lor0\\
> 0\lor1 & 1\lor1 & 0\lor0
> \end{pmatrix}
> = \begin{pmatrix}
> 1 & 1 & 1\\
> 1 & 1 & 0
> \end{pmatrix}
> $$

## INTERSECCIÓN (MEET)

La **intersección**, también llamada **meet**, aplica **AND ($\land$)** a los elementos correspondientes. El resultado vale $1$ **solamente cuando ambas entradas valen $1$**.

> [!syntax] SINTAXIS
> 
> $$
> (A \land B)_{ij} = a_{ij} \land b_{ij}
> $$

> [!example] EJEMPLO
> 
> Para las mismas matrices $A$ y $B$:
> 
> $$
> A \land B = \begin{pmatrix}
> 1 \land 0 & 0 \land 1 & 1 \land 0\\
> 0 \land 1 & 1 \land 1 & 0 \land 0
> \end{pmatrix}
> = \begin{pmatrix}
> 0 & 0 & 0\\
> 0 & 1 & 0
> \end{pmatrix}
> $$

> [!note] NOTA (para programadores)
> En NumPy resulta cómodo utilizar arrays con `dtype=bool`. Los operadores `|` y `&` representan OR y AND **elemento a elemento**, respectivamente.
> 
> ```python
> import numpy as np
>
> A = np.array(
>     [[1, 0, 1],
>      [0, 1, 0]],
>     dtype=bool
> )
> B = np.array(
>     [[0, 1, 0],
>      [1, 1, 0]],
>     dtype=bool
> )
>
> print((A | B).astype(int))
> # SALIDA:
> # [[1 1 1]
> #  [1 1 0]]
> 
> print((A & B).astype(int))
> # SALIDA:
> # [[0 0 0]
> #  [0 1 0]]
> ```
> 
> `astype(int)` se usa aquí **solo para mostrar** los valores como ceros y unos en lugar de `False` y `True`.

## PRODUCTO BOOLEANO

El **producto booleano** combina **filas de la primera matriz** con **columnas de la segunda**, igual que el producto matricial habitual, pero sustituye las operaciones:

- Producto numérico ($\cdot$) por **AND ($\land$)**.
- Suma numérica ($+$) por **OR ($\lor$)**.

Las dimensiones deben cumplir la misma regla que en el producto matricial: para $A$ de orden $m \times p$ y $B$ de orden $p \times n$, el resultado tiene orden $m \times n$.

> [!syntax] SINTAXIS
> 
> Representamos el producto booleano mediante $\odot$:
> 
> $$
> C = A \odot B
> $$
> 
> $$
> c_{ij} = \bigvee_{k = 1}^{p}
> \left(a_{ik} \land b_{kj} \right)
> $$
> 
> $\bigvee$ significa aplicar OR a todos los términos obtenidos al recorrer la fila y la columna.

> [!example] EJEMPLO PASO A PASO
> 
> $$
> A = \begin{pmatrix}
> 1 & 0\\
> 0 & 1\\
> 1 & 0
> \end{pmatrix}
> \qquad
> B = \begin{pmatrix}
> 1 & 1 & 0\\
> 0 & 1 & 1
> \end{pmatrix}
> $$
> 
> Las dimensiones son $(3 \times 2)(2 \times 3)$, por lo que el resultado será $3 \times 3$.
> 
> Para calcular el elemento de la primera fila y segunda columna:
> 
> $$
> \begin{aligned}
> c_{12} &= (1 \land 1) \lor (0 \land 1)\\
>        &= 1 \lor 0 = 1
> \end{aligned}
> $$
> 
> Aplicando el mismo procedimiento a todas las posiciones:
> 
> $$
> A \odot B = \begin{pmatrix}
> 1 & 1 & 0\\
> 0 & 1 & 1\\
> 1 & 1 & 0
> \end{pmatrix}
> $$

> [!note] NOTA (para programadores)
> Para matrices de ceros y unos, podemos calcular primero un **producto matricial de enteros** y comprobar si cada resultado es mayor que cero. De esa manera, un número positivo de coincidencias equivale a `True`.
> 
> ```python
> import numpy as np
> 
> A = np.array(
>     [[1, 0],
>      [0, 1],
>      [1, 0]],
>     dtype=bool
> )
> B = np.array(
>     [[1, 1, 0],
>      [0, 1, 1]],
>     dtype=bool
> )
>
> C = (A.astype(int) @ B.astype(int)) > 0
> 
> print(C.astype(int))
> # SALIDA:
> # [[1 1 0]
> #  [0 1 1]
> #  [1 1 0]]
> ```
> 
> Esta técnica resulta sencilla para aprender y para matrices pequeñas. No confundas el `@` numérico intermedio con la **definición** del producto booleano: este último combina AND y OR.

## POTENCIA BOOLEANA

Si $A$ es una matriz booleana **cuadrada**, podemos multiplicarla booleanamente por sí misma varias veces.

> [!syntax] SINTAXIS
> 
> $$
> \begin{aligned}
> A^{\odot 0} &= I_n\\
> A^{\odot 1} &= A\\
> A^{\odot 2} &= A \odot A\\
> A^{\odot 3} &= A \odot A \odot A
> \end{aligned}
> $$

> [!example] EJEMPLO
> 
> $$
> A = \begin{pmatrix}
> 0 & 1 & 0\\
> 0 & 0 & 1\\
> 0 & 0 & 0
> \end{pmatrix}
> \qquad
> A^{\odot2} = \begin{pmatrix}
> 0 & 0 & 1\\
> 0 & 0 & 0\\
> 0 & 0 & 0
> \end{pmatrix}
> $$
> 
> En $A$ hay una conexión directa del elemento $1$ al $2$, y otra del $2$ al $3$. En $A^{\odot2}$ aparece una conexión del $1$ al $3$ **en dos pasos**.

> [!important] IMPORTANTE
> **La potencia booleana no es la potencia matricial usual.** El producto numérico puede contar cuántas conexiones hay; el booleano se limita a indicar **si existe al menos una**.

## RELACIONES Y CAMINOS

Una matriz booleana puede ser la **matriz de adyacencia** de una relación o grafo: su entrada $(i, j)$ vale $1$ cuando existe una conexión directa de $i$ a $j$.

- $A^{\odot 2}$ identifica conexiones mediante **dos pasos**.
- $A^{\odot k}$ identifica la existencia de un **recorrido de longitud exactamente $k$**.
- La unión de estas potencias permite estudiar qué elementos pueden alcanzarse, aunque no haya una conexión directa.

Consulta [Relaciones binarias](binary_relations.md) para estudiar cómo se representa y calcula el cierre transitivo de una relación.

## RESUMEN

| OPERACIÓN     | NOMBRE              | REGLA                               |
|:------------- |:------------------- |:----------------------------------- |
| $A \lor B$    | Join / unión        | OR en posiciones correspondientes.  |
| $A \land B$   | Meet / intersección | AND en posiciones correspondientes. |
| $A \odot B$   | Producto booleano   | Fila-columna con AND y OR.          |
| $A^{\odot k}$ | Potencia booleana   | Producto booleano repetido.         |

> [!warning] ERRORES FRECUENTES
> - Sumar números y obtener $2$ donde correspondía aplicar OR y obtener $1$.
> - Confundir **join** (OR) con **meet** (AND).
> - Usar el producto elemento a elemento en lugar del **producto booleano fila-columna**.
> - Confundir $A^{\odot2}$ con $A^2$ (producto matricial numérico).
