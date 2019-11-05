def fibonacci_values(i):
    fib_list = [0, 1 , 1]
    
    j = 1
    
    while j < i - 2:
        fib_list.append(fib_list[j] + fib_list[j+1])
        j += 1
    return fib_list