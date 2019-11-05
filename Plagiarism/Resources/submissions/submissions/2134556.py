a = int(input())
sum = 0
product = 0

for x in range(1, a+1):
    product = 1
    for y in range(1, x+1):
        product *= y
    sum += product
    
print(sum)