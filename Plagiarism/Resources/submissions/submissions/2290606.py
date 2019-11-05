def fibonacci_values(i):
    count = 2
    fib_list = [0, 1]
    while count < i:
        fib_list.append(fib_list[count-1] + fib_list[count-2])
        count += 1
    return fib_list