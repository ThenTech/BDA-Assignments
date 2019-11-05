numberX = int(input())
result = 0
for i in range(1, numberX+1):
    prodX = 1
    for y in range(1, i+1):
        prodX *= y
    result += prodX
print(result)
