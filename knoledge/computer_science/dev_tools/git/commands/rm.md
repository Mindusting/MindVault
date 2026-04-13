---
aliases: [Comando rm en Git]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Git]
---

# COMANDO RM EN GIT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

A la hora de borrar archivos en Git se recomienda usa el comando `rm` que ofrece Git: `git rm` en vez de usar el `rm` del sistema, ya que al usar el que nos provee Git, este añadirá este cambio al estado *staged* automáticamente, a diferencia de lo que ocurriría con el `rm` del sistema, con el que tendremos que después usar el comando [`add`](add.md).

---

```bash
git rm test.md
```
