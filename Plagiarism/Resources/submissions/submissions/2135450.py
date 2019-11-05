x = int(input("x = "))
result = 0
for i in range(x):
	for j in range(i+1):
		result += j+1
print(result)