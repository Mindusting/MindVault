---
aliases: [IEEE 754, Números de coma flotante, Float, Double]
author: Mindusting
corrected: false
creationDate: 2026-11-24 04:29:24
headerFile: false
modificationDate: 2026-11-24 06:25:18
rating: 
tags: [Binary, DigitalLogic]
---

# COMA FLOTANTE: IEEE 754

> [!external-link]- REFERENCIAS WEB
> - [IEEE 754: formatos y redondeo (University of Maryland)](https://www.math.umd.edu/~petersd/466/ieee754h.html)
> - [IEEE y subnormales (Oracle Numerical Computation Guide)](https://docs.oracle.com/cd/E37069_01/html/E39019/z4000ac019677.html)
> - [Documentación de `struct` en Python](https://docs.python.org/3/library/struct.html)

> [!seealso]- MIRA TAMBIÉN
> - [Conversión entre bases](../fundamentals/conversions.md)
> - [Coma fija](fixed_point.md)
> - [Enteros con signo](twos_complement.md)

> [!important] CONCEPTOS IMPORTANTES
> - Un número en coma flotante se representa mediante **signo, exponente y significando**.
> - **binary32** ocupa 32 bits y **binary64** ocupa 64 bits; ambos son formatos binarios definidos por IEEE 754.
> - No todos los números decimales se representan exactamente, por ejemplo $0.1$.
> - Existen codificaciones especiales para **ceros con signo**, **infinito**, **NaN** y **subnormales**.

## DEFINICIÓN

Los números de **coma flotante** (*floating-point*) permiten representar valores de magnitudes muy distintas sin fijar la posición de la coma. Se parecen a la notación científica, pero en los formatos binarios la base es 2:

$$13.25_{10} = 1101.01_2 = 1.10101_2 \times 2^3$$

El estándar **IEEE 754** establece formatos y reglas para la aritmética de coma flotante, incluidos determinados resultados especiales y modos de redondeo. Los formatos `binary32` y `binary64` son los más habituales, aunque el estándar define otros.

## ESTRUCTURA DE LOS FORMATOS BINARIOS

| Campo                                               | binary32 | binary64 |
| --------------------------------------------------- | --------:| --------:|
| Signo $s$                                           |    1 bit |    1 bit |
| Exponente almacenado $E$                            |   8 bits |  11 bits |
| Fracción almacenada $F$                             |  23 bits |  52 bits |
| Sesgo (*bias*)                                      |      127 |     1023 |
| Precisión del significando (incluido bit implícito) |  24 bits |  53 bits |

```text
binary32 (32 bits):
┌─┬────────┬───────────────────────┐
│S│ E (8)  │      F (23)           │
└─┴────────┴───────────────────────┘

binary64 (64 bits):
┌─┬───────────┬────────────────────────────────────────────────────┐
│S│  E (11)   │                      F (52)                        │
└─┴───────────┴────────────────────────────────────────────────────┘
```

Para un número **normalizado**, el significando comienza por `1.`; ese primer 1 se omite porque se sobreentiende.

> [!abstract] VALOR NORMALIZADO
> 
> $$x = (-1)^s\, (1 + F / 2^f)\, 2^{E - \mathrm{bias}}$$
> 
> - $s \in \{0, 1\}$: bit del signo.
> - $F$: entero codificado en los $f$ bits del campo fracción.
> - $f = 23$ para `binary32` y $f = 52$ para `binary64`.
> - $E$: exponente almacenado interpretado como entero **sin signo**; en números normales está entre 1 y el penúltimo valor disponible.

## CONVERTIR UN NÚMERO A BINARY32

> [!example] EJEMPLO RESUELTO—ALMACENAR $13.25$
> 
> **1. Convertir a binario.**
> 
> $$13.25_{10} = 1101.01_2$$
> 
> **2. Normalizar.**
> 
> $$1101.01_2 = 1.10101_2 \times 2^3$$
> 
> **3. Obtener los tres campos.**
> 
> - Signo: `0` (es positivo).
> - Exponente real: `3`; almacenado: $E = 3 + 127 = 130 = 10000010_2$.
> - Fracción: los bits que siguen a `1.` son `10101`, completados con ceros hasta 23 bits: `10101000000000000000000`.
> 
> **4. Unir los campos.**
> 
> ```text
> s | exponente | fracción
> 0 | 10000010  | 10101000000000000000000
> 
> Patrón completo:
> 0100 0001 0101 0100 0000 0000 0000 0000
> Hexadecimal: 0x41540000
> ```
> 
> Cambiar solo el bit $s$ a 1 produce $-13.25$ (*hexadecimal `0xC1540000`*).

## VALORES ESPECIALES

Para `binary32`, sea `E` el campo de 8 bits y `F` el campo de 23 bits:

| Exponente                     | Fracción         | Interpretación           |
|:----------------------------- |:---------------- |:------------------------ |
| `00000000`                    | Todo cero        | $+0$ o $-0$, según `s`   |
| `00000000`                    | Distinta de cero | Número **subnormal**     |
| Entre `00000001` y `11111110` | Cualquiera       | Número **normal**        |
| `11111111`                    | Todo cero        | $+\infty$ o $-\infty$    |
| `11111111`                    | Distinta de cero | **NaN** (*Not a Number*) |

### SUBNORMALES

Los **subnormales** permiten representar valores no nulos más próximos a cero que el menor número normalizado, a costa de perder bits significativos de precisión.

> [!abstract] VALOR SUBNORMAL DE BINARY32
> 
> $$x = (-1)^s\, (F / 2^{23})\, 2^{-126}$$
> 
> No aparece el `1` implícito de los valores normales. El exponente efectivo es $-126$ (no $-127$).

Para `binary32`:

- Menor positivo normal: $2^{-126} \approx 1.1755 \times 10^{-38}$.
- Menor positivo subnormal: $2^{-149} \approx 1.4013 \times 10^{-45}$.
- Máximo finito positivo: $(2 - 2^{-23}) 2^{127} \approx 3.4028 \times 10^{38}$.

## PRECISIÓN Y REDONDEO

Los valores representables son finitos y su distancia aumenta conforme aumenta el exponente. `binary32` tiene **24 bits de precisión** en el significando (aproximadamente 7 cifras decimales significativas); `binary64`, **53 bits** (aproximadamente 15–17).

El redondeo predeterminado habitual es **al más cercano, resolviendo los empates hacia el significando par**. IEEE 754 también define otros modos, como hacia cero y hacia $+\infty$ o $-\infty$.

> [!example] EJEMPLO—POR QUÉ `0,1` NO ES EXACTO
> En binario, $0.1_{10} = 0.0001100110011 \ldots_2$ (*periódico*). `binary32` guarda el patrón `0x3DCCCCCD`, que representa aproximadamente $0.10000000149$.
> 
> Por eso las comparaciones de flotantes calculados suelen requerir una tolerancia adecuada al problema, en lugar de comparar siempre igualdad exacta.

## COMPROBAR LOS BITS CON PYTHON

```python
import struct

number = 13.25
bits = struct.unpack('>I', struct.pack('>f', number))[0]

print(f'{bits:032b}')
print(f'0x{bits:08X}')
# SALIDA:
# 01000001010101000000000000000000
# 0x41540000
```

- `>f` empaqueta el número como `binary32` en orden de bytes big-endian.
- `>I` interpreta esos mismos cuatro bytes como entero sin signo.
- Este código **inspecciona** los bits: no convierte numéricamente el `float` en un entero de ese valor.

> [!note] NOTA
> En sistemas habituales, `float` de C corresponde a `binary32` y `double` a `binary64`, pero conviene verificar las características de la implementación. En Python, `float` suele usar `binary64`; `struct` permite pedir expresamente `binary32`.

## ERRORES FRECUENTES

- Confundir **23 bits de fracción** con 23 bits de precisión total: en normalizados hay un bit implícito adicional.
- Interpretar el exponente almacenado como complemento a dos: es un **campo sesgado**.
- Suponer que `NaN == NaN`: es falso en las comparaciones ordinarias de IEEE 754.
- Suponer que `-0` y `+0` son el mismo **patrón de bits**: sus patrones son distintos, aunque suelen compararse iguales.
- Creer que las operaciones con flotantes se realizan exactamente sin redondeos intermedios.

## EJERCICIOS

1. Codifica $-6.5$ en `binary32` (escribe los tres campos).
2. Explica qué significa que $E = 0$ y $F \neq 0$.
3. ¿Por qué $0.5$ es exacto y $0.1$ no suele serlo?
