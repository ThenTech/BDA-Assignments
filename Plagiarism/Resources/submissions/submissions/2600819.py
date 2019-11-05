getal = int(input("Geef een getal: "))
b = getal
if b < 0:
    print(0)
else:
    while b >= 1:
        b -=1
        getal += b

    print(getal)