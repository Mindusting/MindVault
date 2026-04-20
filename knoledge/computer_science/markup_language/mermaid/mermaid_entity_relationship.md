---
aliases: [Diagrama de entidad relación en Mermaid]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Mermaid]
---

# DIAGRAMA DE ENTIDAD RELACIÓN EN MERMAID

> [!unfinished-file]- ESTE APATADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [Mermaid](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) #WWW/Mermaid

## ENTIDADES

```txt
erDiagram
    users {
        int id
        string fname
        string lname
    }
```

## CONEXIONES

| IZQUIERDA | DERECHA | SIGNIFICADO      |
|:---------:|:-------:|:---------------- |
|    \|o    |   o\|   | De cero a uno    |
|   \|\|    |  \|\|   | Uno exacto       |
|    \}o    |   o\{   | De cero a varios |
|   \}\|    |  \|\{   | De uno a varios  |

| CONEXSIÓN | FORMA       |
|:---------:|:----------- |
|   `--`    | Contínua    |
|   `..`    | Discontínua |
