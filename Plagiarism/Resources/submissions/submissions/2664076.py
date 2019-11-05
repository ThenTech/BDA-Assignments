def shift(l,n):
    copy = []
    for i in range(len(l)):
        old_i = (i-n) % len(l)
        copy.append(list[old_i])
    return copy