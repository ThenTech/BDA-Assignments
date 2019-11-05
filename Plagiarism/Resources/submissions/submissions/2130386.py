getalx = input("wat is x")
getaly = input("wat is y")

getalx = int(getalx)
getaly = int(getaly)

i= 0
j= 0

tel = 0

for i in range(getaly-1):
    printengetal= ""
    for j in range(getalx-1):
        tel += 1
        bijvoegen = str(tel)
        printengetal += bijvoegen
        
    print(printengetal)