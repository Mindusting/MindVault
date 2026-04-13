---
author: Mindusting
corrected: false
tags:
  - OS/Linux/BASH
title: XXD en BASH
---

# BASH EN LINUX

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

- `-r` (*reverse*): invierte el proceso (*de __HEX__ a __BIN__*).
- `-p`: sirve para indicar que queremos que se trate dirctamente como valor en **HEX** ya que sin el obtendremos un una visualización del contenido de un archivo.

Impresion de contenido en **HEX**:

```bash
xxd readme.txt
```

Combersion de archivos:

```bash
xxd -p img.png img.hex
xxd -r -p img.hex img.png
```
