def fibonacci_values(i):
    result = [0]
    if i > 1:
        result.append(1)
    if i > 2:
        for n in range(2,i):
            new = result[n-2]+result[n-1]
            result.append(new)
    return result
