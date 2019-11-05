x = int(input())

factorial = 1
factiorialSum = 0

for j in range(1, x+1):
    factorial *= j
    factiorialSum += factorial
    factorial = 1
    
print(factiorialSum)