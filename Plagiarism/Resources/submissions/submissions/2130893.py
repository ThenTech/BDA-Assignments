getal = int(input("Geef je getal in: "))
som = 0
product = 1

for x in range(1, getal + 1):
    product = product * x
    som = som + product
print(som)