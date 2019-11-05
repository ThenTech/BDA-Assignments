def fibonacci_values(i):
    value = []
    if i == 0:
        return value
    value.append(0)
    if i == 1:
        return value
    else:
        value.append(1)
        for k in range(2, i):
            value.append(value[k - 2] + value[k - 1])
        return value