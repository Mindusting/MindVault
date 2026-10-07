---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - CSS
  - Web
title: FlexBox en CSS3
rating: 0.75
---

# FLEXBOX EN CSS

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar que es el fexbox.
> > - [ ] Explicar el fin de esta propiedad.
> > - [ ] Explicar que son las propiedades de los padres.
> > - [ ] Explicar que son las propiedades de los hijos.
> >     - [ ] Hacer dibujo para `flex-shrink`.
> >     - [ ] Hacer dibujo para `flex-basis`.
> >     - [ ] Hacer dibujo para `align-self`.
> > - [ ] Explicar la propiedad `flex`.

> [!external-link]- REFERENCIAS WEB
> YouTube:
> - [Bro Code](https://youtu.be/GteJWhCikCk) #WWW/YT/BroCode
> - [Coding2GO (flexbox)](https://youtu.be/wsTv9y931o8) #WWW/YT/Coding2GO
> - [Coding2GO (flex shorthand)](https://youtu.be/ZOK-DU7vT0A) #WWW/YT/Coding2GO

## PROPIEDADES DE LOS PADRES

### DISPLAY

Para poder usar el *flexbox* tendremos que a la *etiqueta* **padre** la propiedad `display` con el valor `flex` o `inline-flex`.

> [!syntax] SINTAXIS
> display: flex;

%%
```html
<nav>
    <a href=""></a>
    <a href=""></a>
    <a href=""></a>
</nav>
```
%%

```css
/*
Hacemos que a las etiquetas nav
se les apliceque el flexbox.
*/
nav {
    display: flex;
}
```

### DIRECCIÓN

La **dirección** indica como se van a colocar los elementos **hijos**, la idea es que podemos indicar si queremos que se coloquen de izquierda a derecha o de arriba a bajo.

> [!syntax] SINTAXIS
> flex-direction: ***\[direction\]***;

- `row`: (*valor por defecto*) coloca los elementos de izquierda a derecha.
- `column`: coloca los elementos de arriba a abajo.
- `row-reverse`: es igual que `row` pero invirtiendo el orden.
- `column-reverse`: es igual que `column` pero invirtiendo el orden.

![#center](assets/flexbox_direction_1.excalidraw.md)

> [!important] IMPORTANTE
> En el resto de la documentación se usará en los ejemplos la opción `row`, por lo que el resultado cambiaría si usas otro valor como dirección, solo debes tener en cuenta que cuando se hable de *inicio* se refiere al origen de la flecha, mientras que cuando pone *fin*/*final* se refiere a la punta de la flecha.
> 
> ![#center](assets/flexbox_direction_2.excalidraw.md)

### WRAP

Esta propiedad permite indicar que los elementos **hijos** en caso de no caber dentro del elemento **padre** dentro de una misma línea, estos se reorganizarán en múltiples líneas.

> [!syntax] SINTAXIS
> flex-wrap: ***\[option\]***;

- `nowrap`: (*valor por defecto*) añade todos los elementos en la misma línea.
- `wrap`: si los elementos no entran en una línea, los que no entren saltarán a la siguiente, este proceso se puede repetir varias veces, dividiéndose en múltiples líneas.
- `wrap-reverse`: es lo mismo que `wrap`, pero de forma inversa.

![#center](assets/flexbox_wrap.excalidraw.md)

> [!note] Nota
> En la [imagen](assets/flexbox_wrap.excalidraw.md) se muestra como se reorganizan los elementos cuando la [dirección](#DIRECCIÓN) es de tipo `row` (*horizontal*).
> 
> Si la [dirección](#DIRECCIÓN) es de tipo `column`, funcionaría igual, con la diferencia que iría de arriba a abajo, y cuando ya no caben más elementos, estos irían a la siguiente columna.

> [!warning] Atención
> Para poder ver los efectos del `wrap` en el eje vertical, el elemento *padre* tendrá que tener una altura fija, ya que sino esta crecerá a más elementos *hijo* tenga, provocando que nunca haga el efecto de `wrap`.

### JUSTIFICADO

Esta propiedad permite indicar como queremos que se alineen los elementos *hijo* dentro del *padre*.

> [!syntax] SINTAXIS
> justify-content: ***\[option\]***;

- `flex-start`: coloca los *hijos* en el principio del *padre*.
- `flex-end`: coloca los *hijos* al final del *padre*.
- `center`: coloca los *hijos* en el centro del *padre*.
- `space-between`: separa los *hijos* al máximo, dejando los que se encuentran en los extremos pegados al margen del *padre*.
- `space-around`: pone dos separaciones igual a cada lado de cada *hijos*, haciendo que entre cada *hijo* haya dos separaciones y entre cada *hijo* extremo y el margen del *padre* haya una separación.
- `space-evenly`: separa todos los *hijos* de forma uniforme entre los propios *hijos* y los márgenes del *padre*.

![#center](assets/flexbox_justify-content.excalidraw.md)

### ALINEAR ELEMENTOS

Esta propiedad permite indicar como se deben alinear los elementos *hijos* sobre la línea en la que están colocados, debido a esto, es más fácil entender como funciona cuando se muestran elementos de distintos tamaños y en varias líneas gracias al [`wrap`](#WRAP).

> [!syntax] SINTAXIS
> align-items: ***\[option\]***;

- `flex-start`: alinea todos los elementos en la parte superior.
- `flex-end`: alinea todos los elementos en la parte inferior.
- `center`: alinea todos los elementos en el centro.
- `stretch`: deforma los elementos para que cubran todo el espacio.
- `baseline`: alinea los elementos en la base del texto.

![#center](assets/flexbox_align-items.excalidraw.md)

### ALINEAR CONTENIDO

Esta propiedad alinea todos los *hijos* del *padre* en bloque:

> [!syntax] SINTAXIS
> align-content: ***\[option\]***;

- `flex-start`: alinea todos los elementos en la parte superior.
- `flex-end`: alinea todos los elementos en la parte inferior.
- `center`: alinea todos los elementos en el centro.
- `stretch`: deforma los elementos para que cubran todo el espacio.
- `space-between`: separa los *hijos* al máximo, dejando los que se encuentran en los extremos pegados al margen del *padre*.
- `space-around`: pone dos separaciones igual a cada lado de cada *hijos*, haciendo que entre cada *hijo* haya dos separaciones y entre cada *hijo* extremo y el margen del *padre* haya una separación.

![#center](assets/flexbox_align-content.excalidraw.md)

## PROPIEDADES DE LOS HIJOS

### ORDEN

El orden indica la posición en la que se va a colocar el *hijo*, si multiples *hijos* tienen el mismo valor de orden, estos se organizarán en baso al orden en el que estén en el [HTML](../../markup_language/html/html.md):

![#center](assets/flexbox_order_1.excalidraw.md)

Como se puede ver en la imagen, el valor por defecto es el `0`, y si lo cambiamos por otro como puede ser `-1` ese elemento se situará más cerca del *origen*, mientras que si le ponemos un número mayor como `1` este se situará más cerca del *destino*, el número puede ser el que queramos siempre y cuando sea un número entero y que cuanto menor sea el número, más cerca de *origen* se situará, si es más grande, se situará más cerca del destino.

> [!syntax] SINTAXIS
> order: ***\[number\]***;

### CRECIMIENTO

Cuando los *hijos* no llegan a cubrir por completo el espacio que abarca el *padre*, estos dejan un hueco, si queremos que los *hijos* se estiren para cubrir ese hueco usaremos `flex-grow`, este por defecto tiene el valor de `0`, esto implica que el *hijo* no crece, si le damos de valor `1` o superior, este crecerá para ocupar el hueco restante.

Para calcular cuanto espacio crece cada *hijo* se suman todos los valores de crecimiento de los *hijos* dentro de del mismo *padre*, luego se divide el hueco restante entre el resultado de la suma, para finalmente hacer crecer cada *hijo* la proporción que le corresponde.

![#center](assets/flexbox_flex-grow.excalidraw.md)

> [!syntax] SINTAXIS
> flex-grow: ***\[number\]***;

> [!tip] TIP
> Si el valor de **crecimiento** de todos los *hijos* es `1`, todos crecerán lo mismo (*ten en cuenta que el tamaño inicial puede no ser el mismo, para ello, revisa el apartado [**tamaño base**](#TAMAÑO%20BASE)*).

### ESTRECHAMIENTO

El **estrechamiento** funciona igual que el [**crecimiento**](#CRECIMIENTO) pero a la inversa, si el valor es `0` el *hijo* no se estrechará, si el valor es `1` (*siendo este el valor por defecto*), este cuando no haya suficiente sitio en el *padre* se estrechará, y a payor sea el número de **estrechamiento** le indiquemos más se estrechará el *hijo* siguiendo la misma lógica que el [**crecimiento**](#CRECIMIENTO).

> [!syntax] SINTAXIS
> flex-shrink: ***\[number\]***;

### TAMAÑO BASE

El **tamaño base** de un *hijo* es el tamaño que se tendrá en cuanta a la hora de hacer los cálculos de si sobra o falta espacio para que todos los *hijos* quepan dentro del *padre*.

> [!syntax] SINTAXIS
> flex-basis: ***\[size\]***;

El tamaño se puede especificar mediante cualquier [unidad de medida](css_measure_units.md).

> [!tip] TIP
> Si haces que todos lo *hijos* tengan un **tamaño base** de `0` esto hará que a la hora de estirar todos los *hijos* para que se ajusten al *padre* todos tendrán el mismo tamaño (*en el caso de que la propiedad `flex-grow` sea igual a `1` en todos lo hijos*).

### ALINEACIÓN

La **alineación** es básicamente lo mismo que la [alineación de los elementos](#ALINEAR%20ELEMENTOS) solo que de forma individual para cada *hijo*, si indicamos esta propiedad dentro de un *hijo*, esta sobre escribirá el valor que haya establecido el *padre*.

> [!syntax] SINTAXIS
> align-self: ***\[option\]***;

- `flex-start`: alinea todos los elementos en la parte superior.
- `flex-end`: alinea todos los elementos en la parte inferior.
- `center`: alinea todos los elementos en el centro.
- `stretch`: deforma los elementos para que cubran todo el espacio.
- `baseline`: alinea los elementos en la base del texto.
