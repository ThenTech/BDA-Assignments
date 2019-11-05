def fibonacci_values(nr):
    fib = []
    for i in range(nr):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[i-1] + fib[i-2])
    return fib
