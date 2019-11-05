x = int(input("X="))
som = 0
product = 1
for m in range(x):
    product = product * (m+1)
    som = som + product
print(som)