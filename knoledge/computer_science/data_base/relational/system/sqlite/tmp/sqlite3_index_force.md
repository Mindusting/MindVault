---
tags:
  - Programming
  - SQL/SQLite
---

# Force Index in SQLite

> [!help]- REFERENCIAS WEB
> 
> - [SQLite](https://sqlite.org/lang_indexedby.html)

En SQLite, puedes forzar el uso de un índice específico en una consulta utilizando la cláusula **`INDEXED BY`** en una sentencia `SELECT`, `UPDATE` o `DELETE`. Esta cláusula obliga al planificador de consultas a utilizar un índice nombrado, y si el índice especificado no existe o no puede usarse para la consulta, la preparación de la sentencia fallará.

**Sintaxis:**
```sql
SELECT columnas FROM tabla INDEXED BY nombre_indice WHERE condiciones;
```

**Ejemplo:**
```sql
CREATE INDEX idx_department_id ON employees (department_id);
SELECT name FROM employees INDEXED BY idx_department_id WHERE department_id = 5;
```
Este comando fuerza el uso del índice `idx_department_id`, evitando que SQLite elija otro índice, incluso si otro podría ser más eficiente.

**Consideraciones importantes:**
- **`INDEXED BY` no es una sugerencia**: Es una exigencia. Si el índice no se puede usar, la consulta fallará.
- **No se recomienda en producción**: Según la documentación oficial, `INDEXED BY` debe usarse solo al final del proceso de desarrollo, como una medida de seguridad para detectar cambios no deseados en el plan de ejecución durante pruebas de regresión.
- **Alternativas recomendadas**: Para controlar el uso de índices sin forzarlos, considera:
  - Usar el operador unario `+` para descalificar términos del `WHERE` de los índices.
  - Ejecutar `ANALYZE` para actualizar estadísticas del planificador.
  - Usar `EXPLAIN QUERY PLAN` para analizar cómo se está ejecutando la consulta.

**Cláusula `NOT INDEXED`:**
Para forzar una escaneo completo de la tabla (evitando cualquier índice), usa:
```sql
SELECT name FROM employees NOT INDEXED WHERE department_id = 5;
```

Esta cláusula es útil para pruebas de rendimiento o cuando se sabe que una búsqueda completa es más eficiente.