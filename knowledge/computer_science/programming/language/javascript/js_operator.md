---
aliases:
  - Operadores en JavaScript
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - JavaScript
  - Web
---

# OPERADORES EN JAVASCRIPT

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar el operador binario NOT.
> > - [ ] Explicar el operador binario AND.
> > - [ ] Explicar el operador binario OR.
> > - [ ] Explicar el operador binario NULLISH.

## OPERADORES BOOLEANOS

| OPERADOR | SIGNIFICADO                       |
|:--------:|:--------------------------------- |
|    !     | Negación ([NOT](#OPERADOR%20NOT)) |
|    &&    | Y ([AND](#OPERADOR%20AND))        |
|   \|\|   | O ([OR](#OPERADOR%20OR))          |

### OPERADOR NOT

La doble negación se puede usar como conversión de un valor a [**booleano**](js_data_types.md#BOOLEAN):

```js
let numero = 3;

console.log(!!numero);
// SALIDA:
// true
```

### OPERADOR AND

A diferencia de otros lenguajes este operador no devuelve un [**booleano**](js_data_types.md#BOOLEAN).

Devuelve el primer valor [**falsy**](js_data_types.md#FALSY) (*que se pueda interpretar como falso*) que encuentre; si no hay niguno, devuelve el último [**truthy**](js_data_types.md#TRUTHY) (*que se pueda interpretar como verdadero*).

### OPERADOR OR

A diferencia de otros lenguajes este operador no devuelve un [**booleano**](js_data_types.md#BOOLEAN).

Devuelve el primer valor [**truthy**](js_data_types.md#TRUTHY) (*que se pueda interpretar como verdadero*) que encuentre; si no hay niguno, devuelve el último [**falsy**](js_data_types.md#FALSY) (*que se pueda interpretar como falso*).

## OPERADOR NULLISH

Es un operador más moderno; se usa para buscar el primer valor no [**nullish**](js_data_types.md#NULLISH) que encuentre.

```js
const DEFAULT_NAME = "NoName";
let userName = null;

console.log(userName ?? DEFAULT_NAME);
// SALIDA:
// NoName
```
