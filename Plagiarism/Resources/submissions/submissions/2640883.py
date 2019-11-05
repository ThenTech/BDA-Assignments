def fibonacci_values(i):
    fib = [0, 1]
    for k in range(3, i + 1):
        fib.append(fib[k - 1] + fib[k - 2])
    return fib