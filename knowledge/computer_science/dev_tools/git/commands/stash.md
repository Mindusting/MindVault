---
aliases: [Comando stash en Git]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Git]
---

# COMANDO STASH EN GIT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!internal-link] REFERENCIAS INTERNAS
> - Para enteder bien esta documentación te recomiendo que tengas a mano la documentación a cerca de los [*stash* en **Git**](../theory/stashes.md), ya que contiene la parte teórica a cerca de los *stash*.

> [!syntax] SINTAXIS
> git stash

## LISTAR LOS STASHES

> [!syntax] SINTAXIS
> git stash list

> [!syntax] SINTAXIS
> stash@{***\[index\]***}: WIP on ***\[branch\]***: ***\[commitHash\] \[message\]***

## APLICAR UN STASH

> [!syntax] SINTAXIS
> git stash apply ***\{index\}***

Si no se especifica ningún *índice* se aplicará el *stash* más reciente (*el último stash guardado*) y si indicamos un *índice* se aplicará el *stash* con el *índice* correspondiente.

Cuando se aplica un *stash*, este no se quita de la pila de *stash*, si queremos quitarlo, tendremos que usar el [comando `drop`](#BORRAR%20UN%20STASH).

Si en el proceso de aplicado del *stash* ocurre algún conflicto entre los cambios (*al gual que puede pasar con [`merge`](merge.md)*), **Git** nos lo indicará y trendremos que resolverlo.

## BORRAR UN STASH

> [!syntax] SINTAXIS
> git stash drop

Al igual que con la aplicación de *stashes*, si no se especifica ningún *índice* se borrará el *stash* más reciente (*el último stash guardado*) y si indicamos un *índice* se borrará el *stash* con el *índice* correspondiente.
