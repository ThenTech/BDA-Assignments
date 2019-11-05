n = int(input("Geef een getal n: "))
sum = 0
prod = 1
for i in range(1,n+1):
    prod = 1
    for j in range(1,i+1):
        prod = prod*j
    sum = sum + prod
print(sum)