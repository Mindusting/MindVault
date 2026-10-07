---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - HTML
  - Web
title: Etiqueta input en HTML5
---

# INPUT EN HTML

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > 
> > - [ ] Comprobar que el [`radio`](#RADIO) está completo.

> [!abstract] SINTAXIS
> \<input type="[***\[type\]***](#^input-types)"\>

```html
<input type="button" value="Click me">
```

La etiqueta `input` puede ser de varios tipos:

- [`text`](#TEXT)
- [`password`](#PASSWORD)
- [`button`](#BUTTON)
- [`checkbox`](#CHECKBOX)
- [`radio`](#RADIO)
- [`range`](#RANGE)
- [`date`](#DATE)
- [`week`](#WEEK)

^input-types

## TEXT

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

## PASSWORD

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

## BUTTON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

## CHECKBOX

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

Las propiedades importantes de este tipo de input son:

- `name`: permite dar un nombre a este tipo de input, creando un "grupo" con todos los input con el mismo nombre, de forma que solo se obtendrá el valor del último input seleccionado del "grupo".
- `value`: permite sustituir el valor que obtiene la propiedad al ser seleccionada, estableciendo el valor indicado sustituyendo al `on` por defecto.
- `checked`: permite indicar que opciones queremos establecer como seleccionadas al inicio.
- `disabled`: permite desactivar los inputs que la contengan.

## RADIO

Las propiedades importantes de este tipo de input son:

- `name`: permite dar un nombre a este tipo de input, creando un "grupo" con todos los input con el mismo nombre, de forma que solo se podrá seleccionar uno de ellos dentro de este "grupo".
- `value`: indica el valor que tendrá la opción que elija el usuario.
- `checked`: permite indicar que opción queremos establecer como seleccionada al inicio.
- `disabled`: permite desactivar los inputs que la contengan.

```html
<input
    id="foodRadio1"
    type="radio"
    name="favoriteFoodType"
    value="fruits"
    checked>
<label for="foodRadio1">Frutas</lable>
<br>

<input
    id="foodRadio2"
    type="radio"
    name="favoriteFoodType"
    value="vegetables">
<label for="foodRadio2">Vegetales</lable>
<br>

<input
    id="foodRadio3"
    type="radio"
    name="favoriteFoodType"
    value="meets">
<label for="foodRadio3">Carnes</lable>
<br>

<input
    id="foodRadio4"
    type="radio"
    name="favoriteFoodType"
    value="dairy"
    disabled>
<label for="foodRadio4">Lacteos</lable>
<br>
```

## RANGE

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
