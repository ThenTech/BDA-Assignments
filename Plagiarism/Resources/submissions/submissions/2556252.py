getal_x = int(input("Geef x: "))
getal_y = int(input("Geef y: "))
binomiaal = 1
for i in range(getal_y):
    binomiaal *= (getal_x-i)/(getal_y-i)
print(int(binomiaal))