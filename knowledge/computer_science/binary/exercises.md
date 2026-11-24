---
aliases: [Ejercicios de binario]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# EJERCICIOS DE BINARIO Y SISTEMAS DIGITALES

> [!seealso]- MIRA TAMBIÉN
> - [Índice general](binary.md)
> - [Soluciones](solutions.md)

> [!important] CONCEPTOS IMPORTANTES
> - Los ejercicios están ordenados desde la representación de números hasta los circuitos.
> - Resuelve cada apartado antes de consultar las [soluciones](solutions.md).
> - Indica siempre el **número de bits** y si un entero es con o sin signo.
## BLOQUE 1 — FUNDAMENTOS

**1.** Convierte `10110101₂` a decimal y a hexadecimal. Indica el peso de cada bit activo.

**2.** Convierte `93₁₀` a binario con 8 bits y a hexadecimal.

**3.** Convierte `10,625₁₀` a binario, separando parte entera y parte fraccionaria.

**4.** ¿Cuántos patrones hay con 10 bits? ¿Cuántos bytes hay en 3 KiB?

**5.** Para A=`10101100` y B=`11001010` (ambos 8 bits), calcula AND, OR, XOR y NOT A.

## BLOQUE 2 — ENTEROS CON SIGNO

**6.** Indica los rangos de 8 bits sin signo y en complemento a dos.

**7.** Interpreta `11110110` como entero sin signo y como entero con signo en complemento a dos de 8 bits.

**8.** Representa `-23` en complemento a dos de 8 bits, mostrando el procedimiento.

**9.** Niega `00010101` y `11111100` dentro de 8 bits. ¿Qué valores decimales representan los resultados?

**10.** Realiza la extensión de signo de `10011010` desde 8 a 16 bits.

**11.** ¿Qué sucede al negar `10000000` en complemento a dos de 8 bits? ¿Por qué?

## BLOQUE 3 — COMA FIJA Y FLOTANTE

**12.** Con una representación con signo de 8 bits y 4 bits fraccionarios, interpreta `1110 1000` y calcula el paso mínimo.

**13.** Codifica `13,25` en `binary32` e indica signo, exponente almacenado y fracción.

**14.** Describe qué significan las combinaciones `E=0,F=0`, `E=0,F≠0`, `E=255,F=0` y `E=255,F≠0` en `binary32`.

**15.** Explica por qué `0,1` puede sufrir redondeo incluso cuando su representación decimal es corta.

## BLOQUE 4 — LÓGICA Y COMPONENTES

**16.** Completa los valores AND, XOR, NAND y XNOR para A=1 y B=0.

**17.** Dibuja conceptualmente los caminos de una NAND CMOS: ¿qué transistores deben ir en serie y cuáles en paralelo?

**18.** Expresa NOT, AND y OR utilizando solo puertas NAND.

**19.** En un MUX 4:1, ¿qué entrada se selecciona con `S1S0=10`? ¿Cuántos MUX 2:1 hacen falta para construirlo en árbol?

**20.** En un decodificador 2:4 activo en alto, ¿qué salida se activa para `A=0,B=1`? Escribe la expresión de esa salida.

## BLOQUE 5 — ARITMÉTICA

**21.** Diseña un medio sumador: da ecuaciones y tabla de verdad.

**22.** Para un sumador completo, calcula suma y acarreo si `A=1, B=1, C_in=1`. Explica la operación decimal equivalente.

**23.** Con un sumador/restador de 8 bits, realiza `5-9`. Muestra `NOT B`, la entrada de acarreo y el resultado.

**24.** Suma con 4 bits con signo `0111 + 0011`. Explica si hay desbordamiento y por qué.

**25.** Multiplica `1101₂ × 1011₂` mediante productos parciales, conservando el resultado completo.

**26.** Divide `10111₂` entre `11₂` por el método de desplazamiento y resta; indica cociente y resto.

**27.** Calcula cociente y resto de `-13 ÷ 3` con truncamiento hacia cero. Comprueba la identidad $A=BQ+R$.

**28.** ¿En qué situación la resta $A-B$ puede usar el bit de signo de su resultado para decidir `A<B` de forma incorrecta si no se tiene en cuenta el desbordamiento?

## BLOQUE 6 — DISEÑO DE UNA ALU

**29.** Propón una ALU que haga AND, XOR, suma y resta. Indica las líneas de selección necesarias y qué bloques se reutilizan.

**30.** Describe la diferencia entre un sumador combinacional y un registro de salida: ¿cuál de los dos conserva información entre ciclos de reloj?

> [!seealso]- MIRA TAMBIÉN
> - [Soluciones razonadas](solutions.md)
> - [Chuleta de fórmulas](binary_cheatsheet.md)
