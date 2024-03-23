        #Se crea la funcion con el parametro "n"
def algoritmo_raro(n): 
    
        #Se crea una variable sencuencia_lista la cual tranforma "n" en un array.
    contadorN = [n]             
    
        #Se usa el bucle mientras con la condicion de n distinto de 1.
    while n != 1:               
        
        #Condicional, si el resto de n / 2 es 0, es un numero par, entronces se divide por 2.
        if n % 2 == 0:            
            n = n // 2
        #Caso contrario se lo multiplica por 3 y lo suma 1.
        else:                    
            n = 3 * n + 1
        #El contadorN almacena el nuevo numero en el array. 
        contadorN.append(n)       
        #Retorna el resultado por consola.
    return contadorN              

assert algoritmo_raro(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")

