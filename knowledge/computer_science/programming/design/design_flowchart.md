---
aliases: [Diagrama de flujo]
alias: Flow chart
author: Mindusting
corrected: false
tags:
  - SoftwareDesign
cssclasses: [center-mermaid]
---

# DIAGRAMA DE FLUJO

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Documentar terminales.
> > - [ ] Documentar instrucciones.
> > - [ ] Documentar IO.
> > - [ ] Documentar condicionales/bucles.

> [!faq]- FAQ
> - [¿Como puede hacer diagramas de flujo en Mermad/Obsidian?](../../markup_language/mermaid/mermaid_flowchart.md)

Los **diagramas de flujo** representan los caminos que puede tomar un programa de forma visual.

## SIMBOLOS

```mermaid
flowchart TB
    terminal([TERMINAL])
    process[PROCESS]
    page_ref((REF. PAG.))
```

```mermaid
flowchart TB
    if{DECISIÓN}
    io[/I/O/]
```

### TERMINAL

El objetivo del terminal 

```mermaid
flowchart TB
    inicio([INICIO]) -->
    fin([FIN])
```

### OPERACIONES

### REFERENCIA DE PÁGINA

```mermaid
flowchart TB
    inicio((INICIO))
```
