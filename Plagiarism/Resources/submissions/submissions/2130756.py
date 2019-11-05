x = int(input("x = "))
product = 1

if x < 1:
    print("x has to be more than 0")
else:
    for value in range(1,x+1):
        product = product * value

    print(product)