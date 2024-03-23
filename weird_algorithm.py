def algoritmo_raro(n):            #Se crea la funcion con el parametro "n"
    contadorN = [n]         #Se crea una variable sencuencia_lista la cual tranforma "n" en un array.
    while n != 1:                 #Se usa el bucle mientras con la condicion de n distinto de 1.
        if n % 2 == 0:            #Condicional, si el resto de n / 2 es 0, es un numero par, entronces se divide por 2.
            n = n // 2
        else:                     #Caso contrario se lo multiplica por 3 y lo suma 1.
            n = 3 * n + 1
        contadorN.append(n)       #El contadorN almacena el nuevo numero en el array. 
    print(contadorN)              #Muestra el resultado por consola.

#algoritmo_raro(3)       
assert algoritmo_raro(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"

