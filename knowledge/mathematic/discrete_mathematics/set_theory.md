---
aliases: [Teoría de conjuntos en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-23 03:48:55
headerFile: false
modificationDate: 2026-11-02 04:11:27
rating: 
tags: [Math]
---

# TEORÍA DE CONJUNTOS

> [!seealso]- MIRA TAMBIÉN
> - [Proposiciones](logic/propositions.md)
> - [Predicados](logic/predicates.md)
> - [Cuantificadores](logic/quantifiers.md)
> - [Conectores lógicos](logic/logical_connectives.md)

Un **conjunto** es una colección bien definida de **elementos** (*números, objetos, personas, etc.*).

- Los elementos de un conjunto **no se repiten**.
- **El orden no importa**: $\{1, 2, 3\} = \{3, 1, 2\}$.
- Los conjuntos suelen representarse mediante letras mayúsculas: $A$, $B$, $C$.

## REPRESENTACIÓN DE CONJUNTOS

- **Por extensión:** se enumeran sus elementos.
- **Por comprensión:** se indica una condición que deben cumplir sus elementos.

> [!syntax] SINTAXIS
> 
> $$A = \{1, 2, 3\}$$
> 
> $$A = \{x \in \mathbb{N} \mid 1 \leq x \leq 3\}$$
> 
> - $\in$: "pertenece a".
> - $\mid$: "tal que".
> - Ambas expresiones representan el mismo conjunto.

## PERTENENCIA

El símbolo $\in$ indica que un **elemento pertenece a un conjunto**; $\notin$ indica que no pertenece.

> [!example] EJEMPLO
> Si $A = \{1, 2, 3\}$:
> - $2 \in A$: verdadero.
> - $5 \notin A$: verdadero.

## CONJUNTOS ESPECIALES

- **Conjunto vacío ($\varnothing$):** no contiene elementos.
- **Conjunto universal ($U$):** reúne todos los elementos considerados en un contexto.
- **Conjunto finito:** tiene un número limitado de elementos.
- **Conjunto infinito:** no tiene un número finito de elementos.

Conjuntos numéricos habituales:

|   SÍMBOLO    | CONJUNTO            |
|:------------:|:------------------- |
| $\mathbb{N}$ | Números naturales.  |
| $\mathbb{Z}$ | Números enteros.    |
| $\mathbb{Q}$ | Números racionales. |
| $\mathbb{R}$ | Números reales.     |
| $\mathbb{C}$ | Números complejos.  |

> [!note] NOTA
> Algunos textos incluyen el $0$ en $\mathbb{N}$ y otros no. En estos apuntes utilizaremos $\mathbb{N} = \{0, 1, 2, \ldots\}$.

## RELACIONES ENTRE CONJUNTOS

- **Subconjunto ($A \subseteq B$):** todos los elementos de $A$ pertenecen a $B$; pueden ser iguales.
- **Subconjunto propio ($A \subsetneq B$):** $A \subseteq B$ y $A \neq B$.
- **Igualdad ($A = B$):** ambos conjuntos contienen exactamente los mismos elementos.
- **Disjuntos:** no tienen elementos en común ($A \cap B = \varnothing$).

> [!example] EJEMPLO
> Si $A = \{1, 2\}$ y $B = \{1, 2, 3\}$:
> - $A \subseteq B$: verdadero.
> - $A \subsetneq B$: verdadero.
> - $B \subseteq A$: falso.

> [!important] IMPORTANTE
> **Pertenencia** ($\in$) relaciona un elemento con un conjunto; **inclusión** ($\subseteq$) relaciona dos conjuntos.
> 
> Si $A = \{1, 2\}$, entonces $1 \in A$ y $\{1\} \subseteq A$.

## OPERACIONES CON CONJUNTOS

Consideremos:

$$A = \{1, 2, 3\}, \quad B = \{3, 4\}, \quad U = \{1, 2, 3, 4, 5\}$$

### UNIÓN

La **unión** ($A \cup B$) contiene los elementos que están en $A$, en $B$ o en ambos.

> [!example] EJEMPLO
> 
> $$A \cup B = \{1, 2, 3, 4\}$$

### INTERSECCIÓN

La **intersección** ($A \cap B$) contiene los elementos que pertenecen **a ambos** conjuntos.

> [!example] EJEMPLO
> 
> $$A \cap B = \{3\}$$

### DIFERENCIA

La **diferencia** ($A \setminus B$) contiene los elementos de $A$ que **no** pertenecen a $B$.

> [!example] EJEMPLO
> 
> $$A \setminus B = \{1, 2\}$$
> 
> $$B \setminus A = \{4\}$$

### COMPLEMENTO

El **complemento** ($A^c$) contiene los elementos del conjunto universal $U$ que **no** pertenecen a $A$.

> [!syntax] SINTAXIS
> 
> $$A^c = U \setminus A$$

> [!example] EJEMPLO
> 
> $$A^c = \{4, 5\}$$

### DIFERENCIA SIMÉTRICA

La **diferencia simétrica** ($A \triangle B$) contiene los elementos que pertenecen a **uno solo** de los conjuntos.

> [!syntax] SINTAXIS
> 
> $$A \triangle B = (A \setminus B) \cup (B \setminus A)$$

> [!example] EJEMPLO
> 
> $$A \triangle B=\{1, 2, 4\}$$

## PRODUCTO CARTESIANO

El **producto cartesiano** ($A \times B$) es el conjunto de todos los **pares ordenados** $(a, b)$ con $a \in A$ y $b \in B$.

> [!example] EJEMPLO
> Si $A = \{1, 2\}$ y $B = \{a, b\}$:
> 
> $$A \times B = \{(1, a),(1, b),(2, a),(2, b)\}$$
> 
> El orden de los elementos de cada par **sí importa**.

## CONJUNTO POTENCIA

El **conjunto potencia** ($\mathcal{P}(A)$) contiene **todos los subconjuntos** de $A$, incluidos $\varnothing$ y el propio $A$.

> [!example] EJEMPLO
> Si $A = \{1, 2\}$:
> 
> $$\mathcal{P}(A)=\{\varnothing, \{1\}, \{2\}, \{1,2\}\}$$

## CARDINALIDAD

La **cardinalidad** ($|A|$) indica cuántos elementos tiene un conjunto finito.

- Si $A=\{1,2,3\}$, entonces $|A| = 3$.
- Si $|A| = n$, el conjunto potencia tiene $2^n$ elementos: $|\mathcal{P}(A)| = 2^n$.

## LEYES DE DE MORGAN

Para conjuntos $A$ y $B$ dentro del mismo universo $U$:

$$(A \cup B)^c = A^c \cap B^c$$

$$(A \cap B)^c= A^c \cup B^c$$

- El complemento de una **unión** es la **intersección de los complementos**.
- El complemento de una **intersección** es la **unión de los complementos**.

## RESUMEN

|      SÍMBOLO      | SIGNIFICADO                 |
|:-----------------:|:--------------------------- |
|     $x \in A$     | $x$ pertenece a $A$.        |
|  $A \subseteq B$  | $A$ es subconjunto de $B$.  |
|    $A \cup B$     | Unión.                      |
|    $A \cap B$     | Intersección.               |
|  $A \setminus B$  | Diferencia.                 |
|       $A^c$       | Complemento respecto a $U$. |
|  $A \triangle B$  | Diferencia simétrica.       |
|   $A \times B$    | Producto cartesiano.        |
| $\mathcal{P}(A)$  | Conjunto potencia.          |
| $\lvert A \rvert$ | Cardinalidad.               |

> [!warning] ERRORES FRECUENTES
> - Confundir **pertenencia** ($\in$) con **inclusión** ($\subseteq$).
> - Repetir elementos o considerar que el orden importa dentro de un conjunto.
> - Confundir **unión** ($\cup$) con **intersección** ($\cap$).
> - Olvidar que el complemento depende del **conjunto universal**.
> - Confundir el conjunto vacío $\varnothing$ con $\{\varnothing\}$, que contiene un elemento.
