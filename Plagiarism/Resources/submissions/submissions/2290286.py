def fibonacci_values(i):
    fib = [0, 1]
    for j in range(2, int(i)):
        fib = fib.append(fib[j]+fib[j+1])
    return fib