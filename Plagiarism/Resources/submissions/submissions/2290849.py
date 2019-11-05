def fibonacci_values(xtimes):
    A = []
    a = 0
    b = 1
    for i in range(xtimes):
        A.append(a)
        z = a + b
        a = b
        b = z
    return A
