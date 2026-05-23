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

La [función](../../essentials/basics/functions.md) `memchr` se usa para obtener un [puntero](../../essentials/memory/pointers.md) a la dirección de memoria en la que encuentre el primer **carácter** que coincida con el especificado; el caracter a buscar se especifica en el argumento `value` de tipo `int`, este es así para permitir los caracterres [**UFT-8**](../../../../data_format/utf-8.md); el argumento `size` indica hasta cuantos caracteres queremos que se lean, para buscar el valor; el valor que devuelve es un [puntero](../../essentials/memory/pointers.md) a `void`, para que podeamos guardarlo en el tipo que queramos.

> [!syntax] SINTAXIS
> memchr(void \*ptr, int value, size\_t size)

## MEMCMP

## MEMCPY

La [función](../../essentials/basics/functions.md) `memcpy` se usar para copiar una región de memoria en otra; hay que tener cuidado con esta [función](../../essentials/basics/functions.md), ya que no es segura con la memoria, esto se debe a que podemos copiar una porción de memoria (*la fuenente \[`src`\]*) en otra más pequeña (*el destino \[`dst`\]*), esto modificaría memoria que no corresponde, pudiendo probocar un "*undefined behavior*", es decir que no podemos saber con certeza el comportamiento que tendrá.

> [!syntax] SINTAXIS
> memcpy(void \*dst, const void \*src, size\_t size)

## MEMMOVE

## MEMSET

La [función](../../essentials/basics/functions.md) `memset` permite establecer un mismo valor acada *byte* de una región de memoria especificada mediante un [puntero](../../essentials/memory/pointers.md) y tamaño en *bytes* de la región de memoria.

> [!syntax] SINTAXIS
> memset(void \*ptr, int value, size\_t size)

- `void *ptr`: indica la direcció de memoria en donde comienza la porción a la que queremos establecerle un valor.
- `int value`: indica el valor que queremos escribir en los distintos *bytes* de la memoria.
- `size_t size`: indica el tamaño en *bytes* de la región de la memoria a la que queremos establecer los valores.
