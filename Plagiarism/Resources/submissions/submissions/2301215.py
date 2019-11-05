def shift(l, n):
    if n > 0:
        l.insert(0, len(l) - 1)
        del l[len(l)-n]
        l.insert(1, (len(l)))
        del l[len(l)-1]
        return l

    elif n == 0:
        return l

    elif n < 0:
        return l


print(shift([1, 2, 3, 4, 5], 0))
