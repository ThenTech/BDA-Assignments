getalX = int(input("Geef een getal groter dan 0: "))
getalY = int(input("Geef een tweede getal groter dan 0: "))

product = getalX * getalY
count = product

for y in range(getalY):
    for x in range(getalX):
        count -= 1
        print((product - count), end=" ")
    print()
