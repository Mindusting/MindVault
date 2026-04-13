---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - C
title: Librería string en C
---

# LIBRERÍA STRING EN C

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/c/c_ref_string.php) #WWW/W3Schools

## MEMCHR

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/c/ref_string_memchr.php) #WWW/W3Schools

La [función](c_func.md) `memchr` se usa para obtener un [puntero](c_pointer.md) a la dirección de memoria en la que encuentre el primer **carácter** que coincida con el especificado; el caracter a buscar se especifica en el argumento `value` de tipo `int`, este es así para permitir los caracterres [**UFT-8**](../../data_format/utf-8.md); el argumento `size` indica hasta cuantos caracteres queremos que se lean, para buscar el valor; el valor que devuelve es un [puntero](c_pointer.md) a `void`, para que podeamos guardarlo en el tipo que queramos.

> [!syntax] SINTAXIS
> memchr(void \*ptr, int value, size\_t size)

## MEMCMP

## MEMCPY

## MEMMOVE

## MEMSET
