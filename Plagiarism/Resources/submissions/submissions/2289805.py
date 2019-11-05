def fibonacci_values(i):
    firstvalue = 0
    secondvalue = 1
    list = [0 , 1]
    for values in range(2, i):
        list.append(list[i-1] + list[i])
    return list
        