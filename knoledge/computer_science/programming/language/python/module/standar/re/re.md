---
aliases: [Módolo RE en Python]
author: Mindusting
corrected: false
creationDate: 2026-09-02 06:44:22
headerFile: false
modificationDate: 2026-09-02 06:44:23
rating: 
tags: [Module, Programming, Python, ReGex]
---

# REGEX EN PYTHON

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Documentar el `fullmatch`.
> > - [ ] Documentar el `search`.
> > - [ ] Documentar el `match`.
> > - [ ] Documentar el `split`.
> > - [ ] Documentar el `findall`.
> > - [ ] Documentar el `finditer`.
> > - [ ] Documentar el `sub`.

> [!external-link]- REFERENCIAS WEB
> - [Python](https://docs.python.org/es/3/library/re.html) #WWW/Python
>     - [`fullmatch`](https://docs.python.org/3/library/re.html#re.fullmatch)
>     - [`search`](https://docs.python.org/3/library/re.html#re.search)
>     - [`match`](https://docs.python.org/3/library/re.html#re.match)
>     - [`split`](https://docs.python.org/3/library/re.html#re.split)
>     - [`findall`](https://docs.python.org/3/library/re.html#re.findall)
>     - [`finditer`](https://docs.python.org/3/library/re.html#re.finditer)
>     - [`sub`](https://docs.python.org/3/library/re.html#re.sub)
> - [W3 scools](https://www.w3schools.com/python/python_regex.asp) #WWW/W3Schools
> 
> YouTube:
> - [Corey Schafer](https://youtu.be/K8L6KVGG-7o) #WWW/YT/CoreySchafer
> - [FRIKIdelTO](https://youtu.be/7QUmK6cW_Rg) #WWW/YT/FRIKIdelTO
> - [NeuralNine](https://youtu.be/wnuBwl2ekmo) #WWW/YT/NeuralNine

> [!faq]- FAQ
> - [¿Qué son las expresiones regulares?](../../../../../../text_processing/regex/regex.md)

El [módulo](../../../basic/module.md) **re** en [Python](../../../py.md) es un estandar, ofrece herramientas para poder trabajar con con [expresiones regulares](../../../../../../text_processing/regex/regex.md); esto lo hace mediante una serie de [funciones](../../../basic/function.md) y [clases](../../../basic/oop.md) que veremos en esta documentación.

| FUNCIÓN                             | USO                                       | RESULTADO           |
|:----------------------------------- |:----------------------------------------- |:------------------- |
| [`fullmatch`](#FUNCIÓN%20FULLMATCH) | ¿Coincide todo?                           | `Match` o `None`    |
| [`match`](#FUNCIÓN%20MATCH)         | ¿Coincide al principio?                   | `Match` o `None`    |
| [`search`](#FUNCIÓN%20SEARCH)       | ¿Existe alguna coincidencia?              | `Match` o `None`    |
| [`findall`](#FUNCIÓN%20FINDALL)     | Dame todas las coincidencias.             | `list`              |
| [`finditer`](#FUNCIÓN%20FINDITER)   | Dame todas las coincidencias con detalle. | Iterador de `Match` |
| [`split`](#FUNCIÓN%20SPLIT)         | Separa por las coincidencias.             | `list`              |
| [`sub`](#FUNCIÓN%20SUB)             | Sustitulle las coincidencias.             | `str`               |

> [!important] IMPORTANTE
> Aunque en esta documentación todo el rato de operar sobre [*strings*](../../../py_str.md) a la hora de encontrar los patrones, realmente también se puede usar [*bytes*](../../../py_bytes.md).

## FUNCIÓN FULLMATCH

La [función](../../../basic/function.md) `fullmatch` se usa para poder comprobar si un [*string*](../../../py_str.md) coincide de forma completa con el patrón con el que lo estemos comparando.

> [!syntax] SINTAXIS
> fullpath([***\[pattern\]***](#^fullmatch-arg-pattern), [***\[string\]***](#^fullmatch-arg-string), [***\{flags\}***](#BANDERAS%20(FRAGS)))

- ***pattern***: (*obligatorio*) es la parte que define la [expresión regular](../../../../../../text_processing/regex/regex.md) que se debe cumplir en todo el [*string*](#^fullmatch-arg-string).
^fullmatch-arg-pattern
- ***string***: (*obligatorio*) es el string sobre el que se va a hacer la comprobación de si el patrón coincide por completo.
^fullmatch-arg-string
- ***flags***: este argumento es opcional y lo sufucientemente complejo como para tener su propio apartado "[BANDERAS (FLAGS)](#BANDERAS%20(FRAGS))".

---

> [!example] EJEMPLO
> Supongamos que tenemos que guardar una fecha con el formato `YYYY-MM-DD`, es decir: cuatro dígitos para el año (`YYYY`), dos dígitos para el mes (`MM`) y dos dígitos para el día (`DD`); sigiendo ese mismo orden y usando un guión (`-`) para separar estos valores, para poder hacer esto podremos usar el patrón `\d{4}-\d\d-\d\d` de la siguiente forma.

```python
import re

pattern: str = r"\d{4}-\d\d-\d\d"
date: str = "2026-09-02"

result: re.Match | None = re.fullmatch(pattern, date)

# Se comprueba si existe una coincidencia o no
if result:
    print("La fecha es válida!")
else:
    print("La fecha es inválida!")
```

Puedes cambiar la fecha y ver como se comporta el programa.

## FUNCIÓN MATCH

La [función](../../../basic/function.md) `match` se usa para poder comprobar si un [*string*](../../../py_str.md) comienza con el patrón con el que lo estamos comparando.

> [!syntax] SINTAXIS
> fullpath([***\[pattern\]***](#^match-arg-pattern), [***\[string\]***](#^match-arg-string), [***\{flags\}***](#BANDERAS%20(FRAGS)))

- ***pattern***: (*obligatorio*) es la parte que define la [expresión regular](../../../../../../text_processing/regex/regex.md) que se debe cumplir en todo el [*string*](#^fullmatch-arg-string).
^match-arg-pattern
- ***string***: (*obligatorio*) es el string sobre el que se va a hacer la comprobación de si el patrón coincide por completo.
^match-arg-string
- ***flags***: este argumento es opcional y lo sufucientemente complejo como para tener su propio apartado "[BANDERAS (FLAGS)](#BANDERAS%20(FRAGS))".

---

> [!example] EJEMPLO

## FUNCIÓN SEARCH

## FUNCIÓN FINDALL

## FUNCIÓN FINDITER

## FUNCIÓN SPLIT

## FUNCIÓN SUB

## CLASE MATCH

## BANDERAS (FRAGS)

Las banderas en son opcionales y debido a su complegidad estas tienen su propio apartado (*es decir, este*) en el que se detalla las características de estas, ya que además son comunes para todas las [funciones](../../../basic/function.md).

---
---
---
---
---

## COMO ESCRIBIR UNA REGEX

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Explicar como se escriben los regex en Python.
> > - [ ] Añadir un enlace al archivo de regex.

Para poder escribir el **patrón** de una [expresión regular](../../../../../../text_processing/regex/regex.md) se utiliza [`r-str`](py_str.md#R-STRING) ya que este nos permite escribir los caracteres de escape de forma que el interprete del padrón podrá leerlos, es puede hacer si el [`r-str`](py_str.md#R-STRING) 

## COINCIDENCIA COMPLETA

Para comprobar si un texto completo coincide con el patrón se utiliza la [función](py_func.md) `fullmatch`, esta devuelve un [objeto](py_class.md) de tipo [`Match`](#CLASE%20MATCH) cuando coincide o un `None` cuando no.

> [!abstract] SINTAXIS
> match(***\[pattern\]***, ***\[string\]***, ***[\{flags\}](#FLAGS)***)

## COINCIDE

> [!abstract] SINTAXIS
> match(***\[pattern\]***, ***\[string\]***, ***[\{flags\}](#FLAGS)***)

- ***pattern***: (*obligatorio*) es la [expresión regular](#REGEX) para dividir el [*strings*](py_str.md).
- ***string***: (*obligatorio*) es el [texto](py_str.md) que va a ser dividido.
- ***flags***: [banderas](#FLAGS) a aplicar sobre el proceso.

## ENCONTRAR TODO

La [función](py_func.md) `findall` devuelve una [lista](py_list.md) con [strings](py_str.md), siendo estos un extracto del [strings](py_str.md) original, el criterio para encontrarlo se indica en *pattern* con una [expresión regular](#REGEX).

- Es el inverso de [`split`](#TROCEADO).
- Si no se encuentra ninguna coincidencia, devuelve una [lista](py_list.md) vacía.

> [!abstract] SINTAXIS
> findall(***\[pattern\]***, ***\[string\]***, ***[\{flags\}](#FLAGS)***)

- ***pattern***: (*obligatorio*) es la [expresión regular](#REGEX) para dividir el [*strings*](py_str.md).
- ***string***: (*obligatorio*) es el [texto](py_str.md) que va a ser dividido.
- ***flags***: [banderas](#FLAGS) a aplicar sobre el proceso.

```python
pattern:  str = r"\d{4}(?:(?:/|-)\d{2}){2}(?: |T)\d\d(?::\d\d){2}"
string:   str = """\
2015/05/21
2008/06/07 11:49:16
2007-05-01T01:16:41
2002-02-19
"""

matches = re.findall(pattern, string)

for match in matches:
    print(match)
# SALIDA:
# 2008/06/07 11:49:16
# 2007-05-01T01:16:41
```

## TROCEADO

La [función](py_func.md) `split` devuelve una [lista](py_list.md) con [strings](py_str.md), siendo estos un extracto del [strings](py_str.md) original, el criterio para dividirlo se indica en *pattern* con una [expresión regular](#REGEX).

- Es el inverso de [`findall`](#ENCONTRAR%20TODO).

> [!abstract] SINTAXIS
> split(***\[pattern\]***, ***\[string\]***, ***\{maxsplit\}***, ***[\{flags\}](#FLAGS)***)

- ***pattern***: (*obligatorio*) es la [expresión regular](#REGEX) para dividir el [*strings*](py_str.md).
- ***string***: (*obligatorio*) es el [texto](py_str.md) que va a ser dividido.
- ***maxsplit***: (*por defecto es 0*) indica el número de veces que se de aplicar el corte, di forma que si indicamos 1, solo se aplicará al primer *pattern* que coincida, aunque después haya otros, si se indica 0, se aplica a todos los *pattern* que se encuentren.
- ***flags***: [banderas](#FLAGS) a aplicar sobre el proceso.

```python
import re

pattern:  str = r"\n\n"
string:   str = """\
Este es un texto de prueba
creado por Mindusting.

Esto es un segundo párrafo
creado para demostar que se
separan.
"""
maxsplit: int = 0

paragraphs = re.split(pattern, string, maxsplit)

print(paragraphs)

for i, paragraph in enumerate(paragraphs):
    print(f"El párrafo {i + 1} es:")
    print(f"{paragraph}\n")
# SALIDA:
# El párrafo 1 es:
# Este es un texto de prueba
# creado por Mindusting.
# 
# El párrafo 2 es:
# Esto es un segundo párrafo
# creado para demostar que se
# separan.
```

## SUSTITUCIÓN

La [función](py_func.md) `sub` sustituye los patrones que encuentre en el texto que le proveamos por otro que también le tendremos que proveer.

> [!abstract] SINTAXIS
> sub(***\[pattern\]***, ***\[repl\]***, ***\[string\]***, ***\{counts\}***, ***[\{flags\}](#FLAGS)***)

- ***pattern***: (*obligatorio*) es al [expresión regular](#REGEX).
- ***repl***: (*obligatorio*) es el [string](py_str.md) que por el que va a ser sustituida las coincidencias del ***pattern***.
- ***string***: (*obligatorio*) es el texto sobre el que se va a trabajar.
- ***counts***: (*por defecto es 0*) indica el número de veces que debe aplicar la sustitución, de forma que si ponemos un 1, solo se aplicará a la primera coincidencia que se encuentre, si se pone 0, se aplica a todas las opciones.
- ***flags***: [banderas](#FLAGS) a aplicar sobre el proceso.

```python
import re

pattern: str = r"\d{4}(?:(?:/|-)\d{2}){2}"
repl:    str = "2024-12-27"
string:  str = """\
Este es un texto de prueba creado por Mindusting
este va a ser usado para sustituir la fecha actual,
siendo esta 1984/01/01.

Sin embargo, somo he indicado que solo se debe hacer
con la primera coincidencia, la fecha 1969/07/21 no
va a ser modificada.
"""
counts:  int = 1

string = re.sub(pattern, repl, string, counts)

print(string)
# SALIDA:
# Este es un texto de prueba creado por Mindusting
# este va a ser usado para sustituir la fecha actual,
# siendo esta 2024-12-27.
# 
# Sin embargo, somo he indicado que solo se debe hacer
# con la primera coincidencia, la fecha 1969/07/21 no
# va a ser modificada.
```

## FLAGS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Explicar las banderas.

https://docs.python.org/3/library/re.html#flags
