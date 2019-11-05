def fibonacci_values(i):
    fib_list = [0, 1 , 1]
    
    j = 1
    
    while j < i - 2:
        fib_list.append(fib_list[i] + fib_list[i+1])
        i += 1
    return fib_list