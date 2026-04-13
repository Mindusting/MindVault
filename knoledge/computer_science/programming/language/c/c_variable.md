---
author: Mindusting
corrected: false
tags:
  - Programming
  - C
title: Variables en C
---

# VARIABLES EN C

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> YouTube:
> - [Bro Code](https://youtu.be/aIQk1O08zpg) #WWW/YT/BroCode

> [!faq]- FAQ
> - [¿Qué son las variables en programación?](../../../../../temp/pc/pc_variable.md)

**C** es un lenguaje de tipado fuerte, esto quiere decir que cuando declaramos una **variable**, debemos indicar el tipo de valor que va a almacenar y este no se podrá cambiar en el transcurso del programa, los tipos son los siguientes:

| NAME        | TYPE    | SIZE IN BYTES |
|:----------- |:------- |:------------- |
| char        | Integer | 1             |
| short       | Integer | 2             |
| int         | Integer | 2 or 4        |
| long        | Integer | 4 or 8        |
| long long   | Integer | 8             |
| float       | Decimal | 4             |
| double      | Decimal | 8             |
| long double | Decimal | 16            |

%%
SINTAXIS

```c
[variable_type] [variable_name];
[variable_type] [variable_name] = [value];
```
%%

> [!abstract] SINTAXIS
> <span class="italic key-word-color">[variable_type]</span><span class="italic variable-color">[variable_name]</span>;
> <span class="italic key-word-color">[variable_type]</span><span class="italic variable-color">[variable_name]</span> = <span class="italic grey">[value]</span>;

```c
#include <stdio.h>

int main(void) {

    int amountOfBits = 0;
    unsigned char byte = 0;
    unsigned char tempByte;

    while (1) {
        tempByte = byte;
        byte <<= 1;
        byte += 1;

        if (byte == tempByte) break;

        amountOfBits++;
    }

    printf("SIZES ON THIS MACHINE\n");
    printf("---------------------\n");
    printf("byte:        %2d bits\n", amountOfBits);
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

```txt
SIZES ON THIS MACHINE
---------------------
byte:         8 bits
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
