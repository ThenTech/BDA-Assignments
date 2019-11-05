def fibonacci_values(i):
    fib = [0, 1]
    for j in range(2, int(i)):
        fib.append(fib[j-2]+fib[j-1])
    return fib