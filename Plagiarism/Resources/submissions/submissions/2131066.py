x = int(input())
som = 0
for i in range(1,x+1):
    prod = 1
    for j in range(1,x+1):
        prod *= j
    som += prod
print(som)