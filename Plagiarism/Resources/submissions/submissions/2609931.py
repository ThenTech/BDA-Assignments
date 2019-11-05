def fibonacci_values(i):
    fib=[]
    if n == 0:
        print([0])
    elif n == 1:
        print([1])
    else:
        for i in range(i):
            if i == 0:
                fib.append(0)
            elif i == 1:
                fib.append(1)
            else:
                fib.append(fib[i-1] + fib[i-2])
    return fib