numero=int(input("numero: "))
filas=int(input("filas: "))


n=1
for i in range(0,filas):
    for j in range(1,numero+1):
        print (n , end=" ")
        n +=1
    print()