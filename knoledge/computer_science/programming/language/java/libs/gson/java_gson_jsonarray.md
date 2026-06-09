---
aliases: [JsonArray en GSON]
author: Mindusting
corrected: true
headerFile: false
rating: 
tags: [Java, JSON, Programming]
---

# JSONARRAY EN GSON

> [!faq]- FAQ
> - [¿Qué es la **copia profunda** (*deepcopy*) en programación?](../../../../fundamentals/temp-dump/pc_deepcopy.md)

> [!important] IMPORTANTE
> Cabe resaltar que esta [clase](../../theory/oop.md) (`JsonArray`) hereda de la [clase](../../theory/oop.md) [`JsonElement`](java_gson_jsonelement.md), por lo que además de los [métodos](../../java_method.md) que se documentan en este apartado, también contienen los de [`JsonElement`](java_gson_jsonelement.md).

Los [*arrays*](../../theory/arrays.md) en [**JSON**](../../../../data_format/json.md) son más flexibles que los [*arrays*](../../theory/arrays.md) en **Java**, ya que estos pueden contener valores de **distintos tipos**, por lo que al tratar con la información contenida dentro de estos, tendremos que ir especificando de qué forma interpretar la información guardada en su interior.

---

Aquí tienes un resumen de los [métodos](../../java_method.md) que contiene esta [**clase**](../../theory/oop.md):

- `add`: añade el nuevo *elemento*.
- `size`: devuelve el número de *elementos* en el `JsonArray`.
- `get`: devuelve un [`JsonElement`](java_gson_jsonelement.md) por *índice*.
- `addAll`: introduce todos los elementos de otro `JsonArray` en el actual.
- `isEmpty`: devuelve un valor [booleano](../../data_types/java_boolean.md) indicando si está vacío o no el `JsonArray`.
- `deepCopy`: hace una [copia profunda](../../../../fundamentals/temp-dump/pc_deepcopy.md) del objeto.
- `contains`: devuelve un valor [booleano](../../data_types/java_boolean.md) indicando si contiene el valor indicado.

## DECLARACIÓN DE UN JSONARRAY

Para declarar un `JsonArray` se hace siguiendo la siguiente sintaxis:

> [!abstract] SINTAXIS
> JsonArray ***\[name\]*** = new JsonArray();

---

En este ejemplo podemos ver cómo se crea un `JsonArray` y se imprime:

```java
JsonArray arr = new JsonArray();

System.out.println(arr);
// SALIDA:
// []
```

## INSERCIÓN DE ELEMENTOS

En el `JsonArray` no se puede meter cualquier tipo de elemento como puede ocurrir en los [*array*](../../theory/arrays.md) de **Java**, sino que solo se pueden guardar unos tipos en concreto:

- `Boolean`
- `Character`
- [`JsonElement`](java_gson_jsonelement.md)
- `Number`
- `String`
^valid-values-on-gsonarray

Por lo que hay que tener esto en cuenta a la hora de introducir información dentro de estos.

### INSERTAR UN ELEMENTO

Para añadir elementos individuales en el `JsonArray` se usa el [método](../../java_method.md) `add`, éste recibe un [valor válido](#^valid-values-on-gsonarray) y lo introduce al final del `JsonArray`.

> [!abstract] SINTAXIS
> ***\[jsonArray\]***.add(***\[element\]***);

---

En el siguiente ejemplo podemos ver como se guarda una lista de frutas:

```java
JsonArray fruits = new JsonArray();

fruits.add("Tomate");
fruits.add("Naranja");
fruits.add("Plátano");
fruits.add("Pera");
fruits.add("Arándano");
fruits.add("Berenjena");

System.out.println(fruits);
// SALIDA:
// ["Tomate","Naranja","Plátano","Pera","Arándano","Berenjena"]
```

---

En el siguiente ejemplo podemos ver como se guarda una lista de usuarios:

```java
JsonArray users = new JsonArray();

JsonObject user1 = new JsonObject();
user1.addProperty("id", 1);
user1.addProperty("name", "Adelio");
users.add(user1);

JsonObject user2 = new JsonObject();
user2.addProperty("id", 2);
user2.addProperty("name", "Adelia");
users.add(user2);

System.out.println(users);
// SALIDA:
// [{"id":1,"name":"Adelio"},{"id":2,"name":"Adelia"}]
```

### INSERTAR MÚLTIPLES ELEMENTOS

Para añadir múltiples elementos en el `JsonArray` se usa el [método](../../java_method.md) `addAll`, este solo puede recibir como parámetro un `JsonArray`; el efecto será como extender el primer `JsonArray` añadiendo le todos los elementos del segundo al final.

> [!abstract] SINTAXIS
> ***\[jsonArray1\]***.addAll(***\[jsonArray2\]***);

---

En este ejemplo podemos ver como tenemos dos `JsonArray` de frutas y vegetales; luego creamos un nuevo `JsonArray` vacío al que añadiremos todos los elementos de ambos `JsonArray`:

```java
JsonArray fruits = new JsonArray();

fruits.add("Tomate");
fruits.add("Naranja");

JsonArray vegetables = new JsonArray();

vegetables.add("Lechuga");
vegetables.add("Remolacha");

JsonArray food = new JsonArray();
food.addAll(fruits);
food.addAll(vegetables);

System.out.println(food);
// SALIDA:
// ["Tomate","Naranja","Lechuga","Remolacha"]
```

## OBTENER ELEMENTOS

Para obtener elementos de un `JsonArray` se usa el [método](../../java_method.md) `get`, éste recibe el índice del elemento como parámetro y devuelve un [`JsonElement`](java_gson_jsonelement.md) del cual se puede obtener el valor estándar de **Java**.

> [!abstract] SINTAXIS
> ***\[jsonArray\]***.get(***\[index\]***);

---

Como se puede ver en el siguiente ejemplo, podemos obtener los elementos mediante el índice, pero como se ha indicado antes, lo que devuelve este [método](../../java_method.md) es un [`JsonElement`](java_gson_jsonelement.md), por lo que se puede guardar el elemento como tal, o podemos obtener de forma directa el valor que contiene:

```java
JsonArray fruits = new JsonArray();

fruits.add("Tomate");
fruits.add("Naranja");
fruits.add("Plátano");
fruits.add("Pera");
fruits.add("Arándano");
fruits.add("Berenjena");

// Se puede guardar el `JsonElement` por separado:
JsonElement element = fruits.get(4);
String elementValue = element.getAsString();
System.out.println(elementValue);
// SALIDA:
// Arándano

// O se puede obtener el valor del String directamente.
String value = fruits.get(4).getAsString();
System.out.println(value);
// SALIDA:
// Arándano
```

## ELIMINAR ELEMENTOS

Para eliminar elementos de un `JsonArray` se pueden usar dos *métodos*, mediante el [índice](#ELIMINAR%20POR%20ÍNDICE) y eliminar por [elemento](#ELIMINAR%20POR%20ELEMENTO); ambos [métodos](../../java_method.md) se llaman de la misma forma (`remove`), aunque actúan de forma distinta.

### ELIMINAR POR ÍNDICE

Para eliminar un elemento por *índice* se usa el [método](../../java_method.md) `remove`, éste recibe un **número entero** como argumento, devolviendo el elemento eliminado; si el *índice* del elemento no existe se lanzará la excepción [`IndexOutOfBoundsException`](../../packages/java/lang/java_lang_indexoutofboundsexception.md).

> [!abstract] SINTAXIS
> ***\[jsonArray\]***.remove(***\[index\]***);

---

En el siguiente ejemplo podemos ver como creamos un `JsonArray` de frutas, para luego eliminar el elemento con *índice* `1` (*siendo este `Naranja`*):

```java
JsonArray fruits = new JsonArray();

fruits.add("Tomate");
fruits.add("Naranja");
fruits.add("Plátano");
fruits.add("Pera");
fruits.add("Arándano");
fruits.add("Berenjena");

// Eliminamos el elemento de índice 1 del JsonArray y lo guardamos.
JsonElement fruit = fruits.remove(1);

// El JsonArray ya no contiene "Naranja".
System.out.println(fruits);
// SALIDA:
// ["Tomate","Plátano","Pera","Arándano","Berenjena"]

System.out.println(fruits.getAsString());
// SALIDA:
// Naranja
```

### ELIMINAR POR ELEMENTO

Para eliminar por **elemento** en `JsonArray` se usa el [método](../../java_method.md) `remove`, recibe un `JsonElement` como argumento y devuelve un valor [*booleano*](../../data_types/java_boolean.md) indicando si lo ha encontrado y eliminado; debes tener en cuenta que este [método](../../java_method.md) elimina el primer el elemento que coincida, por lo que si hay múltiples elementos iguales solo eliminará el primero.

> [!abstract] SINTAXIS
> ***\[jsonArray\]***.remove(***\[jsonElement\]***);

---

En este ejemplo podemos ver como tenemos un `JsonArray` con dos *tomates* y una *naranja*, se obtiene el primer elemento (*un tomate*) y se trata de eliminar tres veces; en el primer intento se elimina y por eso obtenemos el valor `true`, en el segundo pasa lo mismo y en el tercero, debido a que ya no quedan más *tomates* obtenemos el valor `false`:

```java
JsonArray fruits = new JsonArray();

fruits.add("Tomate");
fruits.add("Naranja");
fruits.add("Tomate");

JsonElement element = fruits.get(0);

boolean removed = false;

// Se elimina el primer elemento "Tomate".
removed = fruits.remove(element);
System.out.println(removed);
System.out.println(fruits);
// SALIDA:
// true
// ["Naranja", "Tomate"]

// Se elimina el segundo elemento "Tomate".
removed = fruits.remove(element);
System.out.println(removed);
System.out.println(fruits);
// SALIDA:
// true
// ["Naranja"]

// No se elimina ningún elemento.
removed = fruits.remove(element);
System.out.println(removed);
System.out.println(fruits);
// SALIDA:
// false
// ["Naranja"]
```

## CONTIENE ELEMENTOS

Para comprobar si un elemento se encuentra dentro del `JsonArray` se usa el [método](../../java_method.md) `contains`, este recibe un `JsonElement` como argumento y devuelve un valor [booleano](../../data_types/java_boolean.md) indicando si ha encontrado por lo menos una vez el elemento.

> [!abstract] SINTAXIS
> ***\[jsonArray\]***.contains(***\[jsonElement\]***);

---

En este ejemplo podemos ver dos grupos de nombres y queremos comprobar si el primer nombre del segundo grupo se encuentra en el primero, por lo que primero obtenemos el `JsonElement` del segundo grupo y luego lo comprobamos si existe o no dentro del primero:

```java
JsonArray group1 = new JsonArray();
JsonArray group2 = new JsonArray();

group1.add("Ana");
group1.add("Bob");

group2.add("Bob");
group2.add("Shara");

JsonElement nameElement = group2.get(0);

boolean isIn = group1.contains(nameElement);

System.out.println(isIn);
// SALIDA:
// true
```

## COPIA PROFUNDA

Para poder hacer una [**copia profunda**](../../../../fundamentals/temp-dump/pc_deepcopy.md) de un `JsonArray` se usa el [método](../../java_method.md) `deepCopy`; este no recibe ningún argumento y devuelve otro [objeto](../../theory/oop.md#OBJETOS) de tipo `JsonArray`.

> [!abstract] SINTAXIS
> ***\[jsonArray\]***.deepCopy()

---

A continuación podemos ver un ejemplo de uso del `deepCopy`:

```java
// Se crea el primer grupo con los usuarios.
JsonArray group1 = new JsonArray();

JsonObject user1 = new JsonObject();
user1.addProperty("id", 1);
user1.addProperty("name", "Adelio");
group1.add(user1);

JsonObject user2 = new JsonObject();
user2.addProperty("id", 2);
user2.addProperty("name", "Adelia");
group1.add(user2);

// Se crea una copia profunda con el segundo grupo.
JsonArray group2 = group1.deepCopy();

// Se modifica uno de los usuarios del segundo
// grupo sin afectar al primero.
JsonObject user3 = group2.get(1).getAsJsonObject();
user3.addProperty("id", 3);
user3.addProperty("name", "Antonia");

// Se puede ver como el primer grupo queda intacto
// mientras que el segundo ha sido modificado.
System.out.println(group1);
System.out.println(group2);
// SALIDA:
// [{"id":1,"name":"Adelio"},{"id":2,"name":"Adelia"}]
// [{"id":1,"name":"Adelio"},{"id":3,"name":"Antonia"}]
```

## TAMAÑO Y VACÍO

Para obtener el número de elementos (*el tamaño*) en el `JsonArray` se usa el [método](../../java_method.md) `size`; este no recibe ningún argumento y devuelve un valor de tipo [`int`](../../data_types/java_integer.md#INT).

> [!abstract] SINTAXIS
> ***\[jsonArray\]***.size()

---

En este ejemplo podemos ver como creamos un `JsonArray` al que introducimos nombres de distintas frutas y luego imprimimos el número de elementos para saber cuántas frutas hay guardadas en total:

```java
JsonArray fruits = new JsonArray();

fruits.add("Tomate");
fruits.add("Naranja");
fruits.add("Plátano");
fruits.add("Pera");
fruits.add("Arándano");
fruits.add("Berenjena");

// Imprimimos el número de frutas:
System.out.println(fruits.size());
// SALIDA:
// 6
```

---

Para saber si un elemento está vacío o no se usa el [método](../../java_method.md) `isEmpty`; este no recibe ningún argumento y devuelve un valor [booleano](../../data_types/java_boolean.md) indicando si está vacío.

> [!abstract] SINTAXIS
> ***\[jsonArray\]***.isEmpty()

---

En este ejemplo podemos ver cómo es que obtenemos comprobar si el `JsonArray` está vacío:

```java
JsonArray fruits = new JsonArray();

// Comprobamos si está vacía.
System.out.println(fruits.isEmpty());
// SALIDA:
// true

// Es el equivalente a hacer lo siguiente:
System.out.println(fruits.size() == 0);
// SALIDA:
// true
```
