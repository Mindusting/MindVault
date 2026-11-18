---
aliases: [Vectores]
author: Mindusting
corrected: true
creationDate: 2026-06-30 10:34:40
headerFile: false
modificationDate: 2026-11-16 12:33:53
rating:
tags: [Math, Vector]
---

# VECTORES

> [!external-link]- REFERENCIAS WEB
> - [Math for Game Developers — Freya Holmér](https://www.youtube.com/playlist?list=PLImQaTpSAdsD88wprTConznD1OY1EfK_V) #WWW/YT/acegikmo
> - [Visual Explanations — Freya Holmér](https://www.youtube.com/playlist?list=PLImQaTpSAdsB0DF6JfqTTm0sFdLVa80HJ) #WWW/YT/acegikmo

> [!seealso]- MIRA TAMBIÉN
> - [Escalares](scalar.md)
> - [Resumen de vectores](vector_cheatsheet.md)

> [!important] CONCEPTOS IMPORTANTES
> - Un **vector** de $n$ dimensiones puede representarse mediante $n$ [escalares](scalar.md) ordenados: $\vec{v} = (v_1, v_2, \ldots, v_n)$.
> - En el plano y en el espacio euclídeo, un vector no nulo tiene **magnitud**, **dirección** y **sentido**.
> - La **magnitud** mide su longitud y nunca es negativa: $\lVert \vec{v} \rVert \geq 0$.
> - Los vectores se **suman y restan por componentes**. También pueden multiplicarse o dividirse por un escalar, siempre que no se divida entre cero.
> - No existe una única operación llamada "multiplicación de vectores": el **producto escalar** devuelve un número, mientras que el **producto vectorial** de dos vectores de tres dimensiones devuelve otro vector.
> - **Normalizar** un vector no nulo consiste en dividirlo por su magnitud; el resultado es un vector unitario con la misma dirección y sentido.
> - El vector nulo no tiene una dirección definida y no puede normalizarse.

> [!note] NOTA
> En algunos ejemplos se utiliza una clase llamada `Vector2`. No forma parte de las clases incorporadas de [Python](../../computer_science/programming/language/python/python.md): es una implementación didáctica que aparece al final, en [VECTOR 2D EN PYTHON](#VECTOR%202D%20EN%20PYTHON). Para entender las explicaciones matemáticas no necesitas conocer su código.

## DEFINICIÓN

Un **vector** es un objeto matemático que puede sumarse con otros vectores y multiplicarse por [escalares](scalar.md), cumpliendo determinadas propiedades. En estos apuntes estudiaremos principalmente los **vectores euclídeos**, que son los utilizados para representar desplazamientos, velocidades, fuerzas y otras magnitudes en dos o tres dimensiones.

Cuando escogemos unos ejes de coordenadas, un vector de dos dimensiones puede describirse mediante dos números reales ordenados:

$$\vec{v} = (3, 4)$$

Este vector indica un desplazamiento de **3 unidades en el eje horizontal** y **4 unidades en el eje vertical**. Podemos dibujarlo como una flecha, pero el vector no es el dibujo: la flecha es una forma de representarlo.

En el plano, un vector **no nulo** posee tres características que conviene distinguir:

- **Magnitud o módulo:** cuánto mide el desplazamiento; es la longitud de la flecha.
- **Dirección:** la recta a lo largo de la cual actúa el vector; para describir su orientación también podemos utilizar un ángulo respecto a un eje de referencia.
- **Sentido:** hacia cuál de los dos extremos de esa recta apunta la flecha.

> [!example] EJEMPLO
> Los vectores $\vec{a} = (3, 0)$ y $\vec{b} = (-3, 0)$ tienen la **misma magnitud** y la **misma dirección** (horizontal), pero **sentidos opuestos**: el primero apunta hacia la derecha y el segundo hacia la izquierda.

> [!note] NOTA
> Un **punto** y un **vector** no son exactamente lo mismo. El punto $P = (3, 4)$ indica una posición, mientras que $\vec{v} = (3, 4)$ indica componentes de un desplazamiento. Si el vector parte del origen $O = (0, 0)$ y termina en $P$, se denomina **vector de posición** de $P$ y se escribe $\overrightarrow{OP}$.

## REPRESENTACIÓN

### MATEMÁTICA

En matemáticas suele escribirse una letra con una flecha encima ($\vec{v}$), acompañada de una tupla ordenada de componentes:

$$\vec{v} = (v_x, v_y) = (3, 4)$$

Otra forma habitual es representar los componentes como una **matriz columna**:

$$
\vec{v} = \begin{pmatrix}
3\\
4
\end{pmatrix}
$$

Ambas notaciones indican los mismos componentes en los ejemplos de este documento. La notación de columna es especialmente frecuente en álgebra lineal.

### FÍSICA Y GEOMETRÍA

Un vector puede dibujarse como una **flecha**. Su longitud representa la magnitud, su inclinación representa la dirección y la punta indica el sentido.

![#center](assets/vector_fisico.excalidraw.md)

Un mismo **vector libre** puede dibujarse desde distintos puntos sin cambiar sus componentes, siempre que conserve su magnitud, dirección y sentido. Por ejemplo, una flecha desde $(0, 0)$ hasta $(3, 4)$ representa el mismo desplazamiento que otra desde $(2, 1)$ hasta $(5, 5)$.

No obstante, en determinadas aplicaciones físicas también importa **dónde se aplica** una fuerza; por eso es necesario distinguir el vector de su punto de aplicación.

### PROGRAMACIÓN

En programación es habitual guardar los componentes en una lista, un [*array*](../../computer_science/programming/fundamentals/basics/array.md) o una [clase](../../computer_science/programming/fundamentals/basics/oop.md):

```python
vector = [3, 4]

print(vector)
# SALIDA:
# [3, 4]
```

Una clase permite añadir métodos para calcular magnitudes, sumar vectores y realizar otras operaciones, pero **una lista de números por sí sola no determina qué operaciones matemáticas tienen sentido**: eso depende de cómo interpretemos los datos.

## COMPONENTES DE UN VECTOR

Los **componentes** de un vector son los números que lo describen respecto a los ejes de un sistema de coordenadas. Cada componente indica cuánto contribuye el vector en la dirección de un eje.

En un sistema cartesiano habitual se utilizan los nombres $x$, $y$ y $z$ para los tres primeros ejes. Por convención, a menudo se dibujan **rojo**, **verde** y **azul**, respectivamente, pero **los colores no forman parte de la definición matemática**.

### VECTORES DE DOS DIMENSIONES

Un vector **2D** tiene dos componentes:

$$
\vec{v} = (v_x, v_y)
$$

- $v_x$: componente **horizontal**, asociada al eje $x$.
- $v_y$: componente **vertical**, asociada al eje $y$.

> [!example] EJEMPLO
> Si $\vec{v} = (3, -4)$, entonces $v_x = 3$ y $v_y = -4$. El desplazamiento es de **3 unidades hacia la derecha** y **4 hacia abajo**, suponiendo que $y$ positivo apunta hacia arriba.

Los componentes pueden ser negativos, positivos o cero. **El signo de un componente no indica la magnitud total del vector**: únicamente indica el sentido de su contribución en ese eje.

### VECTORES DE TRES DIMENSIONES

Un vector **3D** tiene tres componentes:

$$\vec{v} = (v_x, v_y, v_z)$$

El componente $v_z$ representa la contribución a lo largo del tercer eje, que suele asociarse con la profundidad o la altura según el sistema de coordenadas.

> [!example] EJEMPLO
> En $\vec{v} = (3, 4, -2)$ tenemos $v_x = 3$, $v_y = 4$ y $v_z = -2$.

### VECTORES DE MÚLTIPLES DIMENSIONES

Los vectores pueden tener **más de tres dimensiones**. Para un vector con $n$ componentes utilizamos la notación:

$$\vec{v} = (v_1, v_2, \ldots, v_n) \in \mathbb{R}^n$$

Aquí $\mathbb{R}^n$ representa el conjunto de todas las tuplas ordenadas de $n$ números reales.

> [!example] EJEMPLO
> $$\vec{v} = (2, -1, 0, 7) \in \mathbb{R}^4$$

No hace falta imaginar cuatro ejes espaciales para trabajar con este vector. Las reglas algebraicas que estudiaremos siguen funcionando componente a componente.

### NOTACIÓN DE LOS COMPONENTES

Cuando tenemos **varios vectores**, podemos identificarlos mediante subíndices:

$$
\vec{v}_1 = (v_{1, x}, v_{1, y})
\qquad
\vec{v}_2 = (v_{2, x}, v_{2, y})
$$

La primera parte del subíndice identifica **qué vector** estamos usando y la segunda indica **qué componente**. Si utilizamos índices numéricos, la coma ayuda a evitar confusiones:

$$
\vec{v}_1 = (v_{1, 1}, v_{1, 2})
\qquad
\vec{v}_2 = (v_{2, 1}, v_{2, 2})
$$

También podemos escribir $\left (\vec{v}_1 \right)_2$ para referirnos al **segundo componente del primer vector**.

> [!note] NOTA
> En matemáticas solemos numerar los componentes desde **1**; en Python, el primer elemento de una lista tiene índice **0**. Así, si `vector = [3, 4]`, entonces `vector[0]` es $v_1 = v_x = 3$ y `vector[1]` es $v_2 = v_y = 4$.

## MAGNITUD DE UN VECTOR

La **magnitud**, **módulo** o **norma euclídea** de un vector mide su longitud. Se representa mediante dos barras verticales a cada lado:

$$\lVert \vec{v} \rVert$$

En algunos libros también aparece $|\vec{v}|$, aunque usaremos las barras dobles para distinguir claramente la norma de un vector del [valor absoluto](scalar.md#VALOR%20ABSOLUTO) de un escalar.

La magnitud **nunca puede ser negativa**. Si el vector es nulo, su magnitud es cero; de lo contrario, es positiva.

### CÁLCULO EN DOS DIMENSIONES

Para $\vec{v} = (v_x, v_y)$ utilizamos el **teorema de Pitágoras**:

$$
\boxed{
\lVert \vec{v} \rVert =
\sqrt{v_x^2 + v_y^2}
}
$$

![#center](assets/pitagoras.excalidraw.md)

> [!example] EJEMPLO
> Calculamos la magnitud de $\vec{v} = (3, 4)$:
> 
> $$
> \begin{aligned}
> \lVert \vec{v} \rVert &= \sqrt{3^2 + 4^2}\\
> &= \sqrt{9 + 16}\\
> &= \sqrt{25}\\
> &= 5
> \end{aligned}
> $$
> 
> El vector mide **5 unidades**, aunque sus componentes midan 3 y 4 en cada eje. La magnitud no se obtiene sumando directamente los componentes.

```python
def mag2d(x, y):
    return (x * x + y * y) ** 0.5

print(mag2d(3, 4))
# SALIDA:
# 5.0
```

### CÁLCULO EN TRES O MÁS DIMENSIONES

En tres dimensiones se añade el cuadrado del tercer componente:

$$
\lVert \vec{v} \rVert =
\sqrt{v_x^2 + v_y^2 + v_z^2}
$$

La fórmula general para $n$ dimensiones es:

$$
\boxed{
\lVert \vec{v} \rVert = \sqrt{
    \sum_{i = 1}^{n} v_i^2
}
}
$$

El símbolo $\sum$ significa **sumar** los términos indicados; en este caso, los cuadrados de todos los componentes. Es una generalización del teorema de Pitágoras.

> [!example] EJEMPLO
> Para $\vec{v} = (2, -3, 6)$:
> 
> $$
> \lVert \vec{v} \rVert
> = \sqrt{2^2 + (-3)^2 + 6^2}
> = \sqrt{49}
> = 7
> $$

Podemos calcularlo en Python para cualquier número de componentes:

```python
def magnitude(vector) -> float:
    return (sum(s * s for s in vector)) ** 0.5

print(magnitude([3, 4]))
# SALIDA:
# 5.0
```

> [!tip] CONSEJO
> Para comparar magnitudes sin calcular raíces cuadradas, a veces basta con comparar **magnitudes al cuadrado**: $\lVert \vec{v} \rVert^2 = v_1^2 + \cdots + v_n^2$. Esto funciona porque las magnitudes son no negativas y elevarlas al cuadrado conserva su orden.

## VECTOR NULO

El **vector nulo** es aquel cuyos componentes son todos cero:

$$\vec{0} = (0, 0) \quad \text{(en 2D)}$$

$$\vec{0} = (0, 0, 0) \quad \text{(en 3D)}$$

Su magnitud es cero:

$$\lVert \vec{0} \rVert = 0$$

Tiene una propiedad fundamental: **sumarlo a otro vector no cambia ese vector**.

$$\vec{v} + \vec{0} = \vec{v}$$

> [!important] IMPORTANTE
> El vector nulo **no tiene una dirección ni un sentido definidos**. Por ello, no se puede **normalizar** ni utilizar para calcular un ángulo con otro vector mediante la fórmula del producto escalar, ya que aparecería una división entre cero.

## DIRECCIÓN Y SENTIDO DE UN VECTOR

En un plano, la dirección y el sentido de un vector no nulo pueden describirse conjuntamente mediante un **ángulo orientado** respecto a un eje de referencia.

### ÁNGULO

La letra griega $\theta$ (*theta*) se utiliza habitualmente para representar un **ángulo**. Para un vector 2D, adoptaremos estas convenciones:

- El ángulo **$0^\circ$** corresponde al eje $x$ positivo (*hacia la derecha*).
- Los ángulos positivos se miden en **sentido antihorario**.
- Una vuelta completa equivale a **$360^\circ$** o **$2 \pi$ radianes**.

Con estas convenciones, algunos ejemplos son:

|  VECTOR   |      ÁNGULO |
|:---------:| -----------:|
| $(1, 0)$  |   $0^\circ$ |
| $(0, 1)$  |  $90^\circ$ |
| $(-1, 0)$ | $180^\circ$ |
| $(0, -1)$ | $270^\circ$ |

Un ángulo puede expresarse en **grados** o **radianes**:

$$180^\circ = \pi\ \text{rad}$$

$$
\theta_{\mathrm{rad}} =
\theta_{\mathrm{deg}} \frac{\pi}{180}
\qquad
\theta_{\mathrm{deg}} =
\theta_{\mathrm{rad}} \frac{180}{\pi}
$$

> [!note] NOTA (para programadores)
> En [Python](../../computer_science/programming/language/python/python.md), las funciones trigonométricas de [`math`](../../computer_science/programming/language/python/module/standar/math/math.md) trabajan con **radianes**, salvo las funciones destinadas expresamente a convertir unidades.

### CÁLCULO DEL ÁNGULO CON `atan2`

Para $\vec{v} = (v_x, v_y)$, la forma más fiable de calcular su ángulo es:

$$
\boxed{
\theta = \operatorname{atan2}(v_y, v_x)
}
$$

La función `atan2` utiliza **ambos componentes** para identificar correctamente el cuadrante. Normalmente devuelve un ángulo entre $-\pi$ y $\pi$; si preferimos el intervalo $[0, 2\pi)$, sumamos una vuelta cuando sea necesario, o usamos el módulo:

$$
\theta_{[0, 2 \pi)} = \operatorname{atan2}(v_y, v_x) \bmod 2 \pi
$$

> [!example] EJEMPLO RESUELTO
> Para $\vec{v} = (-3, 3)$:
> 
> $$
> \theta
> = \operatorname{atan2}(3, -3)
> = 135^\circ
> = \frac{3 \pi}{4}
> $$
> 
> El vector está en el **segundo cuadrante** porque su componente horizontal es negativa y la vertical positiva.

```python
import math

x, y = -3, 3
angle_rad = math.atan2(y, x) % (2 * math.pi)
angle_deg = math.degrees(angle_rad)

print(angle_deg)
# SALIDA:
# 135.0
```

> [!warning] ERROR FRECUENTE
> Utilizar únicamente $\arctan(v_y / v_x)$ **puede dar un cuadrante incorrecto** y falla si $v_x = 0$. Por ejemplo, los vectores $(1, 1)$ y $(-1, -1)$ producen el mismo cociente $v_y / v_x = 1$, aunque apuntan en sentidos opuestos. `atan2` evita este problema.

En **tres dimensiones** un único ángulo respecto al eje $x$ no basta para describir cualquier orientación. Se necesitan más datos, como dos ángulos de orientación o un vector unitario.

## RELACIONES TRIGONOMÉTRICAS

El **seno**, el **coseno** y la **tangente** son funciones del ángulo $\theta$, no propiedades exclusivas de un vector. Sin embargo, los componentes de un vector 2D permiten calcularlas cuando conocemos su orientación.

Para un vector no nulo $\vec{v} = (v_x, v_y)$, la hipotenusa del triángulo rectángulo asociado es su magnitud $\lVert \vec{v} \rVert$. Cuando el vector se encuentra en otros cuadrantes, las mismas fórmulas siguen funcionando porque los componentes conservan sus signos.

![#center](assets/trigonometric_relations.excalidraw.md)

### SENO

El **seno** del ángulo mide la proporción vertical con signo respecto a la magnitud del vector:

$$
\boxed{ \sin \theta = \frac{v_y}{\lVert \vec{v} \rVert}}
$$

> [!example] EJEMPLO
> Si $\vec{v} = (3, 4)$, su magnitud es $5$ y:
> 
> $$\sin \theta = \frac 45 = 0.8$$

El seno siempre pertenece al intervalo $[-1, 1]$. Puede ser negativo si el vector apunta hacia la parte inferior del plano.

### COSENO

El **coseno** del ángulo mide la proporción horizontal con signo respecto a la magnitud:

$$
\boxed{ \cos \theta = \frac{v_x}{\lVert \vec{v} \rVert}}
$$

> [!example] EJEMPLO
> Para el mismo vector $\vec{v} = (3, 4)$:
> 
> $$\cos \theta = \frac 35 = 0.6$$

El coseno también se encuentra en el intervalo $[-1, 1]$. Un coseno negativo indica que el componente horizontal apunta hacia el eje $x$ negativo.

### TANGENTE

La **tangente** relaciona los componentes vertical y horizontal:

$$
\boxed{ \tan \theta = \frac{v_y}{v_x}}
\qquad (v_x \ne 0)
$$

> [!example] EJEMPLO
> Para $\vec{v} = (3, 4)$:
> 
> $$\tan \theta = \frac 43 \approx 1.3333$$

A diferencia del seno y el coseno, la tangente **no está limitada entre $-1$ y $1$**. Además, no está definida cuando $v_x = 0$.

> [!important] IMPORTANTE
> Para calcular $\sin \theta$ y $\cos \theta$ mediante los componentes necesitamos un **vector no nulo**. La tangente necesita, además, que $v_x \ne 0$. Recuerda que la tangente por sí sola tampoco permite distinguir dos sentidos opuestos.

### RECUPERAR LOS COMPONENTES A PARTIR DEL ÁNGULO

Si conocemos la magnitud $r = \lVert \vec{v} \rVert$ y el ángulo $\theta$, podemos invertir las fórmulas anteriores:

$$\boxed{v_x = r \cos \theta}$$

$$\boxed{v_y = r \sin \theta}$$

Por tanto:

$$\boxed{\vec{v} = (r \cos \theta, r \sin \theta)}$$

> [!example] EJEMPLO RESUELTO
> Un vector de magnitud $10$ y ángulo $30^\circ$ tiene componentes:
> 
> $$
> \begin{aligned}
> v_x &= 10 \cos 30^\circ = 5 \sqrt 3 \approx 8.66\\
> v_y &= 10 \sin 30^\circ = 5
> \end{aligned}
> $$
> 
> Así, $\vec{v} \approx(8.66, 5)$.

```python
import math

magnitude = 10
angle = math.radians(30)
vector = (
    magnitude * math.cos(angle), 
    magnitude * math.sin(angle)
)

print(tuple(round(component, 2) for component in vector))
# SALIDA:
# (8.66, 5.0)
```

## VECTOR UNITARIO

Un **vector unitario** es un vector cuya magnitud es exactamente **1**:

$$\lVert \hat{v} \rVert = 1$$

Suele representarse con un **sombrero** encima de la letra: $\hat{v}$. Al tener magnitud 1, es útil para representar una orientación sin incluir una distancia o intensidad concreta.

Por ejemplo, en dos dimensiones:

$$
\hat{u} = (1,  0)
\qquad
\hat{w} = (0, -1)
$$

Ambos son unitarios porque su magnitud es 1, aunque apuntan en sentidos diferentes.

También son importantes los **vectores unitarios de los ejes**:

$$
\hat{\imath} = (1, 0)
\qquad
\hat{\jmath} = (0, 1)
$$

En tres dimensiones se añade $\hat{k} = (0, 0, 1)$. Podemos expresar un vector 2D como:

$$
\vec{v} = v_x \hat{\imath} + v_y \hat{\jmath}
$$

Esto significa que el vector es la suma de sus contribuciones sobre cada eje.

## NORMALIZACIÓN

**Normalizar un vector** consiste en transformarlo en un vector de **magnitud 1**, conservando su dirección y sentido. Para ello dividimos cada componente entre la magnitud original:

$$
\boxed{ \hat{v} =
\frac{
    \vec{v}}{ \lVert \vec{v} \rVert}
} \qquad(\vec{v} \ne \vec{0})
$$

> [!example] EJEMPLO RESUELTO
> Normalicemos $\vec{v} = (3, 4)$, cuya magnitud es $5$:
> 
> $$
> \hat{v} = \frac{(3, 4)} 5
> = \left( \frac 35, \frac 45 \right)
> = (0.6, 0.8)
> $$
> 
> Comprobamos su magnitud:
> 
> $$
> \lVert \hat{v} \rVert
> = \sqrt{0.6^2 + 0.8^2} = \sqrt 1
> = 1
> $$

El nuevo vector conserva la orientación original, pero ahora su longitud es 1. Esto ocurre tanto si la magnitud inicial era **mayor** como si era **menor** que 1.

> [!warning] NO CONFUNDIR
> En estadística y programación se habla a veces de "normalizar datos" para cambiar sus valores a un intervalo, como $[0, 1]$. **Normalizar un vector** significa aquí **hacer que su magnitud sea 1**, no obligar a que cada componente sea positivo ni a que todos se encuentren en $[0, 1]$. De hecho, los componentes de un vector unitario pueden ser negativos.

```python
import math

def magnitude(vector) -> float:
    return (sum(s * s for s in vector)) ** 0.5

def normalize(vector):
    length = magnitude(vector)

    if length == 0:
        raise ValueError("No se puede normalizar el vector nulo")

    return [component / length for component in vector]

print(normalize([3, 4]))
# SALIDA:
# [0.6, 0.8]
```

## OPERACIONES CON VECTORES

Al operar **componente a componente** (por ejemplo, al sumar o restar), los vectores deben tener el **mismo número de dimensiones**. Otras operaciones, como el producto vectorial habitual, tienen requisitos específicos.

### SUMA DE VECTORES

La suma de dos vectores se calcula **sumando los componentes correspondientes**:

$$
\boxed{
    (a_x, a_y) + (b_x, b_y)
    = (a_x + b_x, a_y + b_y)
}
$$

> [!example] EJEMPLO RESUELTO
> 
> $$
> \begin{aligned}
> \vec{a} &= ( 3, 4)\\
> \vec{b} &= (-4, 1)\\
> \vec{a} + \vec{b} &= (3 + (-4), 4 + 1) = (-1, 5)
> \end{aligned}
> $$

Geométricamente podemos colocar el origen de la segunda flecha en la punta de la primera. El vector resultante va desde el comienzo de la primera hasta el final de la segunda.

```python
a = [ 3, 4]
b = [-4, 1]

result = [x + y for x, y in zip(a, b)]

print(result)
# SALIDA:
# [-1, 5]
```

> [!note] NOTA
> En este ejemplo las listas tienen la misma longitud. En código real conviene comprobarlo antes de utilizar `zip`, porque `zip` se detiene al acabar la lista más corta.

### RESTA DE VECTORES

La resta se calcula **restando los componentes correspondientes**:

$$
\boxed{
    (a_x, a_y) - (b_x, b_y)
    = (a_x - b_x, a_y - b_y)
}
$$

> [!example] EJEMPLO RESUELTO
> 
> $$
> \begin{aligned}
> \vec{a} &= ( 3, 4)\\
> \vec{b} &= (-4, 1)\\
> \vec{a} - \vec{b} &= (3 - (-4), 4 - 1) = (7, 3)
> \end{aligned}
> $$

También puede entenderse como **sumar el vector opuesto**:

$$\vec{a} - \vec{b} = \vec{a} + (-\vec{b})$$

### VECTOR OPUESTO

El **vector opuesto** $-\vec{v}$ conserva la magnitud y la dirección de $\vec{v}$, pero tiene el **sentido contrario**. Se obtiene cambiando el signo de todos los componentes:

$$
\vec{v} = (3, -4)
\qquad
-\vec{v} = (-3, 4)
$$

Por definición:

$$\vec{v} + (-\vec{v}) = \vec{0}$$

### MULTIPLICACIÓN POR UN ESCALAR

Multiplicar un vector por un **escalar** $k$ consiste en multiplicar **todos sus componentes** por ese número:

$$\boxed{ k(v_x, v_y) = (kv_x, kv_y) }$$

El resultado sigue siendo un vector. Su magnitud se modifica según:

$$\lVert k \vec{v} \rVert = |k| \lVert \vec{v} \rVert$$

- Si $k > 0$, conserva el sentido y multiplica la magnitud por $k$.
- Si $k < 0$, invierte el sentido y multiplica la magnitud por $|k|$.
- Si $k = 0$, obtenemos el vector nulo.

> [!example] EJEMPLO
> Si $\vec{v} = (3, 4)$:
> 
> $$
> 2\vec{v} = (6, 8)
> \qquad
> -\vec{v} = (-3, -4)
> $$
> 
> El primer resultado tiene el doble de magnitud y el mismo sentido. El segundo tiene la misma magnitud y sentido opuesto.

> [!important] IMPORTANTE
> En álgebra vectorial ordinaria, **sumar un escalar a un vector**, como $\vec{v} + 3$, **no está definido**. Algunas bibliotecas de programación permiten hacerlo sumando 3 a cada componente; se trata de una convención adicional, no de la suma matemática de vectores.

### DIVISIÓN POR UN ESCALAR

Dividir un vector entre un escalar **no nulo** equivale a multiplicarlo por su inverso:

$$
\boxed{
    \frac{ \vec{v}} k =
    \left(
        \frac{v_x} k,
        \frac{v_y} k \right
    )
}
\qquad(k \ne 0)
$$

> [!example] EJEMPLO
> 
> $$\frac{(6, -9)} 3 = (2, -3)$$

Si el escalar es negativo, se invierte el sentido; si es cero, la operación no existe.

### PRODUCTO ESCALAR

El **producto escalar** (*dot product*) de dos vectores devuelve un **escalar**, no otro vector. Se calcula multiplicando los componentes correspondientes y sumando los resultados:

$$
\boxed{ \vec{a} \cdot \vec{b} = a_x b_x + a_y b_y}
$$

Para $n$ dimensiones:

$$
\boxed{ \vec{a} \cdot \vec{b} = \sum_{i = 1}^{n} a_i b_i}
$$

> [!example] EJEMPLO RESUELTO
> 
> $$
> \begin{aligned}
> \vec{a} &= (3, 4)\\
> \vec{b} &= (-4, 1)\\
> \vec{a} \cdot \vec{b} &= 3(-4) + 4(1)\\
> &= -12 + 4\\
> &= -8
> \end{aligned}
> $$
> 
> El resultado es el **número** $-8$.

```python
def dot_product(a, b) -> float:
    if len(a) != len(b):
        raise ValueError("Los vectores deben tener la misma dimensión")
    return sum(x * y for x, y in zip(a, b))

print(dot_product([3, 4], [-4, 1]))
# SALIDA:
# -8
```

El producto escalar también tiene una **interpretación geométrica**:

$$
\boxed{
    \vec{a} \cdot \vec{b}
    = \lVert \vec{a} \rVert \lVert \vec{b} \rVert \cos \varphi
}
$$

Aquí $\varphi$ es el ángulo **menor** entre ambos vectores no nulos, comprendido entre $0^\circ$ y $180^\circ$.

- Si $\vec{a} \cdot \vec{b} > 0$, el ángulo es **agudo**.
- Si $\vec{a} \cdot \vec{b} = 0$ y ambos vectores son no nulos, son **perpendiculares**.
- Si $\vec{a} \cdot \vec{b} < 0$, el ángulo es **obtuso**.

Una propiedad útil es que el producto escalar de un vector consigo mismo equivale a su magnitud al cuadrado:

$$
\vec{v} \cdot \vec{v} = \lVert \vec{v} \rVert^2
$$

### ÁNGULO ENTRE DOS VECTORES

Si tenemos dos vectores no nulos, podemos despejar el coseno del ángulo $\varphi$ entre ellos:

$$
\cos \varphi = \frac{
    \vec{a} \cdot \vec{b}
}{
    \lVert \vec{a} \rVert \lVert \vec{b} \rVert
}
$$

Para obtener el ángulo, aplicamos la función inversa del coseno:

$$
\boxed{
\varphi = \arccos \left( \frac{
    \vec{a} \cdot \vec{b}
}{
    \lVert \vec{a} \rVert \lVert \vec{b} \rVert} \right)
}
$$

> [!example] EJEMPLO RESUELTO
> Sean $\vec{a} = (1, 0)$ y $\vec{b} = (0, 1)$. Su producto escalar es $0$ y ambos tienen magnitud $1$:
> 
> $$
> \varphi
> = \arccos \left( \frac{0}{1 \cdot 1} \right)
> = \arccos(0)
> = 90^\circ
> $$
> 
> Por tanto, son **perpendiculares**.

El cociente anterior también se llama **similitud del coseno** (*cosine similarity*). Su valor está entre $-1$ y $1$:

- $1$: los vectores apuntan **exactamente en el mismo sentido**.
- $0$: son **perpendiculares**.
- $-1$: apuntan **exactamente en sentidos opuestos**.

> [!warning] ERROR FRECUENTE
> La **similitud del coseno no es un ángulo**. Una función llamada `angle_to()` debería devolver el ángulo (por ejemplo, en radianes) y no directamente el cociente de la fórmula anterior. Si quieres obtener la similitud, resulta más claro usar el nombre `cosine_similarity()`.

En dos dimensiones podemos distinguir también **hacia qué lado girar**. El ángulo orientado desde $\vec{a}$ hasta $\vec{b}$ se puede calcular mediante:

$$
\Delta \theta
= \operatorname{atan2}(
    a_x b_y - a_y b_x,
    \vec{a} \cdot \vec{b}
)
$$

Con ejes cartesianos habituales, un resultado positivo indica giro **antihorario** y uno negativo indica giro **horario**. Este ángulo orientado no es lo mismo que el ángulo menor no orientado de la fórmula con $\arccos$.

### PRODUCTO VECTORIAL

El **producto vectorial** (*cross product*) habitual se define entre dos vectores de **tres dimensiones** y devuelve otro vector perpendicular a ambos:

$$\vec{a} \times \vec{b}$$

Si $\vec{a} = (a_x, a_y, a_z)$ y $\vec{b} = (b_x, b_y, b_z)$:

$$
\boxed{
\vec{a} \times \vec{b} =
\left(
 a_y b_z - a_z b_y,
 a_z b_x - a_x b_z,
 a_x b_y - a_y b_x
\right)
}
$$

Su magnitud es:

$$
\lVert \vec{a} \times \vec{b} \rVert
= \lVert \vec{a} \rVert \lVert \vec{b} \rVert \sin \varphi
$$

El sentido del resultado se determina mediante la **regla de la mano derecha**. El orden importa, porque:

$$
\vec{a} \times \vec{b} = -(\vec{b} \times \vec{a})
$$

> [!example] EJEMPLO
> 
> $$(1, 0, 0) \times (0, 1, 0) = (0, 0, 1)$$
> 
> El resultado apunta hacia el eje $z$ positivo.

> [!note] NOTA
> En geometría plana se utiliza a veces la expresión $a_x b_y - a_y b_x$ para obtener un **escalar con signo** que informa sobre la orientación de dos vectores 2D. Está relacionada con el componente $z$ del producto vectorial si representamos esos vectores en 3D añadiendo una coordenada $z = 0$. No debe confundirse con un producto vectorial que devuelva un vector 2D ordinario.

### MULTIPLICACIÓN Y DIVISIÓN COMPONENTE A COMPONENTE

En programación pueden resultar útiles operaciones que **multiplican o dividen los componentes correspondientes**. La multiplicación de este tipo se llama **producto de Hadamard**:

$$(a_x, a_y) \odot (b_x, b_y) = (a_x b_x, a_y b_y)$$

Por ejemplo:

$$(2, 3) \odot (4, 5) = (8, 15)$$

La división componente a componente se puede escribir, si ningún componente del divisor es cero, como:

$$(8, 15) \oslash (4, 5) = (2, 3)$$

> [!important] IMPORTANTE
> Estas operaciones **no son el producto escalar ni el producto vectorial**. Tampoco existe, en el álgebra vectorial ordinaria, una operación general llamada **división de un vector entre otro**. Si una biblioteca permite escribir `a * b` o `a / b` con dos vectores, hay que revisar cómo ha definido esos operadores. En la clase `Vector2` de este documento conservaremos esa posibilidad como extensión útil para programación, indicando expresamente que es componente a componente.

### DISTANCIA ENTRE DOS PUNTOS

Si $P = (p_x, p_y)$ y $Q = (q_x, q_y)$ son dos puntos, el vector que va de $P$ hasta $Q$ es:

$$\overrightarrow{PQ} = Q - P = (q_x - p_x, q_y - p_y)$$

La **distancia** entre los puntos es la magnitud de ese desplazamiento:

$$
\boxed{ d(P, Q)
= \lVert Q - P \rVert
= \sqrt{(q_x - p_x)^2 + (q_y - p_y)^2}}
$$

> [!example] EJEMPLO
> Para $P = (1, 2)$ y $Q = (4, 6)$:
> 
> $$
> \overrightarrow{PQ} = (3, 4)
> \qquad
> d(P, Q) = \sqrt{3^2 + 4^2} = 5
> $$

### PROYECCIÓN DE UN VECTOR SOBRE OTRO

La **proyección** permite conocer qué parte de un vector está alineada con otro vector no nulo. Por ejemplo, si queremos proyectar $\vec{a}$ sobre $\vec{b}$:

$$
\boxed{
    \operatorname{proj}_{\vec{b}}(\vec{a}) = \frac{
        \vec{a}\cdot\vec{b}
    }{
        \lVert \vec{b} \rVert^2
    } \vec{b}
}
\qquad(\vec{b} \ne \vec{0})
$$

> [!example] EJEMPLO
> Si $\vec{a} = (3, 4)$ y $\vec{b} = (1, 0)$:
> 
> $$
> \operatorname{proj}_{\vec{b}}(\vec{a}) =
> \frac{3 \cdot 1 + 4 \cdot 0}{1^2}(1, 0) = (3, 0)
> $$
> 
> La proyección conserva únicamente la parte de $\vec{a}$ que apunta a lo largo del eje horizontal.

## VECTOR 2D EN PYTHON

La siguiente clase `Vector2` reúne en un solo lugar varias operaciones explicadas en estos apuntes. Está escrita con fines didácticos, no pretende sustituir una biblioteca de álgebra lineal.

He conservado la idea y muchos de los nombres de la clase original, pero con dos aclaraciones importantes: `angle_to()` devuelve ahora **un ángulo en radianes**, y `cosine_similarity()` devuelve la **similitud del coseno**. Además, los operadores `*` y `/` con **dos vectores** realizan operaciones **componente a componente**, que no son operaciones vectoriales estándar.

> [!note] CONVENCIONES DE ESTA CLASE
> - `mag()` devuelve la magnitud; `mag_squared()` devuelve su cuadrado.
> - `dir()` devuelve el ángulo del vector respecto al eje $x$, en **radianes**, dentro de $[0, 2 \pi)$.
> - `norm()` **modifica el propio vector**, mientras que `normalized()` devuelve una **copia** normalizada.
> - `a @ b` calcula el **producto escalar**.
> - `a * 2` multiplica por un escalar, mientras que `a * b` utiliza el **producto de Hadamard**.
> - `a / 2` divide por un escalar, mientras que `a / b` divide **componente a componente**.
> - `a + 2` y `a - 2` son extensiones para programación y no operaciones habituales del álgebra vectorial.

```python
import math


class Vector2:
    def __init__(self, x=0, y=0):
        if isinstance(x, Vector2):
            self.x = x.x
            self.y = x.y
        else:
            self.x = x
            self.y = y

    @classmethod
    def new_from_rad(cls, angle, magnitude=1):
        return cls(magnitude * math.cos(angle),
                   magnitude * math.sin(angle))

    @classmethod
    def new_from_deg(cls, angle, magnitude=1):
        return cls.new_from_rad(math.radians(angle), magnitude)

    def __str__(self):
        return f"Vector2({self.x:.6g}, {self.y:.6g})"

    def __repr__(self):
        return f"Vector2({self.x!r}, {self.y!r})"

    def __iter__(self):
        return iter((self.x, self.y))

    def __getitem__(self, index):
        return (self.x, self.y)[index]

    def __setitem__(self, index, value):
        if index in (0, -2):
            self.x = value
        elif index in (1, -1):
            self.y = value
        else:
            raise IndexError("Vector2 solo tiene dos componentes")

    def __bool__(self):
        return not self.is_null()

    def __eq__(self, other):
        if not isinstance(other, Vector2):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def clone(self):
        return Vector2(self)

    def is_null(self):
        return self.x == 0 and self.y == 0

    def mag_squared(self):
        return self.x * self.x + self.y * self.y

    def mag(self):
        return math.hypot(self.x, self.y)

    def __abs__(self):
        return self.mag()

    def abs_components(self):
        self.x = abs(self.x)
        self.y = abs(self.y)
        return self

    def norm(self):
        length = self.mag()
        if length == 0:
            raise ValueError("No se puede normalizar el vector nulo")
        self.x /= length
        self.y /= length
        return self

    def normalized(self):
        return self.clone().norm()

    def dir(self):
        if self.is_null():
            raise ValueError("El vector nulo no tiene dirección")
        return math.atan2(self.y, self.x) % (2 * math.pi)

    def cos(self):
        if self.is_null():
            raise ValueError("El vector nulo no tiene coseno de dirección")
        return self.x / self.mag()

    def sin(self):
        if self.is_null():
            raise ValueError("El vector nulo no tiene seno de dirección")
        return self.y / self.mag()

    def tan(self):
        if self.x == 0:
            raise ValueError("La tangente no está definida para x = 0")
        return self.y / self.x

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        if isinstance(other, (int, float)):
            return Vector2(self.x + other, self.y + other)
        return NotImplemented

    def __iadd__(self, other):
        result = self + other
        if result is NotImplemented:
            return NotImplemented
        self.x, self.y = result.x, result.y
        return self

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        if isinstance(other, (int, float)):
            return Vector2(self.x - other, self.y - other)
        return NotImplemented

    def __isub__(self, other):
        result = self - other
        if result is NotImplemented:
            return NotImplemented
        self.x, self.y = result.x, result.y
        return self

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        if isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        result = self * other
        if result is NotImplemented:
            return NotImplemented
        self.x, self.y = result.x, result.y
        return self

    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        if isinstance(other, (int, float)):
            return Vector2(self.x / other, self.y / other)
        return NotImplemented

    def __itruediv__(self, other):
        result = self / other
        if result is NotImplemented:
            return NotImplemented
        self.x, self.y = result.x, result.y
        return self

    def __mod__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x % other.x, self.y % other.y)
        if isinstance(other, (int, float)):
            return Vector2(self.x % other, self.y % other)
        return NotImplemented

    def __imod__(self, other):
        result = self % other
        if result is NotImplemented:
            return NotImplemented
        self.x, self.y = result.x, result.y
        return self

    def __matmul__(self, other):
        if not isinstance(other, Vector2):
            return NotImplemented
        return self.x * other.x + self.y * other.y

    def cosine_similarity(self, other):
        if not isinstance(other, Vector2):
            raise TypeError("Se requiere otro Vector2")
        if self.is_null() or other.is_null():
            raise ValueError("No existe ángulo con el vector nulo")
        similarity = (self @ other) / (self.mag() * other.mag())
        return max(-1.0, min(1.0, similarity))

    def angle_to(self, other):
        # Ángulo menor, en radianes: [0, pi].
        return math.acos(self.cosine_similarity(other))

    def signed_angle_to(self, other):
        # Giro orientado, en radianes: [-pi, pi].
        if not isinstance(other, Vector2):
            raise TypeError("Se requiere otro Vector2")
        if self.is_null() or other.is_null():
            raise ValueError("No existe ángulo con el vector nulo")
        cross_z = self.x * other.y - self.y * other.x
        return math.atan2(cross_z, self @ other)

    def distance_to(self, other):
        if not isinstance(other, Vector2):
            raise TypeError("Se requiere otro Vector2")
        return (self - other).mag()
```

### EJEMPLOS CON LA CLASE

```python
import math

v = Vector2(3, 4)
print(v.mag())           # 5.0
print(v.normalized())    # Vector2(0.6, 0.8)
print(v * 2)             # Vector2(6, 8)
print(v @ Vector2(1, 0)) # 3

right = Vector2(1, 0)
up = Vector2(0, 1)
print(math.degrees(right.angle_to(up)))        # 90.0
print(math.degrees(right.signed_angle_to(up))) # 90.0

print(Vector2.new_from_deg(90))
# Aproximadamente Vector2(0, 1): cos(90°) tiene
# un pequeño error de redondeo en coma flotante.
```

> [!tip] SOBRE LOS NÚMEROS DECIMALES
> Muchas operaciones trigonométricas se calculan mediante números en **coma flotante**. Por ejemplo, `math.cos(math.pi / 2)` puede devolver un número muy pequeño en lugar de cero exacto. Si necesitas comprobar si dos magnitudes calculadas son aproximadamente iguales, utiliza una comparación con tolerancia como `math.isclose()`.

## EJERCICIOS

Intenta resolver estos ejercicios antes de consultar las soluciones. Cuando se pida un ángulo, expresa el resultado en **grados**.

> [!exercise] EJERCICIOS
> 1. Dado $\vec{v} = (-3, 4)$, identifica sus componentes, su cuadrante y su magnitud.
> 2. Calcula la suma y la resta de $\vec{a} = (2, -1)$ y $\vec{b} = (-4, 3)$.
> 3. Para $\vec{v} = (2, -3)$, calcula $3\vec{v}$ y $-\vec{v}$. Indica cómo cambian la magnitud y el sentido.
> 4. Normaliza $\vec{v} = (5, 12)$ y comprueba que el resultado tiene magnitud 1.
> 5. Calcula el ángulo orientado respecto al eje $x$ del vector $\vec{v} = (-1, -1)$ en el intervalo $[0^\circ, 360^\circ)$.
> 6. Un vector tiene magnitud $8$ y forma un ángulo de $60^\circ$ con el eje $x$ positivo. Calcula sus componentes.
> 7. Calcula el producto escalar de $\vec{a} = (2, 1)$ y $\vec{b} = (-1, 2)$. ¿Qué puedes concluir sobre el ángulo entre ambos?
> 8. Calcula el ángulo menor entre $\vec{a} = (1, 0)$ y $\vec{b} = (-1, 1)$.
> 9. Calcula la distancia entre $P = (-2, 1)$ y $Q = (1, 5)$.
> 10. Explica por qué no se puede normalizar $\vec{0}$ y por qué $(1, 2) / (0, 3)$ no es una división componente a componente válida.

> [!example]- MOSTRAR SOLUCIONES
> **1. Componentes, cuadrante y magnitud.** $v_x = -3$, $v_y = 4$, segundo cuadrante, $\lVert \vec{v} \rVert = \sqrt{9 + 16} = 5$.
> 
> **2. Suma y resta.** $\vec{a} + \vec{b} = (-2, 2)$ y $\vec{a} - \vec{b} = (6, -4)$.
> 
> **3. Multiplicación por escalar.** $3\vec{v} = (6, -9)$: magnitud tres veces mayor, mismo sentido. $-\vec{v} = (-2, 3)$: misma magnitud, sentido contrario.
> 
> **4. Normalización.** $\lVert \vec{v} \rVert = 13$ y $\hat{v} = (5 / 13, 12 / 13)$. Su magnitud es $\sqrt{25 / 169 + 144 / 169} = 1$.
> 
> **5. Dirección.** $\operatorname{atan2}(-1, -1) = -135^\circ$, equivalente a **$225^\circ$** en el intervalo pedido.
> 
> **6. Componentes.** $v_x = 8 \cos 60^\circ = 4$ y $v_y = 8 \sin 60^\circ = 4 \sqrt 3 \approx 6.93$.
> 
> **7. Producto escalar.** $2(-1) + 1(2) = 0$. Como ninguno es nulo, son **perpendiculares**.
> 
> **8. Ángulo menor.** $\cos \varphi = -1 / \sqrt 2$; por tanto, $\varphi = 135^\circ$.
> 
> **9. Distancia.** $Q - P = (3, 4)$ y $d(P, Q) = 5$.
> 
> **10. Operaciones no definidas.** La norma de $\vec{0}$ es cero, así que su normalización exigiría dividir entre cero. En $(1, 2) \oslash (0, 3)$ el primer componente también exigiría dividir entre cero.
