def shift(listy, n):
    if n < 0:
        n = len(listy) + n
    new_list = listy[:]
    a = 0
    for j in range(n):
        for i in range(len(listy)):
            new_list[i] = listy[i-1-a]
        a = a + 1