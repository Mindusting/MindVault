---
aliases: [Método main en Java]
author: Mindusting
corrected: false
creationDate: 2026-06-09 01:51:57
headerFile: false
modificationDate: 2026-06-09 01:51:57
rating: 
tags: [Programming, Java]
---

# MÉTODO MAIN EN JAVA

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Para indicar por donde debe empezar a ejcutarse un programa en **Java**, se usa el [**método**](oop.md#MÉTODOS) `main`; este es el que generalmente se usa cuando estamos aprendiendo a programar en **Java**, posteriormente este para a tener la tarea de *inicializar* el [**objeto**](oop.md#OBJETOS) que se usará como inicio del programa.

> [!note] NOTA
> Cada [**clase**](oop.md#CLASES) puede contener un [**método**](oop.md#MÉTODOS) `main`, por lo que puede haber varios dentro de un mismo programa; comento esto ya que es una duda que suele tener los programadores nuevos.

## DECLARACIÓN DEL MÉTODO MAIN

Para declarar un [**método**](oop.md#MÉTODOS) `main` tendremos que escribir lo siguiente dentro de una [**clase**](oop.md#CLASES) (*es siempre de esta forma, no hay margen a modificación*):

```java
public static void main(String[] args) {}
```

La siguiente explicación es un poco técnica así que no te preocupes si no entiendes algo si eres nuevo en **Java** y/o programación: `public` perimte que se pueda acceder a este [**método**](oop.md#MÉTODOS) desde fuera de la [**clase**](oop.md#CLASES); `static` permite que se ejecute este [**método**](oop.md#MÉTODOS) sin tener que instanciar la [**clase**](oop.md#CLASES) que la contiene, ya que como el programa a este punto todavía no ha sido iniciado, no puede haber ninguna [**clase**](oop.md#CLASES) inicializada; `void` indica que este [**método**](oop.md#MÉTODOS) no debuelve ningún valor; `main` es el nombre del [**método**](oop.md#MÉTODOS) para que la [**JVM**](jvm.md) pueda identificarlo; `(String[] args)` indica los argumentos que recivirá este [**método**](oop.md#MÉTODOS), siendo estos los valores que se especifican seguidos a la ejecución del programa ([*más detalle sobre esto en el apartado específico*](#ARGUMENTOS)); `{}` es el cuerpo, este contendrá todas las instrucciones que pertenezcan a este [**método**](oop.md#MÉTODOS).

---

Este [**método**](oop.md#MÉTODOS) por sí solo dentro de un archivo de **Java** no funciona, ya que debe estar dentro de una clase; para hacer que funcione seguiremos el siguiente ejemplo:

Crearemos el archivo `Program.java` con el siguiente contenido:

```java
// Esto es la clase.
//       v
public class Program {
    // Esto es el método main.
    //       v
    public static void main(String[] args) {
        // Esta es una instrucción en el cuerto
        // del método main.
        //      v
        System.out.println("Hola mundo!");
    }
}
```

Este archivo es el primer programa que se suele crear cuando empezamos a aprender a programar en **Java** (*un problema que tiene **Java** es que no es facil para un novato empezar a programar en este lenguaje ya que para crear un programa tan simple como este requiere escribir muchas cosas que el novato no entiende*); para poder poner en marcha este programa tendremos que compilarlo con el siguiente comando:

```bash
javac Program.java
```

Este nos creará un archivo llamado `Program.class` (*este contiene una versión "compacta" del archivo `.java`, a esta versión "compacta" se le llama "bytecode"*), este lo podremos ejecutar con el siguiente comando:

```bash
java Program
```

Imprimiendonos como resultado el siguiente texto:

```txt
Hola mundo!
```

## ARGUMENTOS
