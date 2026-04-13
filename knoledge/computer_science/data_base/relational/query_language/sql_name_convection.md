---
author: Mindusting
corrected: false
tags:
  - DataBase
  - SQL
title: Convención de nombres en SQL
---

# CONVENCIÓN DE NOMBRES

SQL no tiene una convención de nombre propiamente, por lo que tendrás que regirte a la convención que te ofrezca si estás en un proyecto por cuenta ajeta o usar el tuyo propio si es por cuenta propia; yo por mi cuenta he terminado llegando a un formato que me gusta ya que me permite separar múltiples elementos haciendo uso de una combinación de `camelCase` y `snake_case` que me permite crear nombres comuestos y al mismo tiempo identificar de forma sencilla los diferentes elementos dentro del nombre.

1. Los nombre tanto de las **tablas** como de las **columnas** se escriben en `camelCase`.
2. Cuando se define un nombre conpuesto por nombres de **tablas** y/o **columnas** se escriben la separación de estos con `snake_case`.
3. Los nombres de las restricciones contienen prefijos:
    1. Las **claves primarias** comienzan con `pk`.
    2. Las **claves** foráneas comienzan con `fk`.
    3. Los `NOT NULL` comienzan con `nn`.
    4. Los `UNIQUE` comienzan con `uk`.
    5. Los `CHECK` comienzan con `chk`.
4. Las vistas comienzan por `v` seguidos del nombre de la propia vista; si la vista está pensada para mostrar los datos de forma bonita o para poder encontrar fallos (*es decir, que solo van a ser usadas por el ardministrador de la base de datos para el mantenimiento de esta*), entonces estas llevarán una `w` en vez de una `v`.
5. Los índices comienzan por `i`, seguido de los nombres de las **columnas** que indexan y terminan con el nombre de la **tabla** a la que pertenecen dicas **columnas**.
6. Los triggers debe de tener un prefijo compuesto; este prefijo deberá seguir ciertas reglas:
    1. Tendrá que comenzar por `b` o `a` dependiendo de si es `BEFORE` o `AFTER`.
    2. Seguido de un `i`, `u` o `d`; dependiendo de si es para `INSERT`, `UPDATE` o `DELETE`; en caso de ser compuesto, es decir que abarque por ejemplo `INSERT` y `UPDATE` se pondrán los dos, en este caso `iu`.
    3. En caso de aplicarse sobre unas columnas en concreto se especificará el nombre de estas con `camelCase` tras el prefijo.
    4. Al final del nombre debe estar el nombre de la tabla sobre la que se aplicará el trigger.

---

Aquí podemos ver un pequeño ejemplo de una pequeña base de datos con un poco de todo para que puedas ver como se aplican estas reglas.

```sql
CREATE TABLE files (
    id      INTEGER,
    path    TEXT NOT NULL,
    name    TEXT NOT NULL,
    content BLOB NOT NULL,
    cDate   TEXT NOT NULL,
    mDate   TEXT NOT NULL,

    CONSTRAINT pk_id_files
    PRIMARY KEY(id),

    CONSTRAINT uk_path_name_files
    UNIQUE(path, name)
);

CREATE INDEX i_name_files ON files (
    name ASC
);

CREATE TRIGGER ai_files
AFTER INSERT ON files
BEGIN
    UPDATE files
    SET
        cDate = datetime('now'),
        mDate = datetime('now')
    WHERE id = NEW.id;
END;

CREATE TRIGGER au_path_name_content_files
AFTER UPDATE OF path, name, content ON files
BEGIN
    UPDATE files
    SET
        mDate = datetime('now'),
    WHERE id = NEW.id;
END;

CREATE VIEW w_files AS
SELECT
    path,
    name,
    content
FROM files
ORDER BY
    path ASC,
    name ASC;
```
