def fibonacci_values(i):
    list = [1,1]
    for i in range(i-2):
        list += (list[i]+list[i+1])
    return list