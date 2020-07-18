#objSqlite3
--------

Pequeño conector para base de datos Sqlite3 para ahorra en ciertas tareas reiterativas.

## Importando el objeto:

```python 
from objSqlite import objSqlite
```


## Crear Base de datos y conectarse.
---------------------------------------

Para crear la base de datos o abrirla simplemente instanciamos el objetos:


Directamente aquí al instanciarse se crea o se conecta a la base de datos
ya que la opción *con* esta por defecto en *True*

```python
database = 'basededatos.db'
objLite = objSqlite(database)
```

Si queres que no se conecte simplemente hacemos lo siguiente:

```python
database = 'basededatos.db'
objLite = objSqlite(database, con=False)
objLite.sql_conection()
```

## Crear Tablas.



