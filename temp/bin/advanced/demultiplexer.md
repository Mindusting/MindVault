---
aliases: [Demultiplexor]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Binary]
---

<h1 style="text-align:center;">DEMULTIPLEXOR</h1>

---

# CHIP

```txt
   ╔═══════╗
A>─╣       ║
B>─╣ DEMUX ╠─>Y
S>─╣       ║
   ╚═══════╝
```

# ESQUEMA

%%

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

%%
