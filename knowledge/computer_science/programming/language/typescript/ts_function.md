---
aliases:
  - Funciones en TypeScript
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - TypeScript
  - Web
  - Function
---

# FUNCIONES EN TYPESCRIPT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO
> > - [ ] Explicar la sobrecarga de funciones.

> [!external-link]- REFERENCIAS WEB
> - [W3 Schools](https://www.w3schools.com/typescript/typescript_functions.php) #WWW/W3Schools

> [!syntax] SINTAXIS
> functino ***\[funcName\]***(***\[funcParameters\]***): ***\[returnType\]*** { ***\[code\]*** }

## SOBRECARGA

```ts
function pitagoras(x: number, y: number);
function pitagoras(x: number, y: number, z: number);

function pitagoras(x: number, y: number, z?: number) {
    if (typeof z === "number") {
        return (x * x) + (y * y) + (z * z);
    }
    return (x * x) + (y * y);
}
```

```ts
console.log(pitagoras(3, 4));
console.log(pitagoras(3, 4, 5));
// SALIDA:
// 25
// 50
```
