kolom = input("Hoeveel kolommen wilt u?")
rijen = input("Hoeveel rijen wilt u?")

for r in range(0, int(rijen)):
    for k in range(1, int(kolom)+1):
        print(k+(int(kolom)*r), end=" ")
    print()
    