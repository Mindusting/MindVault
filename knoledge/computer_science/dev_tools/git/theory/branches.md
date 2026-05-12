---
aliases: [Ramas en Git]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Git]
---

# RAMAS EN GIT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Una **rama** se define como una **línea independiente de desarrollo** que permite trabajar sobre el código sin alterar el comportamiento del proyecto hasta que esta **rama** se integra de forma definitiba al propio proyecto; permitiendo así aislar las modificaciones del código.

Una explicación un poco más técnica sería que una **rama** es un puntero a un [*commit*](commits.md), permitiendo de esta forma identificaer un [*commit*](commits.md) mediante un nombre (*este nombre es la rama*).

Cuando creamos un [repositorio](repositories.md) de **Git** este contiene una **rama** llamda `master` (*a la cual se le suele cambiar el nombre, por ejemplo `main`; aunque no es necesario*); esto ocurre de esta forma, ya que no puede haver un [repopsitorio](repositories.md) sin **ramas**, siempre debe haber por lo menos una; es decir un proyecto puede tener de $1$ a $N$ **ramas**.

## TRABAJAR SOBRE UNA RAMA

Cuando estamos empezando a usar **Git** lo normal es usar solo una **rama**, y a medida que vamos entendiendo como trabajar sobre una **rama**, nos animamos a trabajar sobre varias (*para empezar, con dos*) y es cuando descubrimos el verdadero potencial de **Git**.

Para empezar, imaginemos que tenemos solo una **rama** a la que llamaremos `main`, dentro de esta se han hecho unos cambios y en total se han realizado tres [*commits*](commits.md) (*A, B, C*); cada uno de los [*commits*](commits.md) apunta a su padre y la **rama** `main` apunta al último de los [*commits*](commits.md)

%%
```txt
Esto es la rama main ->  [main]
                           v
(A)<---------(B)<---------(C)
    Estos son los commits
```
%%

![#center](../assets/branch_main.md)

## TRABAJAR SOBRE VARIAS RAMAS
