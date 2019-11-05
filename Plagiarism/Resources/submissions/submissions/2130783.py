num1 = input("X = ")
num1 = int(num1)
num2 = input("Y = ")
num2 = int(num2)
output = 0
for i in range(num2):
    for j in range(num1):
        output += 1
        print(output, end=" ")
    print()