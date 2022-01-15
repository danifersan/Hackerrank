#! /bin/python3
def to_list(cadena):
    l = []
    for numero in cadena:
        l.append(int(numero))
    return l
def homogeneo(lista):
    homog = True
    for elemento in lista:
        if elemento == lista[0]:
            pass
        elif elemento != lista[0]:
            homog = False
            break
    return homog

def compress_the_string(lista): #Tengo una lista de números como entrada
    salida = [] #del tipo [(int,int)]
    repeticiones = 1
    i = 0

    if homogeneo(lista): #Si la lista es toda de un solo  numero estoy jodido
        salida = [(len(lista),lista[0])]
        return salida

    while i < len(lista) - 1:
        if lista[i] == lista[i+1]:
            repeticiones += 1
            lista.pop(i)

        else:
            par = (repeticiones,lista[i])
            salida.append(par)
            i = i+1
            repeticiones = 1
        
        if i == len(lista) - 1: #En la última iteracción tengo que apendear
            if lista[i] == lista[i-1]:
                repeticiones += 1
                par = (repeticiones,lista[i])
            else:
                par =(repeticiones,lista[i])
            salida.append(par)
    return salida        

def imprimir_bonito(lista):
    imprimir = ""
    for elemento in lista:
        imprimir = imprimir + str(elemento) + " "
    print(imprimir)

if __name__ == "__main__":
    cadena = input()
    cadena = to_list(cadena)
    solucion = compress_the_string(cadena)
    imprimir_bonito(solucion)