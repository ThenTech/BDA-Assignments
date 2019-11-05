getal1 = int(input("Geef een getal: "))
getal2 = int(input("Geef nog een getal: "))
lijst = list()
product = 1
for i in range(getal2-1):
    lijst.append(((getal1-i)/(getal2-i)))
for x in lijst:
    product = x*product
print(product)
