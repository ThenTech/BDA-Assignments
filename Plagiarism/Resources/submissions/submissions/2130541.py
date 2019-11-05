getal1 = int(input("getal 1:"))
getal2 = int(input("getal 2:"))
maal = getal1 * getal2
rij = 0
for k in range(getal2):
    for l in range(getal1):
        print((l+1+rij), end=" ")
    rij = rij + getal1
    print()