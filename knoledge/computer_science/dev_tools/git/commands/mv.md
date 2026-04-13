---
aliases: [Comando mv en Git]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Git]
---

# COMANDO MV EN GIT

> [!unfinished-file]- ESTE APARTADO ESTA INCOMPLETO
> 
> > [!todo] #TODO

Para mover o renombrar archivo en Git se usa el comando `git mv` en sustituto del comando del sistema `mv`, ya que el de Git nos ahorra el tener que [borrar el archivo](rm.md) original y [añadir el nuevo](add.md) de forma manual; es decir, que nos quita el archivo antiguo del estado *staged* y nos añade el nuevo archivo a este estado.

> [!syntax] SINTAXIS
> git mv ***\[origin\] \[destine\]***

---

```bash
git mv readme.md readme
```

Equivale a hacer:

```bash
mv readme.md readme
git rm readme.md
git add readme
```
