def fibonacci_values(n):
    list = [0, 1]
    for i in range(n-2):
        som = list[i] + list[i + 1]
        list.append(som)
    return list
