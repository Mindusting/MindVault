---
aliases: []
author: Mindusting
corrected: false
creationDate: 2026-11-24 04:29:24
headerFile: false
modificationDate: 2026-11-24 06:15:25
rating: 
tags: [Binary, DigitalLogic]
---

# CONVERSIÓN ENTRE BASES

> [!seealso]- MIRA TAMBIÉN
> - [Sistema de numeración posicional](positional_systems.md)
> - [Coma flotante IEEE 754](../representation/ieee754.md)

> [!important] CONCEPTOS IMPORTANTES
> - Para pasar de binario a decimal, se suman los pesos de las posiciones con valor `1`.
> - Para convertir un entero decimal positivo a binario, se divide sucesivamente entre 2.
> - Para convertir una fracción decimal a binario, se multiplica sucesivamente por 2; puede no terminar.

## BINARIO A DECIMAL

Descomponemos el número en potencias de 2:

> [!example] EJEMPLO—`11010` A DECIMAL
> 
> $$11010_2 = 1\cdot16+1\cdot8+0\cdot4+1\cdot2+0\cdot1=26_{10}$$

## DECIMAL ENTERO A BINARIO

Dividimos entre 2 y anotamos el resto en cada paso. Los restos se leen **de abajo arriba**.

> [!example] EJEMPLO—26 A BINARIO
> 
> |  División   | Cociente | Resto |
> |:-----------:| --------:| -----:|
> | $26 \div 2$ |     $13$ |   $0$ |
> | $13 \div 2$ |      $6$ |   $1$ |
> | $6 \div 2$  |      $3$ |   $0$ |
> | $3 \div 2$  |      $1$ |   $1$ |
> | $1 \div 2$  |      $0$ |   $1$ |
> 
> Resultado: $26_{10} = 11010_2$.

## DECIMAL FRACCIONARIO A BINARIO

Multiplicamos la parte fraccionaria por 2. La parte entera obtenida en cada paso es el siguiente bit tras la coma; repetimos con la nueva fracción.

> [!example] EJEMPLO—`0,625` A BINARIO
> 
> |        Operación        | Bit obtenido | Fracción siguiente |
> |:-----------------------:| ------------:| ------------------:|
> | $0.625 \times 2 = 1.25$ |          $1$ |             $0.25$ |
> |  $0.25 \times 2 = 0.5$  |          $0$ |              $0.5$ |
> |  $0.5 \times 2 = 1.0$   |          $1$ |                $0$ |
> 
> Resultado: $0.625_{10} = 0.101_2$.

Algunas fracciones finitas en decimal, como `0,1`, tienen **expansión binaria infinita y periódica**. Para almacenarlas con un número finito de bits habrá que redondear.

## CONVERSIÓN BINARIO–HEXADECIMAL

Agrupamos los bits de cuatro en cuatro empezando por la derecha (y, si hay coma, hacia ambos lados desde ella):

```text
    111 1010 0011
=>  0111 1010 0011
=>     7    A    3
=>  0x7A3
```

## NÚMEROS NEGATIVOS

El signo matemático `-` escrito delante de una cifra **no es una codificación binaria**. Para almacenar un entero negativo con un número fijo de bits se utiliza normalmente [complemento a dos](../representation/twos_complement.md).

## EJERCICIOS

1. Convierte $101011_2$ a decimal.
2. Convierte $57_{10}$ a binario y hexadecimal.
3. Convierte $0.375_{10}$ a binario.
