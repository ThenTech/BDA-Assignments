def shift(l, n):
    copy = []
    for i in range(len(list)):
        old_i = (i-n) % len(list)
        copy.append(l[old_i])
    return copy
        