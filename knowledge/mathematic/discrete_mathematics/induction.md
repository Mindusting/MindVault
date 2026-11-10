---
aliases: [Inducción en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-23 03:50:27
headerFile: false
modificationDate: 2026-11-10 03:39:45
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

## INDUCCIÓN FUERTE

Es una variante en la que, para demostrar $P(k + 1)$, suponemos que se cumplen **todos los casos anteriores**, desde $n_0$ hasta $k$:

$$P(n_0) \land P(n_0 + 1) \land \cdots \land P(k) \implies P(k + 1)$$

- Es útil cuando un caso depende de varios anteriores.
- También requiere comprobar los casos base necesarios.

## EJEMPLO DE INDUCCIÓN FUERTE

> [!example] EJEMPLO
> **Demostrar:** todo entero $n \geq 2$ puede escribirse como producto de números primos.
> 
> - **Caso base:** $n = 2$ es primo.
> - **Hipótesis:** suponemos que la propiedad se cumple para todos los enteros entre $2$ y $k$.
> - **Paso inductivo:** si $k+1$ es primo, ya cumple la propiedad. Si es compuesto, $k + 1 = a \cdot b$, con $2 \leq a, b \leq k$.
> - Por la hipótesis, $a$ y $b$ pueden expresarse como productos de primos; por tanto, $k + 1$ también.
> - **Conclusión:** se cumple para todos los enteros $n \geq 2$.

## PRINCIPIO DE BUEN ORDEN

El **principio de buen orden** establece que todo subconjunto no vacío de los números naturales tiene un **elemento mínimo**.

> [!syntax] SINTAXIS
> 
> $$A \subseteq \mathbb{N},\ A \neq \varnothing\ \implies\ \exists m \in A: \forall n \in A,\ m \leq n$$
> 
> - $A$: subconjunto no vacío de $\mathbb{N}$.
> - $m$: menor elemento de $A$.

- Este principio es **equivalente** a los principios de inducción ordinaria y fuerte sobre $\mathbb{N}$.
- Permite justificar la inducción: si hubiera contraejemplos, existiría uno **mínimo**, incompatible con el caso base y el paso inductivo.

## INDUCCIÓN GENERALIZADA

La **inducción generalizada** extiende la idea inductiva a otros **conjuntos bien ordenados**.

- Para demostrar una propiedad de un elemento, se puede suponer que se cumple para **todos los elementos anteriores** en ese orden.
- Es una ampliación del principio de inducción; no es necesario desarrollarla más para esta introducción.

## APLICACIÓN: TRIANGULACIÓN

- En **geometría computacional**, un polígono simple de $n \geq3$ lados puede dividirse mediante diagonales en **$n-2$ triángulos**.

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
