def shift(l, n):
    copy = l[:]
    for i in range(len(l)):
        copy[(i + n)%len(l)] = l[i]
    return copy