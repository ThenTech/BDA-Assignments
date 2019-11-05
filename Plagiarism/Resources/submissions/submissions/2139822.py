getal = input("Getal?")
counter = 0
for i in range(0,len(getal)):
    if int(getal[i]) % 2 == 0:
        counter+=1
    else:
        continue
print(counter)