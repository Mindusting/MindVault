---
aliases:
  - Comando Make
  - Archivos MakeFile
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - C
title: Makefile en C
---

# MAKEFILE EN C

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Mover esta documentación a otro sitio ya que `make` y los archivos `makefile` no son propios de C aunque se usen mucho, sirve a priori para cualquier archivo.

> [!help]- REFERENCIAS WEB
> YouTube:
> - [Jacob Sorber](https://youtu.be/a8mPKBxQ9No) #WWW/YT/JacobSorber

Los archivos **makefile** se usan para poder tener cubiertas las dependencias del proyecto de una forma más sencilla, ya que a medida que vamos añadiendo dependencias, el comando para compilar el proyecto puede ir complicandose, y por tanto podremos comenter más errores.

Para usar un archivo **makefile** trendremos que ir al directorio de nuestro proyecto y crearemos un archivo con el nombre `makefile`; dentro de este podremos definir comandos para ejercutar de forma sencilla.

Imaginemos que tenemos únicamente un archivo `main.c`, para automatizar la compilación del archivo con sus dependencias (*en este caso el uso de la librería math*), podremos hacerlo añadiendo lo siguiente en el archivo:

```makefile
main: main.c
    gcc -o main main.c -lm
```

Des esta forma, ejecutando el siguiente comando será como ejecuar el comando completo para compilarlo:

```bash
make main
```

