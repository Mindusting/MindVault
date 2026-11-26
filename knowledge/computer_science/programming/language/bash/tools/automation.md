---
aliases: ["Automatización de scripts en linux"]
author: Mindusting
corrected: false
creationDate: 2026-11-25 12:00:00
headerFile: false
modificationDate: 2026-11-26 12:57:11
rating:
tags: [BashScript, OS/Linux/BASH, Programming]
---

# AUTOMATIZACIÓN DE SCRIPTS EN LINUX

> [!external-link]- REFERENCIAS WEB
> - [Manual de GNU Bash](https://www.gnu.org/software/bash/manual/html_node/Environment.html) #WWW/GNU
> - [systemd.timer](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html)
> - [crontab(5)](https://man7.org/linux/man-pages/man5/crontab.5.html)

> [!seealso]- MIRA TAMBIÉN
> - [Bash Script](../bash.md)
> - [Variables de entorno en bash](../environment/environment_variables.md)
> - [Gestión de errores en bash](../advanced/error_handling.md)
> - [Estructura de un script en bash](../advanced/script_structure.md)

## DEFINICIÓN

Automatizar consiste en ejecutar tareas sin intervención manual en cada ocasión. Bash permite implementar la tarea, pero su programación periódica corresponde a servicios como cron o los temporizadores de systemd.

## CRON

`crontab -e` permite editar la tabla de tareas del usuario. Una entrada contiene cinco campos temporales y una orden:

```text
MIN HOUR DAY_OF_MONTH MONTH DAY_OF_WEEK command
```

Por ejemplo, para ejecutar diariamente a las 02:30 un script del usuario ficticio `ana`:

```cron
30 2 * * * /bin/bash /home/ana/scripts/report.sh >> /home/ana/report.log 2>&1
```

Adapta rutas y horario. El script debe existir y el servicio cron debe estar disponible. Cron no suele proporcionar el mismo entorno que un terminal interactivo. Usa rutas absolutas, declara `PATH` si lo necesitas y no dependas de `.bashrc`. Las reglas para día del mes y de la semana pueden combinarse de forma especial; consulta `man 5 crontab`. En implementaciones habituales `%` sin escapar tiene tratamiento especial dentro de la orden.

## SYSTEMD

Un temporizador (`.timer`) puede activar una unidad de servicio (`.service`). Permite gestionar dependencias y consultar diagnósticos con herramientas de systemd. Los servicios de usuario y del sistema tienen contextos y permisos distintos. Consulta `man systemd.timer` y `man systemd.service` antes de instalarlos.

## EVITAR EJECUCIONES SIMULTÁNEAS

En GNU/Linux, `flock` (util-linux) permite adquirir un bloqueo cooperativo. Ejemplo para lanzar manualmente un script que solo debe tener una instancia por usuario:

```bash
flock -n "$HOME/.report.lock" /bin/bash "$HOME/scripts/report.sh"
```

Si otro proceso mantiene el mismo bloqueo, `-n` no espera. No borres arbitrariamente el archivo de bloqueo mientras otros procesos puedan utilizarlo. Este ejemplo supone que la ruta del script y el directorio personal son de confianza.

## NOTAS

Prueba el script manualmente antes de programarlo. Registra errores, evita tareas que requieran entrada interactiva y considera qué ocurre si una ejecución falla o dura más que el intervalo. Para copias de seguridad, comprueba también que se puedan restaurar.
