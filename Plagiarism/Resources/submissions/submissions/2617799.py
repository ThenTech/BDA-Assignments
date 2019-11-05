def fibonacci_values(i):
    fib = [0,1]
    if i >= 2:
        for i in range(2,i):
            a = fib[i-1]
            b =fib[i-2]
            c = a + b
            fib.append(c)

    if i == 1:
        print(fib)

    if i == 0:
        print(fib[0])
    return fib