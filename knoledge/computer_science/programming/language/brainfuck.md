---
aliases: [BrainFuck 🧠]
author: Mindusting
corrected: false
creationDate: 2026-09-05 12:39:51
headerFile: true
modificationDate: 2026-09-15 05:26:06
rating: 
tags: [Programming]
---

# BRAINFUCK

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Explicar las bases del lenguaje.
> > - [ ] Hacer un mejor ejeplo de un pequeño programa en BrainFuck.
> > - [ ] Añadir un programa escrito en C para poder ejecutar código BrainFuck.

> [!external-link]- REFERENCIAS WEB
> - [brainfuck](https://brainfuck.org) #WWW/brainfuck



```brainfuck
[ Todo este bloque es un comentario:

    Este texto ha sido escrito por "Mindusting", este es un
    programa escrito para ser ejecutado por el intreprete de
    BrainFuck, pudiendo ser usado como una mini máquina
    virtual para futuros programas.

    Los únicos caracteres que necesita este lenguaje son los
    siguientes:
        + y -: permite incrementar y decrementar el valor del
        byte al que apunta la cabeza de la memoria.

        [ y ]: permite definir los bucles y condicionales,
        ya que su comportamiento es similar al "jump if
        not cero".

        > y <: permiten desplazar la cabeza (puntero) de la
        memoria un byte a la derecha o izquierda respectivamente.

        . y ,: permiten mandar al stdout el byte que se encutra
        sobre la cabeza de la memoria o recibir un byte desde
        el stdin y escribirlo bajo la cabeza de la memoria.

    Este programa en particular, sencillamente escribe el
    texto "HOLA" a través del stdout, puediendo llegar a ser
    redirigido a otro FILE.
]

++++++++++[ Establecemos los valores del texto en magnitudes de 10
    >+++++++
    >++++++++
    >++++++++
    >++++++
    >+
    [<]>- Al final del bucle volvemos al inicio y restamos un ciclo
]
>++ Establecemos los valores en magnitudes de 1
>-
>----
>+++++
>
[<]> Vamos hasta el inicio del string
[.>] Imprimimos todo el string
<[[-]<] Borramos el string desde el final al principio
```
