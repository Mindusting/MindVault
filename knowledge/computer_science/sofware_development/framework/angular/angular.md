---
aliases:
  - Angular
author: Mindusting
corrected: false
headerFile: true
tags:
  - Programming
  - Web
  - Angular
rating:
---

# ANGULAR

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!external-link]- REFERENCIAS WEB
> YouTube:
> - [pildorasinformáticas](https://youtube.com/playlist?list=PLU8oAlHdN5BnNAe8zXnuBNzKID39DUwcO) #WWW/YT/pildorasinformaticas

[**Angular**](https://angular.dev) es un framework de código abierto desarollado por **Google** para crear aplicaciones Web; haciendo uso del lenguaje [**TypeScript**](../../../programming/language/typescript/ts.md).

## TEORÍA

- [Instalación](theory/installation.md)
- [Componentes](theory/components.md)

## COMANDOS

- [`generate component`](commands/generate_component.md)
- [`new`](commands/new.md)

%%

## ÍNDICE

- [Instalación](theory/installation.md)
- [Nuevo proyecto](commands/new.md)
- [Componentes](commands/generate_component.md)

```base
filters:
  and:
    - file.name.startsWith("angular")
    - "!file.properties.headerFile"
formulas:
  Título: link(file, title)
  Puntuación: 'if(file.properties.rating, "Puntuación: " + file.properties.rating, "")'
  Descripción: 'if(file.properties.description, "Descripción: " + file.properties.description, "")'
views:
  - type: list
    name: Todo
    order:
      - formula.Título
      - formula.Descripción
      - formula.Puntuación
    indentProperties: true

```

%%
