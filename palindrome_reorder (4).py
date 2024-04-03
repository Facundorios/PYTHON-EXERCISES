def ordenador_palindromo(n):
    # Verificar si n es una cadena de texto del alfabeto inglés y no supera 10^6
    if not isinstance(n, str) or len(n) > 10**6:
        return "n no cumple con las condiciones para verificar si es palindromo, o si puede ser uno."
    else:
        contador_letras = {}  # Contar las ocurrencias de cada letra en la cadena
    # Bucle for in para recorrer n y contar las repeticiones de cada letra
    for letra in n:
        contador_letras[letra] = contador_letras.get(letra, 0) + 1

    # creamos una variable para la letra impar
    letra_impar = ""

    palindromo = ""

    # Recorrer contador_letras para saber si hay mas de una letra impar
    for letra, count in contador_letras.items():
        if count % 2 != 0:
            if letra_impar:
                # Si hay más de una letra con frecuencia impar, devolver "NO SOLUTION"
                return "NO SOLUTION"
            else:  # En caso contrario
                # Se guarda la letra con frecuencia impar y se construye la mitad del palíndromo
                letra_impar = letra
        palindromo += letra * (count // 2)
    # Se retorna el palíndromo completo
    return palindromo + letra_impar + palindromo[::-1]


print(ordenador_palindromo("151515515"))

# Caso de prueba
assert ordenador_palindromo("aabbc") == "abcba", "Error en el casode prueba"
print("Todos los casos de prueba han pasado correctamente")
