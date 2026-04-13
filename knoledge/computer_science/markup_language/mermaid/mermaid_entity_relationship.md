---
author: Mindusting
corrected: false
tags:
  - Mermaid
title: Diagrama de entidad relación en Mermaid
---

# DIAGRAMA DE ENTIDAD RELACIÓN EN MERMAID

> [!fail]- ESTE APATADO ESTÁ INCOMPLETO
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
|    --     | Contínua    |
|    ..     | Discontínua |
