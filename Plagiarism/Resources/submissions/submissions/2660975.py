def fibonacci_values(i):
    fib = [0, 1]
    sum = 0
    for k in range(2, i):
        sum = fib[k-2] + fib[k-1]
        fib.append(sum)
    return fib