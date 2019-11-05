def lucky_number(n):
    lista = [i for i in range(1, n+1)]
    paso = 2
    while paso < len(lista):
        lista = [i for i in range(1, len(lista)) if i%paso != 0]
        paso += 1
    return lista

n = int(input(" valor de n: "))
print(lucky_number(n))