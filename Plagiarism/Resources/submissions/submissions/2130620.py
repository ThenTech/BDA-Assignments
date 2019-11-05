x = int(input("geef getal"))
y = int(input("geef getal"))
resultaat = 1
for i in range(0,y):
    resultaat = resultaat*((x-i)(y-i))
resultaat = resultaat//1
print(resultaat)