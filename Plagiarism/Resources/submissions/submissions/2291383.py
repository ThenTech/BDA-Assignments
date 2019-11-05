def fibonacci_values(i):
    value = []
    if i == 0:
        return value
    value.append(0)
    if i == 1:
        return value
    value.append(1)
    else:
        for k in range(2, i):
            value.append(value[k - 2] + value[k - 1])
        return value