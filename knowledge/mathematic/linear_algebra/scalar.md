---
aliases: [Escalares en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-06-30 01:40:14
headerFile: false
modificationDate: 2026-11-15 09:09:52
rating:
tags: [Math]
---

# ESCALARES EN MATEMÁTICAS

> [!important] CONCEPTOS IMPORTANTES
> - Un **escalar** es un número que puede utilizarse por sí solo o para operar con otros objetos matemáticos, como vectores y matrices.
> - En álgebra lineal, los escalares suelen pertenecer al conjunto de los **números reales** ($\mathbb{R}$) o al de los **números complejos** ($\mathbb{C}$).
> - Un escalar **no tiene dirección espacial propia**. Si es real, su signo indica si es mayor o menor que cero.
> - El **valor absoluto** de un escalar real expresa su distancia a cero, independientemente de su signo.
> - El cero tiene valor absoluto cero y **no es positivo ni negativo**.
> - Al multiplicar un vector por un escalar real, su longitud se multiplica por el valor absoluto del escalar. Un escalar negativo invierte el sentido del vector.

## DEFINICIÓN

Un **escalar** es un elemento numérico que se utiliza en operaciones matemáticas. A diferencia de un vector geométrico, que puede tener una dirección y un sentido en el espacio, un escalar queda determinado por su valor numérico.

En **álgebra lineal**, los escalares son los números con los que se multiplican vectores y matrices. El conjunto al que pertenecen depende del espacio vectorial con el que se esté trabajando. En estos apuntes utilizaremos principalmente:

- **Números reales** ($\mathbb{R}$): por ejemplo, $-3$, $0$, $2.5$ o $\sqrt{2}$.
- **Números complejos** ($\mathbb{C}$): por ejemplo, $2 + 3i$, donde $i^2 = -1$.

Habitualmente se representan mediante letras minúsculas, como $a$, $k$ o $\lambda$, aunque no existe una letra exclusiva para los escalares.

> [!example] EJEMPLOS
> - $k = 3$ es un escalar real positivo.
> - $a = -2$ es un escalar real negativo.
> - $b = 0$ es un escalar real nulo.
> - $z = 3 + 4i$ es un escalar complejo.

En física también se habla de **magnitudes escalares**: magnitudes descritas mediante un valor y, cuando corresponda, una unidad, sin necesidad de especificar una dirección espacial. Algunos ejemplos son la masa, la temperatura y el tiempo transcurrido.

> [!note] NOTA
> Que un número tenga signo negativo no lo convierte en un vector. Por ejemplo, una temperatura de $-5\ ^ \circ \mathrm{C}$ sigue siendo una magnitud escalar: el signo no indica que la temperatura apunte hacia una dirección del espacio.

## REPRESENTACIÓN EN LA RECTA NUMÉRICA

Los escalares reales pueden representarse como **puntos de una recta numérica**. En ella, cada número tiene una posición concreta respecto al cero.

%%

```text
           NEGATIVOS                       POSITIVOS
           <--------                       -------->
      -3      -2      -1       0       1       2       3
<------o-------o-------o-------o-------o-------o-------o------>
```

%%

![#fillall](assets/scalar_number_line.excalidraw.md)

- El **cero** es el origen de referencia de la recta.
- Los números **positivos** se sitúan a la derecha del cero.
- Los números **negativos** se sitúan a la izquierda del cero.
- Cuanto más separado está un número del cero, mayor es su **valor absoluto**.

> [!note] NOTA
> Los escalares $-2$ y $2$ están situados en lados opuestos de la recta numérica, pero ambos se encuentran a una [distancia](#VALOR%20ABSOLUTO) de $2$ unidades del cero.
> 
> $$
> \lvert -2 \rvert = \lvert 2 \rvert = 2
> $$

La recta numérica permite hablar de **izquierda** y **derecha**, pero estas son convenciones para representar los números reales; no significan que el escalar posea una dirección espacial como la de un vector.

## SIGNO

El **signo** de un escalar real indica su relación con el cero. Permite distinguir tres casos:

| CONDICIÓN | CLASIFICACIÓN | EJEMPLO |
|:---------:|:------------- | -------:|
|  $x > 0$  | Positivo      |     $5$ |
|  $x < 0$  | Negativo      |    $-5$ |
|  $x = 0$  | Nulo          |     $0$ |

Un escalar positivo suele escribirse sin el símbolo `+`, mientras que uno negativo se escribe con el símbolo `-`.

> [!example] EJEMPLO
> Los números $+4$ y $4$ representan exactamente el mismo escalar. En cambio, $-4$ es su **opuesto**: tiene el mismo [valor absoluto](#VALOR%20ABSOLUTO), pero signo contrario.

### EL SIGNO DEL CERO

El número $0$ **no es positivo ni negativo**. Como no está situado a ninguno de los dos lados del origen, no tiene un signo positivo o negativo en el sentido matemático habitual.

Esto no impide que se considere simultáneamente **no negativo** ($0 \geq 0$) y **no positivo** ($0 \leq 0$). Es importante distinguir estas expresiones de *positivo* ($x > 0$) y *negativo* ($x < 0$).

> [!note] NOTA
> A veces se describe el signo de un escalar como su "sentido" sobre la recta numérica. Esta interpretación puede ser útil de manera informal, pero **signo y dirección vectorial son conceptos distintos**. Un escalar nulo sigue siendo un escalar, aunque su valor absoluto sea cero.

## VALOR ABSOLUTO

El **valor absoluto** de un número real es su **distancia al cero** en la recta numérica. Por tanto, siempre es un número mayor o igual que cero.

Se representa mediante dos barras verticales alrededor del número:

$$\lvert x \rvert$$

> [!abstract] DEFINICIÓN MATEMÁTICA
> Para cualquier número real $x$:
> 
> $$
> \lvert x \rvert = \begin{cases}
> x & \text{si }x \geq 0,\\
> -x & \text{si }x < 0.
> \end{cases}
> $$
> 
> Es decir, si $x$ es positivo o cero, se conserva su valor; si es negativo, se cambia su signo para obtener una distancia no negativa.

> [!example] EJEMPLOS
> 
> $$
> \begin{aligned}
> \lvert  5   \rvert &= 5\\
> \lvert -5   \rvert &= 5\\
> \lvert  0   \rvert &= 0\\
> \lvert -2.5 \rvert &= 2.5
> \end{aligned}
> $$

> [!note] NOTA (para programadores)
> Para calcular el **valor absocuto** en programación se suele usar una función dedicada a ello como es el caso de [`abs`](../../computer_science/programming/language/python/basic/builtins/abs.md) en [Python](../../computer_science/programming/language/python/python.md):
> 
> ```python
> print(abs(5))
> print(abs(-5))
> print(abs(0))
> print(abs(-2.5))
> # SALIDA:
> # 5
> # 5
> # 0
> # 2.5
> ```

### DISTANCIA ENTRE DOS ESCALARES

El valor absoluto también permite calcular la distancia entre dos números reales $a$ y $b$:

$$d(a, b) = \lvert b - a \rvert$$

> [!example] EJEMPLO
> La distancia entre $-3$ y $2$ es:
> 
> $$
> d(-3, 2) = \lvert 2 - (-3) \rvert = \lvert 5 \rvert = 5
> $$
> 
> El resultado es el mismo si intercambiamos el orden: $\lvert -3 - 2 \rvert = 5$.

> [!note] NOTA (para programadores)
> Para calcular la distancia entre dos escalares en programación se puede hacer de la siguiente forma:
> 
> ```python
> def distance(x: int | float, y: int | float) -> int | float:
>     """
>     Return the distance between two scalars.
>     """
>     if not isinstance(x, (int, float)):
>         raise ValueError("x must by int or float")
>     if not isinstance(y, (int, float)):
>         raise ValueError("y must by int or float")
>     return abs(y - x)
> 
> print(distance(-3, 2))
> # SALIDA:
> # 5
> ```

### VALOR ABSOLUTO Y MAGNITUD

En algunos contextos se utiliza la palabra **magnitud** para referirse al valor absoluto de un escalar real. Por ejemplo, $-8$ tiene valor absoluto $8$.

No obstante, conviene evitar llamar "longitud del escalar" a ese valor sin dar más contexto: la **longitud** se utiliza principalmente para vectores y objetos geométricos. En un escalar real, lo preciso es hablar de su **valor absoluto** o de su **distancia al cero**.

### MÓDULO DE UN ESCALAR COMPLEJO

Los números complejos no se clasifican en positivos o negativos como los reales. Sin embargo, también tienen **módulo**, que se escribe con las mismas barras $\lvert z \rvert$.

Si $z = a + bi$, con $a, b \in \mathbb{R}$, su módulo es:

$$
\lvert z \rvert = \sqrt{a^2 + b^2}
$$

> [!example] EJEMPLO
> Para $z = 3 + 4i$:
> 
> $$
> \lvert 3 + 4i \rvert = \sqrt{3^2 + 4^2} = \sqrt{25} = 5
> $$
> 
> Este resultado representa la distancia del número complejo al origen en el plano complejo.

## MULTIPLICACIÓN POR UN ESCALAR

Una de las aplicaciones más importantes de los escalares es **multiplicar [vectores](vector.md) y [matrices](matrix.md)**. En este contexto, el escalar actúa como un factor de escala.

### MULTIPLICACIÓN DE VECTORES

Cuando multiplicamos un vector por un escalar real $k$, multiplicamos cada componente del vector por ese número.

> [!abstract] SINTAXIS
> Para un vector de dos componentes $\vec{v} = (v_x, v_y)$:
> 
> $$k \vec{v} = (kv_x, kv_y)$$

> [!example] EJEMPLO
> Sea $\vec{v} = (2, -1)$.
> 
> Si lo multiplicamos por $3$:
> 
> $$3 \vec{v} = (6, -3)$$
> 
> Si lo multiplicamos por $-2$:
> 
> $$-2 \vec{v} = (-4, 2)$$
> 
> Y si lo multiplicamos por $0$:
> 
> $$0\vec{v} = (0, 0)$$

Para un vector real **no nulo**, el efecto del escalar es el siguiente:

- Si $k > 1$, aumenta su longitud y conserva su sentido.
- Si $0 < k < 1$, reduce su longitud y conserva su sentido.
- Si $k < 0$, multiplica su longitud por $\lvert k \rvert$ e invierte su sentido.
- Si $k = 0$, se obtiene el **vector nulo**, que no tiene dirección definida.

La relación entre la longitud del vector original y la del vector resultante es:

$$
\lVert k \vec{v} \rVert = \lvert k \rvert\, \lVert \vec{v} \rVert
$$

Aquí, $\lvert k \rvert$ representa el **valor absoluto del escalar**, mientras que $\lVert \vec{v} \rVert$ representa la **norma o longitud del vector**.

> [!note] NOTA
> Para $k = 1$, el vector no cambia. Para $k = -1$, conserva su longitud, pero se invierte su sentido. Por eso el signo del escalar **sí influye en el resultado de una operación vectorial**, aunque el propio escalar no sea un vector.

### MULTIPLICACIÓN DE MATRICES

Para multiplicar una matriz por un escalar, multiplicamos **cada uno de sus elementos** por él.

> [!example] EJEMPLO
> Si $k = 3$ y:
> 
> $$
> A = \begin{pmatrix}
> 1 &  2\\
> 0 & -1
> \end{pmatrix}
> $$
> 
> Entonces:
> 
> $$
> kA = 3 \begin{pmatrix}
> 1 &  2\\
> 0 & -1
> \end{pmatrix}
> = \begin{pmatrix}
> 3 &  6\\
> 0 & -3
> \end{pmatrix}
> $$
> 
> Consulta [operaciones con matrices](matrix_operations.md).

> [!warning] NO CONFUNDIR
> **Multiplicar un vector por un escalar** ($k \vec{v}$) y calcular el **producto escalar de dos vectores** ($\vec{u} \cdot \vec{v}$) son operaciones diferentes. La primera devuelve un vector; la segunda devuelve un escalar.

## EJERCICIOS

> [!exercise] EJERCICIOS
> 1. Clasifica los escalares $-7$, $0$, $3.5$ y $2 + 3i$ como reales o complejos. Cuando tenga sentido, indica si son positivos, negativos o nulos.
> 2. Calcula $\lvert -9 \rvert$, $\lvert 4 \rvert$ y $\lvert 0 \rvert$. Explica por qué ninguno de los resultados puede ser negativo.
> 3. Calcula la distancia entre $-6$ y $2$ en la recta numérica.
> 4. Sea $\vec{v} = (3, -2)$. Calcula $2 \vec{v}$, $-\vec{v}$ y $0 \vec{v}$. Explica qué ocurre con el sentido del vector en cada caso.
> 5. Calcula el módulo de $z = 5 + 12i$.

> [!example]- SOLUCIONES
> 1. $-7$ es real negativo; $0$ es real nulo; $3.5$ es real positivo; $2 + 3i$ es complejo y no tiene clasificación de signo positivo o negativo. Todos los reales también son complejos, pero aquí se distinguen por su forma habitual de representación.
> 2. $\lvert -9 \rvert = 9$, $\lvert 4 \rvert = 4$ y $\lvert 0 \rvert = 0$. El valor absoluto representa una distancia, por lo que nunca es negativo.
> 3. $\lvert 2 - (-6) \rvert = 8$ unidades.
> 4. $2 \vec{v} = (6, -4)$ (mismo sentido); $-\vec{v} = (-3, 2)$ (sentido opuesto); $0 \vec{v} = (0, 0)$ (vector nulo, sin dirección definida).
> 5. $\lvert 5 + 12i \rvert = \sqrt{25 + 144} = 13$.
