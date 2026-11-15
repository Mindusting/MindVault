---
aliases: [Matrices cero-uno]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-15 05:58:42
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

## DIFERENCIA ENTRE MATRICES NUMÉRICAS Y BOOLEANAS

Una matriz de números puede utilizarse para sumar, multiplicar y representar transformaciones. Una matriz booleana usa la **misma organización en filas y columnas**, pero interpretamos sus entradas como condiciones verdaderas o falsas.

Esta diferencia afecta a las operaciones. Con aritmética usual, $1 + 1 = 2$; con el operador lógico OR, $1 \lor 1 = 1$. De forma similar, con AND tenemos $1 \land 1 = 1$, pero $1 \land 0 = 0$.

> [!example] EJEMPLO
> En un grafo, si una persona puede llegar a otra por dos caminos alternativos, una matriz de **accesibilidad booleana** solo necesita indicar que la conexión existe. Por eso el resultado es $1$, no $2$. Si quisiéramos **contar** caminos, necesitaríamos otra interpretación y posiblemente un producto numérico.

### CONDICIONES PARA OPERAR

- La unión e intersección se realizan **entrada a entrada** y requieren matrices de las mismas dimensiones.
- El producto booleano combina filas y columnas; requiere que las **columnas de la primera** coincidan en número con las **filas de la segunda**.
- Las potencias booleanas se aplican a matrices cuadradas, porque multiplicamos reiteradamente una matriz por sí misma.

> [!important] IMPORTANTE
> "Matrices del mismo orden" significa aquí que tienen el mismo número de filas y de columnas. Dos matrices pueden ser ambas booleanas y, sin embargo, tener dimensiones incompatibles para una operación.

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
> A \lor B = \begin{pmatrix}
> 1 \lor 0 & 0 \lor 1 & 1 \lor 0\\
> 0 \lor 1 & 1 \lor 1 & 0 \lor 0
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

## RELACIÓN CON CONJUNTOS Y OPERADORES LÓGICOS

La unión y la intersección de matrices booleanas pueden entenderse como operaciones con conjuntos de posiciones. Si $A$ contiene unos en las posiciones $S_A$ y $B$ en las posiciones $S_B$, entonces $A \lor B$ pone un uno en las posiciones de $S_A \cup S_B$, mientras que $A \land B$ conserva únicamente las de $S_A \cap S_B$.

También existen relaciones algebraicas útiles:

- **Conmutatividad:** $A \lor B = B \lor A$ y $A \land B = B \land A$.
- **Idempotencia:** $A \lor A = A$ y $A \land A = A$.
- **Distributividad:** $A \land (B \lor C) = (A \land B) \lor (A \land C)$ para matrices compatibles.

Estas leyes son versiones **posición a posición** de las leyes de los conectores lógicos. No hay que confundirlas con el producto booleano de matrices, que es una operación distinta.

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

## CÁLCULO DETALLADO DE UN PRODUCTO BOOLEANO

Sean:

$$
A = \begin{pmatrix}
1 & 0 & 1\\
0 & 1 & 1
\end{pmatrix},
\qquad B = \begin{pmatrix}
0 & 1\\
1 & 0\\
1 & 1
\end{pmatrix}
$$

La primera matriz tiene dimensión $2 \times 3$ y la segunda $3 \times 2$. Como las dimensiones interiores coinciden, el resultado será $2 \times 2$.

Calculamos sus cuatro entradas. En cada una, emparejamos los elementos de una fila de $A$ con una columna de $B$:

$$
\begin{aligned}
c_{11} &= (1 \land 0) \lor (0 \land 1) \lor (1 \land 1) = 1\\
c_{12} &= (1 \land 1) \lor (0 \land 0) \lor (1 \land 1) = 1\\
c_{21} &= (0 \land 0) \lor (1 \land 1) \lor (1 \land 1) = 1\\
c_{22} &= (0 \land 1) \lor (1 \land 0) \lor (1 \land 1) = 1
\end{aligned}
$$

Por tanto:

$$
A \odot B = \begin{pmatrix}
1 & 1\\
1 & 1
\end{pmatrix}
$$

> [!important] IMPORTANTE
> Cada entrada del resultado representa una **pregunta existencial**: ¿hay al menos un índice $k$ para el cual $a_{ik} = 1$ y $b_{kj} = 1$? Si existe tal índice, el valor es $1$. Si no existe ninguno, es $0$.

Esta interpretación conecta el producto booleano con una expresión de lógica de predicados:

$$
c_{ij} = 1 \iff \exists k\ (a_{ik} = 1 \land b_{kj} = 1)
$$

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

## POTENCIAS Y RECORRIDOS DE LONGITUD EXACTA

Consideremos los vértices $1$, $2$ y $3$, con conexiones $1 \to 2$ y $2\to3$. Su matriz booleana de adyacencia es:

$$
A = \begin{pmatrix}
0 & 1 & 0\\
0 & 0 & 1\\
0 & 0 & 0
\end{pmatrix}
$$

- En $A$, la entrada $(1, 2)$ es $1$ porque existe un recorrido de **un paso** desde $1$ hasta $2$.
- En $A^{\odot 2}$, la entrada $(1, 3)$ vale $1$ porque existe el recorrido $1 \to 2 \to 3$ de **dos pasos**.
- En $A^{\odot 3}$, todas las entradas valen $0$: en este grafo no existe ningún recorrido de tres pasos.

Una potencia $A^{\odot k}$ indica si existe un recorrido de longitud **exactamente $k$**, no necesariamente el más corto. Si un grafo tiene ciclos, un par de vértices puede estar conectado mediante recorridos de diferentes longitudes.

### CIERRE TRANSITIVO

Para representar que podemos llegar de un vértice a otro mediante **uno o más pasos**, combinamos las potencias booleanas con OR. Si hay $n$ vértices, basta considerar las potencias de $1$ a $n$:

$$
T = A \lor A^{\odot 2} \lor \cdots \lor A^{\odot n}
$$

Para incluir también los recorridos de **cero pasos** (cada vértice puede alcanzarse a sí mismo), añadimos la identidad $I_n$:

$$T^* = I_n \lor T$$

La justificación de usar hasta $n$ pasos es que un recorrido suficientemente largo en un grafo finito repite vértices y contiene un ciclo; los ciclos pueden eliminarse para estudiar conexiones entre vértices distintos. Los recorridos cerrados necesarios para detectar ciclos pueden representarse con una longitud de hasta $n$.

## ALGORITMO DE WARSHALL

El algoritmo de Warshall calcula la accesibilidad de un grafo de forma sistemática, sin construir explícitamente todas las potencias. Partimos de su matriz de adyacencia $R$ y permitimos progresivamente vértices intermedios.

> [!syntax] SINTAXIS
> 
> $$r_{ij} \gets r_{ij} \lor (r_{ik} \land r_{kj})$$
> 
> Para cada vértice intermedio $k$, comprobamos todos los pares $(i, j)$: si podemos ir de $i$ a $k$ y de $k$ a $j$, entonces también podemos ir de $i$ a $j$.

> [!note] NOTA (para programadores)
> Una implementación sencilla en Python usando listas:
> 
> ```python
> def cierre_transitivo(matriz: list[list[int]]) -> list[list[int]]:
>     n = len(matriz)
>     alcance = [fila.copy() for fila in matriz]
>     for k in range(n):
>         for i in range(n):
>             for j in range(n):
>                 alcance[i][j] = int(
>                     alcance[i][j] or (alcance[i][k] and alcance[k][j])
>                 )
>     return alcance
> ```
> 
> El algoritmo realiza del orden de $n^3$ comprobaciones. Calcula el **cierre transitivo**; si queremos el **reflexivo-transitivo**, debemos poner a $1$ también la diagonal.

## EJERCICIOS DE COMPROBACIÓN

1. Calcula $\begin{pmatrix} 1 & 0\\ 1 & 1 \end{pmatrix} \lor \begin{pmatrix} 0 & 1\\ 1 & 0\end{pmatrix}$.
2. ¿Qué significa que $(A^{\odot2})_{14} = 1$ para una matriz de adyacencia?
3. ¿Por qué $A \odot B$ no se calcula multiplicando directamente entradas con la misma posición?

> [!abstract] SOLUCIONES
> 1. $\begin{pmatrix} 1 & 1\\ 1 & 1\end{pmatrix}$.
> 2. Existe algún recorrido desde el vértice $1$ hasta el $4$ que utiliza exactamente dos conexiones.
> 3. Porque cada entrada del resultado combina **una fila de $A$ con una columna de $B$**, mediante AND y OR.

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
