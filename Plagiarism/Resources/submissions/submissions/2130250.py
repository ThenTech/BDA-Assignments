x = int(input("number?"))
fac = 0
sum1 = 0
for j in range(x + 1):
    for i in range(j):
        fac = fac * (i + 1)
    sum1 += fac
    fac = 1
print(sum1)