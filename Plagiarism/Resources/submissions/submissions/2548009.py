getal = int(input("Geef een getal: "))
dubbele_som = 0
for i in range(getal):
    for j in range(i+1):
        dubbele_som += j+1
print(dubbele_som)
