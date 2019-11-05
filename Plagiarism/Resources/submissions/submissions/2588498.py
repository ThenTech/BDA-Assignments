def fibonacci_values(i):
    fib = [0,1]
    if i == 1:
        return [0]
    elif i == 2:
        return [0, 1]
    else:
        for k in range(2,i)
            fib.append(fib[k - 1] + fib[k - 1])
    return fib