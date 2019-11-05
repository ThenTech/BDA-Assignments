getal1 = int(input("Geef een getal: "))
getal2 = int(input("Geef nog een getal: "))
teller=1
for x in range(getal2):
    for i in range(getal1):
        print(teller, " ", end=(""))
        teller=teller+1
    print()