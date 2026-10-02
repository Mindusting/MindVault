---
aliases: [Vectores]
author: Mindusting
corrected: false
creationDate: 2026-06-30 10:34:40
headerFile: false
modificationDate: 2026-09-30 01:49:17
rating: 
tags: [Math, Vector]
---

# VECTORES

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Reorganización de los apuntes, ya que como soy nuevo en este tema, no he empezado poniendo el contendido en el que corresponde.
> > 
> > ---
> > 
> > - [ ] DEFINICIÓN
> >     - Angulo $\theta$.
> > - [ ] REPRESENTACIÓN:
> >     - [ ] REPRESENTACIÓN EN MATEMÁTICAS
> >     - [ ] REPRESENTACIÓN EN FÍSICA
> >     - [ ] REPRESENTACIÓN EN PROGRAMACIÓN
> > - [ ] COMPONENTES DE UN VECTOR:
> >     - [ ] VECTORES DE DOS DIMENSIONES
> >     - [ ] VECTORES DE TRES DIMENSIONES
> >     - [ ] VECTORES DE MÚLTIPLES DIMENSIONES
> > - [ ] VECTOR NULO
> > - [ ] OPERACIONES BÁSICAS CON VECTORES
> >     - [ ] SUMA DE VECTORES
> >     - [ ] RESTA DE VECTORES
> >     - [ ] MULTIPLICACIÓN DE VECTORES
> >     - [ ] DIVISIÓN DE VECTORES
> > - [ ] MAGNITUD DE UN VECTOR
> > - [ ] DIRECCIÓN DE UN VECTOR
> > - [ ] RELACIONES TRIGONOMÉTRICAS:
> >     - [ ] SENO
> >         - $\sin{\theta} = \frac{v_y}{\lVert\vec{v}\rVert}$
> >     - [ ] COSENO
> >         - $\cos{\theta} = \frac{v_x}{\lVert\vec{v}\rVert}$
> >     - [ ] TANGENTE
> >         - $\tan{\theta} = \frac{v_y}{v_x}$
> > - [ ] NORMALIZACIÓN
> >     - Un vector normalizado se representa con $\hat{v}$.
> > - [ ] VECTOR UNITARIO
> > 
> > ---
> > 
> > - [ ] Explicar que es $\theta$ y como calcularlo.
> > - [x] Vectores nulos.
> > - [ ] Vectores unitarios.
> > - [ ] Componentes de un vector.
> > - [ ] Operaciones con vectores.
> >     - [ ] Magnitud de un vector.
> >     - [ ] Seno de un vector.
> >     - [ ] Coseno de un vector.
> >     - [ ] Tangente de un vector.
> >     - [ ] Producto escalar de un vector.
> > - [ ] Normalización de un vector $\hat{v}$.

> [!external-link]- REFERENCIAS WEB
> YouTube:
> 
> - [Math For Game Devs (2020)](https://www.youtube.com/playlist?list=PLImQaTpSAdsD88wprTConznD1OY1EfK_V) #WWW/YT/acegikmo
> - [Visual Explanations](https://www.youtube.com/playlist?list=PLImQaTpSAdsB0DF6JfqTTm0sFdLVa80HJ) #WWW/YT/acegikmo

> [!note] NOTA
> Si quieres una versión resumida/chuleta de estos apuntes, tienes el archivo [*vector_cheatsheet*](vector_cheatsheet.md).

## DEFINICIÓN

Un **vector** es un objeto matemático y físico definido por tres características: **dirección**, **magnitud** y **sentido**; este permite representar: un **puto en el espacio**, **fuerza**, **velocidad**, **aceleración**, entre otras cosas.

## REPRESENTACIÓN

Ya que el concepto de vector es una idea un tanto abstracta, esta se puede representar de diversas forman en base a nuestras necesidades: [matemática](#MATEMÁTICA), [física](#FÍSICA) y [programación](#PROGRAMACIÓN).

%%

Un **vector** es un conjunto de [escalares](scalar.md) (*tendiendo este dos o más [escalares](scalar.md)*); sirve para repesentar una posición, velocidad o fuerza, entre otros; este suele representarse de tres formas distintas, el cual escojas usar depederá fuertemente de en el ámbito en el que te muevas:

1. **Matemáticos**: estos suelen ver los vectores como una letra con una flecha sobre ella que apunta a la derecha ($\vec{v}$); estas se utilizan en funciónes.

$$
\begin{aligned}
\vec{a} &=
\begin{pmatrix}
1 & 2
\end{pmatrix}
\\
\vec{b} &=
\begin{pmatrix}
4 & -1
\end{pmatrix}
\\
\vec{c} &= \vec{a} + \vec{b}
\\
\vec{c} &\rightarrow
\begin{pmatrix}
5 & 1
\end{pmatrix}
\end{aligned}
$$

2. **Físicos**: estos suelen ver los vectores como una flecha con magnitud, dirección y sentido, esta permite indicar la posición (*respecto a un punto de origen*), una velocidad o fuerza aplicada sobre un elemento físico.
![#center](assets/vector_fisico.md)
3. **Programadores**: estos suelen ver los vectores como una lista ordenada de números (*[escalares](scalar.md)*), es decir, a la hora de trabajar con un vector de dos dimensiones, este sería una lista con dos número (*el número $x$ y el número $y$, estando estos siempre en este orden*).

```python
import numpy as np

a = np.array([1, 2])
b = np.array([4, -1])

c = a + b

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
# SALIDA:
# a = [1 2]
# b = [4 -1]
# c = [5 1]
```

En cualquier caso las tres formas de representar los **vectores** son eso mismo, una forma de representarlos, por lo que podemos una forma u otra en base a nuestra combeniencia.

%%

### MATEMÁTICA

En **matemáticas** un vector se suele representar con una **letra** que tiene una **flecha encima de ella** ($\vec{v}$), esta referencia a una **tupla** que contiene un conjunto de [**escalares**](scalar.md) (*número reales*):

$$\vec{v} = (3, 4)$$

### FÍSICA

En **física** un vector se suele representar como **una flecha** que apunta a un punto en el espacio; normalmente situando su origen en el origen del plano cartesiano, pero este puede estar en cualquier punto.

![#center](assets/vector_fisico.md)

### PROGRAMACIÓN

## COMPONENTES DE UN VECTOR

%%

Ya que un **vector** es en esecia un conjunto de [**escalares**](scalar.md), puede darse la situación en la que queramos tratar sobre uno de estos [**escalares**](scalar.md) en concreto, para ello tendremos que poder referenciar a cada uno de estos de forma independiente, esto se hace de las siguientes formas:

1. **Vector 2D:**
    Si tenemos un **vector** con dos dimensiones, se suele usar la $x$ para referirse al primer [**escalar**](scalar.md) y la $y$ para el segundo.

    $$\vec{v} = (v_x, v_y)$$

2. **Vector 3D:**
    Funciona igual que un **vector 2D** pero se añade la tercera dimensión, siendo esta referenciada con la letra $z$.

    $$\vec{v} = (v_x, v_y, v_z)$$

3. **Vector $n$D:**
    En el caso de estar tratando con **vectores** bien de **dos o más dimensiones** se puede usar un número para referirnos al componente; este es el método que se utiliza cuando el **vector** tiene más de tres dimensiones; ten en cuenta que se empieza a contar desde el $1$ hasta $n$.

    $$\vec{v} = (v_1, v_2, v_3,...)$$

^comp-nd

En caso de estar trabajando con varios **vectores** con el mismo nombre, tendremos que especificar a cual de ellos nos referimos y luego su componente:

$$\vec{v}_1 = (v_{1x}, v_{1y})$$

$$\vec{v}_2 = (v_{2x}, v_{2y})$$

$$\vec{v}_1 + \vec{v}_2 = (v_{1x} + v_{2x}, v_{1y} + v_{2y})$$

También se puede indicar el componente [mediante un número](#^comp-nd), pero esto puede ser confuso ya que si bien tenemos muchos vectores o componentes, podría llegar a ser ambiguo, por esto mismo, lo que se puede hacer es separar el identificador del vector y el del componente con una coma:

$$
\vec{v}_1 + \vec{v}_2 =
(v_{1,1} + v_{2,1}, v_{1,2} + v_{2,2})
$$

Esto tra otros problemas, ya que la coma en este caso también se usa para separar la suma de los componentes de ambos vectores, entonces, en el caso de que queramos ser aún más explícitos con a qué nos estamos refiriendo podemos seguir la siguiente sintaxis:

$$(\vec{v}_1)_x = (\vec{v}_1)_1$$

Aunque en este caso pueda quedar más sucio devido al incremento de paréntesis en la fórmula, el resultado es más explicito:

$$
\vec{v}_1 + \vec{v}_2 =
((\vec{v}_1)_1 + (\vec{v}_2)_1, (\vec{v}_1)_2 + (\vec{v}_2)_2)
$$

%%

### VECTORES DE DOS DIMENSIONES

### VECTORES DE TRES DIMENSIONES

### VECTORES DE MÚLTIPLES DIMENSIONES

## VECTORES NULOS

Un **vector nulo** es aquel cullos [**componentes**](#COMPONENTES%20DE%20UN%20VECTOR) están establecidos a cero, es decir, cuya [**magnitud**](#MAGNITUD%20DE%20UN%20VECTOR) sea cero (*su longitud es cero*).

$$\vec{vec\_nulo} = (0, 0)$$

$$\lVert \vec{vec\_nulo} \rVert = 0$$

## OPERACIONES BÁSICAS CON VECTORES

### SUMA DE VECTORES

### RESTA DE VECTORES

### MULTIPLICACIÓN DE VECTORES

### DIVISIÓN DE VECTORES

## MAGNITUD DE UN VECTOR

## DIRECCIÓN DE UN VECTOR

## RELACIONES TRIGONOMÉTRICAS

### SENO

### COSENO

### TANGENTE

## NORMALIZACIÓN

## VETOR UNITARIO

%%

---
---
---
---
---

## OPERACIONES CON VECTORES

### MAGNITUD DE UN VECTOR

La **magnitud** o **módulo** de un **vector** es la longitud de la flecha que representa dicho **vector**.

La representación de este valor se escribe poniendo una flecha sobre el **vector** y dos barras verticales a cada lado de este:

$$\lVert \vec{v} \rVert$$

Aunque bajo ciertos contextos también hay otras dos formas de representarlo: 1) poniendo una única barra vertical a cada lado del vector, 2) sin poner barras verticales ni la flecha sobre el vector (*siendo esta la menos usada*).

$$\lVert \vec{v} \rVert=|\vec{v}|=v$$

---

Para calcualr la **magnitud** de un **vector** tendremos que hallar la raiz cuadrada de la suma de los [componentes del vector](#COMPONENTES%20DE%20UN%20VECTOR) elevados al cudarado:

$$\lVert \vec{v} \rVert=\sqrt{v^2_1+v^2_2+v^2_3+...}$$

En el caso de un **vector** de dos dimensiones tendremos elevar al cuadrado los compoentes $x$ e $y$ para luego sumarlos y obtener su raiz cuadrada:

$$\lVert \vec{v} \rVert=\sqrt{v^2_x+v^2_y}$$

En donde $x=3$ e $y=4$:

$$\sqrt{3^2+4^2}$$

$$=\sqrt{9+16}$$

$$=\sqrt{25}$$

$$=5$$

Por lo que la **magnitud** del **vector** $\vec{v}=(3, 4)$ es $\lVert \vec{v} \rVert=5$.

![#center](assets/pitagoras.md)

^img-pitagoras

---

Si queremos implementar en código el cálculo de la **magnitud** podemos hacerlo de la siguiente forma (*lo he puesto en [Python](../../computer_science/programming/language/python/py.md) para que sea facil de enteder, pero este mismo concepto se puede aplicar en otros lenguajes de programación*):

```python
import math

def magnitude(vector) -> float:
    summation = 0
    for scalar in vector:
        summation += scalar * scalar
    return math.sqrt(summation)

vector = [3, 4]
print(magnitude(vector))
# SALIDA:
# 5.0
```

También podemos escribirlo de la siguiente forma:

```python
import math

def magnitude(vector) -> float:
    return math.sqrt(sum(map(lambda scalar: scalar*scalar, vector)))

vector = [3, 4]
print(magnitude(vector))
# SALIDA:
# 5.0
```

---

A la hora de trabajar sobre **vectores** con más de dos dimensiones la formula completa es la siguiente:

$$
\lVert \vec{v} \rVert =
\sqrt{v^2_1+(\sqrt{v^2_2+(\sqrt{v^2_3+...})^2})^2}
$$

Consiste en ir aplicando el [teorema de pitágoras](#^img-pitagoras) sobre cada par de [componente del vector](#COMPONENTES%20DE%20UN%20VECTOR) de forma recursiva; si te fijas este tiene un patrón que se repite:

$$(\sqrt{...})^2$$

Resulta que este patrón se puede obviar ya que $n=(\sqrt{n})^2$; por lo que simplificando la fórmula quitando esa parte obtenemos lo siguiente:

$$\lVert \vec{v} \rVert=\sqrt{v^2_1+v^2_2+v^2_3+...}$$

Esta es la fórmula que realmente se usa; me parece importante saber cual es la formula completa ya que nos puede dar una idea más profunda de como funciona.

### SENO, COSENO Y TANGENTE DE UN VECTOR

Para entender bien como calcular el [**seno**](#SENO%20DE%20UN%20VECTOR) y el [**coseno**](#COSENO%20DE%20UN%20VECTOR) de un vector, primero tenemos que entender en qué consiste la normalización de una lista de números; imaginemos que somos un profesor y hemos puesto un examen de tipo test a nuestros alunos, sabemos que el examen tenía 20 pregusta y que tenemos una lista de números en donde cada número representa la cantidad de preguntas correctas que escribio el aluno:

```python
numero_de_pregunta = 20
puntuaciones = [18, 7, 13]
# Hay tres alunos.
```

Para poder transformar estas puntuaciones en una nota de 0 a 10, perimero tenemos que normalizarlas, para ello, dividiremos cada puntuación (*número de respuestas correctas*) entre el total de preguntas:

```python
numero_de_pregunta = 20
puntuaciones = [18, 7, 13]

for i in range(len(puntuaciones)):
    puntuaciones[i] = puntuaciones[i] / numero_de_pregunta

print(puntuaciones)
# SALIDA:
# [0.9, 0.35, 0.65]
```

Al haber normalizado las `puntuaciones`, estas quedan en un número entre el `0.0` (*siendo esta la nota mínima que se puede obtener*) y el `1.0` (*siendo esta la nota máxima que se puede obtener*); una vez hecho esto podríamos multiplicar todas las puntuaciones por 10 para obtener la nota entre 0 y 10 (*como se suele puntuar en España*), pero para lo que estamos aprendiendo ahora no hace falta, ya que el punto es entender como podemos normalizar una serie de número para tranformarlos en un rango entre 0 y 1.

---

El **coseno** como el **seno** son los componentes $x$ e $y$ de un **vector** normalizados en un rango [$[-1, 1] \subset \mathbb{R}$](../temp/math_range_notation.md), para calcular estos dos valores primero tendremos que entender en qué consiste la normalización de un conjunto de números:

![#center](assets/cos_sin_30.md)

> [!important] IMPORTANTE
> Es importante saber que a la hora de calcular tanto el [**seno**](#SENO%20DE%20UN%20VECTOR), [**coseno**](#COSENO%20DE%20UN%20VECTOR) y [**tangente**](#TANGENTE%20DE%20UN%20VECTOR); no se puede usar un [**vector nulo**](#VECTORES%20NULOS), ya que como el cálculo de estos requieren de una división, implica que tendríamos que hacer una división entre 0.

#### SENO DE UN VECTOR

El **seno** de un vector consiste en la normalización de la componente $y$ sobre la [**magnitud**](#MAGNITUD%20DE%20UN%20VECTOR) del mismo:

$$\sin(\theta) = \frac{\vec{v}_y}{\lVert \vec{v} \rVert}$$

La parte en la que pone 

```python
import math

def magnitude(vector) -> float:
    summation = 0
    for scalar in vector:
        summation += scalar * scalar
    return math.sqrt(summation)

def sin(vector) -> float:
    return vector[1] / magnitude(vector)

vector = [3, 4]
print(sin(vector))
# SALIDA:
# 0.8
```

#### COSENO DE UN VECTOR

El **coseno** de un **vector** representa el componente $x$ normalizada en el rango 

```python
import math

def magnitude(vector) -> float:
    summation = 0
    for scalar in vector:
        summation += scalar * scalar
    return math.sqrt(summation)

def cos(vector) -> float:
    return vector[0] / magnitude(vector)

vector = [3, 4]
print(cos(vector))
# SALIDA:
# 0.6
```

#### TANGENTE DE UN VECTOR

```python
def tan(vector) -> float:
    return vector[1] / vector[0]

vector = [3, 4]
print(tan(vector))
# SALIDA:
# 1.3333333333333333
```

### PRODUCTO ESCALAR

El producto escalar (*dot product*)

$$\vec{v}_1 \cdot \vec{v}_2$$

la suma de las multiplicaciones de los pares de componentes de dos vectores

$$v_{1,x}$$

```python
def dot_product(v1, v2) -> float:
    assert len(v1) == len(v2), "Vectores incompatiples."
    result = 0
    for i in range(len(v1)):
        result += v1[i] * v2[i]
    return result
```

```python
def dot_product(v1, v2) -> float:
    assert len(v1) == len(v2), "Vectores incompatiples."
    return sum([v1[i] * v2[i] for i in range(len(v1))])
```

%%
