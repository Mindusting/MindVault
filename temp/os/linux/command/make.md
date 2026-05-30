---
aliases:
  - Comando MAKE
  - Archivos Makefile 🔨
author: Mindusting
corrected: false
headerFile: false
tags:
  - Makefile
---

# COMANDO MAKE Y ARCHIVOS MAKEFILE

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > 
> > - [ ] Mover este archivo a donde corresponde.
> > - [ ] Explicar para qué sirven el comando `make`.
> > - [ ] Explicar para qué sirven los archivos `makefile`.
> > - [ ] Explicar las variables.
> >     - [ ] Explicar como establecer varibles desde la ejecución del comando `make`.
> >     - [ ] Explicar las variables automáticas.
> > - [ ] Explicar que una instrucción se divide en *objetivo*, *dependencias* y *comando*.

El comando `make` junto a los archivos `Makefile` son una herramienta muy buena para los programadores, ya que permite automatizar ciertas tareas durante el desarrollo, como por ejemplo la compilación de todos los archivos, ejecución del programa, lipieza de los archivos temporales y cubrir dependencias.

Cuando nosotro ejecutamos el comando `make` este buscará en el directorio en el que nos encontremos un archivo con el nombre `Makefile` y ejecutará las instrucciones que le hayamos indicado.

---

Imaginemos que tenemos la siguiente estructura en un proyecto:

```txt
/.
|- main.c
|- Makefile
```

Dentro del archivo `Makefile` podríamos tener algo así:

```makefile
all: main.c
    gcc -o main main.c -lm && ./main
    # Combinamos compilación y ejecución.

compile: main.c
    gcc -o main main.c -lm
    # Compilamos el archivo con sus dependencias.

run: main
    ./main
    # Ejecutamos el archivo.

clear:
    rm ./main
    # Borramos el ejecutable.
```
