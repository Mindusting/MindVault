---
aliases: [Recursión en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-23 03:52:00
headerFile: false
modificationDate: 2026-11-02 03:39:31
rating: 
tags: [Math]
---

# RECURSIÓN

> [!seealso]- MIRA TAMBIÉN
> - [Inducción matemática](induction.md)
> - [Proposiciones](propositions.md)
> - [Métodos de demostración](proof_methods.md)

La **recursión** es una técnica que permite definir una **función, sucesión o estructura** utilizando versiones más pequeñas de sí misma.

Una definición recursiva necesita:

- **Caso base:** define directamente uno o varios casos iniciales.
- **Regla recursiva:** define los demás casos a partir de otros más sencillos.

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
> n != \begin{cases}
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
