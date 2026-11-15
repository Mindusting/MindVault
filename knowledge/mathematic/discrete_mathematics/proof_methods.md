---
aliases: [Métodos de demostración en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-23 03:44:51
headerFile: false
modificationDate: 2026-11-15 06:34:26
rating: 
tags: [Math]
---

# MÉTODOS DE DEMOSTRACIÓN

> [!seealso]- MIRA TAMBIÉN
> - [Proposiciones](logic/propositions.md)
> - [Conectores lógicos](logic/logical_connectives.md)
> - [Reglas de inferencia](logic/inference_rules.md)
> - [Cuantificadores](logic/quantifiers.md)

Una **demostración matemática** es una secuencia de razonamientos válidos que permite justificar que una afirmación es verdadera, utilizando definiciones, premisas y [reglas de inferencia](logic/inference_rules.md).

En una afirmación condicional $p \to q$:

- **Hipótesis (antecedente):** $p$, aquello de lo que partimos.
- **Tesis (consecuente):** $q$, aquello que queremos demostrar.

Los métodos principales son la [**demostración directa**](#DEMOSTRACIÓN%20DIRECTA) y las [**demostraciones indirectas**](#DEMOSTRACIONES%20INDIRECTAS).

## ESTRUCTURA DE UNA DEMOSTRACIÓN

Una demostración no consiste en escribir muchos cálculos: consiste en construir una cadena de afirmaciones donde cada paso se justifica mediante una **definición**, una **hipótesis**, un **resultado ya demostrado** o una [regla de inferencia](logic/inference_rules.md).

En las demostraciones de tipo "si $p$, entonces $q$" es útil organizarse así:

1. **Identificar la hipótesis:** qué sabemos o qué podemos suponer.
2. **Identificar la tesis:** qué hay que conseguir exactamente.
3. **Desplegar definiciones:** por ejemplo, "$n$ es par" significa $n=2k$ para algún entero $k$.
4. **Justificar transformaciones:** cada igualdad debe ser algebraicamente correcta.
5. **Cerrar la prueba:** explicar por qué la expresión obtenida verifica la definición de la tesis.

> [!important] IMPORTANTE
> Una demostración general utiliza una variable **arbitraria** del dominio. Comprobar $n = 2$, $n = 4$ y $n = 6$ puede sugerir una conjetura, pero no justifica una afirmación sobre infinitos enteros.

### DEFINICIONES QUE SE UTILIZAN HABITUALMENTE

| CONCEPTO         | DEFINICIÓN PARA $n \in \mathbb Z$                  |
|:---------------- |:-------------------------------------------------- |
| Par              | $n = 2k$ para algún $k \in \mathbb Z$.             |
| Impar            | $n = 2k + 1$ para algún $k \in \mathbb Z$.         |
| $a$ divide a $b$ | Existe $k \in \mathbb Z$ tal que $b = ak$.         |
| Múltiplo de $a$  | Un número de la forma $ak$, con $k \in \mathbb Z$. |

Estas definiciones permiten **pasar de palabras a expresiones algebraicas**. Por ejemplo, si queremos demostrar que la suma de dos números pares es par, escribimos $a = 2r$ y $b = 2s$. Entonces:

$$a + b = 2r + 2s = 2(r + s)$$

Como $r + s$ es entero, la suma tiene la forma $2k$ y por tanto es par. El argumento vale para **cualquier** par de enteros pares.

## DEMOSTRACIÓN DIRECTA

La **demostración directa** consiste en suponer verdadera la hipótesis $p$ y, mediante pasos lógicos, demostrar la conclusión $q$.

> [!syntax] SINTAXIS
> 
> $$p \to q$$
> 
> - Suponemos que $p$ es verdadera.
> - Aplicamos definiciones y reglas de inferencia.
> - Llegamos a $q$.

> [!example] EJEMPLO
> **Demostrar:** si un número entero $n$ es impar, entonces $n^2$ es impar.
> 
> - Si $n$ es impar, $n = 2k + 1$, con $k \in \mathbb{Z}$.
> - Elevamos al cuadrado:
> 
> $$n^2 = (2k + 1)^2 = 2(2k^2 + 2k) + 1$$
> 
> - Tiene la forma $2m + 1$, con $m \in \mathbb{Z}$.
> - **Conclusión:** $n^2$ es impar.

## ELEGIR ENTRE PRUEBA DIRECTA Y PRUEBA INDIRECTA

Normalmente conviene intentar primero la demostración directa. Sin embargo, algunas afirmaciones se entienden mejor al estudiar qué ocurriría si el resultado fallara.

Para una proposición condicional $p\to q$ tenemos tres enfoques habituales:

- **Directo:** suponemos $p$ y obtenemos $q$.
- **Contraposición:** suponemos $\neg q$ y obtenemos $\neg p$.
- **Reducción al absurdo:** suponemos $p$ y $\neg q$ simultáneamente y deducimos una contradicción.

Los tres enfoques pueden demostrar la misma afirmación. En lógica clásica, son válidos, pero elegir uno u otro cambia el camino de razonamiento.

> [!example] EJEMPLO: ESTRATEGIA
> "Si un entero $n$ es impar, entonces $n^2$ es impar" resulta fácil por demostración directa, porque podemos sustituir $n=2k+1$. Para "si $n^2$ es par, entonces $n$ es par", la contraposición transforma el problema en el anterior y evita una cuenta innecesariamente complicada.

## DEMOSTRACIONES INDIRECTAS

Una **demostración indirecta** prueba una afirmación sin partir directamente de la hipótesis para alcanzar la conclusión. Dos técnicas importantes son la **contraposición** y la **reducción al absurdo**.

### DEMOSTRACIÓN POR CONTRAPOSICIÓN

Consiste en demostrar $\neg q \to \neg p$ en lugar de $p \to q$, ya que ambas expresiones son [lógicamente equivalentes](logic/logical_connectives.md).

> [!syntax] SINTAXIS
> 
> $$(p \to q) \iff (\neg q \to \neg p)$$
> 
> - Suponemos que $q$ es falsa ($\neg q$).
> - Demostramos que $p$ también es falsa ($\neg p$).

> [!example] EJEMPLO
> **Demostrar:** si $n^2$ es par, entonces $n$ es par.
> 
> - Demostramos la contraposición: "si $n$ es impar, entonces $n^2$ es impar".
> - Ya hemos demostrado esta afirmación mediante el método directo.
> - **Conclusión:** si $n^2$ es par, entonces $n$ es par.

### DEMOSTRACIÓN POR REDUCCIÓN AL ABSURDO

Consiste en suponer **falsa** la afirmación que queremos demostrar y llegar a una **contradicción**. Por tanto, la suposición inicial debe ser falsa.

> [!syntax] SINTAXIS
> 
> $$\neg p \implies \bot \quad \therefore \quad p$$
> 
> - $\neg p$: negación de lo que queremos demostrar.
> - $\bot$: contradicción (imposibilidad lógica).
> - $p$: conclusión que queda demostrada.

> [!example] EJEMPLO
> **Demostrar:** existen infinitos números primos.
> 
> - Suponemos que solamente existen $n$ primos: $p_1, p_2, \ldots, p_n$.
> - Construimos $N = p_1 p_2 \cdots p_n + 1$.
> - Ningún primo de la lista divide a $N$, porque siempre queda resto $1$.
> - Pero todo entero mayor que $1$ tiene algún divisor primo.
> - **Contradicción:** la lista no contenía todos los primos.
> - **Conclusión:** existen infinitos números primos.

## DEMOSTRACIÓN POR REDUCCIÓN AL ABSURDO: DETALLE ADICIONAL

Una contradicción consiste en llegar a algo imposible, como $0 = 1$, o en obtener una proposición y su negación simultáneamente. **No basta con que un resultado parezca extraño o improbable**: hay que explicar por qué es incompatible con una definición o una premisa.

> [!example] EJEMPLO CLÁSICO: $\sqrt{2}$ ES IRRACIONAL
> Suponemos lo contrario: que $\sqrt 2 = a / b$ para enteros $a, b$, con $b \ne 0$ y la fracción en términos irreducibles.
> 
> 1. Elevamos al cuadrado: $2 = a^2 / b^2$; luego $a^2 = 2b^2$.
> 2. $a^2$ es par. Por la contraposición del resultado "el cuadrado de un impar es impar", deducimos que $a$ es par.
> 3. Escribimos $a = 2k$. Entonces $4k^2 = 2b^2$ y $b^2 = 2k^2$.
> 4. También $b$ es par.
> 5. Si $a$ y $b$ son pares, la fracción $a / b$ se puede simplificar entre $2$, contradiciendo que estaba en términos irreducibles.
> 
> Por tanto, la suposición era falsa: **$\sqrt 2$ no puede expresarse como cociente de dos enteros**.

Este ejemplo combina definiciones de divisibilidad, álgebra y un resultado sobre números pares. Es importante que cada paso sea independiente de la afirmación que queremos demostrar; de lo contrario, caeríamos en un **razonamiento circular**.

## CONTRAEJEMPLOS

Un **contraejemplo** es un caso concreto que demuestra que una afirmación universal es falsa.

> [!syntax] SINTAXIS
> 
> Para refutar $\forall x \in D,\ P(x)$ basta encontrar $a \in D$ tal que $\neg P(a)$.

> [!example] EJEMPLO
> **Afirmación:** "Todo número entero tiene un cuadrado mayor que cero".
> 
> $$\forall n \in \mathbb{Z},\quad n^2 > 0$$
> 
> - Si $n = 0$, entonces $0^2 = 0$.
> - **Conclusión:** la afirmación es falsa.

> [!important] IMPORTANTE
> Un contraejemplo basta para **refutar** una afirmación universal; comprobar varios ejemplos favorables no basta para **demostrarla**.

## PRUEBAS DE EXISTENCIA Y UNICIDAD

No todas las demostraciones tienen forma condicional. A veces queremos demostrar que **existe** un objeto que cumple cierta propiedad.

### EXISTENCIA CONSTRUCTIVA

Proporcionamos un ejemplo y verificamos la propiedad.

> [!example] EJEMPLO
> Queremos demostrar $\exists n \in \mathbb Z,\ n^2 = 25$. Elegimos $n = 5$ y comprobamos $5^2 = 25$. Con esto queda demostrada la **existencia**, aunque también exista el testigo $-5$.

### EXISTENCIA NO CONSTRUCTIVA

Justificamos que existe algún objeto sin dar necesariamente una expresión explícita para él. No debe confundirse con "no comprobar nada": hace falta un argumento deductivo que garantice la existencia.

### UNICIDAD

Para demostrar que existe **exactamente uno**, hay que demostrar dos cosas: **existencia** y **unicidad**. Esta última significa que, si dos candidatos cumplen la propiedad, en realidad tienen que ser el mismo.

> [!example] EJEMPLO RESUELTO
> Demostremos que existe un único entero $x$ con $x + 3 = 7$.
> 
> - Existencia: $x = 4$ sirve, porque $4 + 3 = 7$.
> - Unicidad: si $x + 3 = 7$ e $y + 3 = 7$, restando $3$ obtenemos $x = 4$ e $y = 4$. Por tanto, $x = y$.
> 
> Hemos probado $\exists! x \in \mathbb Z,\ x + 3 = 7$.

## DEMOSTRACIÓN DE UN BICONDICIONAL

Para demostrar $p \leftrightarrow q$ debemos justificar **ambas direcciones**: $p \to q$ y $q \to p$. Aunque una de ellas parezca evidente, no se puede omitir.

> [!example] EJEMPLO
> "Un entero $n$ es par si y solo si $n^2$ es par".
> 
> - Si $n$ es par, $n = 2k$, luego $n^2 = 4k^2 = 2(2k^2)$ es par.
> - Si $n^2$ es par, por contraposición: si $n$ fuera impar, $n = 2k + 1$ y $n^2 = 2(2k^2 + 2k) + 1$ sería impar. Por tanto, $n$ tiene que ser par.

## DEMOSTRACIÓN POR CASOS

Consiste en dividir el problema en **todos los casos posibles** y demostrar la afirmación en cada uno de ellos.

> [!example] EJEMPLO
> **Demostrar:** para todo entero $n$, el producto $n(n + 1)$ es par.
> 
> - **Caso 1:** si $n$ es par, $n(n + 1)$ es par.
> - **Caso 2:** si $n$ es impar, $n + 1$ es par; por tanto, $n(n + 1)$ es par.
> - **Conclusión:** se cumple para todo entero, porque todo entero es par o impar.

## ESTRATEGIAS DE DEMOSTRACIÓN

- **Razonamiento hacia delante:** partir de la hipótesis y avanzar hacia la conclusión.
- **Razonamiento hacia atrás:** partir de lo que se quiere demostrar y buscar qué condiciones permitirían obtenerlo; después justificar esas condiciones.
- **Adaptar demostraciones conocidas:** reutilizar ideas o pasos de una demostración que ya conocemos.
- **Elegir el método:** probar primero una demostración directa y, si resulta difícil, considerar un método indirecto o una división por casos.

## EJERCICIOS DE COMPROBACIÓN

1. Demuestra directamente que, si $a$ y $b$ son impares, $a + b$ es par.
2. Refuta "todo número primo es impar".
3. Explica por qué comprobar una propiedad para los primeros cien enteros no prueba que se cumpla para todos.

> [!abstract] SOLUCIONES
> 1. Escribimos $a = 2r + 1$ y $b = 2s + 1$ con $r, s \in \mathbb Z$. Entonces $a + b = 2(r + s + 1)$, que es par.
> 2. El número $2$ es primo y par: contraejemplo.
> 3. Porque la afirmación es universal y todavía podrían existir contraejemplos fuera de los cien casos verificados.

## RESUMEN

| MÉTODO                   | IDEA PRINCIPAL                                         |
|:------------------------ |:------------------------------------------------------ |
| **Directa**              | Partir de $p$ y demostrar $q$.                         |
| **Contraposición**       | Demostrar $\neg q \to \neg p$.                         |
| **Reducción al absurdo** | Suponer lo contrario y llegar a una contradicción.     |
| **Por casos**            | Demostrar cada caso posible.                           |
| **Contraejemplo**        | Encontrar un caso que refute una afirmación universal. |

> [!warning] ERRORES FRECUENTES
> - Dar varios ejemplos y creer que con eso se ha demostrado una afirmación universal.
> - No contemplar todos los casos en una demostración por casos.
> - Confundir $\neg q \to \neg p$ (contraposición) con $q \to p$ (recíproca).
> - Realizar operaciones inválidas, como dividir entre cero.
> - Introducir conclusiones que no se deducen de los pasos anteriores.

> [!seealso] MIRA TAMBIÉN
> La [inducción matemática](induction.md) es otro método de demostración para propiedades sobre los números naturales o estructuras recursivas.
