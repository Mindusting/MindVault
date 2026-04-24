---
author: Mindusting
corrected: false
headerFile: true
tags:
  - Programming
  - PHP
title: PHP 🐘
---

# PHP

> [!fail]- ESTE APARTADO ESTÁ INCOMPLETO
> > [!todo] #TODO

> [!help]- REFERENCIAS WEB
> YouTube:
> - [MoureDev by Brais Moure](https://youtu.be/nPCJAx5c1uE) #WWW/YT/MoureDevByBraisMoure
> - [PHP (docs)](https://www.php.net/docs.php) #WWW/PHP

- [VARIABLES](php_variable.md)
- [OPERADORES](php_operator.md)
- [CONDICIONALES](php_condition.md)
- [ARRAY](php_array.md)
- [BUCLES](php_loop.md)
- [FUNCIONES](php_func.md)
- [OOP](php_oop.md)
- [FECHAS](php_date.md)
- [RNG](php_rng.md)

## PRIMER PROGRAMA

Para visualizar el archivo de PHP se debe instroducir dentro del directori `htdocs`, dentro del directorio `xmapp` de la instalación del propio **XAMPP**.

Luego desde el buscador de internet escribimos la siguiente URL `http://localhost/[fileName].php`.

> [!important] IMPORTANTE
> 
> Hay que tener el servidor de Apache encendido.

### ARCHIVOS DE PHP

```php
<!DOCTYPE html>
<html lang="es">
<head>
  <title>Mi primer programa en PHP</title>
</head>
<body>
  <!-- Aquí tenemos el código de PHP -->
  <?php
  echo "Hola mundo!";
  ?>
</body>
</html>
```

## FORMULARIOS

Para acceder a los datos de un formulario se hace de la siguiente forma:

**pagina1.php**

```php
<!DOCTYPE html>
<html lang="es">
<head>
  <title>Página de formulario.</title>
</head>
<body>
  <form method="post", action="pagina2.php">
        Ingrese su nombre
        <input type="text" name="name">
    <br>
        <input type="submit" value="Confirmar">
  </form>
  <?php ?>
</body>
</html>
```

**pagina2.php**

```php
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Segunda página página.</title>
</head>
<body>
    <?php
    echo "El nombre ingresado es: ";
    echo $_REQUEST['name'];
    ?>
</body>
</html>
```
