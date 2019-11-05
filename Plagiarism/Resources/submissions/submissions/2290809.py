def shift(l, n):
    new_list = l[:]
    for i in range(len(l)):
        new_pos = i + n
        new_list[new_pos % len(l)] = l[i]
    return new_list