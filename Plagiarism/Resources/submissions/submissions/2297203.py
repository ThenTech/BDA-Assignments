def fibonacci_values(i):
    fib = []
    for m in range(0,i+1):
        if m == 0:
            fib.append(0)
        elif m == 1:
            fib.append(1)
        else:
            fib.append(fib[m-1]+fib[m-2])
    return fib
        