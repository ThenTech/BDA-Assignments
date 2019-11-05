x = int(input())
sum1 = 0
sum2 = 0

for i in range(x + 1):
    for j in range(i + 1):
	    sum1 = sum1 + j
    sum2 = sum2 + sum1
	sum1 = 0

print(sum2)