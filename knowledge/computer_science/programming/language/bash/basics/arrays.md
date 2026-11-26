---
aliases: ["Arrays en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25
headerFile: false
modificationDate: 2026-11-25
rating:
tags: [Programming, BashScript, OS/Linux/BASH]
---

# ARRAYS EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Arrays.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Comillas y caracteres de escape en bash](quoting.md)
> - [Bucles en bash](loop.md)
> - [Lectura y escritura de archivos en bash](../io/reading_files.md)

## DEFINICIÓN

Un array agrupa varios valores bajo un mismo nombre. Bash permite arrays indexados (índices enteros) y asociativos (claves de texto, desde Bash 4). No es necesario que los índices sean consecutivos.

> [!abstract] SINTAXIS
> ```bash
> array=(value1 value2)
> array[0]=value3
> printf '%s\n' "${array[0]}"
> ```

## ARRAYS INDEXADOS

```bash
fruits=('manzana' 'pera verde' 'naranja')
fruits+=('uva')
printf '%s\n' "${fruits[1]}" # pera verde
printf '%s\n' "${#fruits[@]}" # 4
for fruit in "${fruits[@]}"; do
    printf '%s\n' "$fruit"
done
unset 'fruits[1]'
```

`unset` elimina el elemento, pero no desplaza los índices restantes. Las comillas de `unset 'fruits[1]'` impiden que el argumento se trate como patrón de archivo. `${!fruits[@]}` expande los índices existentes.

## ARRAYS ASOCIATIVOS

```bash
declare -A ports=([ssh]=22 [http]=80)
ports[https]=443
printf '%s\n' "${ports[ssh]}"
for service in "${!ports[@]}"; do
    printf '%s: %s\n' "$service" "${ports[$service]}"
done
```

No dependas del orden de recorrido de un array asociativo. Sus claves no pueden estar vacías.

## EXPANSIÓN DE ELEMENTOS

| SINTAXIS         | SIGNIFICADO                                              |
|:---------------- |:-------------------------------------------------------- |
| `"${array[@]}"`  | Cada elemento como argumento independiente.              |
| `"${array[*]}"`  | Todos juntos, separados por el primer carácter de `IFS`. |
| `${#array[@]}`   | Número de elementos.                                     |
| `"${!array[@]}"` | Índices o claves.                                        |

```bash
options=(-l -a)
ls "${options[@]}" -- "$HOME"
```

> [!important] NOTAS
> No uses `array=($(command))` para leer líneas: divide el resultado en palabras y expande comodines. Usa `mapfile -t` o un bucle `read` según el caso. Los arrays no se exportan como arrays al entorno de otros programas.
