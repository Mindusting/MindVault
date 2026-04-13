---
aliases: [Número decimales aleatorios en C]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [C, Programming]
---

# NÚMERO DECIMALES ALEATORIOS EN C

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

```c
// file: rand.c
#include <stdlib.h>
#include <stdint.h>

#include "rand.h"

float randf(void) {
    //                       randMask    exponent
    uint32_t num = (rand() & 0x7fffff) | 0x3f800000;
    return *((float*)(&num)) - 1;
}

double randd(void) {
    uint64_t num = ((uint64_t)(rand()) << 32) | rand();
    //           randMask           exponent
    num = (num & 0xfffffffffffff) | 0x3ff0000000000000;
    return *((double*)(&num)) - 1;
}
```

```c
// file: rand.h
#ifndef RAND_H
#define RAND_H

float randf(void);
double randd(void);

#endif
```
