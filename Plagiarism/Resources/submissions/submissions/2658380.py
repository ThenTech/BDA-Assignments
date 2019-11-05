def fibonacci_values(i):
    fib_list = [0,1]
    a = 0
    b = 1
    if i == 0:
        return [0]
    elif i == 1:
        return [0,1]
    else:
        i = i - 2
        for j in range(i):
            x = fib_list[len(fib_list)-1] + fib_list[len(fib_list)-2]
            fib_list.append(x)
    return fib_list
    
    