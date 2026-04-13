---
aliases: [Comando switch en Git]
author: Mindusting
corrected: false
description: |-
    Se usa para cambiar entre ramas.
headerFile: false
rating: 
tags: [Git]
---

# COMANDO SWITCH EN GIT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

> [!seealso] Ver también
> - [Comando `checkout` en **Git**](checkout.md).

Este comando fué introducido en **Git 2.23**; en caso de posibilidad se recomienda usar este comando en vez de [`checkout`](checkout.md) ya que este es menos ambiguo y por tanto menos propenso a errores.

## CAMBIAR DE RAMA

> [!syntax] SINTAXIS
> git switch ***\[branchName\]***

## CREAR RAMA Y CAMBIARSE A ELLA

Crea la rama y nos situamos sobre ella.

> [!syntax] SINTAXIS
> git switch -c ***\[branchName\]***

## DESACOPLAR HEAD

Para desacoplar **HEAD** de una rama se debe usar la opción `--detach`:

> [!syntax] SINTAXIS
> git switch --detach ***\[commitHash\]***
