getal1 = int(input("Geef een eerste getal"))
getal2 = int(input("Geef een tweede getal"))
a = 1
for i in range(getal2):
    a = a * (getal1/getal2)
    getal1 -= 1
    getal2 -= 1
print(int(a))