---
author: Mindusting
corrected: false
tags:
  - Programming
  - Python
  - Class
  - Method
title: Métodos en Python
---

# MÉTODOS EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [x] Documentar los métodos estáticos.
> > - [x] Documentar los métodos de clase.
> > - [ ] Documentar los métodos de instancia.
> > - [ ] Documentar los métodos como propiedad.
> > - [ ] Documentar los métodos mágicos.
> >     - [ ] Documentar `__new__`.
> >         - [ ] Añadir enlace y explicación a la documentación del "singleton".

> [!help]- REFERENCIAS WEB
> YouTube:
> - [pildorasinformaticas](https://youtu.be/Y_SiIgxc-xI) #WWW/YT/pildorasinformaticas

Un **método** es una [función](../py_func.md) que se encuentra en el ámbito de una [clase](../py_class.md), al estar dentro de esta última, el nombre que se le da es “**método**” en vez de [función](../py_func.md), esto es debido a que así es más fácil diferenciar cuando nos referimos a si está dentro o fuera de una [clase](../py_class.md).

A diferencia de otros lenguajes de programación orientados a objetos, en Python existen tres tipos de **métodos** en vez de dos, esto es debido a que los "estáticos" se separan en dos versiones:

En Python tenemos **cinco tipos de métodos**, podremos elegir el tipo dependiendo de nuestras necesidades:

- [Métodos estáticos](#MÉTODOS%20ESTÁTICOS)
- [Métodos de clase](#MÉTODOS%20DE%20CLASE)
- [Métodos de instancia](#MÉTODOS%20DE%20INSTANCIA)
- [Métodos como propiedad](#MÉTODOS%20COMO%20PROPIEDAD)
- [Métodos mágicos](#MÉTODOS%20MÁGICOS)

## MÉTODOS ESTÁTICOS

Para crear un **método** estático en Python se hace de la misma forma que con una [función](../py_func.md) solo que en el ámbito de la [clase](../py_class.md), de todas formas esta no es una buena práctica, ya que se tendría que hacer añadiendo le el decorador `@staticmethod`:

> [!success]- FORMA CORRECTA
> ```python
> class Trig(object):
> 
>     @staticmethod
>     def pitagoras(dx: float, dy: float) -> float:
>         return ((dx * dx) + (dy * dy)) ** 0.5
> ```

> [!failure]- FORMA INCORRECTA
> ```python
> class Trig(object):
> 
>     def pitagoras(dx: float, dy: float) -> float:
>         return ((dx * dx) + (dy * dy)) ** 0.5
> ```

Este tipo de **métodos** no tienen acceso a **atributos** no a otros **métodos** de la [clase](../py_class.md), únicamente pueden recibir **argumentos**, operar con ellos y/o devolver valores.

Aun que sea de tipo *estático*, se puede acceder tanto desde la [clase](../py_class.md) como desde las instancias de esta:

```python
class Trig(object):

    @staticmethod
    def pitagoras(dx: float, dy: float) -> float:
        return ((dx * dx) + (dy * dy)) ** 0.5


trig: Trig = Trig()

print(Trig.pitagoras(3.0, 4.0)) # <- Clase
print(trig.pitagoras(3.0, 4.0)) # <- Objeto
# SALIDA:
# 5.0
# 5.0
```

## MÉTODOS DE CLASE

Para crear un **método** de [clase](../py_class.md) en Python se hace de la misma forma que con una [función](../py_func.md) solo que en el ámbito de la [clase](../py_class.md), a su vez, este requiere que le indiquemos que es un **método** de [clase](../py_class.md) haciendo uso del decorador `@classmethod`, estos además siempre reciben como primer argumento la propia [clase](../py_class.md), es un estándar llamarlo `cls` (*abreviación de "class"*), este nos permitirá acceder a las propiedades y otros **métodos** de la [clase](../py_class.md):

> [!success]- FORMA CORRECTA
> Los **métodos** sí tienen el primer argumento `cls`.
> ```python
> class Trig:
> 
>     degree_in_radians: float = 0.017453292519943295
>     radian_in_degrees: float = 57.29577951308232
> 
>     @classmethod
>     def to_degrees(cls, radians: float) -> float:
>         # Se accede a la propiedad con la clase.
>         #                 v
>         return radians * cls.radian_in_degrees
> 
>     @classmethod
>     def to_radians(cls, degrees: float) -> float:
>         # Se accede a la propiedad con la clase.
>         #                 v
>         return degrees * cls.degree_in_radians
> ```

> [!failure]- FORMA INCORRECTA
> Los **métodos** no tienen el primer argumento `cls`.
> ```python
> class Trig:
> 
>     degree_in_radians: float = 0.017453292519943295
>     radian_in_degrees: float = 57.29577951308232
> 
>     @classmethod
>     def to_degrees(radians: float) -> float:
>         return radians * radian_in_degrees
> 
>     @classmethod
>     def to_radians(degrees: float) -> float:
>         return degrees * degree_in_radians
> ```

Este tipo de **métodos**  tienen acceso a **atributos** y a otros **métodos** de la [clase](../py_class.md) a trabes de la referencia a esta (`cls`).

Aun que sea de tipo de *clase*, se puede acceder tanto desde la [clase](../py_class.md) como desde las instancias de esta:

```python
class Trig:

    degree_in_radians: float = 0.017453292519943295
    radian_in_degrees: float = 57.29577951308232

    @classmethod
    def to_degrees(cls, radians: float) -> float:
        return radians * cls.radian_in_degrees

    @classmethod
    def to_radians(cls, degrees: float) -> float:
        return degrees * cls.degree_in_radians


trig: Trig = Trig()

print(Trig.to_degrees(2.5)) # <- Clase
print(trig.to_degrees(2.5)) # <- Objeto
print(Trig.to_radians(45))  # <- Clase
print(trig.to_radians(45))  # <- Objeto
# SALIDA:
# 143.2394487827058
# 143.2394487827058 
# 0.7853981633974483
# 0.7853981633974483
```

## MÉTODOS DE INSTANCIA

Para crear un **método** de instancia en Python se hace de la misma forma que con una [función](../py_func.md) solo que en el ámbito de la [clase](../py_class.md), estos además siempre reciben como primer argumento la propia instancia, es un estándar llamarlo `self`, este nos permitirá acceder a las propiedades y otros **métodos** de la instancia:

---

Este tipo de **métodos**  tienen acceso a **atributos** y a otros **métodos** de la [clase](../py_class.md) a trabes de la referencia a esta (`cls`).

Aun que sea de tipo de *clase*, se puede acceder tanto desde la [clase](../py_class.md) como desde las instancias de esta:

## MÉTODOS COMO PROPIEDAD

```python
from datetime import date


class User(object):

    def __init__(self, name: str, birthdate: date):
        self.name:      str  = name
        self.birthdate: date = birthdate

    def years(self) -> int:
        t = date.today()
        b = self.birthdate
        return t.year-b.year-(
            (t.month,t.day)<(b.month,b.day)
        )


user = User("Adelio", date(1984, 1, 1))

print(user.years()) # <- Objeto
# SALIDA:
# 41

print(User.years()) # <- Clase
# Da una excepción
```

## MÉTODOS MÁGICOS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [geeksforgeeks](https://www.geeksforgeeks.org/dunder-magic-methods-python/)
> 
> YouTube:
> - [mCoding (`__new__` vs `__init__`)](https://youtu.be/-zsV0_QrfTw)

> [!warning] WARNING
> Existe una diferencia sustancial entre los métodos `__div__`, `__truediv__` y `__floordiv__`.
> 
> La diferencia es que `__div__` es el usado para Python2, mientras qué `__truediv__` y `__floordiv__` son para Python3.
> 
> [FUENTES](https://stackoverflow.com/questions/29155829/operator-overloading-for-truediv-in-python)

### CONSTRUCTORES Y DESTRUCTORES

- `__new__`
- `__init__`
- `__del__`

### NUMÉRICO

- `__trunc__` (`math.trunc()`)
- `__ceil__` (`math.ceil()`)
- `__floor__` (`math.floor()`)
- `__round__` (`round()`)
- `__invert__` (`~`)
- `__abs__` (`abs()`)
- `__neg__` (`-[class]`)
- `__pos__` (`+[class]`)

### ARITMÉTICO

- `__add__` (`[class] + [class]`)
- `__sub__` (`[class] - [class]`)
- `__mul__` (`[class] * [class]`)
- `__div__` (`[class] / [class]` in `Python2`)
- `__truediv__` (`[class] / [class]` in `Python3`)
- `__floordiv__` (`[class] // [class]` in `Python3`)
- `__mod__` (`[class] % [class]`)
- `__divmod__` (`divmod([class], [class])`)
- `__pow__` (`[class] ** [class]`)
- `__lshift__` (`[class] << [class]`)
- `__rshift__` (`[class] >> [class]`)
- `__and__` (`[class] & [class]`)
- `__or__` (`[class] | [class]`)
- `__xor__` (`[class] ^ [class]`)
- `__matmul__` (`[class] @ [class]`)

Todos estos tienen su propia variante con una `r` por delante para transformar el `[class] + [class]` en `[class] += [class]`.

## STRING

- `__str__` (`str([class])`)
- `__repr__` (`repr([class])`)
- `__unicode__` (`__str__` unicode version)
- `__format__` (New style of string)
- `__hash__` (`hash([class])`)
- `__nonzero__` (`bool([class])`)
- `__dir__` (Return a list of atributes of the class)
- `__sizeof__` (It returns the size of the object)

## COMPARACIÓN

- `__eq__` (`[class] == [class]`)
- `__ne__` (`[class] != [class]`)
- `__lt__` (`[class] < [class]`)
- `__gt__` (`[class] > [class]`)
- `__le__` (`[class] <= [class]`)
- `__ge__` (`[class] >= [class]`)

## ITERABLES

`__iter__` (`list([class])`, `tuple([class])`, ...)

## CRUD

```python
def main() -> None:
    c = C()
    c[1:2, 3]
    c[1:2, 3] = 1
    del c[1:2, 3]


class C:
    def __getitem__(self, key):
        print(f"GET: {key}")

    def __setitem__(self, key, value):
        print(f"SET: {key}; {value}")

    def __delitem__(self, key):
        print(f"DEL: {key}")


if "__main__" == __name__:
    main()
```

## EXAMPLE

```python
class Color:
    def __init__(self):
        pass

    def _on_8bit_bounds(self, number: int) -> bool:
        return 0 <= number and number <= 255


class RGBColor(Color):
    def __init__(self, red: int, green: int, blue: int):
        super().__init__()

        if not isinstance(red, int):
            raise ValueError("red must be int")
        if not isinstance(green, int):
            raise ValueError("green must be int")
        if not isinstance(blue, int):
            raise ValueError("blue must be int")

        if not self._on_8bit_bounds(red):
            raise ValueError("red must be between 0 and 255")
        if not self._on_8bit_bounds(green):
            raise ValueError("green must be between 0 and 255")
        if not self._on_8bit_bounds(blue):
            raise ValueError("blue must be between 0 and 255")

        self._red   = red
        self._green = green
        self._blue  = blue

    @classmethod
    def from_hex(cls, value: str):
        if not isinstance(value, str):
            raise ValueError("value must be str")

        if value is None or len(value) == 0:
            raise ValueError("value can't be None or empty")

        if value[0] == "#":
            value = value[1:]

        if len(value) == 6:
            return cls(
                int(value[:2],  16),
                int(value[2:4], 16),
                int(value[4:6], 16)
            )
        elif len(value) == 3:
            return cls(
                int(value[0] * 2, 16),
                int(value[1] * 2, 16),
                int(value[2] * 2, 16)
            )
        else:
            raise ValueError("length of value must be 6 or 3")

    @classmethod
    def from_bytes(cls, value: bytes):
        if not isinstance(value, bytes):
            raise ValueError("value must be bytes")

        if value is None or len(value) != 3:
            raise ValueError("value must be 3 bytes")

        return cls(*value)

    def __str__(self) -> str:
        red:   str = hex(self._red)[2:]
        green: str = hex(self._green)[2:]
        blue:  str = hex(self._blue)[2:]
        return f"#{red:>02}{green:>02}{blue:>02}"

    def __bytes__(self) -> bytes:
        return bytes([self._red, self._green, self._blue])

    def __repr__(self) -> str:
        return f"RGBColor({self._red}, {self._green}, {self._blue})"

    def __eq__(self, other) -> bool:
        return (
            self._red   == other.red   and
            self._green == other.green and
            self._blue  == other.blue
        )

    def __iter__(self):
        yield self._red
        yield self._green
        yield self._blue

    def items(self):
        return {
            "red":   self._red,
            "green": self._green,
            "blue":  self._blue
        }

    def clone(self):
        return self.__class__(self._red, self._green, self._blue)

    @property
    def red(self) -> int:
        return self._red

    @red.setter
    def red(self, red) -> int:
        if not isinstance(red, int):
            raise ValueError("red must be int")
        if not self._on_8bit_bounds(red):
            raise ValueError("red must be between 0 and 255")
        self._red = red

    @property
    def green(self) -> int:
        return self._green

    @green.setter
    def green(self, green) -> int:
        if not isinstance(green, int):
            raise ValueError("green must be int")
        if not self._on_8bit_bounds(green):
            raise ValueError("green must be between 0 and 255")
        self._green = green

    @property
    def blue(self) -> int:
        return self._blue

    @blue.setter
    def blue(self, blue) -> int:
        if not isinstance(blue, int):
            raise ValueError("blue must be int")
        if not self._on_8bit_bounds(blue):
            raise ValueError("blue must be between 0 and 255")
        self._blue = blue

```