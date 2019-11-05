getal = int(input("Geef een getal: "))
lijst = list()
teller = 0
for i in range(1,getal+1):
    faculteit = i*(i-teller)
    lijst.append(faculteit)
print(sum(lijst))