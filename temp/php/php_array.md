---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - PHP
title: Arrays en PHP
---

# ARRAYS EN PHP

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

Los arrays en PHP tienen poco o nada que ver con los arrays del resto del resto de lenguajes, ya que en PHP los arrays se comportan como una combinación entre los [vectores](../pc/data_structures/pc_ds_list.md#VECTOR) y [diccionarios](../pc/data_structures/pc_ds_dict.md), esto es por que se pueden usar indistintamente de una forma u otra.

%%

En PHP hay dos tipos de **vectores**: [*indixados*](#INDEXADO) y [*asociativos*](#ASOCIATIVO); internamente ambos son el mismo, pero se trabaja sobre ellos de forma distinta.

---

Para crear un **vector** en PHP se puede hacer de la siguiente forma:

> [!abstract] SINTAXIS
> 
> $***\[vecName\]***\[***\{index\}***\] = ***\[value\]***;

## INDEXADO

Para crear un **vector indexado** se puede hacer de dos formas, la primera es asignando los valores a pelo:

```php
$numbers[0] = 3;
$numbers[1] = 2;
```

Mientras que la segunda es mediante la función `array`:

```php
$numbers = array(3, 2);
```

---

Además si no indicamos el índice en el que queremos introducir un nuevo elemento automáticamente se añadirá al final del vector; además extenderá el vector automáticamente en caso de que no tibiera espacio.

```php
$numbers[] = 3;
$numbers[] = 2;
```

### ITERARLOS

Para iterar un vector indexado se puede hacer con un [bucle `foreach`](php_loop.md#FOREACH) de la siguiente forma:

```php
$numbers = array(3, 2, 5, 7);

foreach ($numbers as $number) {
    echo $number . "<br>";
}
```

## ASOCIATIVO

Los **vectores** a asociativos de PHP se comportan como las *tablas hash* de toda la vida, por lo que la información contenida en estos se divide en pares de *calve* y *valor*.

Para crear un **vector asociativo** se puede hacer de dos formas, la primera es asignando los valores a pelo:

```php
$user["id"]   = 1;
$user["name"] = "Adelio";
```

Mientras que la segunda es mediante la función `array`:

```php
$user = array(
    "id"   => 1;
    "name" => "Adelio";
);
```

### ITERARLOS

Para iterar un vector asociativo se puede hacer con un [bucle `foreach`](php_loop.md#FOREACH) de la siguiente forma:

```php
$user = array(
    "id" => 1,
    "name" => "Adelio",
    "birth" => "2000-01-01",
);

foreach ($user as $key => $value) {
    echo $key . ": " . $value . "<br>";
    // Aquí se imprimen la clave y el valor.
}
```

%%
