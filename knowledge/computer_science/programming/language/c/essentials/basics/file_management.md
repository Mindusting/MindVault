---
author: Mindusting
corrected: false
tags:
  - Programming
  - C
title: Manejo de archivos con C
---

# MANEJO DE ARCHIVOS CON C

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

```c
#include <stdio.h>

int main() {
    char *fpath = "data.txt";

    FILE *fptr = fopen(fpath, "r");

    if (fptr == NULL) {
        printf("No se ha podido abrir el archivo.\n");
        return 0;
    }

    char buffer[1024];

    while (fgets(buffer, sizeof(buffer), fptr)) {
        printf("%s", buffer);
    }

    fclose(fptr);
    return 0;
}
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char *freadall(FILE *file) {
    if (NULL == file) return NULL;
    
    const float GROW_FACTOR = 1.5f;
    char buffer[512];
    size_t dataHead = 0;
    size_t dataSize = 1024;
    char *data = malloc(dataSize);

    if (NULL == data) return NULL;

    while (1) {
        char *result = fgets(buffer, sizeof(buffer), file);

        if (NULL == result) break;

        if (dataSize - dataHead < sizeof(buffer)) {
            char *oldData  = data;
            size_t oldSize = dataSize;
            dataSize = dataSize * GROW_FACTOR;
            data = malloc(dataSize);

            if (NULL == data) {
                free(oldData);
                return NULL;
            }

            memcpy(data, oldData, oldSize);
            free(oldData);
        }

        size_t bufferStringLenght = strlen(buffer);
        
        for (size_t i = 0; i < bufferStringLenght; i++) {
            data[dataHead + i] = buffer[i];
        }
        dataHead += bufferStringLenght;
    }

    return data;
}
```
