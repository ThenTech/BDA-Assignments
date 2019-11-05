def fibonacci_values(i):
    fib = [0, 1]

    for x in range(2, i):
        fib.append(fib[x - 1] + fib[x - 2])
    return fib


print(fibonacci_values(7))
