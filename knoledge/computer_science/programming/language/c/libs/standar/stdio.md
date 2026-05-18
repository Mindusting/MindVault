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
> - [Wikipedia](https://es.wikipedia.org/wiki/Stdio.h) #WWW/Wikipedia

La librería `stdio` contiene [funciones](../../essentials/basics/functions.md) que facilitan el uso de la entrada y salida de datos en nuestro programa, como puede ser a través de la consola o archivos.

## FUNCIONES

### FCLOSE

### FEOF

### FERROR

### FGETC

> [!syntax] SINTAXIS
> fgetc(FILE \****\[file\]***)

### FGETS

> [!syntax] SINTAXIS
> fgets(char \****\[buffer\]***, int ***\[size\]***, FILE \****\[file\]***)

### FOPEN

### FPRINTF

### FPUTC

### FPUTS

### FREAD

### FSCANF

### FSEEK

### FTELL

### FWRITE

### GETC

### GETCHAR

### PRINTF

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

### PUTC

### PUTCHAT

### PUTS

### REMOVE

### RENAME

### REWIND

### SCANF

### SNPRINTF

### SSCANF
