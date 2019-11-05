def fibonacci_values(i):
    lis = []
    val1 = 0
    val2 = 1
    for i in range(0, i):
        lis.append(val1+val2)
        keep = val1
        val1 = val2
        val2 = keep + val2
    return lis