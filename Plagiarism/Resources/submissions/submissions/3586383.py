x = int(input())

factorial = 1
factiorialSum = 0

for i in range(x):
    for j in range(1, x+1):
        factorial *= j
    factiorialSum += factorial
    
print(factiorialSum)