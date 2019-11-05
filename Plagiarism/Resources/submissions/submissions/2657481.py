def shift(l, n):
    new_l = l[:]
    for i in range(len(l)):
        new_pos = (i + n) % len(l)
        new_l[i] = l[new_pos]
    return new_l