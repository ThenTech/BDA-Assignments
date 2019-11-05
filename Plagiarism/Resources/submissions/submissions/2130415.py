getalx = input("wat is x")
getaly = input("wat is y")

getalx = int(getalx)
getaly = int(getaly)

i= 0
j= 0

tel = 1
bijvoegen = str(tel)


for i in range(getaly):
    tel += 1
    bijvoegen = str(tel)
    printengetal= bijvoegen
    
    for j in range(getalx):
        tel += 1
        bijvoegen = str(tel)
        printengetal += " " + bijvoegen
        
        
    print(printengetal)