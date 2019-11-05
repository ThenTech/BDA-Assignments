x = int(input())
sum1 = 0
sum2 = 0
for i in range(1, x + 1):
    sum1 = 0
    for j in range(1, i + 1):
        sum1 += j
    sum2 += sum1
print(sum2)