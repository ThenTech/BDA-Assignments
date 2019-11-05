# write your code here

x = int(input("number"))
som = 0
factorial = 1
for i in range(1, (x + 1)):
    for j in range(i):
        factorial = factorial * j
    som = som + factorial