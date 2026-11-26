---
aliases: ["Bucles en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:48:41
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# BUCLES EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Arrays en bash](arrays.md)
> - [Patrones y expresiones regulares en bash](patterns.md)
> - [Lectura y escritura de archivos en bash](../io/reading_files.md)

## DEFINICIÓN

Un bucle repite instrucciones. Bash proporciona `for`, `while` y `until`, además de `break` y `continue` para modificar el flujo.

## FOR

> [!abstract] SINTAXIS
> 
> ```bash
> for variable in values; do
>     commands
> done
> ```

```bash
for name in 'Ana García' Luis Marta; do
    printf '%s\n' "$name"
done

for i in {1..3}; do
    printf '%d\n' "$i"
done
```

Para límites calculados durante la ejecución, usa un bucle aritmético:

```bash
limit=3

for ((i=0; i<limit; i++)); do
    printf '%d\n' "$i"
done
```

## WHILE Y UNTIL

```bash
counter=0

while (( counter < 3 )); do
    printf '%d\n' "$counter"
    counter=$((counter + 1))
done

until (( counter == 0 )); do
    counter=$((counter - 1))
done
```

`while` repite mientras la condición devuelve 0; `until` repite mientras devuelve un estado no nulo. Ambos pueden ejecutar el cuerpo cero veces.

## BREAK Y CONTINUE

```bash
for i in {1..10}; do
    if (( i == 5 )); then
        break
    fi

    if (( i % 2 == 0 )); then
        continue
    fi

    printf '%d\n' "$i"
done
# 1
# 3
```

`break` termina el bucle; `continue` pasa a la siguiente iteración. En bucles anidados, `break 2` sale de dos niveles. `while true; do...; done` permite crear un bucle indefinido, pero debe tener una salida o una espera razonable.

## RECORRER ARCHIVOS

```bash
for file in ./*.txt; do
    [[ -f $file ]] || continue
    printf '%s\n' "$file"
done
```

Por defecto, un patrón sin coincidencias permanece literal. No recorras los resultados de `ls` mediante `for file in $(ls)`, pues perderías la separación correcta de nombres.
