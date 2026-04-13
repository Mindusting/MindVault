---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming/Android
title: Intents en Android
---

# INTENTS EN ANDROID

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

La clase `Intent` es la encargada de iniciar una actividad o servicio; intercambiar datos entre dos apps o componentes; o solicitar operaciones al OS.

Los usos de un *intent* se clasifican de las siguientes formas:
- **Explícita**: cuando desea arrancar un componente en concreto; se usa generalmente para iniciar otras actividades dentro de una misma app, permitiendo así "cambiar de ventana".
- **Implícita**: 

```kt
Intent intent = new Intent(
    getApplicationContext(),
    Activity2.class
);
intent.putExtra("userName", userName);
startActitivy(intent);
// Se puede finalizar la actividad.
//finish();
```
