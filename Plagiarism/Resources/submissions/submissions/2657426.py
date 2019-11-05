def fibonacci_values(i):
    first = 0
    second = 1
    string = [0, 1]
    for i in range(i-2):
        first += second
        second =first
        string += [first]
    return string