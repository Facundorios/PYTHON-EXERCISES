          #Funcion creada con parametros n y numeros
def numero_perdido(n, arreglo):      

           #Fomula para sacar el total de la suma del arreglo completo en base a la cantidad de elementos del arreglo.
     
    arreglo_completo = (n * (n + 1) // 2) 

          #Suma de todos los numeros que se pasan en el segundo parametro, es decir, el arreglo incompleto.
    
    suma_del_arreglo = sum(arreglo)

           #La resta entre el total de la suma de los elementos del array y la suma de todos los elementos del array incompleto dan como resultado el numero que falta en el arreglo. A esto se le llama la formula de la suma de los primeros " n " numeros naturales. 

    return(arreglo_completo - suma_del_arreglo)
    
assert numero_perdido(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
print("Todos los casos de prueba han pasado correctamente")
