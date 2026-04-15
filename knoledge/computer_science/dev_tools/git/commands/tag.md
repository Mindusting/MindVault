---
aliases: [Comando tag en Git]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Git]
---

# COMANDO TAG EN GIT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Revisar que me he podido dejar.

> [!internal-link] ENLACES INTERNOS
> Antes de ver como usar el comando `tag`, recomiendo que veas como funcionan las [etiquetas en **Git**](../theory/tags.md).

Las etiquetas permiten marcar **commits** en Git, generalmente usado para marcar versiones del programa (*`1.0`, `2.0`, etc*)

> [!syntax] SINTAXIS
> git tag ***\[tagName\] [\{options\}](#^options) \{target\}***

Opciones (*options*):

- `-a`, `--annotate`: esta opción indica que queremos anotar la etiqueta, es decir, que le queremos adjuntar un texto que irá relacionada a ella; si no se especifica la opción [`-m`](#^option-m), se nos abrirá el editor de texto que tengamos establecido y podremos escribir la anotación.
^option-a
- `-m <msg>`, `--message=<msg>`: esta opción va seguida de un mensaje (*preferiblemente entrecomillado para evitar problemas*) que es el que hará de anotación de la etiqueta; si se especifica la opción [`-a`](#^option-a) junto a esta otra, no se abrirá el editor de texto por defecto.
^option-m
- `-l <pattern>` o `--list <pattern>`: esta opción indica que queremos listar las etiquetas existentes; el patrón es opcional, en caso de que no se indique, se listan todas las etiquetas; si se indica un patrón, se listará todas las etiquetas que cumplan con ese patrón.
^option-l
- `-d` o `--delete`: esta opción va seguida de por lo menos el nombre de una etiqueta, se usa para eliminar etiquetas.
^option-d

^options

Objetivo (*target*):

El parámetro `target` (*que es opcional*), permite indicar a qué [**commit**](../theory/commits.md) queremos que apunte la etiqueta, bien con el [**hash** del **commit**](../theory/commits.md#HASH%20DEL%20COMMIT), el nombre de una [**rama**](../theory/branches.md).

## LISTAR ETIQUETAS

Para listar etiquetas se puede hacer de varias formas dependiendo de qué es lo que necesitemos hacer:

- [Listar todas las etiquetas](#LISTAR%20TODAS%20LAS%20ETIQUETAS)
- [Listar listar etiquetas por patrón](#LISTAR%20ETIQUETAS%20POR%20PATRÓN)

### LISTAR TODAS LAS ETIQUETAS

Para listar todas las *tags* se usa el comando `git tag`, no necesita ningún argumento más.

```bash
git tag
```

```txt
v1.0
v1.1
v1.2
v2.0
v2.1
```

### LISTAR ETIQUETAS POR PATRÓN

Si queremos listar las etiquetas que cumplan con un patón en concreto a modo de filtro se usa el argumento [`-l` o `--list`](#^option-l) seguido del patrón (*UNIX*) entrecomillado.

```bash
git tag -l "v2.*"
```

```txt
v2.0
v2.1
```

## CREAR ETIQUETAS

Para crear etiquetas se puede hacer de varias formas, el como lo vayamos a hacer dependerá de cual sea nuestro objetivo:

> [!example] EJEMPLO: Creación de etiqueta ligera
> 
> ```bash
> git tag v1.0
> ```
> 
> Este comando crea la etiqueta `v1.0` relacionada al [**commit**](../theory/commits.md) en el que estemos situado.

> [!example] EJEMPLO: Creación de una etiqueta con anotación corta.
> 
> ```bash
> git tag v1.1 -m "Sigue siendo retrocompatible con v1.0"
> ```
> 
> Este comando crea la etiqueta `v1.1` relacionada al [**commit**](../theory/commits.md) en el que estemos situado y asocia el mensaje indicado a la propia etiqueta.

> [!example] EJEMPLO: Creación de una etiqueta con anotación.
> 
> ```bash
> git tag v2.0 -a
> ```
> 
> Este comando crea la etiqueta `v2.0` relacionada al [**commit**](../theory/commits.md) en el que estemos situado y asocia el mensaje indicado a la propia etiqueta.

## ELIMINAR ETIQUETAS

> [!example] EJEMPLO: Eliminación de una etiqueta
> 
> ```bash
> git tag -d testTag
> ```
> 
> Este comando elimina la etiqueta `testTag`.

> [!example] EJEMPLO: Eliminación de una etiqueta
> 
> ```bash
> git tag -d tempTag1 tempTag2 tempTag3
> ```
> 
> Este comando elimina las etiquetas `tempTag1`, `tempTag2` y `tempTag3`.
