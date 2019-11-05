def fibonacci_values(i):
    fib = [0, 1]
    if i > 0:
        for n in range(2,i):
            a = fib[n-1]
            b = fib[n-2]
            c = a+b

            fib.append(c)
    print(fib)