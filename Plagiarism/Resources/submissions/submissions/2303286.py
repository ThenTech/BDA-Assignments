def fibonacci_values(n):
    counter = 2
    l = [0, 1]
    for i in range(n - 2):
        l.append(l[counter - 1] + l[counter - 2])
        counter += 1
    return l