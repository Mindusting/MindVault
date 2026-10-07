---
aliases: [Números de coma flotante]
author: Mindusting
corrected: false
creationDate: 2026-09-24 09:37:56
headerFile: false
modificationDate: 2026-09-24 09:39:04
rating: 
tags: []
---

# NÚMEROS DE COMA FLOTANTE

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

%%

Este es un ejemplo de como el problema de redondeo puede afectar a los resultados:

```python
import math

print(math.sin(math.radians(30)))
# SALIDA:
# 0.49999999999999994
```

El resultado real tendría que ser 0.5, pero debido a que el número PI es un número irracional y este se usa para hacer la conversion de grados a radianes, el restulado de la conversión no es totalmente precioso, haciendo que el resultado sea 0.49999999999999994 en vez de 0.5.

%%
