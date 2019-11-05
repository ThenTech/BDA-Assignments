def fibonacci_values(i):
    for value in range(1, len(i)):
        i[value] = i[value - 1] + i[value - 2]