---
aliases: [Tablas de la verdad en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-21 07:09:44
headerFile: false
modificationDate: 2026-10-21 07:09:52
rating:
tags: [Math]
---

# TABLAS DE LA VERDAD

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

## NEGACIÓN

%%

| $p$ | $\neg p$ |
|:---:|:--------:|
|  F  |    V     |
|  V  |    F     |

%%

|   $p$   | $\neg p$ |
|:-------:|:--------:|
| ==🔴F== | ==🟢V==  |
| ==🟢V== | ==🔴F==  |

## CONJUGACIÓN

%%

| $p$ | $q$ | $p \land q$ |
|:---:|:---:|:-----------:|
|  F  |  F  |      F      |
|  F  |  V  |      F      |
|  V  |  F  |      F      |
|  V  |  V  |      V      |

%%

|   $p$   |   $q$   | $p \land q$ |
|:-------:|:-------:|:-----------:|
| ==🔴F== | ==🔴F== |   ==🔴F==   |
| ==🔴F== | ==🟢V== |   ==🔴F==   |
| ==🟢V== | ==🔴F== |   ==🔴F==   |
| ==🟢V== | ==🟢V== |   ==🟢V==   |

## DISYUNCIÓN

%%

| $p$ | $q$ | $p \lor q$ |
|:---:|:---:|:----------:|
|  F  |  F  |     F      |
|  F  |  V  |     V      |
|  V  |  F  |     V      |
|  V  |  V  |     V      |

%%

|   $p$   |   $q$   | $p \lor q$ |
|:-------:|:-------:|:----------:|
| ==🔴F== | ==🔴F== |  ==🔴F==   |
| ==🔴F== | ==🟢V== |  ==🟢V==   |
| ==🟢V== | ==🔴F== |  ==🟢V==   |
| ==🟢V== | ==🟢V== |  ==🟢V==   |

## CONDICIONAL

%%

| $p$ | $q$ | $p \to q$ |
|:---:|:---:|:---------:|
|  F  |  F  |     V     |
|  F  |  V  |     V     |
|  V  |  F  |     F     |
|  V  |  V  |     V     |

%%

|   $p$   |   $q$   | $p \to q$ |
|:-------:|:-------:|:---------:|
| ==🔴F== | ==🔴F== |  ==🟢V==  |
| ==🔴F== | ==🟢V== |  ==🟢V==  |
| ==🟢V== | ==🔴F== |  ==🔴F==  |
| ==🟢V== | ==🟢V== |  ==🟢V==  |

## BICONDICIONAL

%%

| $p$ | $q$ | $p \leftrightarrow q$ |
|:---:|:---:|:---------------------:|
|  F  |  F  |           V           |
|  F  |  V  |           F           |
|  V  |  F  |           F           |
|  V  |  V  |           V           |

%%

|   $p$   |   $q$   | $p \leftrightarrow q$ |
|:-------:|:-------:|:---------------------:|
| ==🔴F== | ==🔴F== |        ==🟢V==        |
| ==🔴F== | ==🟢V== |        ==🔴F==        |
| ==🟢V== | ==🔴F== |        ==🔴F==        |
| ==🟢V== | ==🟢V== |        ==🟢V==        |
