---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming/Concept
  - DesignPattern
title: Retorno anticipado en programación
---

# RETORNO ANTICIPADO EN PROGRAMACIÓN

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

```python
def contains_all_bocals(text: str) -> bool:
    result = False
    if 'a' in text:
        if 'e' in text:
            if 'i' in text:
                if 'o' in text:
                    if 'u' in text:
                        result = True
                    else:
                        result = False
                else:
                    result = False
            else:
                result = False
        else:
            result = False
    else:
        result = False
    return result
```

```python
def contains_all_bocals(text: str) -> bool:
    if 'a' not in text:
        return False
    if 'e' not in text:
        return False
    if 'i' not in text:
        return False
    if 'o' not in text:
        return False
    if 'u' not in text:
        return False
    return True
```

```python
def contains_all_bocals(text: str) -> bool:
    return (
        'a' in text and
        'e' in text and
        'i' in text and
        'o' in text and
        'u' in text
    )
```

```python
def contains_all_bocals(text: str) -> bool:
    return all(map(lambda char: char in text, "aeiou"))
```
