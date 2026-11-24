---
aliases: [Binary, Sistemas digitales]
author: Mindusting
corrected: false
creationDate: 2026-11-23 02:34:25
headerFile: true
modificationDate: 2026-11-23 02:34:25
rating: 
tags: [Binary]
---

# BINARIO Y SISTEMAS DIGITALES

> [!external-link]- REFERENCIAS WEB
> - [IEEE 754: conceptos y formatos (University of Maryland)](https://www.math.umd.edu/~petersd/466/ieee754h.html)
> - [Circuitos combinacionales, sumadores y restadores (Sonoma State University)](https://bob.cs.sonoma.edu/IntroCompOrg-x64/bookch5.html)
> - [Fundamentos de puertas CMOS (UCLA Tapeout Club)](https://ucla-tapeout-club.github.io/pd-wiki/docs/fundamentals/mosfets-and-cmos.html)

> [!important] CONCEPTOS IMPORTANTES
> - Un **bit** representa uno de dos estados; su significado depende de cómo se interprete.
> - El complemento a dos permite trabajar con enteros negativos usando el mismo sumador.
> - Las **puertas lógicas** construyen circuitos combinacionales y secuenciales.
> - La coma flotante IEEE 754 tiene precisión finita y requiere reglas de redondeo.

## DEFINICIÓN

En informática, **binario** suele referirse tanto al sistema de numeración de base 2 como a la representación y procesamiento de información mediante dos estados lógicos (`0` y `1`). Son ideas relacionadas, pero no idénticas: los mismos ocho bits pueden representar un número entero, parte de un `float`, una máscara de permisos o cualquier otro dato.

Esta sección estudia **cómo se representa la información** y **cómo se construyen circuitos capaces de operar con ella**, desde puertas lógicas hasta una unidad aritmético-lógica (ALU). El objetivo no es memorizar circuitos aislados, sino entender cómo se componen.

## RUTA DE APRENDIZAJE

### FUNDAMENTOS

- [Bits, bytes y unidades](fundamentals/bits_and_bytes.md): estados, tamaño, orden y unidades de almacenamiento.
- [Sistema de numeración posicional](fundamentals/positional_systems.md): base 2, potencias de 2 y notación hexadecimal.
- [Conversión entre bases](fundamentals/conversions.md): enteros y fracciones de decimal a binario y viceversa.
- [Operaciones bit a bit](fundamentals/bitwise_operations.md): máscaras, desplazamientos y XOR.

### REPRESENTACIÓN DE NÚMEROS

- [Enteros sin signo](representation/unsigned_integers.md).
- [Enteros con signo: complemento a dos](representation/twos_complement.md).
- [Cambio de signo en complemento a dos](representation/twos_complement_negation.md).
- [Coma fija](representation/fixed_point.md).
- [Coma flotante IEEE 754](representation/ieee754.md).

### LÓGICA DIGITAL

- [Álgebra de Boole](logic/boolean_algebra.md).
- [Puertas lógicas y tablas de verdad](logic/logic_gates.md).
- [Transistores, CMOS y construcción de NAND](logic/cmos_nand.md).
- [Construir otras puertas utilizando NAND](logic/nand_composition.md).

### COMPONENTES COMBINACIONALES

- [Multiplexadores y demultiplexadores](components/multiplexers_demultiplexers.md).
- [Codificadores y decodificadores](components/encoders_decoders.md).
- [Comparadores](components/comparators.md).
- [Desplazadores y rotadores](components/shifters.md).

### CIRCUITOS ARITMÉTICOS

- [Medio sumador](arithmetic/half_adder.md).
- [Sumador completo](arithmetic/full_adder.md).
- [Sumador/restador reutilizando el mismo circuito](arithmetic/adder_subtractor.md).
- [Multiplicación binaria](arithmetic/multiplier.md).
- [División binaria](arithmetic/divider.md).
- [Unidad aritmético-lógica (ALU)](arithmetic/alu.md).

### MEMORIA Y REPASO

- [Circuitos secuenciales y registros](components/sequential_logic.md): cuando la salida depende también del estado anterior.
- [Chuleta de binario y circuitos](binary_cheatsheet.md): fórmulas, reglas y tablas concentradas.
- [Ejercicios](exercises.md) y [soluciones razonadas](solutions.md).

## CONVENCIONES UTILIZADAS

- El bit menos significativo (**LSB**, índice `0`) aparece a la **derecha**; el más significativo (**MSB**) a la **izquierda**.
- Cuando hay riesgo de ambigüedad, indicamos el **ancho de palabra**: `1111 1011` (8 bits).
- `0b1010` indica binario, `0x0A` hexadecimal y `10` decimal, si no se especifica otra base.
- La notación $A_i$ representa el bit de posición $i$ de un operando $A$.
- El símbolo $\overline{A}$ representa NOT; $A \land B$ es AND; $A \lor B$ es OR; $A \oplus B$ es XOR.
