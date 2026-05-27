---
aliases:
  - CSV
author: Mindusting
corrected: false
headerFile: true
tags:
  - CSV
---

# CSV

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Sintaxis del **CSV** (*Comma-separated values*):

- **Encabezado**: nombres de las columnas/propiedades de los registros separados por el mismo **delimitador de campo**.
- **Delimitación de campo**: generalmente una **coma** (`,`).
- **Comillas anidadas**: generalmente suelen ser **comillas dobles** (`"`), si un campo contien unas **comillas** estas se tendrán que **duplicar** y poner el valor del campo entre **comillas**; si un campo contien un salto de línea, se debe entrecomillar, y no se debe sustituir por un `\n`, se deja talcuál.
- **Campos vacíos**: deben mantener la posición entre los **delimitadores de campo** para mantener la integridad de los datos.
- **Codificación**: los archivos deben estár codificados en [**UTF-8**](utf.md#UTF-8).
- **Salto de línea**: cada registro debe terminar con un salto de línea `LN` o `CR` + `LN`.

%%

```csv
id,name,age
1,Adelio,20
2,Adelia,22
```

```py
import csv


def main() -> None:
    with open("data.csv") as file:
        #"""
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(row)
        #"""
        """
        #reader = csv.DictReader(file)
        users = list()
        for row in reader:
            users.append(User(*row.values()))

        for user in users:
            print(user)
        #"""


class User:

    def __init__(self, iid: int, name: str, age: int):
        self._id  = iid
        self.name = name
        self.age  = age

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, iid) -> None:
        self._id = iid

    def __str__(self) -> str:
        return f"User(id={self._id}, name={self.name}, age={self.age})"

    def __repr__(self) -> str:
        return f"User(id={self._id}, name={self.name}, age={self.age})"


if "__main__" == __name__:
    main()
```

%%
