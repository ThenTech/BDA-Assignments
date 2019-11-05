def shift(l, n):
    shifted_list = list(range(len(l)))
    for i in range(len(l)):
        shifted_list[(i+n) % len(l)] = l[i]
    return shifted_list