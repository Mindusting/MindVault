---
aliases: [Multiplexador]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Binary]
---

<h1 style="text-align:center;">MULTIPLEXOR</h1>

---

# CHIP

```txt
   ╔═════╗
A>─╣     ║
B>─╣ MUX ╠─>Y
S>─╣     ║
   ╚═════╝
```

# ESQUEMA

```txt
A>────────────╦═════╗
              ║ AND ╠─┐
   ┌──────────╩═════╝ └─╦════╗
   │                    ║ OR ╠─>Y
B>─┼──────────╦═════╗ ┌─╩════╝
   │ ╔═════╗  ║ AND ╠─┘
S>─╩─╣ NOT ╠──╩═════╝
     ╚═════╝
```
