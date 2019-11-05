x = int(input("Geef x:"))
y = int(input("Geef y:"))
getal = 1
for i in range(y):
    for j in range(x):
        print(getal, end=" ")
        getal += 1
    print()