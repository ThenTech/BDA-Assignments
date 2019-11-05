def shift(l, n):
    l2 = l[:]
    for i in range(0, len(l)):
        l2[i] = l[(i + n + 1) % len(l)]
    return l2