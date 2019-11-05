x = int(input("give ma a number: "))
result1 = 0
for i in range(1, x+1):
    result = 1
    for j in range(1, i+1):
        result *= j
    result1 += result

print(result1)