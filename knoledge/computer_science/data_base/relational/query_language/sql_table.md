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

> [!syntax] SINTAXIS
> CREATE TABLE ***\{IF NOT EXISTS\}*** ([***\[columnDefinitions\]***](#DEFINICIÓN%20DE%20COLUMNAS))

## DEFINICIÓN DE COLUMNAS

> [!syntax] SINTAXIS
> ***\[columnName\] [\[columnType\]](#TIPOS%20DE%20DATOS) [\{constraints\}](#RESTRUCCIONES)***

### TIPOS DE DATOS

Los tipos de datos cambian dependiendo del **SQL** que estemos usando pero hay ciertos tipos de datos que son "estandar" (*son comunes a nivel conceptual*); estos son los tipos de datos más básicos y simples que permitirán representar las **identidades**:

- [**Booleano**](../../../../../temp/pc/pc_boolean.md)
- **Número enteros**
- **Número decimales**
- **Texto**
- **Binario**

### RESTRUCCIONES

Las restricciones permiten definir de una forma más exacta el comportamiento que debe tener cada columna.
