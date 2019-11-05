x = input("X = ")
x = int(x)
output = 0
for j in range(x):
    factorial = 1
    for i in range(j+1):
        factorial *= i+1
    output += factorial
output = int(output)
print(output)