---
aliases: [Comando commit en Git]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Git]
---

# COMANDO COMMIT EN GIT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Documentar argumento `-m`.
> > - [ ] Documentar argumento `-am`.
> > - [ ] Documentar argumento `--amend`.

> [!internal-link] REFERENCIAS INTERNAS
> - Recomiendo que antes de empezar a ver esta documentación a cerca del comando `commit`, veas primero la teoría sobre los [**commits**](../theory/commits.md).

- `-a`: añade todos los cambios de archivos que ya estuvieran siendo observados por Git al **commit** a realizar.
- `-m`: este parámetro debe estar seguido de un texto entrecomillado el cual será la descripción del **commit** a realizar.

---

```bash
git init
echo "# README" > readme.md
git add readme.md
git commit -m "Inicio del proyecto"
echo "Esta es una nueva líena" >> readme.md
git commit -a -m "Modificación del readme.md"
```

## DESCRIPCIÓN BÁSICA (MONO LÍNEA)

> [!syntax] SINTAXIS
> git commit -m "***\[basicDescription\]***"

## DESCRIPCIÓN EXTENDIDA (MULTI LÍNEA)

> [!syntax] SINTAXIS
> git commit
