getal1 = int(input("Geef het eerste getal."))
getal2 = int(input("Geef het tweede getal."))
a = 1
for j in range(getal2):
    for i in range(getal1):
        print(i + a, end = " ")
    a = a + getal1
    print()
