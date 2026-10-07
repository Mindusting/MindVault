---
alias: Deep copy en programación
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming/Concept
title: Copia profunda en programación
---

# COPIA PROFUNDA EN PROGRAMACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

![#fillall](drawing/deepcopy_diagram.excalidraw.md)

```mermaid
flowchart LR
    ptr1("Array Original")
    ptr2("Array Copia")
    obj1(["Elemento 1"])
    obj2(["Elemento 2"])
    obj3(["Elemento 3"])

    ptr1 ----> obj3
    ptr1 ---> obj2
    ptr1 --> obj1
    ptr2 -.-> obj1
    ptr2 -..-> obj2
    ptr2 ~~~ obj3
```