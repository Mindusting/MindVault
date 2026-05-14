---
aliases: [Binario, Binary]
author: Mindusting
corrected: false
cssclasses: [center-table]
headerFile: true
rating: 
tags: [Binary]
---

<h1 style="text-align:center;">BINARY</h1>

![#logo](../../imgs/retro_monitor.png)

---

# BINARIO

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [Wikipedia](https://en.wikipedia.org/wiki/Byte) #WWW/Wikipedia
> 
> YouTube:
> - [Core Dumped](https://youtu.be/HjneAhCy2N4) #WWW/YT/CoreDumped
> - [Josh's Channel](https://youtu.be/PMpNhbMjDj0) #WWW/YT/JoshsChannel

> [!note] NOTA
> Esta documentación está oriendada al binario en la informática, por lo que si no sabes nada de binario, primero te recomiendo mirar la documentación del [**sistema numérico binario**](../../knoledge/mathematic/number_system/math_ns_bin.md), ya que biene bien como introducción.

## UNIDADES DE MEDIDA

En la informática existen muchas unidades de medida además de tener nombre parecidos, esto suele probocar que la gente las confunda.

> [!nota] NOTA
> Si eres usuario de Windows lo más probable es que pienses que *1 MegaByte* son *1024 kiloBytes*, cosa que no es cierta, y es que Windows todabía (*estoy escribiendo esto en 2026-03-18*) no se ha adaptado al estandar que estableció la **Comisión Electrotécnica Internacional** (*IEC*) en **1998**; por lo qué, supongo que de ahí es que la gente sigue confundiendolos.

| Nombre    | Sím. | Nombre   | Sím. | Nombre   | Sím. | Nombre  | Sím. |
|:--------- |:----:|:-------- |:----:|:-------- |:----:|:------- |:----:|
| KiloByte  |  kB  | KibiByte | kiB  | Kilobit  |  kb  | Kibibit | kib  |
| MegaByte  |  MB  | MebiByte | MiB  | Megabit  |  Mb  | Mebibit | Mib  |
| GigaByte  |  GB  | GibiByte | GiB  | Gigabit  |  Gb  | Gibibit | Gib  |
| TeraByte  |  TB  | TebiByte | TiB  | Terabit  |  Tb  | Tebibit | Tib  |
| PetaByte  |  PB  | PebiByte | PiB  | Petabit  |  Pb  | Pebibit | Pib  |
| ExaByte   |  EB  | ExbiByte | EiB  | Exabit   |  Eb  | Exbibit | Eib  |
| ZettaByte |  ZB  | ZebiByte | ZiB  | Zettabit |  Zb  | Zebibit | Zib  |
| YottaByte |  YB  | YobiByte | YiB  | Yottabit |  Yb  | Yobibit | Yib  |

## PUERTAS LÓGICAS

### NOT

![#logo](../../imgs/logic_gate_not.png)


### AND

![#logo](../../imgs/logic_gate_and.png)

### OR

![#logo](../../imgs/logic_gate_or.png)

### XOR

![#logo](../../imgs/logic_gate_xor.png)

### NAND

![#logo](../../imgs/logic_gate_nand.png)

### NOR

![#logo](../../imgs/logic_gate_nor.png)

### XNOR

![#logo](../../imgs/logic_gate_xnor.png)

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
> 1. Si todos los inputs son Trues el resulado es True.
> 2. Si todos los inputs son Falses el resulado es False.
> 3. Si el número de Trues es mayor que Falses, el resultado es False.
> 4. Si el número de Falses es mayor que Trues, el resultado es True.

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
