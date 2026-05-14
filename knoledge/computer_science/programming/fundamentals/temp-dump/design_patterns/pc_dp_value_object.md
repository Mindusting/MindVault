---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming/Concept
  - DesignPattern
title: Patón objeto de valor programación
---

# PATÓN OBJETO DE VALOR PROGRAMACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Hacer el caso de uso de los número naturales (*por ejemplo, monedas*).
> > - [ ] Añadir dibujos y diagramas.

Características de un **objeto** para cumplir con este parón:

- **Inmutabilidad**: el valor no se puede modificar, en caso de que tenga un método que lo "modifique", no lo tendrá que modificar, sino crear una nueva instancia del mismo tipo de objeto con el nuevo valor.
- **Igualdad por valor**: al compara dos objetos del mismo tipo, se comparará el valor que contienen, no la instancia de estos (*no se compararán las direcciones de memoria de los punteros*).
- **Sin identidad signeficativa**: el objeto como tal prácticamente no tiene importancia, ya que lo verdaderamente importante es el valor que contiene.

Por ejemplo, lo [`String`](../../../language/java/packages/java/lang/java_lang_string.md) en [**Java**](../../../language/java/java.md) siguen este patón, ya que encapsulan el **valor** real, son inmutables, al comparar dos [`String`](../../../language/java/packages/java/lang/java_lang_string.md) se hace comprobado que su contenido sea el mismo y no se le da importancia al **objeto** que contiene el texto, sino al texto ensí.

> [!quote]- ANALOGÍA
> Imaginemos que tenemos un almacén de hojas, estas hojas debe de estar sueltas, no nos sirve si son las hojas de un libro, tampoco nos sirve que nos dén las hojas sueltas ya que podrían perder el orden; por tanto tendremos que establecer unas reglas en las que se establece como se deben guardar las hojas.
> 
> A la hora de programar, (*siguiendo con la analogía*) muchagente lo que aría sería hacer que las hojas llegan al almacén de cualquier forma y allí es donde hace la comprobación para segurarse de que las hojas están en un formato válido; esto si se aplica en un caso en particular, no hay demasiado problema, pero imaginemos que ahora tenemos múltiples almacenes, tendríamos que aplicar el mismo proceso de comprobación en todos los sitios, y si el protocolo es medianamente complejo, podría ocurrir que haya pequeñas variaciones entre los distintos almacenes.
> 
> La solución sería establecer una serie de normas para entregar los papeles, de forma que quienes quieran entregar los papeles al almacén serán los responsables de **enpaquetar** los papeles de la forma correcta.
> 
> Por ejemplo, usando una carpeta, de esta forma, los papeles no estarán sueltos y no podrán meter un libro ya que sería muy grande.
> 
> De esta forma, como el almacén solo admite carpetas, se asegura que únicamente recivirá papeles y que no podrá perdér el orden (*ya que no se pueden mover ahí dentro*).
> 
> ---
> 
> En esta analogía, la carpeta es nuestro **objeto**, mientras que los papeles en su interior es el **valor**; es por esto que se dice que el **objeto** no tiene importancia, ya que la carpeta es solo el medio de tranporte para asegurar tanto la integridad como la veracidad de que lo que se está entregando es lo esperado, pero no es lo importante, lo imporatante es el contenido de esta carpeta, el **valor** del **objeto**.

## CASO DE USO

> [!example] EJEPLO
> Imaginemos que nemos que manejar una serie de precios de productos/servicios, un precio siempre debe ser positivo, por lo que podríamos comprobar cada vez que a una función se pasa un precio en forma de número, si este es mayor que 0, pudiendo llevar a fallo si en algúna de las funciones se nos olbida añadir esa comprobación.
> 
> Para evitar este problema podemos hacer una clase llamada `Precio` en la que su constructor, compruebe si el **valor** que queremos darle es un precio válido, de esta forma, la comprobación únicamente tendremos que implementarla una vez, haciendo que siempre se apliquen las mismar reglas en todos los sitios en donde se use esta clase (*además de poder corregir un posible error dentro de la propia clase, haciendo que esa corrección a la comprobación se aplique en todos los sitios en donde se use*).

Ahora sí, veamos el caso de uso en [**Java**](../../../language/java/java.md):

```java
public class Price {

    private int value;

    public Price(int value)
    throws IllegalArgumentException {
        if (value <= 0) {
            throw new IllegalArgumentException();
        }
        this.value = value;
    }

    public int getValue() {
        return this.value;
    }

    @Override
    public boolean equals(Object other) {
        if (other == null) return false;
        if (this.getClass() != other.getClass()) return false;
        return this.value == (Price)(other).value;
    }
}
```

Ahora veamos como se usaría a la hora de establecerlo en un producto:

```java
// Constructor de producto:
// Product(String name, Price price)

// Aquí funciona bien:
Product potatoe = new Product("Patata", new Price(42);)

// Aquí da una excepción:
Product apple = new Product("Manzana", new Price(-8);)
```
