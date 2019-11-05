# write your code here

x = int(input("Val of x"))
y = int(input("Val of y"))

def fac(a):
    fact = 1
    for i in range(1, a+1):
        fact *= i
    return fact

print( fac(x) // (fac(y) * fac(x - y)))