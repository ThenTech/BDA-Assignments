number = int(input("Number: "))
result = 1

for i in range(number+1):
    if i != 0:
        result *= i

print(result)