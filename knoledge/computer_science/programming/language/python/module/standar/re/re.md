---
aliases: [Módolo RE en Python]
author: Mindusting
corrected: false
creationDate: 2026-09-02 06:44:22
headerFile: false
modificationDate: 2026-09-05 03:28:26
rating: 
tags: [Module, Programming, Python, ReGex]
---

# REGEX EN PYTHON

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [x] Documentar el `fullmatch`.
> > - [x] Documentar el `match`.
> > - [x] Documentar el `search`.
> > - [ ] Documentar el `findall`.
> > - [ ] Documentar el `finditer`.
> > - [ ] Documentar el `split`.
> > - [ ] Documentar el `sub`.
> > - [ ] Documentar las *flags*.
> > - [ ] Documentar la clase `Match`.

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

El [módulo](../../../basic/module.md) **re** en [Python](../../../py.md) es un estandar, ofrece herramientas para poder trabajar con con [expresiones regulares](regex.md); esto lo hace mediante una serie de [funciones](../../../basic/function.md) y [clases](../../../basic/oop.md) que veremos en esta documentación.

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

La [función](../../../basic/function.md) `fullmatch` se usa para poder comprobar si un [*string*](../../../py_str.md) **coincide de forma completa** con el patrón con el que lo estemos comparando.

Si todo el texto coincide, esta [función](../../../basic/function.md) nos devolverá un [objeto](../../../basic/oop.md) de tipo [`Match`](#CLASE%20MATCH), sino nos devolverá [`None`](../../../basic/none.md).

> [!syntax] SINTAXIS
> fullpath([***\[pattern\]***](#^fullmatch-arg-pattern), [***\[string\]***](#^fullmatch-arg-string), [***\{flags\}***](flags.md))

- ***pattern***: (*obligatorio*) es la parte que define la [expresión regular](regex.md) que se debe cumplir en todo el [*string*](#^fullmatch-arg-string).
^fullmatch-arg-pattern
- ***string***: (*obligatorio*) es el string sobre el que se va a hacer la comprobación de si el patrón coincide por completo.
^fullmatch-arg-string
- ***flags***: este argumento es opcional y lo sufucientemente complejo como para tener su propio apartado sobre [*flags*](flags.md).

---

> [!example] EJEMPLO
> Supongamos que tenemos que guardar una fecha con el formato `YYYY-MM-DD`, es decir: cuatro dígitos para el año (`YYYY`), dos dígitos para el mes (`MM`) y dos dígitos para el día (`DD`); sigiendo ese mismo orden y usando un guión (`-`) para separar estos valores, para poder hacer esto podremos usar el patrón `\d{4}-\d\d-\d\d` de la siguiente forma.

```python
import re

pattern: str = r"\d{4}-\d\d-\d\d"
date: str = "2026-09-02"

result: re.Match | None = re.fullmatch(pattern, date)

if result:
    print("La fecha es válida!")
else:
    print("La fecha es inválida!")

# SALIDA:
# La fecha es válida!
```

Puedes cambiar la fecha y ver como se comporta el programa.

## FUNCIÓN MATCH

La [función](../../../basic/function.md) `match` se usa para poder comprobar si un [*string*](../../../py_str.md) **comienza** con el patrón con el que lo estamos comparando.

Si se encuentra una coincidencia al principio, esta [función](../../../basic/function.md) nos devolverá un [objeto](../../../basic/oop.md) de tipo [`Match`](#CLASE%20MATCH), sino nos devolverá [`None`](../../../basic/none.md).

> [!syntax] SINTAXIS
> fullpath([***\[pattern\]***](#^match-arg-pattern), [***\[string\]***](#^match-arg-string), [***\{flags\}***](flags.md))

- ***pattern***: (*obligatorio*) es la parte que define la [expresión regular](regex.md) que se debe cumplir en todo el [*string*](#^fullmatch-arg-string).
^match-arg-pattern
- ***string***: (*obligatorio*) es el string sobre el que se va a hacer la comprobación de si el patrón coincide por completo.
^match-arg-string
- ***flags***: este argumento es opcional y lo sufucientemente complejo como para tener su propio apartado sobre [*flags*](flags.md).

---

> [!example] EJEMPLO
> Imaginemos que queremos tener un programa que debe administrar una lista de productos, estos deben de estar identificados por un nombre, pero este nombre no puede estar hecho de cualquier forma, queremos que este empiece por un número de tres dígitos, un guión y a partír de ahí lo que queramos; para ello podremos usar esta [función](../../../basic/function.md), ya que lo que tendremos que hacer es comprobar si el inicio del nombre coincide con el patrón `\d{3}-`.

```python
import re

pattern: str = r"\d{3}-"
name: str = "123-Engranage"

result: re.Match | None = re.match(pattern, name)

if result:
    print("El nombre es valido!")
else:
    print("El nombre es inválido!")

# SALIDA:
# El nombre es válido!
```

Puedes cambiar el nombre y ver como se comporta el programa.

## FUNCIÓN SEARCH

La [función](../../../basic/function.md) `search`, a diferencia de [`match`](#FUNCIÓN%20MATCH) en donde busca la coincidencia del patrón al principio del [*string*](../../../py_str.md), esta busca la **primera coincidencia** independientemente de la posición en la que se encuentre dentro de [*string*](../../../py_str.md).

Si se encuentra una coincidencia, esta [función](../../../basic/function.md) nos devolverá un [objeto](../../../basic/oop.md) de tipo [`Match`](#CLASE%20MATCH), sino nos devolverá [`None`](../../../basic/none.md).

> [!syntax] SINTAXIS
> search([***\[pattern\]***](#^search-arg-pattern), [***\[string\]***](#^search-arg-string), [***{flags}***](flags.md))

- ***pattern***: (*obligatorio*) es la parte que define la [expresión regular](regex.md) que se quiere buscar dentro del [*string*](#^search-arg-string).
  ^search-arg-pattern
- ***string***: (*obligatorio*) es el string sobre el que se va a buscar la primera coincidencia.
  ^search-arg-string
- ***flags***: este argumento es opcional y lo sufucientemente complejo como para tener su propio apartado sobre [*flags*](flags.md).

---

> [!example] EJEMPLO
> Imaginemos que tenemos un texto y queremos encontrar la primera fecha que aparece dentro de este, para ello podemos hacerlo como en el siguiente ejemplo, pero hay que tener una cosa clara, solo obtendremos la primera fecha.

```python
import re

pattern: str = r"\d{4}-\d\d-\d\d"
text: str = "Empecé a programar al rededor de 2020-10-15 y estoy escribiendo esto en 2026-09-05."

result: re.Match | None = re.search(pattern, text)

if result:
    print(f"Fecha encontrada: {result.group()}")
else:
    print("No se ha encontrado ninguna fecha.")

# SALIDA:
# Fecha encontrada: 2020-10-15
```

Como se puede ver en el ejemplo a pesar de que haya dos fechas en el texto, solo obtenemos la primera.

## FUNCIÓN FINDALL

La [función](../../../basic/function.md) `findall` se usa para obtener **todas las coincidencias** de un patrón dentro de un [*string*](../../../py_str.md), esta nos las devolverá en el orden en las que las ha ido encontrando.

Esta [función](../../../basic/function.md) devuelve una [lista](../../../py_list.md), esta puede contener [*strings*](../../../py_str.md) o [tuplas](../../../py_tuple.md), dependiendo de la catidad de grupos que contenga el patrón que estamos aplicando; si solo tiene un grupo tendrá [*strings*](../../../py_str.md) sino [tuplas](../../../py_tuple.md).

> [!syntax] SINTAXIS
> search([***\[pattern\]***](#^search-arg-pattern), [***\[string\]***](#^search-arg-string), [***{flags}***](flags.md))

- ***pattern***: (*obligatorio*) es la parte que define la [expresión regular](regex.md) que se quiere buscar dentro del [*string*](#^search-arg-string).
  ^findall-arg-pattern
- ***string***: (*obligatorio*) es el string sobre el que se va a buscar la primera coincidencia.
  ^findall-arg-string
- ***flags***: este argumento es opcional y lo sufucientemente complejo como para tener su propio apartado sobre [*flags*](flags.md).

---

> [!example] EJEMPLO
> Imaginemos que queremos obtener todas las fechas de un texto; podemos hacerlo usando el patrón de la fecha (`\d{4}-\d\d-\d\d`) y como se puede ver en el ejemplo, terminamos obteniendo las dos fechas.

```python
import re

text: str = """\
Este es un texto que estoy
escribiendo el día 2026-09-06.

Como podeis ver me lo estoy
tomando con calma ya que el
anterior apartado lo redacte
ayer (2026-09-05).
"""

pattern: str = r"\d{4}-\d\d-\d\d"

dates = re.findall(pattern, text)

print(dates)

# SALIDA:
# ['2026-09-06', '2026-09-05']
```

---

> [!example] EJEMPLO
> Ahora imaginemos que queremos obtener la fecha y en caso de que lo haya, también la hora; este ejemplo es un poco más complicado ya que contendrá grupos, por lo que en la [lista](../../../py_list.md) tendremos [tuplas](../../../py_tuple.md) en vez de [*strings*](../../../py_str.md).

```python
import re

text: str = """\
Lanzamiento: 1969-07-16
Alunizaje: 1969-07-20 20:17:00
Primer paso humano: 1969-07-21 02:56:00
Retorno a la Tierra: 1969-07-24
"""

pattern: str = r"(\d{4}-\d\d-\d\d)(?:\s(\d\d(?:\:\d\d){2}))?"

dates = re.findall(pattern, text)

for date in dates:
    print(date)

# SALIDA:
# ('1969-07-16', '')
# ('1969-07-20', '20:17:00')
# ('1969-07-21', '02:56:00')
# ('1969-07-24', '')
```

Como se puede ver en el ejemplo, en los casos en los que encuentra una fecha sin hora, obtenemos la [tupla](../../../py_tuple.md) teniendo como primer elemento la propia fecha mientras que el segundo elemento se queda vacío; por otro lado, si la fecha incluye la hora, esta aparecerá como segundo elemento.

## FUNCIÓN FINDITER

## FUNCIÓN SPLIT

## FUNCIÓN SUB

## CLASE MATCH

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

Para poder escribir el **patrón** de una [expresión regular](regex.md) se utiliza [`r-str`](py_str.md#R-STRING) ya que este nos permite escribir los caracteres de escape de forma que el interprete del padrón podrá leerlos, es puede hacer si el [`r-str`](py_str.md#R-STRING) 

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
