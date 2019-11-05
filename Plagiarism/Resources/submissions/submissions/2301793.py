def shift(l, n):
    copy = l[:]
    for i in range(len(l)):
        old_i = (i-n) % len(l)
        copy.append(l[old_i])
    return copy