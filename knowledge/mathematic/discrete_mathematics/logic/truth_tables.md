---
aliases: [Tablas de la verdad en matemáticas]
author: Mindusting
corrected: false
creationDate: 2026-10-21 07:09:44
headerFile: false
modificationDate: 2026-11-15 05:40:53
rating:
tags: [Math]
---

# TABLAS DE VERDAD

> [!seealso]- MIRA TAMBIÉN
> - [Proposiciones](propositions.md)
> - [Conectores lógicos](logical_connectives.md)
> - [Reglas de inferencia](inference_rules.md)
> - [Métodos de demostración](../proof_methods.md)

Una **tabla de verdad** muestra el valor de verdad de una [proposición compuesta](propositions.md) para **todas las combinaciones posibles** de los valores de verdad de sus proposiciones atómicas.

- **V:** verdadero.
- **F:** falso.
- Cada fila representa una combinación posible.
- Cada columna muestra una proposición o el resultado de aplicar un [conector lógico](logical_connectives.md).

## CONSTRUCCIÓN DE UNA TABLA DE VERDAD

1. Identificar las variables proposicionales ($p$, $q$, $r$, etc.).
2. Escribir todas las combinaciones posibles de **V** y **F**.
3. Añadir columnas para las operaciones intermedias, si hacen falta.
4. Calcular el resultado final siguiendo los conectores y los paréntesis.

---

$$2^n$$

- $n$: número de variables proposicionales distintas.
- Con **1 variable**: $2$ filas.
- Con **2 variables**: $4$ filas.
- Con **3 variables**: $8$ filas.

## CÓMO ENUMERAR LAS FILAS SIN OMITIR NINGUNA

La expresión $2^n$ procede de que cada una de las $n$ variables tiene **dos opciones independientes**, V o F. Si tenemos $3$ variables, las combinaciones son $2 \cdot 2 \cdot 2 = 8$.

Una técnica práctica es alternar valores en bloques cada vez más cortos:

| $p$ | $q$ | $r$ |
|:---:|:---:|:---:|
|  V  |  V  |  V  |
|  V  |  V  |  F  |
|  V  |  F  |  V  |
|  V  |  F  |  F  |
|  F  |  V  |  V  |
|  F  |  V  |  F  |
|  F  |  F  |  V  |
|  F  |  F  |  F  |

La primera columna cambia cada cuatro filas, la segunda cada dos y la tercera en cada fila. El orden elegido no altera el resultado del análisis, siempre que aparezcan **todas las combinaciones una sola vez**.

> [!important] IMPORTANTE
> Una tabla de verdad con $n$ variables **no** necesita $2^n$ columnas, sino $2^n$ **filas** de asignaciones; el número de columnas depende de las expresiones intermedias que decidamos mostrar.

## TABLAS DE LOS CONECTORES LÓGICOS

| $p$ | $q$ | $\neg p$ | $p \land q$ | $p \lor q$ | $p \to q$ | $p \leftrightarrow q$ |
|:---:|:---:|:--------:|:-----------:|:----------:|:---------:|:---------------------:|
|  V  |  V  |    F     |      V      |     V      |     V     |           V           |
|  V  |  F  |    F     |      F      |     V      |     F     |           F           |
|  F  |  V  |    V     |      F      |     V      |     V     |           F           |
|  F  |  F  |    V     |      F      |     F      |     V     |           V           |

- **Negación ($\neg p$):** invierte el valor de $p$.
- **Conjunción ($p \land q$):** verdadera si ambas son verdaderas.
- **Disyunción ($p \lor q$):** verdadera si al menos una es verdadera (incluidas ambas).
- **Condicional ($p \to q$):** falsa únicamente si $p$ es verdadera y $q$ es falsa.
- **Bicondicional ($p \leftrightarrow q$):** verdadero cuando $p$ y $q$ tienen el mismo valor.

## EJEMPLO DE CONSTRUCCIÓN

Comprobemos los valores de verdad de la expresión $\neg p \lor q$.

> [!example] EJEMPLO
> 
> | $p$ | $q$ | $\neg p$ | $\neg p \lor q$ |
> |:---:|:---:|:--------:|:---------------:|
> |  V  |  V  |    F     |        V        |
> |  V  |  F  |    F     |        F        |
> |  F  |  V  |    V     |        V        |
> |  F  |  F  |    V     |        V        |
> 
> - Primero calculamos $\neg p$.
> - Después aplicamos la disyunción ($\lor$) entre $\neg p$ y $q$.
> - El resultado es verdadero en tres casos y falso en uno.

## EJEMPLO COMPLETO CON TRES VARIABLES

Estudiemos la fórmula $(p \lor q) \land \neg r$. Calcularemos primero $p \lor q$, después $\neg r$ y, finalmente, la conjunción de ambas.

| $p$ | $q$ | $r$ | $p \lor q$ | $\neg r$ | $(p \lor q)\land\neg r$ |
|:---:|:---:|:---:|:----------:|:--------:|:-----------------------:|
|  V  |  V  |  V  |     V      |    F     |            F            |
|  V  |  V  |  F  |     V      |    V     |            V            |
|  V  |  F  |  V  |     V      |    F     |            F            |
|  V  |  F  |  F  |     V      |    V     |            V            |
|  F  |  V  |  V  |     V      |    F     |            F            |
|  F  |  V  |  F  |     V      |    V     |            V            |
|  F  |  F  |  V  |     F      |    F     |            F            |
|  F  |  F  |  F  |     F      |    V     |            F            |

La fórmula es verdadera exactamente cuando **$r$ es falsa** y **al menos una de $p$ y $q$ es verdadera**. Es una contingencia porque algunas filas terminan en V y otras en F.

> [!note] NOTA
> Con muchas variables la tabla crece exponencialmente: cuatro variables requieren $16$ filas, cinco requieren $32$ y diez requieren $1024$. Por eso en lógica y programación se emplean también equivalencias, demostraciones y algoritmos para razonar sin construir una tabla inmensa.

## CLASIFICACIÓN SEGÚN EL VALOR DE VERDAD

- **Tautología:** la columna final siempre contiene **V**.

$$p \lor \neg p$$

- **Contradicción:** la columna final siempre contiene **F**.

$$p \land \neg p$$

- **Contingencia:** la columna final contiene tanto **V** como **F**.

$$p \land q$$

## EQUIVALENCIA LÓGICA

Dos expresiones son **lógicamente equivalentes** cuando sus columnas finales tienen **los mismos valores en todas las filas**; para expresar esto debemos escribir las dos expresiones separadas por una flecha bidireccional con doble línea en el cuerpo de esta.

> [!syntax] SINTAXIS
> 
> $$A \iff B$$

> [!example] EJEMPLO
> 
> Comprobemos la equivalencia entre $p \to q$ y $\neg p \lor q$:
> 
> | $p$ | $q$ | $p \to q$ | $\neg p \lor q$ |
> |:---:|:---:|:---------:|:---------------:|
> |  V  |  V  |     V     |        V        |
> |  V  |  F  |     F     |        F        |
> |  F  |  V  |     V     |        V        |
> |  F  |  F  |     V     |        V        |
> 
> Las dos últimas columnas coinciden, por lo que son equivalentes:
> 
> $$(p \to q) \iff (\neg p \lor q)$$

## VALIDAR ARGUMENTOS CON TABLAS DE VERDAD

Una tabla no solo evalúa expresiones: también permite comprobar si una **inferencia** es válida. Consideremos las premisas $p \to q$ y $p$ y la conclusión $q$.

Formamos la proposición:

$$((p \to q) \land p) \to q$$

Si esta fórmula es una tautología, significa que **en ningún caso** pueden ser verdaderas las dos premisas y falsa la conclusión.

| $p$ | $q$ | $p \to q$ | $(p \to q) \land p$ | $((p \to q) \land p) \to q$ |
|:---:|:---:|:---------:|:-------------------:|:---------------------------:|
|  V  |  V  |     V     |          V          |              V              |
|  V  |  F  |     F     |          F          |              V              |
|  F  |  V  |     V     |          F          |              V              |
|  F  |  F  |     V     |          F          |              V              |

Como la última columna es completamente verdadera, hemos verificado el **modus ponens**.

### CÓMO DETECTAR UNA INFERENCIA INVÁLIDA

Para demostrar que una inferencia **no** es válida, basta encontrar una fila donde **todas las premisas sean verdaderas y la conclusión sea falsa**. Por ejemplo, en la falacia "$p \to q$, $q$; por tanto, $p$", basta tomar $p = \text{F}$ y $q = \text{V}$. Ambas premisas son verdaderas, pero $p$ es falsa.

## EJERCICIOS DE COMPROBACIÓN

1. ¿Cuántas filas necesita una tabla con cinco variables proposicionales distintas?
2. Clasifica $p \land \neg p$.
3. Comprueba si $\neg(p \lor q)$ y $\neg p \land \neg q$ son equivalentes.

> [!abstract] SOLUCIONES
> 1. $2^5 = 32$ filas.
> 2. Contradicción: $p$ y $\neg p$ nunca son verdaderas simultáneamente.
> 3. Sí. Las dos fórmulas tienen la misma columna final para las cuatro combinaciones de $p$ y $q$; es la ley de De Morgan.

## RESUMEN

| OBJETIVO                              | QUÉ COMPROBAR                                          |
|:------------------------------------- |:------------------------------------------------------ |
| **Evaluar una proposición compuesta** | Revisar su columna final.                              |
| **Tautología**                        | Todas las filas son V.                                 |
| **Contradicción**                     | Todas las filas son F.                                 |
| **Contingencia**                      | Hay filas V y F.                                       |
| **Equivalencia lógica**               | Las columnas finales de las dos expresiones coinciden. |

> [!warning] ERRORES FRECUENTES
> - Olvidar combinaciones: con $n$ variables distintas deben aparecer $2^n$ filas.
> - Interpretar $\lor$ como "una u otra, pero no ambas"; en lógica proposicional, la disyunción habitual es **inclusiva**.
> - Creer que $p \to q$ es falsa cuando $p$ es falsa; en lógica clásica, en ese caso es **verdadera**.
> - Confundir una **tautología** con una proposición que solo es verdadera en algunos casos.
