---
aliases: [CMOS, Transistores en NAND, MOSFET]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# TRANSISTORES CMOS Y PUERTA NAND

> [!seealso]- MIRA TAMBIÉN
> - [Puertas lógicas](logic_gates.md)
> - [Otras puertas con NAND](nand_composition.md)

> [!important] CONCEPTOS IMPORTANTES
> - Un transistor MOSFET puede funcionar como un **interruptor controlado eléctricamente**.
> - En CMOS estático, los **nMOS** suelen formar la red que conecta la salida a tierra y los **pMOS** la que conecta a alimentación.
> - Una NAND de dos entradas se construye con **dos nMOS en serie** y **dos pMOS en paralelo**.
## DEL TRANSISTOR A LA LÓGICA DIGITAL

Un **MOSFET** tiene tres terminales funcionales principales: **puerta** (*gate*), **drenador** (*drain*) y **fuente** (*source*). La tensión entre la puerta y la fuente controla la conducción entre los otros dos terminales.

De manera **simplificada** para circuitos CMOS digitales:

- Un **nMOS** conduce cuando su puerta está a nivel lógico alto (`1`) respecto a su fuente; abierto cuando está bajo (`0`).
- Un **pMOS** conduce cuando su puerta está a nivel lógico bajo (`0`) respecto a su fuente; abierto cuando está alto (`1`).

> [!warning] MODELO SIMPLIFICADO
> Un MOSFET real tiene umbrales de tensión, capacitancias, resistencias y corrientes de fuga. La equivalencia “interruptor ideal” es útil para aprender la lógica, pero no describe todos sus efectos analógicos ni todas las condiciones posibles.

## INVERSOR CMOS: PUERTA NOT

Un **inversor** utiliza normalmente **un pMOS arriba** (hacia $V_{DD}$, alimentación) y **un nMOS abajo** (hacia GND, tierra); sus puertas reciben la misma señal $A$, y los drenadores se unen en la salida $Y$.

```text
        VDD (+)
          │
      [ pMOS ]  ← A
          │
          ├──────── Y
          │
      [ nMOS ]  ← A
          │
         GND
```

- Si `A=0`, conduce el pMOS y no el nMOS: la salida se conecta a VDD y vale `1`.
- Si `A=1`, no conduce el pMOS y sí el nMOS: la salida se conecta a GND y vale `0`.

## NAND CMOS DE DOS ENTRADAS

Una NAND produce $Y=\overline{A\land B}$. Necesitamos que la salida se conecte a tierra **solo cuando A y B sean 1**. Para ello, los **nMOS se ponen en serie**. La red pMOS es dual: **en paralelo**, para que alguno conecte la salida a VDD cuando al menos una entrada es 0.

```text
                VDD
               ┌──┴─────────┐
               │            │
           [pMOS A]      [pMOS B]
               │            │
               └─────┬──────┘
                     │
                     ├──────────── Y
                     │
                 [nMOS A]
                     │
                 [nMOS B]
                     │
                    GND
```

*Esquema conceptual de conexiones. Las etiquetas A y B señalan la señal que controla la puerta de cada transistor; no representan terminales de alimentación.*

| A | B | Camino nMOS a GND | Algún camino pMOS a VDD | Y |
| :-: | :-: | --- | --- | :-: |
| 0 | 0 | No | Sí | 1 |
| 0 | 1 | No | Sí | 1 |
| 1 | 0 | No | Sí | 1 |
| 1 | 1 | Sí | No | 0 |

Por ello, la implementación requiere **cuatro transistores** en el esquema CMOS estático convencional de dos entradas.

## NOR Y OTRAS FUNCIONES

La **NOR** de dos entradas usa los **pMOS en serie** y los **nMOS en paralelo**. Para construir **AND** con CMOS estático suele ser práctico crear NAND y añadir un inversor: 

$$A\land B=\overline{\operatorname{NAND}(A,B)}$$

De la misma manera, OR puede implementarse como NOR seguida de NOT.

## CONSUMO Y RETARDO

En condiciones estáticas ideales, una puerta CMOS complementaria conecta la salida a una alimentación **o** a tierra, no a ambas simultáneamente. Durante conmutaciones puede existir corriente transitoria y hay pérdidas por fugas. Las capacidades eléctricas también hacen que las salidas **no cambien instantáneamente**.

## MÁS ALLÁ DE DOS ENTRADAS

Una NAND CMOS de tres entradas tiene **tres nMOS en serie** y **tres pMOS en paralelo**; la red en serie permite llegar a GND solo cuando las tres entradas valen 1. El principio se generaliza a más entradas, aunque aparecen limitaciones prácticas de velocidad y dimensionamiento.

> [!external-link]- REFERENCIAS WEB
> - [MOSFET y CMOS (UCLA Tapeout Club)](https://ucla-tapeout-club.github.io/pd-wiki/docs/fundamentals/mosfets-and-cmos.html)
> - [NAND, NOR y puertas CMOS (NPTEL)](https://archive.nptel.ac.in/content/storage2/courses/117103066/chap1/slides/slide7.htm)
