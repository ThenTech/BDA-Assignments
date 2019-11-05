x  =int(input("Geef een getal"))
som_1 = 0
som_2 = 0
for i in range(1, x+1):
    for j in range(1, i+1):
        som_1 = som_1 + j
    som_2 = som_2 + som_1
    som_1 = 0
print(som_2)