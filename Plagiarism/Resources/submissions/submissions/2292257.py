def fibonacci_values(i):
    fib_result = [0, 1]
    a = 0
    for j in range(2, i):
        fib_new = fib_result[(j-2)] + fib_result[j-1]
        fib_result.append(fib_new)
    return fib_result