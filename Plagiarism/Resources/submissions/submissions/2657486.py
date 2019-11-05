def shift(l, n):
    new_l = l[:]
    for i in range(len(l)):
        new_pos = (i + n) % len(l)
        new_l[new_pos] = l[i]
    return new_l