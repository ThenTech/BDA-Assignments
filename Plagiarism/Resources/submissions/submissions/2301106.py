def shift(l, n):
    l.insert(0, len(l) - 1)
    del l[len(l)-1]
    l.insert(1, (len(l)))
    del l[len(l)-1]
    return l


print(shift([1, 2, 3, 4, 5], 2))
