---
author: Mindusting
corrected: true
tags:
  - Mermaid
title: Diagrama circular en Mermaid
rating: 1.0
---

# DIAGRAMA CIRCULAR EN MERMAID

> [!help]- REFERENCIAS WEB
> - [Mermaid](https://mermaid.js.org/syntax/pie.html) #WWW/Mermaid

Para poder crear un diagrama de (proporción, circular o "*de pastel*") debemos seguir la siguiente sintaxis:

> [!abstract] SINTAXIS
> [***\[header\]***](#ENCABEZADO)
> [***\[key-value\]***](#VALORES)
> ***...***

## ENCABEZADO

El identificador de los diagramas de PIE es el `pie`; se puede poner de forma opcional la palabra clave `title` seguido del título que queremos que tenga el esquema.

> [!abstract] SINTAXIS
> pie ***\{showData\} \{title \[title\]}***

```txt
pie title Este es mi título
```

## VALORES

Para indicar los valores que se deben mostrar en el diagrama se hace mediante un par de *clave*, *valor*; estos se separan por dos *puntos* (`:`) y un *espacio* (` `) a cada lado.

> [!abstract] SINTAXIS
> "***\[key\]***" : ***\[value\]***

## EJEMPLOS

```txt
pie showData title Proporción de mascotas
    "Gatos" : 3
    "Perros" : 2
```

```mermaid
pie showData title Proporción de mascotas
    "Gatos" : 3
    "Perros" : 2
```

---

```txt
pie title Por qué no salgo de casa
    "C" : 256
    "C (En otro color)" : 128
    "Python" : 64
    "SQL" : 32
```

```mermaid
pie title Por qué no salgo de casa
    "C" : 256
    "C (En otro color)" : 128
    "Python" : 64
    "SQL" : 32
```
