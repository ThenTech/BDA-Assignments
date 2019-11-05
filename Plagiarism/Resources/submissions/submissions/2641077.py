def shift(l, n):
    newlist = [" "]*len(l)
    for i in range(len(l)):
        newlist[(i + n) % len(l)] = l[i]
    return newlist