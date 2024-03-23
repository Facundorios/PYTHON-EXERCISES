
n = int
contador = [n]

def algoritmo_rarote(n):         # Comenzamos definiendo la funcion, pasandole como parametro "n".

    while ( n != 1 ):            #Usamos el bucle "mientras" donde condicionamos que n sea distinto de 1.
      contador.append(n)  
    if ( n % 2 != 0 ):       #Condicional, si n divido 2 es distinto de 0, quiere decir que es impar
            n = (n * 3) + 1      #Por lo que n se multiplica por 3 y se la suma  1.
    else:                    # En caso de que no sea así, se lo divide por 2.
            n //= 2             
    contador.append(1)       #Se añade el numero 1 al final del arreglo.


algoritmo_rarote(3)
