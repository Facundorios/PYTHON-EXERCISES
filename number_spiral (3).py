def espiral_de_numeros(filas, columnas):
    #Condicional para saber si el el parametro de filas es mayor que el de columnas
    if filas > columnas:
    #En caso de ser verdadero, calculamos el cuadrado del anterior numero de filas, y le sumamos el numero de las columnas.
        return (filas - 1) ** 2 + columnas
    #En caso contrario:
    else:
        #Verificamos que x sea columnaas sea par.
        if columnas % 2 == 0:
        #Devuelva el anterior de columna al cuadrado, sumado el numero filas
            return (columnas - 1) ** 2 + filas
        else:
        #Si columnas es impar, se calcula el cuadrado y selo resta por numero de filas - 1
            return (columnas **  2) - filas + 1
    
print(espiral_de_numeros(4,4))
# assert espiral_de_numeros(2, 2) == 3, "Error en el caso de prueba"
# print("Todos los casos de prueba han pasado correctamente")
