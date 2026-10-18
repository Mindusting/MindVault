---
aliases:
  - Comentarios en C
  - Comments in C
author: Mindusting
corrected: true
creationDate: 2026-09-05 12:40:15
headerFile: false
modificationDate: 2026-10-18 10:00:39
rating:
tags:
  - C
  - Programming
---

# COMENTARIOS EN C

> [!internal-link]- REFERENCIAS INTERNOS
> - [Comentarios en programación.](../../../fundamentals/basics/comment.md)

## COMENTARIOS DE UNA LÍNEA

Para crear un comentario de una línea tendremos que poner dos barras (`//`), el comentario se extiende hasta el final de la línea.

```c
// Esto es un comentario de una línea.
```

## COMENTARIOS MULTILÍNEA

Para crear un comentario multilínea tendremos que poner una barra y un asterisco (`/*`) este conjunto representa el comienzo del comentario, este comentario termina con el conjunto asterisco y barra (`*/`) o sé acabe el contenido del archivo, todo el texto que se encuentre entre estos dos conjuntos será un comentario.

```c
/*
Esto es un
comentario
multilínea.
*/
```

# COMENTARIOS TEMPORALES

Los comentarios temporales se pueden usar para *desactivar* código de forma temporal, permitiendo activar y desactivar código para hacer pruebas:

```c
/* <-- La diferencia está aquí.
Este texto está comentado.
//*/

//* <-- La diferencia está aquí.
Este texto no está comentado.
//*/
```
