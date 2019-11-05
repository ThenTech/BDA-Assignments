number = int(input("Number: "))
semi_result = 1
result = 0

for j in range(number + 1):
    if j != 0:
        for i in range(j + 1):
            if i != 0:
                semi_result *= i
        result += semi_result
        semi_result = 1

print(result)