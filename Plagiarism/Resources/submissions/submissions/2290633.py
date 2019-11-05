def fibonacci_values(i):
    fib = [0,1]
    for x in range(i-2):
        fib.append(fib[x] + fib[x+1])
    return fib