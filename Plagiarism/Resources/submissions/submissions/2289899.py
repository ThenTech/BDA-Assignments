def fibonacci_values(i):
    firstvalue = 0
    secondvalue = 1
    list = [0 , 1]
    for values in range(2, i):
        list.append(list[values-2] + list[values-1])
    return list
        