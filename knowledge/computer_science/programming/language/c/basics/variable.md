---
aliases: [Variables en C]
author: Mindusting
corrected: false
creationDate: 2026-09-05 12:40:15
cssclasses: [center-table]
headerFile: false
modificationDate: 2026-10-18 10:11:59
rating: 
tags: [C, Programming]
---

# VARIABLES EN C

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Añadir un enlace al apartado de booleanos en la especificación del valor `_Bool`.

> [!external-link]- REFERENCIAS WEB
> YouTube:
> - [Bro Code](https://youtu.be/aIQk1O08zpg) #WWW/YT/BroCode

> [!internal-link]- REFERENCIAS INTERNAS
> - [Variables en programación.](../../../fundamentals/temp-dump/pc_variable.md)

C es un lenguaje de programación con tipado estático, esto quiere decir que una vez hemos declarado el tipo de dato que va a guardar una variable, no puede cambiar durante el transcurso de la ejecución; para declarar una variable en este lenguaje tendremos que seguir la siguiente sintaxis:

> [!syntax] SINTAXIS
> ***\{sign\} \[dataType\] \[varName\]***;

El nombre de la variable debe de estar conformado por letras [ASCII](../../../data_format/ascii.md), barra baja (`_`) y números siempre y cuando no sean el primer caracter.

Los tipos de datos de números enteros pueden llevar por delante el signo; para indicar que el tipo debe ser con signo pondremos `signed` y para indicar que no debe tener signo `unsigned`.

Ahora, el tipo de dato es más complicado, ya que C nos ofrece unos tipos estandar, pero también podemos crear nuestros propios tipos (*esto último lo veremos más adelante y en otros documentos*); los tipos de datos estandar son los siguientes:

- `_Bool`:
    Este permite guardar un `0` o un `1`, ya que es para guardar valore booleanos.
    El signo no es aplicable en este tipo de dato.
    Tiene un tamaño de 1 byte.

- `char`:
    Este permite guardar números enteros.
    No tiene un signo asignado (*depende de la máquina*).
    Tiene un tamaño de 1 o más bytes.

- `short` o `short int`:
    Este permite guardar números enteros.
    Este tipo por defecto tiene signo.
    Tiene un tamaño de 2 o más bytes.

- `int`:
    Este permite guardar números enteros.
    Este tipo por defecto tiene signo.
    Tiene un tamaño de 2 o más bytes.

- `long` o `long int`:
    Este permite guardar números enteros.
    Este tipo por defecto tiene signo.
    Tiene un tamaño de 4 o más bytes.

- `long long` o `long long int`:
    Este permite guardar números enteros.
    Este tipo por defecto tiene signo.
    Tiene un tamaño de 8 o más bytes.

- `float`:
    Este permite guardar números de coma flotante.
    Siempre tiene signo.
    Tiene un tamaño de 4 bytes.

- `double`:
    Este permite guardar números de coma flotante.
    Siempre tiene signo.
    Tiene un tamaño de 8 bytes.

- `long double`:
    Este permite guardar números de coma flotante.
    Siempre tiene signo.
    Tiene un tamaño de 8 bytes o más.

Los tipos de número entero tienen que cumplir la siguiente regla:

%%
char <= short <= int <= long <= long long
%%

$$
char \leq short \leq int \leq long \leq long long
$$

## TAMAÑO DE LOS TIPOS BÁSICOS

Para poder comprobar el tamaño concreto en tu máquina puedes compilar el siguiente programa en ella y luego ejecutarlo:

```c
#include <stdio.h>
#include <limits.h>

int main(void) {

    printf("SIZES ON THIS MATHINE\n");
    printf("---------------------\n");
    printf("byte:        %2d bits\n", CHAR_BIT);
    printf("---------------------\n");
    printf("_Bool:       %2zu bytes\n", sizeof(_Bool));
    printf("---------------------\n");
    printf("char:        %2zu bytes\n", sizeof(char));
    printf("short:       %2zu bytes\n", sizeof(short));
    printf("int:         %2zu bytes\n", sizeof(int));
    printf("long:        %2zu bytes\n", sizeof(long));
    printf("long long:   %2zu bytes\n", sizeof(long long));
    printf("---------------------\n");
    printf("float:       %2zu bytes\n", sizeof(float));
    printf("double:      %2zu bytes\n", sizeof(double));
    printf("long double: %2zu bytes\n", sizeof(long double));
    printf("---------------------\n");
    printf("void*:       %2zu bytes\n", sizeof(void*));
    printf("size_t:      %2zu bytes\n", sizeof(size_t));

    return 0;
}
```

---

En mi máquina el resultado es el siguiente:

```txt
SIZES ON THIS MATHINE
---------------------
byte:         8 bits
---------------------
_Bool:        1 bytes
---------------------
char:         1 bytes
short:        2 bytes
int:          4 bytes
long:         8 bytes
long long:    8 bytes
---------------------
float:        4 bytes
double:       8 bytes
long double: 16 bytes
---------------------
void*:        8 bytes
size_t:       8 bytes
```
