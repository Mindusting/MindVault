---
aliases: [Tablas en SQL]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [DataBase, SQL]
---

# TABLAS EN SQL

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Explicar las restricciones de columnas.
> > - [ ] Explicar las claves primarias y foráneas.
> > - [ ] Añadir ejemplos de creación de tablas.

Para definir tablas en **SQL** podremos hacer siguiendo la siguiente sintaxis, ten en cuenta que es una sintaxis compuesta, es decir, si clicas en los diferentes componentes de la sintaxis, te va a llevar a otras "subsintaxis":

> [!syntax] SINTAXIS
> CREATE TABLE ***\{IF NOT EXISTS\} \[tableName\]*** ([***\[colDef\]***](#DEFINICIÓN%20DE%20COLUMNAS), [***\{constraints\}***](#RESTRUCCIONES))

En caso de querer definir múltiples *columnas* y/o *restricciones* se deben separa estas definiciones mediante comas.

La parte de `IF NOT EXISTS` es opcional, si la indicamos, al tratar de ejecutar la instrucción de cereación de la tabla, si ya existe una con ese mismo nombre, simplemente ignorará nuestra instrucción, de lo constrario, no dará un error indicandonos que ya existe una tabla con dicho nombre.

Aquí os dejo un ejeplo de una sola tabla para que veais como quedaría, está hecha en [**SQLite3**](../system/sqlite/sqlite3.md) (*ya que es muy sencillo*):

```sql
CREATE TABLE users (
    -- Aquí empiezan las definiciones de las columnas,
    -- algunas de ellas ya tienen restricciones.
    id         INTEGER PRIMARY KEY,
    fatherId   INTEGER,
    motherId   INTEGER,
    firstName  TEXT NOT NULL,
    lastName1  TEXT,
    lastName2  TEXT,
    birthDate  TEXT,
    height     REAL CHECK (height > 0),
    weight     REAL CHECK (height > 0),
    sex        TEXT CHECK (sex IN ('M', 'F')),
    personalId TEXT UNIQUE,

    -- Aquí empiezan las restricciones con nombre.
    CONSTRAINT fk_users_fatherId
    FOREIGN KEY (fatherId)
    REFERENCES users(id)
    ON UPDATE CASCADE,

    CONSTRAINT fk_users_motherId
    FOREIGN KEY (motherId)
    REFERENCES users(id)
    ON UPDATE CASCADE,

    -- Si se establece una fecha de nacimiento,
    -- comprobamos que sea una fecha válida.
    CONSTRAINT chk_users_birthDate
    CHECK (birthDate IS date(birthDate, '+0 days'))
);
```

## DEFINICIÓN DE COLUMNAS

La definición de una *columna* se compone de varias partes

> [!syntax] SINTAXIS
> ***\[columnName\] [\[columnType\]](#TIPOS%20DE%20DATOS) [\{constraints\}](#RESTRUCCIONES)***

### TIPOS DE DATOS

Los tipos de datos cambian dependiendo del tipo de **SQL** que estemos usando, pero hay ciertos tipos de datos que son "estandar" (*son comunes a nivel conceptual*); estos son los tipos de datos más básicos y simples que permitirán representar las **identidades**:

- [**Booleano**](../../../../../temp/pc/pc_boolean.md)
- **Número enteros**
- **Número decimales**
- **Texto**
- **Tiempo**
- **Binario**

### RESTRUCCIONES

Las restricciones permiten definir de una forma más exacta el comportamiento que debe tener cada columna.

#### NULL Y NOT NULL

#### UNIQUE

#### CHECK

#### CLAVE PRIMARIA

#### CLAVE FORÁNEA
