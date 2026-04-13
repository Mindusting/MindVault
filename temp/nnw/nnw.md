---
alias: Neuronal Network
author: Mindusting
corrected: false
tags:
  - Programming
  - NeuronalNetwork
title: Redes neuronales
---

# REDES NEURONALES

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [sentdex (Neural Networks from Scratch in Python)](https://www.youtube.com/playlist?list=PLQVvvaa0QuDcjD5BAw2DxE6OF2tius3V3) #WWW/YT/sentdex

![#center](assets/nnw_simple_neuron_schema.excalidraw.md)

```py
def main() -> None:
    neurons = [
        Neuron( 1.0,  0.0),
        Neuron( 0.5,  0.0),
        Neuron(-0.5,  1.0),
        Neuron( 0.1,  0.5),
        Neuron( 4.0, -1.0),
    ]

    for neuron in neurons:
        print(neuron)
        for i in range(10):
            width: float = 10
            res:   int   = int(round(neuron.process(i * 0.1) * 20))
            res:   int   = min(res, 20)
            res:   int   = max(res, 0)
            print(f"|{'#' * res:<{width * 2}}|")
        print()


class Neuron:
    def __init__(self, weight: float, bias: float):
        assert isinstance(weight, (float, int))
        assert isinstance(bias,   (float, int))
        self.weight: float = weight
        self.bias:   float = bias

    def __str__(self):
        return f"Neuron({self.weight}, {self.bias})"

    def process(self, data: float) -> float:
        assert isinstance(data, (float, int))
        return data * self.weight + self.bias


if __name__ == "__main__":
    main()
```

```txt
Neuron(1.0, 0.0)  
|                    |  
|##                  |  
|####                |  
|######              |  
|########            |  
|##########          |  
|############        |  
|##############      |  
|################    |  
|##################  |  
  
Neuron(0.5, 0.0)  
|                    |  
|#                   |  
|##                  |  
|###                 |  
|####                |  
|#####               |  
|######              |  
|#######             |  
|########            |  
|#########           |  
  
Neuron(-0.5, 1.0)  
|####################|  
|################### |  
|##################  |  
|#################   |  
|################    |  
|###############     |  
|##############      |  
|#############       |  
|############        |  
|###########         |  
  
Neuron(0.1, 0.5)  
|##########          |  
|##########          |  
|##########          |  
|###########         |  
|###########         |  
|###########         |  
|###########         |  
|###########         |  
|############        |  
|############        |  
  
Neuron(4.0, -1.0)  
|                    |  
|                    |  
|                    |  
|####                |  
|############        |  
|####################|  
|####################|  
|####################|  
|####################|  
|####################|
```
