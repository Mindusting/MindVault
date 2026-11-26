---
aliases: ["Soluciones de los ejercicios de bash"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:24:59
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# SOLUCIONES DE LOS EJERCICIOS DE BASH

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](bash.md)
> - [Ejercicios de bash](exercises.md)
> - [Chuleta de bash](bash_cheatsheet.md)

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Shell-Scripts.html) #WWW/GNU

## EJERCICIOS 1–5

### 1. ARGUMENTOS

```bash
if (( $# != 1 )); then
    printf 'Uso: %s NOMBRE\n' "$0" >&2
    exit 2
fi
printf 'Hola %s\n' "$1"
```

Las comillas conservan el nombre completo como un argumento. Un argumento vacío cuenta como uno; si además quieres rechazarlo, comprueba `[[ -n $1 ]]` después de validar la cantidad.

### 2. COMILLAS

Sin comillas se obtienen `<uno>` y `<dos>` en líneas distintas. Con comillas, `<uno dos>` en una línea. La expansión sin comillas también permitiría globbing si el valor contuviera comodines.

### 3. ARITMÉTICA

```bash
raw=${1-}
if [[ ! $raw =~ ^[0-9]{1,6}$ ]]; then
    printf 'Número no válido\n' >&2
    exit 2
fi
number=$((10#$raw))
if (( number % 2 == 0 )); then
    printf 'Par\n'
else
    printf 'Impar\n'
fi
```

La expresión regular restringe los datos a dígitos decimales y limita su tamaño; `10#` evita la interpretación octal de `008`.

### 4. ARRAYS

```bash
items=('uno dos' '*' '')
for item in "${items[@]}"; do
    printf '<%s>\n' "$item"
done
```

Se obtienen `<uno dos>`, `<*>` y `<>`. El último argumento vacío no desaparece.

### 5. FUNCIONES

```bash
has_text() {
    [[ -n ${1-} ]]
}
if has_text 'hola'; then
    printf 'Hay texto\n'
fi
```

El estado de la última prueba se convierte en el de la función. `return 0` expresa éxito; para producir datos se utiliza normalmente stdout.

## EJERCICIOS 6–9

### 6. REDIRECCIONES

```bash
{ printf 'datos\n'; printf 'error\n' >&2; } > demo.log 2>&1
{ printf 'datos\n'; printf 'error\n' >&2; } 2>&1 > demo.log
```

Primera orden: ambos mensajes al archivo. Segunda: `error` va al stdout original (normalmente terminal), `datos` al archivo. `2>&1` copia el destino actual, no establece un vínculo dinámico entre ambos descriptores.

### 7. LECTURA

```bash
while IFS= read -r line || [[ -n $line ]]; do
    printf '<%s>\n' "$line"
done < demo.txt
```

`IFS=`, `-r` y la condición alternativa cubren los tres requisitos.

### 8. RUTAS

```bash
while IFS= read -r -d '' file; do
    printf '%q\n' "$file"
done < <(find . -type f -name '*.txt' -print0)
```

El delimitador NUL no puede formar parte del nombre de un archivo. `%q` presenta rutas con escapes legibles por Bash. Para una búsqueda cuyo resultado deba ser completo, captura primero la lista en un temporal y comprueba `find` (consulta [lectura de archivos](io/reading_files.md)).

### 9. PIPEFAIL Y SUBSHELL

```bash
false | true
printf '%d\n' "$?" # 0
(
    set -o pipefail
    false | true
    printf '%d\n' "$?" # 1
)
count=0
printf '%s\n' a b | while IFS= read -r line; do
    count=$((count + 1))
done
printf '%d\n' "$count" # normalmente 0
```

Por defecto el bucle del pipeline se ejecuta en un subshell. La sustitución de procesos puede mantener el bucle en el shell actual; `lastpipe` también puede cambiar el comportamiento.

## EJERCICIOS 10–12

### 10. OPCIONES

La solución completa está desarrollada en [opciones de línea de comandos](advanced/command_line_options.md). El punto esencial es usar `getopts ':vn:h'`, distinguir `:` y `?`, desplazar los argumentos con `shift "$((OPTIND - 1))"` y comprobar que `$#` sea cero.

### 11. TEMPORALES

```bash
#!/usr/bin/env bash
tmp_dir=$(mktemp -d) || exit 1
trap 'rm -rf -- "$tmp_dir"' EXIT
printf 'Temporal\n' > "$tmp_dir/demo.txt" || exit 1
printf 'Directorio: %s\n' "$tmp_dir"
exit 1
```

Comprueba desde otro shell que el directorio mostrado ya no existe. `trap` se registra solo después de crear correctamente el directorio y actúa también con `exit 1`.

### 12. FRECUENCIAS

```bash
#!/usr/bin/env bash
if (( $# != 1 )); then
    printf 'Uso: %s ARCHIVO\n' "$0" >&2
    exit 2
fi
set -o pipefail
if ! result=$(LC_ALL=C sort -- "$1" | uniq -c | sort -nr); then
    printf 'Error procesando el archivo\n' >&2
    exit 1
fi
if [[ -n $result ]]; then
    printf '%s\n' "$result"
fi
```

`pipefail` permite detectar fallos de `sort` aunque el último programa termine correctamente. La salida se captura antes de mostrarla; en archivos muy grandes puede ser mejor almacenarla temporalmente. Una entrada vacía no produce una línea ficticia.
