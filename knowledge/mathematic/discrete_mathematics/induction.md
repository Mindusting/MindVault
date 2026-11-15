---
aliases: [Inducción en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-23 03:50:27
headerFile: false
modificationDate: 2026-11-15 06:21:17
rating: 
tags: [Math]
---

# INDUCCIÓN MATEMÁTICA

> [!seealso]- MIRA TAMBIÉN
> - [Proposiciones](logic/propositions.md)
> - [Cuantificadores](logic/quantifiers.md)
> - [Reglas de inferencia](logic/inference_rules.md)
> - [Métodos de demostración](proof_methods.md)

La **inducción matemática** es un método de demostración que permite probar que una [proposición](logic/propositions.md) $P(n)$ se cumple para **todos los números naturales a partir de un valor inicial** $n_0$.

Para ello, debemos demostrar dos cosas:

- **Caso base:** la proposición se cumple para $n_0$.
- **Paso inductivo:** si se cumple para un número $k$, también se cumple para $k + 1$.

## POR QUÉ FUNCIONA LA INDUCCIÓN

Imagina una fila infinita de fichas de dominó numeradas desde $n_0$. Queremos garantizar que todas caigan. No necesitamos empujarlas una por una: basta con **tirar la primera** y asegurar que **cada ficha que cae derriba la siguiente**.

Esa es la idea de la inducción:

- **Caso base:** la primera ficha cae; es decir, $P(n_0)$ es verdadera.
- **Paso inductivo:** para cualquier $k \ge n_0$, si la ficha $k$ cae, también cae la ficha $k + 1$.
- **Conclusión:** por repetición de este razonamiento, todas las fichas a partir de $n_0$ caen.

La **hipótesis de inducción** no consiste en afirmar sin pruebas que todos los casos son ciertos. Es una **suposición condicional y temporal**: tomamos un $k$ arbitrario, suponemos $P(k)$ y demostramos que ello obliga a que $P(k + 1)$ sea verdadero.

Si falta el caso base, no se ha puesto en marcha la cadena. Si falta el paso inductivo, no sabemos si la propiedad continúa después del primer número.

> [!example] EJEMPLO DE LO QUE NO BASTA
> La propiedad $P(n): n < 10$ es verdadera para $n = 1$, pero no para todos los naturales a partir de $1$. El paso "si $k < 10$, entonces $k + 1 < 10$" falla para $k = 9$. El ejemplo muestra por qué probar unos pocos valores iniciales nunca sustituye al paso inductivo.

## PRINCIPIO DE INDUCCIÓN

> [!syntax] SINTAXIS
> 
> **1. Caso base:**
> 
> $$P(n_0)$$
> 
> **2. Hipótesis de inducción:** suponemos que, para un $k \ge n_0$, se cumple:
> 
> $$P(k)$$
> 
> **3. Paso inductivo:** usando esa hipótesis, demostramos:
> 
> $$P(k) \implies P(k + 1)$$
> 
> **Conclusión:**
> 
> $$\forall n \in \mathbb{N}, \quad (n \ge n_0 \to P(n))$$

> [!important] IMPORTANTE
> En el paso inductivo **no suponemos que $P(k + 1)$ sea verdadera**: tenemos que demostrarlo a partir de $P(k)$.
> 
> El valor inicial $n_0$ puede ser $0$, $1$ u otro natural, dependiendo de la afirmación.

## EJEMPLO DE DEMOSTRACIÓN

Queremos demostrar que la suma de los primeros $n$ números naturales positivos es:

$$P(n): \quad 1 + 2 + \cdots + n = \frac{n(n + 1)}{2}, \qquad n \ge 1$$

### CASO BASE

Comprobamos $n = 1$:

$$1 = \frac{1(1 + 1)}{2} = 1$$

Por tanto, **$P(1)$ es verdadera**.

### HIPÓTESIS DE INDUCCIÓN

Suponemos que la fórmula se cumple para un entero $k \ge 1$:

$$1 + 2 + \cdots + k = \frac{k(k + 1)}{2}$$

### PASO INDUCTIVO

Debemos demostrar que también se cumple para $k + 1$:

$$
\begin{aligned}
1 + 2 + \cdots + k + (k + 1)
&= \frac{k(k + 1)}{2} + (k + 1)\\
&= \frac{k(k + 1) + 2(k + 1)}{2}\\
&= \frac{(k + 1)(k + 2)}{2}
\end{aligned}
$$

Esta es la fórmula original sustituyendo $n$ por $k+1$.

**Conclusión:** por inducción matemática, la fórmula se cumple para todo $n \in \mathbb{N}$ con $n \ge 1$.

## SEGUNDO EJEMPLO DESARROLLADO: UNA DESIGUALDAD

Demostraremos que, para todo natural $n \ge 0$:

$$2^n \ge n+1$$

### CASO BASE

Para $n = 0$ tenemos $2^0 = 1$ y $0 + 1 = 1$. La desigualdad es cierta.

### HIPÓTESIS DE INDUCCIÓN

Tomamos un $k \ge 0$ arbitrario y suponemos que:

$$2^k \ge k + 1$$

### PASO INDUCTIVO

Queremos demostrar $2^{k + 1} \ge k + 2$. Empezamos por la potencia:

$$2^{k + 1} = 2 \cdot 2^k$$

Aplicamos la hipótesis (multiplicar por $2>0$ conserva la desigualdad):

$$2 \cdot 2^k \ge 2(k + 1) = 2k + 2$$

Como $k \ge 0$, se cumple $2k + 2 \ge k + 2$. Encadenando ambas:

$$2^{k + 1} \ge 2k + 2 \ge k + 2$$

Esta es exactamente la desigualdad que necesitamos para $k + 1$. Por tanto, el resultado queda demostrado para todo $n \ge 0$.

> [!important] IMPORTANTE
> Es útil escribir la **tesis del paso inductivo** antes de comenzar la cuenta. De esa manera podemos comprobar que la última expresión obtenida es realmente $P(k + 1)$ y no otra fórmula parecida.

## INDUCCIÓN FUERTE

Es una variante en la que, para demostrar $P(k + 1)$, suponemos que se cumplen **todos los casos anteriores**, desde $n_0$ hasta $k$:

$$
P(n_0) \land P(n_0 + 1) \land \cdots \land P(k) \implies P(k + 1)
$$

- Es útil cuando un caso depende de varios anteriores.
- También requiere comprobar los casos base necesarios.

## EJEMPLO DE INDUCCIÓN FUERTE

> [!example] EJEMPLO
> **Demostrar:** todo entero $n \geq 2$ puede escribirse como producto de números primos.
> 
> - **Caso base:** $n = 2$ es primo.
> - **Hipótesis:** suponemos que la propiedad se cumple para todos los enteros entre $2$ y $k$.
> - **Paso inductivo:** si $k + 1$ es primo, ya cumple la propiedad. Si es compuesto, $k + 1 = a \cdot b$, con $2 \leq a, b \leq k$.
> - Por la hipótesis, $a$ y $b$ pueden expresarse como productos de primos; por tanto, $k + 1$ también.
> - **Conclusión:** se cumple para todos los enteros $n \geq 2$.

## CUÁNDO UTILIZAR INDUCCIÓN FUERTE

En la inducción ordinaria, la hipótesis disponible es $P(k)$. En la fuerte podemos utilizar **todos los casos anteriores**: $P(n_0),P(n_0+1),\ldots,P(k)$.

Esto resulta útil cuando el objeto $k+1$ se descompone en partes de tamaños **menores que $k + 1$**, pero esos tamaños no tienen por qué ser exactamente $k$. En el ejemplo de factorización prima, un número compuesto $k+1$ se escribe como $ab$ y necesitamos aplicar la propiedad a los factores $a$ y $b$, cuyos valores pueden ser muy distintos de $k$.

> [!note] NOTA
> La inducción ordinaria y la fuerte tienen **la misma capacidad demostrativa** sobre los naturales. La fuerte permite escribir pruebas más cómodas cuando el paso depende de varios casos anteriores, pero no permite demostrar afirmaciones que la ordinaria no pueda demostrar.

### VARIOS CASOS BASE

Cuando la regla del paso depende de **dos valores anteriores**, suele ser necesario verificar dos casos iniciales. Por ejemplo, si queremos estudiar una sucesión que usa $F_{n - 1}$ y $F_{n - 2}$, no podemos empezar un paso inductivo sin disponer de ambos términos.

No existe una regla universal de "siempre comprobar uno o dos": debemos comprobar **todos los casos base necesarios para que la cadena inductiva quede bien iniciada**.

## PRINCIPIO DE BUEN ORDEN

El **principio de buen orden** establece que todo subconjunto no vacío de los números naturales tiene un **elemento mínimo**.

> [!syntax] SINTAXIS
> 
> $$
> A \subseteq \mathbb{N},
> \ A \neq \varnothing\ \implies\ \exists m \in A: \forall n \in A,
> \ m \leq n
> $$
> 
> - $A$: subconjunto no vacío de $\mathbb{N}$.
> - $m$: menor elemento de $A$.

- Este principio es **equivalente** a los principios de inducción ordinaria y fuerte sobre $\mathbb{N}$.
- Permite justificar la inducción: si hubiera contraejemplos, existiría uno **mínimo**, incompatible con el caso base y el paso inductivo.

## INDUCCIÓN GENERALIZADA

La **inducción generalizada** extiende la idea inductiva a otros **conjuntos bien ordenados**.

- Para demostrar una propiedad de un elemento, se puede suponer que se cumple para **todos los elementos anteriores** en ese orden.
- Es una ampliación del principio de inducción; no es necesario desarrollarla más para esta introducción.

## ERRORES DE RAZONAMIENTO EN INDUCCIÓN

### UTILIZAR LA HIPÓTESIS FUERA DE SU ALCANCE

Si solo suponemos $P(k)$, no está permitido usar $P(k+1)$ como si ya estuviera demostrada. Esa sería precisamente la conclusión pendiente.

### PARTIR DE UNA IGUALDAD QUE SE QUIERE DEMOSTRAR

A veces es válido desarrollar algebraicamente ambos lados de una igualdad. Sin embargo, una demostración correcta debe dejar claro **qué igualdad sabemos** y **qué pasos están justificados**. Es más seguro comenzar por un lado conocido y transformarlo hasta obtener el otro.

### OLVIDAR LAS CONDICIONES DE LA DESIGUALDAD

Si en un paso multiplicamos una desigualdad por un número negativo, el sentido del signo cambia. Si dividimos entre un parámetro, debemos comprobar antes que no vale cero. Estos detalles importan tanto como la propia hipótesis de inducción.

## EJEMPLOS DE PROPIEDADES QUE SE DEMUESTRAN POR INDUCCIÓN

- **Sumas:** $1 + 2 + \cdots + n = \frac{n (n + 1)} 2$.
- **Potencias:** $2^n \ge n + 1$ para $n \ge 0$.
- **Divisibilidad:** $6 \mid(7^n - 1)$ para $n \ge 1$.
- **Sucesiones recursivas:** relaciones entre términos consecutivos.
- **Estructuras:** propiedades de cadenas, árboles y fórmulas definidas recursivamente.

> [!example] EJEMPLO BREVE DE DIVISIBILIDAD
> Base: $7^1 - 1 = 6$, divisible entre $6$. Si $7^k - 1 = 6m$, entonces
> 
> $$7^{k + 1} - 1 = 7(7^k - 1) + 6 = 7 \cdot 6m + 6 = 6(7m + 1)$$
> 
> Es un múltiplo de $6$, así que el paso inductivo es correcto.

## EJERCICIOS DE COMPROBACIÓN

1. Escribe $P(k + 1)$ si $P(n)$ dice $1 + 3 + \cdots + (2n - 1) = n^2$.
2. ¿Por qué no basta comprobar $P(1)$, $P(2)$ y $P(3)$?
3. Demuestra el caso base de la identidad anterior para $n = 1$.

> [!abstract] SOLUCIONES
> 1. $1 + 3 + \cdots + (2k - 1) + (2k + 1) = (k + 1)^2$.
> 2. Porque se desconoce qué ocurre para todos los números posteriores.
> 3. El lado izquierdo vale $1$ y el derecho $1^2 = 1$.

## APLICACIÓN: TRIANGULACIÓN

- En **geometría computacional**, un polígono simple de $n \geq 3$ lados puede dividirse mediante diagonales en **$n - 2$ triángulos**.

$$T(n) = n - 2$$

- Triángulo ($n = 3$): $1$ triángulo.
- Cuadrilátero ($n = 4$): $2$ triángulos.

## RESUMEN

| PASO               | QUÉ HACEMOS                                              |
|:------------------ |:-------------------------------------------------------- |
| **Caso base**      | Demostrar $P(n_0)$.                                      |
| **Hipótesis**      | Suponer $P(k)$ para un $k \ge n_0$ arbitrario.           |
| **Paso inductivo** | Demostrar $P(k + 1)$ utilizando $P(k)$.                  |
| **Conclusión**     | Afirmar que $P(n)$ se cumple para todos los $n \ge n_0$. |

> [!warning] ERRORES FRECUENTES
> - Comprobar varios ejemplos y considerar que eso demuestra el caso general.
> - Olvidar el **caso base**.
> - Suponer $P(k + 1)$ en lugar de demostrarlo.
> - No utilizar correctamente la **hipótesis de inducción**.
> - No especificar desde qué valor $n_0$ se quiere demostrar la afirmación.

> [!note] NOTA
> La inducción matemática es una **demostración deductiva**, no una simple generalización a partir de ejemplos observados.
