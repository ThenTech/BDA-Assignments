x = int(input(""))
fac = 1
sum = 0


for i in range(1, x + 1):
    fac *= i
    sum += fac

print(sum)