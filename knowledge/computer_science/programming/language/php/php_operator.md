---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - PHP
title: Operadores en PHP
---

# OPERADORES EN PHP

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

## CONPARACIÓN

| OPERADOR | DESCRIPCIÓN       |
|:--------:|:----------------- |
|    ==    | igual qué         |
|    !=    | diferente qué     |
|    >=    | mayor o igual qué |
|    >     | mayor qué         |
|    <=    | menor o igual qué |
|    <     | menor qué         |

## OPERADOR ESPACIAL

El operador espacial obtiene su nombre debido a su forma que se asemeja a una nave alienígena (`<=>`); se usa para poder ordenar valores, ya que al comparar dos valores nos podrá ofrecer res valores distintos (`-1`, `0`, `1`) indicando como están ordenados.

- `-1`:
    Indica que los valores está ordenados de forma ascendente.
- `0`:
    Indica que los valores son iguales.
- `1`:
    Indica que los valores están ordenados de forma descendente.

Este operador se suele usar para ordenar conjuntos

```php
$items = [3, 2, 5, 7, 8, 4, 6, 1, 9, 0];

// Ordena de forma ascendente.
usort($items, function($x, $y) {
    return $x <=> $y;
});

foreach ($items as $item) {
    echo $item." "
}
// SALIDA:
// 0 1 2 3 4 5 6 7 8 9
```

```php
$items = [3, 2, 5, 7, 8, 4, 6, 1, 9, 0];

// Ordena de forma descendente.
usort($items, function($x, $y) {
    return -($x <=> $y);
});

foreach ($items as $item) {
    echo $item." "
}
// SALIDA:
// 9 8 7 6 5 4 3 2 1 0
```

> [!note] NOTA
> No tiene por qué ser una lista de núemros, puede ser de textos; en ese caso, se ordenaría de forma alfabética.
