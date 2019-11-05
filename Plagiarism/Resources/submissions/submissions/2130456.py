x = int(input())

total = 0

for X in range(1,x+1):
    fac = 1
    for i in range(1,X+1):
        fac *= i
    total += fac

print(total)