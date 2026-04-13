---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - Java
  - Socket
  - Thread
  - Network
title: Networking en Java
---

# NETWORKING EN JAVA

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!faq]- FAQ
> - [¿Qué son los sockets en programación?](../../../../../temp/pc/pc_socket.md)
> - [¿Qué son los hilos en programación?](../../../../../temp/pc/pc_thread.md)

En este apartado se verá como trabajar a través de la red con **Java**, haciendo uso de los *sockets*; estos también permiten comunicar procesos dentro de una misma máquina.

## GENÉRICO Y SIMPLE

Aquí vas a poder ver un cliente y servidor genérico y simple, es decir son de juguete, están hechos de forma que ejecutas el servidor, y este se queda a las espera del cliente, una vez el cliente se conecta, ambos obtienen los flujos de entrada y salida; finalmente se cierra la conexión y terminan ambos programas; no sirven para un caso real estos son didácticos.

### SERVIDOR

```java
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args) {
        // Se debe indicar el puerto por le que queremos
        // que el servidor escuche a la espera de soli-
        // citudes de conexión.
        int          port         = 12345;
        ServerSocket serverSocket = null;
        Socket       clientSocket = null;
        InputStream  inputStream  = null;
        OutputStream outputStream = null;

        try {
            // Se crea un socket de servidor preparado
            // para escuchar por el puerto indicado,
            // si ocurre algún problema de tipo IO
            // se lanzará una excepción de IOException.
            serverSocket = new ServerSocket(port);
            // El servidor se detiene hasta recivir un
            // una petición de conexión y la guarda en
            // forma de socket, si ocurre algún problema
            // de tipo IO se lanzará una excepción de
            // tipo IOException.
            clientSocket = serverSocket.accept();

            // Obtenemos los flujos de salida y entrada,
            // teniendo en cuenta que el de salida se debe
            // obtener antes que el se entrada ya que si
            // no, no funciona.
            outputStream = clientSocket.getOutputStream();
            inputStream  = clientSocket.getInputStream();

            // Aquí pondríamos el código que queramos
            // que se ejecute en el transcurso de la
            // comunicación.

        } catch (IOException ex) {
            // En caso de que ocurra una excepción de tipo
            // IOException imprimimos el mensaje de error,
            // en un caso real tendremos que poner que
            // queremos que se haga en caso de error o dejar
            // que se propague.
            ex.printStackTrace();
        } finally {
            // Finalmente cerramos todos los recursos
            // usados para la conexión.
            try {
                if (inputStream != null) inputStream.close();
            } catch (Exception ex) {}

            try {
                if (outputStream != null) outputStream.close();
            } catch (Exception ex) {}

            try {
                if (clientSocket != null) clientSocket.close();
            } catch (Exception ex) {}

            try {
                if (serverSocket != null) serverSocket.close();
            } catch (Exception ex) {}
        }
    }
}
```

### CLIENTE

```java
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class Client {

    public static void main(String[] args) {
        // Se debe indicar el puerto al que debe mandar la
        // solicitud de conexión en el cliente además de la
        // dirección IP del servidor, en este caso como
        // ambos procesos se encuentran en la misma maquina
        // podemos usar la IP "localhost", pero en caso de
        // querer conectarnos a una dirección en concreto
        // tendremos que indicarla, como por ejemplo:
        // 192.168.0.111
        int          port         = 12345;
        String       host         = "localhost";
        Socket       socket       = null;
        InputStream  inputStream  = null;
        OutputStream outputStream = null;

        try {
            // Establecemos la conexión con el servidor
            // especificado, en caso de que no se
            // encuentre lanzará una excepción de tipo
            // UnknownHostException y si ocurre algún
            // problema de tipo IO lanzará IOException.
            socket = new Socket(host, port);

            // Obtenemos los flujos de salida y entrada,
            // teniendo en cuenta que el de salida se debe
            // obtener antes que el se entrada ya que si
            // no, no funciona.
            outputStream = socket.getOutputStream();
            inputStream  = socket.getInputStream();

            // Aquí pondríamos el código que queramos
            // que se ejecute en el transcurso de la
            // comunicación.

        } catch (UnknownHostException ex) {
            // En caso de que ocurra una excepción de tipo
            // UnknownHostException imprimimos el mensaje
            // de error, en un caso real tendremos que poner
            // que queremos que se haga en caso de error o
            // dejar que se propague.
            ex.printStackTrace();
        } catch (IOException ex) {
            // En caso de que ocurra una excepción de tipo
            // IOException imprimimos el mensaje de error,
            // en un caso real tendremos que poner que
            // queremos que se haga en caso de error o dejar
            // que se propague.
            ex.printStackTrace();
        } finally {
            // Finalmente cerramos todos los recursos
            // usados para la conexión.
            try {
                if (inputStream != null) inputStream.close();
            } catch (Exception ex) {}

            try {
                if (outputStream != null) outputStream.close();
            } catch (Exception ex) {}

            try {
                if (socket != null) socket.close();
            } catch (Exception ex) {}
        }
    }
}
```

## TRANSMISIÓN DE OBJETOS

## CASO REAL

### SERVIDOR

```java
import java.net.ServerSocket;
import java.net.Socket;

public class ServerListenerRunnable implements Runnable {

    protected ServerSocket serverSocket = null;


    public ServerListenerRunnable(ServerSocket serverSocket) {
        this.serverSocket = serverSocket;
    }


    @Override
    public void run() {
        Socket clientSocket = null;
        Thread thread       = null;

        while (true) {
            try {
                clientSocket = this.serverSocket.accept();

                thread = new Thread(new ClientHandlerRunnable(
                    clientSocket
                ));
                thread.start();
            } catch (Exception ex) {
                // ...
            }
        }
    }
}
```

```java
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class ClientHandlerRunnable implements Runnable {

    protected Socket clientSocket = null;


    public ClientHandlerRunnable(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }


    @Override
    public void run() {
        InputStream  inputStream  = null;
        OutputStream outputStream = null;

        try {
            outputStream = this.clientSocket.getOutputStream();
            inputStream  = this.clientSocket.getInputStream();

        } catch (IOException ex) {
            ex.printStackTrace();
        } finally {
            try {
                if (inputStream != null) inputStream.close();
            } catch (Exception ex) {}

            try {
                if (outputStream != null) outputStream.close();
            } catch (Exception ex) {}

            try {
                if (clientSocket != null) clientSocket.close();
            } catch (Exception ex) {}
        }
    }
}
```

### CLIENTE
