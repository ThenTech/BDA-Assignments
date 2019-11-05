x=int(input("x: "))


producto=1

if x > 0:
    for i in range(1, x+1):
        producto = producto *i
    print(producto)

elif x==0:
    print("1")

else:
    print()