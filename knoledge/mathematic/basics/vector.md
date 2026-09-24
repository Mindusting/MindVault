---
aliases: [Vectores en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-06-30 10:34:40
headerFile: false
modificationDate: 2026-09-25 12:55:29
rating: 
tags: [Math]
---

# VECTORES EN MATEMÁTICAS

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

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

## COMPONENTES DE UN VECTOR

## OPERACIONES CON VECTORES

### MAGNITUD DE UN VECTOR

La **magnitud** o **módulo** de un **vector** es la longitud de la flecha que representa dicho **vector**.

La representación de este valor se escribe poniendo una flecha sobre el **vector** y dos barras verticales a cada lado de este:

$$
\lVert \vec{v} \rVert
$$

Aunque bajo ciertos contextos también hay otras dos formas de representarlo: 1) poniendo una única barra vertical a cada lado del vector, 2) sin poner barras verticales ni la flecha sobre el vector (*siendo esta la menos usada*).

$$
\lVert \vec{v} \rVert=|\vec{v}|=v
$$

---

Para calcualr la **magnitud** de un **vector** tendremos que hallar la raiz cuadrada de la suma de los [componentes del vector](#COMPONENTES%20DE%20UN%20VECTOR) elevados al cudarado:

$$
\lVert \vec{v} \rVert=\sqrt{v^2_1+v^2_2+v^2_3+...}
$$

En el caso de un **vector** de dos dimensiones tendremos elevar al cuadrado los compoentes $x$ e $y$ para luego sumarlos y obtener su raiz cuadrada:

$$
\lVert \vec{v} \rVert=\sqrt{v^2_x+v^2_y}
$$

En donde $x=3$ e $y=4$:

$$
\sqrt{3^2+4^2}
$$

$$
=\sqrt{9+16}
$$

$$
=\sqrt{25}
$$

$$
=5
$$

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
\lVert \vec{v} \rVert=
\sqrt{v^2_1+(\sqrt{v^2_2+(\sqrt{v^2_3+...})^2})^2}
$$

Consiste en ir aplicando el [teorema de pitágoras](#^img-pitagoras) sobre cada par de [componente del vector](#COMPONENTES%20DE%20UN%20VECTOR) de forma recursiva; si te fijas este tiene un patrón que se repite:

$$
(\sqrt{...})^2
$$

Resulta que este patrón se puede obviar ya que $n=(\sqrt{n})^2$; por lo que simplificando la fórmula quitando esa parte obtenemos lo siguiente:

$$
\lVert \vec{v} \rVert=\sqrt{v^2_1+v^2_2+v^2_3+...}
$$

Esta es la fórmula que realmente se usa; me parece importante saber cual es la formula completa ya que nos puede dar una idea más profunda de como funciona.

### COSENO Y SENO DE UN VECTOR

El **coseno** como el **seno** son los componentes $x$ e $y$ de un **vector** normalizados en un rango [$[-1, 1] \subset \mathbb{R}$](../temp/math_range_notation.md), para calcular estos dos valores primero tendremos que entender en qué consiste la normalización de un conjunto de números:

> [!example] EJEMPLO
> #TODO: Explicar como normalizar una lista de números; para luego explicar como se normaliza el vector y así obtener el seno y coseno.

![#center](assets/cos_sin_30.md)

El **coseno** de un **vector** representa el componente $x$ normalizada en el rango 

### TANGENTE DE UN VECTOR

### PRODUCTO ESCALAR

El producto escalar (*dot product*)

$$
\vec{v}_1 \cdot \vec{v}_2
$$

la suma de las multiplicaciones de los pares de componentes de dos vectores

$$
v_{1,x}
$$

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
