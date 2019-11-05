x = input("Geef een x waarde op.")
y = input("Geef een y waarde op.")

sumx = 1
sumy = 1
sumz = 1

for i in range(1, int(x)+1):
    sumx = sumx * i
for j in range(1, int(y)+1):
    sumy = sumy * j

for z in range(1, (int(x)-int(y)+1)):
    sumz = sumz * z

q = ((sumx/(sumy*sumz)))
print(int(q))