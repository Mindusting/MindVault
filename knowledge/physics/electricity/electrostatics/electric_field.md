---
aliases: [Campo eléctrico]
author: Mindusting
corrected: false
creationDate: 2026-11-10 12:47:29
headerFile: false
modificationDate: 2026-11-10 12:50:05
rating: 
tags: [Electricity]
---

# CAMPO ELÉCTRICO

> [!seealso]- MIRA TAMBIÉN
> - [Carga eléctrica](electric_charge.md)
> - [Ley de Coulomb](coulombs_law.md)
> - [Principio de superposición](superposition_principle.md)
> - [Campo eléctrico de cargas discretas](electric_field_discrete_charges.md)

> [!important] CONCEPTOS IMPORTANTES
> - Toda carga eléctrica genera un **campo eléctrico** a su alrededor.
> - El campo eléctrico es una **magnitud vectorial**.
> - Su unidad es el **newton por culombio** ($\mathrm{N / C}$).
> - El campo eléctrico existe aunque no haya otra carga que experimente su fuerza.
> - El campo de una carga positiva apunta hacia fuera.
> - El campo de una carga negativa apunta hacia dentro.
> - La intensidad del campo de una carga puntual disminuye con el cuadrado de la distancia.

## DEFINICIÓN

El **campo eléctrico** ($\vec{E}$) es una magnitud vectorial que describe la fuerza eléctrica por unidad de carga positiva que experimentaría una carga de prueba situada en un punto del espacio.

> [!abstract] FÓRMULA
> 
> $$\vec{E} = \frac{\vec{F}}{q_0}$$
> 
> - $\vec{E}$: campo eléctrico ($\mathrm{N / C}$).
> - $\vec{F}$: fuerza eléctrica sobre la carga de prueba ($\mathrm{N}$).
> - $q_0$: carga de prueba positiva ($\mathrm{C}$).

La carga de prueba se considera suficientemente pequeña para no alterar significativamente la distribución de cargas que genera el campo.

## CAMPO ELÉCTRICO DE UNA CARGA PUNTUAL

El campo eléctrico generado por una carga puntual depende de la magnitud de dicha carga y de la distancia hasta el punto donde se calcula.

> [!abstract] FÓRMULA
> 
> $$E = k \frac{|Q|}{r^2}$$
> 
> - $E$: magnitud del campo eléctrico ($\mathrm{N / C}$).
> - $k$: constante de Coulomb ($\mathrm{N \cdot m^2 / C^2}$).
> - $Q$: carga que genera el campo ($\mathrm{C}$).
> - $r$: distancia desde la carga hasta el punto estudiado ($\mathrm{m}$).

En el vacío:

$$k \approx 8.99 \times 10^9\ \mathrm{N \cdot m^2 / C^2}$$

Esta fórmula permite calcular la **magnitud** del campo eléctrico. Su sentido depende del signo de $Q$.

## DIRECCIÓN Y SENTIDO

El campo eléctrico es una **magnitud vectorial**.

- **Dirección:** la recta que une la carga puntual con el punto estudiado.
- **Sentido:** depende del signo de la carga que genera el campo.
- **Magnitud:** se calcula mediante la fórmula del campo eléctrico.

### CARGA POSITIVA

El campo eléctrico apunta **hacia fuera** de la carga positiva.

### CARGA NEGATIVA

El campo eléctrico apunta **hacia dentro** de la carga negativa.

%%

```text
    ^           |
  \ | /       \ v /
<--(+)-->   -->(-)<--
  / | \       / ^ \
    v           |
```

%%

![#center](assets/electric_field_direction.excalidraw.md)

## LÍNEAS DE CAMPO ELÉCTRICO

Las **líneas de campo eléctrico** son representaciones gráficas que permiten visualizar la dirección, el sentido y la intensidad relativa de un campo eléctrico.

- Salen de las cargas positivas.
- Entran en las cargas negativas.
- Nunca se cruzan.
- Cuanto más juntas se representan, mayor es la intensidad del campo.
- La dirección del campo en cada punto es tangente a la línea que pasa por él.

> [!note] NOTA  
> Las líneas de campo son una representación gráfica, no trayectorias físicas que existan en el espacio.

%%

```txt
 /---->----\
/ /--->---\ \
\ \ /->-\ / /
 >(+)->-(-)<
/ / \->-/ \ \
\ \--->---/ /
 \---->----/
```

%%

![#center|300](assets/electric_field_lines.excalidraw.md)

## FUERZA SOBRE UNA CARGA

Cuando una carga eléctrica se encuentra dentro de un campo eléctrico, experimenta una fuerza.

> [!abstract] FÓRMULA
> 
> $$\vec{F} = q\vec{E}$$
> 
> - $\vec{F}$: fuerza eléctrica ($\mathrm{N}$).
> - $q$: carga que experimenta la fuerza ($\mathrm{C}$).
> - $\vec{E}$: campo eléctrico ($\mathrm{N/C}$).

El sentido de la fuerza depende del signo de la carga:

- **Carga positiva:** fuerza en el mismo sentido que el campo.
- **Carga negativa:** fuerza en sentido contrario al campo.

> [!important] IMPORTANTE  
> No debemos confundir la carga que **genera el campo** ($Q$) con la carga que **experimenta la fuerza** ($q$).

## EJEMPLOS

> [!example] EJEMPLO 1 - CALCULAR EL CAMPO ELÉCTRICO  
> Una carga positiva de $Q = +3,\mu\mathrm{C}$ genera un campo eléctrico. Calcula su magnitud a $2\ \mathrm{m}$ de distancia.
> 
> **1. Convertimos la carga:**
> 
> $$Q = 3\times10^{-6}\ \mathrm{C}$$
> 
> **2. Aplicamos la fórmula:**
> 
> $$E = k\frac{|Q|}{r^2}$$
> 
> $$E = 8.99\times10^9\frac{3\times10^{-6}}{2^2}$$
> 
> $$E = 6742.5\ \mathrm{N/C}$$
> 
> **Resultado:** un campo de $6742.5\ \mathrm{N/C}$ dirigido hacia fuera de la carga positiva.

> [!example] EJEMPLO 2 - CALCULAR LA FUERZA  
> Una carga de $q=-2,\mu\mathrm{C}$ se encuentra en un campo eléctrico uniforme de $E=500\ \mathrm{N/C}$ dirigido hacia la derecha.
> 
> **1. Convertimos la carga:**
> 
> $$q=-2\times10^{-6}\ \mathrm{C}$$
> 
> **2. Aplicamos la fórmula:**
> 
> $$F=qE$$
> 
> $$F=(-2\times10^{-6})\times500$$
> 
> $$F=-0.001\ \mathrm{N}$$
> 
> **Resultado:** una fuerza de $0.001\ \mathrm{N}$ hacia la izquierda, en sentido contrario al campo eléctrico.
