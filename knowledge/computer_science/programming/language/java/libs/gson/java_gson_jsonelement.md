---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - Java
  - JSON
title: JsonElement en GSON
---

# JSONELEMENT EN GSON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

## MÉTODOS DE TRANSFORMACIÓN DE TIPO

Para transformar un `JsonElement` en otro tipo de dato más concreto (*ya que este es genérico*), podremos usar los siguientes métodos para concretar que tipo de dato representa; pudiendo ser **valores primitivos** u otro **objeto**.

| MÉTODO               | DEVUELVE                                                         |
|:-------------------- |:---------------------------------------------------------------- |
| `getAsBoolean`       | `boolean`                                                        |
| `getAsByte`          | `byte`                                                           |
| `getAsShort`         | `short`                                                          |
| `getAsInt`           | `int`                                                            |
| `getAsLong`          | `long`                                                           |
| `getAsFloat`         | `float`                                                          |
| `getAsDouble`        | `double`                                                         |
| `getAsCharacter`     | `char`                                                           |
| `getAsString`        | [`String`](../../packages/java/lang/java_lang_string.md)         |
| `getAsJsonPrimitive` | [`JsonPrimitive`](java_gson_jsonprimitive.md)                    |
| `getAsJsonArray`     | [`JsonArray`](java_gson_jsonarray.md)                            |
| `getAsJsonObject`    | [`JsonObject`](java_gson_jsonobject.md)                          |
| `getAsJsonNull`      | [`JsonNull`](java_gson_jsonnull.md)                              |
| `getAsBigDecimal`    | [`BigDecimal`](../../packages/java/math/java_math_bigdecimal.md) |
| `getAsBigInteger`    | [`BigInteger`](../../packages/java/math/java_math_biginteger.md) |
