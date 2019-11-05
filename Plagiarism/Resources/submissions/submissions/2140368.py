x=int(input("x: "))
y=int(input("y: "))

producto=1

if x>0 and y>0:
    for t in range(1,(y+1)):
        producto=producto*((x-t)+1)/(y-t+1)
    print(int(producto))

else:
    print()