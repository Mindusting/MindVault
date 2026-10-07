---
aliases: [Instalación de Git]
author: Mindusting
corrected: false
description: |-
    Se describe el proceso de instalación de Git.
headerFile: false
rating:
tags: [Git]
---

# INSTALACIÓN DE GIT

Para instalar **Git** en nuestro ordenador, tendremos que seguir unos pasos distintos dependiendo del sistema operativos que tengamos.

## INSTALACIÓN EN LINUX (DEBIAN)

Antes de comenzar con la instalación es recomendable ejecutar el siguiente comando para que se compruebe las posibles dependencias:

```bash
sudo apt update
```

Para comenzar con la instalación tendremos que ejecutar el siguiente comando:

```bash
sudo apt install git
```

Una vez terminada la instalación podemos comprobar que responde correctamente revisando la [versión](../commands/version.md) que hemos instalado, para ello ejecutaremos el siguiente comando:

```bash
git version
```

Si todo va bien, tendría que salir algo parecido a:

```txt
git version X.XX.X
```

En donde `X` serán número que indiquen la versión.
