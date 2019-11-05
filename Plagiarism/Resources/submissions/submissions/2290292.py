def fibonacci_values(i):
    list = [0, 1]
    for q in range(2, i):
        sum = list[q-1] + list[q-2]
        list.append(sum)
    return list