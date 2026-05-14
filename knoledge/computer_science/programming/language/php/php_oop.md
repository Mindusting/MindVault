---
aliases: [OOP en PHP, Programación orientada a objetos en PHP, Clases en PHP]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [OOP, PHP, Programming]
---

# OOP EN PHP

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

> [!internal-link] REFERENCIAS INTERNAS
> Antes de empezar a leer esta documentación, recomiendo que tengas a mano la documentación a cerca de la [OOP (*Object Oriented Programmin*)](../../fundamentals/temp-dump/pc_oop.md); ya que es la parte teórica y general de este apartado, en el que se va a ver la [OOP](../../fundamentals/temp-dump/pc_oop.md) concretamente de [**PHP**](php.md).

## DECLARACIÓN DE CLASES

> [!syntax] SINTAXIS
> class ***\[className\]*** {***\[classBody\]***}

### PROPIEDADES

> [!syntax] SINTAXIS
> ***[\[accessMod\]](#MODIFICADORES%20DE%20ACCESO) \[propertyName\]\{*** = ***\[value\]\};***

### MÉTODOS

> [!syntax] SINTAXIS
> ***[\{accessMod\}](#MODIFICADORES%20DE%20ACCESO)*** function ***\[methodName\]***(***\[parameters\]***) {***\[methodBody\]***}

### MODIFICADORES DE ACCESO

El modificador de acceso predeterminado para los [**métodos**](#MÉTODOS) es `public`, sin embargo, las [**propiedades**](#PROPIEDADES) no puede no tener un **modificador de acceso** (*esto último se aplica desde la versión 7.4 de PHP*).

| MODIFICADOR | DENTRO | SUB | FUERA |
|:----------- |:------ |:--- |:----- |
| `public`    | Sí     | Sí  | Sí    |
| `protected` | Sí     | Sí  | NO    |
| `private`   | Sí     | NO  | NO    |

^access-modifiers-table

### CONSTRUCTOR

> [!syntax] SINTAXIS
> [***\{accessMod\}***](#MODIFICADORES%20DE%20ACCESO) function \_\_constructor(***\[parameters\]***) {***\[body\]***}

## CREACIÓN DE OBJETOS

> [!syntax] SINTAXIS
> new [***\[className\]***](#DECLARACIÓN%20DE%20CLASES)(***\[arguments\]***)

## ACCESO A PROPIEDADES Y MÉTODOS

> [!syntax] SINTAXIS
> ***\[objectName\]***->***\[propertyName/methodName\]***

### ACCESO DE FORMA DINÁMICA

> [!syntax] SINTAXIS
> ***\[objectName\]***->{***\[propertyName/methodName\]***}
