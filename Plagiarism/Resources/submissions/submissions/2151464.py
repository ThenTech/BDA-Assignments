x = int(input("enter a number"))
fac = 1
sum = 0
for k in range(x):
    for i in range(k+1):
        fac = fac * (i+1)
    sum = sum + fac    
    fac = 1
print(sum)