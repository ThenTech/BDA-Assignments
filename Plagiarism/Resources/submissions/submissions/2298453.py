def fibonacci_values(i):
    fib = [0, 1]
    for value in range(3, i):
        fib.append(fib[value-1] +fib[value -2])    
    return fib