x = int(input("Geef een getal x"))
y = int(input("Geef een getal y"))
prod = 1
for i in range(y):
    prod = prod*((x-i)/(y-i))
print(int(prod))