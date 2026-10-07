---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - JavaScript
  - Web
title: Eventos en JS
---

# EVENTS EN JS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar el evento `onclick`.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/js/js_events.asp) #WWW/W3Schools
> - [geeksforgeeks](https://www.geeksforgeeks.org/javascript-events/) #WWW/geeksforgeeks

## TIPOS DE EVENTOS

### EVENTOS DE INTERACCIÓN CON EL CURSOR

- `click`
- `dblclick`
- `mousedown`
- `mouseup`
- `mousemove`
- `mouseenter`
- `mouseleave`
- `mouseover`
- `mouseout`
- `contextmenu`

### EVENTOS DE TECLADO

- `keydown`
- `keypress`: (*obsoleto*)
- `keyup`

### EVENTOS DE ENFOQUE

- `focus`
- `blur`

### EVENTOS DE FORMULARIO

- `submit`
- `reset`
- `input`
- `change`
- `focusin`
- `focusout`

### EVENTOS DE CAMBIO DE ESTADO Y VISIBILIDAD

- `load`
- `unload`
- `resize`
- `scroll`
- `visibilitychange`
- `beforeunload`

### EVENTOS DE PANTALLA TÁCTIL

- `touchstart`
- `touchmove`
- `touchend`
- `touchcancel`

### EVENTOS DE PUNTERO

- `pointerdown`
- `pointerup`
- `pointermove`
- `pointerover`
- `pointerout`
- `pointerenter`
- `pointerleave`
- `pointercancel`

### EVENTOS DE UI

- `scroll`
- `resize`

### EVENTOS DE MEDIOS

- `play`
- `pause`
- `ended`
- `volumechange`
- `timeupdate`

### EVENTOS DE ANIMACIÓN Y TRANSICIÓN

- `animatinostart`
- `animationend`
- `animationiteration`
- `transitionstart`
- `transitionend`
- `transitioniteration`

## AÑADIR EVENTOS

> [!abstract] SINTAXIS
> ***\[htmlElement\]***.addEventListener(***\[eventType\]***, ***\[function\]***);

---
---
---
---
---

> [!abstract] SINTAXIS
> <***\[tag\] \[event\_type\]***="***\[function\]***"></***\[tag\]***>
%%
> ***\[element\]***.addEventListener(***\[type\]***, ***\[function\]***)
%%

- `onclick`: Ejecuta cuando el elemento es clicado.
- `ondblclick`: Ejecuta cuando el elemento recibe un doble click.
- `onmousedown`: Ejecuta cuando el click se pulsa sobre el elemento.
- `onmouseup`: Ejecuta cuando el click se deja de pulsar sobre el elemento.
- `onmouseover`: Ejecuta cuando el cursor se encuentra encima del elemento.
- `onmouseout`: Ejecuta cuando el cursor deja de tocar el elemento.
- `onmousemove`: Ejecuta cuando el cursor se mueve.
- `onchange`: Ejecuta cuando el *input* de un elemento cambia.
- `onload`: Ejecuta cuando la página termina de cargarse.
- `onsubmit`: Ejecuta cuando un formulario es enviado.
- `onfocus`: Ejecuta cuando el elemento recibe el foco.
- `onblur`: Ejecuta cuando el elemento pierde el foco.



%%
## ONCLICK

> [!help]- REFERENCIAS WEB
> - [geeksforgeeks](https://www.geeksforgeeks.org/html-dom-onclick-event) #WWW/geeksforgeeks

> [!abstract] SINTAXIS
> <***\[tag\]*** onclick="***\[function\]***"></***\[tag\]***>
> 
> ---
> 
> ***\[element\]***.addEventListener("click", ***\[function\]***);
%%
