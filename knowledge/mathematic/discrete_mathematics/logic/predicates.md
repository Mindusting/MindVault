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

Un predicado es una expresión matemática que representa una propiedad o relación cuyo valor de verdad depende de una o varias variables.

Cuando se asignan valores concretos a todas sus variables libres, el predicado da lugar a una [proposición](propositions.md), que puede ser verdadera o falsa.

Imaginemos que queremos representar la propiedad de si un número es mayor que $0$, pero sin especificar inicialmente de qué número se trata; para ello, podemos definir un predicado que reciba ese número ($x$) como argumento:

$$P(x): x > 0$$

^predicates-math-example

De esta manera podremos usar el **predicado** escribiendo lo siguiente:

$$P(3)$$

Dándonos como resultado **verdadero**, ya que sería como escribir:

$$3 > 0$$

> [!note] NOTA (para programadores)
> En programación el equivalente a los predicados serían las **funciones** que devuelven valroes booleanos:
> 
> ```python
> def P(x: int) -> bool:
>     return x > 0
> 
> print(P(3))
> # SALIDA:
> # True
> ```
> 
> Dando `True` como resultado de la operación `P(3)`.
> 
> Y si usamos las funciones lambda de Python, se parece aún más a la [representación matemática que usamos en el ejemplo](#^predicates-math-example):
> 
> ```python
> P = lambda x: x > 0
> 
> print(P(3))
> # SALIDA:
> # True
> ```

La principal diferencia entre un predicado abierto y una [proposición](propositions.md) es que ==el valor de verdad del predicado depende de sus **variables libres**==, mientras que una proposición tiene un valor de verdad definido.

Por tanto, un predicado abierto no es una proposición falsa ni incorrecta: es una expresión que puede dar lugar a distintas proposiciones cuando se asignan valores a sus variables.

Siguiendo con el [ejemplo de antes](#^predicates-math-example), si asignamos a la variable $x$ el valor $3$ el resultado es verdadero, sin embargo, si el valor de $x$ lo establecemos a $-2$, el resultado es falso.

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

Si establecemos que el dominio del discurso son los **números naturales** ($\mathbb{N}$), el único valor que da como resultado verdadero es $2$, ya que $2^2$ es igual a $4$.

Sin embargo, si establecemos como dominio los **números enteros** ($\mathbb{Z}$), tanto el valor $2$ como $-2$ dan como resultado verdadero.

Podemos indicar el dominio de una variable especificando el conjunto al que pertenece mediante el símbolo de pertenencia ($\in$):

$$P(x): x^2 = 4, x \in \mathbb{N}$$

De esta manera estamos indicando que $x$ pertenece al conjunto de los números naturales ($\mathbb{N}$). Esto significa que solamente podemos utilizar números naturales como argumentos del predicado.

Sin embargo, esto no implica que todos los valores del dominio satisfagan la condición. En este ejemplo, el único número natural que hace verdadero el predicado es $2$.

> [!important] IMPORTANTE
> El dominio del discurso no indica qué valor tiene una variable, sino **qué valores puede tomar**.
>
> Por ejemplo, si el dominio es $\mathbb{N}$, no podemos utilizar $P(-2)$ como una instancia válida del predicado, porque $-2 \notin \mathbb{N}$.

> [!note] NOTA (para programadores)
> Buscando un símil de esto último con la programación es como si a la hora de crear la función que representará el predicado, le añadiésemos una comprobación para lanzar una excepción cuando no pertenezca al grupo de valores esperados:
> 
> ```python
> def P(x: int) -> bool:
>     if type(x) is not int or x < 0:
>         raise ValueError("x debe ser un número natural")
>     return (x * x) == 4
> 
> print(P(2))
> # SALIDA:
> # True
> 
> print(P(3))
> # SALIDA:
> # False
> 
> print(P(-2)) # Lanza una excepción de ValueError.
> ```
> 
> Por lo que al añadir la comprobación, estamos especificando que en este caso $x$ debe pertenecer a los números naturales (*incluyendo el $0$*); y no es que dé como resultado el valor `False` si $x$ es negativo, sino que da un error, ya que no pertenece al [conjunto](../set_theory.md) de los números naturales ($\mathbb{N}$).

---

El dominio del discurso no tiene por qué ser un [conjunto](../set_theory.md) numérico; también puede ser un [conjunto](../set_theory.md) de personas, objetos u otros elementos; por ejemplo, si nuestro dominio es el [conjunto](../set_theory.md) de animales ($A$), podemos definir:

$$P(x): \text{x es un mamífero}, x \in A$$

En donde animales es:

$$A=\{\text{gato},\text{perro},\text{hámster},\text{pez}\}$$

Por lo que podemos obtener los siguientes resultados:

$$
\begin{aligned}
P(gato)&: Verdadero\\
P(pez)&: Falso
\end{aligned}
$$
