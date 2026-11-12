---
aliases: [Relaciones binarias]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-10 06:45:34
rating: 
tags: [Math]
---

# RELACIONES BINARIAS

> [!seealso]- MIRA TAMBIÉN
> - [Teoría de conjuntos](set_theory.md)
> - [Matrices booleanas](boolean_matrices.md)
> - [Matrices](../linear_algebra/matrix.md)
> - [Chuleta de matrices](../linear_algebra/matrix_cheatsheet.md)

Una **relación binaria** indica qué pares de elementos de dos conjuntos cumplen una determinada condición. Matemáticamente, se representa como un **conjunto de pares ordenados**, es decir, como un subconjunto del [producto cartesiano](set_theory.md#PRODUCTO%20CARTESIANO).

Por ejemplo, si relacionamos personas con las asignaturas en las que están matriculadas, cada par $(\text{persona}, \text{asignatura})$ puede pertenecer o no a la relación.

## REPRESENTACIÓN Y NOTACIÓN

> [!syntax] SINTAXIS
> 
> $$
> R \subseteq A \times B
> $$
> 
> - $A$, $B$: conjuntos entre los que se define la relación.
> - $R$: conjunto de pares ordenados que **sí** cumplen la relación.
> - $(a, b) \in R$: el elemento $a$ de $A$ está relacionado con $b$ de $B$; también escribimos $aRb$.

Cuando ambos elementos pertenecen al mismo conjunto, escribimos $R \subseteq A \times A$. Es el caso habitual al estudiar **reflexividad, simetría y transitividad**.

> [!example] EJEMPLO
> 
> $$
> \begin{aligned}
> A &= \{1, 2, 3\}\\
> R &= \{(1, 2), (2, 3)\}
> \end{aligned}
> $$
> 
> - $1R2$ y $2R3$ son verdaderas.
> - $1R3$ es falsa para la relación inicial: ese par todavía no pertenece a $R$.

## MATRIZ DE UNA RELACIÓN

Cuando los conjuntos son finitos, podemos representar la relación con una **matriz booleana**, que contiene $1$ o $0$ según exista o no el par correspondiente.

Si $A = \{a_1, \ldots, a_n\}$ y $R \subseteq A \times A$:

> [!syntax] SINTAXIS
> 
> $$
> m_{ij} = \begin{cases}
> 1, & (a_i, a_j) \in R\\
> 0, & (a_i, a_j) \notin R
> \end{cases}
> $$
> 
> La **fila** representa el primer elemento del par y la **columna** el segundo.

> [!example] EJEMPLO
> 
> Para $A = \{1,2,3\}$ y $R = \{(1, 2), (2, 3)\}$:
> 
> $$
> M_R = \begin{pmatrix}
> 0 & 1 & 0\\
> 0 & 0 & 1\\
> 0 & 0 & 0
> \end{pmatrix}
> $$
> 
> El $1$ de la posición $(1, 2)$ representa el par $(1, 2)$; el $1$ de la posición $(2, 3)$ representa $(2, 3)$.

## PROPIEDADES BÁSICAS

Para una relación $R$ definida **sobre el mismo conjunto** $A$:

- **Reflexiva:** cada elemento está relacionado consigo mismo: $aRa$ para todo $a \in A$. En la matriz, toda la **diagonal principal vale $1$**.
- **Simétrica:** si $aRb$, también $bRa$. Su matriz cumple $M_R = M_R^T$.
- **Antisimétrica:** si $aRb$ y $bRa$, entonces $a = b$. No prohíbe los pares $(a, a)$; prohíbe tener ambos sentidos entre elementos **distintos**.
- **Transitiva:** si $aRb$ y $bRc$, entonces $aRc$.

> [!example] EJEMPLO DE TRANSITIVIDAD
> Si una relación contiene $(1, 2)$ y $(2, 3)$, para ser transitiva también debe contener $(1, 3)$.
> 
> En el ejemplo anterior **falta** $(1, 3)$, así que la relación todavía no es transitiva.

## CIERRES DE UNA RELACIÓN

Un **cierre** añade a una relación los **pares estrictamente necesarios** para que cumpla una propiedad, sin eliminar los pares originales.

### CIERRE REFLEXIVO

Para conseguir reflexividad, añadimos los pares $(a, a)$ que falten; en la matriz equivale a realizar la unión booleana con la identidad:

$$
M_{\text{ref}} = M_R \lor I_n
$$

### CIERRE SIMÉTRICO

Para conseguir simetría, añadimos la relación en sentido contrario cuando falte. Matricialmente:

$$
M_{\text{sim}} = M_R \lor M_R^T
$$

### CIERRE TRANSITIVO

El **cierre transitivo** $R^+$ es la relación transitiva **más pequeña que contiene a $R$**. Añade los pares necesarios para reflejar conexiones que pueden obtenerse concatenando pasos.

> [!example] EJEMPLO
> 
> $$
> \begin{aligned}
> R &= \{(1, 2), (2, 3)\}\\
> R^+ &= \{(1, 2), (2, 3), (1, 3)\}
> \end{aligned}
> $$
> 
> $$
> M_{R^+} = \begin{pmatrix}
> 0 & 1 & 1\\
> 0 & 0 & 1\\
> 0 & 0 & 0
> \end{pmatrix}
> $$
> 
> Añadimos $(1, 3)$ porque existe una conexión $1 \to 2 \to 3$.

## CÁLCULO DEL CIERRE CON MATRICES BOOLEANAS

Las [potencias booleanas](boolean_matrices.md#POTENCIA%20BOOLEANA) detectan recorridos de distintas longitudes. Para un conjunto finito de $n$ elementos, basta unir las primeras $n$ potencias booleanas para obtener el cierre transitivo:

> [!syntax] SINTAXIS
> 
> $$
> M_{R^+}
> = M_R \lor M_R^{\odot 2} \lor \cdots \lor M_R^{\odot n}
> $$
> 
> - $\odot$ es el **producto booleano**.
> - $M_R^{\odot k}$ muestra si existe un recorrido de longitud $k$.
> - $\lor$ une todas las conexiones descubiertas.

El **cierre reflexivo-transitivo**, representado $R^*$, incluye además los pares $(a,a)$:

$$
M_{R^*} = I_n \lor M_{R^+}
$$

> [!important] IMPORTANTE
> **Transitivo** no significa necesariamente **reflexivo**. El cierre $R^+$ añade conexiones obtenidas con uno o más pasos; $R^*$ incluye también los recorridos de longitud cero, representados por la identidad.

## NOTA PARA PROGRAMADORES: NUMPY

> [!note] NOTA (para programadores)
> Una matriz de adyacencia se representa en NumPy con un array bidimensional booleano. Para nuestro ejemplo, calculamos los recorridos de dos pasos y los añadimos mediante OR:
> 
> ```python
> import numpy as np
>
> R = np.array(
>     [[0, 1, 0],
>      [0, 0, 1],
>      [0, 0, 0]],
>     dtype=bool
> )
>
> R2 = (R.astype(int) @ R.astype(int)) > 0
> cierre_transitivo = R | R2
> cierre_reflexivo = R | np.eye(3, dtype=bool)
>
> print(cierre_transitivo.astype(int))
> # SALIR:
> # [[0 1 1]
> #  [0 0 1]
> #  [0 0 0]]
> ```
> 
> Para una relación de cualquier tamaño finito $n$, el cierre transitivo puede construirse acumulando las potencias booleanas desde $1$ hasta $n$.

## RESUMEN

| CONCEPTO                          | IDEA ESENCIAL                                  |
|:--------------------------------- |:---------------------------------------------- |
| Relación binaria                  | Subconjunto de $A \times B$.                   |
| Matriz de relación                | $m_{ij} = 1$ si existe el par $(a_i, a_j)$.    |
| Reflexiva                         | La diagonal contiene unos.                     |
| Simétrica                         | $M_R = M_R^T$.                                 |
| Transitiva                        | $aRb$ y $bRc$ implican $aRc$.                  |
| Cierre transitivo $R^+$           | Añade conexiones obtenidas en uno o más pasos. |
| Cierre reflexivo-transitivo $R^*$ | Incluye además la identidad.                   |

> [!warning] ERRORES FRECUENTES
> - Confundir el producto cartesiano de conjuntos con el producto de matrices.
> - Confundir la posición $(i, j)$ con $(j, i)$: el orden de los pares importa.
> - Interpretar simetría como transitividad: son propiedades diferentes.
> - Confundir el cierre transitivo $R^+$ con el reflexivo-transitivo $R^*$.
