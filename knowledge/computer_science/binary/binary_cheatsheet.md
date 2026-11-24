---
aliases: [Chuleta binaria, Binary cheatsheet]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# CHULETA DE BINARIO Y CIRCUITOS

> [!seealso]- MIRA TAMBIÉN
> - [Índice](binary.md)
> - [Ejercicios](exercises.md)

> [!important] CONCEPTOS IMPORTANTES
> - Resumen para consultar rápidamente; las demostraciones y explicaciones están en los documentos principales.
## BASES Y TAMAÑOS

- Un grupo de $n$ bits tiene $2^n$ patrones.
- Los pesos del entero binario son $\ldots,16,8,4,2,1$.
- Los pesos de la parte fraccionaria son $1/2,1/4,1/8,\ldots$.
- Cuatro bits equivalen a una cifra hexadecimal.
- `1 byte = 8 bits` en sistemas modernos.
- `1 kB = 1000 B`; `1 KiB = 1024 B`.

## ENTEROS

| Representación | Mínimo | Máximo |
| --- | ---: | ---: |
| Sin signo de $n$ bits | $0$ | $2^n-1$ |
| Con signo en complemento a dos de $n$ bits | $-2^{n-1}$ | $2^{n-1}-1$ |

- Negar: $-x=(\overline x+1)\bmod2^n$.
- Extender sin signo: añadir **ceros** a la izquierda.
- Extender con signo: repetir el **MSB**.
- El mínimo negativo no tiene opuesto representable con el mismo ancho.

## COMA FIJA Y FLOTANTE

- Coma fija: $x=I/2^f$.
- IEEE 754 `binary32`: `1` signo + `8` exponente + `23` fracción; sesgo `127`.
- IEEE 754 `binary64`: `1` signo + `11` exponente + `52` fracción; sesgo `1023`.
- Número normal: $(-1)^s(1+F/2^f)2^{E-bias}$.
- Exponente todo cero: cero o subnormal.
- Exponente todo unos: infinito o NaN.
- `0,1` no puede representarse exactamente en formatos binarios de precisión finita.

## PUERTAS LÓGICAS

| Puerta | Función | Salida 1 cuando... |
| --- | --- | --- |
| NOT | $\overline A$ | A=0 |
| AND | $AB$ | A=B=1 |
| OR | $A\lor B$ | Al menos una entrada es 1 |
| XOR | $A\oplus B$ | Entradas diferentes |
| NAND | $\overline{AB}$ | No son ambas 1 |
| NOR | $\overline{A\lor B}$ | Ambas son 0 |
| XNOR | $\overline{A\oplus B}$ | Entradas iguales |

- NAND CMOS: **nMOS en serie**, **pMOS en paralelo**.
- NOT con NAND: $N(A,A)$.
- AND con NAND: $N(N(A,B),N(A,B))$.
- OR con NAND: $N(N(A,A),N(B,B))$.

## COMPONENTES

- MUX 2:1: $Y=(\overline S\land A)\lor(S\land B)$.
- DEMUX 1:2: $Y_0=D\overline S$; $Y_1=DS$.
- Decodificador $n:2^n$: activa la salida asociada al código.
- Codificador $2^n:n$: codifica una entrada activa (o aplica prioridad).
- Registro: $n$ flip-flops pueden guardar una palabra de $n$ bits.

## ARITMÉTICA

> [!abstract] SUMADORES
> **Medio sumador:**
> $$S=A\oplus B,\qquad C_{out}=AB$$
>
> **Sumador completo:**
> $$S=A\oplus B\oplus C_{in}$$
> $$C_{out}=AB+C_{in}(A\oplus B)$$

> [!abstract] SUMADOR/RESTADOR
> $$B'_i=B_i\oplus M,\qquad C_0=M$$
>
> - $M=0$: suma.
> - $M=1$: resta, invirtiendo B y sumando 1.
> - Desbordamiento con signo: $V=C_{n-1}\oplus C_n$.

> [!abstract] MULTIPLICACIÓN Y DIVISIÓN
> Multiplicación: $A\cdot B=\sum b_i(A\ll i)$.
>
> División entera sin signo: $A=BQ+R$, donde $0\le R<B$.

## BANDERAS

- `Z`: resultado igual a cero.
- `N`: bit más significativo del resultado.
- `C`: acarreo de salida; en resta sin signo $C=1$ indica ausencia de préstamo.
- `V`: desbordamiento con signo.
- Comparación con signo mediante A-B: $A<B$ si `N XOR V` vale 1.

## ENLACES

- [Índice general](binary.md)
- [Representación de enteros](representation/twos_complement.md)
- [IEEE 754](representation/ieee754.md)
- [Puertas lógicas](logic/logic_gates.md)
- [Sumador/restador](arithmetic/adder_subtractor.md)
- [Multiplicador](arithmetic/multiplier.md)
- [Divisor](arithmetic/divider.md)
