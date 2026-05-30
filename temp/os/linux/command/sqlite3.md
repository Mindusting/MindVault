---
author: Mindusting
corrected: false
tags:
  - OS
  - Linux
  - Bash
  - Command
title: SQLite3 en BASH
---

# SQLITE3 EN BASH

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

El comando `sqlite3` sirve para poder crear y acceder a [bases de datos](../../../../knoledge/computer_science/data_base/relational/theory/db.md) de [**SQLite3**](../../../../knoledge/computer_science/data_base/relational/system/sqlite/sqlite3.md), permitiendo ejecutar instrucciones de [**SQL**](../../../../knoledge/computer_science/data_base/relational/query_language/sql.md); todo ocurre de forma local ya que las [bases de datos](../../../../knoledge/computer_science/data_base/relational/theory/db.md) de [**SQLite3**](../../../../knoledge/computer_science/data_base/relational/system/sqlite/sqlite3.md) son un único archivo local.

## ABRIR BASE DE DATOS

Para abrir una [base de datos](../../../../knoledge/computer_science/data_base/relational/theory/db.md) se puede hacer de forma directa con el propio comando `sqlite3` seguido del nombre del archivo de la [base de datos](../../../../knoledge/computer_science/data_base/relational/theory/db.md).

> [!abstract] SINTAXIS
> sqlite3 ***\[dbName\]***

Esta forma sirve tanto para abrir una [base de datos](../../../../knoledge/computer_science/data_base/relational/theory/db.md) como para crear una nueva, esto último ocurre cuando el nombre del archivo no existe.

```bash
sqlite3 main.db
```

---

Si hemos ejecutado el comando `sqlite3` sin especificar el nombre de un archivo y por tanto no tenemos ninguna [base de datos](../../../../knoledge/computer_science/data_base/relational/theory/db.md) abierta o tenemos ya una abierta y queremos abrir otra, podremos usar la instrucción `.open` seguida del nombre del archivo.

> [!abstract] SINTAXIS
> .open ***\[dbName\]***

```bash
.open main.md
```

## LISTAR ELEMENTOS

- `.table`: muestra los nombres de las [**tablas**](../../../../knoledge/computer_science/data_base/relational/system/sqlite/sqlite3_table.md) y [**vistas**](../../../../knoledge/computer_science/data_base/relational/system/sqlite/sqlite3_view.md).
- `.index`: muestra los nombres de los [**índices**](../../../../knoledge/computer_science/data_base/relational/system/sqlite/sqlite3_index.md).

## EJECUTAR ARCHIVOS SQL

Para ejecutar un conjunto de instrucciones alojados en un archivo [`.sql`](../../../../knoledge/computer_science/data_base/relational/query_language/sql.md) sobre una [base de datos](../../../../knoledge/computer_science/data_base/relational/theory/db.md) tenemos dos opciones:

1. Se puede ejecutar la instrucción `.read` una vez ya tengamos una [base de datos abierta](#ABRIR%20BASE%20DE%20DATOS); esta necesita del nombre de un archivo para leer.
    > [!abstract] SINTAXIS
    > .read ***\[sqlFileName\]***
2. Se puede ejecutar el programa `sqlite3` seguido por el nombre de la [base de datos](../../../../knoledge/computer_science/data_base/relational/theory/db.md), un **menor que** (`<`) y el nombre del archivo [`.sql`](../../../../knoledge/computer_science/data_base/relational/query_language/sql.md); esto abrirá o creará la [base de datos](../../../../knoledge/computer_science/data_base/relational/theory/db.md) y ejecutará todo el contenido del archivo.
    > [!abstract] SINTAXIS
    > sqlite3 ***\[dbName\]*** < ***\[sqlFileName\]***
