def shift(lista, n):
    nueva =[]
    for i in range(0, len(lista)):
        viejo_indice_i = (i-n) % len(lista)
        nueva.append(lista[viejo_indice_i])
    return nueva