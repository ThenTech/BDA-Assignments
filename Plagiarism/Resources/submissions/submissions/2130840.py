x = int(input("x = ?\n"))

sum = 0

for i in range(1, x+1):
    sum2 = 0
    for j in range(1, i+1):
        sum2 += j

    sum += sum2

print(sum)
