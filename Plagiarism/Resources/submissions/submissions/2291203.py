def fibonacci_values(i):
    fib = [" "]*i
    fib[0] = 0
    fib[1] = 1
    for j in range(2,i):
        fib[j] = fib[j-1] + fib[j-2]
    return fib