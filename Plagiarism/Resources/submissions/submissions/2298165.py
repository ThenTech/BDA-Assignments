def fibonacci_values(i):
    fib = [0, 1]
    for value in range(2, i):
        formule = fib[value] = fib[value-1] + fib[value -2]
        fib.append(formule)    
    return fib