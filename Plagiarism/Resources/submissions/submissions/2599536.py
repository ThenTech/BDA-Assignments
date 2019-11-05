x = int(input("x"))
sum = 0
sum2 = 0

for j in range(x+1):
    sum = 0
    for i in range(j+1):
        sum += i
    sum2 += sum
print(sum2)