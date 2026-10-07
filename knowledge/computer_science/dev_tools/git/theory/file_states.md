---
aliases: [Estados de los archivos en Git]
author: Mindusting
corrected: false
headerFile: false
rating: 
tags: [Git]
---

# ESTADOS DE LOS ARCHIVOS EN GIT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO

Para comprobar en qué estado se encuentran los archivos consulta el comando [`status`](../commands/status.md).

> ![#fillall](../assets/git_file_life_cicle_state.excalidraw.md)
> Figura 8 del PDF [**Pro Git (*en*)**](https://git-scm.com/book/en/v2) (*pag. 28*).

- **Untraked**: 
    El archivo no está siendo vigilado por **Git**; este es en el estado en le que se encuentran todos los archivos nuevo a los que no le hemos indicado a **Git** que debe vigilar; para pasar desde este estado a **Staged** se puede hacer mediante el comando [`add`](../commands/add.md).
- **Unmodified**:
    El archivo no ha cambiado desde el último [`commit`](../commands/commit.md); los archivo que se encuentren en este estado no se mostrarán con el comando [`status`](../commands/status.md)
- **Modified**:
    El archivo ha sido modificado desde el último [`commit`](../commands/commit.md) y no se le ha indicado a **Git** que debe tener lo en cuenta par el próximo [`commit`](../commands/commit.md).
- **Staged**:
    El archivo está preparado para ser guardado en el próximo [`commit`](../commands/commit.md); este puede pasar al estado **Unmodified** tras hacer un [`commit`](../commands/commit.md)
