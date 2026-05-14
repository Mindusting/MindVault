---
author: Mindusting
corrected: false
headerFile: false
tags:
  - Programming
  - Python
  - Singleton
title: Singleton en Python
---

# SINGLETON EN PYTHON

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!faq]- FAQ
> - [¿Qué son los *singleton* en programación?](../../fundamentals/temp-dump/design_patterns/pc_dp_singleton.md)

Para crear una [clase](py_class.md) *singleton* en **Python** se puede hacer de varias forma, una de ellas es mediante los [**decoradores**](py_decorator.md):

```python
def singleton(class_):
    instances = {}
    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance
```
