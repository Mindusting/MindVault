---
aliases: [Proposiciones en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-21 06:50:39
headerFile: false
modificationDate: 2026-11-15 05:21:08
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

## CÓMO RECONOCER UNA PROPOSICIÓN

Para decidir si una frase es una proposición, no debemos preguntarnos si estamos de acuerdo con ella, sino **si afirma algo que puede ser verdadero o falso**. En lógica clásica se presupone que cada proposición posee un único valor de verdad, aunque las personas no sepamos cuál es.

Por ejemplo, "El número de estrellas de nuestra galaxia es par" es una proposición: afirma un hecho que será verdadero o falso, aunque no conozcamos su valor. En cambio, "¡Qué bonito es este número!" es un juicio subjetivo cuyo significado no está suficientemente fijado para tratarlo directamente como una proposición matemática.

Para clasificar un enunciado conviene seguir estos pasos:

1. **Identificar la modalidad:** ¿es una afirmación, una pregunta, una orden o una exclamación?
2. **Comprobar si tiene variables libres:** si decimos "$x$ es par", todavía no hemos fijado de qué $x$ hablamos.
3. **Precisar el contexto:** "Hoy llueve" puede ser una proposición cuando están fijados el lugar, el día y el significado de "llueve".
4. **Separar verdad y conocimiento:** no saber si una frase es verdadera no significa que carezca de valor de verdad.

> [!example] EJEMPLO RESUELTO
> Consideremos "Existe un número primo mayor que $100$".
> 
> - Es una afirmación, no una pregunta.
> - La variable que podría usarse para representar el número queda vinculada por "existe".
> - Tiene valor de verdad: **verdadero**, porque $101$ es primo y $101 > 100$.
> 
> La frase "$x$ es primo y $x > 100$", sin indicar $x$, es un **predicado abierto**, no una proposición cerrada.

## VERDAD, FALSABILIDAD Y VALIDEZ

Tres conceptos relacionados no significan lo mismo:

- **Valor de verdad:** describe si una proposición concreta es verdadera o falsa.
- **Satisfacibilidad:** una fórmula con variables proposicionales es satisfacible si existe alguna asignación de valores que la haga verdadera.
- **Validez lógica o tautología:** una fórmula es válida si resulta verdadera con **todas** las asignaciones posibles.

Por ejemplo, $p \land q$ es satisfacible: basta con que $p$ y $q$ sean verdaderas. Sin embargo, **no es una tautología**, porque falla cuando cualquiera de ellas es falsa. En cambio, $p \lor \neg p$ es verdadera para cualquier valor de $p$.

Esto explica una distinción importante: la proposición "$2+2=4$" es verdadera, pero hablar de "tautología" resulta más apropiado al estudiar una **forma lógica**, como $p \lor \neg p$, que no depende del contenido de $p$.

> [!note] NOTA
> En las demostraciones también se habla de **argumentos válidos**. Un argumento es válido cuando no existe un caso en el que todas sus premisas sean verdaderas y su conclusión falsa. "Válido" no significa que las premisas sean verdaderas de hecho.

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

## LENGUAJE NATURAL Y FORMALIZACIÓN

La lógica utiliza símbolos porque las frases cotidianas pueden ser ambiguas. Formalizar significa **elegir proposiciones simples y representar cómo se combinan**, sin cambiar su significado.

> [!example] EJEMPLO PASO A PASO
> Frase: "Si estudio y practico, entonces apruebo".
> 
> Definimos:
> 
>$$
>\begin{aligned}
>p&: \text{Estudio}\\
>q&: \text{Practico}\\
>r&: \text{Apruebo}
>\end{aligned}
>$$
> 
> La parte "estudio y practico" necesita una conjunción: $p \land q$. La expresión "si..., entonces..." introduce un condicional. Por tanto, la formalización completa es:
> 
> $$(p \land q) \to r$$
> 
> No sería correcto escribir $p \land (q \to r)$: esa fórmula dice algo distinto, porque condiciona solo el efecto de "practicar".

> [!important] IMPORTANTE
> Las letras $p$, $q$ y $r$ representan **afirmaciones completas**, no números ni valores booleanos almacenados. El valor de verdad es una propiedad de esas afirmaciones. Los paréntesis muestran qué partes de la fórmula se evalúan juntas.

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
\begin{aligned}
p &: 10 = 10\\
&\neg p
\end{aligned}
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

## FORMAS LÓGICAS Y ASIGNACIONES

Cuando una fórmula contiene variables proposicionales, como $p \land q$, podemos estudiarla sin decidir qué frases concretas significan $p$ y $q$. Una **asignación de verdad** consiste en dar a cada letra el valor V o F. Para dos letras existen cuatro asignaciones diferentes.

La misma fórmula puede representar "$3 > 1$ y $5 > 2$" (verdadera) o "$3 > 1$ y $5 < 2$" (*falsa*). Su estructura es la misma: $p \land q$. Lo que cambia es la asignación de valores de verdad de las proposiciones que hemos elegido.

Esta separación entre **contenido** y **estructura** permite que una [tabla de verdad](truth_tables.md) sirva para analizar infinitas frases concretas que comparten una misma forma lógica.

## EJERCICIOS DE COMPROBACIÓN

1. Clasifica: "$7$ es un número primo", "¿$7$ es primo?", "$x + 2 = 5$" y "Existe un entero que, al sumarle $2$, da $5$".
2. Formaliza "No estudio, pero practico" con $p$: "estudio" y $q$: "practico".
3. Explica por qué $p \lor \neg p$ es una tautología, pero $p \lor q$ no lo es.

> [!abstract] SOLUCIONES
> 1. Proposición verdadera; pregunta; predicado abierto; proposición verdadera (el entero es $3$).
> 2. $\neg p \land q$. En lógica, "pero" suele comportarse como "y" para el cálculo de verdad.
> 3. Si $p$ es verdadera, vale la primera parte; si es falsa, vale $\neg p$. En $p \lor q$ pueden ser falsas ambas.

## CLASIFICACIÓN SEGÚN EL VALOR DE VERDAD

Las [proposiciones compuestas](#PROPOSICIONES%20COMPUESTAS) pueden clasificarse en tres categorías según los valores de verdad que pueden tomar:

- **Tautología:** siempre es verdadera.
- **Contradicción:** siempre es falsa.
- **Contingencia:** puede ser verdadera o falsa dependiendo de los valores de las proposiciones que la componen.

Este tema se trata más en detalle en el apartado [Tablas de verdad](truth_tables.md).
