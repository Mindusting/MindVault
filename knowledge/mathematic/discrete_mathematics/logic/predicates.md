---
aliases: [Predicados en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-21 07:07:04
headerFile: false
modificationDate: 2026-11-15 05:11:43
rating: 
tags: [Math]
---

# PREDICADOS

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
> En programación el equivalente a los predicados serían las **funciones** que devuelven valores booleanos:
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

## DEL PREDICADO A LA PROPOSICIÓN

Un predicado funciona como una **plantilla de afirmaciones**. La expresión $P(x):x>0$ no afirma todavía que un número concreto sea positivo: declara una propiedad que podemos comprobar para distintos valores de $x$.

Se distinguen tres situaciones:

- **Predicado abierto:** $P(x): x > 0$; el resultado depende de $x$.
- **Instancia del predicado:** $P(4)$; sustituimos $x$ por $4$ y obtenemos la proposición $4 > 0$.
- **Proposición cuantificada:** $\forall x \in \mathbb N,\ x\ge0$; el cuantificador especifica que la propiedad se comprueba para **todos** los naturales.

> [!example] EJEMPLO PASO A PASO
> Definimos $P(x): x^2 = 9$ sobre el dominio $\mathbb Z$.
> 
> - $P(3)$ es verdadera porque $3^2 = 9$.
> - $P(-3)$ también es verdadera porque $(-3)^2 = 9$.
> - $P(4)$ es falsa porque $4^2 = 16 \ne 9$.
> - $\exists x \in \mathbb Z,\ P(x)$ es verdadera porque hay, al menos, un valor que funciona.
> - $\forall x \in \mathbb Z,\ P(x)$ es falsa porque $x = 0$ es un contraejemplo.

El dominio fija **qué sustituciones están permitidas**. Una entrada fuera del dominio no se clasifica como falsa por ese simple motivo; no corresponde a una instancia válida de ese predicado tal y como se ha definido.

## CONJUNTO DE VERDAD

El **conjunto de verdad** (o extensión) de un predicado unario es el subconjunto del dominio formado por los valores que hacen verdadera la propiedad.

> [!syntax] SINTAXIS
> 
> $$S_P = \{x \in D \mid P(x)\}$$
> 
> - $D$ es el dominio del predicado.
> - $P(x)$ es la condición.
> - $S_P$ reúne únicamente los elementos que la satisfacen.

Por ejemplo, si $D = \{-2, -1, 0, 1, 2, 3\}$ y $P(x): x^2 = 4$, entonces:

$$S_P = \{-2, 2\}$$

No debemos confundir el **dominio** con su **conjunto de verdad**: el dominio incluye todos los candidatos; el conjunto de verdad, solo las soluciones. Esta idea enlaza directamente con la [teoría de conjuntos](../set_theory.md).

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
- **Binarios:** reciben dos argumentos: $P(x, y)$.
- **Ternarios:** reciben tres argumentos: $P(x, y, z)$.

Por ejemplo, podemos definir un predicado binario:

$$P(x, y): x > y$$

## PREDICADOS DE VARIOS ARGUMENTOS

Un predicado puede describir una **relación** entre varios elementos. Si definimos $R(x, y): x < y$, necesitamos dos valores para obtener una proposición concreta: $R(2, 5)$ es verdadera y $R(5, 2)$ es falsa.

En general, si un predicado tiene $n$ argumentos, se le llama **predicado $n$-ario**. Sus argumentos no tienen por qué pertenecer al mismo dominio. Por ejemplo:

$$M(e, a): \text{"El estudiante }e\text{ está matriculado en }a\text{"}$$

Aquí $e$ puede pertenecer al conjunto de estudiantes y $a$ al conjunto de asignaturas. Si ambos conjuntos son finitos, podemos representar los pares que cumplen el predicado como una [relación binaria](../binary_relations.md).

> [!example] EJEMPLO
> Sean $E = \{\text{Ana}, \text{Luis}\}$ y $A = \{ \text{Álgebra}, \text{Física} \}$. Si Ana cursa ambas asignaturas y Luis solo Física, la extensión de $M$ es:
> 
> $$
> \{
> (\text{Ana}, \text{Álgebra}),
> (\text{Ana}, \text{Física}),
> (\text{Luis}, \text{Física})
> \}
> $$
> 
> Un predicado binario no es simplemente "dos condiciones": relaciona **dos posiciones** y el orden de los argumentos importa.

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

$$
A = \{
\text{gato},
\text{perro},
\text{hámster},
\text{pez}
\}
$$

Por lo que podemos obtener los siguientes resultados:

$$
\begin{aligned}
P(gato)&: Verdadero\\
P(pez)&: Falso
\end{aligned}
$$

## CUANTIFICACIÓN Y ALCANCE

Los [cuantificadores](quantifiers.md) permiten afirmar que una condición se cumple para todos los elementos de un dominio o para alguno de ellos. Su **alcance** es la parte de la fórmula sobre la que actúan; solo dentro de ese alcance quedan ligadas las variables correspondientes.

Comparemos, para $x, y \in \mathbb Z$:

$$\exists x \in \mathbb Z,\ x > y$$

La variable $x$ está ligada, pero $y$ continúa libre. La fórmula expresa una propiedad de $y$: "existe un entero mayor que $y$". En cambio:

$$\forall y \in \mathbb Z, \exists x \in \mathbb Z,\ x > y$$

Las dos variables están ligadas y la fórmula entera es una proposición verdadera.

> [!important] IMPORTANTE
> Cuando una misma letra aparece libre en una parte y ligada en otra, hay que respetar los paréntesis y el alcance de cada cuantificador. Renombrar una variable ligada sin alterar el significado se llama **renombrado de variables**; por ejemplo, $\forall x \,P(x)$ y $\forall t \,P(t)$ expresan lo mismo si el cambio es coherente y no captura otras variables.

## COMBINAR PREDICADOS

Los predicados pueden combinarse con los mismos [conectores lógicos](logical_connectives.md) que las proposiciones. Si $P(x)$ significa "$x$ es par" y $Q(x)$ "$x$ es mayor que $10$", entonces:

- $P(x) \land Q(x)$ significa "$x$ es par **y** mayor que $10$".
- $P(x) \lor Q(x)$ significa "$x$ es par **o** mayor que $10$ (o ambas)".
- $\neg P(x)$ significa "$x$ no es par", es decir, que es impar si $x \in \mathbb Z$.
- $P(x) \to Q(x)$ significa "si $x$ es par, entonces $x$ es mayor que $10$".

El conector no elimina la dependencia de $x$. Por ejemplo, $P(x) \land Q(x)$ continúa siendo un predicado abierto hasta que **fijamos $x$ o lo cuantificamos**.

> [!example] EJEMPLO CON DOMINIO FINITO
> Sea $D = \{8, 11, 12, 13\}$. El conjunto de verdad de $P(x) \land Q(x)$ es $\{12\}$, porque $12$ es el único elemento del dominio que es par y mayor que $10$.
> 
> En cambio, el conjunto de verdad de $P(x) \lor Q(x)$ es todo $D$: $8$ satisface la primera condición; $11$ y $13$, la segunda; $12$, ambas.

### PREDICADOS FRENTE A FUNCIONES NUMÉRICAS

Una función como $f(x) = x^2$ produce un **número**, mientras que un predicado como $P(x): x^2 > 9$ expresa una **propiedad**. Es habitual definir un predicado mediante una función, pero no son conceptos idénticos.

Por ejemplo, si $f: \mathbb Z \to \mathbb Z$ viene dada por $f(x) = x^2$, podemos definir $P(x): f(x) = 16$. El conjunto de verdad de $P$ es $\{-4, 4\}$. Para comprender la notación de predicados conviene pensar: "¿qué propiedad estamos verificando?" y "¿sobre qué dominio?".

## EJERCICIOS DE COMPROBACIÓN

1. Con $D = \{-1, 0, 1, 2\}$ y $P(x): x > 0$, calcula $S_P$.
2. Con $R(x, y): x + y = 5$, determina el valor de $R(2, 3)$ y de $R(2, 2)$.
3. Identifica las variables libres en $\forall x \in \mathbb N,\ x + y > 0$.

> [!abstract] SOLUCIONES
> 1. $S_P = \{1, 2\}$.
> 2. Verdadera y falsa, respectivamente.
> 3. $x$ está ligada por $\forall$; $y$ queda libre.

## VARIABLES LIBRES Y LIGADAS

- **Variable libre:** son aquellas variables que no está ligada por un [cuantificador](quantifiers.md).
^free-var-def
- **Variable ligada:** son aquellas variables que está bajo el alcance de un [cuantificador](quantifiers.md) ($\forall$, $\exists$).
^bound-var-def

Una expresión puede contener variables libres y ligadas simultáneamente.

> [!example] EJEMPLO: Variable libre
> En el siguiente predicado la variable $x$ es libre:
> 
> $$P(x): x > 3$$

> [!example] EJEMPLO: Variable ligada
> En la siguiente [proposición](propositions.md) la variable $x$ está ligada por $\forall$:
> 
> $$\forall x \in \mathbb{N}, \quad x > 3$$
> 
> En este caso la expresión es una [proposición](propositions.md) falsa; ya que no todos lo números naturales son mayores a $3$.

> [!example] EJEMPLO: Variable libre y ligada
> - $x$ está ligada.
> - $y$ está libre.
> 
> $$\exists x \in \mathbb{N}, \quad x > y$$
