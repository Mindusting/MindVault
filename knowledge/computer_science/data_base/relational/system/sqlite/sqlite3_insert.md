---
author: Mindusting
corrected: false
tags:
  - DataBase
  - SQL
  - SQLite3
title: Insertar datos en SQLite3
---

# INSERT EN SQLITE3

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [SQLite](https://sqlite.org/lang_insert.html) #WWW/SQLite

Para poder insertar un nuevo registro en una tabla se sigue el siguiente esquema:

Un ejemplo de ello es el siguiente:

```sql
INSERT INTO users (
    name,
    last_name,
    email
) values (
    'Adelio',
    'Gonzalez',
    'adelio@gmail.com'
);
```
