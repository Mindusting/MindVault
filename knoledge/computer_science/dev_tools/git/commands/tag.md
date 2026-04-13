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

Las etiquetas permiten marcar **commits** en Git, generalmente usado para marcar versiones del programa (*`1.0`, `2.0`, etc*)

## LISTAR TAGS

Para listar etiquetas se puede hacer de varias formas dependiendo de qué es lo que necesitemos hacer:

- [Listar todas las tags](#LISTAR%20TODAS%20LAS%20TAGS)
- [Listar listar etiquetas por patrón](#LISTAR%20LISTAR%20ETIQUETAS%20POR%20PATRÓN)

### LISTA TODAS LAS TAGS

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

### LISTAR LISTAR ETIQUETAS POR PATRÓN

Si queremos listar las etiquetas que cumplan con un patón en concreto a modo de filtro se usa el argumento `-l` o `--list` seguido del patrón (*UNIX*) entrecomillado.

```bash
git tag -l "v2.*"
```

```txt
v2.0
v2.1
```

## CREAR TAGS

## ELIMINAR TAGS
