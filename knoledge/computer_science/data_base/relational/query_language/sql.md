---
aliases: [SQL 🛢]
author: Mindusting
corrected: false
headerFile: true
logo: imgs/db.png
rating: 
tags: [DataBase, SQL]
---

<h1 align="center">SQL</h1>

![#logo](../../../../../imgs/db.png)

---

# SQL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Explicar que es SQL.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/sql/default.asp) #WWW/W3Schools
> - [Geeksforgeeks](https://www.geeksforgeeks.org/sql/sql-tutorial) #WWW/geeksforgeeks
> 
> YouTube:
> - [Data with Baraa](https://youtu.be/SSKVgrwhzus) #WWW/YT/DataWithBaraa
> - [ByteByteGo](https://youtu.be/yMqldbY2AAg) #WWW/YT/ByteByteGo
> - [Decomplexify (chanel)](https://www.youtube.com/@decomplexify) #WWW/YT/Decomplexify
> - [CS50](https://youtu.be/1RCMYG8RUSE) #WWW/YT/CS50

> [!important] IMPORTANTE
> Esta documentación de SQL está a medio hacer (*como casido todo lo que podeis encontrar en esta bóveda de notas*), está desordenada, entre otra serie de problemas, ya que estube escribiendo esta documentación, a medía que iba aprendiendo SQL y las diferencias entre los distintos tipos; por lo que voy a cambiar muchas cosas de esta sección, tengo pensado concentrarme en completar primero la documentación de SQL genérica, que es esta; y luego ir escribiendo la documentación de los SQL específicos, por lo que va a estár sujeto a muchos cambios.

SQL (`Structured Query Language`) es un estándar para gestionar bases de datos, existen diferentes tipos de SQL, teniendo cada uno sus pros y sus contras, pero todos siguen la misma estructura pese a las diferencias que tienen entre ellos.

Se suele decir que aprender SQL es como andar en bicicleta una vez aprendes, al cambiar de bicicleta no tienes que empezar desde cero, solamente acostumbrarte a los pequeños detalles que cambian.

Por ello, he dividido esta documentación en varias partes, en la [primera](#DOCUMENTACIÓN%20GENERAL) se explica de forma general las características del estándar SQL, y su funcionamiento, en contraste, en la [segunda parte](#DOCUMENTACIÓN%20CONCRETA) se explica más en detalle cada uno de los tipos de SQL.

> [!note] Nota
> Las palabras clave de **SQL** se pueden escribir tanto en mayúsculas como en minúsculas, pero suele ser recomendable escribirlo todo en mayúsculas ya que así es más fácil de identificar que son palabras clave y que son nombres.

## DOCUMENTACIÓN GENERAL

- [COMENTARIOS 💬](sql_comments.md)
- [CONVECCIÓN DE NOMBRE](sql_name_convection.md)
- [BASE DE DATOS 🛢](sql_db.md)
- [TABLAS 📋](sql_table.md)
- [CRUD](sql_crud.md)
    - [OPERADORES](sql_operators.md)
- [FUNCIONES](sql_func.md)
- [ÍNDICES](sql_index.md)
- [VARIABLE](sql_variables.md)
- [PROCEDIMIENTOS](sql_procedures.md)
- [USUARIOS](sql_users.md)
- [TRIGGERS 🔫](sql_triggers.md)
- [EXCEPCIONES ⚠️](sql_exceptions.md)
- [INYECCIÓN DE SQL](sql_injection.md)

## TIPOS DE INSTRUCCIONES

**SQL** se compone de multiples instrucciones, estos se dividen en varios grupos:

- [DDL (Data Definition Language)](sql_ddl.md)
- [DQL (Data Query Language)](sql_dql.md)
- [DML  (Data Manipulation Language)](sql_dml.md)
- [DCL (Data Control Language)](sql_dcl.md)
- [TCL (Transaction Control Language)](sql_tcl.md)

## DOCUMENTACIÓN CONCRETA

- [SQLite3](../system/sqlite/sqlite3.md)
- [MySQL](../system/mysql/mysql.md)
- [SQL-Server](../system/sql_server/sql_server.md)
