def fibonacci_values(i):
    fib1 = 0
    fib2 = 1
    list = [0, 1]
    for x in range(2, i):
        fib3 = fib1 + fib2
        list.append(fib3)
        fib1 = fib2
        fib2 = fib3
    return list