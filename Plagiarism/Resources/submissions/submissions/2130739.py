getal = int(input("Geef een getal"))
uitkomst = 1
geheel = 0
for j in range(getal):

    for i in range(j+1):
        uitkomst = uitkomst * (i+1)
    geheel = geheel + uitkomst
    uitkomst = 1
print(geheel)