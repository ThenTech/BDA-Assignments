def fibonacci_values(i):
    fib_list = [0, 1]
    for index in range(2, i):
        fib_list.append(fib_list[index-1] + fib_list[index-2])
    return fib_list