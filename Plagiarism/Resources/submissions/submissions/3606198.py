def fibonacci_values(i):
    fib_list = [0, 1 , 1]
    
    j = 1
    if i == 1:
        return [0]
    if i == 2:
        return [0 , 1]
    else:
        while j < i - 2:
            fib_list.append(fib_list[j] + fib_list[j+1])
            j += 1
    return fib_list