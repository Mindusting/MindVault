---
aliases: [Fixed-point, Q format]
author: Mindusting
corrected: false
headerFile: false
tags: [Binary, DigitalLogic]
---

# NÚMEROS DE COMA FIJA

> [!seealso]- MIRA TAMBIÉN
> - [Enteros con signo](twos_complement.md)
> - [Coma flotante IEEE 754](ieee754.md)

> [!important] CONCEPTOS IMPORTANTES
> - La coma fija almacena un entero y aplica un **factor de escala** predeterminado.
> - Si hay $f$ bits fraccionarios, el valor es el entero almacenado dividido por $2^f$.
> - Es sencilla y predecible, pero su rango y precisión son constantes.
## DEFINICIÓN

En una representación de **coma fija** (*fixed-point*), la posición de la coma binaria se decide de antemano y es idéntica para todos los números de ese formato. Los bits almacenados son los de un **entero** (con o sin signo), cuya interpretación incluye un factor de escala.

> [!abstract] FÓRMULA
> $$x=\frac{I}{2^f}$$
>
> - $I$: entero almacenado.
> - $f$: número de bits fraccionarios.

## EJEMPLO CON 8 BITS

Usaremos el nombre **Q4.4** en este documento para indicar expresamente **8 bits en total, incluidos el signo si existe, y 4 bits fraccionarios**. Algunas fuentes usan otras convenciones de nomenclatura Q: comprueba siempre qué cuenta cada cifra.

```text
Representación:  0011 1000
Separación:      0011.1000
Valor:           3 + 1/2 = 3,5
```

Con signo en complemento a dos de 8 bits:

```text
+1,5 => 0001 1000 => I =  24 => 24/16 =  1,5
-1,5 => 1110 1000 => I = -24 => -24/16 = -1,5
```

## RANGO Y RESOLUCIÓN

Para **Q4.4 con signo** y 8 bits:

- Paso mínimo entre representables: $2^{-4}=0.0625$.
- Mínimo: $-128/16=-8$.
- Máximo: $127/16=7.9375$.

> [!abstract] CODIFICACIÓN
> $$I\approx\operatorname{redondear}(x\cdot2^f)$$
>
> Después se comprueba que $I$ cabe en el entero de $n$ bits, y se aplica la regla de redondeo elegida. No existe una sola regla universal para todas las implementaciones de coma fija.

## OPERACIONES

- **Suma y resta:** si ambos operandos tienen la misma escala, se suman o restan los enteros almacenados.
- **Multiplicación:** el producto de dos enteros con $f$ bits fraccionarios tiene **$2f$ bits fraccionarios**. Hay que volver a escalar (normalmente, desplazar $f$ bits) y gestionar redondeo y desbordamiento.
- **División:** se suele ampliar el numerador, desplazándolo $f$ bits a la izquierda antes de dividir, con capacidad suficiente para no perder información.

## COMA FIJA FRENTE A COMA FLOTANTE

La coma fija ofrece una separación constante entre números representables y facilita ciertos circuitos embebidos y de procesamiento de señales. La coma flotante representa un rango dinámico mucho mayor, pero con separación variable y reglas propias de aproximación.
