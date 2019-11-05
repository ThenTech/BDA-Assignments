def fibonacci_values(i):
    list = [0, 1, 1 ]
    if i == 1:
        list = [0]
    if i == 2:
        list =[0, 1]
    if i == 3:
        list = [0, 1, 1]
    else:
        for i in range(i - 3):
            list.append(list[i + 2] + list[i + 1])
    return list    