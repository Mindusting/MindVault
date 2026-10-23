---
aliases: [Predicados en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-21 07:07:04
headerFile: false
modificationDate: 2026-10-22 07:24:23
rating: 
tags: [Math]
---

# PREDICADOS

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

> [!seealso]- MIRA TAMBIÉN
> - [Proposiciones](propositions.md)
> - [Cuantificadores](quantifiers.md)
> - [Conectores lógicos](logical_connectives.md)
> - [Tablas de verdad](truth_tables.md)
> - [Reglas de inferencia](inference_rules.md)

Un predicado es una expresión matemática que representa una propiedad o relación cuyo valor de verdad depende de una o varias variables (*a estas se les llama "variables libres", ya que de primeras no están definidas*).

Cuando se asignan valores concretos a todas sus variables libres, el predicado da lugar a una [proposición](propositions.md), que puede ser verdadera o falsa.

Imaginemos que tenemos una [proposición](propositions.md) que indica si un número es mayor a $0$, pero no queremos que se especifique un número en concreto, sino que queremos que este se pueda especificar más adelante, para ello, podremos expresarlo mediante un predicado de la siguiente forma:

$$P(x): x > 0$$

^predicates-math-example

De esta manera podremos usar el **predicado** escribiendo lo siguiente:

$$P(3)$$

Dándonos como resultado **verdadero**, ya que sería como escribir:

$$3 > 0$$

> [!note] NOTA (para programadores)
> En programación el equivalente a los predicados serían las **funciones**:
> 
> ```python
> def P(x: int) -> bool:
>     return x > 0
> 
> P(3)
> ```
> 
> Dando `True` como resultado de la operación `P(3)`.
> 
> Y si usamos las funciones lambda de Python, se parece aún más a la [representación matemática que usamos en el ejemplo](#^predicates-math-example):
> 
> ```python
> P = lambda x: x > 0
> 
> P(3)
> ```

La principal diferencia entre un predicado abierto y una [proposición](propositions.md) es que ==el valor de verdad del predicado depende de sus **variables libres**==, mientras que una proposición tiene un valor de verdad definido.

Por tanto, un predicado abierto no es una proposición falsa ni incorrecta: es una expresión que puede dar lugar a distintas proposiciones cuando se asignan valores a sus variables.

Siguiendo con el [ejemplo de antes](#^predicates-math-example), si definimos la variable $x$ com $3$ el resultado es verdadero, sin embargo, si el valor de $x$ lo establecemos a $-2$, el resultado es falso.

$$
\begin{aligned}
P(3)&:   3 > 0 && \text{(Verdadero)}\\
P(-2)&: -2 > 0 && \text{(Falso)}
\end{aligned}
$$

## REPRESENTACIÓN Y NOTACIÓN

Los **predicados** se representan habitualmente mediante una letra mayúscula seguida de una o varias variables entre paréntesis separadas por comas, a estas variables en este contexto se les suele llamar **argumentos**:

$$P(x): x > 0$$

En este caso, el predicado se puede dividir en las siguientes partes:

- $P$: es el nombre del predicado.
- $x$: es el argumento (*o variable*).
- $x > 0$: es la condición que determina su valor de verdad.

### ARIDAD

La **aridad** es el número de argumentos que recibe un predicado.

Los predicados pueden clasificarse según su aridad:

- **Unarios:** reciben un argumento: $P(x)$.
- **Binarios:** reciben dos argumentos: $P(x,y)$.
- **Ternarios:** reciben tres argumentos: $P(x,y,z)$.

Por ejemplo, podemos definir un predicado binario:

$$P(x, y): x > y$$

## DOMINIO DEL DISCURSO

El **dominio del discurso** es el conjunto de elementos sobre los que se aplica un predicado y del que pueden tomar sus valores los argumentos.

Imaginemos que estamos trabajando con el siguiente predicado:

$$P(x): x^2 = 4$$

Si establecemos que el dominio del discurso son los **números naturales** ($\mathbb{N}$), el único valor que da como resultado vedadero es $2$, ya que $2^2$ es igual a $4$.

Sin embargo, si establecemos como dominio los **números enteros** ($\mathbb{Z}$), tanto el valor $2$ como $-2$ dan como resultado verdadero.

Por lo que si queremos especificar el dominio de un argumento tendremos que hacerlo de la siguiente forma:

$$P(x): x^2 = 4, x \in \mathbb{N}$$

De esta manera estamos indicando que $x$ pertenece al conjunto de los números naturales ($\mathbb{N}$). Esto significa que solamente podemos utilizar números naturales como argumentos del predicado.

Sin embargo, esto no implica que todos los valores del dominio satisfagan la condición. En este ejemplo, el único número natural que hace verdadero el predicado es $2$.

> [!important] IMPORTANTE
> El dominio del discurso no indica qué valor tiene una variable, sino **qué valores puede tomar**.
>
> Por ejemplo, si el dominio es $\mathbb{N}$, no podemos utilizar $P(-2)$ como una instancia válida del predicado, porque $-2 \notin \mathbb{N}$.

> [!note] NOTA (para programadores)
> Buscando un simil de esto último con la programación es como si a la hora de crear la función que representará el predicado, le añadiesemos una comprobación para lanzar una excepció cuando no pertenezca al grupo de valores esperados:
> 
> ```python
> def P(x: int) -> bool:
>     if type(x) is not x or x < 0:
>         raise ValueError("x debe ser un número natural")
>     return (x * x) == 4
> 
> P(2) # Su valor es True.
> P(3) # Su valor es False.
> 
> P(-2) # Lanza una excepción de ValueError.
> ```
> 
> Por lo que al añadir la comprobación, estamos especificando que en este caso $x$ debe pertenecer a los número naturales (*inclullendo el $0$*); y no es que de como resultado el valor `False` si $x$ es negativo, sino que da un error, ya que no pertenece al [conjunto](../set_theory.md) de los número naturales ($\mathbb{N}$).

---

El dominio del discurso no tiene por qué ser un [conjunto](../set_theory.md) numérico; también puede ser un [conjunto](../set_theory.md) de personas, objetos u otros elementos; por ejemplo, si nuestro dominio es el conjunto de animales, podemos definir:

$$P(x): \text{x es un mamífero}, x \in animales$$

En este caso, el predicado indica si un animal del dominio es un mamífero o no, por lo que no está relacionado con lo números.
