def fibonacci_values(i):
    fib = 0
    list= [0, 1]
    for value in range(2, i):
        fib = list[value-1] + list[value-2]
        list.append(fib)
    return fib