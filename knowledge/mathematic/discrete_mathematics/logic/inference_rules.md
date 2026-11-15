---
aliases: [Reglas de inferencia en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-21 07:11:17
headerFile: false
modificationDate: 2026-11-15 04:20:20
rating: 
tags: [Math]
---

# REGLAS DE INFERENCIA

> [!seealso]- MIRA TAMBIÉN
> - [Proposiciones](propositions.md)
> - [Predicados](predicates.md)
> - [Conectores lógicos](logical_connectives.md)
> - [Tablas de verdad](truth_tables.md)
> - [Métodos de demostración](../proof_methods.md)

Una **regla de inferencia** es un patrón de razonamiento que permite obtener una **conclusión** a partir de una o varias **premisas**.

Una inferencia es **válida** cuando, **si todas sus premisas fueran verdaderas**, la conclusión necesariamente también lo sería.

- **Premisas:** afirmaciones de las que partimos.
- **Conclusión:** afirmación que deducimos de las premisas.
- **$\therefore$:** significa "*por tanto*".
- **$p$, $q$, $r$:** representan [proposiciones](propositions.md).

## QUÉ SIGNIFICA QUE UN ARGUMENTO SEA VÁLIDO

Un **argumento** es un conjunto de premisas junto con una conclusión. La validez evalúa la **forma del razonamiento**, no si las premisas describen correctamente el mundo.

> [!example] EJEMPLO
> - Premisa: si todos los gatos vuelan, mi gato vuela.
> - Premisa: todos los gatos vuelan.
> - Conclusión: mi gato vuela.
> 
> La primera premisa está formulada de manera poco natural y la segunda es falsa en el mundo real, pero la **estructura deductiva** es válida: si ambas premisas fueran verdaderas, la conclusión tendría que serlo.

Para verificar la validez buscamos un **contraejemplo lógico**: una asignación en la que todas las premisas sean verdaderas y la conclusión falsa. Si existe, el argumento es inválido. Si no existe, es válido.

La relación se puede expresar como una tautología. Si las premisas son $P_1, \ldots, P_n$ y la conclusión es $Q$, el razonamiento es válido cuando:

$$(P_1 \land \cdots \land P_n) \to Q$$

es una tautología. Esta es la conexión fundamental entre inferencias y [tablas de verdad](truth_tables.md).

## MODUS PONENS

El **modus ponens** consiste en concluir $q$ cuando sabemos que $p  \to q$ y que $p$ es verdadera.

> [!syntax] SINTAXIS
> 
> $$
> \begin{array}{c}
> p \to q\\
> p\\
> \hline
> \therefore q
> \end{array}
> $$
> 
> - $p \to q$: si se cumple $p$, entonces se cumple $q$.
> - $p$: se cumple la condición inicial.
> - $q$: podemos concluir que también se cumple.

> [!example] EJEMPLO
> - **Premisa 1:** si $12$ es múltiplo de $4$, entonces $12$ es par.
> - **Premisa 2:** $12$ es múltiplo de $4$.
> - **Conclusión:** $12$ es par.

## MODUS TOLLENS

El **modus tollens** consiste en concluir $\neg p$ cuando sabemos que $p \to q$ y que $q$ es falsa.

> [!syntax] SINTAXIS
> 
> $$
> \begin{array}{c}
> p \to q\\
> \neg q\\
> \hline
> \therefore \neg p
> \end{array}
> $$
> 
> - $p \to q$: si se cumple $p$, entonces se cumple $q$.
> - $\neg q$: sabemos que $q$ no se cumple.
> - $\neg p$: concluimos que $p$ tampoco se cumple.

> [!example] EJEMPLO
> - **Premisa 1:** si $7$ es múltiplo de $4$, entonces $7$ es par.
> - **Premisa 2:** $7$ no es par.
> - **Conclusión:** $7$ no es múltiplo de $4$.

## SILOGISMO HIPOTÉTICO Y CONJUNCIÓN

Además de las reglas anteriores, es frecuente usar las siguientes:

### SILOGISMO HIPOTÉTICO

> [!syntax] SINTAXIS
> 
> $$
> \begin{array}{c}
> p \to q\\
> q \to r\\
> \hline \therefore p \to r
> \end{array}
> $$

Por ejemplo: si termino los ejercicios, entiendo el tema; si entiendo el tema, puedo resolver el examen. De ambas premisas deducimos que **si termino los ejercicios, puedo resolver el examen**. No deducimos que ya haya terminado los ejercicios.

### INTRODUCCIÓN DE LA CONJUNCIÓN

> [!syntax] SINTAXIS
> 
> $$
> \begin{array}{c}
> p\\
> q\\
> \hline \therefore p \land q
> \end{array}
> $$

Si sabemos por separado que $4>2$ y que $4$ es par, podemos afirmar su conjunción. Al revés, la **simplificación** permite extraer cualquiera de las dos partes de una conjunción conocida.

### RESOLUCIÓN

> [!syntax] SINTAXIS
> 
> $$
> \begin{array}{c}
> p \lor q\\
> \neg p \lor r\\
> \hline \therefore q \lor r
> \end{array}
> $$

La resolución elimina una proposición que aparece afirmada en una premisa y negada en otra. Es fundamental en sistemas de razonamiento automático y en el estudio de problemas de satisfacibilidad lógica.

## OTRAS REGLAS DE INFERENCIA

- **Simplificación:** $p \land q \implies p$
Si ambas se cumplen, podemos deducir una de ellas.
- **Adición:** $p \implies p \lor q$
Si $p$ es verdadera, $p$ o $q$ también lo es.
- **Modus tollendo ponens:** $(p \lor q) \land \neg p \implies q$
Si al menos una es verdadera y $p$ es falsa, entonces $q$ es verdadera.
- **Transitividad:** $((p \to q) \land (q \to r)) \implies (p \to r)$
Si $p$ lleva a $q$ y $q$ lleva a $r$, entonces $p$ lleva a $r$.

## EQUIVALENCIAS LÓGICAS ÚTILES

Una **equivalencia lógica** indica que dos expresiones tienen siempre el mismo valor de verdad.

- **Doble negación:**
$p \iff \neg \neg p$
- **Transposición (contraposición):**
$(p \to q) \iff (\neg q \to \neg p)$
- **Ley de De Morgan:**
$\neg (p \lor q) \iff \neg p \land \neg q$
$\neg (p \land q) \iff \neg p \lor \neg q$

## REGLAS CON CUANTIFICADORES

Las inferencias anteriores tratan proposiciones. En **lógica de predicados** también usamos reglas para los [cuantificadores](quantifiers.md).

### INSTANCIACIÓN UNIVERSAL

Si $P(x)$ se cumple para **todos** los elementos del dominio, entonces se cumple para uno concreto $a$ del mismo dominio:

$$
\forall x \in D,\ P(x) \quad \implies \quad P(a) \qquad(a \in D)
$$

Por ejemplo, si todos los enteros múltiplos de $4$ son pares, podemos aplicarlo al número $12$.

### GENERALIZACIÓN EXISTENCIAL

Si encontramos un valor permitido $a$ que cumple $P$, entonces existe al menos uno:

$$
P(a) \quad \implies \quad \exists x \in D,\ P(x) \qquad(a \in D)
$$

> [!warning] ERRORES FRECUENTES CON CUANTIFICADORES
> - De $P(3)$ **no** podemos concluir $\forall x\,P(x)$: un ejemplo no demuestra una afirmación universal.
> - De $\exists x\,P(x)$ **no** podemos afirmar $P(3)$ sin justificar que el testigo es precisamente $3$.
> - La generalización universal exige razonar sobre un elemento arbitrario, no sobre un caso elegido por tener una propiedad especial.

## EJEMPLO RESUELTO DE RAZONAMIENTO EN CADENA

Sean las premisas "Si estudio, practico", "Si practico, comprendo" y "Estudio". Definimos $p$: estudio; $q$: practico; $r$: comprendo.

1. $p \to q$ (primera premisa).
2. $q \to r$ (segunda premisa).
3. $p$ (tercera premisa).
4. $p \to r$ (silogismo hipotético aplicado a 1 y 2).
5. $r$ (modus ponens aplicado a 3 y 4).

La conclusión no aparece por intuición: cada paso está justificado por una regla concreta.

## EJERCICIOS DE COMPROBACIÓN

1. De $p \to q$ y $\neg q$, ¿qué deducimos?
2. ¿Es válido inferir $p$ a partir de $p \lor q$?
3. De $p \lor q$ y $\neg p$, ¿qué concluimos?

> [!abstract] SOLUCIONES
> 1. $\neg p$, por modus tollens.
> 2. No: puede ser verdadera solo $q$.
> 3. $q$, por modus tollendo ponens (silogismo disyuntivo).

## RELACIÓN CON LOS MÉTODOS DE DEMOSTRACIÓN

- Las **reglas de inferencia** justifican los pasos de un razonamiento.
- Los [**métodos de demostración**](../proof_methods.md) organizan esos pasos para probar una afirmación.

## RESUMEN

| REGLA                     |      PREMISAS       | CONCLUSIÓN |
|:------------------------- |:-------------------:|:----------:|
| **Modus ponens**          |    $p\to q$, $p$    |    $q$     |
| **Modus tollens**         | $p\to q$, $\neg q$  |  $\neg p$  |
| **Modus tollendo ponens** | $p\lor q$, $\neg p$ |    $q$     |

> [!warning] ERRORES FRECUENTES
> - **Afirmar el consecuente:** de $p \to q$ y $q$ **no** podemos deducir $p$.
> - **Negar el antecedente:** de $p \to q$ y $\neg p$ **no** podemos deducir $\neg q$.
> - Confundir que una inferencia sea **válida** con que sus premisas sean verdaderas.
> - Confundir una **implicación** ($\implies$) con una **equivalencia lógica** ($\iff$).
