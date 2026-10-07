---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - Java
  - JSON
title: JsonObject en GSON
---

# JSONOBJECT EN GSON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!faq]- FAQ
> - [¿Qué es la **copia profunda** (*deepcopy*) en programación?](../../../../fundamentals/temp-dump/pc_deepcopy.md)

- `add`: añade el par de clave y [`JsonElement`](java_gson_jsonelement.md).
- `addProperty`: añade el par de clave y valor.
- `deepCopy`: devuelve una copia profunda del objeto.
- `get`: devuelve el `JsonElement` correspondiente a la clave indicada.
- `has`: devuelve el valor [booleano](../../data_types/java_boolean.md) indicando si contiene la clave indicada.
- `isEmpty`: devuelve el valor [booleano](../../data_types/java_boolean.md) indicando si está vacío.
- `keySet`: devuelve un [`Set`](../../packages/java/util/set.md) con las claves.
- `remove`: elimina el par clave, valor en base a la clave indicada, devolviendo el [`JsonElement`](java_gson_jsonelement.md) perteneciente a la clave indiada.
- `size`: devuelve el número de pares de clave, valor.

## DECLARACIÓN DE UN JSONARRAY

Para declarar un `JsonObject` se hace siguiendo la siguiente sintaxis:

> [!abstract] SINTAXIS
> JsonObject ***\[name\]*** = new JsonObject();

---

En este ejemplo podemos ver cómo se crea un `JsonObject` y se imprime:

```java
JsonObject obj = new JsonObject();

System.out.println(obj);
// SALIDA:
// {}
```

## INSERCIÓN DE PARES

En el `JsonObject` no se puede meter cualquier tipo de elemento como puede ocurrir en los [*map*](../../packages/java/util/map.md) de **Java**, sino que solo se puede guardar unos tipos en concreto:

- `Boolean`
- `Character`
- [`JsonElement`](java_gson_jsonelement.md)
- `Number`
- `String`
^valid-values-on-gsonarray

Por lo que hay que tener esto en cuenta a la hora de introducir información dentro de estos.

---

A la hora de introducir los pares de *clave*, *valor* se diferencian entre dos tipos, cuando queremos valor *"genérico"* y cuando queremos insertar un [`JsonElement`](java_gson_jsonelement.md); para esto se usan dos [métods](../../java_method.md): [`addProperty`](#INSERCIÓN%20DE%20VALOR) y [`add`](#INSERCIÓN%20DE%20JSONELEMENT).

### INSERCIÓN DE VALOR

Para insertar un valor

> [!abstract] SINTAXIS  
> ***\[jsonObject\]***.addProperty(***\[key\]***, ***\[value\]***);

### INSERCIÓN DE JSONELEMENT

> [!abstract] SINTAXIS  
> ***\[jsonObject\]***.add(***\[key\]***, ***\[jsonElement\]***);
