---
aliases: [Comparador digital]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# COMPARADORES BINARIOS

> [!seealso]- MIRA TAMBIÉN
> - [Puertas lógicas](../logic/logic_gates.md)
> - [Sumador/restador](../arithmetic/adder_subtractor.md)
> - [ALU](../arithmetic/alu.md)

> [!important] CONCEPTOS IMPORTANTES
> - Un comparador indica si dos números son iguales, menores o mayores.
> - La comparación de igualdad se construye con XOR/XNOR y una reducción lógica.
> - Para comparar números **con signo**, hay que interpretar el bit de signo y el posible desbordamiento.
## DEFINICIÓN

Un **comparador** es un circuito combinacional que recibe dos operandos de $n$ bits y produce señales como `EQ` ($A=B$), `LT` ($A<B$) y `GT` ($A>B$).

## COMPROBAR IGUALDAD

Dos palabras son iguales si **cada pareja de bits coincide**. Podemos usar una XNOR por posición y después combinar con AND:

> [!abstract] FÓRMULA
> $$EQ=\bigwedge_{i=0}^{n-1}\overline{A_i\oplus B_i}$$

Una forma equivalente es combinar los XOR con OR y luego negar:

$$EQ=\overline{\bigvee_{i=0}^{n-1}(A_i\oplus B_i)}$$

> [!example] EJEMPLO
> ```text
> A = 1011
> B = 1010
> XOR = 0001
> ```
>
> Como el XOR no es todo cero, `EQ=0`.

## ORDEN EN ENTEROS SIN SIGNO

Se comparan desde el bit más significativo hacia el menos significativo. **El primer bit diferente** determina qué número es mayor:

```text
A = 1001 (9)
B = 0111 (7)
    ↑
Primer bit: 1 > 0, luego A > B
```

Un circuito también puede deducir $A<B$ mediante la [resta](../arithmetic/adder_subtractor.md). En una resta sin signo $A-B$ implementada con $A+\overline B+1$, `C_out=0` significa que hubo préstamo y por tanto $A<B$.

## ORDEN EN ENTEROS CON SIGNO

En complemento a dos no basta con comparar los patrones como si fueran sin signo. Por ejemplo:

```text
A = 1111 1111 = -1 (con signo)
B = 0000 0001 = +1 (con signo)
```

Como enteros **con signo**, $A<B$, pero como **sin signo** 255 es mayor que 1.

Si la comparación se obtiene mediante un restador de $n$ bits, se pueden usar las banderas habituales:

> [!abstract] COMPARACIÓN CON SIGNO A PARTIR DE A-B
> $$LT=N\oplus V$$
>
> - $N$: bit de signo del resultado almacenado de $A-B$.
> - $V$: bandera de desbordamiento con signo.
>
> Además, $EQ=Z$ y $GT=\overline{LT}\land\overline Z$.

Si los signos de entrada son distintos, el negativo siempre es menor; si coinciden, puede compararse su magnitud binaria como sin signo.

## APLICACIONES

- Condiciones de salto en procesadores.
- Comparación de contadores o direcciones.
- Operaciones mínimo/máximo y clasificación.
