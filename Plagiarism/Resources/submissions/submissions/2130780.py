getalx = input("wat is x")
getalx = int(getalx)
i=1
tussenuitkomst = 1
hulpgetal = 1
uitkomst = 0
for j in range (getalx):
    for k in range (hulpgetal):
        tussenuitkomst *= i
        i += 1
    i=1
    tussenuitkomst = 1
    uitkomst += tussenuitkomst
    hulpgetal += 1
print (uitkomst)