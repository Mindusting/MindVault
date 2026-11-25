---
aliases: [Bit, Byte]
author: Mindusting
corrected: false
creationDate: 2026-11-24 04:29:24
headerFile: false
modificationDate: 2026-11-24 06:10:17
rating: 
tags: [Binary, DigitalLogic]
---

# BITS, BYTES Y UNIDADES

> [!seealso]- MIRA TAMBIÉN
> - [Sistema posicional](positional_systems.md)
> - [Enteros sin signo](../representation/unsigned_integers.md)

> [!important] CONCEPTOS IMPORTANTES
> - Un **bit** almacena o comunica una elección entre dos estados lógicos.
> - Un **byte** moderno se define convencionalmente como **8 bits**; no todos los sistemas históricos han utilizado bytes de ocho bits.
> - Los prefijos decimales (`kB`, `MB`) y binarios (`KiB`, `MiB`) no significan lo mismo.

## DEFINICIÓN

Un **bit** (*binary digit*) es la unidad básica de información binaria y toma uno de dos valores: `0` o `1`. Físicamente, estos estados pueden codificarse mediante niveles de tensión, carga, magnetización u otros mecanismos. **Un 1 lógico no implica necesariamente que circule corriente y un 0 que no circule:** depende de la tecnología y del convenio eléctrico.

Un **byte** es una agrupación de **8 bits** en los sistemas modernos. En C, el término *byte* está ligado al tamaño de `char`, que tiene al menos ocho bits, aunque puede tener más en una implementación.

```text
1 bit:       1
4 bits:      1101  (nibble o semibyte)
8 bits:      1101 0010  (byte habitual)
16 bits: 1010 1111 0011 0101
```

## CAPACIDAD DE REPRESENTACIÓN

Un grupo de $n$ bits tiene $2^n$ combinaciones distintas:

> [!abstract] FÓRMULA
> 
> $$N = 2^n$$
> 
> - $n$: número de bits.
> - $N$: combinaciones disponibles.

| Bits | Combinaciones | Ejemplo                |
| ----:| -------------:|:---------------------- |
|    1 |             2 | `0` a `1`              |
|    4 |            16 | `0000` a `1111`        |
|    8 |           256 | Un byte                |
|   16 |        65 536 | Una palabra de 16 bits |

Las combinaciones **no tienen por qué representar números**; su interpretación depende del formato acordado.

## UNIDADES DE ALMACENAMIENTO

| Unidad decimal |           Valor | Unidad binaria |          Valor |
| -------------- | ---------------:| -------------- | --------------:|
| 1 kB           |    $10^3$ bytes | 1 KiB          | $2^{10}$ bytes |
| 1 MB           |    $10^6$ bytes | 1 MiB          | $2^{20}$ bytes |
| 1 GB           |    $10^9$ bytes | 1 GiB          | $2^{30}$ bytes |
| 1 TB           | $10^{12}$ bytes | 1 TiB          | $2^{40}$ bytes |

> [!note] NOTA
> La `B` mayúscula significa *byte*; la `b` minúscula, *bit*. Una conexión de `100 Mb/s` transmite teóricamente `12,5 MB/s` de datos antes de contabilizar las sobrecargas del protocolo.

## ORDEN DE LOS BYTES Y DE LOS BITS

En un número de varios bytes, **endianness** indica en qué orden se colocan los bytes en memoria. Por ejemplo, `0x12345678` en cuatro bytes:

```text
Direcciones crecientes:  +0   +1   +2   +3
Big-endian:              12   34   56   78
Little-endian:           78   56   34   12
```

Esto es distinto del orden gráfico de los bits dentro de un byte o del orden de transmisión de bits en un protocolo.

## EJEMPLO

> [!example] EJEMPLO—TAMAÑO DE UNA MÁSCARA
> Con 8 bits hay $2^8 = 256$ patrones. Si cada bit representa un permiso independiente, una máscara puede combinar ocho permisos distintos, y **no** 256 permisos.

## EJERCICIOS

1. ¿Cuántos patrones distintos tienen 12 bits?
2. ¿Cuántos bytes son 2 KiB?
3. ¿Qué diferencia existe entre 10 MB y 10 MiB?
