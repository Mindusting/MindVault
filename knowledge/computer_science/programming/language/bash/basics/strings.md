---
aliases: ["Cadenas de texto en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:51:08
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# CADENAS DE TEXTO EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Parameter-Expansion.html) #WWW/GNU

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Expansión de parámetros en bash](parameter_expansion.md)
> - [Condicionales en bash](conditionals.md)
> - [Entrada y salida en bash](input_output.md)

## DEFINICIÓN

Una cadena (*string*) es una secuencia de caracteres. Se puede concatenar texto, comprobar su longitud y transformarlo mediante expansiones de parámetros.

## CONCATENACIÓN

```bash
first='Hola'
second='mundo'
message="$first $second"
message+='!!!'
printf '%s\n' "$message"
```

## OPERACIONES

```bash
text='Hola Mundo'
printf '%s\n' "${#text}"     # 10
printf '%s\n' "${text:0:4}"  # Hola
printf '%s\n' "${text,,}"    # hola mundo
printf '%s\n' "${text^^}"    # HOLA MUNDO
printf '%s\n' "${text// /_}" # Hola_Mundo
```

Las transformaciones de mayúsculas y minúsculas dependen de la configuración regional. `${text,,}` y `${text^^}` requieren Bash 4 o posterior.

## COMPARACIÓN

```bash
name='Ana García'
if [[ -n $name && $name == 'Ana García' ]]; then
    printf 'Coincide\n'
fi
```

`-n` comprueba que la cadena no esté vacía; `-z` comprueba lo contrario. Dentro de `[[ ]]`, el operando derecho de `==` puede ser un patrón si no está entrecomillado.

## FORMATEO

```bash
printf -v message 'Nombre: %s | ID: %04d' 'Ana' 7
printf '%s\n' "$message"
# Nombre: Ana | ID: 0007
```

`printf -v` guarda el resultado en una variable sin imprimirlo. Para datos externos, mantén el formato fijo y pasa el texto como argumento.
