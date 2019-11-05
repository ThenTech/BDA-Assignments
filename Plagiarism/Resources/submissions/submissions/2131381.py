x = int(input())
sumTot = 0

for i in range(1, x+1):
    for j in range(1, i+1):
        sumTot += j

print(str(sumTot))
