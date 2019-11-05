x = int(input("number?"))
sum2 = 0
sum1 = 0
for i in range(x + 1):
    for j in range(i):
        sum2 += (j +1)
    sum1 += sum2
    sum2 = 0
print(sum1)