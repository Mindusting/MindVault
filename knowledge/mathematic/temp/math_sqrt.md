---
aliases:
  - Raizes cuadradas
author: Mindusting
corrected: false
headerFile: false
tags:
  - Math
---

# RAIZ CUADRADA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

$$
y_{n+1} = \frac{1}{2} (y_n + \frac{x}{y_n})
$$

```c
float sqrtf(float x) {
    float res = x;
    float y;

    do {
        y = res;
        res = (y + x / y) * 0.5;
    } while (res != y);

    return res;
}
```
