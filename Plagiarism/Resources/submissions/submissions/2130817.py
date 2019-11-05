x = int(input())

sum = 0


product = 1

for i in range(x):

	for j in range(i + 1):
		product = product * (j + 1)
	sum = product + sum
	product = 1
print(sum)