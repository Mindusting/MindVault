---
aliases: [Conectores lógicos matemáticos]
author: Mindusting
corrected: false
creationDate: 2026-10-21 07:03:59
headerFile: false
modificationDate: 2026-11-02 03:07:31
rating: 
tags: [Math]
---

# CONECTORES LÓGICOS

> [!seealso]- MIRA TAMBIÉN
> - [Proposiciones](propositions.md)
> - [Predicados](predicates.md)
> - [Cuantificadores](quantifiers.md)
> - [Tablas de verdad](truth_tables.md)
> - [Reglas de inferencia](inference_rules.md)

Un **conector lógico** es un operador que permite **negar o combinar [proposiciones](propositions.md)** para construir una [proposición compuesta](propositions.md#PROPOSICIONES%20COMPUESTAS).

- **[Negación ($\neg$)](#NEGACIÓN%20(NO)):** se aplica a una sola [proposición](propositions.md) (*estando esta última a la izquierda del conector*).
- **[Conjunción ($\land$)](#CONJUNCIÓN%20(Y)), [disyunción ($\lor$)](#DISYUNCIÓN%20(O)), [condicional ($\to$)](#CONDICIONAL%20(SI...%20ENTONCES...)) y [bicondicional ($\leftrightarrow$)](#BICONDICIONAL%20(SI%20Y%20SOLO%20SI)):** relacionan dos [proposiciones](propositions.md) (*estando estas últimas, una acada lado del conector*).

## NEGACIÓN (NO)

La **negación** ($\neg$) invierte el valor de verdad de una [proposición](propositions.md).

| $p$ | $\neg p$ |
|:---:|:--------:|
|  F  |    V     |
|  V  |    F     |

> [!syntax] SINTAXIS
> 
> $$\neg p$$

> [!example] EJEMPLO
> 
> $$p: 5 < 3$$
> 
> Por lo que $p$ es falso y por tanto $\neg p$ es verdadero.

## CONJUNCIÓN (Y)

La **conjunción** ($\land$) es verdadera **únicamente cuando ambas [proposiciones](propositions.md) son verdaderas**.

| $p$ | $q$ | $p \land q$ |
|:---:|:---:|:-----------:|
|  F  |  F  |      F      |
|  F  |  V  |      F      |
|  V  |  F  |      F      |
|  V  |  V  |      V      |

> [!syntax] SINTAXIS
> 
> $$p \land q$$

> [!example] EJEMPLO
> 
> $$
> p: 3 > 2\\
> q: 8 < 5
> $$
> 
> Al ser $p$ verdadero y $q$ falso, $p \land q$ es falso.

## DISYUNCIÓN (O)

La **disyunción** ($\lor$) es verdadera cuando **al menos una de las proposiciones es verdadera**.

| $p$ | $q$ | $p \lor q$ |
|:---:|:---:|:----------:|
|  F  |  F  |     F      |
|  F  |  V  |     V      |
|  V  |  F  |     V      |
|  V  |  V  |     V      |

> [!syntax] SINTAXIS
> 
> $$p \lor q$$

> [!example] EJEMPLO
> 
> $$
> p: 3 > 2\\
> q: 8 < 5
> $$
> 
> Al ser $p$ verdadero y $q$ falso, $p \lor q$ es verdadero.

## CONDICIONAL (SI... ENTONCES...)

El **condicional** ($\to$) expresa "si se cumple $p$, entonces se cumple $q$". **Solo es falso cuando $p$ es verdadera y $q$ es falsa**.

| $p$ | $q$ | $p \to q$ |
|:---:|:---:|:---------:|
|  F  |  F  |     V     |
|  F  |  V  |     V     |
|  V  |  F  |     F     |
|  V  |  V  |     V     |

> [!syntax] SINTAXIS
> 
> $$p \to q$$

En este contexto ==a $p$ se le llama **antecedente**== o hipótesis; mientras que ==a $q$ se le llama **consecuente**== o conclusión del condicional.

> [!example] EJEMPLO
> 
> $$
> \begin{aligned}
> p&: 6 \text{ es par}\\
> q&: 6 \text{ es múltiplo de } 4
> \end{aligned}
> $$
> 
> En donde $p$ es verdadero y $q$ es falso, por lo que $p \to q$ es falso, ya que si $p$ es verdadero, $q$ también lo tendría que ser si $p \to q$ fuese verdadero.

> [!important] IMPORTANTE
> Si $p$ es falsa, el condicional $p \to q$ se considera **verdadero** en lógica clásica, independientemente del valor de $q$.

## BICONDICIONAL (SI Y SOLO SI)

El **bicondicional** ($\leftrightarrow$) es verdadero cuando **ambas proposiciones tienen el mismo valor de verdad** (las dos verdaderas o las dos falsas).

| $p$ | $q$ | $p \leftrightarrow q$ |
|:---:|:---:|:---------------------:|
|  F  |  F  |           V           |
|  F  |  V  |           F           |
|  V  |  F  |           F           |
|  V  |  V  |           V           |

> [!syntax] SINTAXIS
> 
> $$p \leftrightarrow q$$

> [!example] EJEMPLO
> 
> $$
> \begin{aligned}
> P(n)&: n \text{ es par}\\
> Q(n)&: n \text{ es divisible en tre } 2
> \end{aligned}
> $$
> 
> En este caso se puede decir que $P(n) \leftrightarrow Q(n)$, ya que los números pares son divisibles entre $2$.

## PRIORIDAD DE LOS CONECTORES

La prioridad indica en qué orden se debe aplicar los conectores lógicos:

1. **[Negación](#NEGACIÓN%20(NO)):** $\neg$
2. **[Conjunción](#CONJUNCIÓN%20(Y)) y [disyunción](#DISYUNCIÓN%20(O)):** $\land$, $\lor$
3. **[Condicional](#CONDICIONAL%20(SI...%20ENTONCES...)):** $\to$
4. **[Bicondicional](#BICONDICIONAL%20(SI%20Y%20SOLO%20SI)):** $\leftrightarrow$

> [!important] IMPORTANTE
> Para evitar ambigüedades, utiliza **paréntesis**:
> 
> $$p \land (q \lor r)$$
> 
> $$ (p \land q) \lor r$$

## IMPLICACIÓN Y EQUIVALENCIA LÓGICA

Las **flechas simples** representan conectores; las **flechas dobles** expresan relaciones lógicas válidas en todas las combinaciones de valores de verdad.

- **Condicional ($\to$):** proposición que puede ser verdadera o falsa.
- **Implicación lógica ($\implies$):** $A \implies B$ cuando $A \to B$ es una **tautología**.
- **Bicondicional ($\leftrightarrow$):** proposición que puede ser verdadera o falsa.
- **Equivalencia lógica ($\iff$):** $A \iff B$ cuando $A \leftrightarrow B$ es una **tautología**.

> [!example] EJEMPLOS
> - **Implicación lógica:** $(p \land q) \implies p$
> - **Equivalencia lógica:** $(p \lor q) \iff (q \lor p)$
> 
> Consulta las [tablas de verdad](truth_tables.md) para comprobar estas relaciones.

## RESUMEN

| CONECTOR          |        SÍMBOLO        | ES VERDADERO CUANDO...                       |
|:----------------- |:---------------------:|:-------------------------------------------- |
| **Negación**      |       $\neg p$        | $p$ es falsa.                                |
| **Conjunción**    |      $p \land q$      | Ambas son verdaderas.                        |
| **Disyunción**    |      $p \lor q$       | Al menos una es verdadera.                   |
| **Condicional**   |       $p \to q$       | No ocurre que $p$ sea verdadera y $q$ falsa. |
| **Bicondicional** | $p \leftrightarrow q$ | Ambas tienen el mismo valor de verdad.       |

> [!warning] ERRORES FRECUENTES
> - Interpretar $p \lor q$ como "una u otra, pero no ambas".
> - Considerar falso $p \to q$ cuando $p$ es falsa.
> - Olvidar que $p \leftrightarrow q$ es verdadero si **ambas son falsas**.
> - Confundir $\to$ con $\implies$, o $\leftrightarrow$ con $\iff$.
> - Omitir paréntesis en expresiones ambiguas.
