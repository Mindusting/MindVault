---
aliases: []
author: Mindusting
corrected: false
creationDate: 2026-11-24 04:29:24
headerFile: false
modificationDate: 2026-11-24 06:51:15
rating: 
tags: [Binary, DigitalLogic]
---

# ENTEROS SIN SIGNO

> [!seealso]- MIRA TAMBIÉN
> - [Complemento a dos](twos_complement.md)
> - [Sumador / restador](../arithmetic/adder_subtractor.md)

> [!important] CONCEPTOS IMPORTANTES
> - Un entero **sin signo** usa todas las combinaciones para representar números no negativos.
> - Con $n$ bits, el rango es de $0$ a $2^n - 1$.
> - Las operaciones con ancho fijo pueden desbordarse y perder bits más significativos.

## DEFINICIÓN

En la representación **sin signo** (*unsigned*), cada patrón de $n$ bits se interpreta como un entero no negativo en base 2. Todos los bits contribuyen al valor; no hay bit reservado al signo.

> [!abstract] RANGO
> 
> $$0 \le x \le 2^n - 1$$

| Bits | Mínimo |        Máximo |
| ----:| ------:| -------------:|
|    4 |      0 |            15 |
|    8 |      0 |           255 |
|   16 |      0 |        65 535 |
|   32 |      0 | 4 294 967 295 |

## INTERPRETACIÓN

```text
1001 0110 = 128 + 16 + 4 + 2 = 150
```

Los ceros iniciales no cambian el valor, pero sí indican **cuántos bits** ocupan el dato cuando trabajamos con circuitos o tipos de tamaño fijo.

## DESBORDAMIENTO

En $n$ bits, la suma sin signo se calcula módulo $2^n$ si se descarta el acarreo final:

> [!abstract] FÓRMULA
> 
> $$\operatorname{resultado} = (A + B) \bmod 2^n$$

> [!example] EJEMPLO—8 BITS
> 
> ```text
>   1111 1111   (255)
> + 0000 0001   (1)
> ------------
> 1 0000 0000   (256, requiere 9 bits)
>   0000 0000   (resultado almacenado en 8 bits)
> ```
> 
> El acarreo de salida vale 1, pero no forma parte del resultado de 8 bits.

## EXTENSIÓN A MÁS BITS

Para convertir un entero sin signo a un ancho mayor, añadimos **ceros** a la izquierda:

```text
 8 bits:           1111 1011 (251)
16 bits: 0000 0000 1111 1011 (251)
```

Esto es diferente de la extensión de signo para enteros negativos.
