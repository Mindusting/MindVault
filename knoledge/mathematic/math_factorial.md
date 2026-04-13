---
author: Mindusting
corrected: false
tags:
  - Math
title: Factorial
---

# FACTORIAL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Para obtener un número aproximado al resultado del factorial, podemos seguir la siguiente fórmula:

$$
n! \approx \sqrt{2 \pi n} (n / e )^n
$$

```python
def factorial(n) -> float:
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def factorial_approx(n) -> float:
    return math.sqrt(2 * math.pi * n) * math.pow((n / math.e), n)
```
