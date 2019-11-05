def fact(inp):
    result = 1
    for i in range(1, inp+1):
        result *= i
    return result
x = int(input("x? "))
y = int(input("y? "))
x_fac = fact(x)
y_fac = fact(y)
xy_fac = fact(x-y)
result = x_fac/(y_fac*xy_fac)
print(int(result))