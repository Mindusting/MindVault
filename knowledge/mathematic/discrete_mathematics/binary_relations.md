---
aliases: [Relaciones binarias]
author: Mindusting
corrected: false
creationDate: 2026-11-10 04:31:51
headerFile: false
modificationDate: 2026-11-15 05:43:00
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

## CÓMO SABER SI UN PAR PERTENECE A UNA RELACIÓN

Una relación binaria es un **conjunto de pares ordenados**. Por tanto, $aRb$ no significa necesariamente que $a$ y $b$ sean iguales o que uno sea mayor: depende de cómo hayamos definido $R$.

> [!example] EJEMPLO
> Sea $A = \{1, 2, 3, 4\}$ y definamos $R$ mediante "$a$ divide a $b$":
> 
> $$aRb \iff \exists k \in \mathbb Z,\ b = ak$$
> 
> Entonces $2R4$ es verdadero, porque $4 = 2 \cdot 2$; $3R4$ es falso porque $4$ no es múltiplo entero de $3$.

El mismo par puede pertenecer a una relación y no a otra. Por ejemplo, $(2, 4)$ pertenece a la relación "divide", pero no a la relación "es mayor que". **Siempre debemos conocer la definición de la relación** antes de examinarla.

### DOMINIO, CODOMINIO E IMAGEN

Si $R \subseteq A \times B$:

- **Conjunto de partida:** $A$, de donde se toma el primer elemento de cada par.
- **Conjunto de llegada:** $B$, de donde se toma el segundo.
- **Dominio efectivo de $R$:** elementos de $A$ que aparecen como primera componente de algún par.
- **Imagen o rango de $R$:** elementos de $B$ que aparecen como segunda componente de algún par.

> [!example] EJEMPLO
> Para $A = \{1, 2, 3\}$, $B = \{a, b\}$ y $R = \{(1, a), (3, a)\}$, el dominio efectivo es $\{1, 3\}$ y la imagen es $\{a\}$. El conjunto de partida sigue siendo $A$, aunque el número $2$ no participe en ningún par.

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
> Para $A = \{1, 2, 3\}$ y $R = \{(1, 2), (2, 3)\}$:
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

## PROPIEDADES ADICIONALES Y CÓMO COMPROBARLAS

Las propiedades estudiadas se definen sobre una relación $R \subseteq A \times A$. Podemos expresarlas formalmente:

| PROPIEDAD     | CONDICIÓN FORMAL                                  |
|:------------- |:------------------------------------------------- |
| Reflexiva     | $\forall a \in A,\ aRa$                           |
| Irreflexiva   | $\forall a \in A,\ \neg(aRa)$                     |
| Simétrica     | $\forall a, b \in A,\ aRb \to bRa$                |
| Antisimétrica | $\forall a, b \in A,\ (aRb \land bRa) \to a = b$  |
| Asimétrica    | $\forall a, b \in A,\ aRb \to \neg(bRa)$          |
| Transitiva    | $\forall a, b, c \in A,\ (aRb \land bRc) \to aRc$ |

La **antisimetría** no es lo contrario de la simetría. Una relación puede ser simultáneamente simétrica y antisimétrica, como la **igualdad**: solo contiene pares $(a, a)$.

> [!example] EJEMPLO COMPARATIVO
> La relación "$a < b$" sobre los enteros es **irreflexiva, asimétrica y transitiva**. Nunca ocurre $a < a$, ni pueden cumplirse a la vez $a < b$ y $b < a$.
> 
> La relación "$a \le b$" es **reflexiva, antisimétrica y transitiva**, pero no simétrica. Por ejemplo, $2 \le 3$, pero no $3 \le 2$.

### COMPROBACIÓN EN UNA MATRIZ

- Reflexiva: toda la diagonal principal debe valer $1$.
- Irreflexiva: toda la diagonal principal debe valer $0$.
- Simétrica: las entradas de posiciones $(i, j)$ y $(j, i)$ deben coincidir.
- Antisimétrica: para $i \ne j$, no puede haber un $1$ simultáneamente en $(i, j)$ y $(j, i)$.
- Transitiva: cada vez que exista un camino $i \to j \to k$, también debe existir la arista directa $i \to k$.

En la prueba de transitividad **no** basta mirar dos o tres parejas convenientes: hay que considerar todos los pares de aristas que puedan concatenarse.

## RELACIONES DE EQUIVALENCIA

Una relación es de **equivalencia** cuando cumple **reflexividad, simetría y transitividad**. La igualdad es el ejemplo más conocido, pero no el único.

> [!example] EJEMPLO: MISMO RESTO AL DIVIDIR ENTRE $3$
> Sobre los enteros, definimos $aRb$ cuando $a$ y $b$ tienen el mismo resto al dividir entre $3$. Equivalentemente, $3 \mid (a - b)$.
> 
> - Reflexiva: $a - a = 0$ es múltiplo de $3$.
> - Simétrica: si $3 \mid (a - b)$, también $3 \mid (b - a)$.
> - Transitiva: si $3 \mid (a - b)$ y $3 \mid (b - c)$, entonces $3 \mid (a - c)$ porque $(a - c) = (a - b) + (b - c)$.

Las relaciones de equivalencia dividen el conjunto en **clases de equivalencia**, grupos de elementos que están relacionados entre sí. En el ejemplo hay tres clases, correspondientes a restos $0$, $1$ y $2$.

## RELACIONES DE ORDEN

Una relación es un **orden parcial** si es **reflexiva, antisimétrica y transitiva**. Se llama *parcial* porque no exige que todos los pares de elementos distintos sean comparables.

> [!example] EJEMPLO
> En el conjunto de subconjuntos de $\{1, 2\}$, la inclusión $\subseteq$ es un orden parcial. Sin embargo, $\{1\}$ y $\{2\}$ son incomparables: ninguno es subconjunto del otro.

Un **orden total** añade que para cualesquiera $a, b$ del conjunto, $aRb$ o $bRa$. La relación $\le$ sobre los enteros es un orden total.

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
> R &= \{
>     (1, 2), 
>     (2, 3)
> \}\\
> R^+ &= \{
>     (1, 2),
>     (2, 3),
>     (1, 3)
> \}
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

## CONSTRUIR UN CIERRE PASO A PASO

Sea $A = \{1, 2, 3\}$ y $R = \{(1, 2), (2, 3)\}$. Queremos entender qué pares se añaden en cada tipo de cierre.

### CIERRE REFLEXIVO

Para que todos los elementos estén relacionados consigo mismos, añadimos $(1, 1)$, $(2, 2)$ y $(3, 3)$:

$$
R_{\mathrm{ref}} = \{
    (1, 2),
    (2, 3),
    (1, 1),
    (2, 2),
    (3, 3)
\}
$$

### CIERRE SIMÉTRICO

Necesitamos que cada conexión tenga su inversa. Añadimos $(2, 1)$ y $(3, 2)$:

$$
R_{\mathrm{sim}} = \{
    (1, 2),
    (2, 1),
    (2, 3),
    (3, 2)
\}
$$

### CIERRE TRANSITIVO

Como $1R2$ y $2R3$, añadimos $(1, 3)$. Ya no hay nuevos pares exigidos por transitividad:

$$
R^+= \{
    (1, 2),
    (2, 3),
    (1, 3)
\}
$$

> [!important] IMPORTANTE
> Los tres cierres son **operaciones distintas**. No debe añadirse automáticamente la diagonal cuando solo se pide el cierre transitivo. Tampoco debemos añadir pares inversos si únicamente nos piden el cierre reflexivo.

## INTERPRETACIÓN COMO GRAFO DIRIGIDO

Una relación sobre un conjunto finito se puede dibujar como un **grafo dirigido**:

- Cada elemento del conjunto es un vértice.
- Cada par $(a, b)$ de la relación representa una flecha de $a$ hacia $b$.
- Un par $(a, a)$ es un **bucle**.
- Una pareja de flechas en ambos sentidos representa $(a, b)$ y $(b, a)$.

Esta representación hace más visuales las propiedades: la simetría exige flechas de regreso; la reflexividad exige un bucle en todos los vértices; la transitividad exige conexiones directas para los caminos de dos pasos.

> [!note] NOTA
> Cuando una relación contiene un **ciclo**, su cierre transitivo puede contener pares $(a, a)$ aunque no estuvieran en la relación original. Por ejemplo, si $(1, 2)$ y $(2, 1)$ pertenecen a $R$, entonces el cierre transitivo contiene $(1, 1)$ y $(2, 2)$ gracias a los recorridos de longitud dos.

## CÁLCULO DEL CIERRE CON MATRICES BOOLEANAS

Las [potencias booleanas](boolean_matrices.md#POTENCIA%20BOOLEANA) detectan recorridos de distintas longitudes. Para un conjunto finito de $n$ elementos, basta unir las primeras $n$ potencias booleanas para obtener el cierre transitivo:

> [!syntax] SINTAXIS
> 
> $$
> M_{R^+} =
> M_R \lor M_R^{\odot 2} \lor \cdots \lor M_R^{\odot n}
> $$
> 
> - $\odot$ es el **producto booleano**.
> - $M_R^{\odot k}$ muestra si existe un recorrido de longitud $k$.
> - $\lor$ une todas las conexiones descubiertas.

El **cierre reflexivo-transitivo**, representado $R^*$, incluye además los pares $(a, a)$:

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
> # SALIDA:
> # [[0 1 1]
> #  [0 0 1]
> #  [0 0 0]]
> ```
> 
> Para una relación de cualquier tamaño finito $n$, el cierre transitivo puede construirse acumulando las potencias booleanas desde $1$ hasta $n$.

## COMPOSICIÓN DE RELACIONES

Además de estudiar una relación individualmente, podemos **componer** dos relaciones. Si $R \subseteq A \times B$ y $S \subseteq B \times C$, la composición que se aplica primero como $R$ y después como $S$ relaciona $a \in A$ con $c \in C$ cuando existe un elemento intermedio $b \in B$:

$$
\begin{aligned}
S \circ R = \{
&(a, c) \mid{} \exists b\in B,\\
&(a, b) \in R \land(b, c) \in S\}
\end{aligned}
$$

> [!example] EJEMPLO
> Si $R = \{(1, a), (2, b)\}$ y $S = \{(a, X), (b, Y)\}$, entonces $S \circ R = \{(1, X), (2, Y)\}$. Existe una conexión desde $1$ hasta $X$ pasando por $a$, y otra desde $2$ hasta $Y$ pasando por $b$.

El producto booleano de sus matrices representa precisamente este tipo de composición, con la convención de **fila = origen** y **columna = destino**:

$$M_{S \circ R} = M_R \odot M_S$$

## EJERCICIOS DE COMPROBACIÓN

1. Si $R = \{(1, 2), (2, 1)\}$ sobre $A = \{1, 2\}$, ¿es simétrica? ¿Es reflexiva?
2. Si $R = \{(1, 2), (2, 3)\}$, ¿qué par falta para cumplir la transitividad mínima?
3. ¿Puede una relación ser simétrica y antisimétrica a la vez?

> [!abstract] SOLUCIONES
> 1. Es simétrica, pero no reflexiva: faltan $(1, 1)$ y $(2, 2)$.
> 2. Falta $(1, 3)$.
> 3. Sí. La relación igualdad es ambas; para elementos distintos no contiene pares en ninguno de los dos sentidos.

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
