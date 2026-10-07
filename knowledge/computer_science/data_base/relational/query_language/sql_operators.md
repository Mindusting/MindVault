---
author: Mindusting
corrected: false
headerFile: false
tags:
  - DataBase
  - SQL
title: Operadores en SQL
---

# OPERADORES DE SQL

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Explicar los operadores relacionales.
> > - [ ] Explicar los operadores lógicos.
> > - [ ] Explicar el operador `IN`.
> > - [ ] Explicar el operador `BETWEEN`.

> [!help]- REFERENCIAS WEB
> - [W3 Schools (LIKE)](https://www.w3schools.com/sql/sql_like.asp) #WWW/W3Schools

## OPERADORES RELACIONALES

## OPERADORES LÓGICOS

## OPERADOR LIKE

El operador `LIKE` se usa para comparar textos de una forma más flexible haciendo uso de caracteres especiales para definir patrones:

- Porcentaje (`%`): expresa la existencia de cero a múltiples [\[0, x\]](../../../../mathematic/temp/math_range_notation.md) caracteres.
- Barrabaja (`_`): expresa la existencia obligatoria de un caracter.

---

Imaginemos que tenemos la siguiente tabla de usuarios para hacer unas operaciones y entender como funciona este operador:

|  id | name  |
| ---:|:----- |
|   1 | Mar   |
|   2 | María |
|   3 | Marta |
|   4 | Jaime |
|   5 | Mario |

---

En la siguiente consulta podemos ver como se obtienen todos los IDs de los usuarios junto con el resultado de la operación en la que se comprueba si el nombre comienza por "Mar":

```sql
SELECT
    id,
    name LIKE 'Mar%' AS nameCondition
FROM users;
```

Aquí podemos ver el resultado de la operación:

|  id | nameCondition |
| ---:| -------------:|
|   1 |             1 |
|   2 |             1 |
|   3 |             1 |
|   4 |             0 |
|   5 |             1 |

---

En la siguiente consulta podemos ver como se obtienen todos los IDs y nombres de los usuarios cullos nombres comiencen por "Mar" seguido de dos caracteres:

```sql
SELECT
    id,
    name
FROM users
WHERE name LIKE 'Mar__';
```

Aquí podemos ver el resultado de la operación:

|  id | name  |
| ---:|:----- |
|   2 | María |
|   3 | Marta |
|   5 | Mario |

---

En la siguiente consulta podemos ver como se obtienen todos los IDs y nombres de los usuarios cullos nombres contengan la letra "i" sin tilde:

```sql
SELECT
    id,
    name
FROM users
WHERE LOWER(name) LIKE '%i%';
```

Aquí podemos ver el resultado de la operación:

|  id | name  |
| ---:|:----- |
|   4 | Jaime |
|   5 | Mario |

---

> [!tip] CONSEJO
> Trata de evitar el signo de porcentage (`%`) al principio del texto, ya que esto inavilita el uso de los [índices](sql_index.md), obligando a que la consulta tenga que hacer un barrido de la columna completa, pudiendo ralentizar de forma significante las consultas.

## OPERADOR IN

## OPERADOR BETWEEN

%%

```sql
SELECT *
FROM users
WHERE name BETWEEN "W%" AND "Z%";
```

%%
