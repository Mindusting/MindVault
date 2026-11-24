---
aliases: [Flip-flop, Registro, Secuencial]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# CIRCUITOS SECUENCIALES Y REGISTROS

> [!seealso]- MIRA TAMBIÉN
> - [Multiplexadores](multiplexers_demultiplexers.md)
> - [Sumador completo](../arithmetic/full_adder.md)
> - [ALU](../arithmetic/alu.md)

> [!important] CONCEPTOS IMPORTANTES
> - Un circuito **combinacional** depende de las entradas actuales; uno **secuencial** también del estado almacenado.
> - Los **biestables** (*flip-flops*) pueden retener un bit.
> - Varios biestables forman **registros** que permiten almacenar palabras binarias.
## COMBINACIONAL FRENTE A SECUENCIAL

Un sumador o un MUX puramente combinacional no “recuerda” un resultado: dadas las mismas entradas estables, produce la misma salida. Un **circuito secuencial** añade memoria; su salida puede depender del estado anterior.

```text
Combinacional:   entradas ──► lógica ──► salidas

Secuencial:      entradas ──► lógica ──► salidas
                               ▲   │
                               │   ▼
                              estado
```

## LATCH Y FLIP-FLOP

- **Latch:** elemento sensible a nivel; mientras está habilitado puede seguir la entrada, dependiendo de su implementación.
- **Flip-flop:** elemento normalmente sensible a un **flanco de reloj**; captura la entrada en un instante asociado al flanco y mantiene su estado hasta la siguiente actualización.

### FLIP-FLOP TIPO D

Un biestable D de flanco ascendente tiene entrada de datos `D`, reloj `CLK` y salida `Q`:

| Evento | Q después del evento |
| --- | --- |
| Flanco ascendente de CLK | Valor presente en D al capturar |
| Sin flanco de captura | Mantiene Q anterior |

> [!note] NOTA
> El muestreo correcto exige respetar tiempos de **setup** y **hold** alrededor del flanco. No todos los cambios de D son seguros: si ocurren demasiado cerca del flanco, puede aparecer metastabilidad.

## REGISTROS

Un **registro** de 8 bits puede implementarse con ocho flip-flops D que comparten el reloj. Cada uno almacena un bit del dato de entrada.

> [!example] EJEMPLO
> - Antes del flanco, el registro contiene `0011 0001`.
> - En las entradas D se presenta `1010 0110`.
> - En el siguiente flanco de captura, el registro actualiza su salida a `1010 0110`.
> - Si no llega otro flanco de captura, conserva ese estado (suponiendo alimentación y funcionamiento normales).

Un registro con señal **ENABLE** puede mantener el estado mientras `ENABLE=0`. Un MUX delante de cada D puede elegir entre el valor antiguo y el dato nuevo:

$$D_{\text{FF}}=\overline{EN}\cdot Q+EN\cdot DATA$$

## CONTADORES Y MEMORIAS

- Un **contador** actualiza su valor en cada evento de reloj, por ejemplo incrementando en uno.
- Un **registro de desplazamiento** mueve su contenido una posición por ciclo.
- Las memorias almacenan conjuntos más grandes de bits y utilizan circuitos de direccionamiento, lectura y escritura.

## POR QUÉ IMPORTA EL RELOJ

La lógica combinacional tarda un tiempo en estabilizar su salida. El reloj permite organizar cuándo se aceptan nuevos resultados. Esto facilita diseñar sistemas digitales de múltiples etapas, aunque introduce requisitos de temporización.

## EJERCICIOS

1. ¿Puede un circuito combinacional puro recordar una entrada pasada?
2. ¿Cuántos flip-flops D hacen falta para un registro de 32 bits?
3. ¿Qué hace un registro si `ENABLE=0` y no existe otra condición de actualización?
