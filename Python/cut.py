def reverse_word(str):
    i = len(str) - 1
    reverse = ""
    while i >= 0:
        reverse += str[i]
        i = i - 1
    return reverse


def cut(str,chrt):
    l = []
    word = ""
    
    """
    if str[0] == chrt: #Si el primer caracter es el de cut mejor nos lo saltamos
        str = str[1:]

    if reverse_word(str)[0] == chrt: #Si el ultimo caracter es el de cut entonces nos lo saltamos
        aux = reverse_word(str)
        aux = aux[1:]
        str = reverse_word(aux)
    """

    for letra in str:
        if letra == chrt:
            l.append(word)
            word = ""
        else:
            word += letra
    l.append(word)
    return l
