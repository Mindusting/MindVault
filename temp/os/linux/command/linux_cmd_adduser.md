---
author: Mindusting
corrected: false
tags:
  - OS
  - Linux
  - Bash
  - Command/Users
title: Crear de usuarios en Linux
---

# CREAR USUARIOS EN LINUX

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

Para crear usuarios en **Linux** se usa el comando `adduser`, este requiere del prefijo `sudo` ya que sino, no tendremos los permisos para poder ejecutarlo; seguido del comando `adduser` y el nombre (*que tendrá de forma interna para identificarlo*); opcionalmente podemos indicar el grupo al que va a pertenecer:

> [!abstract] SINTAXIS
> sudo adduser ***\[username\] \{\[group\]\}***

> [!note] NOTA
> Si el usuario ya existe no lo indicará y no realizará ningún cambio; si el usuario ya existe e indicamos el nombre de un grupo, el usuario se añadirá al grupo indicado.
