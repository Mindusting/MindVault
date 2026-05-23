---
aliases: [Proyectos en Java]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Java, Programmin]
---

# PROYECTOS EN JAVA

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

```txt
./ (directorio del proyecto)
 |-/src (aquí va el código fuente)
 |-/bin (aquí va el código compilado)
 |- makefile
```

**makefile:**

```makefile
all:
    rm -r bin/* && \
    javac -sourcepath src -d bin src/Main.java && \
    clear && \
    java -cp bin Main.java

compile:
    javac -sourcepath src -d bin src/Main.java

run:
    java -cp bin Main.java

clear:
    rm -r bin/*
```
