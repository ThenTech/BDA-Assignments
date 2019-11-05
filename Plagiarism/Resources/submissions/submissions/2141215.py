def factorial(x):
    producto = 1

    if x > 0:
        for i in range(1, x + 1):
            producto = producto * i
        return producto

    elif x==0:
        return "1"

def sumade(x):
    suma=0
    for i in x:
        suma= suma+i

    return suma

x=int(input("x: "))
suma=0
for i in range (1, x+1):
    lista=(factorial(i))


    suma = suma+lista
print(suma)

