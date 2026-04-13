---
aliases:
  - Compilación de Java
author: Mindusting
corrected: false
tags:
  - Programming
  - Java
  - Package
---

# COMPILACIÓN DE JAVA

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar como compilar archivos de Java.
> > - [ ] Explicar como ejecutar archivos de Java.

```makefile
all: src/main/Main.java
    javac src/main/Main.java -sourcepath src -d bin && java -cp bin main.Main

comp: src/main/Main.java
    javac src/main/Main.java -sourcepath src -d bin

run: bin/main/Main.class
    java -cp bin main.Main

clear: bin
    rm -rf bin
```
