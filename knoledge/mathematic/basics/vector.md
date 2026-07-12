---
aliases: [Vectores en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-06-30 10:34:40
headerFile: false
modificationDate: 2026-06-30 06:20:40
rating: 
tags: [Math]
---

# VECTORES EN MATEMÁTICAS

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

Un **vector** es un conjunto de [escalares](scalar.md) (*tendiendo este dos o más [escalares](scalar.md)*); sirve para repesentar una posición, velocidad o fuerza, entre otros; este suele representarse de tres formas distintas, el cual escojas usar depederá fuertemente de en el ámbito en el que te muevas:

1. **Matemáticos**: estos suelen ver los vectores como una letra con una flecha sobre ella que apunta a la derecha ($\vec{v}$); estas se utilizan en funciónes.
2. **Físicos**: estos suelen ver los vectores como una flecha con dirección y sentido, esta permite indicar la posición (*respecto a un punto de origen*), una velocidad o fuerza aplicada sobre un elemento físico.
3. **Programadores**: estos suelen ver los vectores como una lista ordenada de números, es decir, a la hora de trabajar con un vector de dos dimensiones, este sería una lista con dos número (*el número $x$ y el número $y$, estando estos siempre en este orden*).

En cualquier caso las tres formas de representar los **vectores** son eso mismo, una forma de representarlos, por lo que podemos una forma de representación u otra en base a nuestra combeniencia.

Imaginemos que tenemos los **vectores** $\vec{a}$ y $\vec{b}$ y queremos sumarlos para crear así el **vector** $\vec{c}$, podremos ver las tres formas de representar el mismo proceso se suma de los dos vectores:

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

---

```py
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

---

![#center](assets/vector_fisico.md)

## MÓDULO

El **módulo** de un **vector** es la longitud de la flecha que representa dicho **vector**, para calcular este valor

$$
\lVert \vec{v} \rVert
$$
