---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming/Concept
  - Rcursivity
title: Recursividad en programación
---

# RECURSIVIDAD EN PROGRAMACIÓN

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!faq]- FAQ
> - [¿Qué es la recursividad?](../../dump/recursivity.md)

$$
n! = n \cdot (n-1)!
$$

```python
def main():
    for i in range(1, 16):
        print(f"{i:>3}: {factorial(i):>14}")


def factorial(n: int) -> int:
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1


if "__main__" == __name__:
    main()
```

Tabla de resultado:

|  N |     FACTORIAL |
| --:| -------------:|
|  1 |             1 |
|  2 |             2 |
|  3 |             6 |
|  4 |            24 |
|  5 |           120 |
|  6 |           720 |
|  7 |          5040 |
|  8 |         40320 |
|  9 |        362880 |
| 10 |       3628800 |
| 11 |      39916800 |
| 12 |     479001600 |
| 13 |    6227020800 |
| 14 |   87178291200 |
| 15 | 1307674368000 |
