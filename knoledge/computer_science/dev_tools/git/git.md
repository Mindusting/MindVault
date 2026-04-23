---
aliases: [Git]
author: Mindusting
corrected: false
headerFile: true
logo: imgs/git_logo.png
rating:
tags: [Git]
---

<h1 align="center" style="color:df4c37;">GIT</h1>

![#logo](../../../../imgs/git_logo.png)

---

# GIT

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Hay que hacerle un logo a esta documentación.
> > - [ ] Explicar para qué sirve git.
> > - [ ] Explicar el funcionamiento interno de git.
> > - [ ] Explicar como instalar git.
> > - [ ] Explicar el comando `init`.
> > - [ ] Explicar el comando `status`.
> > - [ ] Explicar el comando `add`.
> > - [ ] Explicar el comando `commit`.
> > - [ ] Explicar el comando `log`.
> > - [ ] Explicar el comando `reset`.
> > - [ ] Explicar el comando `cherry-pick`.
> > git reset --hard ***\[commit_hex_code\]***

> [!external-link]- REFERENCIAS WEB
> - [Git (Doc)](https://git-scm.com/docs) #WWW/Git
> - [Git (PDF)](https://git-scm.com/book/en/v2) #WWW/Git
> - [W3 Schools](https://www.w3schools.com/git/default.asp?remote=github) #WWW/W3Schools
> - [Linuxize](https://linuxize.com/tags/git) #WWW/Linuxize
> 
> YouTube:
> - [LearnThatStack](https://youtu.be/Ala6PHlYjmw) #WWW/YT/LearnThatStack
> - [codingjerk](https://youtu.be/G3NJzFX6XhY) #WWW/YT/codingjerk
> - [pildorasinformaticas](https://www.youtube.com/playlist?list=PLU8oAlHdN5BlyaPFiNQcV0xDqy0eR35aU) #WWW/YT/pildorasinformaticas
> - [MoureDev by Brais Moure](https://youtu.be/3GymExBkKjE) #WWW/YT/MoureDevByBraisMoure
> - [Informatica Live](https://youtu.be/NvazARiMEIw) #WWW/YT/InformaticaLive

**Git** es un sistema de control de versiones distribuido. Permite guardar el historial de cambios de un proyecto, trabajar en equipo y volver a estados anteriores del código fácilmente.

## TEORÍA

- [Instalación](theory/installation.md)
- [Estados de los archivos](theory/file_states.md)
- [Commits](theory/commits.md)
- [Etiquetas (Tags)](theory/tags.md)
- [Ramas](theory/branches.md)
- [Merges](theory/merges.md)
- [Stash (Alijo)](theory/stashes.md)

## COMANDOS

```base
filters:
  and:
    - file.folder == "knoledge/computer_science/dev_tools/git/commands"
formulas:
  Comando: file
  Descripción: 'if(file.properties.description, "Descripción: "+file.properties.description, "")'
views:
  - type: list
    name: List
    order:
      - formula.Comando
      - formula.Descripción
    sort: []
    indentProperties: true
    markers: bullet

```

%%

- [`add`](commands/add.md)
- [`branch`](commands/branch.md)
- [`checkout`](commands/checkout.md)
- [`commit`](commands/commit.md)
- [`config`](commands/config.md)
- [`diff`](commands/diff.md)
- [`init`](commands/init.md)
- [`log`](commands/log.md)
- [`merge`](commands/merge.md)
- [`mv`](commands/mv.md)
- [`reset`](commands/reset.md)
- [`rm`](commands/rm.md)
- [`shortlog`](commands/shortlog.md)
- [`status`](commands/stash.md)
- [`status`](commands/status.md)
- [`switch`](commands/switch.md)
- [`tag`](commands/tag.md)
- [`version`](commands/version.md)

%%

## ÍNDICE

- [Instalación de Git](theory/installation.md)
- [Versión](commands/version.md)
- [Configuración](commands/config.md)
- [Crear repositorios](commands/init.md)
- [Añadir archivos](commands/add.md)
- [Estado de configuración](commands/status.md)
- [Ignorar archivos](theory/gitignore.md)
- [Clonar repositorio](theory/remote.md)

%%

## RESTABLECER

> [!abstract] SINTAXIS
> git reset --hard ***\[code\]***

## SUBIR CAMBIOS

> [!abstract] SINTAXIS
> git push -u original main

## BAJAR CAMBIOS

> [!abstract] SINTAXIS
> git pull

## SUBIR RAMA A GITHUB

> [!abstract] SINTAXIS
> git push -u origin ***\[nombreDeRama\]***

%%
