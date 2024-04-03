# Hace una funcion que toma como parametros x e y, que sirven para ubicar el numero en el espiral.
def espiral_de_numeros(x, y):
    # Condicional para saber si el el parametro de filas es mayor que el de columnas

    if x > y:

        # Condicional para saber si  "filas" son par
        if x % 2 == 0:
            # En caso de ser verdadero, devuelve el cuadrado de "filas", menos "el siguiente" de columnas
            return (x**2) - y + 1
        # En caso contrario:
        else:
            # Retorna el anterior de "filas" al cuadrado, más "columnas"

            return (x - 1) ** 2 + y
    # Caso en que las filas sean menor que las columnas:
    else:
        # Verifica de que las columnas sean par.
        if y % 2 == 0:
            # En caso de ser verdadero, devuelve el anterior de "columnas" al cuadrado, sumado "filas"
            return (y - 1) ** 2 + x
        else:
            # En caso de ser falso, retorna "columnas" al cuadrado menos el siguiente de "filas".
            return (y**2) - x + 1


assert espiral_de_numeros(5, 2) == 3, "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")
