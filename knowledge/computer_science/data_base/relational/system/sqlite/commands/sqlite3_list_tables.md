---
author: Mindusting
corrected: false
tags:
  - Programming
  - SQL
  - SQLite3
title: Listar tablas en SQLite3
---

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Para listar las tablas que tenemos creadas en nuestra base de datos podemos usar le comando `.tables`.

%%
```sql
PRAGMA table_info(sqlite_master);
```

```sql
SELECT name
FROM sqlite_master
WHERE type='table';
```
%%
