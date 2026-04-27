---
aliases: [Librería string en C]
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - C
---

# LIBRERÍA STRING EN C

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!external-link]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/c/c_ref_string.php) #WWW/W3Schools

## MEMCHR

> [!external-link]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/c/ref_string_memchr.php) #WWW/W3Schools

La [función](c_func.md) `memchr` se usa para obtener un [puntero](c_pointer.md) a la dirección de memoria en la que encuentre el primer **carácter** que coincida con el especificado; el caracter a buscar se especifica en el argumento `value` de tipo `int`, este es así para permitir los caracterres [**UFT-8**](../../data_format/utf-8.md); el argumento `size` indica hasta cuantos caracteres queremos que se lean, para buscar el valor; el valor que devuelve es un [puntero](c_pointer.md) a `void`, para que podeamos guardarlo en el tipo que queramos.

> [!syntax] SINTAXIS
> memchr(void \*ptr, int value, size\_t size)

## MEMCMP

## MEMCPY

la [función](c_func.md) `memcpy` se usar para copiar una región de memoria en otra; hay que tener cuidado con esta [función](c_func.md), ya que no es segura con la memoria, esto se debe a que podemos copiar una porción de memoria (*la fuenente \[`src`\]*) en otra más pequeña (*el destino \[`dst`\]*), esto modificaría memoria que no corresponde, pudiendo probocar un "*undefined behavior*", es decir que no podemos saber con certeza el comportamiento que tendrá.

> [!syntax] SINTAXIS
> memcpy(void \*dst, const void \*src, size\_t size)

```c
#include <stdio.h>

```

## MEMMOVE

## MEMSET
