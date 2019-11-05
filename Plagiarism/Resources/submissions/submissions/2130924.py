x = int(input())

product = 1
product2 = 1
for i in range(1, x+1):
	fac = 1
	for j in range(1, i + 1):
		fac = j * fac
	result = result + fac
print(result)