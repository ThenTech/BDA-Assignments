def fibonacci_values(i):
    lista=[0,1]
    while len(lista) < i:
        l=len(lista)
        lista.append(lista[l-1] + lista[l-2])
    return lista