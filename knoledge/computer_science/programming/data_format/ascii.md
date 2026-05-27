---
aliases: [Codifiación de texto ASCII]
author: Mindusting
corrected: false
headerFile: true
rating: 
tags: [ASCII]
---

# CODIFIACIÓN DE TEXTO ASCII

El sexto bit de los caracteres ASCII indican si la letra está mayúsculas o minúsculas, de forma que si está en `0` es mayúsculas mientras que si está en `1` es minúsculas.

```python
def ascii_upper(text: str) -> str:
    chars: list[str] = [None for _ in range(len(text))]

    for i, char in enumerate(text):
        chars[i] = chr(ord(char) & 0b0101_1111)

    return "".join(chars)


def ascii_lower(text: str) -> str:
    chars: list[str] = [None for _ in range(len(text))]

    for i, char in enumerate(text):
        chars[i] = chr(ord(char) | 0b0010_0000)

    return "".join(chars)
```
