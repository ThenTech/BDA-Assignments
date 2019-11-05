def fibonacci_values(i):
    li = [0, 1]
    for i in range(2, i):
        li.append(li[i-2] + li[i-1])
    return li
