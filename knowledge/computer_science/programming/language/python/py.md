---
aliases: [Lenguaje Python 🐍]
author: Mindusting
corrected: false
description: |-
  Documentación de Python; conteniendo: 
  - Los aspectos básicos del lenguaje.
  - Módulos tanto internos como externos.
headerFile: true
logo: imgs/py_logo.png
rating: 
tags: [Programming, Python]
---

<h1 align="center">
<span style="color:#48b;">PYT</span><span style="color:#ed5;">HON</span>
</h1>

![#logo](../../../../../imgs/py_logo.png)

---

# PYTHON

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> > [!todo] #TODO
> > - [ ] Documentar como [ejecutar funciones de C en Python](https://stackoverflow.com/questions/16647186/calling-c-functions-in-python) y documentarlo.
> > - [ ] Documentar como [trabajar sobre la red](https://youtu.be/DFTwB2nAexs) desde Python.
> > - [ ] Documentar el módulo `platform`:
> > ```python
> > import os
> > import sys
> > import platform
> > 
> > print(os.path)
> > print(os.name)
> > print(sys.platform)
> > print(os.getcwd())
> > #os.chdir("..") # cd command
> > print(os.listdir())
> > #os.mkdir("tmp") # mkdir command
> > """
> > for module in sys.modules:
> >     print(module)
> > #"""
> > print(platform.architecture())
> > print(platform.machine())
> > print(platform.processor()) # CPU
> > print(platform.platform()) # OS version
> > print(platform.system()) # OS
> > ```

> [!external-link]- REFERENCIAS WEB
> - [Python](https://docs.python.org/es/3/) #WWW/Python
> - [TpointTech](https://www.tpointtech.com/python-tutorial) #WWW/TpointTeach
> - [Linuxize](https://linuxize.com/tags/python) #WWW/Linuxize

> [!seealso]- Ver también
> - [Comando `make`:](../../../../../temp/os/linux/command/make.md)
>     Sirve para poder trabajar sobre proyectos de programación más facilmente.
> - [Git:](../../../dev_tools/git/git.md)
>     Es un sistema de control de versiones, permite tener un desarrollo de proyecto más estructurado.

%%

```txt
/python
|- python.md
|
|-/core
| |- comments.md
| |- variables.md
| |- flow_control.md
| |- functions.md : Debe incluir lambda.
| |- oop.md
| |- exceptions.md
| |- file_management.md
| |- modules_and_packages.md
| |- decoratos.md
| |
| |-/data_types
| | |- int.md
| | |- float.md
| | |- bool.md
| | |- str.md
| | |- list.md
| | |- tuple.md
| | |- dict.md
| | |- set.md
| |
| |-/builtins
| | |- sorted.md
| | |- map.md : Grupo funcional.
| | |- filter.md : Grupo funcional.
| | |- any : Grupo iterables.
| | |- all : Grupo iterables.
| | |- zip : Grupo iterables.
| | |- enumerate : Grupo iterables.
|
|-/modules
| |- modules.md
| |
| |-/built_it
| | |- os.md : Pensa en como plantear los subpaquetes.
| | |- sys.md
| | |- random.md
| | |- json.md
| | |- time.md
| | |- sqlite3.md
| | |- struct.md
| | |- re.md
| | |- socket.md
| |
| |-/third_party
| | |- numpy.md
| | |- opensimplex.md
```

%%

## ÍNDICE

- [ARCHIVOS DE PYTHON 📄](py_files.md)
- [COMENTARIOS 💬](basic/comment.md)
- [OUTPUT POR CONSOLA 🖥️](basic/builtins/print.md)
- [VARIABLES 💾](basic/variable.md)
- [INPUT POR CONSOLA ⌨️](basic/builtins/input.md)
- [SLICES 📏](basic/builtins/slice.md)
    - [LISTAS](basic/data_types/list.md)
    - [TUPLAS](basic/data_types/tuple.md)
    - [SET](basic/data_types/set.md)
    - [DICCIONARIOS](basic/data_types/dict.md)
- [CONDICIONALES 🚦](py_conditionals.md)
- [BUCLES ➰](basic/loop.md)
- [DOC-STRING](basic/docstring.md)
- [FUNCIONES 📞](py_func.md)
    - [MAP 🗺](basic/builtins/map.md)
    - [FILTRO](basic/builtins/filter.md)
    - [ZIP](basic/builtins/zip.md)
    - [ENUMERATE](basic/builtins/enumerate.md)
    - [GENERADORES](basic/generator.md)
    - [DECORADORES](basic/decorator.md)
- [SWITCH](basic/switch.md)
- [ASSERT](basic/assert.md)
- [BREAKPOINT 🔴](basic/breakpoint.md)
- [CLASES 📦](py_class.md)
- [EXCEPCIONES ⚠️](basic/exception.md)
- [MÓDULOS 🛄](py_module.md)
    - [VENV](basic/venv.md)
    - [COMANDO PIP](basic/pip.md)
- [ARCHIVOS EXTERNOS](basic/builtins/open.md)
- [GUI 🖼](py_gui.md)
    - [MANEJO DE IMÁGENES](py_image.md)

## MÓDULOS

- [COLORAMA](colorama/py_colorama.md)
- [CSV](csv/py_csv.md)
- [DATETIME](datetime/py_datetime.md)
- [EXCEL 🍫](openpyxl/py_openpyxl.md)
- [HASHLIB](module/standar/hashlib/hashlib.md)
- [HILOS 🧵](threading/py_threading.md)
- [JSON 🗃](module/standar/json/json.md)
- [MANIM](py_manim.md)
- [MATH 🧮](module/standar/math/math.md)
- [MATHPLOTLIB](py_matplotlib.md)
- [NUMPY 🧮](module/third_party/numpy/numpy.md)
- [OPENSIMPLEX](module/third_party/opensimplex/opensimplex.md)
- [OS](module/standar/os/os.md)
    - [PATH](module/standar/os/path/path.md)
- [PANDAS 📈](module/third_party/pandas/pandas.md)
- [PASSWORD 🔑](module/standar/getpass/getpass.md)
- [PATHFINDING](py_pathfinding.md)
- [PILLOW](py_pillow.md)
- [PORTA PAPELES 📋](module/third_party/clipboard/clipboard.md)
- [PSUTIL](module/third_party/psutil/psutil.md)
- [PYAUTOGUI 🖱️](module/third_party/pyautogui/pyautogui.md)
- [PYGAME 🕹️](module/third_party/pygame/pygame.md)
    - [MIXER](module/third_party/pygame/mixer/mixer.md)
- [QR 🔗](module/third_party/qrcode/qrcode.md)
- [RANDOM 🎲](module/standar/random/random.md)
- [RE](module/standar/re/re.md)
- [SOCKET](module/standar/socket/py_socket.md)
- [SQLCIPHER3 🛢](module/third_party/pysqlcipher3/pysqlcipher3.md)
- [SQLITE3 🛢](module/standar/sqlite3/sqlite3.md)
- [STRUCT](module/standar/struct/struct.md)
- [SHUTIL](module/standar/shutil/shutil.md)
- [SYS](module/standar/sys/sys.md)
- [TIME ⌛](module/standar/time/time.md)
- [XML](module/standar/xml/xml.md)
- [YAML](module/third_party/yaml/yaml.md)
- [ZIPFILE 🗄️](zipfile/py_zipfile.md)
