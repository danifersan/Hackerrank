#! /bin/python3


if __name__ == "__main__":
    n = int(input())
    palabras = []
    iguales = 0
    
    for i in range(n):
        palabra_input = input()
        if palabra_input in palabras:
            iguales += 1
        palabras.append(palabra_input)
    
    contador = []

    while palabras != []:
        word = palabras[0]
        palabras.pop(0)
        j = 1
        i = 0
        while i < len(palabras):
            if palabras[i] == word:
                palabras.pop(i)
                j += 1
            else:
                i = i+1
        contador.append(j)
    
    output = ""
    for numero in contador:
        output += (str(numero) + " ")
    print(n - iguales)
    print(output)