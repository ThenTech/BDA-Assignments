number = input("enter a number: ")
even = 0
for i in range(len(number)):
	if (int(number[i])%2) ==0:
		even +=1
print(even)
