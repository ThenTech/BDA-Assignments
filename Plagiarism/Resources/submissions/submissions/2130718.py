
x = int(input())
y = int(input())

getallen = 0

for i in range(1, x*y+1):
	getallen = getallen + 1
	print(i, end=" ")
	if getallen > 6:
		getallen = 0
		print()