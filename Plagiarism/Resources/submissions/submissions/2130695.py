x = int(input("Waarde van x = "))
y = int(input("Waarde van y = "))
z = 0

for i in range(y):
    for j in range(x):
        z = z + 1
        print(z, end=" ")

    print()
