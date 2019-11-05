def fibonacci_values(i):
    fibl = []
    for j in range(0, i):
        if j == 0:
            fibl.append(0)
        elif j == 1:
            fibl.append(1)
        else:
            fibl.append(fibl[j - 1] + fibl[j - 2])
    return fibl