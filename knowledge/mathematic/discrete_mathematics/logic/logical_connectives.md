---
aliases: [Conectores lógicos matemáticos]
author: Mindusting
corrected: false
creationDate: 2026-10-21 07:03:59
headerFile: false
modificationDate: 2026-11-15 04:40:11
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

- **[Negación ($\neg$)](#NEGACIÓN%20(NO)):** se aplica a una sola [proposición](propositions.md) (*escribiendo el conector delante de la proposición*).
- **[Conjunción ($\land$)](#CONJUNCIÓN%20(Y)), [disyunción ($\lor$)](#DISYUNCIÓN%20(O)), [condicional ($\to$)](#CONDICIONAL%20(SI...%20ENTONCES...)) y [bicondicional ($\leftrightarrow$)](#BICONDICIONAL%20(SI%20Y%20SOLO%20SI)):** relacionan dos [proposiciones](propositions.md) (*estando estas últimas, una a cada lado del conector*).

## CÓMO EVALUAR UNA FÓRMULA LÓGICA

Los conectores reciben proposiciones y producen **nuevas proposiciones**. Su funcionamiento se determina exclusivamente por los valores de verdad de sus entradas, no por el tema del que hablan las frases.

Una regla práctica es leer los paréntesis desde dentro hacia fuera. Por ejemplo, en $\neg(p \land q)$ primero calculamos $p\land q$ y luego negamos el resultado. No es lo mismo que $\neg p \land q$, donde únicamente se niega $p$.

> [!example] EJEMPLO PASO A PASO
> Supongamos $p = \text{V}$ y $q = \text{F}$. Evaluamos $\neg (p \land q)$:
> 
> 1. $p \land q = \text{F}$, porque no son verdaderas ambas.
> 2. $\neg \text{F} = \text{V}$.
> 3. Por tanto, la fórmula completa es **verdadera**.
> 
> Si calculamos $\neg p \land q$, obtenemos $\text{F} \land \text{F} = \text{F}$: los paréntesis cambian el resultado.

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
> \begin{aligned}
> p &: 3 > 2\\
> q &: 8 < 5
> \end{aligned}
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
> \begin{aligned}
> p &: 3 > 2\\
> q &: 8 < 5
> \end{aligned}
> $$
> 
> Al ser $p$ verdadero y $q$ falso, $p \lor q$ es verdadero.

## DISYUNCIÓN EXCLUSIVA

En lenguaje cotidiano "o" a veces significa "una alternativa u otra, pero no las dos". Esta lectura se denomina **disyunción exclusiva** (XOR). Es diferente de la disyunción inclusiva $\lor$, que admite que las dos proposiciones sean verdaderas.

> [!syntax] SINTAXIS
> 
> $$
> p \oplus q \iff (p \lor q) \land \neg (p \land q)
> $$

| $p$ | $q$ | $p \lor q$ | $p \oplus q$ |
|:---:|:---:|:----------:|:------------:|
|  V  |  V  |     V      |      F       |
|  V  |  F  |     V      |      V       |
|  F  |  V  |     V      |      V       |
|  F  |  F  |     F      |      F       |

> [!note] NOTA (para programadores)
> En Python, con valores de tipo `bool`, `or` corresponde a la disyunción inclusiva; `^` corresponde a XOR. Por ejemplo, `True ^ True` es `False`, mientras que `True or True` es `True`.

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

## POR QUÉ EL CONDICIONAL CON ANTECEDENTE FALSO ES VERDADERO

El condicional de la lógica clásica $p \to q$ expresa que **no puede darse el caso** en el que se cumpla $p$ y falle $q$. Es equivalente a $\neg p \lor q$.

Imaginemos: "Si un número es divisible entre $4$, entonces es par". La afirmación no se invalida por encontrar un número impar que no es divisible entre $4$, ni por encontrar un número par que no sea divisible entre $4$. **Lo único que la refutaría** sería un número divisible entre $4$ que no fuese par.

Esto se llama, a veces, "verdad vacía" cuando la hipótesis es falsa: la condición no se ha incumplido. No debe confundirse con una relación de causalidad en el mundo real; el condicional material solo depende de los valores de verdad.

### RECÍPROCA, INVERSA Y CONTRAPOSITIVA

Para $p \to q$ distinguimos:

| FORMA          | FÓRMULA             | RELACIÓN CON LA ORIGINAL             |
|:-------------- |:------------------- |:------------------------------------ |
| Original       | $p \to q$           | La afirmación que estudiamos.        |
| Recíproca      | $q \to p$           | No es equivalente en general.        |
| Inversa        | $\neg p \to \neg q$ | No es equivalente en general.        |
| Contrapositiva | $\neg q \to \neg p$ | **Sí es equivalente** a la original. |

> [!example] EJEMPLO
> "Si un entero es divisible entre $4$, entonces es par" es verdadero. Su recíproca "si es par, entonces es divisible entre $4$" es falsa: $6$ es un contraejemplo. Su contrapositiva "si no es par, entonces no es divisible entre $4$" es verdadera.

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
> Q(n)&: n \text{ es divisible entre } 2
> \end{aligned}
> $$
> 
> En este caso se puede decir que $P(n) \leftrightarrow Q(n)$, ya que los números pares son divisibles entre $2$.

## PRIORIDAD DE LOS CONECTORES

En muchos cursos se usa, de mayor a menor prioridad, **negación**, **conjunción**, **disyunción**, **condicional** y **bicondicional**. Sin embargo, algunas convenciones dan prioridad igual a ciertos conectores, por lo que **siempre es preferible usar paréntesis**.

1. **Negación:** $\neg$.
2. **Conjunción:** $\land$.
3. **Disyunción:** $\lor$.
4. **Condicional:** $\to$.
5. **Bicondicional:** $\leftrightarrow$.

> [!important] IMPORTANTE
> Para evitar ambigüedades, utiliza **paréntesis**:
> 
> $$p \land (q \lor r)$$
> 
> $$ (p \land q) \lor r$$

## LEYES FUNDAMENTALES DE LOS CONECTORES

Estas identidades son útiles para transformar fórmulas sin alterar su valor de verdad. Se pueden verificar con [tablas de verdad](truth_tables.md).

| NOMBRE          | EQUIVALENCIA                                            |
|:--------------- |:------------------------------------------------------- |
| Doble negación  | $\neg \neg p \iff p$                                    |
| Conmutatividad  | $p \land q \iff q \land p$ y $p c \lor q \iff q \lor p$ |
| Asociatividad   | $(p \land q) \land r \iff p \land (q \land r)$          |
| Distributividad | $p \land (q \lor r) \iff (p \land q) \lor (p \land r)$  |
| De Morgan       | $\neg (p \land q) \iff \neg p \lor \neg q$              |
| De Morgan       | $\neg (p \lor q) \iff \neg p \land \neg q$              |
| Condicional     | $p \to q \iff \neg p \lor q$                            |
| Bicondicional   | $p \leftrightarrow q \iff (p \to q) \land (q \to p)$    |

> [!example] EJEMPLO RESUELTO
> Negar "Estudio y apruebo" no significa "No estudio y no apruebo". La negación correcta es "No estudio **o** no apruebo", porque basta con que falle una de las dos condiciones para que la conjunción original sea falsa.

## TRADUCIR CONECTORES DESDE EL LENGUAJE COTIDIANO

Al convertir frases en fórmulas es importante distinguir la **forma lógica** de la intención coloquial. Algunas expresiones habituales se traducen del siguiente modo:

| EXPRESIÓN                    | INTERPRETACIÓN HABITUAL EN LÓGICA                    |
|:---------------------------- |:---------------------------------------------------- |
| "$p$ y $q$"                  | $p \land q$                                          |
| "$p$ o $q$"                  | $p \lor q$ (o inclusiva, salvo indicación contraria) |
| "Si $p$, entonces $q$"       | $p \to q$                                            |
| "$p$ solo si $q$"            | $p \to q$                                            |
| "$p$ si $q$"                 | $q \to p$                                            |
| "$p$ si y solo si $q$"       | $p \leftrightarrow q$                                |
| "No es cierto que $p$ y $q$" | $\neg(p\land q)$                                     |

> [!example] EJEMPLO: "SOLO SI"
> "Un número es divisible entre $4$ solo si es par" significa: **ser par es una condición necesaria para ser divisible entre $4$**. Si $p$ significa "divisible entre $4$" y $q$ significa "par", la traducción correcta es $p \to q$.
> 
> La frase no afirma $q \to p$; de hecho, $6$ es par pero no es divisible entre $4$.

### CONDICIONES NECESARIAS Y SUFICIENTES

En $p \to q$:

- **$p$ es suficiente para $q$:** que ocurra $p$ garantiza $q$.
- **$q$ es necesaria para $p$:** si no ocurre $q$, no puede ocurrir $p$.

Por ejemplo, ser divisible entre $4$ es **suficiente** para ser par, y ser par es **necesario** para ser divisible entre $4$. Ninguna de las dos condiciones es suficiente para caracterizar completamente la otra. Para decir que una condición es **necesaria y suficiente** se utiliza el bicondicional.

## EJERCICIOS DE COMPROBACIÓN

1. [ ] Calcula $p \to q$ y $p \leftrightarrow q$ para $p = \text{F}$ y $q = \text{V}$.
2. Niega $p \lor q$ aplicando De Morgan.
3. ¿Son equivalentes $p \to q$ y $q \to p$? Razona con $p = \text{F}$, $q = \text{V}$.

> [!abstract] SOLUCIONES
> 1. Condicional verdadero; bicondicional falso.
> 2. $\neg p \land \neg q$.
> 3. No. $p \to q$ es verdadero, pero $q \to p$ es falso para esos valores.

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
