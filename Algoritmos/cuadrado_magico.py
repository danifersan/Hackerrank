#! /bin/python3
def posibles_cuadrados():
    cuadrados = []
    c1 = [[8,1,6],[3,5,7],[4,9,2]]; cuadrados.append(c1)
    c2 = [[8,3,4],[1,5,9],[6,7,2]]; cuadrados.append(c2)
    c3 = [[6,7,2],[1,5,9],[8,3,4]]; cuadrados.append(c3)
    c4 = [[4,9,2],[3,5,7],[8,1,6]]; cuadrados.append(c4)
    c5 = [[2,9,4],[7,5,3],[6,1,8]]; cuadrados.append(c5)
    c6 = [[2,7,6],[9,5,1],[4,3,8]]; cuadrados.append(c6)
    c7 = [[4,3,8],[9,5,1],[2,7,6]]; cuadrados.append(c7)
    c8 = [[6,1,8],[7,5,3],[2,9,4]]; cuadrados.append(c8)
    return cuadrados
def magic_square(s):
    n = len(s)
    cuadrados = posibles_cuadrados()
    minimo = 100
    cuadrado_minimo = [[]]
    for cuadrado in cuadrados:
        sumatorio = 0
        for i in range(n):
            for j in range(n):
                sumatorio += abs(s[i][j] - cuadrado[i][j])
        if sumatorio < minimo:
            minimo = sumatorio
            cuadrado_minimo = cuadrado
    return minimo

if __name__== "__main__":
    prueba = [[4,8,2],[4,5,7],[6,1,6]]
    minimo = magic_square(prueba)
    print(minimo)
