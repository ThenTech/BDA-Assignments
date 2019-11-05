x = int(input())

doubleSum = 0

for i in range(1, x+1):
    for j in range(i+1):
        doubleSum += j

print(doubleSum)