def shift(l, n):
    new_l = []
    for i in range(len(l)):
        new_pos = (i + n) % len(l)
        new_l.append(l[new_pos])
    return new_l