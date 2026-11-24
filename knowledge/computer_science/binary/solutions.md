---
aliases: [Soluciones de binario]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# SOLUCIONES RAZONADAS DE LOS EJERCICIOS

> [!seealso]- MIRA TAMBIÉN
> - [Ejercicios](exercises.md)
> - [Chuleta](binary_cheatsheet.md)

> [!important] CONCEPTOS IMPORTANTES
> - Se muestran resultados y procedimientos de los ejercicios de [práctica](exercises.md).
> - Comprueba las operaciones y presta atención al ancho y al signo.
## BLOQUE 1 — FUNDAMENTOS

**1.** `10110101₂` tiene activos los pesos $128+32+16+4+1=181$. En hexadecimal, agrupando `1011 0101`, es `0xB5`.

**2.** $93=64+16+8+4+1$, por tanto `01011101₂` (8 bits) y `0x5D`.

**3.** $10_{10}=1010_2$ y $0.625=1/2+1/8=0.101_2$. Resultado: `1010.101₂`.

**4.** $2^{10}=1024$ combinaciones. $3\ \mathrm{KiB}=3\cdot1024=3072$ bytes.

**5.**

```text
A      1010 1100
B      1100 1010
AND    1000 1000
OR     1110 1110
XOR    0110 0110
NOT A  0101 0011
```

## BLOQUE 2 — ENTEROS CON SIGNO

**6.** Sin signo: $[0,255]$. Con signo en complemento a dos: $[-128,127]$.

**7.** Sin signo: $246$. Con signo: $246-256=-10$.

**8.** $23=0001\ 0111$; invertir → `1110 1000`; sumar 1 → **`1110 1001`**, que representa -23.

**9.** Negar `0001 0101` (+21): `1110 1011` (-21). Negar `1111 1100` (-4): `0000 0100` (+4).

**10.** `1001 1010` tiene MSB=1; extensión de signo: **`1111 1111 1001 1010`**. Ambas representan -102.

**11.** `1000 0000` representa -128. Invertir → `0111 1111`; sumar 1 → `1000 0000`. El valor matemático +128 no cabe en 8 bits con signo: **desbordamiento**.

## BLOQUE 3 — COMA FIJA Y FLOTANTE

**12.** `1110 1000` es -24 como entero con signo; dividido por 16 da **-1,5**. Paso: $1/16=0.0625$.

**13.** $13.25=1.10101_2\times2^3$. Signo `0`; exponente $3+127=130=$ `10000010`; fracción `10101000000000000000000`. Patrón completo **`01000001010101000000000000000000`** (`0x41540000`).

**14.** `E=0,F=0`: cero con signo; `E=0,F≠0`: subnormal; `E=255,F=0`: infinito con signo; `E=255,F≠0`: NaN.

**15.** $0.1_{10}$ tiene una expansión binaria periódica infinita. Un significando finito solo puede guardar un número limitado de bits y debe redondear.

## BLOQUE 4 — LÓGICA Y COMPONENTES

**16.** Para A=1, B=0: AND=0; XOR=1; NAND=1; XNOR=0.

**17.** En NAND CMOS estática de dos entradas, **nMOS(A) y nMOS(B) en serie hacia GND**; **pMOS(A) y pMOS(B) en paralelo hacia VDD**. Y solo baja a 0 cuando A=B=1.

**18.** Si $N(A,B)=\overline{AB}$, NOT A = $N(A,A)$; AND = $N(N(A,B),N(A,B))$; OR = $N(N(A,A),N(B,B))$.

**19.** `10` selecciona **D2**. Hacen falta **tres MUX 2:1** en árbol (dos en el primer nivel y uno final).

**20.** Se activa **Y1**. Ecuación: $Y_1=\overline A\land B$.

## BLOQUE 5 — ARITMÉTICA

**21.** Medio sumador: $S=A\oplus B$ y $C=AB$. Filas `(A,B → S,C)`: `00→00`, `01→10`, `10→10`, `11→01`.

**22.** $1+1+1=3_{10}=11_2$. Por tanto `S=1` y `C_out=1`.

**23.** `A=0000 0101`, `B=0000 1001`; `NOT B=1111 0110`; `C_in=1`. Entonces $5+(\sim9)+1$ da **`1111 1100`**, que representa **-4** (sin acarreo exterior en la resta).

**24.** `0111` (+7) + `0011` (+3) → `1010`, que vale -6 en complemento a dos de 4 bits. Los dos operandos son positivos y el resultado codificado es negativo: **V=1**.

**25.** $13\cdot11=143$. Productos parciales: 13, 26, 0, 104. Suma: $143=10001111_2$ (8 bits).

**26.** $23\div3=7$ y resto 2. En binario: **Q=`00111`** y **R=`00010`**. Comprobación: $23=3\cdot7+2$.

**27.** $-13/3$ truncado hacia cero: **Q=-4, R=-1**. Identidad: $3(-4)+(-1)=-13$.

**28.** Si la resta con signo **desborda**, el MSB del resultado puede no representar correctamente el signo de la diferencia matemática. Por ejemplo, en 8 bits $127-(-1)=128$ da patrón `1000 0000` (N=1), pero $127$ **no** es menor que $-1$. Hay que corregir con **`N XOR V`**: en este caso V=1 y `N XOR V=0`.

## BLOQUE 6 — DISEÑO DE UNA ALU

**29.** Cuatro operaciones necesitan **2 bits de selección**. Un bloque lógico produce AND y XOR; un **único sumador/restador** calcula tanto suma como resta con XOR sobre B y acarreo inicial controlado. Un **MUX 4:1 por bit** elige qué resultado se entrega.

**30.** El sumador combinacional solo calcula una salida correspondiente a las entradas actuales; **no almacena estado**. Un registro hecho con flip-flops puede capturar y conservar el resultado entre flancos de reloj.

## REVISIÓN

Si aparece una respuesta diferente, revisa antes de nada:

- Si el número se interpreta **con o sin signo**.
- Si se han conservado o descartado los **acarreos externos**.
- Si la operación se realizó con el **ancho correcto**.
- Si una división con signo usa **truncamiento hacia cero** o división hacia $-\infty$.
