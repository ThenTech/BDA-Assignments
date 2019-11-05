x = int(input())
sum1 = 0
sum2 = 0


for i in range(x):
    for j in range(i):
        sum1 += j+1
    sum2 += sum1 +i +1
    sum1 = 0

print(sum2)