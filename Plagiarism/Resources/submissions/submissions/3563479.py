def fibonacci_values(i):

    fib = []

    for j in range(i):
        if j == 0 or j == 1:
            fib += [j]
        else:
            next_number = [fib[j - 1] + fib[j - 2]]
            fib += next_number
    return fib