# write your code here

x = int(input("Value x: "))

sum = 0

for i in range(x):
    i = i + 1
    product = 1
    for y in range(i):
        product = product * (y)
    sum = sum + product