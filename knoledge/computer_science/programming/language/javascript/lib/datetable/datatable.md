---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - JavaScript
  - Web
title: DataTable
---

# DATATABLE

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Impoortante remarcar que hay diferencias entre el `DataTable` normal y el `DataTable` de jQuery; principalmente que cambia el como declararlas; se debe explicar la diferencia y poner ejemplo.

> [!help]- REFERENCIAS WEB
> - [DataTables](https://datatables.net) #WWW/DataTables

## ORDENAR DATOS

Para ordenar los datos y permitir que el usuario pueda ordenarlos a su gusto, se usa la *calve* `order`, esta contendrá una [**matriz**](../../js_array.md) (*no te sustes si no sabes de matriz, es muy facil*); en el eje $y$ tendremos los diferentes factores de ordenado, mientras que en eje $x$ tendremos dos elementos, el **índice** (*el cual empieza a contar desde el `0`*) de la columna y la dirección de ordenado (*pudiendoser `asc` para "ascendente" y `desc` para "descendente"*).

---

Imaginemos que tenemos la siguiente tabla:

|  ID | NAME    | BIRTH DATE |
| ---:|:------- |:---------- |
|   1 | Adelio  | 2000-01-01 |
|   2 | Adelia  | 2000-01-01 |
|   3 | Antonia | 1984-01-01 |
|   4 | Antonio | 1984-01-01 |

Si aplicásemás la siguiente configuración de ordenado:

```js
{
    order: [
         [2, "asc"],
         [1, "desc"]
    ]
}
```

Se vería de la siguiente forma:

|  ID | NAME    | BIRTH DATE |
| ---:|:------- |:---------- |
|   4 | Antonio | 1984-01-01 |
|   3 | Antonia | 1984-01-01 |
|   1 | Adelio  | 2000-01-01 |
|   2 | Adelia  | 2000-01-01 |

## DEFINICIÓN DE COLUMNAS

```js
{
    columnDefs: [
        {
            target: 1,
            visible: false,
            searchable: false
        }
    ]
}
```
