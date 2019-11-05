number = int(input("Number = "))
sum = 0
string = "1"

for value in range(1, number+1):
    sum = sum + value
for value in range(2,number+1):
    string = string + " + " + str(value)

print(string, " = ", sum)