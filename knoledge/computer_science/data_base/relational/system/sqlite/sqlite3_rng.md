---
aliases: [Números decimales aleatorios en SQLite3]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [SQLite3, DataBase, SQL]
---

# NÚMEROS DECIMALES ALEATORIOS EN SQLITE3

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [x] Explicar como generar el rango exclusivo.
> > - [x] Explicar como generar el rango inclusivo.
> > - [ ] Explicar como como funciona la generación del rango.

Para generar número aleatorios decimales en **SQLite3** no hay una función concreata (*por lo menos en el momento en el que estoy escribiendo esto*), solo tenemos una para generar números enteros (*`RANDOM`, la cual genera un número entero con signo de 64 bits*), por lo que si queremos un número decimal, tenemos que buscarnos la vida.

## RANGO EXCLUSIVO

Un número decimal en el rango [**\[0.0, 1.0)**](../../../../../mathematic/temp/math_range_notation.md) (*es decir, que esté entre 0 y 1, excluyendo el 1*) nos permite acceder a prácticamente cualquier rango de números si sabemos como hacerlo, ya que con multiplicaciones y sumas, podremos aumentar y desplazar el rango de número que podemos obtener.

> [!seealso] Ver también
> - [Número aleatorios en informática.](../../../../programming/fundamentals/theory/rng.md)

---

Primero me gustaría explicar lo que **NO** devemos hacer y es lo que suelen sugerir las IAs (*por lo menos, a día de hoy cuando estoy escribiendo esto*):

> [!bug] Este método es inseguro
> ```sql
> --                            (2 ^ 63) - 1
> SELECT ABS(RANDOM()) / 9223372036854775807.0 AS RNG
> ```
> 
> Esta forma de generar número aleatorios no es fiable:
> 
> 1. **El número 0:**
>     Tiene la mitad de provavilidades de salir que el resto, por tanto la proporción de resultados no es correcta; esto ocurre por la función `ABS` que "*pliega*" el rango de número posibles por la mitad, y como el 0 no tiene una versión negativa este es el único número (*excepto por una excepción*) que no tiene una "*pareja*", de ahí que este tenga menos provavilidades de que salga.
> 2. **La excepción:**
>     Existe la pequeña posivilidada de que el número que salga sea `-9223372036854775808` ($-2^{63}$), este no tiene una versión positiva en un número con signo de 64 bits, por lo que nos dará un error de "*overflow*" (*o ignorará la query dependiendo del interpete desde donde la estemos ejecutando*); lo dicho, esta posibilidad es microscópicamente probable, tendría que coincidir en binario un 1 seguido de 63 ceros; pero por muy improbable que sea, podría ser el causante de algún problema real en el caso de que nuestro programa no esté preparado para esa casuistica.

Ahora vemos como sí se tiene que hacer:

> [!success] Este método es seguro
> ```sql
> --                                               2 ^ 53
> SELECT (RANDOM() & 9007199254740991) / 9007199254740992.0 AS RNG
> ```
> 
> Se limita el número de bits a un rango relevante (*53 bits, ya que el estandar [IEEE 754](https://es.wikipedia.or/wiki/IEEE_754) determina que la mantisa tiene un tamaño de 53 bits*), esto además excluye la parte negativa que nos pueda dar problemas con el número $-2^{63}$, además de no duplicar las posibilidades de los número positivos excluyendo al 0.

^exclusive-example

---

Si pones este método a prueba puede ser que pienses que pienses que no es exclusivo ya que si sustituimos la función `RANDOM` y la **máscara**, por el número más grande que nos puede salir (*siendo este el mismo número que la máscara*):

```SQL
--         valor máximo             2 ^ 53
SELECT 9007199254740991 / 9007199254740992.0 AS RNG
-- SALIDA:
-- 1.0
```

Obtendremos el número $1.0$, por tanto es inclusivo, no exclusivo; esto por raro que suene, no es así, en realidad lo que está pasando es que se está redondeando el valor a la hora de mostrarlo por pantalla, eso es por que el resultado que nos da realmente es **cero coma nueve periódico** ($0.\overline{9}$), que al ser redondeado da como resultado $1.0$; si no me crees, puedes probarlo tú mismo usando la función `FLOOR`, para descartar la parte decimal; si realmente es un $1.0$ el resultado no cambiaría, sin embargo al usar esta función obtenemos $0.0$, demostrando así que el valor real que obtuvimos es menor a $1.0$:

```SQL
--               valor máximo             2 ^ 53
SELECT FLOOR(9007199254740991 / 9007199254740992.0) AS RNG
-- SALIDA:
-- 0.0
```
^exclusive-proof

## RANGO INCLUSIVO

Hay a veces que lo que necesitamos no es un [número decimal exclusivo](#RANGO%20EXCLUSIVO), si no que hay a veces que necesitamos que sea inclusivo, es decir, que se encuentre en el rango [**\[0.0, 1.0\]**](../../../../../mathematic/temp/math_range_notation.md); para esa clase de casos podremos usar el siguiente método:

```sql
--                                         (2 ^ 53) - 1
SELECT (RANDOM() & 9007199254740991) / 9007199254740991.0 AS RNG
```

Podrías pensar que es idéntico al método para consegir un [número decimal exclusivo](#RANGO%20EXCLUSIVO), pero no, fíjate bien; el divisor en este caso es una unidad menor, permitiendo así que el número aleatorio más alto que se puede calcular sea $1.0$.

Para ponerlo a prueba y comprobar así que en este caso sí que es inclusivo, podemos usar el [mísmo método que aplicamos sobre el método exclusivo](#^exclusive-proof):

```SQL
--         valor máximo       (2 ^ 53) - 1
SELECT 9007199254740991 / 9007199254740991.0 AS RNG
-- SALIDA:
-- 1.0
```

Aplicamos la función `FLOOT`:

```SQL
--               valor máximo       (2 ^ 53) - 1
SELECT FLOOR(9007199254740991 / 9007199254740991.0) AS RNG
-- SALIDA:
-- 1.0
```

Y el resultado como se puede ver es el mismo ($1.0$), demostrando así que en este caso ese $1.0$ no es fruto de un redondeo a la hora de mostrar el valor, sino que realmente es el valor que hemos obtenido como resultado.

## EXPLICACIÓN DE LA GENERACIÓN DE RANGO

```python
def randIntToFloat(
        number: int,
        precission: int = 53,
        inclusive: bool = False
    ) -> float:
    divisor: int = 2 ** precission
    mask:    int = divisor - 1
    if inclusive:
        divisor = mask
    return (number & mask) / float(divisor)
```
