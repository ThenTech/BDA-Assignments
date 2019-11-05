def fibonacci_values(i):
    result = [0]
    if i > 1:
        result.append(1)
    if i > 2:
        for n in range(2,i):
            new = result[i-2]+result[i-1]
            result.append(new)
    return result
