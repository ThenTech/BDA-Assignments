def shift(l, n):
    copy = l[:]
    for i in range(len(l)):
        old.i = (i-n) % len(l)
        copy.append(l[old.i])
    return copy