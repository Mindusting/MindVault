---
aliases: [Comando branch en Git]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Git]
---

# COMANDO BRANCH EN GIT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

> [!internal-link] REFERENCIAS INTERNAS
> - Para enteder bien esta documentación te recomiendo que tengas a mano la documentación a cerca de las [ramas en **Git**](../theory/branches.md), ya que contiene la parte teórica a cerca de las ramas.

## CREAR RAMA

Para crear una nueva rama se usa el comando `git branch` seguido del nombre.

> [!syntax] SINTAXIS
> 
> git branch ***\[newBranchName\]***

Esto crea una rama con el nombre indicado en el **commit** en el que está situada la cabeza (*head*); hay que tener en cuenta que no cambia automáticamente a esta rama (*para ello se usa el comando [`git checkout`](checkout.md)*), a menos que estemos con la cabeza desconectada (*head detached*) y creemos por tanto una rama en un **commit** que no tenga ninguna, en ese caso la cabeza (*head*) apuntará a la nueva rama automáticamente.

### CREAR RAMA EN UN COMMIT EN CONCRETO

Para crear una rama en un **commit** en concreto sin que haga falta que estemos situado en él, podemos hacerlo añadiendo al final bien el *hash* del **commit** sobre el que queremos que se cree la nueva rama o con el nombre de una rama ya existente, por si queremos crear otra rama donde ya existe una.

> [!syntax] SINTAXIS
> 
> git branch ***\[newBranchName\] \[commitHash\|branchName\]***

## LISTAR RAMAS

Para poder listar las ramas y así poder ver como se llaman, podemos usar el comando `git branch` sin especificar ningún argumento:

```bash
git branch
```

```txt
* main
  testing
```

El asterisco (`*`) indica que la cabeza (*head*) está situada en esa rama; si la cabeza está desconectada (*detached head*) debería de aparecer un primer elemento en la lista el cual tendrá el asterisco (`*`), este será un mensaje entre paréntesis indicando que la cabeza (*head*) está situada en un **commit** e indicará el *hash* del **commit**.

Sería algo parecido a esto:

```txt
* (HEAD detached at cb866dc)
  main
  testing
```

## MOVER RAMA

Para mover una rama se puede hacer con el argumento `-f` seguido del nombre de la rama que queremos mover y bien el nombre de otra rama o el hash de un commit a la que queremos mover la.

> [!syntax] SINTAXIS
> 
> git branch -f ***\[branch (from)\] \[branch/commit (to)\]***

## BORRAR RAMA

Para borrar una rama se hace de la misma forma que crearlas pero con el argumento `-d`:

> [!syntax] SINTAXIS
> 
> git branch -d ***\[newBranchName\]***

```bash
git branch -d testing
```

Si borrar la rama implicaría que se perdiese algún [*commit*](../theory/commits.md) devido a que ya no tendría referencia, [*Git*](../git.md) se negará a borrarlo y nos avisará con un mensaje indicando que debemos usar `-D` en vez ce `-d` para forzar el borrado; ==cuidado con lo que estás borrando, podría ser algo que no quieras perder==.

En el caso en el que sepacom que sí queremos borrar esa rama junto con la perdida de datos que esto conlleva, tendremos que seguir la siguiente sintaxis (*que en esencia es lo mismo que el anterior pero usando `D` mayúscula en vez de minúscula*):

> [!syntax] SINTAXIS
> 
> git branch -D ***\[newBranchName\]***