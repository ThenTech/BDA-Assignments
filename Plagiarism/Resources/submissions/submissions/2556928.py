def orden(lista):
    if lista == lista.sort():
        return True
    else:
        return False

lista = []
n = int(input("n: "))
for i in range(n):
    i = int(input("element: "))
    lista.append(i)

print(orden(lista))