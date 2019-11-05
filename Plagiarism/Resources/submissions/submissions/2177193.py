x = int(input("Give x: "))
y = int(input("Give y: "))
for i in range(0, y):
    for j in range(1, x + 1):
        print(i * x + j, end=" ")
    print()
