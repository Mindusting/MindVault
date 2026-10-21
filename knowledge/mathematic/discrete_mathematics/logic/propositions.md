---
aliases: [Proposiciones en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-21 06:50:39
headerFile: false
modificationDate: 2026-10-21 06:55:47
rating: 
tags: [Math]
---

# PROPOSICIONES

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

> [!seealso]- MIRA TAMBIÉN
> - [Predicados](predicates.md)
> - [Cuantificadores](quantifiers.md)
> - [Conectores lógicos](logical_connectives.md)
> - [Tablas de la verdad](truth_tables.md)
> - [Reglas de inferencia](inference_rules.md)

Una **proposición** es un ==enunciado declarativo== al que se le puede asignar un ==valor de verdad==; es decir, **verdadero** o **falso**; pero ==no ambos de forma simultánea==.

Una **proposición** ==no necesita ser **verdadera**== para considerarse una **proposición**, únicamente debe tener un valor de verdad definido.

> [!success] QUÉ SÍ SON PROPOSICIONES
> - $5 > 3$:
>     Sí es una proposición ya que es una aformación y sabemos sin duda que su valor es verdadero.
> - $5 < 3$:
>     Sí es una proposición ya que es una aformación y sabemos sin duda que su valor es falso.
> - Existen infinitos números primos:
>     Sí es una proposición ya que esta tiene un valor de verdad, siendo esta **verdadera**.

> [!failure] QUÉ SÍ SON PROPOSICIONES
> - $x > 3$:
>     No es una proposición ya que el valor $x$ no está definido, por lo que no podemos determinar su valor de verdad.
> - ¿Cuánto es $5 + 3$?:
>     No es una proposición ya que es una pregunta.
> - Calcula $5 + 3$:
>     No es una proposición ya que es una orden.

> [!note] NOTA (para programadores)
> Si bienes de la rama de la programación, una proposición podría ser una comparación de dos valores fijos:
> 
> - `5 == 3` es falsa.
> - `5 != 3` es verdadera.
> - `5 < 3` es falsa.
> - `5 > 3` es verdadera.
> 
> Todas estas operaciones de comparación con valores definidos (*es decir, que no son variables*) son las que en el ámbito de las matemáticas se les llama **proposiciones**.

## PROPOSICIONES COMO LETRAS

Las proposiciones pueden estar representadas mediante letras, esto permite su reutilización, estas letras sueles ser en mayúsculas o en minúsculas: $p, q, r...$; como por ejemplo:

$$
p: 5 > 3\\
q: 4 < 10
$$

De forma que ahora $p$ tiene el valor **verdadero**, mientras que $q$ tiene el valor **falso**.

> [!note] NOTA (para programadores)
> En programación, esto sería el equivalente a usar variables para guardar los valores booleanos:
> 
> ```python
> p = 5 > 3
> q = 4 < 10
> ```
> 
> De forma que allá donde usemos las poroposiciones representadas como una letra tendremos acceso a su valor.

## PROPOSICIONES COMPUESTAS

Para poder crear proposiciones compuestas, tendremos que hacer uso de las [**conexiones lógicas**](logical_connectives.md), permitiendo así concatenar múltiples proposiciones.


$$5 > 3 \land 4 < 10$$

Esta expresión se lee de la siguiente forma: $5$ es mayor que $3$ y $4$ es menor que $10$; concatenando así las dos proposiciones con el operador "y".

También podemos usar las proposiciones representadas en forma de letas:

$$
p: 5 > 3\\
q: 4 < 10\\
\\
p \land q
$$

> [!note] NOTA (para programadores)
> Las proposicones compuestas es como cuando usamos operadores booleanos entre comparaciones:
> 
> ```python
> 5 > 3 and 4 < 10
> ```
> 
> En este caso podemos ver que se usa el operador `and`, este indica que se debe cumplir la proposición de la izquierda (`5 > 3`) y la de la derecha (`4 < 10`) para que la proposición compuesta se cumpla.
> 
> Y siguiendo con el ejemplo de antes, también se podría expresar de la siguiente forma:
> 
> ```python
> p = 5 > 3
> q = 4 < 10
> 
> p and q
> ```
