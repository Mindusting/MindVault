---
aliases: [Commits en Git]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Git]
---

# COMMITS EN GIT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar que hay que tratar que cada **commit** contenga un único cambio lógico.

> [!internal-link] REFERENCIAS INTERNAS
> - Para enteder bien esta documentación te recomiendo que tengas a mano la documentación a cerca de los [estados de los archivos en **Git**](file_states.md), ya que está bastante relacionado con el contenido de este archivo.

## DESCRIPCIÓN EN LOS COMMIT

### DESCRIPCIÓN BÁSICA (MONO LÍNEA)

> [!syntax] SINTAXIS
> ***\[type\]***: ***\[description\]***

- `feat` (*feature*): Nueva funcionalidad en el código.
- `fix`: Corrección de bug existente.
- `refactor`: Mejora sin cambiar comportamiento.
- `docs`: Documentación de código.
- `style`: Formato del código: espacios, sangría, camelCase, snake_case.
- `test`: Tests de código.
- `WIP` (*Work In Progress*): Indica que el *commit* contiene cambios que no están terminados, por lo que se está usando el *commit* como punto de guardado del avance (*==se debe evitar==; usa los [stashes](stashes.md)*).

> [!like] EJEMPLOS BUENOS
> - `feat: calculo de pitagoras con Vector 2D`
> - `fix: error de calculo de dot product con Vector 2D`
> - `refactor: función intToString`
> - `docs: función dot product con Vector 2D`
> - `style: sangría en pitagoras con Vector 2D`
> - `test: función intToSctring`
> - `WIP: calculo de interpolación de Vector 2D`

> [!dislike] EJEMPLOS MALOS
> - `arreglos`
> - `update`
> - `nuevas funciones`
> - `corrección`

### DESCRIPCIÓN EXTENDIDA (MÚLTI LÍNEA)

> [!syntax] SINTAXIS
> ***\[type\]***: ***\[description\]***
> ***\[extendedDescription\]***

## HASH DEL COMMIT
