getal = int(input("Geef een getal."))
uitkomst = 0
for j in range(getal):
    for i in range(getal):
        uitkomst = uitkomst + i + 1
    getal = getal-1
print(uitkomst)