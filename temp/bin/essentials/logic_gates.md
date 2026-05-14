---
aliases: [Puertas lógicas]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Binary]
---

# PUERTAS LÓGICAS

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

![#center](assets/conversion_schema.excalidraw.md)

## NOT

![#logo](../../../imgs/logic_gate_not.png)

## AND

![#logo](../../../imgs/logic_gate_and.png)

## OR

![#logo](../../../imgs/logic_gate_or.png)

## XOR

![#logo](../../../imgs/logic_gate_xor.png)

## NAND

![#logo](../../../imgs/logic_gate_nand.png)

## NOR

![#logo](../../../imgs/logic_gate_nor.png)

## XNOR

![#logo](../../../imgs/logic_gate_xnor.png)

%%

# BINARIO

## PUERTAS LÓGICAS

### NOT

La puerta lógica **NOT** está compuesta por una entrada y una salida.

| A | S |
|:-:|:-:|
| 0 | 1 |
| 1 | 0 |

### AND

| A | B | S |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### OR

![#logo](assets/or.excalidraw.md)

| A | B | S |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### XOR

![#logo](../../imgs/logic_gate_xor.png)

> [!note]
> Si el número de inputs es par, las reglas son las siguientes:
> 1. Si los inputs son todos iguales el resultado es False.
> 2. Si el número de Falses es igual al número de Trues el resulado es False.
> 3. Si el número de Falses es diferente del número de Trues, el resulado es True.
> 
> Si el número de inputs es inpar, las reglas son las siguientes:
> 4. Si todos los inputs son Trues el resulado es True.
> 5. Si todos los inputs son Falses el resulado es False.
> 6. Si el número de Trues es mayor que Falses, el resultado es False.
> 7. Si el número de Falses es mayor que Trues, el resultado es True.

| A | B | S |
|:-:|:-:|:-:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

## FORMAS DE INTERPRETAR EL BINARIO

- [ENTERO](bin_int.md)
- [DECIMALES](bin_float.md)

## OPERAR EN BINARIO

- [SUMA](bin_add.md)

# OTROS

- [Multiplexer](bin_multiplexer.md)
- [De-Multiplexer](bin_de-multiplexer.md)

%%
