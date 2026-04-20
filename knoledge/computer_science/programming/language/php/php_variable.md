---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - PHP
title: Variables en PHP
---

# VARIABLES EN PHP

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

Las variables en PHP se decalra haciendo uso del dolar (`$`) seguido del nombre; además son dinámicas, por lo que no hay que especificar el tipo de dato que guardará cada variable:

> [!abstract] SINTAXIS
> 
> \$***\[varName\]*** = ***\[varValue\]***;

## TIPOS DE DATOS BÁSICOS

- [boolean](#BOOLEAN)
- integer
- double
- [string](#STRING)

## BOOLEAN

Al parecer los **booleanos** en PHP se guardan como [`strings`](#STRING)?

Cuando es verdadero se guarda un [`string`](#STRING) (`"1"`) y cuando es falso se guada un [`string`](#STRING) vacío (`""`).

Si queremos establecer un valor booleano a una variable podemos hacerlo con las palabras `true` (*verdadero*) y `false` (*falso*).

## STRING

Para concatenar *strings* se utiliza el operador punto (`.`).
