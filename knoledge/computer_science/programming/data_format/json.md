---
aliases:
  - JSON
author: Mindusting
corrected: false
headerFile: true
tags:
  - Programming
  - JSON
  - DataFormat
---

# JSON

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

**JSON** es un formato de datos basado en texto; no permite estructurar información con estructuras complejas de forma sencilla mediente texto, por lo que podremos manipularlo a mano con ayuda de cualquier editor de texto; es muy usado mundialmente debido a su sencillez y compacta sintaxis.

---

Veamos un ejemplo sencillo de los datos de una persona almacenadas en formato **JSON**:
```json
{
    "id": 1,
    "name": "Adelio",
    "male": true,
    "birthDate": "2000-01-01"
}
```
^basic-example

(Figura 1)

## TIPOS PRIMITIVOS

Los tipos primitivos en **JSON** son los tipos de datos más pequeños que podemos encontrar, existen varios tipos, teniendo cada uno sus peculliaridades.

### NULO

El valor **nulo** indica que ahí en donde se encuentra podría haber un dato, pero en ese momento se desconoce, es decir se usa como "*bacio*", para indicar la inexistencia de cierta información.

Para escribir un valor **nulo** se usa la palabra literal `null` en minúsculas.

---

En este caso podemos ver un [*objeto*](#OBJETO) que contien dos *claves*: `firstName` (*nombre*), teniendo este el valor "*Adelio*" y `lastName` (*apellido*) teniendo este el valor *nulo*; indicandonos así que se conce el nombre de esta parsona pero no su apellido.

```json
{
    "firstName": "Adelio",
    "lastName": null
}
```

Podrías pensar que un valor *nulo* no indica nada, por lo que se podría incluso descartar la *clave* `lastName`, pero esto no es así, ya que la existencia de esta *clave* indica que existe la intención de guardar dicha información, y el *nulo* nos indica que no se ha podido darle un valor, por el motivo que sea; por tanto ese *nulo* de cierta forma sí nos está dando algo de información, la existencia de un dato que desconocemos.

### BOOLEANO

Los [**booleanos**](../../../mathematic/math_boolean.md) son aquellos valores que solo pueden estar en dos estados, *verdadero* (`true`) o *false* (`false`); pudiendo ser usados para lo que nosotros queramos, por ejemplo, en la [(Figura 1)](#^basic-example) podemos ver como se ha usado para identificar si el usuario representado por esos datos es un hombre o una mujer (*siendo en este caso un hombre*).

Para usar este tipo de datos se usan las palabas clave; `true` y `false`.

### NUMÉRICO

Los valores numéricos son aquellos que representan (*como su nombre indica*) un número en [base 10](../../../mathematic/number_system/math_ns_dec.md), este puede ser **entero** o **decimal** (*separando la parte fraccionaria con un punto (`.`)*)

### TEXTO

## ESTRUCTURAS DE DATOS

El formato **JSON**

### LISTA

### OBJETO

## FECHAS

- Unix date format
- Fecha Juliana
- ISO 8601

## ARCHIVOS JSON

`.json`

%%

==DOCUMENTACIÓN ANTIGUA==

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Rehacer toda la documentación desde cero para trocearlo en múltiples archivos, explicando el uso de este formato, objetos, array, valores, etc.
> > - [ ] Explicar que JSON es JavaScript Object Notation.
> > - [ ] Revisar todo el contenido para valorar que se puede mejorar.
> > - [ ] Comprobar faltas de ortografía.

Los archivos JSON están pensados para guardar información de forma sencilla, vienen por parte de [JavaScript](../language/javascript/js.md), pero se puede usar en otros lenguajes con ayuda de librerías.

El objetivo de estos es guardar información de forma permanente en un archivo externo para poder acceder a la información en el futuro.

## ARCHIVOS

Los archivos de JSON tienen la extensión `.json` y el formato interno que usa es texto plano.

## ESTRUCTURA DE LA INFORMACIÓN

La información dentro de los archivos JSON se escribe al igual que en [JavaScript](../language/javascript/js.md) se escriben los [array](../language/javascript/js_array.md) y los [objetos](../language/javascript/js_object.md), este último tiene un matiz y es que no se pueden guardar funciones, únicamente información.

Por lo general los archivos JSON suelen empezar con un [objetos](../language/javascript/js_object.md), pero también puede comenzar con [array](../language/javascript/js_array.md).

En el próximo ejemplo podemos ver como el primer nivel del archivo tiene un [objetos](../language/javascript/js_object.md), este contiene dos *llaves* (`key`), con cada uno su respectivo *valor* (`value`):

```json
{
    "PI": 3.14159236535,
    "E" : 2.71828182845
}
```

En el próximo ejemplo, a diferencia del anterior, este comienza con un [array](../language/javascript/js_array.md), conteniendo este dos elementos.

```json
[
    3.14159236535,
    2.71828182845
]
```

>[!note]
>Cada archivo JSON solo puede tener un [array](../language/javascript/js_array.md) u [objeto](../language/javascript/js_object.md) en el primer nivel, de lo contrario nos dará un error.

---

La información puede tener forma de *matriuska*, de forma que un [array](../language/javascript/js_array.md) u [objeto](../language/javascript/js_object.md) se puede encontrar dentro de otro, en el próximo ejemplo se muestra como hacerlo.

```json
{
    "users": [
        {"name": "Mindusting", "age": 18, "height": 1.75},
        {"name": "Adelio", "age": 32, "height": 1.8}
    ],
    "products": [
        {"name": "Apple", "price": 3.5},
        {"name": "Banana", "price": 5}
    ]
}
```

Otra forma de guardar la misma información que en el ejemplo anterior pero con la misma estructura es la siguiente.

```json
{
    "users": {
        "name": ["Mindusting", "Adelio"],
        "age": [18, 32],
        "height": [1.75, 1.8]
    },
    "products": {
        "name": ["Apple", "Banana"],
        "price": [3.5, 5]
    }
}
```

---

Los ejemplos que has visto hasta ahora están hechos de una forma visualmente agradable, pero el contenido no tiene por qué guardarse de esa forma, por lo genera, para ahorrar espacio, se suele guardar de una forma más compacta, escribiendo lo todo en una sola línea:

```json
{"users":{"name":["Mindusting","Adelio"],"age":[18,32],"height":[1.75,1.8]},"products":{"name":["Apple","Banana"],"price":[3.5,5]}}
```

En cualquiera de los dos casos funciona de la misma forma, por lo que cuando el archivo va a guardar muchísimos datos y no vamos a acceder a la información de forma directa al archivo, no tenemos ningún interés en guardarlo de forma visualmente agradable ya que ocupa más espacio, en cambio si es un archivo por ejemplo de configuración, que es pequeño y queremos que sea fácil de manejar abriendo el archivo de forma directa, podemos usar el formato agradable a la vista, esto último os lo digo por qué cuando vamos a guardar datos en un archivo JSON desde otro archivo de código, por lo general, existe la opción de elegir en qué forma queremos guardar el archivo. si de forma visual o compacta.

%%
