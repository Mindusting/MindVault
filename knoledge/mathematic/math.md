---
author: Mindusting
corrected: false
headerFile: true
tags:
  - Math
title: Matemáticas 🧮
---

# MATEMÁTICAS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> YouTube:
> - [The Organic Chemistry Tutor](https://www.youtube.com/@TheOrganicChemistryTutor) #WWW/YT/TheOrganicChemistryTutor
> - [Nic Barker](https://youtu.be/U-ve8Yh4Ro8) #WWW/YT/NicBraker

- [Sistemas numéricos](number_system/math_ns.md)
- [Teoría de conjuntos](theory/sett/sett.md)
- [Vectors](math_vector.md)
- [Trigonometry](trigonometry/trigonometry.md)
- [Matrix](matrix/matrix.md)
- [Pitagoras](math_pitagoras.md)
- [Contar tanques](math_count_tanks.md)
- [Notación de intervalo](math_range_notation.md)
- [Logaritmo](math_log.md)
- [Factorial](math_factorial.md)
- [Raiz cuadrada](math_sqrt.md)

## NÚMEROS

- [Número Aureo](math_golden_ratio.md)

## INTERPOLATION

### FADE

Si queremos hacer transformar una interpolación lineal a una más suavizada podemos usar la siguiente fórmula:

$$
r = 6t^5-15t^4+10t^3
$$

```python
def fade(t: float) -> float:
    if t < 0:   return 0
    elif t > 1: return 1
    return 6*t**5-15*t**4+10*t**3
```

```python
def fade(t: float) -> float:
    if t < 0:   return 0
    elif t > 1: return 1
    return t*t*t*(t*(t*6-15)+10)
```

```mermaid
xychart-beta
    x-axis "x" 0.0 --> 1.0
    y-axis "y" 0.0 --> 1.0
    line [0.0, 0.0, 0.0, 0.01, 0.02, 0.04, 0.06, 0.09, 0.12, 0.16, 0.21, 0.26, 0.32, 0.38, 0.44, 0.5, 0.56, 0.62, 0.68, 0.74, 0.79, 0.84, 0.88, 0.91, 0.94, 0.96, 0.98, 0.99, 1.0, 1.0, 1.0]
```

%%

```python
def main() -> None:
    file = open("img.mermaid", "w")
    file.write("xychart-beta\n")
    file.write('    x-axis "x" 0.0 --> 1.0\n')
    file.write('    y-axis "y" 0.0 --> 1.0\n')
    points = []
    max_value = 30
    for x in range(0, max_value + 1):
        x /= max_value
        y = fade(x)
        points.append(y)
    points = list(map(
        lambda x: round(x, 2),
        points
    ))
    file.write(f"    line {points}\n")
    file.close()

def fade(t: float) -> float:
    if t < 0:   return 0
    elif t > 1: return 1
    return t*t*t*(t*(t*6-15)+10)

if "__main__" == __name__:
    main()
```

%%
