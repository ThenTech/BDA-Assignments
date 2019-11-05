getal = int(input("Geef een getal: "))
lijst = list()
som = 0
for i in range(1, getal+1):
    som = som + i
    lijst.append(som)
print(sum(lijst))