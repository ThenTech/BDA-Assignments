def fibonacci_values(i):
    list = [0, 1, 1 ]
    for i in range(i - 3):
        list.append(list[i + 2] + list[i + 1])
    return list    