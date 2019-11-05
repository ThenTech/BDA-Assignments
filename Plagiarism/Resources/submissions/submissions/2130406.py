getalx = input("wat is x")
getaly = input("wat is y")

getalx = int(getalx)
getaly = int(getaly)

i= 0
j= 0

tel = 1
bijvoegen = str(tel)


for i in range(getaly):
    printengetal= bijvoegen
    for j in range(getalx):
        printengetal += " " + bijvoegen
        tel += 1
        bijvoegen = str(tel)
        
    print(printengetal)