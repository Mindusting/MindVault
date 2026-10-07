---
aliases: [Vectores]
author: Mindusting
corrected: false
creationDate: 2026-06-30 10:34:40
headerFile: false
modificationDate: 2026-10-07 03:07:29
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
> > - [x] REPRESENTACIÓN:
> >     - [x] REPRESENTACIÓN EN MATEMÁTICAS
> >     - [x] REPRESENTACIÓN EN FÍSICA
> >     - [x] REPRESENTACIÓN EN PROGRAMACIÓN
> > - [x] COMPONENTES DE UN VECTOR:
> >     - [x] VECTORES DE DOS DIMENSIONES
> >     - [x] VECTORES DE TRES DIMENSIONES
> >     - [x] VECTORES DE MÚLTIPLES DIMENSIONES
> > - [x] VECTOR NULO
> > - [ ] OPERACIONES BÁSICAS CON VECTORES
> >     - [x] SUMA DE VECTORES
> >     - [x] RESTA DE VECTORES
> >     - [ ] MULTIPLICACIÓN DE VECTORES
> >     - [ ] DIVISIÓN DE VECTORES
> > - [x] MAGNITUD DE UN VECTOR
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
> >     - Si la magnitud del vector, sin importar si esta es mayor o menor a 1, tras normalizarlo esta termina siendo igual a 1.
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
> 1. Si quieres una versión resumida/chuleta de estos apuntes, tienes el archivo [*vector_cheatsheet*](vector_cheatsheet.md).
> 2. En algunos de los ejemplo de código de este documento se usa la clase `Vector2`, esta no es una clase propia de [**Python**](../../computer_science/programming/language/python/py.md), sino que la he escrito a mano, si quieres ver su código fuente para enterder como funciona, la tienes en el apartado [Vector 2D en  Python](#VECTOR%202D%20EN%20PYTHON); no es necesario entender el código para estos apuntes, ya que estos están más orientados a el manejo de vectores en general, pero por si te interesa, ahí lo tienes.

## DEFINICIÓN

Un **vector** es un objeto matemático y físico definido por tres características: **dirección**, **magnitud** y **sentido**; este permite representar: un **puto en el espacio**, **fuerza**, **velocidad**, **aceleración**, entre otras cosas.

## REPRESENTACIÓN

Ya que el concepto de vector es una idea un tanto abstracta, esta se puede representar de diversas forman en base a nuestras necesidades: [matemática](#MATEMÁTICA), [física](#FÍSICA) y [programación](#PROGRAMACIÓN); anuque todas ellas tiene algo en común y es que un vector es un **conjunto de [escalares](scalar.md) ordenados**.

### MATEMÁTICA

En **matemáticas** un vector se suele representar con una **letra** que tiene una **flecha encima de ella** ($\vec{v}$), esta referencia a una **tupla** que contiene un conjunto de [**escalares**](scalar.md) (*número reales*):

$$\vec{v} = (3, 4)$$

### FÍSICA

En **física** un vector se suele representar como **una flecha** que apunta a un punto en el espacio; normalmente situando su origen en el origen del plano cartesiano, pero este puede estar en cualquier punto.

![#center](assets/vector_fisico.md)

### PROGRAMACIÓN

En **programación** un vector es suele representar con un [*array*](../../computer_science/programming/fundamentals/basics/array.md) con números, también se puede representar con una [clase](../../computer_science/programming/fundamentals/basics/oop.md) para añadir neveles de abstracción y encapsulación, pero lo mínimo que se necesita es un [*array*](../../computer_science/programming/fundamentals/basics/array.md) con números.

```python
vector = [3, 4]

print(vector)
# SALIDA:
# [3, 4]
```

## COMPONENTES DE UN VECTOR

Los componentes de un **vector** son los [**escalares**](scalar.md) que lo componen, por lo que tenemos diferentes formas de indicar a cual de ellos nos estamos refiriendo.

%%

Ya que un **vector** es en esecia un **conjunto de [escalares](scalar.md) ordenados**, tenemos que tener una forma de referenciar cada uno de estos [**escalares**](scalar.md) de forma individual.

puede darse la situación en la que queramos tratar sobre uno de estos [**escalares**](scalar.md) en concreto, para ello tendremos que poder referenciar a cada uno de estos de forma independiente, esto se hace de las siguientes formas:

%%

Cabe resaltar que cuando se le quiere dar color a cada uno de los componentes de un vector, estos tienen la regla ***RGB*** (*rojo, verde, azul*); veremos unos ejemplos de esto en los siguientes apartados.

%%

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

Los vectores de dos dimensiones son aquellos que contienen dos [**escalares**](scalar.md); al primero de ellos se le llama $x$, es de color rojo y representa el eje horizontal; al segundo de ellos se le llama $y$, es de color verde y representa el eje vertical.

Teniendo el siguiente vector:

$$\vec{v} = (3, 4)$$

Podemos decir que $x$ es igual a $3$ e $y$ es igual a 4, pero para poder indicar dentro de una fórmula mate mática que queremos referenciar a uno de estos se hace escribiendo el vector sin la flecha de arriba seguido de el nombre del componente, escrto en pequeño a su izquierda, siendo en este caso:

$$\vec{v} = (v_x, v_y)$$

---

Si estuviesemos trabajando sobre varios vectores y quisieramos indicar a cual de ellos nos estamos refiriendo, podemos hacerlo escribiendo un número pequeño abajo a la derecha del vector:

$$
\vec{v}_1 = (v_{1x}, v_{1y})\\
\vec{v}_2 = (v_{2x}, v_{2y})\\
...
$$

Esta forma de definir el vector y luego su componente puede llegar a ser un poco confusa sobre todo, como veremos más adelante, cuando estemos referenciando [los componentes mediante números](#COMPONENTES%20MEDIANTE%20NÚMEROS); por lo que una forma que bajo ciertos contextos puede ser más explícita es separando el número del vector y el identificador del componente con una coma:

$$
\vec{v}_1 = (v_{1,x}, v_{1,y})\\
\vec{v}_2 = (v_{2,x}, v_{2,y})\\
...
$$

Aunque en este caso en concreto puede llegar a hacer que sea más confuso.

Otra forma de hacerlo ahún más explícito es encapsulando el vector entre paréntesis para luego indicar el identificador:

$$
\vec{v}_1 = ((v_1)_x, (v_1)_y)\\
\vec{v}_2 = ((v_2)_x, (v_2)_y)\\
...
$$

### VECTORES DE TRES DIMENSIONES

Los vectores de tres dimensiones son aquellos que contienen tres [**escalares**](scalar.md); los dos primeros funcionan igual que con los [vectores de dos dimensiones](#VECTORES%20DE%20DOS%20DIMENSIONES); el tercer componente se le llama $z$, es de color azul y representa el eje de la profundidad.

Teniendo el siguinte vector:

$$\vec{v} = (3, 4, 5)$$

Podemos decir que $x$ es igual a $3$, $y$ es igual a 4 y $z$ es igual a $5$; la identificación de estos tres componentes se comporta de la misma forma que con los [vectores de dos dimensiones](#VECTORES%20DE%20DOS%20DIMENSIONES):

$$\vec{v} = (v_x, v_y, v_z)$$

---

Y si estamos trabajando sobre varios vectores de tres dimensiones, al igual que con los de dos, podemos escribirlo de las siguientes formas:

$$
\vec{v}_1 = (v_{1x}, v_{1y}, v_{1z})\\
\vec{v}_2 = (v_{2x}, v_{2y}, v_{2z})\\
...
$$

$$
\vec{v}_1 = (v_{1,x}, v_{1,y}, v_{1,z})\\
\vec{v}_2 = (v_{2,x}, v_{2,y}, v_{2,z})\\
...
$$

$$
\vec{v}_1 = ((v_1)_x, (v_1)_y, (v_1)_z)\\
\vec{v}_2 = ((v_2)_x, (v_2)_y, (v_2)_z)\\
...
$$

### COMPONENTES MEDIANTE NÚMEROS

Otra forma de identificar los componentes es mediante números, este funciona bien cuando trabajamos con vectores con más de tres dimensiones; aunque también se puede usar con vectores tanto de dos como tres dimensiones; en donde el $1$ equivale a $x$, el $2$ equivale a $y$, el $3$ equivale a $z$ y el resto de números identifican más disensiones del vector aunque no tengan una letra asignada; de forma que podríamos hacer un vector de 4 dimesiones (*o más*):

$$\vec{v} = (v_1, v_2, v_3, v_4)$$

$$
v_x = v_1\\
v_y = v_2\\
v_z = v_3
$$

Cuando trabajamos con varios vectores podemos identificar cada uno de los vectores de la misma forma que hemos visto en los apartados anteriores, y aquí es donde podemos ver como la primera forma trae probemas, ya que es dificil de identificar donde empieza y termina el identificador de vector y el identificador del componente, sore todo en el momento en el que uno de ellos llega a los dos dígitos:

$$
\vec{v}_1 = (v_{11}, v_{12}, v_{13})\\
\vec{v}_2 = (v_{21}, v_{22}, v_{23})\\
...
$$

Es por esto, que en estos casos es mejor usar una de las dos siguientes formas para marcar una separación:

$$
\vec{v}_1 = (v_{1,1}, v_{1,2}, v_{1,3})\\
\vec{v}_2 = (v_{2,1}, v_{2,2}, v_{2,3})\\
...
$$

$$
\vec{v}_1 = ((v_1)_1, (v_1)_2, (v_1)_3)\\
\vec{v}_2 = ((v_2)_1, (v_2)_2, (v_2)_3)\\
...
$$

## VECTORES NULOS

Un **vector nulo** es aquel cullos [**componentes**](#COMPONENTES%20DE%20UN%20VECTOR) están establecidos a cero, es decir, cuya [**magnitud**](#MAGNITUD%20DE%20UN%20VECTOR) sea cero (*su longitud es cero*):

$$
\vec{vec\_nulo} = (0, 0)\\
\lVert \vec{vec\_nulo} \rVert = 0
$$

Al trabajar con vectores se suele revisar si alguno de estos es nulo ya que hay ciertas operaciones (*como veremos más adelante*) que no se puede efectuar sobre vectores nulos; al igual que, por ejemplo, no se puede hacer una disivión entre $0$.

## OPERACIONES BÁSICAS CON VECTORES

Para poder realizar operciones básicas entre vectores estos tienen que tener el mismo número de dimensiones.

### SUMA DE VECTORES

Para sumar dos vectores se debe sumar cada uno de los [componetes](#COMPONENTES%20DE%20UN%20VECTOR) de ambos vectores con sus pares; es decir: se susman los primeros [componetes](#COMPONENTES%20DE%20UN%20VECTOR) de ambos vectores, el resulado de esta suma se establece como el primer [componete](#COMPONENTES%20DE%20UN%20VECTOR) del vector sesultate, lo mismo se hace con el segundo y así asta completar el vector.

---

Veamos un ejemplo en donde sumamos los vectores $\vec{a}$ y $\vec{b}$ para obtener como resultado el vector $\vec{r}$:

$$
\vec{a} = (3, 4)\\
\vec{b} = (-4, 1)
$$

$$
\vec{a} + \vec{b} =\\
(3, 4) + (-4, 1) =\\
(3 + (-4), 4 + 1) =\\
(-1, 5)
$$

$$\vec{r} = (-1, 5)$$

El resultado de esta suma es que el vector $\vec{r}$ tiene como resultado $(-1, 5)$.

```python
a = Vector2( 3, 4)
b = Vector2(-4, 1)

r = a + b

print(r)
# SALIDA:
# Vector2(-1, 5)
```

### RESTA DE VECTORES

La resta de dos vectores si gue exáctamente el mismo procedimiento que la suma de estos, con la diferencia que en esta en vez de sumar los [componentes](#COMPONENTES%20DE%20UN%20VECTOR), se restan.

---

Veamos un ejemplo en donde restamos los vectores $\vec{a}$ y $\vec{b}$ para obtener como resultado el vector $\vec{r}$:

$$
\vec{a} = (3, 4)\\
\vec{b} = (-4, 1)
$$

$$
\vec{a} - \vec{b} =\\
(3, 4) - (-4, 1) =\\
(3 - (-4), 4 - 1) =\\
(7, 3)
$$

$$\vec{r} = (7, 3)$$

El resultado de esta resta es que el vector $\vec{r}$ tiene como resultado $(7, 3)$.

```python
a = Vector2( 3, 4)
b = Vector2(-4, 1)

r = a - b

print(r)
# SALIDA:
# Vector2(7, 3)
```

### MULTIPLICACIÓN DE VECTORES

### DIVISIÓN DE VECTORES

## MAGNITUD DE UN VECTOR

La **magnitud**, **módulo** o **longitud** (*este último en el sentido matemático y no en el de la programación*) de un **vector** es la longitud de la flecha que representa dicho **vector**.

La representación de este valor se escribe poniendo una flecha sobre el **vector** y dos barras verticales a cada lado de este:

$$\lVert \vec{v} \rVert$$

Aunque bajo ciertos contextos también hay otras dos formas de representarlo: 1) poniendo una única barra vertical a cada lado del vector, 2) sin poner barras verticales ni la flecha sobre el vector (*siendo esta la menos usada devido a su ambigüedad*).

$$\lVert \vec{v} \rVert=|\vec{v}|=v$$

---

Para calcular la **magnitud** de un **vector** tendremos que hallar la raiz cuadrada de la suma de los [componentes del vector](#COMPONENTES%20DE%20UN%20VECTOR) elevados al cudarado; es decir, el teorema de Pitágoras:

$$\lVert \vec{v} \rVert=\sqrt{v^2_1+v^2_2+v^2_3+...}$$

En el caso de un **vector** de dos dimensiones tendremos que elevar al cuadrado los compoentes $x$ e $y$ para luego sumarlos y obtener su raiz cuadrada:

$$\lVert \vec{v} \rVert=\sqrt{v^2_x+v^2_y}$$

En donde $x=3$ e $y=4$:

$$
\sqrt{3^2+4^2}\\
=\sqrt{9+16}\\
=\sqrt{25}\\
=5
$$

Por lo que la **magnitud** del **vector** $\vec{v}=(3, 4)$ es $\lVert \vec{v} \rVert=5$.

![#center](assets/pitagoras.md)

^img-pitagoras

```python
v = Vector2(3, 4)
print(v.mag())
# SALIDA:
# 5.0
```

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

## DIRECCIÓN DE UN VECTOR

## RELACIONES TRIGONOMÉTRICAS

### SENO

### COSENO

### TANGENTE

## NORMALIZACIÓN

## VETOR UNITARIO

$$
\hat{v}
$$

$$
\vec{v_1} \cdot \vec{v_2} =
(v_1)_x \cdot (v_2)_x + (v_1)_y \cdot (v_2)_y
$$

$$
\lVert \vec{v} \rVert = \sqrt{\text{dot}(\vec{v}, \vec{v})}
$$

## PRODUCTO ESCALAR

## ÁNGULO ENTRE DOS VECTORES

## VECTOR 2D EN PYTHON

```python
class Vector2:
    def __init__(self, x=0, y=0):
        assert isinstance(x, (float, int, self.__class__))
        assert isinstance(y, (float, int))

        self.__scalars = [0, 0]

        if isinstance(x, self.__class__):
            self.x = x.x
            self.y = x.y
            return

        self.x = x
        self.y = y

    @classmethod
    def new_from_rad(cls, angle):
        assert isinstance(angle, (float, int))
        return cls(math.cos(angle), math.sin(angle))

    @classmethod
    def new_from_deg(cls, angle):
        assert isinstance(angle, (float, int))
        return cls.new_from_rad(math.radians(angle))

    def __str__(self):
        return f"Vector2({round(self.x, 6)}, {round(self.y, 6)})"

    def __repr__(self):
        return f"({round(self.x, 2)}, {round(self.y, 2)})"

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __eq__(self, other):
        assert isinstance(other, self.__class__)
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        assert isinstance(other, self.__class__)
        return self.x != other.x or self.y != other.y

    def clone(self):
        return self.__class__(self)

    @property
    def x(self):
        return self.__scalars[0]

    @x.setter
    def x(self, x):
        assert isinstance(x, (float, int))
        self.__scalars[0] = x

    @property
    def y(self):
        return self.__scalars[1]

    @y.setter
    def y(self, y):
        assert isinstance(y, (float, int))
        self.__scalars[1] = y

    def mag(self) -> float:
        return math.sqrt((self.x * self.x) + (self.y * self.y))

    def cos(self) -> float:
        return self.x / self.mag()

    def sin(self) -> float:
        return self.y / self.mag()

    def tan(self) -> float:
        return self.y / self.x

    def __matmul__(self, other):
        assert isinstance(other, self.__class__)
        return self.x * other.x + self.y * other.y

    def __add__(self, other):
        assert isinstance(other, (float, int, self.__class__))

        new_vec = self.clone()

        if isinstance(other, (float, int)):
            new_vec.x += other
            new_vec.y += other
            return new_vec

        new_vec.x += other.x
        new_vec.y += other.y
        return new_vec

    def __radd__(self, other):
        assert isinstance(other, (float, int, self.__class__))

        if isinstance(other, (float, int)):
            self.x += other
            self.y += other
            return self

        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        assert isinstance(other, (float, int, self.__class__))

        new_vec = self.clone()

        if isinstance(other, (float, int)):
            new_vec.x -= other
            new_vec.y -= other
            return new_vec

        new_vec.x -= other.x
        new_vec.y -= other.y
        return new_vec

    def __rsub__(self, other):
        assert isinstance(other, (float, int, self.__class__))

        if isinstance(other, (float, int)):
            self.x -= other
            self.y -= other
            return self

        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        assert isinstance(other, (float, int, self.__class__))

        new_vec = self.clone()

        if isinstance(other, (float, int)):
            new_vec.x *= other
            new_vec.y *= other
            return new_vec

        new_vec.x *= other.x
        new_vec.y *= other.y
        return new_vec

    def __rmul__(self, other):
        assert isinstance(other, (float, int, self.__class__))

        if isinstance(other, (float, int)):
            self.x *= other
            self.y *= other
            return self

        self.x *= other.x
        self.y *= other.y
        return self

    def __truediv__(self, other):
        assert isinstance(other, (float, int, self.__class__))

        new_vec = self.clone()

        if isinstance(other, (float, int)):
            new_vec.x /= other
            new_vec.y /= other
            return new_vec

        new_vec.x /= other.x
        new_vec.y /= other.y
        return new_vec

    def __rtruediv__(self, other):
        assert isinstance(other, (float, int, self.__class__))

        if isinstance(other, (float, int)):
            self.x /= other
            self.y /= other
            return self

        self.x /= other.x
        self.y /= other.y
        return self

    def __mod__(self, other):
        assert isinstance(other, (float, int, self.__class__))

        new_vec = self.clone()

        if isinstance(other, (float, int)):
            new_vec.x %= other
            new_vec.y %= other
            return new_vec

        new_vec.x %= other.x
        new_vec.y %= other.y
        return new_vec

    def __rmod__(self, other):
        assert isinstance(other, (float, int, self.__class__))

        if isinstance(other, (float, int)):
            self.x %= other
            self.y %= other
            return self

        self.x %= other.x
        self.y %= other.y
        return self

    def __abs__(self):
        new_vec = self.clone()
        new_vec.x = abs(new_vec.x)
        new_vec.y = abs(new_vec.y)
        return new_vec

    def __neg__(self):
        new_vec = self.clone()
        new_vec.x = -new_vec.x
        new_vec.y = -new_vec.y
        return new_vec

    def __hash__(self):
        return hash(self.__scalars)

    def norm(self):
        mag = self.mag()
        self.x /= mag
        self.y /= mag
        return self

    def __iter__(self):
        return iter(self.__scalars)

    def angle_to(self, other):
        assert isinstance(other, self.__class__)
        return self.dot(other) / (self.mag() * other.mag())

    def __getitem__(self, key):
        assert isinstance(key, int)
        return self.__scalars[key]

    def __setitem__(self, key, value):
        assert isinstance(key, int)
        self.__scalars[key] = value
```

%%

---

---

---

---

---

## OPERACIONES CON VECTORES

### MAGNITUD DE UN VECTOR

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
