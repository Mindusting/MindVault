---
aliases: [Teoría de conjuntos en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-23 03:48:55
headerFile: false
modificationDate: 2026-11-15 06:58:56
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

## CARACTERÍSTICAS DE UN CONJUNTO

Decimos que una colección está **bien definida** cuando podemos decidir, dentro del contexto considerado, si un objeto determinado pertenece o no a ella. Por ejemplo, "los enteros pares" es un conjunto porque la condición de pertenencia es precisa; "los números bonitos" no es una definición matemática suficientemente clara sin especificar qué significa "bonito".

Los conjuntos no son listas ordenadas:

$$\{1, 2, 2, 3\} = \{3, 2, 1\}$$

La repetición del $2$ no crea un nuevo elemento y el orden no afecta a la igualdad. Sin embargo, en un **par ordenado** $(a, b)$ el orden sí importa: $(1, 2) \ne (2, 1)$.

> [!note] NOTA (para programadores)
> El concepto matemático de conjunto se parece al tipo `set` de Python: elimina duplicados y permite comprobar pertenencia. Es solo una analogía: las estructuras informáticas tienen restricciones de implementación, mientras que los conjuntos matemáticos pueden ser infinitos o contener objetos abstractos.

## CUANTIFICADORES PARA DESCRIBIR CONJUNTOS

La notación por comprensión expresa una **condición lógica**. Por ejemplo:

$$A = \{x \in \mathbb Z \mid x^2 < 10\}$$

Para resolverla buscamos los enteros cuyo cuadrado es menor que $10$:

$$A = \{-3, -2, -1, 0, 1, 2, 3\}$$

El dominio $\mathbb Z$ forma parte de la definición. Sin él, una misma condición podría describir conjuntos muy diferentes; en $\mathbb R$ habría infinitos números con $x^2 < 10$.

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

## DEMOSTRAR INCLUSIÓN E IGUALDAD

La igualdad de conjuntos no depende de cómo escribamos sus elementos, sino de qué elementos contienen. Una técnica general para demostrar $A=B$ es probar ambas inclusiones:

$$A \subseteq B \quad \text{y} \quad B \subseteq A$$

> [!example] EJEMPLO RESUELTO
> Demostremos $A \cap B \subseteq A$.
> 
> Tomamos un elemento cualquiera $x \in A \cap B$. Por definición de intersección, $x \in A$ **y** $x \in B$. En particular, $x \in A$. Como el argumento vale para cualquier elemento de $A \cap B$, se cumple la inclusión.

La **inclusión propia** exige algo más: además de $A \subseteq B$, debemos encontrar un elemento de $B$ que no pertenezca a $A$.

### CONJUNTO VACÍO Y CONJUNTOS QUE LO CONTIENEN

Es importante distinguir:

- $\varnothing$: conjunto sin elementos, con cardinalidad $0$.
- $\{ \varnothing \}$: conjunto cuyo **único elemento** es el conjunto vacío, con cardinalidad $1$.

Además, $\varnothing \subseteq A$ para cualquier conjunto $A$. La razón es que no existe ningún elemento del conjunto vacío que viole la condición de inclusión.

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
> $$A \triangle B = \{1, 2, 4\}$$

## DEFINICIONES FORMALES DE LAS OPERACIONES

A continuación se escribe cada operación mediante una condición de pertenencia. Estas definiciones ayudan a reconocer su relación con los [conectores lógicos](logic/logical_connectives.md).

| OPERACIÓN            | CONDICIÓN PARA $x$                                      |
|:-------------------- |:------------------------------------------------------- |
| Unión                | $x \in A \cup B \iff(x \in A) \lor (x \in B)$           |
| Intersección         | $x \in A \cap B \iff(x \in A) \land (x \in B)$          |
| Diferencia           | $x \in A \setminus B \iff (x \in A) \land (x \notin B)$ |
| Complemento          | $x \in A^c \iff x \in U \land x \notin A$               |
| Diferencia simétrica | $x \in A \triangle B \iff (x \in A) \oplus (x \in B)$   |

Las operaciones de conjuntos comparten muchas leyes con la lógica proposicional. Por ejemplo, las leyes de De Morgan explican que "no estar en $A$ ni en $B$" es equivalente a "no estar en la unión".

### PROPIEDADES ÚTILES

- Conmutativas: $A \cup B = B \cup A$ y $A \cap B = B \cap A$.
- Asociativas: $(A \cup B) \cup C = A \cup (B \cup C)$.
- Distributivas: $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$.
- Idempotentes: $A \cup A = A$ y $A \cap A = A$.
- Neutros: $A \cup \varnothing = A$ y $A \cap U = A$.

> [!example] EJEMPLO CON DE MORGAN
> Si $U = \{1, 2, 3, 4\}$, $A = \{1, 2\}$ y $B = \{2, 3\}$, entonces $(A \cup B)^c = \{4\}$. Por otro lado, $A^c = \{3, 4\}$ y $B^c = \{1, 4\}$; su intersección también es $\{4\}$.

## PRODUCTO CARTESIANO

El **producto cartesiano** ($A \times B$) es el conjunto de todos los **pares ordenados** $(a, b)$ con $a \in A$ y $b \in B$.

> [!example] EJEMPLO
> Si $A = \{1, 2\}$ y $B = \{a, b\}$:
> 
> $$A \times B = \{(1, a), (1, b), (2, a), (2, b)\}$$
> 
> El orden de los elementos de cada par **sí importa**.

## TAMAÑO DEL PRODUCTO CARTESIANO

Si $A$ tiene $m$ elementos y $B$ tiene $n$ elementos, entonces $A \times B$ tiene $m \cdot n$ pares. La razón es que para cada uno de los $m$ elementos de $A$ podemos elegir cualquiera de los $n$ elementos de $B$.

> [!example] EJEMPLO
> Con $A = \{1, 2, 3\}$ y $B = \{a, b\}$, el producto contiene seis pares: $(1, a)$, $(1, b)$, $(2, a)$, $(2, b)$, $(3, a)$ y $(3, b)$.

Esta idea es fundamental para las [relaciones binarias](binary_relations.md), porque una relación de $A$ a $B$ es un subconjunto de $A \times B$.

## CONJUNTO POTENCIA

El **conjunto potencia** ($\mathcal{P}(A)$) contiene **todos los subconjuntos** de $A$, incluidos $\varnothing$ y el propio $A$.

> [!example] EJEMPLO
> Si $A = \{1, 2\}$:
> 
> $$\mathcal{P}(A) = \{\varnothing, \{1\}, \{2\}, \{1, 2\}\}$$

## CARDINALIDAD

La **cardinalidad** ($|A|$) indica cuántos elementos tiene un conjunto finito.

- Si $A = \{1, 2, 3\}$, entonces $|A| = 3$.
- Si $|A| = n$, el conjunto potencia tiene $2^n$ elementos: $|\mathcal{P}(A)| = 2^n$.

## CONTEO DE ELEMENTOS: PRINCIPIO DE INCLUSIÓN-EXCLUSIÓN

Cuando dos conjuntos finitos se solapan, sumar sus cardinalidades cuenta los elementos comunes **dos veces**. Por eso debemos restar una vez la intersección:

> [!syntax] SINTAXIS
> 
> $$|A \cup B| = |A| + |B| - |A \cap B|$$

> [!example] EJEMPLO
> En un grupo, $18$ personas estudian Python, $12$ estudian Java y $5$ estudian ambos. El número de personas que estudian **al menos uno** de los dos lenguajes es:
> 
> $$18 + 12 - 5 = 25$$
> 
> No es $30$ porque estaríamos contando dos veces a las cinco personas que estudian ambos.

Para tres conjuntos se añade y resta cada solapamiento según corresponda:

$$
\begin{aligned}
|A \cup B \cup C| = {}& |A| + |B| + |C|\\
&- |A \cap B| - |A \cap C| - |B \cap C|\\
&+ |A \cap B \cap C|
\end{aligned}$$

## DEMOSTRACIÓN DE UNA LEY CON ELEMENTOS

Para demostrar $(A \cup B)^c = A^c \cap B^c$, tomamos un elemento arbitrario $x$ del universo:

$$

\begin{aligned}

x \in (A \cup B)^c & \iff x \notin A \cup B\\

&\iff (x \notin A) \land (x \notin B)\\

&\iff x \in A^c \cap B^c

\end{aligned}

$$

Cada equivalencia expresa la definición del conjunto correspondiente. Como la cadena vale para todo $x$, los conjuntos son iguales.

## EJERCICIOS DE COMPROBACIÓN

1. Calcula $\mathcal P(\{a, b, c\})$ y su cardinalidad.
2. Con $A = \{1, 2, 3\}$ y $B = \{3, 4\}$, calcula $A \setminus B$ y $B \setminus A$.
3. Si $|A| = 9$, $|B| = 7$ y $|A \cap B| = 3$, ¿cuánto vale $|A \cup B|$?

> [!abstract] SOLUCIONES
> 1. $\{\varnothing, \{a\}, \{b\}, \{c\}, \{a, b\}, \{a, c\}, \{b, c\}, \{a, b, c\} \}$; tiene $2^3 = 8$ elementos.
> 2. $A \setminus B = \{1, 2\}$ y $B \setminus A = \{4\}$.
> 3. $9 + 7 - 3 = 13$.

## LEYES DE DE MORGAN

Para conjuntos $A$ y $B$ dentro del mismo universo $U$:

$$(A \cup B)^c = A^c \cap B^c$$

$$(A \cap B)^c = A^c \cup B^c$$

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
