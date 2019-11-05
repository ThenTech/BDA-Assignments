def fibonacci_values(i):
    fib1 = 0
    fib2 = 1
    list = []
    for x in range(2, i):
        fib3 = fib1 + fib2
        list.apprehend(fib3)
        print(fib3)
        fib1 = fib2
        fib2 = fib3
