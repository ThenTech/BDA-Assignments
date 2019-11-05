x = input("Geef een random x-waarde op.")
product1 = 1
sum1 = 0
for i in range(1, int(x)+1):
    for j in range(1, i+1):
        product1 = product1*j
    sum1 = sum1+product1
    product1 = 1
print(sum1)
