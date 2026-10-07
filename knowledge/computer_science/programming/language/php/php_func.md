---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - PHP
title: Funciones en PHP
---

# FUNCIONES EN PHP

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!abstract] SINTAXIS
> function ***\[name\]***([***\[parameters\]***](#PARÁMETROS)) {***\[code\]***}

```php
function pitagoras($x, $y) {
    return sqrt(($x * $x) + ($y * $y));
}

echo(pitagoras(3, 4));
```

## PARÁMETROS

Para especificar parámetros en una función se hace de la misma forma que cualquier [variable](php_variable.md); en caso de querer definir multiples parámetros, tendremos que separarlos con comas.

```php
function greet($name) {
    echo "Hola ".$name."!";
}
```

### VALORES POR DEFECTO EN PARÁMETROS

Los valores por defecto se definen poniendo un igual (`=`) seguido del valor en frente del parámetro al que queremos darle el valor por defecto.

```php
function increse($number, $increseNumber = 1) {
    return $number + $increseNumber
}

echo increse(3);
// SALIDA:
// 4

echo increse(3, 5);
// SALIDA:
// 8
```

### ARGUMENTOS CON NÚMERO DE VALORES VARIABLE

```php
function pitagoras(...$numbers) {
    $sumatory = 0;

    foreach ($numbers as $number) {
        $sumatory += $number * $number;
    }

    return sqrt($sumatory);
}

echo(pitagoras(3, 4, 5));
```

## FUNCIONES VARIABLES

En PHP para acceder a una función no hace falta que escribamos su nombre talcual, podemos hacerlo mediante un string que contenga el nombre de la función:

```php
function add($x, $y) {
    return $x + $y;
}

function sub($x, $y) {
    return $x - $y;
}

$operators = array("add", "sub");

echo $operators[1](3, 2);
// SALIDA:
// 1
```

## FUNCIONES ANÓNIMAS

```php
$greet = function ($name) {
    echo "Hola ".$name."!";
}

$greet("Adelio");
```
