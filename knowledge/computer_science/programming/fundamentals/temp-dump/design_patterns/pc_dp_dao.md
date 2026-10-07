---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming/Concept
  - DesignPattern
title: DAO de programación
---

# DAO EN PROGRAMACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Los **DAO** en el ámbito de la programación se refiere a la abstracción del acceso a la fuente de datos, bien de una [**base de datos**](../../../../data_base/relational/theory/db.md) o **ficheros**; permitiendo que no se tenga que acceder a la fuente de datos de forma directa.

> [!example] EJEMPLO DE DAO
> Un ejemplo de esto sería cuando tenemos una entidad `User` con sus *gestion* (`UserManager`) que permite hacer las operaciones básicas de [**CRUD**](../../../../data_base/relational/query_language/sql_crud.md) sobre una [**base de datos**](../../../../data_base/relational/theory/db.md); encargadose este último de la conecxión a la [**base de datos**](../../../../data_base/relational/theory/db.md) entre otras cosas.
