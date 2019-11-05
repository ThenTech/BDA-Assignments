import math
x = int(input())
y = int(input())
if y == x:
    print(1)
elif y == 1: 
    print(x)
elif y > x:  
    print(0)
else:  
    a = math.factorial(x)
    b = math.factorial(y)
    c = math.factorial(x-y)
    div = a // (b * c)
    print(div)