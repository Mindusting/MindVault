---
aliases: [Carga eléctrica]
author: Mindusting
corrected: false
creationDate: 2026-11-04 03:36:51
headerFile: false
modificationDate: 2026-11-05 08:01:20
rating: 
tags: [Electricity]
---

# CARGA ELÉCTRICA

> [!seealso]- MIRA TAMBIÉN
> - [Ley de Coulomb](coulombs_law.md)
> - [Campo eléctrico](electric_field.md)

> [!info] CONCEPTOS IMPORTANTES
> - La carga eléctrica es una magnitud **escalar con signo**.
> - Un cuerpo neutro puede contener muchas cargas eléctricas; su carga neta es cero.
> - Ganar electrones hace que la carga sea más negativa.
> - Perder electrones hace que la carga sea más positiva.
> - La cuantización y la conservación son propiedades diferentes: la primera establece los valores permitidos y la segunda que la carga total se mantiene constante en un sistema aislado.

## DEFINICIÓN

La **carga eléctrica** es una propiedad física de la materia que determina cómo interactúan eléctricamente las partículas.

Existen dos tipos de carga:

- **Positiva (+):** como la de los protones.
- **Negativa (−):** como la de los electrones.

Las cargas del mismo signo se repelen y las de signo contrario se atraen.

%%

```text
  Atracción   |   Repulsión
(+) -> <- (-) | <- (+) (+) ->
              | <- (-) (-) ->
```

%%

![#center|300](assets/attraction_and_repulsion.excalidraw.md)

### PARTÍCULAS SUBATÓMICAS

Las **partículas subatómicas** son aquellas que forman los **átomos**, hay tres tipos de **partículas subatómicas**, cada una de ellas tiene una **carga eléctrica** distinta; para medir la **carga eléctrica** se usa la constante $e$ con un valor de $1.602176634 \times 10^{-19}\ \mathrm{C}$ ([*Culombio*](#UNIDAD%20DE%20MEDIDA)), pudiendo llegar a ser positivo, negativo o neutro.

| PARTÍCULA | CARGA |
|:--------- |:-----:|
| Protón    | $+e$  |
| Electrón  | $-e$  |
| Neutrón   |  $0$  |

%%

```text
     ......(-)
   ..         ..
  .     (+)     .
  .   (0) (0)   .
  .     (+)     .
   ..         ..
     (-)......
```

%%

![#center|300](assets/atom.excalidraw.md)

> [!note] NOTA
> El **átomo** de este ejemplo tiene una [**carga eléctrica neutra**](#^neutral-electrical-status), ya que el número de protones y electrónes es el mismo, por lo que la carga positiva y negativa se cancelan.

### ESTADO ELÉCTRICO DE UN CUERPO

Dependiendo del valance de la cantidade protones y electrones dentro de un cuerpo, se puede clasificar dicho cuerpo con uno de los siguientes tres estados:

- **Neutro:** igual cantidad de protones y electrones.
^neutral-electrical-status
- **Positivo:** déficit de electrones.
- **Negativo:** exceso de electrones.

En los procesos habituales de electrización, son los electrones los que se transfieren entre cuerpos.

%%

```text
Objeto neutro
+--------------------+
| (-)         (-)(+) |
|   (+)   (+)        |
|          (-)       |
+--------------------+

Objeto positivo
+--------------------+
| (-)         (-)(+) |
|   (+)   (+)        |
|                    |
+--------------------+

Objeto negativo
+--------------------+
| (-)         (-)(+) |
|   (+)              |
|          (-)       |
+--------------------+
```

%%

![#center|300](assets/electrical_status.excalidraw.md)

## UNIDAD DE MEDIDA

La unidad de carga eléctrica en el ==Sistema Internacional== es el **culombio (C)**.

| UNIDAD        | SÍMBOLO |      EQUIVALENCIA      |
|:------------- |:-------:|:----------------------:|
| Miliculombio  |   mC    | $10^{-3}\ \mathrm{C}$  |
| Microculombio |   µC    | $10^{-6}\ \mathrm{C}$  |
| Nanoculombio  |   nC    | $10^{-9}\ \mathrm{C}$  |
| Picoculombio  |   pC    | $10^{-12}\ \mathrm{C}$ |

## CUANTIZACIÓN DE LA CARGA

La carga eléctrica está **cuantizada** ($Q$): la carga neta de un cuerpo se expresa como un múltiplo entero de la carga elemental.

> [!abstract] FÓRMULA
> 
> $$Q = n \cdot e$$
> 
> - $Q$: carga eléctrica neta (*[C](#UNIDAD%20DE%20MEDIDA)*).
> - $n$: número entero (*puede ser: positivo, negativo o cero*); se calcula restando la cantidad de electrones a la cantidad de protones ($N_p - N_e$).
> - $e$: carga elemental[^electric-charge] (*[C](#UNIDAD%20DE%20MEDIDA)*).

Para calcular la carga a partir del número de protones y electrones:

$$Q = (N_p - N_e) \cdot e$$

- $N_p$: número de protones.
- $N_e$: número de electrones.

> [!example] EJEMPLO
> Un cuerpo tiene 8 protones y 11 electrones.
> 
> $$Q = (8 - 11) e = -3e$$
> 
> $$Q \approx -4.807 \times 10^{-19}\ \mathrm{C}$$
> 
> El cuerpo tiene carga negativa.

## CONSERVACIÓN DE LA CARGA

La **carga eléctrica total de un sistema aislado permanece constante**; la carga no se crea ni se destruye, únicamente se transfiere entre cuerpos.

> [!abstract] FÓRMULA
> 
> $$Q_{\text{inicial}} = Q_{\text{final}}$$

### TRANSFERENCIA DE ELECTRONES

- Si un cuerpo **gana electrones**, su carga disminuye en $e$ por cada electrón ganado.
- Si un cuerpo **pierde electrones**, su carga aumenta en $e$ por cada electrón perdido.

> [!example] EJEMPLO
> Dos cuerpos neutros, $A$ y $B$. El cuerpo $A$ transfiere 4 electrones al cuerpo $B$.
> 
> Cuerpo $A$:
> 
> $$Q_A = +4e$$
> 
> Cuerpo $B$:
> 
> $$Q_B = -4e$$
> 
> Carga total:
> 
> $$Q_{\text{total}} = +4e -4e = 0$$
> 
> La carga total se conserva.

%%

```text
Antes del contacto   Después del contacto
   100e-    50e-         75e-    75e-
   ( ) ---> ( )          ( ) ---> ( )
                             25e-
---------------------------------------->
Antes del contacto   Después del contacto
   100e+    50e+         75e+    75e+
   ( ) <--- ( )          ( ) <--- ( )
                             25e-
```

%%

![#center|400](assets/electron_transfer.excalidraw.md)

[^electric-charge]: $1.602176634 \times 10^{-19}\ \mathrm{C}$
