---
aliases: [Reglas de inferencia en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-21 07:11:17
headerFile: false
modificationDate: 2026-10-27 06:16:43
rating: 
tags: [Math]
---

# REGLAS DE INFERENCIA

> [!seealso]- MIRA TAMBIÉN
> - [Proposiciones](propositions.md)
> - [Predicados](predicates.md)
> - [Conectores lógicos](logical_connectives.md)
> - [Tablas de verdad](truth_tables.md)
> - [Métodos de demostración](proof_methods.md)

Una **regla de inferencia** es un patrón de razonamiento que permite obtener una **conclusión** a partir de una o varias **premisas**.

Una inferencia es **válida** cuando, si todas sus premisas son verdaderas; por tanto, la conclusión necesariamente también lo es.

- **Premisas:** afirmaciones de las que partimos.
- **Conclusión:** afirmación que deducimos de las premisas.
- **$\therefore$:** significa "*por tanto*".
- **$p$, $q$, $r$:** representan [proposiciones](propositions.md).

## MODUS PONENS

El **modus ponens** consiste en concluir $q$ cuando sabemos que $p \to q$ y que $p$ es verdadera.

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
> - $p\to q$: si se cumple $p$, entonces se cumple $q$.
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

## RELACIÓN CON LOS MÉTODOS DE DEMOSTRACIÓN

- Las **reglas de inferencia** justifican los pasos de un razonamiento.
- Los [**métodos de demostración**](proof_methods.md) organizan esos pasos para probar una afirmación.

## RESUMEN

| Regla                     |      Premisas       | Conclusión |
|:------------------------- |:-------------------:|:----------:|
| **Modus ponens**          |    $p\to q$, $p$    |    $q$     |
| **Modus tollens**         | $p\to q$, $\neg q$  |  $\neg p$  |
| **Modus tollendo ponens** | $p\lor q$, $\neg p$ |    $q$     |

> [!warning] ERRORES FRECUENTES
> - **Afirmar el consecuente:** de $p\to q$ y $q$ **no** podemos deducir $p$.
> - **Negar el antecedente:** de $p\to q$ y $\neg p$ **no** podemos deducir $\neg q$.
> - Confundir que una inferencia sea **válida** con que sus premisas sean verdaderas.
> - Confundir una **implicación** ($\implies$) con una **equivalencia lógica** ($\iff$).
