def orden(lista):
    return lista == lista.sort()

lista = []
n = int(input("n: "))
for i in range(n):
    i = int(input("element: "))
    lista.append(i)

print(orden(lista))