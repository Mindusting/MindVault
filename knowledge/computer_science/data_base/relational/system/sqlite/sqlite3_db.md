---
author: Mindusting
corrected: false
tags:
  - DataBase
  - SQL
  - SQLite3
title: Bases de datos en SQLite3
---

# BASES DE DATOS EN SQLITE3

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Corregir ortografía.

> [!help]- REFERENCIAS WEB
> - [SQLite](https://sqlite.org/inmemorydb.html) #WWW/SQLite

Las [bases de datos](../../theory/db.md) en SQLite3 son guardadas en forma de un único archivo dentro de nuestro dísco duro en local.

También existe la posibilidad de trabajar sobre una [base de datos](../../theory/db.md) en memoria, esto se consigue cuando a la hora de indicar la ruta del archivo de la [base de datos](../../theory/db.md), indicamos la dirección `:memory:`; al hacer esto no se trabajara sobre el disco sino sobre la memoria, haciendo que esta [base de datos](../../theory/db.md) sea temporal, y se borrara en el momento en que se cierre la conexión con esta.
