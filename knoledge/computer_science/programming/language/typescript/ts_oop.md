---
aliases:
  - OOP en TypeScript
  - Programación Orientada a Objetos en TypeScript
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - TypeScript
  - Web
---

# OOP EN TYPESCRIPT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar las clases.
> > - [ ] Explicar el constructor.
> > - [ ] Explicar la herencia.
> > - [ ] Explicar los modificadores de acceso.

> [!internal-link]- REFERENCIAS INTERNAS
> - [¿Qué es la OOP en programación?](../../fundamentals/temp-dump/pc_oop.md)

## CLASSES

Para definir una clase se usa la palabra clave `class` seguida el nombre de la propia clase, luego se definirá el cuerpo de la clase entre corchetes.

> [!syntax] SINTAXIS
> class ***\[className\]*** {***\[classBody\]***}

Un ejemplo simple de una clase es el siguiente:

```ts
class User {
    id:   number;
    name: string;
}
```

Para crear un objeto de esta, tendremos que usar la palabra clave `new`:

```ts
let user: User = new User();

user.id   = 1;
user.name = "Adelio";

console.log(user);
// SALIDA:
// User { id: 1, name: 'Adelio' }
```

## CONSTRUCTOR

Para definir el contructor se usa la palabra clave `constructor`, seguida de unos parénteses con los argumentos y unas llaves para definir el cuerpo del contructor (*al igual que con las [funciones](ts_function.md)*):

> [!syntax] SINTAXIS
> contructor(***\[args\]***) {***\[constructorBody\]***}

Veamos un ejemplo de un constructor:

```ts
class User {
    constructor(public id: number, public name: string) {}
}
```

Una umplementación más tradicional (*aunque en este caso ambas clases sean idénticas en cuanto a comportamiento*) sería la siguiente:

```ts
class User {
    public id:   number;
    public name: string;


    constructor(id: number, name: string) {
        this.id   = id;
        this.name = name;
    }
}
```

Gracias al contructor, podremos especificar los valores de los atributos en la misma línea en la que declaramos el objeto:

```ts
let user: User = new User(1, "Adelio");

console.log(user);
// SALIDA:
// User { id: 1, name: 'Adelio' }
```

### SOBRECARGA DEL CONTRUCTOR

Para sobrecargar los constructores se hace de la misma forma que con las [funciones](ts_function.md):

```ts
class User {
    public id:   number;
    public name: string;


    constructor(id: User);
    constructor(id: number, name: string);

    constructor(id: number | User, name?: string) {
        if (typeof id === "number" && typeof name === "string") {
            this.id   = id;
            this.name = name;
            return;
        }

        if (typeof id === "object") {
            this.id   = id.id;
            this.name = id.name;
            return;
        }

        throw new Error("Invalid arguments.");
    }
}
```

En el siguiente ejemplo podemos ver como funciona la sobrecarga de constructores, ya que primero creamos el objeto estableciendo los datos a pelo, mientras que en la segunda se crea otra identidad identica a la primera; se puede comprobar que son distintas por mucho que los valores son distintos porque la última comparación da como resultado `false`:

```ts
let user0: User = new User(1, "Adelio");
let user1: User = new User(user0);

console.log(user0);
console.log(user1);
console.log(user0 === user1);
// SALIDA:
// User { id: 1, name: 'Adelio' }
// User { id: 1, name: 'Adelio' }
// false
```

## HERENCIA

```ts
class Animal {
    constructor(public nombre: string) {}
    
    hablar(): void {
        console.log(`${this.nombre} hace un sonido`)
    }
}

class Perro extends Animal {
    hablar(): void {
        console.log(`${this.nombre} ladra`)
    }
}

let p = new Perro("Rex");
p.hablar();
// SALIDA:
// Rex ladra
```

## MODIFICADORES DE ACCESO

- `public`: accesible en todas partes.
- `private`: solo dentro de la clase.
- `protected`: accesible en la clase y subclase.

```ts
class Cuenta {
    private saldo: number = 0;
    
    addSaldo(cantidad: number) {
        this.saldo += cantidad;
    }
    
    getSaldo() {
        return this.saldo;
    }
}

let c = new Cuenta();
c.addSaldo(100);
console.log(c.getSaldo());
// SALIDA:
// 100

//console.log(c.saldo);
// ERROR
```

## ASERCIONES DE TIPO

```ts
let valor: any = "Hola mundo!";
let long: number = (valor as string).length;

console.log(long);
// SALIDA:
// 12
```

## UTILIDADES

`Partial` combierte todas las propiedades en opcionales.

```ts
interface User {
    id: number;
    name: string;
}

let u = Partial<User> = {}; // Usuario vacio.
```

`Readonly` hace que todas las propiedades sean de solo lectura.

```ts
interface User {
    id: number;
    name: string;
}

let u = Readonly<User> = {id: 1}; // Error
```
