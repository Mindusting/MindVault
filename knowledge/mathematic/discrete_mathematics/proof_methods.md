---
aliases: [Métodos de demostración en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-23 03:44:51
headerFile: false
modificationDate: 2026-11-01 01:18:37
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
> - Si $n$ es impar, $n=2k+1$, con $k \in \mathbb{Z}$.
> - Elevamos al cuadrado:
> 
> $$n^2 = (2k + 1)^2 = 2(2k^2 + 2k) + 1$$
> 
> - Tiene la forma $2m + 1$, con $m \in \mathbb{Z}$.
> - **Conclusión:** $n^2$ es impar.

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
> - Si $n=0$, entonces $0^2=0$.
> - **Conclusión:** la afirmación es falsa.

> [!important] IMPORTANTE
> Un contraejemplo basta para **refutar** una afirmación universal; comprobar varios ejemplos favorables no basta para **demostrarla**.

## DEMOSTRACIÓN POR CASOS

Consiste en dividir el problema en **todos los casos posibles** y demostrar la afirmación en cada uno de ellos.

> [!example] EJEMPLO
> **Demostrar:** para todo entero $n$, el producto $n(n+1)$ es par.
> 
> - **Caso 1:** si $n$ es par, $n(n + 1)$ es par.
> - **Caso 2:** si $n$ es impar, $n + 1$ es par; por tanto, $n(n + 1)$ es par.
> - **Conclusión:** se cumple para todo entero, porque todo entero es par o impar.

## ESTRATEGIAS DE DEMOSTRACIÓN

- **Razonamiento hacia delante:** partir de la hipótesis y avanzar hacia la conclusión.
- **Razonamiento hacia atrás:** partir de lo que se quiere demostrar y buscar qué condiciones permitirían obtenerlo; después justificar esas condiciones.
- **Adaptar demostraciones conocidas:** reutilizar ideas o pasos de una demostración que ya conocemos.
- **Elegir el método:** probar primero una demostración directa y, si resulta difícil, considerar un método indirecto o una división por casos.

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

> [!note] NOTA
> La **inducción matemática** se menciona en el Tema 1 del PDF, pero su desarrollo se reserva para el tema siguiente.
