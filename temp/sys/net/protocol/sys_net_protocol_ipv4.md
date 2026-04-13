---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Computing
  - Systems
  - Network
title: IPv4 en Redes
rating: 0.5
---

# IPV4 EN REDES

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar como calcular las subredes.
> > - [ ] Poner un ejemplo complejo de cálculo (*usando una máscara que no sea múltiplo de 8*).
> > - [ ] Añadir un código en bien en C o en Python para mostrar como se calculan las redes.

El formato de **IPv4** se compone por una **dirección IP** (*IP address*) y una **máscara** (*mask*); representado la **IP** con cuatro bytes en [decimal](../../../../knoledge/mathematic/number_system/math_ns_dec.md) separados con un punto (`.`); y la **máscara** se sitúa al final separada por una barra (`/`); quedando algo con el siguiente aspecto: `192.168.0.1/24`.

## DIVISIÓN DE LA DIRECCIÓN IP Y LA MÁSCARA

Una dirección **IPv4** de primeras se divide por la **barra** (`/`) quedándonos con la **dirección IP** a la izquierda y la **máscara** a la derecha.

Una **dirección IP** (*IP address*) son simplemente los cuatro bytes separados por punto; a continuación podemos ver la el ejemplo de antes tanto en [decimal](../../../../knoledge/mathematic/number_system/math_ns_dec.md) como en [binario](../../../../knoledge/mathematic/number_system/math_ns_bin.md):

```txt
Decimal:
192.168.0.1

Binario:
11000000.10101000.00000000.00000001
```

> [!important] IMPORTANTE
> Es importante saber que estos número son internamente en [binario](../../../../knoledge/mathematic/number_system/math_ns_bin.md) ya que se van a hacer [operaciones binarias](../../../bin/bin.md) con estos para calcular ciertas cosas.

La **máscara** (*mask*) consiste en tener tantos unos a la izquierda de un número entero de 32 bits como indique la máscara; esto se ve mejor con unos ejemplos:

> [!example] Ejemplo máscara (24):
> Una máscara de 24 bints es fácil de calcular ya que es múltiplo de 8, por tanto los tres primeros bytes serán todo unos y el último todo ceros.
> ```txt
> 11111111.11111111.11111111.00000000
> ```

> [!example] Ejemplo máscara (12):
> Una máscara de 12 bites no es tan fácil de sacar ya que no es múltiplo de 8 pero podemos hacerlo en dos pasos, ya que el 12 se puede dividir en dos grupo, uno de 8 bits y otro de 4 (*dando como total 12*), teniendo esto en cuenta, la máscara tendría el siguiente aspecto.
> ```txt
> 11111111.11110000.00000000.00000000
> ```

Note sé que para calcular el número de bytes llenos de unos es tan fácil como dividir la máscara entre ocho y obtener el valor de suelo `numBytes = floor(mask / 8)`; mientras que para calcular el número de bits restantes se puede hacer con el operador módulo `numBits = mask % 8`.

## DIVISIÓN DE LA RED Y EL ANFITRIÓN

La **dirección IP** (*IP address*) se divide a su vez en dos partes: la **red** (*net*) y **anfitrión** (*host*); para obtener estos dos elementos de la **dirección IP** se usa la **máscara** (*mask*); para obtener la **red** (*net*) se aplica el [operador binario **AND**](../../../bin/bin.md#AND) sobre la **dirección IP**; mientras que el **anfitrión** (*host*) se hace de la misma forma solo que invirtiendo la **máscara** (*mask*) mediante el [operador binario **NOT**](../../../bin/bin.md#NOT):

```txt
Dirección IP:
11000000.10101000.00000000.00000001

Máscara
11111111.11111111.11111111.00000000

Máscara invertida:
00000000.00000000.00000000.11111111

Cálculo de red:
  11000000.10101000.00000000.00000001
& 11111111.11111111.11111111.00000000
-------------------------------------
  11000000.10101000.00000000.00000000

Cálculo de anfitrión:
  11000000.10101000.00000000.00000001
& 00000000.00000000.00000000.11111111
-------------------------------------
  00000000.00000000.00000000.00000001
```

Si cogemos los valores del ejemplo y los pasamos al decimal obtendremos que la **red** (*net*) es `192.168.0.0` y el **anfitrión** (*host*) es `0.0.0.1`.

## DIRECCIONES DISPONIBLES

El número de **direcciones disponibles** de una **red** (*net*) indica hasta cuantas combinaciones de bits puedes hacer con la porción de bits del **anfitrión** (*host*); es decir si tenemos una máscara de 24 y tenemos en cuenta que el máximo de bits son 32, le restamos a 32 los 24 y nos quedan 8, luego elevamos 2 a en este caso 8 y obtendremos el número de direcciones (*en este caso 256*).

$$
2^{(32-mask)}=validIps
$$

En caso de estar programandolo, es tan simple como invertir la máscara con el [operador binario **not**](../../../bin/bin.md#NOT) como un único número entero de cuatro bytes e interpretarlo en [decimal](../../../../knoledge/mathematic/number_system/math_ns_dec.md).

---

Quedando así (*siguiendo con el ejemplo*) la primera y última dirección:

```txt
Primera en binario:
11000000.10101000.00000000.00000000

Última en binario:
11000000.10101000.00000000.11111111

Primera en decimal:
192.168.0.0

Última en decimal:
192.168.0.255
```

## RANGO VÁLIDO

Dentro de las [**direcciones disponibles**](#DIRECCIONES%20DISPONIBLES) existe lo que se llama el **rango válido** este indica las direcciones que se pueden usar para identificar a un equipo en concreto, esto es devido a que se reservan dos para un propósito especial, siendo la dirección 0 para identificar la **red** (*net*) y la última disponible para los mensages de **broadcast** (*este último sirve para enviar inforació a todos los equipos de la red*); por lo que el rángo válido se define desde la segunda dirección disponible hasta la anteúltima; siguiendo con el ejemplo de antes: la dirección de **red** (*net*) sería `192.168.0.0`, la primera IP sería `192.168.0.1`, la última IP sería `192.168.0.254`, el **broadcast** sería `192.168.0.255` y por último el número de direcciones válidas sería `253` siguiendo la siguiente fórmula:

$$
validIps-2=validRange
$$

## REGEX PARA IPV4

Sin máscara: `[1-2]?\d{1,2}(?:\.[1-2]?\d{1,2}){3}`
Com máscara: `[1-2]?\d{1,2}(?:\.[1-2]?\d{1,2}){3}\/[1-3]?\d`
Com posíble máscara: `[1-2]?\d{1,2}(?:\.[1-2]?\d{1,2}){3}(?:\/[1-3]?\d)?`
