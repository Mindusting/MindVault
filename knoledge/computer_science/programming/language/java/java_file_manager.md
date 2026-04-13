---
author: Mindusting
corrected: false
tags:
  - Programming
  - Java
  - Class
title: Clases en Java
---

# CONTROL DE ARCHIVOS

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar que las excepciones de los ejemplos no tienen por que ser capturadas en un caso rea.
> > - [ ] Documentar como escribir archivos de texto.
> > - [ ] Documentar como leer archivos de texto.
> > - [ ] Documentar como escribir archivos binarios.
> > - [ ] Documentar como leer archivos binarios.
> > - [ ] Documentar como escribir archivos de objetos.
> > - [ ] Documentar como leer archivos de objetos.

> [!help]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/java/java_files.asp) #WWW/W3Schools
> 
> YouTube:
> - [Bro Code](https://youtu.be/MwYRVKfb2M0) #WWW/YT/BroCode
> - [Coding with John](https://youtu.be/ScUJx4aWRi0) #WWW/YT/CodingWithJohn

## ARCHIVOS DE TEXTO

### ESCRITOR DE ARCHIVOS

```java
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;

public class WriteFiles {
    public static void main(String[] args) {
        FileWriter     fw = null;
        BufferedWriter bw = null;

        try {
            fw = new FileWriter("./myFile.txt");
            bw = new BufferedWriter(fw);

            bw.write("Hola mundo!");
        } catch (IOException ex) {
            System.out.println("An error ocurred.");
        } catch (Exception ex) {
            System.out.println("An error ocurred.");
        } finally {
            try {bw.close();}
            catch(Exception ex) {}

            try {fw.close();}
            catch(Exception ex) {}
        }
    }
}
```

### LECTOR DE ARCHIVOS

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class ReadFiles {
    public static void main(String[] args)
    throws IOException {
        FileReader     fr = null;
        BufferedReader br = null;

        try {
            fr = new FileReader("./myFile.txt");
            br = new BufferedReader(fr);

            String line = br.readLine();

            while (null != line) {
                System.out.println(line);
                line = br.readLine();
            }

        } catch (IOException ex) {
            System.out.println("An error ocurred.");
        } catch (Exception ex) {
            System.out.println("An error ocurred.");
        } finally {
            try {br.close();}
            catch(Exception ex) {}

            try {fr.close();}
            catch(Exception ex) {}
        }
    }
}
```

## ARCHIVOS BINARIOS

### ARRAYS DE BYTES

```java
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class App {

    public static String rutaOrigen  = "entrada.bin";
    public static String rutaDestino = "copia.bin";

    public static void oneBlock()
        throws IOException {

        byte[] data    = null;
        Path   origen  = null;
        Path   destino = null;

        origen  = Path.of(rutaOrigen);
        destino = Path.of(rutaDestino);

        data = Files.readAllBytes(origen);

        Files.write(destino, data);
    }
    
    public static void efficient()
        throws IOException {

        int                  bufferUsed = 0;
        byte[]               buffer     = null;
        BufferedInputStream  in         = null;
        BufferedOutputStream out        = null;

        buffer = new byte[64 * 1024];
        in     = new BufferedInputStream(
            new FileInputStream(rutaOrigen)
        );
        out    = new BufferedOutputStream(
            new FileOutputStream(rutaDestino)
        );

        while ((bufferUsed = in.read(buffer)) != -1) {
            out.write(buffer, 0, bufferUsed);
        }

        out.flush();

        in.close();
        out.close();
        
    }
}
```

### TIPOS PRIMITIVOS

```java
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;

public class App {
    
    public static String filePath  = "data.bin";

    public static void writeExample()
        throws IOException {

        DataOutputStream out = null;

        out = new DataOutputStream(new FileOutputStream(filePath));

        out.writeInt(42);
        out.writeDouble(3.1415926535);
        out.writeBoolean(true);
        out.writeUTF("Hola");

        out.close();
    }

    public static void readExample()
        throws IOException {

        DataInputStream in = null;

        in = new DataInputStream(new FileInputStream(filePath));

        System.out.println(in.readInt());
        System.out.println(in.readDouble());
        System.out.println(in.readBoolean());
        System.out.println(in.readUTF());

        in.close();
    }
}
```

```java
import java.io.IOException;
import java.io.RandomAccessFile;

public class AccesoAleatorio {
    public static void main(String[] args) {
        String archivo = "registro.bin";
        RandomAccessFile raf = null;
        
        raf = new RandomAccessFile(archivo, "rw");
        try {
            // Escribir 8 bytes (un long)
            raf.writeLong(123456789L);

            // Escribir un int a continuación
            raf.writeInt(2025);

            // Volver al inicio y sobreescribir el long
            raf.seek(0);          // mueve el puntero de archivo
            raf.writeLong(987654321L);

            // Ir a la posición del int (offset 8) y leerlo
            raf.seek(8);
            int valor = raf.readInt();
            System.out.println("Valor int en offset 8: " + valor);
        } catch (IOException ex) {
            System.out.println("Ha ocurrido algún problema.");
        }
    }
}
```

## ARCHIVOS DE OBJETOS

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;


public class ObjectFileManager<T> {

    public ObjectFileManager() {}

    public void write(T object, String filePath)
    throws FileNotFoundException, IOException {
        File               file = null;
        FileOutputStream   fos  = null;
        ObjectOutputStream oos  = null;

        try {
            file = new File(filePath);
            fos  = new FileOutputStream(file);
            oos  = new ObjectOutputStream(fos);

            oos.writeObject(object);
        } finally {
            try {if (null != oos) {oos.close();}}
            catch (Exception ex) {}

            try {if (null != fos) {fos.close();}}
            catch (Exception ex) {}
        }
    }
    
    @SuppressWarnings("unchecked")
    public T read(String filePath)
    throws ClassNotFoundException, IOException {
        T                 object = null;
        File              file   = null;
        FileInputStream   fis    = null;
        ObjectInputStream ois    = null;

        try {
            file = new File(filePath);
            fis  = new FileInputStream(file);
            ois  = new ObjectInputStream(fis);

            object = (T) ois.readObject();
        } finally {
            try {if (null != ois) ois.close();}
            catch (Exception ex) {}

            try {if (null != fis) fis.close();}
            catch (Exception ex) {}
        }

        return object;
    }
}
```
