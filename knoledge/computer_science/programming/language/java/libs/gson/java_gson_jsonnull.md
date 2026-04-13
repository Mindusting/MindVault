---
author: Mindusting
corrected: true
headerFile: false
tags:
  - Programming
  - Java
  - JSON
title: JsonNull en GSON
---

# JSONNULL EN GSON

Este objeto representa el valor `null` de [**JSON**](../../../../data_format/json.md); el objetivo de este objeto es poder diferenciar entre la inexistencia de un valor que se representa con el valor `null` de **Java** y la existencia del valor `null` en el [**JSON**](../../../../data_format/json.md); esto se entiende mejor con un ejemplo:

```java
JsonObject emptyObj = new JsonObject();

emptyObj.get("key");
// Este `get` devuelve un valor `null` de Java
// ya que no existe ese valor dentro del JsonObject.

JsonObject noEmptyObj = new JsonObject();
noEmptyObj.add("key", JsonNull.INSTANCE);

noEmptyObj.get("key");
// Este `get` no devuelve un valor `null` de Java sino
// un `JsonNull` indicando que sí existe la clave `key`
// pero que este contiene un valor nulo.
```
