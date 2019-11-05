x = int(input("Geef een positief getal"))
y = int(input("Geef een positief getal"))
n = 1
for i in range(y):
    n = n * (x - i) / (y - i)
print(n)