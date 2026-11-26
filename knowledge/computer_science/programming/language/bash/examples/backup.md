---
aliases: ["Ejemplo: copia de seguridad en bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:54:10
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# EJEMPLO: COPIA DE SEGURIDAD EN BASH

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html) #WWW/GNU
> - [GNU Tar](https://www.gnu.org/software/tar/manual/)

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Señales y trap en bash](../advanced/traps.md)
> - [Gestión de errores en bash](../advanced/error_handling.md)
> - [Gestión de archivos y directorios en bash](../tools/file_management.md)
> - [Automatización de scripts en linux](../tools/automation.md)

## OBJETIVO

Crear un archivo comprimido `.tar.gz` de un directorio. Se genera primero un archivo temporal y se publica el resultado sin sobrescribir un archivo existente. Se usan herramientas GNU/Linux (`realpath`, `mktemp`, `tar`, `ln`). No es un sistema completo de copias de seguridad.

## CÓDIGO

Guarda como `backup.sh`:

```bash
#!/usr/bin/env bash

if (( $# != 2 )); then
    printf 'Uso: %s ORIGEN DIRECTORIO_DESTINO\n' "$0" >&2
    exit 2
fi
if [[ ! -d $1 || ! -d $2 ]]; then
    printf 'Origen y destino deben ser directorios existentes\n' >&2
    exit 1
fi
IFS= read -r -d '' source_dir < <(realpath -ez -- "$1") || exit 1
IFS= read -r -d '' destination_dir < <(realpath -ez -- "$2") || exit 1

# No archivar todo el sistema ni guardar la copia dentro del origen.
if [[ $source_dir == / || $destination_dir == "$source_dir" || $destination_dir == "$source_dir/"* ]]; then
    printf 'El destino debe estar fuera del origen y el origen no puede ser /\n' >&2
    exit 1
fi

stamp=$(date +%Y%m%d_%H%M%S) || exit 1
archive="$destination_dir/backup_${stamp}.tar.gz"
tmp_file=$(mktemp -- "$destination_dir/.backup.XXXXXXXX") || exit 1
trap 'rm -f -- "$tmp_file"' EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

if ! tar -czf "$tmp_file" -C "$source_dir" .; then
    printf 'No se pudo crear el archivo\n' >&2
    exit 1
fi
if ! tar -tzf "$tmp_file" >/dev/null; then
    printf 'No se pudo leer el archivo creado\n' >&2
    exit 1
fi
# ln -T crea un enlace al archivo terminado y falla si el nombre existe.
if ! ln -T -- "$tmp_file" "$archive"; then
    printf 'No se pudo publicar la copia: %s\n' "$archive" >&2
    exit 1
fi
printf 'Copia creada: %s\n' "$archive"
```

## EXPLICACIÓN

`realpath -e` resuelve rutas existentes y enlaces simbólicos; `-z` termina la ruta con NUL, y `read -d ''` la conserva incluso si contiene saltos de línea. Se rechaza un destino situado dentro del origen para evitar incluir la copia en sí misma. `tar -C` cambia el directorio utilizado para archivar: se guardan rutas relativas. `mktemp` crea el archivo provisional dentro del destino y `trap` lo elimina al terminar. El enlace duro publica el archivo completo sin reemplazar otro; al eliminar el nombre temporal el enlace definitivo sigue existiendo.

## PRUEBAS

```bash
mkdir -p 'demo source' 'demo backups'
printf 'Datos de prueba\n' > 'demo source/a.txt'
bash backup.sh 'demo source' 'demo backups'
```

Para inspeccionar y restaurar, sustituye `ARCHIVO.tar.gz` por el nombre real, en un directorio vacío de prueba:

```bash
tar -tzf ARCHIVO.tar.gz
mkdir -p restored
tar -xzf ARCHIVO.tar.gz -C restored
```

> [!warning] LIMITACIONES
> Solo utiliza directorios de confianza. La comprobación de rutas no evita todas las carreras ni los alias creados mediante montajes. Los enlaces duros deben estar soportados por el sistema de archivos del destino. La lectura del listado no garantiza una copia consistente si los archivos cambian mientras se archivan, ni verifica una restauración completa. Para bases de datos activas utiliza sus mecanismos de copia; para información sensible, añade cifrado, retención y verificación de restauración. No extraigas archivos de origen desconocido sin inspeccionarlos.
