---
aliases: [Multiplexador y Demultiplexor, Multiplexador, Demultiplexador, Multiplexer, Demultiplexer, MUX, DEMUX]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Binary]
---

# MULTIPLEXOR Y DEMULTIPLEXOR

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

## MULTIPLEXADOR

```txt
   ╔═════╗
A>─╣     ║
B>─╣ MUX ╠─>Y
S>─╣     ║
   ╚═════╝
```

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

## DEMULTIPLEXADOR

```txt
   ╔═══════╗
A>─╣       ╠─>Y
   ║ DEMUX ║
S>─╣       ╠─>X
   ╚═══════╝
```
