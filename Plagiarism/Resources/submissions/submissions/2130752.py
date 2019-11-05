getalx = input("wat is x")
getalx = int(getalx)
i=1
uitkomst = 1
for j in range (getalx):
    uitkomst *= i
    i += 1
print (uitkomst)