def shift(l, n):
    while n > len(l):
        n -= len(l)
    while n < (len(l)*(-1)):
        n += len(l)
    l.rotate(n)
    return l