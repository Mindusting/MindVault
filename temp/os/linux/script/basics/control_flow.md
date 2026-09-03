---
aliases: [Control de flujo en Bash Script]
author: Mindusting
corrected: false
creationDate: 2026-05-29 11:02:18
headerFile: false
modificationDate: 2026-05-29 11:03:42
rating: 
tags: [BashScript]
---

# CONTROL DE FLUJO EN BASH SCRIPT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

## CONDICIONALES

Operadores numéricos:

| OPERADOR | DESCRIPCIÓN       |
|:--------:|:----------------- |
|  `-eq`   | Igual a           |
|  `-ne`   | Distinto de       |
|  `-gt`   | Mayor que         |
|  `-ge`   | Mayor o igual que |
|  `-lt`   | Menor que         |
|  `-le`   | Menor o igual que |

Operadores de cadena:

|        OPERADOR         | DESCRIPCIÓN         |
|:-----------------------:|:------------------- |
|       `=` 0 `==`        | Igual a             |
|          `!=`           | Distinto de         |
| `<` o `>` o `\<` o `\>` | Orden lexicográfico |
|          `-z`           | Cadena bacía        |
|          `-n`           | Cadena no bacía     |

```bash
$age=20

if [ "$age" -ge 18 ]
then
    echo "Eres mayor de edad."
else
    echo "Eres menor de edad."
fi
```

## BUCLES

### WHILE

```bash
while [condition]; do [commands]; done
```

### FOR

#### FOR BÁSICO

```bash
for var in [list]; do [commands]; done
```

#### FOR ESTILO C

```bash
for ((i=0; i < 10; i++)); do [commands]; done
```

#### FOR DE RANGO

```bash
for i in {0..10}; do [commands]; done
```

### UNTIL

```bash
until [condition]; do [commands]; done
```
