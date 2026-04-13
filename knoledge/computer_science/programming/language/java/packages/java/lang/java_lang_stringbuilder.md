---
author: Mindusting
corrected: false
tags:
  - Programming
  - Java
  - Package
title: StringBuilder en Java
---

# STRINGBUILDER EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!abstract] SINTAXIS
> StringBuilder ***\[name\]*** = new StringBuilder();

El `StringBuilder` se comporta como una [lista](../util/java_util_list.md), ya que podemos ir añadiendo [`Strings`](java_lang_string.md) mediante el [método](../../../java_method.md) `append`, una vez hemos añadido todos los [`Strings`](java_lang_string.md) que queramos, podemos juntarlos todos mediante el [método](../../../java_method.md) `toString`.

```java
StringBuilder stringBuilder = new StringBuilder();

stringBuilder.append("Manzana\n");
stringBuilder.append("Naranja\n");
stringBuilder.append("Plátano\n");
stringBuilder.append("Pera\n");
stringBuilder.append("Arándano\n");
stringBuilder.append("Berenjena\n");

// Se imprimirá todas las palabars como un único String.
System.out.print(stringBuilder.toString());
```
