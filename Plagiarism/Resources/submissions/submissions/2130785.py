x = int(input("x = "))
product = 1
sum = 0

if x < 1:
    print("x has to be more than 0")
else:
    for value in range(1, x+1):
        for number in range(1, value+1):
            product = product * number
        sum = sum + product
        product = 1
    print(sum)
