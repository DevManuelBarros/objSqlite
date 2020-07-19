from objSqlite import objSqlite


if __name__ == "__main__":
    #Conectamos con la base de datos.
    
    db = 'data.db'
    objLite = objSqlite(db)
    
    # Creamos las tablas:
    tablas = {'paises'    : 'id ip, nombre tu, poblacion i',
              'provincia' : 'id ip, nombre tu, pais i, poblacion i'}

    objLite.create_table(tablas)
    
    # Vamos a insertar valores en la tabla.
    tabla = 'paises'
    name = ['Argentina', 'Brazil', 'Alemania', 'Nicaragua']
    poblacion = [543232, 32323112, 321321, 123123123]
    for i, nombre in enumerate(name):
        values = {'nombre' : nombre,
                  'poblacion' : poblacion[i]
                 }
        print(objLite.insert(tabla, values))

    # Vamos a mostrar los datos guardados.
    result = objLite.selectAll(tabla)
    for val in result:
        print('el resultado es: {}'.format(val))

    # Vamos a borrar un registro
    print(objLite.delete(tabla, 3))

    # Vamos a volver a mostrar todos los resultados
    result = objLite.selectAll(tabla)
    for val in result:
        print(val)
    
    
    # Actualizar un valor:
    values = {'poblacion' : 999999}
    print(objLite.update(tabla, values, cond='nombre=\'Argentina\''))
    objLite.close()


