def shift(listy, n):
    if listy == []:
        return listy
    while n > len(listy):
        n = n - len(listy)
    while n < 0:
        n = n + len(listy)
    new_listy = listy[:]
    for i in range(len(listy)):
        if i+n > len(listy)-1:
            n = n - len(listy)
        new_listy[i+n] = listy[i]
    return new_listy

print(shift([], 2))