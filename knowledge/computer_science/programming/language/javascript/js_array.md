---
aliases: [Array en JavaScript]
author: Mindusting
corrected: false
headerFile: false
rating:
tags: [JavaScript, Programming]
---

# ARRAYS EN JS

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Documentar como crear un array.
> > - [ ] Documentar las funciones del array.
> > - [ ] En el apartado **Indice del array**:
> >     - [ ] Explicar como se puede leer.
> >     - [ ] Explicar como se puede escribir.
> >     - [ ] Explicar como se puede sobrescribir.
> >     - [ ] Explicar los índices fuera de los límites.
> >         - [ ] Explicar que los índices negativos se interpretan como una nueva propiedad.
> >         - [ ] Explicar que los índices positibos reservan espacios extra.
> > - [ ] En el apartado **extremos del array**:
> >     - [ ] Explicar que es más eficiente usar `push` y `pop` en vez de `unshift` y `shift`.

> [!external-link]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/js/js_arrays.asp) #WWW/W3Schools

> [!faq]- FAQ
> - [¿Qué son los arrays in programación?](../../fundamentals/temp-dump/data_structures/pc_ds_array.md)

Un **array** en **JS** se guarda dentro de una [variable](js_variables.md), este se expresa con unos *corchetes* (`[]`), entre estos pondremos los diferentes elementos que queramos que tenga en el momento de la declaración.

> [!abstract] SINTAXIS
> let ***\[arr_name]*** = \[***\[element]***,...];

```js
// Declaramos el array con valores establecidos.
let arr = [3, 2, 5];

// Imprimimos el array en consola.
console.log(arr);
// SALIDA:
// [3, 2, 5]
```

Si queremos signar valores o acceder a ellos, podemos hacerlo mediante el nombre del **array** y unos *corchetes* (`[]`):

```js
// Declaramos el array bacio.
let arr = [];

// Asignamos valores a las posiciones.
arr[0] = 3;
arr[1] = 2;
arr[2] = 5;

// Imprimimos el array en consola.
console.log(arr);
// SALIDA:
// [3, 2, 5]
```

## ÍNDICE DEL ARRAY

## LONGITUD DEL ARRAY

Para obtener la longitud del **array** (*el número de elemntos que contiene*), se hace mediante la propiedad `length`; este contiene un número entero indicando el número de leementos.

```js
let frutis = ["Manzana", "Naranja", "Lomón", "Pera"];

console.log(fruits.length);
// SALIDA:
// 4
```

Esto se puede usar por ejemplo en conjunto a los [bucles `for`](js_flow_control.md#BUCLE%20FOR):

```js
let frutis = ["Manzana", "Naranja", "Lomón", "Pera"];

for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}
// SALIDA:
// Manzana
// Naranja
// Lomón
// Pera
```

---

En vez de leer la longitud del **array**, también podemos establecerla; esto permite que descartemos una porción o que añadamos una serie de espacios vacíos que podremos usar después, dependiendo de lo que estemos haciendo, esta característica nos puede venir bien.

```js
let frutis = ["Manzana", "Naranja", "Lomón", "Pera"];

console.log(frutis);
// SALIDA:
// [ 'Manzana', 'Naranja', 'Lomón', 'Pera' ]

// Se establece el número de elementos a 2.
fruits.length = 2;
console.log(frutis);
// SALIDA:
// [ 'Manzana', 'Naranja' ]

// Se establece el número de elementos a 4.
fruits.length = 4;
console.log(frutis);
// SALIDA:
// [ 'Manzana', 'Naranja', <2 empty items> ]
```

Si especificamos un tamaño menor al que tiene el **array**, el número de elemntos sobrantes se descartarán al final de este.

Si especificamos un tamaño mayor al que tiene el **array**, se añadirán **elementos vacíos** (*los elementos vacíos son `undefined`*) al final de este.

## EXTREMOS DEL ARRAY

```txt
unsift -> [arr] <- push
  sift <- [arr] -> pop
```

## COPIA DE UN ARRAY

> [!internal-link] REFERENCIAS INTERNAS
> Para entender bien esta parte de la documentación recomiendo tener a mano la [documentación a cerca del *deepcopy*](../../fundamentals/temp-dump/pc_deepcopy.md), ya que es este apartado se explica en detalle las diferencias entre los distintos tipos de copia.

### COPIA SIMPLE

```js
[...arr];
arr.slice();
Array.from(arr);
[].concat(arr);
```

### COPIA PROFUNDA

```js
structuredClone(arr);
JSON.parse(JSON.stringify(arr));
```
