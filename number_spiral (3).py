def espiral_de_numeros(x, y):
    # Condicional para saber si el el parametro de filas es mayor que el de columnas
    if x > y:
        # En caso de ser verdadero usamos otro condicional, en donde determinamos el filas es par.
        if x % 2 == 0:
            return (x**2) - y + 1
        # En caso contrario:
        else:
        #Retorna el anterior de filas alcuadrado, más columnas
            return (x - 1) ** 2 + y
    else:
        # Verificamos que x sea columnaas sea par.
        if y % 2 == 0:
            # Devuelva el anterior de columna al cuadrado, sumado el numero filas
            return (y - 1) ** 2 + x
        else:
            # Si columnas es impar, se calcula el cuadrado y selo resta por numero de filas - 1.
            return (y**2) - x + 1


assert espiral_de_numeros(2, 2) == 3, "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")

