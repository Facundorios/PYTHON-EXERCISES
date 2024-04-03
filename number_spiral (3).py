def espiral_de_numeros(filas, columnas):
    #Condicional para saber si el el parametro de filas es mayor que el de columnas
    if filas > columnas:
    #En caso de ser verdadero usamos

        return (filas - 1) ** 2 + columnas + 1
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

#Hace una funcion que toma como parametros x e y, que sirven para ubicar el numero en el espiral.
def espiral_de_numeros(filas, columnas):
#
    if filas > columnas:
        if filas % 2 == 0:
            return (filas ** 2) - columnas + 1
        else:
            return ( filas - 1 ) ** 2 + columnas
    else:
        if columnas % 2 == 0:
            return ( columnas - 1 ) ** 2 + filas
        else:
            return columnas ** 2 - filas + 1



assert espiral_de_numeros(2, 2) == 3, "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")
