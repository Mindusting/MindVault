---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming/Concept
  - RNG
title: Generación de número aleatorios en programación
---

# RNG EN PROGRAMACIÓN PROGRAMACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

```
s = s ^ (s << 13)
s = s ^ (s >> 7)
s = s ^ (s << 17)
```

```python
def rng(s: int) -> int:
    while True:
        s = s ^ (s << 13)
        s = s ^ (s >> 7)
        s = s ^ (s << 17)
        yield s
```
