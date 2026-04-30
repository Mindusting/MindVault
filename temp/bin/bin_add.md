---
author: Mindusting
corrected: false
tags:
  - Binary
title: Sumas en binario
---

<h1 style="text-align:center;">SUMAR EN BINARIO</h1>

---

> [!fail] ESTE APARTADO ESTÁ INCOMPLETO

| E | Y | X | S | L |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 1 | 0 |
| 0 | 1 | 0 | 1 | 0 |
| 0 | 1 | 1 | 0 | 1 |
| 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 1 | 0 | 1 |
| 1 | 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 1 |

%%

```mermaid
flowchart TD
    x((("X")))
    y((("Y")))
    e((("E")))
    s((("S")))
    l((("L")))
    xor1["XOR"]
    xor2["XOR"]
    and1["AND"]
    and2["AND"]
    or["OR"]

    x --> xor1 --> xor2 --> s
    x --> and2 --> or ~~~ s
    y --> xor1 --> and1 --> or --> l
    y --> and2
    e --> xor2
    e --> and1
    e ~~~ xor1
```

%%

```txt
X────╦──╦═════╗
     │  ║ XOR ╠──╦───╦═════╗
Y─╦──┼──╩═════╝  │   ║ XOR ╠───────────S
  │  │           │ ┌─╩═════╝
E─┼──┼───────────┼─╣
  │  │           │ └─╦═════╗
  │  │           │   ║ AND ╠─┐
  │  │           └───╩═════╝ └─╦════╗
  │  │                         ║ OR ╠──L
  │  └───────────────╦═════╗ ┌─╩════╝
  │                  ║ AND ╠─┘
  └──────────────────╩═════╝
```

```txt
 101
  11 +
-------
1000
```
