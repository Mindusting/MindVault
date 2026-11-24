---
aliases: [Encoder, Decoder, Priority encoder]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# CODIFICADORES Y DECODIFICADORES

> [!seealso]- MIRA TAMBIÉN
> - [Multiplexadores y demultiplexadores](multiplexers_demultiplexers.md)
> - [Álgebra de Boole](../logic/boolean_algebra.md)

> [!important] CONCEPTOS IMPORTANTES
> - Un **decodificador** activa una salida asociada a una combinación de entradas binarias.
> - Un **codificador** obtiene un código binario a partir de una entrada activa.
> - Un **codificador prioritario** resuelve los casos en que varias entradas están activas a la vez.
## DECODIFICADOR

Un **decodificador** $n:2^n$ recibe $n$ bits y genera hasta $2^n$ salidas. En un modelo **activo en alto**, exactamente una salida vale 1 para cada código válido (si está habilitado).

### DECODIFICADOR 2:4

Entradas `A` (bit alto) y `B` (bit bajo):

| A | B | Y0 | Y1 | Y2 | Y3 |
| :-: | :-: | :-: | :-: | :-: | :-: |
| 0 | 0 | 1 | 0 | 0 | 0 |
| 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 | 1 | 0 |
| 1 | 1 | 0 | 0 | 0 | 1 |

> [!abstract] ECUACIONES
> $$Y_0=\overline A\land\overline B$$
> $$Y_1=\overline A\land B$$
> $$Y_2=A\land\overline B$$
> $$Y_3=A\land B$$

Para construirlo bastan inversores para A y B y cuatro puertas AND (o una red de NAND con salida activa en bajo, según el diseño).

## CODIFICADOR

Un **codificador** hace la operación conceptual inversa: transforma la posición de una entrada activa en un código binario.

### CODIFICADOR 4:2 DE UNA ENTRADA ACTIVA

| Entrada activa | A | B |
| --- | :-: | :-: |
| D0 | 0 | 0 |
| D1 | 0 | 1 |
| D2 | 1 | 0 |
| D3 | 1 | 1 |

Suponiendo que exactamente una entrada está a `1`:

$$A=D_2\lor D_3$$

$$B=D_1\lor D_3$$

Esta tabla **no define una salida única para entradas múltiples activas**. Por ejemplo, con D1 y D2 activadas la expresión simple daría `11`, aunque D3 no esté activa. Tampoco permite distinguir D0 de ninguna entrada activa sin una señal adicional de validez.

## CODIFICADOR CON PRIORIDAD

Un **codificador prioritario** define qué entrada gana cuando varias están activas. Si D3 tiene la máxima prioridad, seguido de D2, D1 y D0:

| Entradas activas | Código elegido |
| --- | --- |
| D3 y cualquiera de las otras | `11` |
| D2 (sin D3) | `10` |
| D1 (sin D3 ni D2) | `01` |
| Solo D0 | `00` |
| Ninguna | `00` y `VALID=0` |

Una salida **VALID** indica si existe alguna entrada activa; evita confundir “sin datos” con D0.

## DIFERENCIAS CON DEMUX

Un decodificador genera una línea activa a partir de un **código de selección**. Un DEMUX añade además un **dato de entrada** que se dirige a la salida seleccionada. Por tanto, un DEMUX 1:4 puede implementarse utilizando un decodificador 2:4 cuyas salidas se combinan con la señal de datos mediante AND.

## APLICACIONES

- Selección de registros, memorias o periféricos.
- Decodificación de instrucciones de un procesador.
- Teclados y gestión de interrupciones con prioridad.

## EJERCICIOS

1. En un decodificador 3:8, ¿cuántas salidas hay?
2. ¿Qué salida debe activarse en el decodificador 2:4 con `A=1`, `B=0`?
3. ¿Por qué un codificador 4:2 sin prioridad no admite entradas arbitrarias?
