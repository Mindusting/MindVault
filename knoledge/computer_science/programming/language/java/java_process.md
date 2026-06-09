---
author: Mindusting
corrected: false
tags:
  - Programming
  - Java
title: Procesos en Java
---

# PROCESOS EN JAVA

> [!fail]- ESTE PARTADO ESTÁ INCOMLETO
> > [!todo] #TODO
> > - [ ] Hacer una documentación más extensa y detallada.

> [!help]- REFERENCIAS INTERNAS
> Recomiendo tener a mano los siguiente documentos para poder comprender la siguiente documentación, sobre todo si tu intención es llegar más haya de los ejemplos simples que puedes encontrar aquí, ya que los siguientes documentos entran más en detalle sobre cada [clase](theory/oop.md):
> - [Clase `Process`](packages/java/lang/java_lang_process.md)
> - [Clase `ProcessBuilder`](packages/java/lang/java_lang_processbuilder.md)
> - [Clase `Runtime`](packages/java/lang/java_lang_runtime.md)
> - [Clase `System`](packages/java/lang/java_lang_system.md)

> [!faq]- FAQ
> - [¿Qué es un proceso?](../../fundamentals/temp-dump/pc_process.md)
> - [¿Qué son las tuberías?]()


Para ejecutar otro proceso desde **Java** se usan principalmente dos [clases](theory/oop.md); [`ProcessBuilder`](packages/java/lang/java_lang_processbuilder.md) y [`Process`](packages/java/lang/java_lang_process.md); el primero se encargará de como tal crear el proceso mientras que el segundo es el tipo de objeto que representará el proceso en cuestión.

---

Para el siguiente ejemplo tendremos la siguiente estructura de archivos; en donde tendremos un proyecto con las carpetas `src` (*en donde guardaremos los archivo `.java`*) y `bin` (*en donde guardaremos los archivos `.class` tras ejecutar el compilador de Java sobre los archivo `.java`*); es importante recalcar esto ya que en la ejecución de procesos, nosotros llamaremos a los archivos `.class` no a los `.java`.

```txt
/MyProyect
├─/src
│ └─/processes
│   ├─/MainProcess.java
│   └─/SecondProcess.java
└─/bin
  └─/processes
    ├─/MainProcess.class
    └─/SecondProcess.class
```

**MainProcess.java:**

```java
package processes;

import java.io.IOException;

public class MainProcess {
    public static void main(String[] args) {
        ProcessBuilder processBuilder = null;
        Process        process        = null;

        try {
            processBuilder = ProcessBuilder(
                "java",
                "-cp",
                "bin",
                "processes/SecondProcess"
            );
            // La siguiente instrucción es la que
            // puede lanzar al excepción IOException.
            process = processBuilder.start();
        } catch (IOException ex) {
            // Se ejecuta cuando el proceso no se
            // ha podido ejecutar correctamente.
            System.out.println("Error de proceso.");
        }
    }
}
```

**SecondProcess.java:**

```java
package processes;

import java.io.File;
import java.io.IOException;

public class SecondProcess {
    public static void main(String[] args) {
        File file = null;

        // Este proceso simplemente crea el archivo
        // readme.md en caso de que no exista.

        try {
            file = new File("readme.md");

            if (!file.exists()) {
                file.createNewFile();
            }
        } catch (IOException ex) {
            System.out.println("No se ha podido crear el archivo.");
        }
    }
}
```

> [!example] CASO DE EJEMPLO
> En este caso como se puede ver en el `MainProcess.java`, el [`ProcessBuilder`](packages/java/lang/java_lang_processbuilder.md) recibe varios argumentos que conformarán el comando que ejecutará el proceso en cuestión, en este caso son los siguientes:
> - `java`: indica se se debe ejecutar el comando `java`; al igual que lo hacemos con la [ejecución de Java](java_javac.md#EJECUTAR).
> - `-cp`: (*abreviación de `-classpath`*) indica que vamos a especificar la ruta de los archivos `.class`; si quieres más información sobre esto lo tienes en la [documentación de ejecución de Java](java_javac.md#EJECUTAR).
> - `bin`: es el directorio en donde se guardan los archivos `.class`.
> - `processes/SecondProcess`: es la ruta y nombre del archivo `.class` que contiene el [método `main`](java_main_method.md).

## VERSIÓN OBSOLETA

Hay una forma de crear procesos en **Java** que está ==obsoleta==, esto quiere decir que no se debería de seguir usando esta forma de ejecutar procesos, pero es importante conocerla ya que en la vida real podemos encontrarnos con código antiguo que debamos modificar y contenga esta forma de crearlos o que estemos trabajando sobre una versión de **Java** anterior a la 18, ya que fue en esta en la que se cambió; esta forma consiste en crear el objeto de tipo [`Process`](packages/java/lang/java_lang_process.md) a través de la clase [`Runtime`](packages/java/lang/java_lang_runtime.md); ahora veremos un ejemplo de como se haría:

**MainProcess.java:**

```java
package processes;

import java.io.IOException;

public class MainProcess {
    public static void main(String[] args) {
        Process process = null;

        // Los argumentos hay que pasarlos en forma de array.
        String[] processArgs = {
            "-cp",
            "bin",
            "processes/SecondProcess"
        };

        try {
            // La siguiente instrucción es la que
            // puede lanzar al excepción IOException.
            process = Runtime.getRuntime().exec(
                "java",
                processArgs
            );
        } catch (IOException ex) {
            // Se ejecuta cuando el proceso no se
            // ha podido ejecutar correctamente.
            System.out.println("Error de proceso.");
        }
    }
}
```

## FIN PREMATURO

Si queremos que desde el propio interior del proceso secundario terminarlo debido a algún error o simplemente por qué queremos matarlo antes de su muerte natural, podemos hacerlo mediante el [método `exit` de la clase `System`](packages/java/lang/java_lang_system.md#MÉTODO%20EXIT):

**SecondProcess.java:**

```java
package processes;

import java.io.File;
import java.io.IOException;

public class SecondProcess {
    public static void main(String[] args) {
        int ioCodeError = 100;

        File file = null;

        // Este proceso simplemente crea el archivo
        // readme.md en caso de que no exista.

        try {
            file = new File("readme.md");

            if (!file.exists()) {
                file.createNewFile();
            }
        } catch (IOException ex) {
            // Se termina de forma prematura el proceso
            // con el código de error 100 (es un ejemplo,
            // no tiene por qué ser este número) indicando
            // que ha ocurrido una excepción de tipo
            // IOException.
            System.exit(ioCodeError)
        }
    }
}
```

## ESPERAR A QUE TERMINE

Si queremos que un proceso espere a que termine el otro, lo que podemos usar es el [método](java_method.md) `waitFor`; este no recibe ningún parámetro y puede lanzar una [excepción](java_exception.md) de tipo `InterruptedException` si el proceso secundario es interrumpido.

**MainProcess.java:**

```java
package processes;

import java.io.IOException;

public class MainProcess {
    public static void main(String[] args) {
        int            errorCode      = 0;
        ProcessBuilder processBuilder = null;
        Process        process        = null;

        try {
            processBuilder = ProcessBuilder(
                "java",
                "-cp",
                "bin",
                "processes/SecondProcess"
            );
            // La siguiente instrucción es la que
            // puede lanzar al excepción IOException.
            process = processBuilder.start();

            // El código se detiene al llegar aquí
            // hasta que el proceso secundario
            // termine de ejecutarse; a su vez se
            // guardará el código de error para
            // poder indicar un comportamiento
            // en caso de error.
            errorCode = process.waitFor();

            // Comprobamos si ha ocurrido algún error.
            if (errorCode == 0) {
                System.out.println("No ocurrio ningún error.");
            } else {
                System.out.printf(
                    "Ocurrió el error: %d\n",
                    errorCode
                );
            }
        } catch (IOException ex) {
            // Se ejecuta cuando el proceso no se
            // ha podido ejecutar correctamente.
            System.out.println("Error de proceso.");
        } catch (InterruptedException ex) {
            // En caso de que se interrumpa el proceso
            // se indica lo sucedido.
            System.out.println("Se interrumpio el proceso.");
        }
    }
}
```

> [!example] EJEMPLO
> En este caso además de esperar a que termine de ejecutarse el proceso, recibimos un código de error el cual nos indicará que ha ocurrido algún problema, si conocemos los códigos de error podremos actuar de diferentes formas mediante [condicionales](java_condicion.md).

## CREACIÓN DE TUBERÍAS

Para crear unas [tuberías (*pipes*)](../../fundamentals/temp-dump/pc_pipes.md) entre los **procesos** se pueden usar tres métodos:

- `getInputStream`: devuelve un flujo por el que llegará la información del proceso hijo.
- `getOutputStream`: devuelve un flujo por el que enviaremos información al proceso hijo.
- `getErrorStream`: devuelve un flujo por el que llegarán los mensajes de error del proceso hijo.

> [!important] IMPORTANTE
> Los nombres de entrada y salida de datos pueden llevar a confusión; se deben de ver desde la perspectiva del **proceso padre**, es decir, el `getOutputStream` devuelve el flujo por el que el proceso padre sacará la información (*enviándola al hijo*); mientras que el `getInputStream` devuelve el flujo por el que el proceso padre recibirá información (*enviada por el hijo*).

Estos flojos se suelen combinar con los `BufferedReader` y `BufferendWriter` para mejorar su rendimiento.

```java
package processes;

import java.io.IOException;

public class FirstProcess {
    public static void main(String[] args) {
        ProcessBuilder pb      = null;
        Process        process = null;
        BufferedReader br      = null;
        BufferedWriter bw      = null;

        try {
            // En este caso no pongo el código del otro
            // proceso ya que es un ejemplo simple de
            // como acceder a us flujos de entrada y salida.
            pb = new ProcessBuilder(
                "java",
                "-cp",
                "bin",
                "processes.SecondProcess"
            );
            process = pb.start();
            br = new BufferedReader(
                new InputStreamReader(
                    process.getInputStream()
                )
            );
            bw = new BufferedWriter(
                new OutputStreamWriter(
                    process.getOutputStream()
                )
            );

            // Si el proceso hijo espera input por teclado
            // recibirá este Hola mundo.
            bw.write("Hola mundo!");

            // Si el proceso hijo imprime algo, el padre
            // leerá la impresión del hijo.
            String line = null;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException ex) {
        } finally {
            try {if (br == null) br.close()}
            catch (Exception ex) {}

            try {if (bw == null) bw.close()}
            catch (Exception ex) {}
        }
    }
}
```

## IDENTIFICADOR DEL PROCESO

La clase `Process` contiene una propiedad que es `pid` (*Process Identificator*), este es un número de tipo `long` que identifica de forma húnica el proceso en cuestión.

```java
public class FirstProcess {
    public static void main(String[] args) {
        ProcessBuilder pb      = null;
        Process        process = null;
        
        try {
            pb = new ProcessBuilder(
                "java",
                "-cp",
                "bin",
                "processes.SecondProcess"
            );
            process = pb.start();
            
            System.out.printf(
                "Identificador del hijo: %d\n",
                process.pid()
            );
        } catch (IOException ex) {}
    }
}
```
