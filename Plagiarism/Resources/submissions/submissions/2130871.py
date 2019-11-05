getal = int(input("Geef een getal: "))
lijst = list()
for i in range(1,getal+1):
    faculteit = i
    while i > 2:
        i = i - 1
        faculteit = faculteit * i
    lijst.append(faculteit)
print(sum(lijst))