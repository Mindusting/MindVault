---
aliases:
  - Principio de superposición
author: Mindusting
corrected: true
creationDate: 2026-11-09 03:14:27
headerFile: false
modificationDate: 2026-11-09 11:24:33
rating:
tags:
  - Electricity
---

# PRINCIPIO DE SUPERPOSICIÓN

> [!seealso]- MIRA TAMBIÉN
> - [Carga eléctrica](electric_charge.md)
> - [Ley de Coulomb](coulombs_law.md)
> - [Campo eléctrico](electric_field.md)

> [!important] CONCEPTOS IMPORTANTES
> - La fuerza eléctrica es una **magnitud vectorial**.
> - Cada carga ejerce una fuerza sobre las demás de forma independiente.
> - La fuerza resultante es la **suma vectorial** de todas las fuerzas.
> - Las fuerzas pueden sumarse o compensarse dependiendo de su dirección y sentido.
> - Una fuerza resultante nula no significa que no existan fuerzas individuales.

## DEFINICIÓN

El **principio de superposición** establece que la fuerza eléctrica total sobre una carga es igual a la suma vectorial de las fuerzas ejercidas por las demás cargas.

> [!abstract] FÓRMULA
> 
> $$\vec{F}_{total} = \sum_{i=1}^{n}\vec{F}_i$$
> 
> - $\vec{F}_{total}$: fuerza eléctrica resultante en Newtons ($N$).
> - $\vec{F}_i$: fuerza ejercida por cada carga en Newtons ($N$).
> - $n$: número de fuerzas que actúan sobre la carga.

Cada fuerza individual se calcula mediante la [ley de Coulomb](coulombs_law.md):

$$F = k\frac{|q_1 q_2|}{r^2}$$

> [!note] NOTA (para programadores)
> Si vienes del mundillo de la programación, el sumatorio de un conjunto de fuerzas es el equivalente a tener una lista de números (*siendo estas las fuerzas*), y se sumen todos los números.
> 
> Una pequeña diferencia que hay entre $i$ en la fórmula matemática y la `i` en el código, es que en matemáticas el *index* empieza por $1$ mientras que en programación empieza por `0`, pero la idea sigue siendo la misma.
> 
> ```python
> F = [3, 2, -8] # Conjunto de fuerzas
> n = len(F)     # Número de fuerzas
> 
> F_total = 0
> for i in range(n):
>     F_total += F[i]
> 
> print(f"Fuerza total: {F_total}")
> # SALIDA:
> # Fuerza total: -3
> ```
> 
> Una forma más compacta de hacerlo es usando la función `sum`, esta equivale más a lo que es un sumatorio, pero el código de arriba permite ver más equivalencias entre la fórmula matemática y el código.
> 
> ```python
> F = [3, 2, -8] # Conjunto de fuerzas
> 
> F_total = sum(F) # Cálculo del sumatorio
> 
> print(f"Fuerza total: {F_total}")
> # SALIDA:
> # Fuerza total: -3
> ```

## SUMA DE FUERZAS

### UNA DIMENSIÓN

Cuando las cargas están alineadas sobre un mismo eje, se utiliza el signo de cada fuerza para representar su sentido.

- **Positivo (+):** fuerza hacia la derecha.
- **Negativo (−):** fuerza hacia la izquierda.

> [!abstract] FÓRMULA
> 
> $$F_{total} = F_1 + F_2 + \cdots + F_n$$
> 
> Las fuerzas se introducen con su signo según el sentido elegido para el eje.

> [!example] EJEMPLO
> 
> $$
> F_1 = +8\ \mathrm{N}\\
> F_2 = -3\ \mathrm{N}\\
> F_{total} = 8 - 3 = +5\ \mathrm{N}
> $$
> 
> **Resultado:** una fuerza de $5\ \mathrm{N}$ hacia la derecha.

### DOS DIMENSIONES

Cuando las fuerzas tienen distintas direcciones, se suman sus componentes por separado.

> [!abstract] FÓRMULAS
> 
> $$F_x = \sum_{i = 1}^{n} F_{ix}$$
> 
> $$F_y = \sum_{i = 1}^{n} F_{iy}$$
> 
> La magnitud de la fuerza resultante es:
> 
> $$|\vec{F}_{total}| = \sqrt{F_x^2 + F_y^2}$$

## EJEMPLOS

> [!example] EJEMPLO 1 - TRES CARGAS EN LÍNEA
> Tenemos tres cargas:
> 
> - $q_A = +2\, \mu \mathrm{C}$ en $x = 0\ \mathrm{m}$.
> - $q_B = +1\, \mu \mathrm{C}$ en $x = 1\ \mathrm{m}$.
> - $q_C = +4\, \mu \mathrm{C}$ en $x = 3\ \mathrm{m}$.
> 
> Calculamos la fuerza total sobre $B$.
> 
> **1. Fuerza ejercida por $A$ sobre $B$:**
> 
> $$F_{AB} = 8.99 \times 10^9 \frac{(2 \times 10^{-6})(1 \times 10^{-6})}{1^2}$$
> 
> $$F_{AB} = +0.01798\ \mathrm{N}$$
> 
> Es positiva porque $A$ repele a $B$ hacia la derecha.
> 
> **2. Fuerza ejercida por $C$ sobre $B$:**
> 
> $$F_{CB} = 8.99 \times 10^9 \frac{(4 \times 10^{-6})(1 \times 10^{-6})}{2^2}$$
> 
> $$F_{CB} = -0.00899\ \mathrm{N}$$
> 
> Es negativa porque $C$ repele a $B$ hacia la izquierda.
> 
> **3. Fuerza resultante:**
> 
> $$F_{total} = F_{AB} + F_{CB}$$
> 
> $$F_{total} = 0.01798 - 0.00899$$
> 
> $$F_{total} = +0.00899\ \mathrm{N}$$
> 
> **Resultado:** una fuerza de $0.00899\ \mathrm{N}$ hacia la derecha.
> 
> %%
> 
> ```text
>  0m              1m                    3m
> A(+) --- 1m --- B(+) ------ 2m ------ C(+)
>     ===========>    <-----------------
> ```
> 
> %%
> 
> ![#center](assets/superposition_forces.excalidraw.md)

> [!example] EJEMPLO 2 - FUERZAS QUE SE COMPENSAN
> Tenemos tres cargas:
> 
> - $q_A = -2\,\mu \mathrm{C}$ en $x = -1\ \mathrm{m}$.
> - $q_B = +1\,\mu \mathrm{C}$ en $x = 0\ \mathrm{m}$.
> - $q_C = -2\,\mu \mathrm{C}$ en $x = 1\ \mathrm{m}$.
> 
> Calculamos la fuerza total sobre $B$.
> 
> **1. Fuerza ejercida por $A$:**
> 
> $$F_{AB} = -0.01798\ \mathrm{N}$$
> 
> **2. Fuerza ejercida por $C$:**
> 
> $$F_{CB} = +0.01798\ \mathrm{N}$$
> 
> **3. Fuerza resultante:**
> 
> $$F_{total} = -0.01798 + 0.01798 = 0\ \mathrm{N}$$
> 
> **Resultado:** las fuerzas se compensan y la fuerza resultante es nula.
> 
> %%
> 
> ```text
> -1m              0m              1m
> A(-) --- 1m --- B(+) --- 1m --- C(-)
>     <-----------    ----------->
> ```
> 
> %%
> 
> ![#center](assets/force_cancellation.excalidraw.md)
