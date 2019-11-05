x = int(input())

sum01 = 0
sum_sum = 0
result = 0

for i in range(1, x+1):
	sum01 = sum01 + i
	sum_sum = sum01 + sum_sum

print(sum_sum)
