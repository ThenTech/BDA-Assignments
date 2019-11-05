def shift(ls, n):
    new_list = ls[:]
    for i in range(len(ls)):
        new_list[(i + n) % len(ls)] = ls[i]
    return new_list