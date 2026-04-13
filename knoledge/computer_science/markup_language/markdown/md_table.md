---
aliases: [Tablas en Markdown]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Markdown]
---

# TABLAS EN MARKDOWN

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Rehacer toda la documentación con los estánders de ahora, ya que esta documentación fué de las primeras que hice.

> [!external-link]- REFERENCIAS WEB
> - [Obsidian](https://help.obsidian.md/Editing+and+formatting/Advanced+formatting+syntax#Tables) #WWW/Obsidian

Una lista está compuesta por títulos, justificación y celdas de contenido.

```md
| C. A | C. B | C. C |
|:-----|:----:|-----:|
|  A1  |  B1  |  C1  |
|  A2  |  B2  |  C2  |
|  A3  |  B3  |  C3  |
```
^ejemplo-1-de-tablas

| C. A | C. B | C. C |
|:-----|:----:|-----:|
|  A1  |  B1  |  C1  |
|  A2  |  B2  |  C2  |
|  A3  |  B3  |  C3  |

Como se puede ver en el ejemplo, la primera columna está justificada a la izquierda, la segunda está centrada y la tercera está justificada a la derecha, esto es debido a los guiones y doble puntos que se encuentran en la segunda línea.

| Just. izc. | Centrado | Just. der. |
|:----------:|:--------:|:----------:|
|    :--     |   :-:    |    --:     |

El número mínimo de caracteres para indicar la justificación es de un mínimo de tres, pero a este se le puede añadir guiones para hacer la tabla más estética, esto se puede ver en el anterior [ejemplo](<#^ejemplo-1-de-tablas>).

En este ejemplo se puede ver el uso que se le puede dar a las tablas, almacenando una lista de usuarios con su respectivo **ID**.

```md
| ID | NOMBRE |
|---:|:-------|
|  0 | admin  |
|  1 | Adelio |
|  2 | Jon    |
|  3 | Alex   |
```

| ID | NOMBRE |
|---:|:-------|
|  0 | admin  |
|  1 | Adelio |
|  2 | Jon    |
|  3 | Alex   |
