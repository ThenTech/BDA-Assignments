x = int(input("please enter a number"))
sum1 = 0

for i in range(x):
    for k in range(i):
        sum1 += (k+1)
    sum1 += (i+1)
print(sum1)