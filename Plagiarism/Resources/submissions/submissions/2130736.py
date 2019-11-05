x = int(input("Geef aantal kolommen"))
y = int(input("Geef aantal rijen"))
for j in range(y):
    for i in range(x):
        print((i + 1) + (j * x), " ", end="")
    print()
