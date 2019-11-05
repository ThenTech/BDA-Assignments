getal = int(input("Geef een getal: "))
lijst = list()
som = 1
for i in range(2, getal+1):
    som = som + i
    lijst.append(som)
print(sum(lijst))