def caso_base(lista,paso):
    nueva = []
    for i in range(0, len(lista)):
        if i % paso != 0:
            nueva.append(i)
    return(nueva)


def lucky_number(n):
    lista = [i for i in range(1, n+1)]
    paso = 2
    while paso < len(lista):
        lista = caso_base(lista, paso)
        paso +=1
        
    return lista


n = int(input("n: "))

print(lucky_number(n))