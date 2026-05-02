---
author: Mindusting
corrected: false
tags:
  - Programming
  - C
title: Librería stdio en C
---

# LIBRERÍA STDIO EN C

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!external-link]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/c/c_ref_stdio.php) #WWW/W3Schools

La librería `stdio` contiene [funciones](c_func.md) que facilitan el uso de la entrada y salida de datos en nuestro programa, como puede ser a través de la consola o archivos.

## PRINTF

La función `printf` permite imprimir en consola texto el cual podemos formatear, incrustando valores.

> [!syntax] SINTAXIS
> printf(***\[text\]\{, \[value\], ...\}***);

```c
// Incluimos la librería stdio
// en nuestro proyecto.
#include <stdio.h>

int main()
{
    // Imprimimos un mensage por consola.
    print("Hola mundo!\n");
    return 0;
}
```

## FGETC

> [!syntax] SINTAXIS
> fgetc(FILE \****\[file\]***)

## FGETS

> [!syntax] SINTAXIS
> fgets(char \****\[buffer\]***, int ***\[size\]***, FILE \****\[file\]***)
