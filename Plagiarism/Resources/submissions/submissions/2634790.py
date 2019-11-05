x = int(input(""))

def factorial(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

sum = 0
for i in range(1, x + 1):
    sum += factorial(i)

print(sum)
    
        