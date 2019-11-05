getalx = int(input("Getal 1: "))
getaly = int(input("Getal 2: "))

product = 1
for x in range(0,getaly):
    product = product * ((getalx-x)/(getaly-x))
print(int(product))
