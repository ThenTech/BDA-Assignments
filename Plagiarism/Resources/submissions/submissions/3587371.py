def fibonacci_values(i):
    if i == 1:
        list = [0]
        return list
    elif i == 2:
        list = [0, 1]
        return list
    else:
        list = [0, 1, 1]
        for j in range(2, i):
            list.append(list[j-1] + list[j-2])
        return list