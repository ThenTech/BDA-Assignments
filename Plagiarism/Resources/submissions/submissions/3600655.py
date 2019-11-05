def fibonacci_values(i):
    i -= 2
    fib1 = 0
    fib2 = 1
    list = [0, 1]
    for j in range(i):
        temp = fib2
        fib2 = fib2 + fib1
        fib1 = temp
        list.append(fib2)
    return list