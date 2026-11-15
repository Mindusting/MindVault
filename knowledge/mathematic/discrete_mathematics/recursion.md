---
aliases: [Recursión en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-23 03:52:00
headerFile: false
modificationDate: 2026-11-15 06:43:18
rating: 
tags: [Math]
---

# RECURSIÓN

> [!seealso]- MIRA TAMBIÉN
> - [Inducción matemática](induction.md)
> - [Proposiciones](logic/propositions.md)
> - [Métodos de demostración](proof_methods.md)

La **recursión** es una técnica que permite definir una **función, sucesión o estructura** utilizando versiones más pequeñas de sí misma.

Una definición recursiva necesita:

- **Caso base:** define directamente uno o varios casos iniciales.
- **Regla recursiva:** define los demás casos a partir de otros más sencillos.

## QUÉ HACE QUE UNA DEFINICIÓN RECURSIVA SEA VÁLIDA

Decir que algo se define "en función de sí mismo" no es suficiente. Una definición recursiva útil debe permitir **alcanzar un caso conocido** mediante un número finito de pasos, al menos para todas las entradas de su dominio.

Por ejemplo, si escribimos $a_n = a_{n - 1} + 2$ pero no indicamos ningún valor inicial, conocemos la diferencia entre términos pero **no sabemos sus valores concretos**: numerosas sucesiones cumplen esa misma regla.

Si añadimos $a_0 = 1$, obtenemos una sucesión determinada: $1, 3, 5, 7, \ldots$. La regla usa términos anteriores y el caso base fija el punto de partida.

> [!warning] EJEMPLO DE RECURSIÓN DEFECTUOSA
> Si definimos $f(0) = 0$ y $f(n) = f(n + 1) + 1$ para $n > 0$, el cálculo desde $n = 1$ pide $f(2)$, después $f(3)$ y así sucesivamente. **No se acerca al caso base**. La definición no proporciona un procedimiento finito para hallar los valores positivos.

## RECURSIÓN LINEAL Y RECURSIÓN MÚLTIPLE

En la **recursión lineal**, cada paso depende de un solo caso anterior, como el factorial $n! = n(n - 1)!$. En la **recursión múltiple**, una expresión depende de varios casos: Fibonacci utiliza $F_{n - 1}$ y $F_{n - 2}$.

Esta distinción importa al programar: varias llamadas recursivas pueden repetir muchos cálculos. El significado matemático de la sucesión no cambia, pero el **coste computacional** del método de evaluación sí puede cambiar mucho.

## DEFINICIÓN RECURSIVA

> [!syntax] SINTAXIS
> 
> Una sucesión puede definirse, por ejemplo, mediante:
> 
> $$
> \begin{cases}
> a_0 = c\\
> a_n = g(n, a_{n - 1}), &n \geq 1
> \end{cases}
> $$
> 
> - $a_0 = c$: caso base.
> - $a_n$: término que queremos calcular.
> - $a_{n - 1}$: término anterior.
> - $g$: regla que permite obtener el nuevo término.
> 
> Algunas definiciones necesitan **varios casos base** o utilizan **más de un término anterior**.

## FACTORIAL

El **factorial** de un número natural $n$ se representa como $n!$ y puede definirse recursivamente:

> [!syntax] SINTAXIS
> 
> $$
> n! = \begin{cases}
> 1, &n = 0\\
> n(n - 1)!,&n \geq 1
> \end{cases}
> $$

> [!example] EJEMPLO
> 
> $$
> \begin{aligned}
> 4! &= 4 \cdot 3!\\
> &= 4 \cdot 3 \cdot 2!\\
> &= 4 \cdot 3 \cdot 2 \cdot 1!\\
> &= 4 \cdot 3 \cdot 2 \cdot1 \cdot 0!\\
> &= 24
> \end{aligned}
> $$
> 
> La definición termina al llegar al caso base $0!= 1$.

## DESARROLLO MANUAL DE UNA RECURSIÓN

Sea la sucesión:

$$a_0 = 2, \qquad a_n = 3a_{n - 1} + 1 \quad(n \ge 1)$$

Para encontrar $a_3$ seguimos la definición paso a paso:

$$
\begin{aligned}
a_1 &= 3 a_0 + 1 = 3 \cdot  2 + 1 =  7\\
a_2 &= 3 a_1 + 1 = 3 \cdot  7 + 1 = 22\\
a_3 &= 3 a_2 + 1 = 3 \cdot 22 + 1 = 67
\end{aligned}
$$

El proceso muestra dos ideas:

- **Calcular hacia delante** es sencillo cuando conocemos los casos base.
- La regla recursiva no tiene por qué ser una suma: puede incluir multiplicaciones, condiciones, operaciones con conjuntos o construcción de estructuras.

### FÓRMULA EXPLÍCITA FRENTE A RECURSIVA

La sucesión $a_n = 2n + 1$ puede expresarse de dos maneras:

- **Explícita:** $a_n = 2n + 1$.
- **Recursiva:** $a_0 = 1$ y $a_n = a_{n - 1} + 2$ para $n \ge 1$.

La fórmula explícita calcula directamente un término; la recursiva explica cómo construirlo a partir de otro. No siempre es sencillo encontrar una fórmula explícita para una sucesión recursiva.

## SUCESIONES RECURSIVAS

Una **sucesión recursiva** define sus términos usando uno o varios términos anteriores.

> [!example] EJEMPLO: SUCESIÓN DE FIBONACCI
> 
> $$
> \begin{aligned}
> F_0 &= 0\\
> F_1 &= 1\\
> F_n &= F_{n - 1} + F_{n - 2}, \quad n \geq 2
> \end{aligned}
> $$
> 
> - **Casos base:** $F_0 = 0$ y $F_1 = 1$.
> - **Regla recursiva:** sumar los dos términos anteriores.
> - **Primeros términos:** $0, 1, 1, 2, 3, 5, 8, \ldots$

## CONJUNTOS DEFINIDOS RECURSIVAMENTE

Un **conjunto recursivo** puede describirse mediante **elementos iniciales** y **reglas para generar otros elementos**.

> [!example] EJEMPLO: NATURALES PARES
> Definimos el conjunto $E$:
> - **Caso base:** $0 \in E$.
> - **Regla recursiva:** si $n \in E$, entonces $n + 2 \in E$.
> - **No se incluyen otros elementos** distintos de los obtenidos con estas reglas.
> 
> $$E = \{0, 2, 4, 6, \ldots\}$$

## ESTRUCTURAS RECURSIVAS

También podemos definir **estructuras**, como listas, de manera recursiva.

Por ejemplo, para las listas finitas:

- **Caso base:** la lista vacía $[]$ es una lista.
- **Regla recursiva:** si $L$ es una lista y $x$ es un elemento, $[x] + L$ también es una lista.

La longitud de una lista puede definirse así:

$$
\begin{aligned}
\ell([]) &= 0\\
\ell([x] + L) &= 1 + \ell(L)
\end{aligned}
$$

Aquí $+$ representa la concatenación de listas.

## ÁRBOLES DEFINIDOS RECURSIVAMENTE

Un **árbol con raíz** también puede construirse recursivamente:

- **Caso base:** un único vértice $r$ forma un árbol con raíz.
- **Regla recursiva:** dados varios árboles con raíz **separados**, creamos una raíz nueva $r$ y la conectamos con la raíz de cada árbol.

Así obtenemos árboles cada vez mayores a partir de árboles más pequeños.

## RECURSIÓN SOBRE ESTRUCTURAS

Una lista puede verse como una estructura que tiene dos formas: la **lista vacía** o un **primer elemento seguido de otra lista**. Esta descomposición permite definir operaciones sin conocer de antemano la longitud.

Por ejemplo, para sumar una lista de enteros:

$$
\begin{aligned}
S([]) &= 0\\
S([x] + L) &= x + S(L)
\end{aligned}
$$

> [!example] EJEMPLO
> 
> $$
> \begin{aligned}
> S([2, 3, 4]) &= 2 + S([3, 4])\\
> &= 2 + 3 + S([4])\\
> &= 2 + 3 + 4 + S([])\\
> &= 9
> \end{aligned}
> $$

El caso base establece que la suma de la lista vacía es cero; la regla extrae el primer elemento y reduce la longitud de la lista. Así, cada llamada trata una lista más pequeña.

En los **árboles**, la misma idea se aplica a los subárboles: una propiedad de un nodo puede definirse utilizando esa propiedad en sus hijos. Muchas operaciones sobre expresiones aritméticas, directorios y árboles de sintaxis siguen este patrón.

## RECURSIÓN EN PROGRAMACIÓN

> [!note] NOTA (para programadores)
> Una función recursiva es una función que se llama a sí misma. Por ejemplo:
> 
> ```python
> def factorial(n: int) -> int:
>     if n < 0:
>         raise ValueError("n debe ser natural")
>     if n == 0:
>         return 1
>     return n * factorial(n - 1)
>
> print(factorial(4))
> # SALIDA:
> # 24
> ```
> 
> - `n == 0`: caso base.
> - `factorial(n - 1)`: llamada recursiva.
> - Cada llamada se acerca al caso base.

## RECURSIÓN, PILA DE LLAMADAS Y EFICIENCIA

En programación, cada llamada recursiva suele guardar información sobre su ejecución: argumentos, variables locales y el punto al que debe regresar. Esto se organiza habitualmente en la **pila de llamadas** (*call stack*).

> [!note] NOTA (para programadores)
> En `factorial(4)` se generan llamadas para `factorial(4)`, `factorial(3)`, `factorial(2)`, `factorial(1)` y `factorial(0)`. Cuando llega el caso base, los resultados se devuelven en orden inverso: $1$, $1$, $2$, $6$ y $24$.
> 
> Una profundidad excesiva puede provocar un error de desbordamiento o alcanzar el límite de recursión del lenguaje. Un problema recursivo también puede resolverse, en muchos casos, con **iteración**.

### FIBONACCI: SUBPROBLEMAS REPETIDOS

Al evaluar la definición recursiva ingenua de Fibonacci, $F_5$ requiere $F_4$ y $F_3$; a su vez, $F_4$ vuelve a calcular $F_3$. Este trabajo se repite muchas veces.

Una alternativa es la **memoización**: guardar los valores ya calculados. Otra es un algoritmo iterativo que mantiene los dos términos anteriores. Ambas opciones conservan la **misma definición matemática** pero pueden reducir el coste de cálculo.

```python
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n debe ser natural")
    anterior, actual = 0, 1
    for _ in range(n):
        anterior, actual = actual, anterior + actual
    return anterior
```

Esta versión iterativa calcula $F_n$ en un número de pasos proporcional a $n$ y utiliza una cantidad constante de variables auxiliares.

## EJERCICIOS DE COMPROBACIÓN

1. Calcula $a_3$ cuando $a_0 = 4$ y $a_n = a_{n - 1} + 3$.
2. ¿Por qué la definición $b_n = b_{n - 1} + 1$ no determina una sucesión única si no conocemos $b_0$?
3. Escribe una definición recursiva para $2^n$ con $n \ge 0$.

> [!abstract] SOLUCIONES
> 1. $a_1 = 7$, $a_2 = 10$ y $a_3 = 13$.
> 2. Porque cada posible valor inicial origina una sucesión diferente.
> 3. $f(0) = 1$ y $f(n) = 2f(n - 1)$ para $n \ge 1$.

## INDUCCIÓN ESTRUCTURAL

La **inducción estructural** demuestra propiedades sobre objetos **definidos recursivamente**, como listas, árboles y fórmulas lógicas.

- **Caso base:** demostrar la propiedad para los objetos iniciales.
- **Paso inductivo:** suponer que se cumple para los objetos más pequeños usados en una construcción y demostrar que también se cumple para el objeto construido.

> [!example] EJEMPLO
> **Propiedad:** toda fórmula lógica bien construida tiene el mismo número de paréntesis de apertura y cierre.
> 
> - **Caso base:** una variable [proposicional](logic/propositions.md) $p$ no tiene paréntesis.
> - **Paso inductivo:** si $p$ y $q$ tienen paréntesis equilibrados, también los tienen $(\neg p)$ y $(p \land q)$, ya que cada construcción añade un par completo.
> - **Conclusión:** se cumple para cualquier fórmula generada mediante esas reglas (y las análogas para los demás conectores).

## RELACIÓN CON LA INDUCCIÓN

- **Recursión:** sirve para **definir o calcular** objetos mediante casos anteriores.
- **Inducción:** sirve para **demostrar** propiedades sobre esos objetos.
- Ambas utilizan **casos base** y un paso que relaciona casos consecutivos (o más sencillos).

## RESUMEN

| CONCEPTO                 | FUNCIÓN                                              |
|:------------------------ |:---------------------------------------------------- |
| **Caso base**            | Define directamente un caso inicial.                 |
| **Regla recursiva**      | Obtiene un caso usando otros más sencillos.          |
| **Sucesión recursiva**   | Calcula términos a partir de términos anteriores.    |
| **Estructura recursiva** | Construye objetos a partir de otros más pequeños.    |
| **Inducción**            | Demuestra propiedades; no es lo mismo que recursión. |

> [!warning] ERRORES FRECUENTES
> - Olvidar definir un **caso base**.
> - Crear una regla que **no se acerque al caso base**.
> - No proporcionar suficientes casos iniciales (por ejemplo, Fibonacci necesita dos).
> - Confundir **definir algo recursivamente** con **demostrarlo por inducción**.
