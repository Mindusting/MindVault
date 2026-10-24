---
aliases: [Proposiciones en matemáticas]
author: Mindusting
corrected: true
creationDate: 2026-10-21 06:50:39
headerFile: false
modificationDate: 2026-10-22 04:08:45
rating: 1
tags: [Math]
---

# PROPOSICIONES

> [!seealso]- MIRA TAMBIÉN
> - [Predicados](predicates.md)
> - [Cuantificadores](quantifiers.md)
> - [Conectores lógicos](logical_connectives.md)
> - [Tablas de verdad](truth_tables.md)
> - [Reglas de inferencia](inference_rules.md)

Una **proposición** es un ==enunciado declarativo== el cual tiene un ==valor de verdad==, es decir, **verdadero** o **falso**, pero ==no ambos de forma simultánea==.

Una **proposición** ==no necesita ser **verdadera**== para considerarse una **proposición**, únicamente debe tener un valor de verdad definido.

> [!success] QUÉ SÍ SON PROPOSICIONES
> - $5 > 3$:
> Sí es una proposición ya que es una afirmación y sabemos sin duda que su valor es verdadero.
> - $5 < 3$:
> Sí es una proposición ya que es una afirmación y sabemos sin duda que su valor es falso.
> - $3 + 2 = 5$:
> Sí es una proposición ya que es una afirmación y sabemos sin duda que su valor es verdadero.
> - Existen infinitos números primos:
> Sí es una proposición ya que esta tiene un valor de verdad, siendo esta **verdadera**.

> [!failure] QUÉ NO SON PROPOSICIONES
> - $x > 3$:
> No es una proposición ya que el valor $x$ no está definido, por lo que no podemos determinar su valor de verdad; si $x$ sí estuviese definido, sí sería una proposición.
> - ¿Cuánto es $5 + 3$?:
> No es una proposición ya que es una pregunta.
> - Calcula $5 + 3$:
> No es una proposición ya que es una orden.

> [!note] NOTA (para programadores)
> Si vienes de la rama de la programación, una proposición podría ser una comparación de dos valores:
> 
> ```python
> x = 3
> y = 2
> 
> x == y # es falsa.
> y != 4 # es verdadera.
> 5 < x  # es falsa.
> 5 > 4  # es verdadera.
> ```
> 
> Estas operaciones booleanas son equivalentes a las proposiciones en matemáticas ya que ambas dan como resultado un valor de verdadero o falso; pero no son lo mismo ya que en programación es una expresión que da como resultado un valor booleano, mientras que en matemáticas una proposición es una afirmación.

> [!note] PRINCIPIO DE BIVALENCIA
> En la lógica clásica, toda proposición tiene exactamente uno de los dos valores de verdad posibles:
> 
> - **Verdadero** (*V*)
> - **Falso** (*F*)
> 
> ==Una proposición no puede ser verdadera y falsa simultáneamente, ni carecer de valor de verdad==.
> 
> Existen otros sistemas lógicos que no siguen necesariamente estas mismas reglas.

## REPRESENTACIÓN DE PROPOSICIONES

Las proposiciones pueden estar representadas mediante letras a las que se les llama **variables proposicionales**, estas suelen ser letras en minúsculas como: $p, q, r...$; aunque también pueden estar en mayúsculas.

$$
\begin{aligned}
p &: 5 > 3\\
q &: 4 < 10
\end{aligned}
$$

En este caso, ambas proposiciones son verdaderas.

> [!note] NOTA (para programadores)
> En programación, esto sería el equivalente a usar variables para guardar los valores booleanos:
> 
> ```python
> p = 5 > 3
> q = 4 < 10
> 
> print(p)
> print(q)
> # SALIDA:
> # True
> # True
> ```
> 
> En matemáticas la letra representa una proposición, mientras que en los lenguajes de programación se almacena el resultado de una operación, por lo que son cosas distintas, pero a efectos prácticos, esta sería su equivalencia.

## PROPOSICIONES ATÓMICAS

Una **proposición atómica** es una proposición que no está formada por otras [proposiciones unidas mediante conectores lógicos](#PROPOSICIONES%20COMPUESTAS); las proposiciones atómicas son las más simples de la lógica proposicional; por ejemplo:

- $5 > 3$: Verdadero.
- $2 + 2 = 5$: Falso.
- La Tierra es un planeta: Verdadero.

Estas proposiciones pueden utilizarse individualmente o combinarse con otras mediante [conectores lógicos](logical_connectives.md) para construir proposiciones compuestas.

## PROPOSICIONES COMPUESTAS

Una proposición compuesta es una proposición formada mediante el uso de uno o varios [**conectores lógicos**](logical_connectives.md) sobre una o más proposiciones; dependiendo del [**conector lógico**](logical_connectives.md) que utilicemos, pueden intervenir una o varias proposiciones.

$$(5 > 3) \land (4 < 10)$$

Esta expresión se lee de la siguiente forma: $5$ es mayor que $3$ y $4$ es menor que $10$; juntando así las dos proposiciones con el operador "y".

También podemos usar las proposiciones representadas en forma de letras:

$$
\begin{aligned}
p&: 5 > 3\\
q&: 4 < 10\\
\\
&p \land q
\end{aligned}
$$

> [!note] NOTA (para programadores)
> Las proposiciones compuestas es como cuando usamos operadores booleanos entre comparaciones:
> 
> ```python
> print(5 > 3 and 4 < 10)
> # SALIDA:
> # True
> ```
> 
> En este caso podemos ver que se usa el operador `and`, éste indica que se debe cumplir la proposición de la izquierda (`5 > 3`) y la de la derecha (`4 < 10`) para que la proposición compuesta se cumpla; siendo el resultado en este caso: verdadero.
> 
> Y siguiendo con el ejemplo de antes, también se podría expresar de la siguiente forma:
> 
> ```python
> p = 5 > 3
> q = 4 < 10
> 
> print(p and q)
> # SALIDA:
> # True
> ```

---

También se considera una proposición compuesta una proposición sola con un [**conector lógico**](logical_connectives.md) de **negación**:

$$\neg(10 = 10)$$

De forma que el resultado sea falso.

Pudiendo ser también representado de la siguiente forma:

$$
p: 10 = 10\\
\\
\neg p
$$

> [!note] NOTA (para programadores)
> Este último ejemplo también se puede representar en forma de código:
> 
> ```python
> print(not(10 == 10))
> # SALIDA:
> # False
> ```
> 
> O de la siguiente forma:
> 
> ```python
> p = 10 == 10
> 
> print(not(p))
> # SALIDA:
> # False
> ```

## CLASIFICACIÓN SEGÚN EL VALOR DE VERDAD

Las [proposiciones compuestas](#PROPOSICIONES%20COMPUESTAS) pueden clasificarse en tres categorías según los valores de verdad que pueden tomar:

- **Tautología:** siempre es verdadera.
- **Contradicción:** siempre es falsa.
- **Contingencia:** puede ser verdadera o falsa dependiendo de los valores de las proposiciones que la componen.

Este tema se trata más en detalle en el apartado [Tablas de verdad](truth_tables.md).
