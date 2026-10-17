---
aliases: [Primer programa en C]
author: Mindusting
corrected: false
creationDate: 2026-09-05 12:40:15
headerFile: false
headerfile: false
modificationDate: 2026-10-16 11:58:49
rating: 
tags: [C, Programming]
---

# PRIMER PROGRAMA EN C

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Explicar que el archivo principal no tiene por qué llamarse `main.c`, se le puede dar el nombre que quieras.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/c/index.php) #WWW/W3Schools
> - [W3 Schools (Librería `stdio`)](https://www.w3schools.com/c/c_ref_stdio.php) #WWW/W3Schools

En este archivo daremos los primeros parsos para crear un primer programa, por lo que verás lo báisco si estás empezando y a lo larto del codumento tendrás enlaces a otros archivos en los que se entrará más en detalle sobre ciertos temas.

## MÍNIMO E INDISPENSABLE

Lo que necesitamos es:

1. **Un [archivo C](c_files.md) (`main.c`):**
    Esta clase de archivos no es nada más que un archivo de texto plano como puede ser un `.txt`, pero este tiene una extensión `.c`; para editar este archivo necesitaremos un editor de texto pano, como puede ser **nano** o **vim** en el caso del terminal o un bloc de notas.

2. **[Compilador de C](../../../../../../temp/os/linux/command/gcc.md):**
    Si tienes [GNU Linux](../../../../../../temp/os/linux/linux.md) como sistema operativo tendrías que tener ya un compilador de C instalado (*a menos que sea una distribución tan minimalista que no venga con el incluido*), si en tu sistema no tienes instalado ningún **compilador de C**.

Una vez tengamos estas dos cosas podremos empezar creando el archivo `main.c`, este tiene que contener el siguiente texto:

```c
#include <stdio.h>

int main() {
    printf("Hola mundo!\n");
    return 0;
}
```

Una vez tenemos el archivo con ese texto podemos compilarlo (*transformarlo a binario para que el ordenador entienda las instrucciones*) y así luego ejecutar el programa; para usaremos el siguiente comando.

```bash
gcc main.c -o main
```

Este nos creará un archivo llamado `main`, para ejecutar el programa tendremos que escribir lo siguiente:

```bash
./main
```

Justo debajo de nuestro comando para ejecutar este programa, tendría que aparecer el texto `Hola mundo!`, si es así: Felicidades! Acabas de crear tu primer programa en C, ahora veremos que significa todo lo que hemos hecho asta ahora.

---

Empecemos desgranando el archivo `main.c`, este emieza con la línea `#include <stdio.h>`, esta parte se puede descomponer en dos parte, la primera es `#include`, esta le indica al compilador de código C que queremos traer código de una librería, esto nos permite ejecutar instrucciones ya prehechas, facilitándonos nuestro trabajo, luego llega el `<stdio.h>`, este indica que queremos incluir la librería estardar de *input* (*entrada de datos*) y *output* (*salida de datos*), esta librería nos permitirá usar más adelante la función `printf` para poder imprimir texto en el terminal.

Lo siguiente que vemos es la declaración de la [función](functions.md) `main` con el texto `int main()`, esto indica que lo que escribamos entre llaves después de esto será el cuerpo de dicha [función](functions.md), la palabra `int` indica que esta [función](functions.md) va a devolver un número entero, este indicará el estado del programa, si devolvemos `0` quiere decir que ha terminado bien, si es cualquier otro número, es que ha ocurrido algún problema, por eso más adelante puedes ver `return 0;`, la palabra `main` indica que es la [función](functions.md) principal, esta es la [función](functions.md) por la que empezará nuestro programa cuando lo ejecutemos (*básicamente indica el punto de inicio de nuestro programa*), seguido por unos paréntesis `()` en este caso no hemos puesto nada entre ellos ya que para lo que estamos haciendo no es necesario, pero entre estos podremos poner más adelante argumentos con los que recibiremos información con la que podremos trabajar.

El cuerpo de la [función](functions.md) `main`, este está definido por dos llaves `{}` entre estas dos, podremos encontrar las instrucciones que le pertenecen a esta [función](functions.md): la primera es `printf("Hola mundo!\n");`, con esta indicamos que queremos imprimir en pantalla el texto `Hola mundo!` seguida de un salto de línea (`\n`), para luego poner `;` indicando que ahí se termina la primera instrucción; luego podremos encontrar la instrucción `return 0;`, esta indica que la [función](function.md) termina ahí y va a devolver el número `0` indicando así que nuestro programa ha terminado correctamente, al final de esta podremos encontrar otro `;` indicando que esta instrucción ha terminado.

---

---

---

---

---

Para poder hacer que un programa de **C** funcione, primero tendremos que crear la siguiente estructura.

```c
// Incluimos en nuestro programa la librería "stdio".
#include <stdio.h>

// Declaramos la función "main".
int main() {
    // Imprimimos un mensaje en consola.
    printf("Hola mundo!\n");

    // La función "main" devuelve 0 si no ocurren errores.
    return 0;
}
```

La función `main` es por donde nuestro programa va a empezar a ejecutarse, si nuestro archivo no tiene función `main` el compilador nos dará un error, ya que esta función representa el punto en el que nuestro programa debe iniciar a ejecutarse.

> [!info]
> La librería `stdio` (*STanDar Input Output*) agrega a nuestro programa varias funciones, entre ellas tenemos la función `printf`, la cual nos permite imprimir texto por consola.
> 
> Si quieres saber más a cerca de esta librería te recomiendo revisar el siguiente [enlace](https://www.w3schools.com/c/c_ref_stdio.php).

De momento todo nuestro programa lo escribiremos dentro de esta función, al gula que hemos hecho a la hora de imprimir el "*Hola mundo!*" por consola.

> [!note]
> El `return` al final de la función `main` le sirve a nuestro programa para saber si ha llegado al final de la ejecución sin errores, es por ello que es importante ponerlo.
