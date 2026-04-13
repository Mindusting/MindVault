---
author: Mindusting
corrected: false
tags:
  - OS/Linux
title: Desktop en Linux
---

# DESKTOP EN LINUX

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> - [ciberciti](https://www.cyberciti.biz/howto/how-to-install-and-edit-desktop-files-on-linux-desktop-entries) #WWW/ciberciti
> 
> YouTube:
> - [Abstract programmer](https://youtu.be/gdYp2d_p8T0) #WWW/YT/AbstractProgrammer

Para añadir nuevos programa tendremos que ir al siguiente directorio.

```bash
cd ~/.local/share/applications
```

> [!note] NOTA
> Los archivos `.desktop` siguen un formato parecido a [**INI**](../../../knoledge/computer_science/programming/data_format/ini.md), pero no es el mismo, este tiene ciertas restricciones.

```ini
[Desktop Entry]
Type=Application
Name=AppName
Exec=ExecPath
Icon=PNGPath
Terminal=false
StartupNotify=false
Categories=Development
```

Para actualizar el registro de archivos `.desktop` se usa el siguiente comando:

```bash
sudo update-desktop-database
```
