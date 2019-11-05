x = int(input())
y = int(input())

formule = 1

for i in range(y):
	formule = formule * ((x-i)/(y-i))
	
print(int(formule))
