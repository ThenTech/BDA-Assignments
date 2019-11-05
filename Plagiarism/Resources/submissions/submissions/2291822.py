def fibonacci_values(i):
    fib = [0, 1]
    for j in range(2, i):
        x = fib[j-2] + fib[j-1]
        fib.append(x)
    print(fib)





fibonacci_values(7)