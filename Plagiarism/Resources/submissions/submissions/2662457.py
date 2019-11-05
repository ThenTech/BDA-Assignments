# write your code here

x = int(input("number"))
som = 0

for i in range(1, (x + 1)):
    factorial = 1
    for j in range(1, (i + 1)):
        factorial = factorial * j
    som = som + factorial
print(int(som))