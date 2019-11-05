def fibonacci_values(i):
    x = []
    a = 0
    b = 1
    c = 0
    for j in range (0, i):
        x.append(c)
        c = a+b
        a = b
        b = c
        
    return x