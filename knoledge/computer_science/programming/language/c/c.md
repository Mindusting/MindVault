---
aliases: [Lenguaje C 🦖]
author: Mindusting
corrected: false
headerFile: true
logo: assets/c_logo.png
rating: 
tags: [C, Programming]
---

<h1 style="text-align:center;color:#888;">LENGUAJE C</h1>

![#logo](assets/c_logo.png)

---

# C

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

> [!external-link]- REFERENCIAS WEB
> YouTube:
> - [Bro Code (Lista de vídeos de C)](https://youtube.com/playlist?list=PLZPZq0r_RZOOzY_vR4zJM32SqsSInGMwe&si=pHjRGW8tcjLduB9E) #WWW/YT/BroCode
> 
> IA:
> - [Grokipedia](https://grokipedia.com/page/C_(programming_language)) #WWW/Grokipedia

> [!seealso] Ver también
> - [Comando `make`:](../../../../../temp/os/linux/command/make.md)
>     Sirve para poder trabajar sobre proyectos de programación más facilmente.
> - [Git:](../../../dev_tools/git/git.md)
>     Es un sistema de control de versiones, permite tener un desarrollo de proyecto más estructurado.

## ÍNDICE

- [ARCHIVOS DE C 📄](tools/c_file.md)
- [COMENTARIOS 💬](essentials/basics/comments.md)
- [ESTRUCTURA BÁSICA](essentials/basics/basic_structure.md)
- [VARIABLES 💾](essentials/basics/variable.md)
- [ARRAYS](essentials/memory/arrays.md)
- [PUNTEROS 👈](essentials/memory/pointers.md)
- [FUNCIONES](essentials/basics/functions.md)
- [ESTRUCTURAS 📦](essentials/basics/struct.md)
- [UNIÓN](essentials/basics/union.md)
- [MANEJO DE ARCHIVOS 📝](essentials/basics/file_management.md)
- [HEADER FILES](essentials/proyect_structure/header_files.md)
- [INLINE](essentials/advanced/inline.md)

## LIBRERÍAS

- [ctype](libs/standar/ctype.md)
- [math](libs/standar/math.md)
- [stdint](libs/standar/stdint.md)
- [stdio](libs/standar/stdio.md)
- [stdlib](libs/standar/stdlib.md)
- [string](libs/standar/string.md)
- [time](libs/standar/time.md)

## USO DE VARIBLES Y FORMATERO DE STRING

```c
#include <stdio.h>

int main()
{
    int age = 18;
    float height = 1.75;
    char chr = 'C';
    char name[] = "Mindusting";

    printf("Tu nombre es %s.\n", name);           // String
    printf("Tienes %d años.\n", age);             // Decimal
    printf("Mides %.2f metros.\n", height);       // Float
    printf("Tu lenguage favorito es %c.\n", chr); // Char

    return 0;
}
```

## TIPOS DE VARIBLES

Una variable puede ser `const`.

Las variables pueden ser `unsigned`.

Las variables `char` se pueden usar tanto como un número o un caracter (`%d` or `%c`).

Los Strings no exsiten, en cambio tenemos los array(s) de char (`%s`).

Las varibles `bool` son la booleanas (`%d`).

Los enteros cortos son `short int` o `sort` (`%d`).

Los valores enteros son `long int` o `int` (`%d` or `%u`).

Los valores largos son `long long int` o `long long` (`%lld` or `%llu`)

Los valores decimales son `float` (`%f`).

Los valores decimales son `double` (`%lf`).

### PRINT FORMAT

- <https://youtu.be/iLZOL-hmr7M?list=PLZPZq0r_RZOOzY_vR4zJM32SqsSInGMwe>

```c
#include <stdio.h>
#include <string.h>

int main()
{
    char name[32];

    printf("Escribe tu nombre: ");
    // fgets(name, 32, stdin)
    // name[strlen(name) - 1] = '\0'

    scanf("%s", name);

    printf("Hola %s.\n", name);

    return 0;
}
```
